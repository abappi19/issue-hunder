import requests

from config.github import API, HEADERS, MIN_STARS


def fetch_top_starred_repos(limit=100, language=None):
    """Top starred public repos, via the Search API's stars-sort. Returns
    [{"repo": "owner/name", "stars": int}, ...] ordered by stars desc.
    Pass `language` (e.g. "TypeScript") to restrict the search to that language."""
    repos = []
    per_page = 100
    page = 1
    query = f"stars:>{MIN_STARS}"
    if language:
        query += f" language:{language}"
    while len(repos) < limit:
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
        resp.raise_for_status()
        items = resp.json()["items"]
        if not items:
            break
        for item in items:
            repos.append({"repo": item["full_name"], "stars": item["stargazers_count"]})
        page += 1
        if len(items) < per_page:
            break
    return repos[:limit]
