import requests

from config.github import API, HEADERS
from constants import RECENT_COUNT
from utils.sanitize import sanitize_text


class FetchError(Exception):
    pass


def fetch_unassigned_summary(repo):
    """Unassigned-issue count (exact if under RECENT_COUNT, else
    "<RECENT_COUNT>+") plus the most recent few -- a single, minimal call
    to the regular issues endpoint (5000/hr core limit), never the Search
    API. Doesn't rely on the Link header's last-page number: GitHub's
    issues endpoint uses cursor-based pagination (an opaque `after` token)
    unconditionally now, regardless of result size, so no last-page number
    is ever available to read."""
    resp = requests.get(
        f"{API}/repos/{repo}/issues",
        headers=HEADERS,
        params={"state": "open", "assignee": "none", "per_page": RECENT_COUNT},
        timeout=30,
    )
    if resp.status_code != 200:
        raise FetchError(f"{repo}: {resp.status_code} {resp.text[:200]}")

    items = resp.json()
    total_count = len(items) if len(items) < RECENT_COUNT else f"{RECENT_COUNT}+"

    recent = [
        {
            "number": item["number"],
            "title": sanitize_text(item["title"]),
            "url": item["html_url"],
            "comments": item["comments"],
        }
        for item in items
    ]
    return {"total_count": total_count, "recent": recent}
