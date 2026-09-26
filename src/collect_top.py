#!/usr/bin/env python3
from main import run_collection
from utils.file_util import load_file

LANGUAGES_FILE = "src/repos/languages.json"


def main():
    run_collection(
        "src/repos/top_repos.json",
        "output/top-projects",
        "output/top-projects/README.md",
        "Top Open-Source Projects",
    )

    languages = load_file(LANGUAGES_FILE)

    for language in languages:
        slug = language.lower()
        run_collection(
            f"src/repos/top_{slug}.json",
            f"output/top-{slug}",
            f"output/top-{slug}/README.md",
            f"Top {language} Projects",
        )


if __name__ == "__main__":
    main()
