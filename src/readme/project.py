import os

from readme.links import unassigned_issues_url


def write_project_readme(repo, summary, output_dir, generated_at):
    owner, name = repo.split("/")
    project_dir = os.path.join(output_dir, owner, name)
    os.makedirs(project_dir, exist_ok=True)

    total_count = summary["total_count"]
    recent = summary["recent"]
    issues_url = unassigned_issues_url(repo)

    with open(os.path.join(project_dir, "README.md"), "w") as f:
        f.write(f"# {repo}\n\n")
        f.write(f"Generated: {generated_at}\n\n")
        f.write(f"- Unassigned: {total_count}\n")
        f.write(f"- [View all unassigned issues]({issues_url})\n\n")
        f.write("Most recently opened:\n\n")
        f.write("| Issue | Comments |\n")
        f.write("|---|---|\n")
        for i in recent:
            f.write(f"| [#{i['number']} {i['title']}]({i['url']}) | {i['comments']} |\n")

    return total_count
