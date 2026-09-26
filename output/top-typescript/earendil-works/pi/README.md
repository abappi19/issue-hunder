# earendil-works/pi

Generated: 2026-09-26T18:25:42.796415+00:00

- Unassigned: 74+
- [View all unassigned issues](https://github.com/earendil-works/pi/issues?q=is%3Aissue%20is%3Aopen%20no%3Aassignee)

Most recently opened:

| Issue | Comments |
|---|---|
| [#10054 registerCommand accepts a non-string name; extension loads, then `/` crashes pi](https://github.com/earendil-works/pi/issues/10054) | 0 |
| [#10024 A mid-run change to the selected tool set moves the head of the system prompt and re-bills the conversation](https://github.com/earendil-works/pi/issues/10024) | 4 |
| [#10022 OpenRouter compaction/summary requests drop x-session-id when cacheRetention is none](https://github.com/earendil-works/pi/issues/10022) | 2 |
| [#10017 Follow-up queued with triggerTurn during a run is stranded when the run aborts](https://github.com/earendil-works/pi/issues/10017) | 0 |
| [#10015 bash: truncation notice reports 0B for a >50KB last line ending in a newline](https://github.com/earendil-works/pi/issues/10015) | 2 |
| [#10002 Extension console output writes over the interactive TUI](https://github.com/earendil-works/pi/issues/10002) | 3 |
| [#9986 Aborting during tool execution leaves unanswered tool calls in the session](https://github.com/earendil-works/pi/issues/9986) | 3 |
| [#9980 Calculated cost for top open models on OpenRouter is off by 2-3x almost always](https://github.com/earendil-works/pi/issues/9980) | 5 |
| [#9962 registerNativeProvider races the startup refresh.  Initial model resolves from a stale snapshot ("No models available")](https://github.com/earendil-works/pi/issues/9962) | 2 |
| [#9954 kimi-coding models fail with ENOENT on ~/.config/anthropic/credentials/default.json (Anthropic SDK ambient credential probing)](https://github.com/earendil-works/pi/issues/9954) | 2 |
| [#9953 anthropic strict tools: makeStrictJsonSchema keeps minimum/maximum/minLength, API rejects every request (400)](https://github.com/earendil-works/pi/issues/9953) | 3 |
| [#9932 before_agent_start: forced system prompt keeps tools that setActiveTools removed in the same chain](https://github.com/earendil-works/pi/issues/9932) | 4 |
| [#9904 Decouple auto-compaction threshold from reserveTokens](https://github.com/earendil-works/pi/issues/9904) | 3 |
| [#9886 clearQueue() silently destroys extension-delivered custom messages without returning them。](https://github.com/earendil-works/pi/issues/9886) | 4 |
| [#9884 Configured default model is sometimes replaced by a fallback at startup](https://github.com/earendil-works/pi/issues/9884) | 5 |
| [#9874 Skills manifest silently omitted from the system prompt when no tool named read/bash is active](https://github.com/earendil-works/pi/issues/9874) | 2 |
| [#9855 Pager mode](https://github.com/earendil-works/pi/issues/9855) | 0 |
| [#9852 [pi-ai] openai-responses: function_call name is not sanitized → 400 invalid_value when history has MCP tool names with ':'](https://github.com/earendil-works/pi/issues/9852) | 2 |
| [#9839 Custom cwd not honored by built-in tools after ctx.cwd change - restore via opt-in customCwd](https://github.com/earendil-works/pi/issues/9839) | 1 |
| [#9819 Contribution proposal: use auth.kimi.ai for global Kimi Code OAuth](https://github.com/earendil-works/pi/issues/9819) | 3 |
| [#9807 perf(tui): full re-render causes scroll/typing lag in sessions with 800+ messages](https://github.com/earendil-works/pi/issues/9807) | 3 |
| [#9793 Ambiguous length stop drops history far below the window when streaming usage omits reasoning tokens](https://github.com/earendil-works/pi/issues/9793) | 2 |
| [#9792 SessionManager.create() does not write session file to disk until first assistant message despite isPersisted() returning true](https://github.com/earendil-works/pi/issues/9792) | 2 |
| [#9787 0.86.0: importing the SDK installs pi's nested undici (8.10.2) as the process-global dispatcher; native fetch abort/streaming breaks in embedded hosts](https://github.com/earendil-works/pi/issues/9787) | 2 |
| [#9773 before_provider_request does not fire for summarization/compaction requests](https://github.com/earendil-works/pi/issues/9773) | 5 |
| [#9757 parseChunkUsage drops provider usage fields that aren't on its known list](https://github.com/earendil-works/pi/issues/9757) | 3 |
| [#9718 --print exits 0 with empty output when the model exhausts its output budget](https://github.com/earendil-works/pi/issues/9718) | 3 |
| [#9678 mistral-conversations: hosted GLM reasoning dispatch drops the requested effort level](https://github.com/earendil-works/pi/issues/9678) | 4 |
| [#9656 Mouse wheel scrolls prompt history instead of transcript in fullscreen on Windows + Zellij](https://github.com/earendil-works/pi/issues/9656) | 1 |
| [#9647 Emit session_compact_end event to extensions after clearing compaction state](https://github.com/earendil-works/pi/issues/9647) | 5 |
| [#9602 Compaction can overflow by including thinking messages omitted from earlier model requests](https://github.com/earendil-works/pi/issues/9602) | 6 |
| [#9583 Windows (pwsh/ConPTY): loader line suddenly paints at the top of the screen (autowrap drift in main-screen renderer)](https://github.com/earendil-works/pi/issues/9583) | 1 |
| [#9571 provider retry: malformed Retry-After HTTP-date retries immediately (NaN delay)](https://github.com/earendil-works/pi/issues/9571) | 7 |
| [#9566 context size defaults to 128k despite the real size being available](https://github.com/earendil-works/pi/issues/9566) | 5 |
| [#9557 Anthropic adapter drops root-level JSON Schema keywords (anyOf, ) from non-strict tool input_schema](https://github.com/earendil-works/pi/issues/9557) | 2 |
| [#9545 Reuse whole-file normalization during batch edit uniqueness checks](https://github.com/earendil-works/pi/issues/9545) | 2 |
| [#9537 SDK embed: /login status line reports the global auth.json path when a custom agentDir is in use](https://github.com/earendil-works/pi/issues/9537) | 2 |
| [#9508 pi-ai sends unsupported OpenAI-specific request fields/roles/auth to compatible providers](https://github.com/earendil-works/pi/issues/9508) | 6 |
| [#9497 Windows：CJK（中日韩）IME 输入卡顿、候选窗口常不显示；启用 showHardwareCursor 可修复 / Windows: CJK IME input is laggy and the candidate window often does not appear — enabling showHardwareCursor fixes it](https://github.com/earendil-works/pi/issues/9497) | 4 |
| [#9474 Codex transport: no non-resetting per-request total deadline; periodic events defeat idle timeout](https://github.com/earendil-works/pi/issues/9474) | 3 |
| [#9448 pi auth check cannot see providers from extensions](https://github.com/earendil-works/pi/issues/9448) | 3 |
| [#9444 openai-completions drops Gemini thoughtSignature on streamed tool_calls, breaking multi-turn tool use](https://github.com/earendil-works/pi/issues/9444) | 3 |
| [#9432 Allow session_start extensions to append stable base system prompt context](https://github.com/earendil-works/pi/issues/9432) | 1 |
| [#9411 Branch summaries pay full fresh input on every navigate: summary request shares no cache prefix with live turns](https://github.com/earendil-works/pi/issues/9411) | 1 |
| [#9410 [Bug]: Pressing Escape to interrupt streaming in large sessions causes ~60s complete TUI freeze](https://github.com/earendil-works/pi/issues/9410) | 4 |
| [#9409 Sessions wedge permanently at the context ceiling on reasoning models](https://github.com/earendil-works/pi/issues/9409) | 2 |
| [#9408 Remember plan-level model errors and surface them in /model (badge, sort, recovery hint)](https://github.com/earendil-works/pi/issues/9408) | 0 |
| [#9332 Fullscreen: drag-selecting the editor row that contains the caret corrupts the display (cursor marker leaks to the terminal)](https://github.com/earendil-works/pi/issues/9332) | 3 |
| [#9331 Bedrock: OpenAI reasoning effort is never sent to the model](https://github.com/earendil-works/pi/issues/9331) | 4 |
| [#9311 Fullscreen mouse selection survives session switch](https://github.com/earendil-works/pi/issues/9311) | 6 |
| [#9268 tui: remote Markdown image with empty alt hides URL in user messages](https://github.com/earendil-works/pi/issues/9268) | 5 |
| [#9265 @earendil-works/pi-ai: O(n²) tool-call argument re-parsing in openai-completions streaming freezes the event loop](https://github.com/earendil-works/pi/issues/9265) | 4 |
| [#9262 find tool: glob patterns with Windows separators (src\**\*.ts) silently return no results](https://github.com/earendil-works/pi/issues/9262) | 4 |
| [#9257 extractCursorPosition leaves duplicate CURSOR_MARKER occurrences](https://github.com/earendil-works/pi/issues/9257) | 5 |
| [#9256 Resumed session re-renders tool-result images as full-size inline images](https://github.com/earendil-works/pi/issues/9256) | 4 |
| [#9255 TuiMainScreen: full-screen redraw storm when changed rows sit above the viewport top (long transcripts jump violently / doubled text)](https://github.com/earendil-works/pi/issues/9255) | 7 |
| [#9221 Reload during an active extension tool can store a successful result as an error](https://github.com/earendil-works/pi/issues/9221) | 0 |
| [#9216 Ollama qwen3.8:27b: stream 'terminated' errors (clean 0.84.x->0.85.x regression) + auto-compaction stops re-triggering after first run](https://github.com/earendil-works/pi/issues/9216) | 5 |
| [#9211 vercelGatewayRouting is inert on the vercel-ai-gateway provider: only the openai-completions adapter sends it, the gateway catalog is all anthropic-messages](https://github.com/earendil-works/pi/issues/9211) | 5 |
| [#9194 RPC: no way to clear queued steering/followUp messages (abort keeps the queues)](https://github.com/earendil-works/pi/issues/9194) | 1 |
| [#9154 RPC prompt during tree navigation can leave active context](https://github.com/earendil-works/pi/issues/9154) | 0 |
| [#9134 Anthropic adapter silently drops root anyOf from custom tool schemas](https://github.com/earendil-works/pi/issues/9134) | 3 |
| [#9129 On Windows, bash timeout kill leaves pipeline processes orphaned](https://github.com/earendil-works/pi/issues/9129) | 4 |
| [#9124 Runtime dispose can leave dangling tool calls in persisted session history](https://github.com/earendil-works/pi/issues/9124) | 0 |
| [#9109 Preserve model selector selection after background refresh](https://github.com/earendil-works/pi/issues/9109) | 2 |
| [#9075 Compaction summarisation inherits the session thinking level on adaptive models and deterministically hits the output cap at high efforts](https://github.com/earendil-works/pi/issues/9075) | 4 |
| [#9074 Anthropic mid-output fallback fails the turn instead of recording the handoff](https://github.com/earendil-works/pi/issues/9074) | 3 |
| [#9051 session_compact custom message misses the immediate overflow retry](https://github.com/earendil-works/pi/issues/9051) | 5 |
| [#9016 fix(coding-agent): enable reasoning and reasoning effort for llama.cpp provider](https://github.com/earendil-works/pi/issues/9016) | 2 |
| [#9013 Cache miss notices false-positive on local vLLM after a cloud model in the same session](https://github.com/earendil-works/pi/issues/9013) | 2 |
| [#9010 Context compaction causes memory spikes with local LLMs due to in-process string duplication](https://github.com/earendil-works/pi/issues/9010) | 2 |
| [#8940 Preserve OpenRouter actual cost, cost details, BYOK flag, and serving provider](https://github.com/earendil-works/pi/issues/8940) | 2 |
| [#8913 Expose the fullscreen renderer's existing `mouse` option: fullscreen unconditionally enables mouse tracking, including 1003 any-event, with no way to opt out](https://github.com/earendil-works/pi/issues/8913) | 6 |
| [#8829 wrapUIPromptContext copying by spread and lose ui prototype methods](https://github.com/earendil-works/pi/issues/8829) | 4 |
