# headroomlabs-ai/headroom

Generated: 2026-10-03T09:42:38.239543+00:00

- Unassigned: 34+
- [View all unassigned issues](https://github.com/headroomlabs-ai/headroom/issues?q=is%3Aissue%20is%3Aopen%20no%3Aassignee)

Most recently opened:

| Issue | Comments |
|---|---|
| [#3943 [BUG] LiteLLM backend maps upstream 400 BadRequestError to 500, breaking client retry-on-400 fallbacks](https://github.com/headroomlabs-ai/headroom/issues/3943) | 0 |
| [#3937 [BUG] Responses (Codex) compression restarts the Kompress deadline per unit, so a timed-out request keeps running inference and quarantines the requests behind it](https://github.com/headroomlabs-ai/headroom/issues/3937) | 0 |
| [#3935 [BUG] HEADROOM_COMPRESS_USER_MESSAGES=0 is ignored under the default `coding` profile, so user-message compression cannot be turned off](https://github.com/headroomlabs-ai/headroom/issues/3935) | 0 |
| [#3933 [BUG] Prefix tracker loses its lineage when Claude Code replaces a trailing role:"system" reminder, so the provider prompt cache is re-written every turn](https://github.com/headroomlabs-ai/headroom/issues/3933) | 0 |
| [#3931 [BUG] One timed-out compression worker quarantines ALL compression while the rest of the pool is idle](https://github.com/headroomlabs-ai/headroom/issues/3931) | 0 |
| [#3929 [BUG] Response cache stores an error delivered as HTTP 200 and replays it for the full TTL](https://github.com/headroomlabs-ai/headroom/issues/3929) | 0 |
| [#3927 [BUG] learn: a failed codex-cli analysis reports Codex's banner and our system prompt, never the reason](https://github.com/headroomlabs-ai/headroom/issues/3927) | 0 |
| [#3925 [BUG] learn: the user's Claude Code hooks run inside the claude-cli analysis, and a blocking Stop hook replaces the analysis](https://github.com/headroomlabs-ai/headroom/issues/3925) | 0 |
| [#3914 [FEATURE] Diagnose and recover Serena MCP after WSL TypeScript timeout](https://github.com/headroomlabs-ai/headroom/issues/3914) | 0 |
| [#3913 Subscription poller keeps using stale in-memory OAuth token after Claude Code refresh (poll fails with 401)](https://github.com/headroomlabs-ai/headroom/issues/3913) | 0 |
| [#3879 --intercept-tool-results is a no-op in the proxy: server.py bypasses _build_default_transforms()](https://github.com/headroomlabs-ai/headroom/issues/3879) | 2 |
| [#3844 Claude code giving classifier requests warning while using headroom proxy](https://github.com/headroomlabs-ai/headroom/issues/3844) | 0 |
| [#3842 [FEATURE] Support a verified newer tree-sitter-language-pack release](https://github.com/headroomlabs-ai/headroom/issues/3842) | 1 |
| [#3840 [COPILOT-SUB] <OS> test report](https://github.com/headroomlabs-ai/headroom/issues/3840) | 2 |
| [#3838 Add headroom to awesome-ai-plugins?](https://github.com/headroomlabs-ai/headroom/issues/3838) | 0 |
| [#3818 [BUG] headroom-ai[proxy]/[all] unresolvable on Intel macOS with Python ≥3.11 (onnxruntime>=1.24.0 has no x86_64 macOS wheels)](https://github.com/headroomlabs-ai/headroom/issues/3818) | 0 |
| [#3815 CCR retrieval is unavailable on OpenAI chat-completions streaming, and toggles the tools cache in mixed-mode sessions](https://github.com/headroomlabs-ai/headroom/issues/3815) | 1 |
| [#3812 Per-session savings attribution (x-claude-code-session-id)](https://github.com/headroomlabs-ai/headroom/issues/3812) | 0 |
| [#3809 openclaw plugin: assemble() rebuilds every history message when anything is compressed, invalidating the provider prompt cache](https://github.com/headroomlabs-ai/headroom/issues/3809) | 1 |
| [#3798 [BUG] Vertex us multi-region is forwarded to incorrect upstream hostname](https://github.com/headroomlabs-ai/headroom/issues/3798) | 0 |
| [#3777 HEADROOM_OFFLINE=1 does not prevent the HuggingFace tokenizer download](https://github.com/headroomlabs-ai/headroom/issues/3777) | 0 |
| [#3768 [FEATURE] Pass through `safeguards` request field and `safeguard_results` response field](https://github.com/headroomlabs-ai/headroom/issues/3768) | 1 |
| [#3749 [BUG] Windows Codex proxy unavailability: sanitized 0.32.1 incident logs and limited 0.37.0 follow-up](https://github.com/headroomlabs-ai/headroom/issues/3749) | 1 |
| [#3732 Unknown model silently priced at the GPT-4o tier, so cost tracking and budget enforcement act on fabricated numbers](https://github.com/headroomlabs-ai/headroom/issues/3732) | 1 |
| [#3716 [BUG] VS Code Copilot requests are not routed through Headroom proxy despite successful wrap vscode setup](https://github.com/headroomlabs-ai/headroom/issues/3716) | 1 |
| [#3711 [BUG] Kompress/ONNX stage takes ~70s on a mixed prose+JSON tool output, exhausting the 30s budget and quarantining all compression (0.38.0)](https://github.com/headroomlabs-ai/headroom/issues/3711) | 1 |
| [#3702 [FEATURE] Support Github Copilot App](https://github.com/headroomlabs-ai/headroom/issues/3702) | 0 |
| [#3697 smart-crusher: remove dead crush_object clone; revisit the bundled whitespace guard from #3648](https://github.com/headroomlabs-ai/headroom/issues/3697) | 1 |
| [#3690 [FEATURE] Optional Jev-backed semantic policy for ModelRouter](https://github.com/headroomlabs-ai/headroom/issues/3690) | 2 |
| [#3669 Opencode plugin: make a version that works with OpenCode v2](https://github.com/headroomlabs-ai/headroom/issues/3669) | 0 |
| [#3667 Wire-contract guard relocates non-text blocks into top-level `system`, causing 400 on every affected request](https://github.com/headroomlabs-ai/headroom/issues/3667) | 2 |
| [#3653 compression_executor leaks a worker thread + fd on every quarantine event; never released after timeout (persists in 0.37.0)](https://github.com/headroomlabs-ai/headroom/issues/3653) | 1 |
| [#3652 [BUG] Columnar command output (ls -la, git status) classifies as PLAIN_TEXT and loses fields to Kompress — Bash missing from DEFAULT_EXCLUDE_TOOLS](https://github.com/headroomlabs-ai/headroom/issues/3652) | 1 |
| [#3649 Docker image: ast-grep binary missing from runtime stage (whitelist COPY) — --intercept-tool-results fails to start](https://github.com/headroomlabs-ai/headroom/issues/3649) | 0 |
