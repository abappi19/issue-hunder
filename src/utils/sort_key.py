"""Unassigned counts are either an exact int, or a "<n>+" string when the
fetched page came back full and there are more issues behind it."""


def unassigned_value(value):
    """The number in a count, whichever of the two forms it takes."""
    if isinstance(value, int):
        return value
    return int(str(value).rstrip("+"))


def is_lower_bound(value):
    return not isinstance(value, int)


def unassigned_sort_key(value):
    """Order counts so a lower bound outranks the exact count it ties with --
    "100+" is at least 100 and probably more -- while two lower bounds still
    order by their numbers instead of collapsing into one undifferentiated
    clump at the top of the table."""
    return (unassigned_value(value), 1 if is_lower_bound(value) else 0)
