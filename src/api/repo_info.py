import requests

from config.github import API, HEADERS


def fetch_repo_stats(repo):
    resp = requests.get(f"{API}/repos/{repo}", headers=HEADERS, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return {"stars": data["stargazers_count"]}
