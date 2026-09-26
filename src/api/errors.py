class FetchError(Exception):
    """A GitHub API request came back with an unusable response."""


class RateLimitError(FetchError):
    """A request was rejected by a primary or secondary rate limit.

    Kept distinct from a plain FetchError because the two call for opposite
    responses: a 404 on one repo is survivable and the run should carry on,
    while a rate limit means every subsequent call is likely to fail too, so
    the caller must stop rather than keep hammering (and must not persist
    whatever partial result it has collected so far)."""


def check_rate_limited(repo, resp):
    """Raise RateLimitError if `resp` is a rate-limit rejection.

    GitHub signals the primary limit with 403 plus X-RateLimit-Remaining: 0,
    and the secondary limit with 403 or 429 plus a "rate limit" message -- a
    bare 403 otherwise just means forbidden (blocked or DMCA'd repo), which
    is not a rate limit and must not be treated as one."""
    if resp.status_code not in (403, 429):
        return

    remaining = resp.headers.get("X-RateLimit-Remaining")
    body = resp.text[:200]
    if resp.status_code == 429 or remaining == "0" or "rate limit" in body.lower():
        retry_after = resp.headers.get("Retry-After")
        detail = f" (Retry-After: {retry_after}s)" if retry_after else ""
        raise RateLimitError(f"{repo}: {resp.status_code} rate limited{detail} {body}")
