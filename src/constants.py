"""All tunable settings for this project in one place -- edit here."""

# GitHub API base URL
API_BASE_URL = "https://api.github.com"

# Concurrency for the ThreadPoolExecutor used by discover_repos.py's
# contributor-count lookups. Secondary rate limits do apply to the core API
# (a concurrency ceiling plus roughly 900 points/min, one point per GET), so
# this is the one burst in the codebase that could trip them -- raising it
# buys little and moves discovery toward that ceiling.
MAX_WORKERS = 10

# "Popular" repo bar, used both by discover_repos.py (auto-discovery) and
# check_new_repos.py (PR check on manually-added repos.json entries).
MIN_STARS = 10000
MIN_CONTRIBUTORS = 50

# discover_repos.py: how many top-starred candidates to pull per search,
# and how many of the qualifying ones to keep.
#
# Mind the budget here: the workflows authenticate with secrets.GITHUB_TOKEN,
# which is capped at 1,000 requests/hour *per repository* -- not the 5,000 a
# personal token gets. Discovery costs 1 + CANDIDATE_POOL_SIZE calls for each
# entry in languages.json (plus one more pass for the all-languages list), so
# every language added is ~101 calls against that 1,000. Around nine languages
# the hourly cap is in reach and discovery starts failing partway through.
CANDIDATE_POOL_SIZE = 100
TOP_N = 20

# discover_repos.py: refuse to overwrite an existing repo list with one that
# has shrunk below this fraction of it. A partial result usually means the run
# hit trouble midway rather than that the ecosystem moved, and the overwritten
# file is what every later collection run reads.
MIN_DISCOVERY_RATIO = 0.5

# api/issues.py: how many recent unassigned issues to pull per repo -- the one
# number controlling page size, with no second knob behind it. Every issue on
# that page is both counted and listed on the repo's own page: one request
# costs the same whatever the page size, so fetching fewer would only throw
# away issues a contributor could have picked up. 100 is the endpoint maximum.
RECENT_COUNT = 100

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
CURATED_DIR_NAME = "projects"
DEFAULT_OUTPUT_DIR = f"{OUTPUT_DIR}/{CURATED_DIR_NAME}"
DEFAULT_SUMMARY_PATH = "README.md"
DEFAULT_TITLE = "Tracked Projects"

# collect_top.py: the general (all-languages) top-repos collection
TOP_DIR_NAME = "top-projects"
TOP_OUTPUT_DIR = f"{OUTPUT_DIR}/{TOP_DIR_NAME}"
TOP_TITLE = "Top Open-Source Projects"

# Every collection drops one of these beside the pages it writes, recording
# what it produced. The root README links every project in every collection,
# but two workflows on different schedules fill those collections, so the
# rebuild reads these instead of whatever one run happens to hold in memory.
INDEX_FILENAME = "index.json"

# utils/write_root_readme.py: markers bounding the section rewritten on
# every run, so a static header above them survives untouched.
README_START_MARKER = "<!-- AUTO-GENERATED:START -->"
README_END_MARKER = "<!-- AUTO-GENERATED:END -->"
