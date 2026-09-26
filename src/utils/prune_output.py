import os
import shutil


def prune_stale_projects(output_dir, repos):
    """Delete generated project pages for repos that are no longer tracked.

    Without this, a repo dropped from a list keeps its page in output/ for
    good and the workflow re-commits it every week, so the tree fills with
    snapshots that nothing links to and that never refresh again.

    Only <output_dir>/<owner>/<name>/ directories are touched, which leaves
    a summary README sitting alongside them intact."""
    if not os.path.isdir(output_dir):
        return []

    keep = {tuple(repo.split("/", 1)) for repo in repos}
    removed = []

    for owner in sorted(os.listdir(output_dir)):
        owner_path = os.path.join(output_dir, owner)
        if not os.path.isdir(owner_path):
            continue

        for name in sorted(os.listdir(owner_path)):
            repo_path = os.path.join(owner_path, name)
            if os.path.isdir(repo_path) and (owner, name) not in keep:
                shutil.rmtree(repo_path)
                removed.append(f"{owner}/{name}")

        if not os.listdir(owner_path):
            os.rmdir(owner_path)

    return removed
