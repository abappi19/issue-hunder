import time

import requests

from config.github import API, HEADERS
from utils.rate_limiter import RateLimiter
from utils.sanitize import sanitize_text

RECENT_COUNT = 5
MAX_RETRIES = 5

# GitHub's Search API caps at 30 requests/min (authenticated) and also
# applies a stricter, undocumented "secondary rate limit" that triggers on
# concurrent/bursty requests regardless of per-minute count. GitHub's own
# guidance is to make requests to this endpoint serially, not concurrently
# -- so this limiter's job is pacing, and callers must not thread this call.
_SEARCH_LIMITER = RateLimiter(max_calls=25, period=60)


class FetchError(Exception):
    pass


def fetch_unassigned_summary(repo):
    """Total open+unassigned issue count and the most recent few, via a
    single Search API call instead of paginating through every issue."""
    for attempt in range(1, MAX_RETRIES + 1):
        _SEARCH_LIMITER.acquire()
        resp = requests.get(
            f"{API}/search/issues",
            headers=HEADERS,
            params={
                "q": f"repo:{repo} type:issue state:open no:assignee",
                "sort": "created",
                "order": "desc",
                "per_page": RECENT_COUNT,
            },
            timeout=30,
        )
        if resp.status_code == 200:
            data = resp.json()
            recent = [
                {
                    "number": item["number"],
                    "title": sanitize_text(item["title"]),
                    "url": item["html_url"],
                    "comments": item["comments"],
                }
                for item in data["items"]
            ]
            return {"total_count": data["total_count"], "recent": recent}

        if resp.status_code in (403, 422) and attempt < MAX_RETRIES:
            # No Retry-After on secondary rate limits is common; GitHub's own
            # guidance is just "wait a few minutes", so back off exponentially
            # with a floor well above the primary limit's 60s window.
            default_wait = min(60 * 2 ** (attempt - 1), 300)
            wait = int(resp.headers.get("Retry-After", default_wait))
            print(f"  ! {repo}: rate limited (attempt {attempt}/{MAX_RETRIES}), retrying in {wait}s")
            time.sleep(wait)
            continue

        raise FetchError(f"{repo}: {resp.status_code} {resp.text[:200]}")

    raise FetchError(f"{repo}: exhausted retries")
