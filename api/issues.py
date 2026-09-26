import sys

import requests

from config.github import API, HEADERS


def fetch_unassigned_issues(repo):
    """Ask GitHub to filter unassigned issues server-side (assignee=none) instead
    of fetching every open issue and filtering client-side."""
    issues = []
    url = f"{API}/repos/{repo}/issues"
    params = {"state": "open", "assignee": "none", "per_page": 100}
    while url:
        resp = requests.get(url, headers=HEADERS, params=params, timeout=30)
        if resp.status_code != 200:
            print(f"  ! {repo}: {resp.status_code} {resp.text[:200]}", file=sys.stderr)
            break
        batch = resp.json()
        for item in batch:
            if "pull_request" in item:  # skip PRs, the issues endpoint includes them
                continue
            issues.append(
                {
                    "number": item["number"],
                    "title": item["title"],
                    "url": item["html_url"],
                    "labels": [l["name"] for l in item.get("labels", [])],
                    "comments": item["comments"],
                    "created_at": item["created_at"],
                    "updated_at": item["updated_at"],
                }
            )
        # Follow the "next" link from the Link header (cursor-based pagination).
        # GitHub rejects page-number pagination past 1000 results ("large datasets").
        url = resp.links.get("next", {}).get("url")
        params = None  # next URL already includes all query params
    return issues
