#!/usr/bin/env python3
import os
from datetime import datetime, timezone

from api.issues import fetch_unassigned_issues
from repos import REPOS

PROJECTS_DIR = "projects"


def write_project_readme(repo, unassigned, generated_at):
    owner, name = repo.split("/")
    project_dir = os.path.join(PROJECTS_DIR, owner, name)
    os.makedirs(project_dir, exist_ok=True)

    unassigned = sorted(unassigned, key=lambda i: i["comments"], reverse=True)

    with open(os.path.join(project_dir, "README.md"), "w") as f:
        f.write(f"# {repo}\n\n")
        f.write(f"Generated: {generated_at}\n\n")
        f.write(f"- Unassigned: {len(unassigned)}\n\n")
        f.write("| Issue | Comments | Labels |\n")
        f.write("|---|---|---|\n")
        for i in unassigned:
            labels = ", ".join(i["labels"]) or "-"
            f.write(
                f"| [#{i['number']} {i['title']}]({i['url']}) | {i['comments']} | {labels} |\n"
            )

    return len(unassigned)


def write_root_readme(summaries, generated_at):
    summaries.sort(key=lambda s: s["unassigned"], reverse=True)
    with open("README.md", "w") as f:
        f.write("# Issue Hunter\n\n")
        f.write("Nightly snapshot of open issues across popular open-source projects.\n\n")
        f.write(f"Generated: {generated_at}\n\n")
        f.write("| Repository | Unassigned |\n")
        f.write("|---|---|\n")
        for s in summaries:
            link = f"projects/{s['repo']}/README.md"
            f.write(f"| [{s['repo']}]({link}) | {s['unassigned']} |\n")


def main():
    generated_at = datetime.now(timezone.utc).isoformat()
    summaries = []

    for repo in REPOS:
        print(f"Fetching unassigned issues for {repo}...")
        unassigned = fetch_unassigned_issues(repo)
        unassigned_count = write_project_readme(repo, unassigned, generated_at)
        summaries.append({"repo": repo, "unassigned": unassigned_count})

    write_root_readme(summaries, generated_at)

    total_unassigned = sum(s["unassigned"] for s in summaries)
    print(f"Done. {total_unassigned} unassigned issues across {len(REPOS)} repos.")


if __name__ == "__main__":
    main()
