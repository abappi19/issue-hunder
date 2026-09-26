#!/usr/bin/env python3
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

from api.contributors import fetch_contributor_count
from api.errors import RateLimitError
from api.search_repos import fetch_top_starred_repos
from constants import (
    CANDIDATE_POOL_SIZE,
    MAX_WORKERS,
    MIN_CONTRIBUTORS,
    MIN_DISCOVERY_RATIO,
    MIN_STARS,
    REPOS_DIR,
    TOP_N,
    TOP_REPOS_FILE,
    TOPIC_MIN_STARS,
    TOPICS_FILE,
)
from utils.file_util import load_file, write_file
from utils.slug import to_slug


def discover(topic=None, pool_size=CANDIDATE_POOL_SIZE, min_stars=MIN_STARS):
    label = f"topic:{topic}" if topic else "all repos"
    print(f"=== Discovering: {label} ===")
    print(f"Searching top {pool_size} starred repos ({label}, >{min_stars:,} stars)...")
    candidates = fetch_top_starred_repos(limit=pool_size, topic=topic, min_stars=min_stars)
    print(f"Found {len(candidates)} candidate(s), checking contributor counts...")

    qualified = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_candidate = {
            executor.submit(fetch_contributor_count, c["repo"]): c for c in candidates
        }
        try:
            for future in as_completed(future_to_candidate):
                c = future_to_candidate[future]
                contributors = future.result()
                print(f"  {c['repo']}: {c['stars']} stars, {contributors} contributors")
                if contributors >= MIN_CONTRIBUTORS:
                    qualified.append({**c, "contributors": contributors})
        except RateLimitError:
            # Drop the queued lookups instead of letting the pool work through
            # them; they would all fail the same way and deepen the limit.
            for future in future_to_candidate:
                future.cancel()
            raise

    qualified.sort(key=lambda c: c["stars"], reverse=True)
    top = [c["repo"] for c in qualified[:TOP_N]]
    print(f"{len(qualified)} qualified (>= {MIN_CONTRIBUTORS} contributors), keeping top {len(top)}")
    return top


def write_repo_list(path, repos):
    """Persist a discovered list, refusing to replace an existing one with a
    result that has shrunk past MIN_DISCOVERY_RATIO -- that pattern means the
    run lost candidates to errors, and this file is the input every later
    collection run reads."""
    if os.path.exists(path):
        previous = load_file(path)
        floor = len(previous) * MIN_DISCOVERY_RATIO
        if previous and len(repos) < floor:
            raise SystemExit(
                f"Refusing to overwrite {path}: discovery returned {len(repos)} repo(s), "
                f"down from {len(previous)} (floor is {floor:.0f}). "
                "Re-run once the cause is understood, or delete the file to force a rebuild."
            )

    write_file(path, repos)
    print(f"Wrote {path}.")


def main():
    write_repo_list(TOP_REPOS_FILE, discover())

    topics = load_file(TOPICS_FILE)
    print(f"Loaded {len(topics)} topic(s) from {TOPICS_FILE}: {', '.join(topics)}")

    for topic in topics:
        path = f"{REPOS_DIR}/top_{to_slug(topic)}.json"
        write_repo_list(path, discover(topic=topic, min_stars=TOPIC_MIN_STARS))


if __name__ == "__main__":
    main()
