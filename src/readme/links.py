import posixpath
from urllib.parse import quote


def unassigned_issues_url(repo):
    return f"https://github.com/{repo}/issues?q=" + quote("is:issue is:open no:assignee")


def project_readme_link(repo, output_dir, summary_path):
    """Markdown link from a summary README to one project's page.

    Relative links resolve against the linking file's own directory, not the
    repo root, so the output dir has to be re-expressed relative to wherever
    the summary lives -- for a summary sitting inside its own output dir
    (output/top-projects/README.md), prefixing the path verbatim would point
    at output/top-projects/output/top-projects/..."""
    target = posixpath.join(output_dir, repo, "README.md")
    return posixpath.relpath(target, posixpath.dirname(summary_path) or ".")
