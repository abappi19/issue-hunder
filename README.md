# Issue Hunter

Issue Hunter tracks **unassigned, open issues** across popular open-source
projects, so contributors can quickly find real work to pick up.

A GitHub Action re-scans every tracked repository on a schedule and rebuilds
the table below with the current unassigned-issue count for each one. Click
a repo's count to jump straight to its live, filtered issue list on GitHub.
Each repo also gets its own page under `output/projects/<owner>/<repo>/README.md`
with a few of the most recently opened unassigned issues.

## Want to add a repo?

Open a pull request adding `"owner/repo"` to `src/repos/repos.json`. A CI
check automatically verifies the repo meets our popularity bar (currently
at least 10,000 stars and 50+ contributors) before it
can be merged.

<!-- AUTO-GENERATED:START -->
<!-- AUTO-GENERATED:END -->
