import requests

from api.client import API, HEADERS
from api.errors import check_rate_limited
from api.rate_limit import SEARCH_LIMITER
from api.repo_info import contribution_blockers
from constants import MIN_STARS


def fetch_top_starred_repos(limit=100, topic=None, min_stars=MIN_STARS):
    """Top starred public repos, via the Search API's stars-sort. Returns
    [{"repo": "owner/name", "stars": int}, ...] ordered by stars desc.

    Pass `topic` (e.g. "react-native") to restrict the search to repos
    carrying that GitHub topic, and `min_stars` to set the floor -- a topic
    draws from a much smaller pool than the whole of GitHub and needs a
    lower one to fill a list.

    Repos nobody outside could contribute to are dropped here rather than
    later: a search result is a full repository payload, so the flags come
    free with a search already being made, where checking them per candidate
    afterwards would cost a request each and double the discovery budget.
    Dropped repos are backfilled from further down the ranking, so a list
    still comes back `limit` long."""
    repos = []
    skipped = []
    per_page = 100
    page = 1
    query = f"stars:>{min_stars}"
    if topic:
        query += f" topic:{topic}"
    while len(repos) < limit:
        SEARCH_LIMITER.acquire()
        resp = requests.get(
            f"{API}/search/repositories",
            headers=HEADERS,
            params={
                "q": query,
                "sort": "stars",
                "order": "desc",
                "per_page": per_page,
                "page": page,
            },
            timeout=30,
        )
        check_rate_limited(query, resp)
        resp.raise_for_status()
        items = resp.json()["items"]
        if not items:
            break
        for item in items:
            blockers = contribution_blockers(item)
            if blockers:
                skipped.append(f"{item['full_name']} ({', '.join(blockers)})")
                continue
            repos.append({"repo": item["full_name"], "stars": item["stargazers_count"]})
        page += 1
        if len(items) < per_page:
            break

    if skipped:
        print(f"  Skipped {len(skipped)} repo(s) that cannot take contributions:")
        for entry in skipped:
            print(f"    - {entry}")
    return repos[:limit]
