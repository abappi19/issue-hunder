import re

import requests

from config.github import API, HEADERS


def fetch_contributor_count(repo):
    """Contributor count for a repo, read off the last-page number in the
    Link header (per_page=1) instead of paginating every contributor."""
    resp = requests.get(
        f"{API}/repos/{repo}/contributors",
        headers=HEADERS,
        params={"per_page": 1, "anon": "false"},
        timeout=30,
    )
    if resp.status_code != 200:
        return 0

    last_url = resp.links.get("last", {}).get("url")
    if last_url:
        match = re.search(r"[?&]page=(\d+)", last_url)
        if match:
            return int(match.group(1))

    return len(resp.json())
