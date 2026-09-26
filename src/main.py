#!/usr/bin/env python3
import sys
from datetime import datetime, timezone

from api.errors import FetchError, RateLimitError
from api.issues import fetch_unassigned_summary
from utils.collection_index import write_collection_index
from utils.file_util import load_file
from utils.parse_args import parse_args
from utils.prune_output import prune_stale_projects
from utils.sort_key import is_lower_bound, unassigned_value
from utils.write_project_readme import write_project_readme
from utils.write_root_readme import write_root_readme
from utils.write_summary_readme import write_summary_readme


def run_collection(repos_path, output_dir, title, summary_path=None):
    """Collect one repo list into its pages and its index. Returns the repos
    that could not be fetched, so the caller can exit non-zero: a repo that
    has been renamed or made private drops out of the table silently
    otherwise, and nothing ever surfaces that it went stale.

    `summary_path` adds a summary README for this collection alone. The
    curated collection passes None -- the root README already lists it
    alongside every other collection, so a second table of the same repos
    would only be one more thing to keep in step.

    A rate limit is not survivable the way a single bad repo is, so it
    propagates instead -- every remaining repo would fail too, and the run
    would write a summary listing only the repos it reached before the
    limit, replacing a complete table with a truncated one."""
    print(f"=== {title} ===")
    repos = load_file(repos_path)
    print(f"Loaded {len(repos)} repo(s) from {repos_path}")
    generated_at = datetime.now(timezone.utc).isoformat()
    summaries = []
    failed = []

    for i, repo in enumerate(repos, start=1):
        try:
            summary = fetch_unassigned_summary(repo)
        except RateLimitError:
            raise
        except FetchError as e:
            print(f"  [{i}/{len(repos)}] {repo}: SKIPPED ({e})")
            failed.append(repo)
            continue
        print(f"  [{i}/{len(repos)}] {repo}: {summary['total_count']} unassigned")
        unassigned_count = write_project_readme(repo, summary, output_dir, generated_at)
        summaries.append({"repo": repo, "unassigned": unassigned_count})

    write_collection_index(output_dir, title, generated_at, summaries)
    if summary_path:
        print(f"Writing summary to {summary_path}")
        write_summary_readme(summaries, output_dir, summary_path, title, generated_at)

    if failed:
        # A pruning pass now would delete the pages of the repos just skipped,
        # reading a transient fetch failure as "no longer tracked".
        print(f"Skipping stale-page cleanup: {len(failed)} repo(s) failed this run.")
    else:
        for repo in prune_stale_projects(output_dir, repos):
            print(f"Removed stale page for {repo} (no longer tracked)")

    # Count every repo, not just the exactly-counted ones: a lower bound still
    # contributes its number, and skipping those made the total read "0+" as
    # soon as every repo came back bounded.
    total_unassigned = sum(unassigned_value(s["unassigned"]) for s in summaries)
    bounded = sum(1 for s in summaries if is_lower_bound(s["unassigned"]))
    if bounded:
        print(
            f"Done. {total_unassigned}+ unassigned issues across {len(summaries)} repos "
            f"({bounded} repo(s) reported as a lower bound)."
        )
    else:
        print(f"Done. {total_unassigned} unassigned issues across {len(summaries)} repos.")

    if failed:
        print(f"{len(failed)} repo(s) could not be fetched: {', '.join(failed)}")
    return failed


def main():
    args = parse_args()
    try:
        failed = run_collection(args.repos, args.output, args.title)
    except RateLimitError as e:
        print(f"Aborted: {e}", file=sys.stderr)
        sys.exit(1)

    # Rebuilt from every collection's index, so the front page keeps linking
    # the top-repo projects this run never touched.
    write_root_readme(args.summary)
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
