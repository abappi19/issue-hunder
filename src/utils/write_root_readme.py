import os

from constants import MIN_CONTRIBUTORS, MIN_STARS, README_END_MARKER, README_START_MARKER
from utils.github_links import project_readme_link, unassigned_issues_url
from utils.sort_key import unassigned_sort_key

DEFAULT_HEADER = f"""# Issue Hunter

Issue Hunter tracks **unassigned, open issues** across popular open-source
projects, so contributors can quickly find real work to pick up.

A GitHub Action re-scans every tracked repository on a schedule and rebuilds
the table below with the current unassigned-issue count for each one. Click
a repo's count to jump straight to its live, filtered issue list on GitHub.
Each repo also gets its own page under `output/projects/<owner>/<repo>/README.md`
listing its most recently opened unassigned issues.

## Want to add a repo?

Open a pull request adding `"owner/repo"` to `src/repos/repos.json`. A CI
check automatically verifies the repo meets our popularity bar (currently
at least {MIN_STARS:,} stars and {MIN_CONTRIBUTORS}+ contributors) before it
can be merged.

"""


def write_root_readme(summaries, output_dir, summary_path, title, generated_at):
    summaries.sort(key=lambda s: unassigned_sort_key(s["unassigned"]), reverse=True)

    table_lines = ["| Repository | Unassigned |", "|---|---|"]
    for s in summaries:
        project_link = project_readme_link(s["repo"], output_dir, summary_path)
        issues_link = unassigned_issues_url(s["repo"])
        table_lines.append(f"| [{s['repo']}]({project_link}) | [{s['unassigned']}]({issues_link}) |")

    generated_block = (
        f"{README_START_MARKER}\n"
        f"_Last updated: {generated_at}_\n\n"
        + "\n".join(table_lines)
        + f"\n{README_END_MARKER}\n"
    )

    existing = None
    if os.path.exists(summary_path):
        with open(summary_path) as f:
            existing = f.read()

    if existing and README_START_MARKER in existing and README_END_MARKER in existing:
        start = existing.index(README_START_MARKER)
        end = existing.index(README_END_MARKER) + len(README_END_MARKER)
        new_content = existing[:start] + generated_block.rstrip("\n") + existing[end:]
    else:
        new_content = DEFAULT_HEADER + generated_block

    os.makedirs(os.path.dirname(summary_path) or ".", exist_ok=True)
    with open(summary_path, "w") as f:
        f.write(new_content)
