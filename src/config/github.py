import os

API = "https://api.github.com"
MAX_WORKERS = 10

# "Popular" repo bar used both by discover_repos.py (auto-discovery) and
# check_new_repos.py (PR check on manually-added repos.json entries).
MIN_STARS = 10000
MIN_CONTRIBUTORS = 50
TOKEN = os.environ.get("GITHUB_TOKEN")
HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"
