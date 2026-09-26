def unassigned_sort_key(value):
    """Unassigned counts are an int, or the string "100+" when a repo has
    a full page of results -- treat the latter as larger than any exact
    count."""
    return value if isinstance(value, int) else float("inf")
