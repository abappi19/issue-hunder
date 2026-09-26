# headroomlabs-ai/headroom

Generated: 2026-09-26T18:42:31.281046+00:00

- Unassigned: 41+
- [View all unassigned issues](https://github.com/headroomlabs-ai/headroom/issues?q=is%3Aissue%20is%3Aopen%20no%3Aassignee)

Most recently opened:

| Issue | Comments |
|---|---|
| [#3798 [BUG] Vertex us multi-region is forwarded to incorrect upstream hostname](https://github.com/headroomlabs-ai/headroom/issues/3798) | 0 |
| [#3777 HEADROOM_OFFLINE=1 does not prevent the HuggingFace tokenizer download](https://github.com/headroomlabs-ai/headroom/issues/3777) | 0 |
| [#3775 HTMLExtractor replaces tool results with unrecoverable output: CompressionStrategy.HTML is missing from LOSSY_UNMARKED_STRATEGIES](https://github.com/headroomlabs-ai/headroom/issues/3775) | 0 |
| [#3768 [FEATURE] Pass through `safeguards` request field and `safeguard_results` response field](https://github.com/headroomlabs-ai/headroom/issues/3768) | 0 |
| [#3760 [BUG] SmartCrusher does nothing for arrays at/above min_items_to_analyze when no rows need trimming (same payload compresses ~99% via either bypass)](https://github.com/headroomlabs-ai/headroom/issues/3760) | 1 |
| [#3749 [BUG] Windows Codex proxy unavailability: sanitized 0.32.1 incident logs and limited 0.37.0 follow-up](https://github.com/headroomlabs-ai/headroom/issues/3749) | 0 |
| [#3732 Unknown model silently priced at the GPT-4o tier, so cost tracking and budget enforcement act on fabricated numbers](https://github.com/headroomlabs-ai/headroom/issues/3732) | 1 |
| [#3716 [BUG] VS Code Copilot requests are not routed through Headroom proxy despite successful wrap vscode setup](https://github.com/headroomlabs-ai/headroom/issues/3716) | 0 |
| [#3711 [BUG] Kompress/ONNX stage takes ~70s on a mixed prose+JSON tool output, exhausting the 30s budget and quarantining all compression (0.38.0)](https://github.com/headroomlabs-ai/headroom/issues/3711) | 1 |
| [#3702 [FEATURE] Support Github Copilot App](https://github.com/headroomlabs-ai/headroom/issues/3702) | 0 |
| [#3698 learn/memory writers: LF pin has no regression guard, and the same bug is live in memory writers](https://github.com/headroomlabs-ai/headroom/issues/3698) | 0 |
| [#3697 smart-crusher: remove dead crush_object clone; revisit the bundled whitespace guard from #3648](https://github.com/headroomlabs-ai/headroom/issues/3697) | 1 |
| [#3690 [FEATURE] Optional Jev-backed semantic policy for ModelRouter](https://github.com/headroomlabs-ai/headroom/issues/3690) | 2 |
| [#3686 plugin(opencode): wrapSpawn does not set windowsHide on Windows — visible cmd.exe windows pop up for every MCP server](https://github.com/headroomlabs-ai/headroom/issues/3686) | 0 |
| [#3676 [BUG] Memory tools are injected into requests that declare no tools, turning text completions into unserviceable tool calls](https://github.com/headroomlabs-ai/headroom/issues/3676) | 0 |
| [#3673 [BUG] Kompress deletes a whole record from single-line JSON, producing valid but incomplete JSON](https://github.com/headroomlabs-ai/headroom/issues/3673) | 1 |
| [#3669 Opencode plugin: make a version that works with OpenCode v2](https://github.com/headroomlabs-ai/headroom/issues/3669) | 0 |
| [#3667 Wire-contract guard relocates non-text blocks into top-level `system`, causing 400 on every affected request](https://github.com/headroomlabs-ai/headroom/issues/3667) | 2 |
| [#3653 compression_executor leaks a worker thread + fd on every quarantine event; never released after timeout (persists in 0.37.0)](https://github.com/headroomlabs-ai/headroom/issues/3653) | 1 |
| [#3652 [BUG] Columnar command output (ls -la, git status) classifies as PLAIN_TEXT and loses fields to Kompress — Bash missing from DEFAULT_EXCLUDE_TOOLS](https://github.com/headroomlabs-ai/headroom/issues/3652) | 1 |
| [#3649 Docker image: ast-grep binary missing from runtime stage (whitelist COPY) — --intercept-tool-results fails to start](https://github.com/headroomlabs-ai/headroom/issues/3649) | 0 |
| [#3633 [BUG] opencode plugin routes ALL HTTP traffic through the proxy — breaks built-in WebFetch and every Node child process (npx/npm/Node MCPs)](https://github.com/headroomlabs-ai/headroom/issues/3633) | 0 |
| [#3608 [BUG] Mixed-content routing can lose the parent HTML type](https://github.com/headroomlabs-ai/headroom/issues/3608) | 0 |
| [#3604 Persistent-service crash loop on macOS 26 (Darwin 27): PyTorch MPS backend aborts on IOGPUMetalCommandBuffer during embedder/kompress model load](https://github.com/headroomlabs-ai/headroom/issues/3604) | 0 |
| [#3598 [FEATURE]](https://github.com/headroomlabs-ai/headroom/issues/3598) | 0 |
| [#3597 headroom wrap sets X-Headroom-Project but the CCR resolver reads x-headroom-project-id/x-headroom-cwd — the supported launcher doesn't satisfy its own resolver](https://github.com/headroomlabs-ai/headroom/issues/3597) | 0 |
| [#3591 headroom_retrieve reports item count in a field named original_tokens](https://github.com/headroomlabs-ai/headroom/issues/3591) | 1 |
| [#3590 Compressing small tool results destroys structure silently; consider excluding shell/file reads by default](https://github.com/headroomlabs-ai/headroom/issues/3590) | 0 |
| [#3589 [BUG] Codex Desktop voice chat fails with 403 when using Headroom persistent proxy](https://github.com/headroomlabs-ai/headroom/issues/3589) | 0 |
| [#3588 Proxy daemon keeps stale env; no way to restart it from inside a session](https://github.com/headroomlabs-ai/headroom/issues/3588) | 0 |
| [#3587 CCR buffered path (stream:false) fires on 71% of opus turns after #3071 and redeems zero retrievals — TTFT becomes the whole generation (0.37.0)](https://github.com/headroomlabs-ai/headroom/issues/3587) | 1 |
| [#3573 [DOCS] --memory context injection is silently skipped in --mode cache](https://github.com/headroomlabs-ai/headroom/issues/3573) | 0 |
| [#3571 [BUILD] Migrate Headroom local and CI Rust to 1.98.1](https://github.com/headroomlabs-ai/headroom/issues/3571) | 0 |
| [#3569 [BUG] Image v0.37.0 switches to `USER root`; with `--userns=keep-id` all newly created files in bind mounts are owned by a subordinate UID](https://github.com/headroomlabs-ai/headroom/issues/3569) | 4 |
| [#3563 [BUG] CCR recovery JSON re-offloaded through Codex functions.exec wrapper; named retrieval exemption passes](https://github.com/headroomlabs-ai/headroom/issues/3563) | 1 |
| [#3561 [BUG] No content compressor runs in proxy mode on the Anthropic /v1/messages path (0.30.0 through 0.37.0)](https://github.com/headroomlabs-ai/headroom/issues/3561) | 2 |
| [#3560 [BUG] CCR makes Jira MCP issue descriptions inaccessible in GitHub Copilot](https://github.com/headroomlabs-ai/headroom/issues/3560) | 0 |
| [#3554 [BUG] Prompt caching gate uses wrong LiteLLM API](https://github.com/headroomlabs-ai/headroom/issues/3554) | 1 |
| [#3549 [BUG] Shared ContentRouter request state can be overwritten by concurrent compression requests](https://github.com/headroomlabs-ai/headroom/issues/3549) | 0 |
| [#3545 [BUG] Search/grep compressor fuses matches into single lines, manufacturing false line↔content associations](https://github.com/headroomlabs-ai/headroom/issues/3545) | 2 |
| [#3544 [BUG] CCR markers spliced into small fields invalidate JSON containers and inject a headroom_retrieve tool non-MCP clients cannot execute](https://github.com/headroomlabs-ai/headroom/issues/3544) | 0 |
