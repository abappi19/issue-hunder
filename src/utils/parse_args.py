import argparse

from constants import DEFAULT_OUTPUT_DIR, DEFAULT_SUMMARY_PATH, DEFAULT_TITLE, REPOS_FILE


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repos", default=REPOS_FILE, help="Repo list JSON file")
    parser.add_argument("--output", default=DEFAULT_OUTPUT_DIR, help="Per-project README output dir")
    parser.add_argument("--summary", default=DEFAULT_SUMMARY_PATH, help="Summary README path")
    parser.add_argument("--title", default=DEFAULT_TITLE, help="Summary README title")
    return parser.parse_args()
