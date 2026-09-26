#!/usr/bin/env python3
import json
import subprocess
import sys

from api.repo_info import fetch_repo_stats
from constants import MIN_STARS, REPOS_FILE


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


def check(repos):
    """Check each repo against the bar, returning the ones that fail it.

    One request per repo: the star count and the contribution blockers both
    come off the same repository payload."""
    failed = []
    for repo in repos:
        try:
            stats = fetch_repo_stats(repo)
        except Exception as e:
            print(f"  [FAIL] {repo}: could not fetch repo info ({e})")
            failed.append(repo)
            continue

        reasons = list(stats["blockers"])
        if stats["stars"] < MIN_STARS:
            reasons.append(f"only {stats['stars']:,} stars")

        if reasons:
            failed.append(repo)
            print(f"  [FAIL] {repo}: {', '.join(reasons)}")
        else:
            print(f"  [OK]   {repo}: {stats['stars']:,} stars")
    return failed


def main():
    if len(sys.argv) != 2:
        print("Usage: check_new_repos.py <base-ref>|--all", file=sys.stderr)
        sys.exit(2)
    target = sys.argv[1]

    with open(REPOS_FILE) as f:
        current = set(json.load(f))

    if target == "--all":
        # For auditing entries added before a bar existed, rather than only
        # what a pull request touches.
        to_check = sorted(current)
        print(f"=== Checking every repo in {REPOS_FILE} ===")
    else:
        print(f"=== Checking new repos against {REPOS_FILE} at {target} ===")
        to_check = sorted(current - set(load_repos_at_ref(target)))
        if not to_check:
            print(f"No new repos added to {REPOS_FILE}.")
            return

    print(
        f"Checking {len(to_check)} repo(s): >= {MIN_STARS:,} stars, "
        "and open to outside contributions..."
    )
    failed = check(to_check)

    if failed:
        print(f"\n{len(failed)} repo(s) do not meet the bar: {', '.join(failed)}")
        sys.exit(1)

    print("\nAll checked repos meet the bar.")


if __name__ == "__main__":
    main()
