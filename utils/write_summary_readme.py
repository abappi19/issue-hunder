import os


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
            link = f"{output_dir}/{s['repo']}/README.md"
            f.write(f"| [{s['repo']}]({link}) | {s['unassigned']} |\n")
