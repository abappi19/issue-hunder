import requests

from api.errors import check_rate_limited
from config.github import API, HEADERS


def fetch_repo_stats(repo):
    resp = requests.get(f"{API}/repos/{repo}", headers=HEADERS, timeout=30)
    check_rate_limited(repo, resp)
    resp.raise_for_status()
    data = resp.json()
    return {"stars": data["stargazers_count"]}
