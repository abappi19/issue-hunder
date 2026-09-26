"""All tunable settings for this project in one place -- edit here."""

# GitHub API base URL
API_BASE_URL = "https://api.github.com"

# Concurrency for the ThreadPoolExecutor used by discover_repos.py's
# contributor-count lookups (core API, no secondary rate limit risk).
MAX_WORKERS = 10

# "Popular" repo bar, used both by discover_repos.py (auto-discovery) and
# check_new_repos.py (PR check on manually-added repos.json entries).
MIN_STARS = 10000
MIN_CONTRIBUTORS = 50

# discover_repos.py: how many top-starred candidates to pull per search,
# and how many of the qualifying ones to keep.
CANDIDATE_POOL_SIZE = 100
TOP_N = 20

# api/issues.py: how many recent unassigned issues to show per repo, and
# the size of the single request used to determine the count (fewer than
# this many results back means that's the exact count; exactly this many
# means the count is reported as "<RECENT_COUNT>+").
RECENT_COUNT = 5

# api/search_rate_limiter.py: pacing for the (now rare) Search API calls,
# e.g. discover_repos.py's candidate search. GitHub's documented primary
# limit is 30 calls/min; max_calls stays a safe margin under that. The
# secondary rate limit reacts to near-zero spacing between calls
# regardless of volume, hence min_interval.
SEARCH_MAX_CALLS = 25
SEARCH_PERIOD_SECONDS = 60
SEARCH_MIN_INTERVAL_SECONDS = 2

# Repo-list data files (see src/repos/)
REPOS_DIR = "src/repos"
REPOS_FILE = f"{REPOS_DIR}/repos.json"
LANGUAGES_FILE = f"{REPOS_DIR}/languages.json"
TOP_REPOS_FILE = f"{REPOS_DIR}/top_repos.json"

# main.py CLI defaults (the manually-curated repos.json collection)
OUTPUT_DIR = "output"
DEFAULT_OUTPUT_DIR = f"{OUTPUT_DIR}/projects"
DEFAULT_SUMMARY_PATH = "README.md"
DEFAULT_TITLE = "Issue Hunter"

# collect_top.py: the general (all-languages) top-repos collection
TOP_OUTPUT_DIR = f"{OUTPUT_DIR}/top-projects"
TOP_SUMMARY_PATH = f"{OUTPUT_DIR}/top-projects/README.md"
TOP_TITLE = "Top Open-Source Projects"

# utils/write_root_readme.py: markers bounding the section rewritten on
# every run, so a static header above them survives untouched.
README_START_MARKER = "<!-- AUTO-GENERATED:START -->"
README_END_MARKER = "<!-- AUTO-GENERATED:END -->"
