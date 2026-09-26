import json
import os

from constants import CURATED_DIR_NAME, INDEX_FILENAME, TOP_DIR_NAME


def write_collection_index(output_dir, title, generated_at, summaries):
    """Record what a collection run produced, next to the pages it wrote.

    The root README lists every project across every collection, but the
    collections are filled by two workflows on different schedules, so
    neither run has the whole picture in memory. Each one leaves its result
    here instead, and the root README is rebuilt from all the indexes on
    disk -- no repo is re-fetched just to be linked."""
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, INDEX_FILENAME), "w") as f:
        json.dump(
            {"title": title, "generated_at": generated_at, "repos": summaries},
            f,
            indent=2,
        )
        f.write("\n")


def _section_order(dir_name):
    """Curated picks first, then the general top list, then the per-topic
    lists alphabetically."""
    if dir_name == CURATED_DIR_NAME:
        return (0, dir_name)
    if dir_name == TOP_DIR_NAME:
        return (1, dir_name)
    return (2, dir_name)


def read_collection_indexes(output_dir):
    """Every collection index under `output_dir`, in display order.

    Yields (dir_name, index) pairs. A collection whose index is missing or
    unreadable is skipped rather than failing the rebuild: a half-written
    output tree should still produce a README for the parts that are fine."""
    if not os.path.isdir(output_dir):
        return []

    found = []
    for dir_name in os.listdir(output_dir):
        path = os.path.join(output_dir, dir_name, INDEX_FILENAME)
        if not os.path.isfile(path):
            continue
        try:
            with open(path) as f:
                found.append((dir_name, json.load(f)))
        except (json.JSONDecodeError, OSError):
            continue

    found.sort(key=lambda pair: _section_order(pair[0]))
    return found
