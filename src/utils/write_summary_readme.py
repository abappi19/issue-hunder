import os

from utils.github_links import unassigned_issues_url


def write_summary_readme(summaries, output_dir, summary_path, title, generated_at):
    summaries.sort(key=lambda s: s["unassigned"], reverse=True)
    os.makedirs(os.path.dirname(summary_path) or ".", exist_ok=True)
    with open(summary_path, "w") as f:
        f.write(f"# {title}\n\n")
        f.write("Snapshot of open issues across popular open-source projects.\n\n")
        f.write(f"Generated: {generated_at}\n\n")
        f.write("| Repository | Unassigned |\n")
        f.write("|---|---|\n")
        for s in summaries:
            project_link = f"{output_dir}/{s['repo']}/README.md"
            issues_link = unassigned_issues_url(s["repo"])
            f.write(f"| [{s['repo']}]({project_link}) | [{s['unassigned']}]({issues_link}) |\n")
