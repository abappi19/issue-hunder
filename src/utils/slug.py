import re

# Language names that a plain lowercase would turn into awkward or
# path-unfriendly filenames ("C++" -> "c++", "C#" -> "c#").
_CHAR_WORDS = {"+": "p", "#": "sharp"}


def language_slug(language):
    """Filename-safe slug for a language name, shared by the writer
    (discover_repos.py) and the reader (collect_top.py) of top_<slug>.json
    so the two can never disagree about where a list lives.

    "TypeScript" -> "typescript", "C++" -> "cpp", "C#" -> "csharp",
    "Jupyter Notebook" -> "jupyter-notebook"."""
    slug = language.lower()
    for char, word in _CHAR_WORDS.items():
        slug = slug.replace(char, word)
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")
