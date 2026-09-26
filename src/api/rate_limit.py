import threading
import time

from constants import SEARCH_MAX_CALLS, SEARCH_MIN_INTERVAL_SECONDS, SEARCH_PERIOD_SECONDS


class RateLimiter:
    """Thread-safe limiter: blocks callers so no more than `max_calls` occur
    within any `period` seconds, and (if set) enforces a minimum gap between
    any two consecutive calls -- GitHub's Search API secondary rate limit
    reacts to near-zero spacing between calls regardless of total volume,
    so pacing every call matters as much as the per-period ceiling."""

    def __init__(self, max_calls, period, min_interval=0):
        self.max_calls = max_calls
        self.period = period
        self.min_interval = min_interval
        self.lock = threading.Lock()
        self.calls = []
        self.last_call = None

    def acquire(self):
        with self.lock:
            now = time.monotonic()

            if self.min_interval and self.last_call is not None:
                elapsed = now - self.last_call
                if elapsed < self.min_interval:
                    time.sleep(self.min_interval - elapsed)
                    now = time.monotonic()

            self.calls = [t for t in self.calls if now - t < self.period]
            if len(self.calls) >= self.max_calls:
                sleep_time = self.period - (now - self.calls[0])
                if sleep_time > 0:
                    time.sleep(sleep_time)
                now = time.monotonic()
                self.calls = [t for t in self.calls if now - t < self.period]

            self.calls.append(now)
            self.last_call = now


# Shared by every caller that hits GitHub's Search API (search_repos.py's
# discovery search), so calls from different modules can't land back-to-back.
# A single process-wide instance is required -- the pacing only works if
# everyone shares it, which is why it lives beside the class rather than
# being constructed where it is used.
SEARCH_LIMITER = RateLimiter(
    max_calls=SEARCH_MAX_CALLS,
    period=SEARCH_PERIOD_SECONDS,
    min_interval=SEARCH_MIN_INTERVAL_SECONDS,
)
