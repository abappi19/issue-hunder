from functools import lru_cache

import requests

from api.errors import FetchError, check_rate_limited
from config.github import API, HEADERS
from constants import RECENT_COUNT
from utils.sanitize import sanitize_text


@lru_cache(maxsize=None)
def fetch_unassigned_summary(repo):
    """Unassigned open issues for a repo -- the count and the issues
    themselves -- from a single call to the regular issues endpoint (core
    limit), never the Search API.

    One call serves both: the count written to the summary table is derived
    from the very page listed on the repo's own page, so asking for the
    detail and asking for the number are never two separate requests.

    Cached per run because the repo lists overlap -- a repo in both
    top_repos.json and top_typescript.json would otherwise be fetched once
    per list. The result is treated as read-only by callers, since repeat
    calls hand back the same object.

    Two things about that endpoint shape the result:

    - It returns pull requests alongside issues -- GitHub models every PR as
      an issue -- so PRs are dropped here. Without that, the count would
      disagree with the `is:issue no:assignee` link shown next to it, badly
      so on repos with heavy PR traffic.
    - It paginates by opaque cursor regardless of result size, so the Link
      header never carries a last-page number to read a total off. Instead
      one page of RECENT_COUNT is fetched: a short page is the complete set
      (exact count), a full page means there are more, reported as "<n>+".

    The same page serves both the count and the listing, so everything
    fetched is everything shown."""
    resp = requests.get(
        f"{API}/repos/{repo}/issues",
        headers=HEADERS,
        params={"state": "open", "assignee": "none", "per_page": RECENT_COUNT},
        timeout=30,
    )
    check_rate_limited(repo, resp)
    if resp.status_code != 200:
        raise FetchError(f"{repo}: {resp.status_code} {resp.text[:200]}")

    page = resp.json()
    issues = [item for item in page if "pull_request" not in item]
    total_count = f"{len(issues)}+" if len(page) == RECENT_COUNT else len(issues)

    recent = [
        {
            "number": item["number"],
            "title": sanitize_text(item["title"]),
            "url": item["html_url"],
            "comments": item["comments"],
        }
        for item in issues
    ]
    return {"total_count": total_count, "recent": recent}
