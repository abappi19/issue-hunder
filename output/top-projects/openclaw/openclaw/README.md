# openclaw/openclaw

Generated: 2026-09-26T18:42:16.002755+00:00

- Unassigned: 45+
- [View all unassigned issues](https://github.com/openclaw/openclaw/issues?q=is%3Aissue%20is%3Aopen%20no%3Aassignee)

Most recently opened:

| Issue | Comments |
|---|---|
| [#159094 [Bug]: 2026.9.6 Gateway owns state-lifecycle lease but internal workers report another OpenClaw process owns state-lifecycle](https://github.com/openclaw/openclaw/issues/159094) | 1 |
| [#159089 [Bug]: contextPruning (cache-ttl) never prunes for OpenAI-compatible providers under a custom provider id](https://github.com/openclaw/openclaw/issues/159089) | 2 |
| [#159080 [Bug]: Runtime-bound LINE conversations fail with AgentSelectionRequiredError on multi-agent installs](https://github.com/openclaw/openclaw/issues/159080) | 3 |
| [#159075 [Bug]: Memory keyword search drops English terms written inside Chinese text without spaces](https://github.com/openclaw/openclaw/issues/159075) | 1 |
| [#159070 [Feature]: Support ordered fallback chains for utilityModel](https://github.com/openclaw/openclaw/issues/159070) | 1 |
| [#159059 Direct subagent result mirror written between a wake's keyed user and its reply triggers 'keyed user is outside the current turn' (2026.9.6)](https://github.com/openclaw/openclaw/issues/159059) | 2 |
| [#159058 Feature request: ACP-only agent identities (deny native/embedded runs, preserve ACP spawn)](https://github.com/openclaw/openclaw/issues/159058) | 1 |
| [#159057 ACP: task-maintenance cleanup re-ensures a completed oneshot, creating a duplicate no-prompt runtime session](https://github.com/openclaw/openclaw/issues/159057) | 2 |
| [#159048 [Bug]: Linux companion Control UI pages fail with `Importing a module script failed` against 2026.9.6 Gateway](https://github.com/openclaw/openclaw/issues/159048) | 3 |
| [#159043 apple-fm host model: tool schemas with literal or patternProperties crash the bundled AppleFoundationModels bridge](https://github.com/openclaw/openclaw/issues/159043) | 1 |
| [#159029 config validate and setup commands call an unreadable config invalid and suggest doctor --fix](https://github.com/openclaw/openclaw/issues/159029) | 1 |
| [#159028 [Bug]: Talk on Watch fails on Start with AVAudioSession '!ses' (561210739) / avfaudio -308 before any Gateway call (watchOS 26.6)](https://github.com/openclaw/openclaw/issues/159028) | 1 |
| [#159025 [Feature]: optional pluggable LLM noise gate on the promotion apply path (fail-open)](https://github.com/openclaw/openclaw/issues/159025) | 1 |
| [#159024 [Feature]: configurable auto-recall minimum score and shared recall groups](https://github.com/openclaw/openclaw/issues/159024) | 1 |
| [#159022 perf(state): cache agent database path identity with stat revalidation instead of realpath walk on every call](https://github.com/openclaw/openclaw/issues/159022) | 1 |
| [#159021 perf(agents): coalesce queued file writer line appends into a single append when no byte cap is configured](https://github.com/openclaw/openclaw/issues/159021) | 2 |
| [#159020 perf(infra): default PRAGMA synchronous to NORMAL for WAL databases (keep FULL for rollback journal)](https://github.com/openclaw/openclaw/issues/159020) | 1 |
| [#159019 perf(memory-lancedb): cache embeddings on the memory_store write path (dedup-check) while keeping recall uncached](https://github.com/openclaw/openclaw/issues/159019) | 1 |
| [#159018 [Bug]: chat history: stale older-page flights land after the reader leaves the boundary, and the loading flag can stick](https://github.com/openclaw/openclaw/issues/159018) | 2 |
| [#159007 Deleted agents retain model and auth database readers](https://github.com/openclaw/openclaw/issues/159007) | 1 |
| [#159005 Update failure: managed-service-preflight (2026.9.4)](https://github.com/openclaw/openclaw/issues/159005) | 1 |
| [#159001 Config-wide Gateway metadata triggers redundant inbound plugin registration](https://github.com/openclaw/openclaw/issues/159001) | 1 |
| [#158997 Process ownership fixture races zombie reaping before PID reuse](https://github.com/openclaw/openclaw/issues/158997) | 2 |
| [#158991 [Bug]: Update on non-default OPENCLAW_STATE_DIR leaves gateway down - 'service management skipped' with no restart fallback (Windows)](https://github.com/openclaw/openclaw/issues/158991) | 1 |
| [#158990 [Bug]: Gateway temp log truncated on every CLI/gateway start destroys crash forensics (Windows)](https://github.com/openclaw/openclaw/issues/158990) | 1 |
| [#158981 Model catalog inventories remain retained across neutral configuration reloads](https://github.com/openclaw/openclaw/issues/158981) | 1 |
| [#158977 Update failure: reconcile:abandoned (2026.9.6)](https://github.com/openclaw/openclaw/issues/158977) | 1 |
| [#158969 cron: startup catch-up write failure leaves the scheduler unarmed](https://github.com/openclaw/openclaw/issues/158969) | 2 |
| [#158968 secrets: rotating a value without --kind converts protected entries to readable env entries](https://github.com/openclaw/openclaw/issues/158968) | 1 |
| [#158967 media: attachment TTL cleanup deletes inbound files still referenced by transcripts](https://github.com/openclaw/openclaw/issues/158967) | 1 |
| [#158966 browser: credentialed CDP WebSocket URLs reach model-facing tab results](https://github.com/openclaw/openclaw/issues/158966) | 0 |
| [#158957 Gateway fixture startup times out under concurrent full-suite load](https://github.com/openclaw/openclaw/issues/158957) | 1 |
| [#158956 Update failure: reconcile:abandoned (2026.9.5)](https://github.com/openclaw/openclaw/issues/158956) | 1 |
| [#158952 Windows regression: gateway startup increased from ~3s to 90–337s after upgrading 2026.7.1-2 → 2026.9.6](https://github.com/openclaw/openclaw/issues/158952) | 1 |
| [#158951 [Bug]: Gateway restart permanently breaks MCP for running CLI agent sessions (401 AUTH_HEADER_REJECTED, --strict-mcp-config cannot recover)](https://github.com/openclaw/openclaw/issues/158951) | 1 |
| [#158947 [Feature]: Separate operator-owned heartbeat scratch from model notes, and keep scratch history](https://github.com/openclaw/openclaw/issues/158947) | 1 |
| [#158946 [Bug]: memory-core watcher reindexes on deleted/renamed non-matching paths, and each pass walks every extraPaths root in full](https://github.com/openclaw/openclaw/issues/158946) | 2 |
| [#158945 [Bug]: sessions_spawn thread:true fails from claude-cli sessions while threadbound-subagent-spawn is advertised](https://github.com/openclaw/openclaw/issues/158945) | 2 |
| [#158944 [Bug]: Expired (and cancelled) plugin approvals render as "Denied" in native channel approval cards](https://github.com/openclaw/openclaw/issues/158944) | 2 |
| [#158936 [Bug]: macOS app readiness watchdog SIGTERMs a slow-starting gateway, causing a restart loop until the app is quit](https://github.com/openclaw/openclaw/issues/158936) | 3 |
| [#158924 [Bug]: Control UI sidebar agent card renders image avatar as a cropped sliver (image box overflows its 28x28 container)](https://github.com/openclaw/openclaw/issues/158924) | 1 |
| [#158922 claude-cli models report `available: false` after Gateway restart on main, hiding the Control UI Effort picker (regression after #157459)](https://github.com/openclaw/openclaw/issues/158922) | 2 |
| [#158921 [Feature]: Native contributor admission, lifecycle and stop contract](https://github.com/openclaw/openclaw/issues/158921) | 1 |
| [#158920 [Feature]: Supported recovery coverage for opaque Workboard and native-harness state](https://github.com/openclaw/openclaw/issues/158920) | 1 |
| [#158917 [Bug]: memory_search intermittently times out at 30s, returns late keyword-only partial results on Gemini](https://github.com/openclaw/openclaw/issues/158917) | 1 |
