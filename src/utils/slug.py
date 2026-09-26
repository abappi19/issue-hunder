import re

# Names a plain lowercase would turn into awkward or path-unfriendly
# filenames ("C++" -> "c++", "C#" -> "c#").
_CHAR_WORDS = {"+": "p", "#": "sharp"}


def to_slug(name):
    """Filename-safe slug, shared by the writer (discover_repos.py) and the
    reader (collect_top.py) of top_<slug>.json so the two can never disagree
    about where a list lives.

    GitHub topics arrive as slugs already ("react-native"), so this is mostly
    a guard against a hand-edited topics.json: "C++" -> "cpp", "C#" ->
    "csharp", "State Management" -> "state-management"."""
    slug = name.lower()
    for char, word in _CHAR_WORDS.items():
        slug = slug.replace(char, word)
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")
