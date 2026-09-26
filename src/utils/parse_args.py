import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repos", default="src/repos/repos.json", help="Repo list JSON file")
    parser.add_argument("--output", default="output/projects", help="Per-project README output dir")
    parser.add_argument("--summary", default="README.md", help="Summary README path")
    parser.add_argument("--title", default="Issue Hunter", help="Summary README title")
    return parser.parse_args()
