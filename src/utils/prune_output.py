import os
import shutil


def prune_stale_collections(output_dir, keep_dir_names, prefix):
    """Delete whole collection directories no longer being produced.

    Dropping a language from languages.json otherwise strands its pages and
    its index, and the index is what the root README is rebuilt from -- so
    the front page would keep advertising a collection that no run refreshes
    any more.

    `prefix` scopes this to the collections a given run owns, so the curated
    projects/ directory is never a candidate."""
    if not os.path.isdir(output_dir):
        return []

    removed = []
    for dir_name in sorted(os.listdir(output_dir)):
        path = os.path.join(output_dir, dir_name)
        if not os.path.isdir(path) or not dir_name.startswith(prefix):
            continue
        if dir_name not in keep_dir_names:
            shutil.rmtree(path)
            removed.append(dir_name)
    return removed


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
