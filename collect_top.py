#!/usr/bin/env python3
from main import run_collection
from utils.file_util import load_file

LANGUAGES_FILE = "repos/languages.json"


def main():
    run_collection("repos/top_repos.json", "top-projects", "top-projects/README.md", "Top Open-Source Projects")

    languages = load_file(LANGUAGES_FILE)

    for language in languages:
        slug = language.lower()
        run_collection(
            f"repos/top_{slug}.json",
            f"top-{slug}",
            f"top-{slug}/README.md",
            f"Top {language} Projects",
        )


if __name__ == "__main__":
    main()
