#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

from api.issues import fetch_unassigned_issues
from config.github import MAX_WORKERS
from utils.file_util import load_file
from utils.parse_args import parse_args
from utils.write_project_readme import write_project_readme
from utils.write_summary_readme import write_summary_readme


def run_collection(repos_path, output_dir, summary_path, title):
    repos = load_file(repos_path)
    generated_at = datetime.now(timezone.utc).isoformat()
    summaries = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_repo = {executor.submit(fetch_unassigned_issues, repo): repo for repo in repos}
        for future in as_completed(future_to_repo):
            repo = future_to_repo[future]
            unassigned = future.result()
            print(f"Fetched {len(unassigned)} unassigned issues for {repo}")
            unassigned_count = write_project_readme(repo, unassigned, output_dir, generated_at)
            summaries.append({"repo": repo, "unassigned": unassigned_count})

    write_summary_readme(summaries, output_dir, summary_path, title, generated_at)

    total_unassigned = sum(s["unassigned"] for s in summaries)
    print(f"Done. {total_unassigned} unassigned issues across {len(repos)} repos.")


def main():
    args = parse_args()
    run_collection(args.repos, args.output, args.summary, args.title)


if __name__ == "__main__":
    main()
