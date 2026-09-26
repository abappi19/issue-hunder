from utils.rate_limiter import RateLimiter

# Shared by every caller that hits GitHub's Search API (issues.py's rare
# large-repo count fallback, search_repos.py's discovery search), so calls
# from different modules can't land back-to-back. A single process-wide
# instance is required -- the pacing only works if everyone shares it.
SEARCH_LIMITER = RateLimiter(max_calls=25, period=60, min_interval=2)
