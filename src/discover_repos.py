#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor, as_completed

from api.contributors import fetch_contributor_count
from api.search_repos import fetch_top_starred_repos
from constants import (
    CANDIDATE_POOL_SIZE,
    LANGUAGES_FILE,
    MAX_WORKERS,
    MIN_CONTRIBUTORS,
    REPOS_DIR,
    TOP_N,
    TOP_REPOS_FILE,
)
from utils.file_util import load_file, write_file


def discover(language=None, pool_size=CANDIDATE_POOL_SIZE):
    label = language or "all languages"
    print(f"=== Discovering: {label} ===")
    print(f"Searching top {pool_size} starred repos ({label})...")
    candidates = fetch_top_starred_repos(limit=pool_size, language=language)
    print(f"Found {len(candidates)} candidate(s), checking contributor counts...")

    qualified = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_candidate = {
            executor.submit(fetch_contributor_count, c["repo"]): c for c in candidates
        }
        for future in as_completed(future_to_candidate):
            c = future_to_candidate[future]
            contributors = future.result()
            print(f"  {c['repo']}: {c['stars']} stars, {contributors} contributors")
            if contributors >= MIN_CONTRIBUTORS:
                qualified.append({**c, "contributors": contributors})

    qualified.sort(key=lambda c: c["stars"], reverse=True)
    top = [c["repo"] for c in qualified[:TOP_N]]
    print(f"{len(qualified)} qualified (>= {MIN_CONTRIBUTORS} contributors), keeping top {len(top)}")
    return top


def main():
    write_file(TOP_REPOS_FILE, discover())
    print(f"Wrote {TOP_REPOS_FILE}.")

    languages = load_file(LANGUAGES_FILE)
    print(f"Loaded {len(languages)} language(s) from {LANGUAGES_FILE}: {', '.join(languages)}")

    for language in languages:
        slug = language.lower()
        path = f"{REPOS_DIR}/top_{slug}.json"
        repos = discover(language=language)
        write_file(path, repos)
        print(f"Wrote {path}.")


if __name__ == "__main__":
    main()
