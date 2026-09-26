import re

# Patterns for common secret formats that could accidentally appear in
# user-generated content (e.g. an issue title) and trip GitHub's push
# protection when copied verbatim into a generated file.
_SECRET_PATTERNS = [
    re.compile(r"gh[oprsu]_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
]


def sanitize_text(text):
    for pattern in _SECRET_PATTERNS:
        text = pattern.sub("[redacted]", text)
    return text
