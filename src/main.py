#!/usr/bin/env python3
from datetime import datetime, timezone

from api.issues import fetch_unassigned_summary
from utils.file_util import load_file
from utils.parse_args import parse_args
from utils.write_project_readme import write_project_readme
from utils.write_root_readme import write_root_readme
from utils.write_summary_readme import write_summary_readme


def run_collection(repos_path, output_dir, summary_path, title, summary_writer=write_summary_readme):
    print(f"=== {title} ===")
    repos = load_file(repos_path)
    print(f"Loaded {len(repos)} repo(s) from {repos_path}")
    generated_at = datetime.now(timezone.utc).isoformat()
    summaries = []

    for i, repo in enumerate(repos, start=1):
        summary = fetch_unassigned_summary(repo)
        print(f"  [{i}/{len(repos)}] {repo}: {summary['total_count']} unassigned")
        unassigned_count = write_project_readme(repo, summary, output_dir, generated_at)
        summaries.append({"repo": repo, "unassigned": unassigned_count})

    print(f"Writing summary to {summary_path}")
    summary_writer(summaries, output_dir, summary_path, title, generated_at)

    exact = [s["unassigned"] for s in summaries if isinstance(s["unassigned"], int)]
    capped = len(summaries) - len(exact)
    total_unassigned = sum(exact)
    if capped:
        print(
            f"Done. {total_unassigned}+ unassigned issues across {len(repos)} repos "
            f"({capped} repo(s) capped at 100+)."
        )
    else:
        print(f"Done. {total_unassigned} unassigned issues across {len(repos)} repos.")


def main():
    args = parse_args()
    run_collection(args.repos, args.output, args.summary, args.title, summary_writer=write_root_readme)


if __name__ == "__main__":
    main()
