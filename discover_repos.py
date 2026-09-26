#!/usr/bin/env python3
from api.contributors import fetch_contributor_count
from api.search_repos import fetch_top_starred_repos
from utils.file_util import load_file, write_file

CANDIDATE_POOL_SIZE = 100
MIN_CONTRIBUTORS = 50
TOP_N = 20
LANGUAGES_FILE = "repos/languages.json"


def discover(language=None, pool_size=CANDIDATE_POOL_SIZE):
    label = language or "all languages"
    print(f"Searching top {pool_size} starred repos ({label})...")
    candidates = fetch_top_starred_repos(limit=pool_size, language=language)

    qualified = []
    for c in candidates:
        contributors = fetch_contributor_count(c["repo"])
        print(f"  {c['repo']}: {c['stars']} stars, {contributors} contributors")
        if contributors >= MIN_CONTRIBUTORS:
            qualified.append({**c, "contributors": contributors})

    qualified.sort(key=lambda c: c["stars"], reverse=True)
    return [c["repo"] for c in qualified[:TOP_N]]


def main():
    write_file("repos/top_repos.json", discover())
    print("Wrote repos/top_repos.json.")

    languages = load_file(LANGUAGES_FILE)

    for language in languages:
        slug = language.lower()
        repos = discover(language=language)
        write_file(f"repos/top_{slug}.json", repos)
        print(f"Wrote repos/top_{slug}.json.")


if __name__ == "__main__":
    main()
