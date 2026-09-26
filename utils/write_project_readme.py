import os


def write_project_readme(repo, unassigned, output_dir, generated_at):
    owner, name = repo.split("/")
    project_dir = os.path.join(output_dir, owner, name)
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
