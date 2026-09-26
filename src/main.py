#!/usr/bin/env python3
"""Entry point for the curated collection in data/repos.json."""

import sys

from api.errors import RateLimitError
from collect import run_collection
from readme.root import write_root_readme
from utils.parse_args import parse_args


def main():
    args = parse_args()
    try:
        failed = run_collection(args.repos, args.output, args.title)
    except RateLimitError as e:
        print(f"Aborted: {e}", file=sys.stderr)
        sys.exit(1)

    # Rebuilt from every collection's index, so the front page keeps linking
    # the top-repo projects this run never touched.
    write_root_readme(args.summary)
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
