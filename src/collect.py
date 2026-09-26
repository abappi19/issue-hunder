"""Collecting one repo list into pages and an index.

Shared by both collection entry points, which is why it sits here rather
than inside either of them -- collect_top.py importing this from main.py
meant one command's behaviour hung off another command's module."""

from datetime import datetime, timezone

from api.errors import FetchError, RateLimitError
from api.issues import fetch_unassigned_summary
from readme.project import write_project_readme
from readme.sort_key import is_lower_bound, unassigned_value
from store.index import write_collection_index
from store.prune import prune_stale_projects
from utils.file_util import load_file


def run_collection(repos_path, output_dir, title):
    """Collect one repo list into its pages and its index. Returns the repos
    that could not be fetched, so the caller can exit non-zero: a repo that
    has been renamed or made private drops out of the table silently
    otherwise, and nothing ever surfaces that it went stale.

    No per-collection summary is written. The root README carries every
    collection's table in full, so a second copy beside the pages would only
    be another thing to keep in step -- the index left here is what that
    rebuild reads.

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
    scope = f"{len(summaries)} repo{'' if len(summaries) == 1 else 's'}"
    if bounded:
        print(
            f"Done. {total_unassigned}+ unassigned issues across {scope} "
            f"({bounded} repo(s) reported as a lower bound)."
        )
    else:
        print(f"Done. {total_unassigned} unassigned issues across {scope}.")

    if failed:
        print(f"{len(failed)} repo(s) could not be fetched: {', '.join(failed)}")
    return failed
