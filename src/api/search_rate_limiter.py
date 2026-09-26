from constants import SEARCH_MAX_CALLS, SEARCH_MIN_INTERVAL_SECONDS, SEARCH_PERIOD_SECONDS
from utils.rate_limiter import RateLimiter

# Shared by every caller that hits GitHub's Search API (search_repos.py's
# discovery search), so calls from different modules can't land back-to-back.
# A single process-wide instance is required -- the pacing only works if
# everyone shares it.
SEARCH_LIMITER = RateLimiter(
    max_calls=SEARCH_MAX_CALLS,
    period=SEARCH_PERIOD_SECONDS,
    min_interval=SEARCH_MIN_INTERVAL_SECONDS,
)
