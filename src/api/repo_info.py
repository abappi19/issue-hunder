import requests

from api.client import API, HEADERS
from api.errors import check_rate_limited


def contribution_blockers(repo_data):
    """Reasons an outside contributor could not pick up work here, read off
    a repository payload. An empty list means nothing is in the way.

    Forking disabled is the one behind GitHub's "only collaborators can
    create PRs": without a fork, someone without push access has no way to
    open a pull request, so those issues are not really up for grabs.
    Archived and disabled repos take nothing at all, and a repo with issues
    switched off has none to offer in the first place -- those are the rows
    of zeroes padding out the table.

    Absent fields default to permissive, so a trimmed payload is never
    mistaken for a restriction."""
    blockers = []
    if repo_data.get("archived"):
        blockers.append("archived")
    if repo_data.get("disabled"):
        blockers.append("disabled")
    if not repo_data.get("allow_forking", True):
        blockers.append("forking disabled")
    if not repo_data.get("has_issues", True):
        blockers.append("issues disabled")
    return blockers


def fetch_repo_stats(repo):
    resp = requests.get(f"{API}/repos/{repo}", headers=HEADERS, timeout=30)
    check_rate_limited(repo, resp)
    resp.raise_for_status()
    data = resp.json()
    return {"stars": data["stargazers_count"], "blockers": contribution_blockers(data)}
