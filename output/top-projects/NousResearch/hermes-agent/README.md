# NousResearch/hermes-agent

Generated: 2026-10-01T10:45:56.796561+00:00

- Unassigned: 26+
- [View all unassigned issues](https://github.com/NousResearch/hermes-agent/issues?q=is%3Aissue%20is%3Aopen%20no%3Aassignee)

Most recently opened:

| Issue | Comments |
|---|---|
| [#130295 MCP OAuth: `mcp add` cannot override the CIMD client-metadata URL for strict authorization servers](https://github.com/NousResearch/hermes-agent/issues/130295) | 0 |
| [#130294 [Bug]: Windows install fails with "failed to remove directory *.data" (os error 2)](https://github.com/NousResearch/hermes-agent/issues/130294) | 1 |
| [#130289 [Bug]: gemini-2.5-* returns empty content under a large tool schema — unbounded thinking starves the answer](https://github.com/NousResearch/hermes-agent/issues/130289) | 0 |
| [#130287 [Bug]: google-workspace OAuth hangs — REDIRECT_URI uses port 1, which browsers refuse to navigate to](https://github.com/NousResearch/hermes-agent/issues/130287) | 0 |
| [#130282 [Bug]: Desktop open tabs do not follow the backend across devices](https://github.com/NousResearch/hermes-agent/issues/130282) | 0 |
| [#130277 [Bug]: Desktop can't connect to a remote gateway since #127201: loopback renderer origin fails /api/ws Origin check](https://github.com/NousResearch/hermes-agent/issues/130277) | 0 |
| [#130272 [Bug]: approval timeout / missing approval channel is reported to the agent as "User denied this command"](https://github.com/NousResearch/hermes-agent/issues/130272) | 1 |
| [#130261 [Bug]: `_LIVE_CACHE_BY_CREDENTIAL` in `plugins/image_gen/xai` is keyed by an api_key fingerprint and never evicted, so each rotated key leaves a permanent catalog entry](https://github.com/NousResearch/hermes-agent/issues/130261) | 0 |
| [#130260 [Bug]: Desktop @mention gives a same-gateway bot a connection-qualified message_agent target the sender's own gateway can't resolve](https://github.com/NousResearch/hermes-agent/issues/130260) | 0 |
| [#130257 [Bug]: TUI guide promises identical CLI behavior despite an explicit snapshot-restore restriction](https://github.com/NousResearch/hermes-agent/issues/130257) | 0 |
| [#130256 [Bug]: copilot_auth `_jwt_cache` / `_exchange_failure_cache` / `_exchange_locks` are keyed by a token fingerprint and only ever popped on a repeat success, so rotated-away tokens are retained forever](https://github.com/NousResearch/hermes-agent/issues/130256) | 1 |
| [#130249 [Bug]: `_codex_quota_probe_cache` in `hermes_cli/auth_codex.py` is keyed by a hash of the access token and never evicted, so every Codex token rotation leaves a permanent entry](https://github.com/NousResearch/hermes-agent/issues/130249) | 0 |
| [#130246 [Bug]: `_codex_oauth_context_cache` / `_codex_oauth_max_context_cache` are keyed by a hash of the access token and never pruned, so every token rotation leaks two permanent entries](https://github.com/NousResearch/hermes-agent/issues/130246) | 0 |
| [#130244 [Bug]: Profile delete still hits WinError 32 on logs/.__agent.lock when a multiplexed gateway holds the handlers (residual gap from #112538)](https://github.com/NousResearch/hermes-agent/issues/130244) | 0 |
| [#130243 [Bug]: `_runtime_cache` in `agent/moa_loop.py` is never evicted, so every resolved (profile, provider, model) runtime — including its resolved api_key — is retained for the life of the process](https://github.com/NousResearch/hermes-agent/issues/130243) | 0 |
| [#130242 Windows: PM file operations fail on paths over 260 characters (copy, walk, digest, delete)](https://github.com/NousResearch/hermes-agent/issues/130242) | 0 |
| [#130241 [Bug]: `_endpoint_model_metadata_cache` is never pruned, so every rotated credential leaves a permanent entry](https://github.com/NousResearch/hermes-agent/issues/130241) | 0 |
| [#130239 [Bug]: Kanban block-loop breaker can't tell a supervisor re-park from a claim loop — parks get poisoned, then lifted through park-blind paths](https://github.com/NousResearch/hermes-agent/issues/130239) | 0 |
| [#130232 Windows: plugin enable fails when PM copies the bundled Python tree past MAX_PATH (WinError 3)](https://github.com/NousResearch/hermes-agent/issues/130232) | 0 |
| [#130231 [Bug]: Rejected terminal/execute_code approval outcomes lost before async delegation summaries](https://github.com/NousResearch/hermes-agent/issues/130231) | 0 |
| [#130227 [Bug]: Desktop preview replaces whole page with "Server nicht gefunden" when a blocked subframe (ad iframe) fails to load](https://github.com/NousResearch/hermes-agent/issues/130227) | 0 |
| [#130226 Async-delegation completions never wake the parent on api_server sessions (personal gateway UX gap)](https://github.com/NousResearch/hermes-agent/issues/130226) | 1 |
| [#130213 [Feature] Desktop image lightbox: optional warm viewing mode (Night Shift-like)](https://github.com/NousResearch/hermes-agent/issues/130213) | 0 |
| [#130208 Plugin discovery races toolset registry iteration: 'dictionary changed size during iteration' aborts plugin registration (not just a false warning)](https://github.com/NousResearch/hermes-agent/issues/130208) | 0 |
| [#130207 [Bug]: Terminal batch timeout self-aborts via a soft interrupt(message) — system stop is booked as interrupted_by_user and shown as "Operation interrupted."](https://github.com/NousResearch/hermes-agent/issues/130207) | 0 |
| [#130197 [Feature]: Profile-level heartbeat that persists across sessions](https://github.com/NousResearch/hermes-agent/issues/130197) | 1 |
