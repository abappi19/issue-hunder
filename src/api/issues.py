import requests

from config.github import API, HEADERS
from utils.sanitize import sanitize_text

PAGE_SIZE = 100
RECENT_COUNT = 5


class FetchError(Exception):
    pass


def fetch_unassigned_summary(repo):
    """Unassigned-issue count (exact if under PAGE_SIZE, else "100+") plus
    the most recent few -- a single call to the regular issues endpoint
    (5000/hr core limit), never the Search API. Doesn't rely on the Link
    header's last-page number: GitHub's issues endpoint uses cursor-based
    pagination (an opaque `after` token) unconditionally now, regardless of
    result size, so no last-page number is ever available to read."""
    resp = requests.get(
        f"{API}/repos/{repo}/issues",
        headers=HEADERS,
        params={"state": "open", "assignee": "none", "per_page": PAGE_SIZE},
        timeout=30,
    )
    if resp.status_code != 200:
        raise FetchError(f"{repo}: {resp.status_code} {resp.text[:200]}")

    items = resp.json()
    total_count = len(items) if len(items) < PAGE_SIZE else f"{PAGE_SIZE}+"

    recent = [
        {
            "number": item["number"],
            "title": sanitize_text(item["title"]),
            "url": item["html_url"],
            "comments": item["comments"],
        }
        for item in items[:RECENT_COUNT]
    ]
    return {"total_count": total_count, "recent": recent}
