#!/usr/bin/env python3
from constants import (
    LANGUAGES_FILE,
    OUTPUT_DIR,
    REPOS_DIR,
    TOP_OUTPUT_DIR,
    TOP_REPOS_FILE,
    TOP_SUMMARY_PATH,
    TOP_TITLE,
)
from main import run_collection
from utils.file_util import load_file


def main():
    run_collection(TOP_REPOS_FILE, TOP_OUTPUT_DIR, TOP_SUMMARY_PATH, TOP_TITLE)

    languages = load_file(LANGUAGES_FILE)
    print(f"Loaded {len(languages)} language(s) from {LANGUAGES_FILE}: {', '.join(languages)}")

    for language in languages:
        slug = language.lower()
        run_collection(
            f"{REPOS_DIR}/top_{slug}.json",
            f"{OUTPUT_DIR}/top-{slug}",
            f"{OUTPUT_DIR}/top-{slug}/README.md",
            f"Top {language} Projects",
        )


if __name__ == "__main__":
    main()
