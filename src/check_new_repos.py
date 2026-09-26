#!/usr/bin/env python3
import json
import subprocess
import sys

from api.contributors import fetch_contributor_count
from api.repo_info import fetch_repo_stats
from constants import MIN_CONTRIBUTORS, MIN_STARS, REPOS_FILE


def load_repos_at_ref(ref):
    """The repo list as of `ref`, or [] if the file did not exist yet.

    An unreadable ref is a different thing entirely and exits instead of
    falling back to []: that fallback would mark every repo in the file as
    newly added, re-checking all of them against the popularity bar and
    failing the PR over a repo that was merged long ago."""
    if subprocess.run(["git", "rev-parse", "--verify", f"{ref}^{{commit}}"]).returncode != 0:
        print(f"Cannot resolve base ref {ref!r}; is the checkout shallow?", file=sys.stderr)
        sys.exit(2)

    result = subprocess.run(
        ["git", "show", f"{ref}:{REPOS_FILE}"], capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"{REPOS_FILE} did not exist at {ref}; treating every entry as new.")
        return []
    return json.loads(result.stdout)


def main():
    if len(sys.argv) != 2:
        print("Usage: check_new_repos.py <base-ref>", file=sys.stderr)
        sys.exit(2)
    base_ref = sys.argv[1]

    print(f"=== Checking new repos against {REPOS_FILE} at {base_ref} ===")
    old_repos = set(load_repos_at_ref(base_ref))
    with open(REPOS_FILE) as f:
        new_repos = set(json.load(f))
    added = sorted(new_repos - old_repos)

    if not added:
        print("No new repos added to src/repos/repos.json.")
        return

    print(
        f"Checking {len(added)} newly added repo(s) against the popularity bar "
        f"(>= {MIN_STARS:,} stars, >= {MIN_CONTRIBUTORS} contributors)..."
    )

    failed = []
    for repo in added:
        try:
            stars = fetch_repo_stats(repo)["stars"]
            contributors = fetch_contributor_count(repo)
        except Exception as e:
            print(f"  [FAIL] {repo}: could not fetch repo info ({e})")
            failed.append(repo)
            continue

        ok = stars >= MIN_STARS and contributors >= MIN_CONTRIBUTORS
        status = "OK" if ok else "FAIL"
        print(f"  [{status}] {repo}: {stars:,} stars, {contributors} contributors")
        if not ok:
            failed.append(repo)

    if failed:
        print(f"\n{len(failed)} repo(s) do not meet the popularity bar: {', '.join(failed)}")
        sys.exit(1)

    print("\nAll new repos meet the popularity bar.")


if __name__ == "__main__":
    main()
