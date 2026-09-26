import re

import requests

from api.search_rate_limiter import SEARCH_LIMITER
from config.github import API, HEADERS
from utils.sanitize import sanitize_text

RECENT_COUNT = 5

# The Search API's secondary rate limit reacts to request *pattern*
# (bursty/rapid-fire calls), not just raw volume -- it applies regardless
# of credential type, so it's avoided by not using this endpoint at all
# for the common case (see fetch_unassigned_summary). SEARCH_LIMITER only
# paces the rare large-repo fallback calls, shared with every other module
# that touches the Search API.


class FetchError(Exception):
    pass


def _get_issues(repo, per_page):
    resp = requests.get(
        f"{API}/repos/{repo}/issues",
        headers=HEADERS,
        params={"state": "open", "assignee": "none", "per_page": per_page},
        timeout=30,
    )
    if resp.status_code != 200:
        raise FetchError(f"{repo}: {resp.status_code} {resp.text[:200]}")
    return resp


def _exact_count(repo):
    """Exact unassigned-issue count via the regular (core-rate-limited)
    issues endpoint, reading the last-page number off the Link header
    (per_page=1, so last page number == total count). Returns None if the
    repo has 1000+ results, where GitHub switches to cursor-based
    pagination with no computable last page."""
    resp = _get_issues(repo, per_page=1)
    if not resp.links:
        return len(resp.json())  # 0 or 1 result: fits on a single page
    last_url = resp.links.get("last", {}).get("url")
    if last_url:
        match = re.search(r"[?&]page=(\d+)", last_url)
        if match:
            return int(match.group(1))
    return None


def _count_via_search(repo):
    SEARCH_LIMITER.acquire()
    resp = requests.get(
        f"{API}/search/issues",
        headers=HEADERS,
        params={"q": f"repo:{repo} type:issue state:open no:assignee", "per_page": 1},
        timeout=30,
    )
    if resp.status_code != 200:
        raise FetchError(f"{repo}: {resp.status_code} {resp.text[:200]}")
    return resp.json()["total_count"]


def fetch_unassigned_summary(repo):
    """Exact unassigned-issue count plus the most recent few. Both come
    from the regular issues endpoint (5000/hr core limit, no secondary
    rate limit risk) except for the rare repo with 1000+ unassigned
    issues, which needs one Search API call just for the count."""
    total_count = _exact_count(repo)
    if total_count is None:
        total_count = _count_via_search(repo)

    recent_resp = _get_issues(repo, per_page=RECENT_COUNT)
    recent = [
        {
            "number": item["number"],
            "title": sanitize_text(item["title"]),
            "url": item["html_url"],
            "comments": item["comments"],
        }
        for item in recent_resp.json()
    ]
    return {"total_count": total_count, "recent": recent}
