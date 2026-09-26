import re
from functools import lru_cache

import requests

from api.client import API, HEADERS
from api.errors import check_rate_limited


@lru_cache(maxsize=None)
def fetch_contributor_count(repo):
    """Contributor count for a repo, read off the last-page number in the
    Link header (per_page=1) instead of paginating every contributor.

    Cached per run: the unscoped candidate pool overlaps heavily with the
    per-topic ones, and a repo appearing in several of them needs looking up
    only once.

    A rate-limit rejection raises rather than returning 0. Returning 0 would
    be indistinguishable from a repo that genuinely has no contributors, and
    since callers filter on a minimum count, a limit hit partway through a
    run would quietly drop every remaining candidate and persist the
    truncated result as if it were the real answer."""
    resp = requests.get(
        f"{API}/repos/{repo}/contributors",
        headers=HEADERS,
        params={"per_page": 1, "anon": "false"},
        timeout=30,
    )
    check_rate_limited(repo, resp)
    if resp.status_code != 200:
        return 0

    last_url = resp.links.get("last", {}).get("url")
    if last_url:
        match = re.search(r"[?&]page=(\d+)", last_url)
        if match:
            return int(match.group(1))

    return len(resp.json())
