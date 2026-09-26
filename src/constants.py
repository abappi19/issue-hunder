"""All tunable settings for this project in one place -- edit here."""

# GitHub API base URL
API_BASE_URL = "https://api.github.com"

# "Popular" repo bar, used both by discover_repos.py (auto-discovery) and
# check_new_repos.py (PR check on manually-added repos.json entries).
#
# Stars are the whole bar. A contributor floor used to sit beside this, but it
# cost a request per candidate -- the only per-candidate request discovery
# made, and by far the largest draw on the hourly budget -- to rule out the
# one-person project, which a five-figure star count already rules out.
MIN_STARS = 10000

# discover_repos.py: how far down the star ranking to look, and how many of
# what comes back to keep. The pool is deliberately far wider than TOP_N so
# that dropping repos closed to contributions still leaves plenty above the
# cut. 100 is the Search API's page maximum, so widening it past here would
# start costing a second request for no benefit.
CANDIDATE_POOL_SIZE = 100
TOP_N = 20

# A note on budget, since this is where it used to be spent: the workflows
# authenticate with secrets.GITHUB_TOKEN, capped at 1,000 requests/hour *per
# repository* -- not the 5,000 a personal token gets. Discovery no longer
# touches that allowance at all. It makes one Search API request per
# collection, and search is metered separately (30/min), so the hourly cap now
# constrains only the collection runs, at one request per repo listed.

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

# Repo-list data files (see data/) -- both the hand-maintained inputs
# (repos.json, topics.json) and the lists discovery regenerates (top_*.json).
# Data, not source, so it sits beside output/ at the repo root rather than
# under src/.
REPOS_DIR = "data"
REPOS_FILE = f"{REPOS_DIR}/repos.json"
TOP_REPOS_FILE = f"{REPOS_DIR}/top_repos.json"

# Per-ecosystem collections, as {"github-topic": "Display Title"} in file
# order. Topics rather than languages: sorting `language:TypeScript` by stars
# returns tutorials and awesome-lists (freeCodeCamp, developer-roadmap) far
# above anything with a contributable issue, while `topic:typescript` returns
# the actual tools and libraries (vscode, langchain, deno, angular). Topics
# also express ecosystems a language cannot -- Next.js, Expo, React Native --
# and reach libraries that rank too low by raw stars to survive a
# language-wide cut, such as zustand under state-management.
TOPICS_FILE = f"{REPOS_DIR}/topics.json"

# A topic search draws from a far smaller pool than a language one, so it
# needs a lower bar to fill a list: at 10,000 stars `topic:expo` matches three
# repos in total, against sixty-three at this figure. It costs the bigger
# topics nothing -- the top 20 kept from `topic:typescript` clear 10,000 stars
# regardless of where the floor sits.
TOPIC_MIN_STARS = 1000

# main.py CLI defaults (the manually-curated repos.json collection)
OUTPUT_DIR = "output"
CURATED_DIR_NAME = "projects"
DEFAULT_OUTPUT_DIR = f"{OUTPUT_DIR}/{CURATED_DIR_NAME}"
DEFAULT_SUMMARY_PATH = "README.md"
DEFAULT_TITLE = "Tracked Projects"

# collect_top.py: the general top-repos collection, scoped to no topic
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
