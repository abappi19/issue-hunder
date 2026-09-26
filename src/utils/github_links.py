from urllib.parse import quote


def unassigned_issues_url(repo):
    return f"https://github.com/{repo}/issues?q=" + quote("is:issue is:open no:assignee")
