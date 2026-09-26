#!/usr/bin/env python3
import sys

from api.errors import RateLimitError
from constants import (
    DEFAULT_SUMMARY_PATH,
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
from utils.slug import language_slug
from utils.write_root_readme import write_root_readme


def main():
    failed = []
    try:
        failed += run_collection(
            TOP_REPOS_FILE, TOP_OUTPUT_DIR, TOP_TITLE, summary_path=TOP_SUMMARY_PATH
        )

        languages = load_file(LANGUAGES_FILE)
        print(f"Loaded {len(languages)} language(s) from {LANGUAGES_FILE}: {', '.join(languages)}")

        for language in languages:
            slug = language_slug(language)
            failed += run_collection(
                f"{REPOS_DIR}/top_{slug}.json",
                f"{OUTPUT_DIR}/top-{slug}",
                f"Top {language} Projects",
                summary_path=f"{OUTPUT_DIR}/top-{slug}/README.md",
            )
    except RateLimitError as e:
        # Later collections would only deepen the limit, so stop here and keep
        # whatever earlier ones already wrote.
        print(f"Aborted: {e}", file=sys.stderr)
        write_root_readme(DEFAULT_SUMMARY_PATH)
        sys.exit(1)

    # This workflow runs after the curated one, so it has the last word on the
    # front page and must relist that collection too, not just its own.
    write_root_readme(DEFAULT_SUMMARY_PATH)
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
