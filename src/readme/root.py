import os

from constants import (
    MIN_CONTRIBUTORS,
    MIN_STARS,
    OUTPUT_DIR,
    README_END_MARKER,
    README_START_MARKER,
)
from readme.links import project_readme_link, unassigned_issues_url
from readme.sort_key import unassigned_sort_key
from store.index import read_collection_indexes

DEFAULT_HEADER = f"""# Issue Hunter

Issue Hunter tracks **unassigned, open issues** across popular open-source
projects, so contributors can quickly find real work to pick up.

A GitHub Action re-scans every tracked repository on a schedule and rebuilds
the tables below with the current unassigned-issue count for each one. Click
a repo's count to jump straight to its live, filtered issue list on GitHub,
or its name to open its page here, listing the most recently opened
unassigned issues waiting for someone to pick them up.

## Want to add a repo?

Open a pull request adding `"owner/repo"` to `data/repos.json`. A CI
check automatically verifies that the repo clears our popularity bar
(currently at least {MIN_STARS:,} stars and {MIN_CONTRIBUTORS}+ contributors)
and is open to outside contributions -- not archived, with forking and
issues both enabled -- before it can be merged.

"""


def _collection_section(dir_name, index, summary_path):
    repos = sorted(index["repos"], key=lambda s: unassigned_sort_key(s["unassigned"]), reverse=True)
    output_dir = os.path.join(OUTPUT_DIR, dir_name)

    lines = [
        f"## {index['title']}",
        "",
        f"_{len(repos)} repo{'' if len(repos) == 1 else 's'} · updated {index['generated_at']}_",
        "",
        "| Repository | Unassigned |",
        "|---|---|",
    ]
    for s in repos:
        project_link = project_readme_link(s["repo"], output_dir, summary_path)
        issues_link = unassigned_issues_url(s["repo"])
        lines.append(f"| [{s['repo']}]({project_link}) | [{s['unassigned']}]({issues_link}) |")
    return "\n".join(lines)


def write_root_readme(summary_path, output_dir=OUTPUT_DIR):
    """Rebuild the root README's generated section from every collection
    index on disk, so each project page is reachable from the front page.

    Both collection runs call this, and each rebuilds all the sections --
    including ones it did not produce. A section therefore carries its own
    collection's timestamp rather than the time of this run, since one
    workflow's figures can be a scheduled run older than another's."""
    collections = read_collection_indexes(output_dir)
    sections = [
        _collection_section(dir_name, index, summary_path) for dir_name, index in collections
    ]
    if not sections:
        print(f"No collection indexes under {output_dir}/; leaving {summary_path} alone.")
        return

    generated_block = (
        f"{README_START_MARKER}\n" + "\n\n".join(sections) + f"\n{README_END_MARKER}\n"
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

    total = sum(len(index["repos"]) for _, index in collections)
    print(f"Rebuilt {summary_path}: {len(sections)} collection(s), {total} project(s) linked.")
