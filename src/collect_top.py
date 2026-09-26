#!/usr/bin/env python3
import sys

from api.errors import RateLimitError
from constants import (
    DEFAULT_SUMMARY_PATH,
    LANGUAGES_FILE,
    OUTPUT_DIR,
    REPOS_DIR,
    TOP_DIR_NAME,
    TOP_OUTPUT_DIR,
    TOP_REPOS_FILE,
    TOP_TITLE,
)
from main import run_collection
from utils.file_util import load_file
from utils.prune_output import prune_stale_collections
from utils.slug import language_slug
from utils.write_root_readme import write_root_readme


def main():
    failed = []
    try:
        failed += run_collection(TOP_REPOS_FILE, TOP_OUTPUT_DIR, TOP_TITLE)

        languages = load_file(LANGUAGES_FILE)
        print(f"Loaded {len(languages)} language(s) from {LANGUAGES_FILE}: {', '.join(languages)}")

        produced = {TOP_DIR_NAME}
        for language in languages:
            slug = language_slug(language)
            produced.add(f"top-{slug}")
            failed += run_collection(
                f"{REPOS_DIR}/top_{slug}.json",
                f"{OUTPUT_DIR}/top-{slug}",
                f"Top {language} Projects",
            )

        if failed:
            # Same reasoning as the per-repo prune: a run that lost repos is
            # not the one to decide a whole collection is obsolete.
            print(f"Skipping stale-collection cleanup: {len(failed)} repo(s) failed this run.")
        else:
            for dir_name in prune_stale_collections(OUTPUT_DIR, produced, prefix="top-"):
                print(f"Removed stale collection {dir_name}/ (no longer in {LANGUAGES_FILE})")
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
