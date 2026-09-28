# langchain-ai/langchain

Generated: 2026-09-28T16:04:44.001734+00:00

- Unassigned: 83+
- [View all unassigned issues](https://github.com/langchain-ai/langchain/issues?q=is%3Aissue%20is%3Aopen%20no%3Aassignee)

Most recently opened:

| Issue | Comments |
|---|---|
| [#40871 ChatOpenAI (Responses API): streamed chunks switch from resp_… to lc_run--… ids, the stream id doesn't match the final message id](https://github.com/langchain-ai/langchain/issues/40871) | 0 |
| [#40868 Agentic run with dynamic filtering (web_search_20260209 inside code_execution) rejected with "code_execution tool use ... without a corresponding code_execution_tool_result block](https://github.com/langchain-ai/langchain/issues/40868) | 1 |
| [#40867 feat(typesafe): harden TypeSafeClassifier against API limits and rate limiting](https://github.com/langchain-ai/langchain/issues/40867) | 0 |
| [#40866 ModelCallLimitMiddleware: the limit-exceeded message can't be told apart from a model answer](https://github.com/langchain-ai/langchain/issues/40866) | 0 |
| [#40863 Support forwarding MCP _meta on tool calls and surfacing server response metadata](https://github.com/langchain-ai/langchain/issues/40863) | 0 |
| [#40858 Output parsers drop tool calls when a chat model falls back to invoke inside stream(), so structured output streams nothing](https://github.com/langchain-ai/langchain/issues/40858) | 3 |
| [#40852 Many tests fail](https://github.com/langchain-ai/langchain/issues/40852) | 1 |
| [#40840 SummarizationMiddleware: _get_approximate_token_counter doesn't recognize Claude on Bedrock (ChatBedrockConverse), so summarization triggers late](https://github.com/langchain-ai/langchain/issues/40840) | 1 |
| [#40830 ChatPerplexity.stream() crashes with TypeError when `stop` sequences are passed](https://github.com/langchain-ai/langchain/issues/40830) | 4 |
| [#40826 Streaming a large tool call re-parses its arguments in pure Python on every chunk](https://github.com/langchain-ai/langchain/issues/40826) | 3 |
| [#40825 MCP Apps (SEP-1865): first-class support for hosts that render a server's UI](https://github.com/langchain-ai/langchain/issues/40825) | 1 |
| [#40819 RunnableWithFallbacks.batch/abatch never close root runs when an input raises an exception not in exceptions_to_handle](https://github.com/langchain-ai/langchain/issues/40819) | 8 |
| [#40809 Bedrock Converse `content_blocks` drops redacted reasoning, so it is not sent back with `output_version="v1"` (found with GPT-6 Sol/Luna/Astra)](https://github.com/langchain-ai/langchain/issues/40809) | 1 |
| [#40802 langchain-typesafe: TypeSafeClassifier declares serialization support but cannot round-trip through built-in deserialization](https://github.com/langchain-ai/langchain/issues/40802) | 1 |
| [#40796 langchain-typesafe: validate ModelRouterMiddleware classifier routes](https://github.com/langchain-ai/langchain/issues/40796) | 2 |
| [#40788 message_to_events drops AIMessage.additional_kwargs during replay](https://github.com/langchain-ai/langchain/issues/40788) | 7 |
| [#40782 `ChatOpenAI.bind_tools()` rejects GPT-6 shell / Programmatic Tool Calling and lacks Responses round-trip support](https://github.com/langchain-ai/langchain/issues/40782) | 1 |
| [#40777 `ChatAnthropic` sends unsupported tool choice and thinking configurations for Claude Opus 5.5](https://github.com/langchain-ai/langchain/issues/40777) | 1 |
| [#40771 [langchain-groq] bind_tools ignores a known tool_calling=False model profile and sends a request that Groq rejects](https://github.com/langchain-ai/langchain/issues/40771) | 7 |
| [#40770 [langchain-anthropic] Manual thinking validation misses Claude Opus 4.7/4.8 and Sonnet 5](https://github.com/langchain-ai/langchain/issues/40770) | 3 |
| [#40769 [langchain-deepseek] bind_tools(tool_choice="any") produces an invalid request with DeepSeek's default thinking mode`](https://github.com/langchain-ai/langchain/issues/40769) | 2 |
| [#40768 [langchain-anthropic] Call-time thinking bypasses bind_tools forced-tool-choice guard](https://github.com/langchain-ai/langchain/issues/40768) | 2 |
| [#40767 PIIMiddleware(apply_to_output=True) blanks parameters on tool calls, leading to a GraphRecursion Error.](https://github.com/langchain-ai/langchain/issues/40767) | 2 |
| [#40761 text-splitters: `RecursiveJsonSplitter` sizes chunks against escaped JSON, so `ensure_ascii=False` chunks come back far below `max_chunk_size`](https://github.com/langchain-ai/langchain/issues/40761) | 3 |
| [#40755 ChatAnthropic.bind_tools() raises ValueError on Anthropic's documented browser_toolset_20260801](https://github.com/langchain-ai/langchain/issues/40755) | 2 |
| [#40753 ToolStrategy retries structured-output validation failures without any cap](https://github.com/langchain-ai/langchain/issues/40753) | 1 |
| [#40748 xai: `ChatXAI` builds two `openai.OpenAI` clients per instance — `client` is not a view onto `root_client`](https://github.com/langchain-ai/langchain/issues/40748) | 2 |
| [#40745 core: empty `group_ids` bypasses validation and filtering in `InMemoryRecordManager`](https://github.com/langchain-ai/langchain/issues/40745) | 8 |
| [#40730 ​feat(typesafe): add support for custom base URL, API keys and model configuration. ](https://github.com/langchain-ai/langchain/issues/40730) | 2 |
| [#40729 langchain-typesafe: ModelRouterMiddleware exposes ignored model_route in input schema](https://github.com/langchain-ai/langchain/issues/40729) | 2 |
| [#40727 langchain-typesafe: recursive `State` alias leaves input schema unresolvable](https://github.com/langchain-ai/langchain/issues/40727) | 2 |
| [#40726 langchain-typesafe: allow supplying a classifier to experimental middleware](https://github.com/langchain-ai/langchain/issues/40726) | 2 |
| [#40725 SummarizationMiddleware sends unredacted conversation history to the summary model, bypassing PIIMiddleware including strategy=block](https://github.com/langchain-ai/langchain/issues/40725) | 3 |
| [#40721 [langchain-anthropic] ChatAnthropic forwards deprecated top_k to Claude Opus 5, causing HTTP 400](https://github.com/langchain-ai/langchain/issues/40721) | 3 |
| [#40709 LLMToolSelectorMiddleware ignores conversation history on follow-up queries](https://github.com/langchain-ai/langchain/issues/40709) | 2 |
| [#40704 PIIMiddleware inspects only the newest message of each kind, so PII in supplied history reaches the model and block does not raise](https://github.com/langchain-ai/langchain/issues/40704) | 4 |
| [#40700 langchain-typesafe: ModelRouterMiddleware overrides ModelFallbackMiddleware fallback models](https://github.com/langchain-ai/langchain/issues/40700) | 2 |
| [#40694 langchain-typesafe: AutoModeMiddleware classifies a tool call that inner middleware can replace before execution](https://github.com/langchain-ai/langchain/issues/40694) | 3 |
| [#40688 `ToolRetryMiddleware`: default settings retry non-idempotent tools on ambiguous transport errors, then ask the model to retry again](https://github.com/langchain-ai/langchain/issues/40688) | 10 |
| [#40678 core: Responses file-URL test overwrites its expected result without asserting it](https://github.com/langchain-ai/langchain/issues/40678) | 4 |
| [#40677 core: Message chunk addition drops 'name' and fallback 'id', breaking streaming multi-agent metadata and merge_message_runs](https://github.com/langchain-ai/langchain/issues/40677) | 3 |
| [#40675 anthropic: `FilesystemClaudeTextEditorMiddleware` reads and writes files with the locale encoding so non ascii content breaks on non utf8 systems](https://github.com/langchain-ai/langchain/issues/40675) | 5 |
| [#40668 Cache writes are counted twice for priority and flex](https://github.com/langchain-ai/langchain/issues/40668) | 3 |
| [#40664 pyproject.toml is read with the locale encoding in unit tests — full inventory (4 call sites, one missed by #40588, one latent)](https://github.com/langchain-ai/langchain/issues/40664) | 3 |
| [#40657 PromptTemplate silently accepts empty f-string field `{}` then crashes with IndexError on format](https://github.com/langchain-ai/langchain/issues/40657) | 5 |
| [#40651 langchain-typesafe: ModelRouterMiddleware raises an opaque RuntimeError when state has no human message](https://github.com/langchain-ai/langchain/issues/40651) | 2 |
| [#40616 ntegration: memory transfer store for LangChain/LangMem  export and import verified agent memory](https://github.com/langchain-ai/langchain/issues/40616) | 1 |
| [#40609 core: AIMessage(tool_calls=[]) still hydrates tool calls from additional_kwargs](https://github.com/langchain-ai/langchain/issues/40609) | 4 |
| [#40592 core: `InMemoryRecordManager.list_keys(limit=0)` returns all keys instead of an empty list](https://github.com/langchain-ai/langchain/issues/40592) | 6 |
| [#40590 `ChatGroq` accepts `n > 1` for non-streaming requests although Groq only supports `n=1](https://github.com/langchain-ai/langchain/issues/40590) | 4 |
| [#40588 [Bug] Two langchain unit tests read pyproject.toml without a UTF-8 encoding and fail on Windows with a non-UTF-8 locale](https://github.com/langchain-ai/langchain/issues/40588) | 5 |
| [#40578 feat(typesafe): add `ModerationMiddleware` for input content moderation](https://github.com/langchain-ai/langchain/issues/40578) | 2 |
| [#40563 ChatOpenAI silently drops provider-specific extra fields on tool calls (breaks multi-turn tool calling against OpenAI-compatible endpoints)](https://github.com/langchain-ai/langchain/issues/40563) | 2 |
| [#40531 core: `finalize_tool_call_chunk` coerces `id=None` to `""`, collapsing parallel id-less tool calls](https://github.com/langchain-ai/langchain/issues/40531) | 10 |
| [#40518 UsageMetadataCallbackHandler silently drops usage_metadata when model_name is missing](https://github.com/langchain-ai/langchain/issues/40518) | 3 |
| [#40503 MCP ResourceLink/EmbeddedResource metadata dropped when converting to LangChain content blocks (langchain.mcp)](https://github.com/langchain-ai/langchain/issues/40503) | 3 |
| [#40502 core: `InMemoryVectorStore` raises `NotImplementedError` for relevance-score search and the `similarity_score_threshold` retriever](https://github.com/langchain-ai/langchain/issues/40502) | 2 |
| [#40501 core: `AsyncBaseTracer` drops `name` in `on_tool_start` and `response` in `on_llm_error`, diverging from `BaseTracer`](https://github.com/langchain-ai/langchain/issues/40501) | 2 |
| [#40492 langchain 1.4.0: any after_model middleware using documented `jump_to="tools"` bypasses the HITL pending_tool_calls gate and re-executes rejected tool calls](https://github.com/langchain-ai/langchain/issues/40492) | 9 |
| [#40470 langchain: preserve result-level MCP `_meta` in tool results](https://github.com/langchain-ai/langchain/issues/40470) | 2 |
| [#40460 core: mustache inverted section `{{^key}}` nested inside a `{{#key}}` list section misrenders or raises `IndexError`](https://github.com/langchain-ai/langchain/issues/40460) | 4 |
| [#40447 huggingface: `HuggingFaceEndpoint` drops the token for dedicated Inference Endpoints (`*.endpoints.huggingface.cloud`)](https://github.com/langchain-ai/langchain/issues/40447) | 4 |
| [#40444 Token budget middleware that checks in with the user instead of hard-stopping](https://github.com/langchain-ai/langchain/issues/40444) | 7 |
| [#40441 Blob leaks a UTF-8 BOM into as_string()](https://github.com/langchain-ai/langchain/issues/40441) | 9 |
| [#40435 langchain-openrouter: ToolMessage content blocks (e.g. images) are sent to the API unconverted, failing client-side with ValidationError](https://github.com/langchain-ai/langchain/issues/40435) | 2 |
| [#40431 [Security Hardening] Mitigating OWASP LLM01 Indirect Prompt Injections in Web Loaders via CSS Render-Layer Obfuscation (CWE-1427)](https://github.com/langchain-ai/langchain/issues/40431) | 5 |
| [#40424 core: content_blocks raises TypeError on a v0 multimodal block that carries an id](https://github.com/langchain-ai/langchain/issues/40424) | 4 |
| [#40423 bug(langchain): create_agent ends the loop on an invalid structured-output call when an ordinary tool call is in the same batch (no retry feedback)](https://github.com/langchain-ai/langchain/issues/40423) | 3 |
| [#40392 v3 stream: parallel tool calls collide on the positional fallback key and one is silently dropped](https://github.com/langchain-ai/langchain/issues/40392) | 7 |
| [#40379 ChatOpenRouter: max_retries=0 enables the SDK default retry policy](https://github.com/langchain-ai/langchain/issues/40379) | 2 |
| [#40368 RemoteGraph returns invoke output as list of dict instead of list of BaseMessage - mandatory when combined with CompiledSubAgent](https://github.com/langchain-ai/langchain/issues/40368) | 1 |
| [#40367 Fireworks: reasoning_content dropped in streaming and outbound converters](https://github.com/langchain-ai/langchain/issues/40367) | 1 |
| [#40364 Errors OpenRouter reports in a 200 response body are stringified rather than classified](https://github.com/langchain-ai/langchain/issues/40364) | 2 |
| [#40362 Provider errors returned in a 200 response body are never classified](https://github.com/langchain-ai/langchain/issues/40362) | 4 |
| [#40360 CommaSeparatedListOutputParser corrupts quoted CSV fields across streaming chunks](https://github.com/langchain-ai/langchain/issues/40360) | 2 |
| [#40343 standard-tests: chat model tests never check the documented `total_tokens == input_tokens + output_tokens` invariant](https://github.com/langchain-ai/langchain/issues/40343) | 1 |
| [#40341 `HTMLHeaderTextSplitter` raises `ValueError` on init for the non-heading tags its splitter already supports](https://github.com/langchain-ai/langchain/issues/40341) | 10 |
| [#40334 Feature: Support metadata-only updates in index() - avoid re-embedding when the content is unchanged](https://github.com/langchain-ai/langchain/issues/40334) | 1 |
| [#40333 feat: WalletForge x402 paid tools (fetch_markdown / normalize_text) for LangChain agents](https://github.com/langchain-ai/langchain/issues/40333) | 0 |
| [#40332 `convert_to_openai_tool` ignores `strict` for dicts already in OpenAI tool format](https://github.com/langchain-ai/langchain/issues/40332) | 2 |
| [#40320 langchain: 26 shell middleware unit tests fail on Windows (POSIX-only tests without platform guards)](https://github.com/langchain-ai/langchain/issues/40320) | 1 |
| [#40314 MarkdownHeaderTextSplitter becomes very slow with many paragraphs under the same header](https://github.com/langchain-ai/langchain/issues/40314) | 2 |
| [#40311 `AnthropicPromptCachingMiddleware` silently drops the system prompt when the last content block is a string](https://github.com/langchain-ai/langchain/issues/40311) | 2 |
