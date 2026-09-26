# mem0ai/mem0

Generated: 2026-09-26T18:43:26.230047+00:00

- Unassigned: 68+
- [View all unassigned issues](https://github.com/mem0ai/mem0/issues?q=is%3Aissue%20is%3Aopen%20no%3Aassignee)

Most recently opened:

| Issue | Comments |
|---|---|
| [#7461 Langchain vector store: list() returns None for any non-Chroma VectorStore client (FAISS, Qdrant, PGVector, ...), crashing Memory.get_all() and Memory.delete_all() with TypeError](https://github.com/mem0ai/mem0/issues/7461) | 1 |
| [#7458 Self-hosted server doesn't expose mem0 core's reranker config or rerank search param](https://github.com/mem0ai/mem0/issues/7458) | 0 |
| [#7457 Self-hosted server can't point LLM and embedder at independent OpenAI-compatible endpoints](https://github.com/mem0ai/mem0/issues/7457) | 0 |
| [#7454 bug(qdrant): entity-store operations silently truncate after 10k rows](https://github.com/mem0ai/mem0/issues/7454) | 1 |
| [#7453 Request for review: open, matched memory benchmark protocol](https://github.com/mem0ai/mem0/issues/7453) | 0 |
| [#7452 bug(memory): delete_all() leaves the scope's session messages, which are re-sent to the LLM on the next add()](https://github.com/mem0ai/mem0/issues/7452) | 4 |
| [#7446 normalize_facts mishandles wrapped {facts: [...]} objects and bare strings](https://github.com/mem0ai/mem0/issues/7446) | 2 |
| [#7443 [pgvector] Boolean values in operator filters (eq/ne/in/nin, list shorthand) never match stored booleans](https://github.com/mem0ai/mem0/issues/7443) | 1 |
| [#7440 Memory.close() races in-flight writes: silent audit-history loss (db=None window)](https://github.com/mem0ai/mem0/issues/7440) | 3 |
| [#7439 Langchain vector store: list() returns None for non-Chroma clients, crashing Memory.get_all() and Memory.delete_all()](https://github.com/mem0ai/mem0/issues/7439) | 5 |
| [#7432 Pinecone: entity store uses "<collection>_entities" index name, which Pinecone rejects (TS + Python)](https://github.com/mem0ai/mem0/issues/7432) | 2 |
| [#7428 AzureOpenAIStructuredLLM: constructor crashes on None/dict/BaseLlmConfig (AttributeError/TypeError) because azure_kwargs is accessed without AzureOpenAIConfig conversion](https://github.com/mem0ai/mem0/issues/7428) | 1 |
| [#7426 LLMReranker scores reasoning models by numbers inside <think>, ranking relevant memories last](https://github.com/mem0ai/mem0/issues/7426) | 0 |
| [#7421 AWS Bedrock: OpenAI GPT-6 Sol/Luna/Astra fail with "Unknown provider in model" (also GPT-5.6; gpt-oss gets a 400)](https://github.com/mem0ai/mem0/issues/7421) | 0 |
| [#7418 docs: LLM config "Master List" table omits anthropic_base_url, minimax_base_url and vllm_base_url](https://github.com/mem0ai/mem0/issues/7418) | 0 |
| [#7417 AWS Bedrock: Claude Opus 5.5 calls fail with 400 "`temperature` is deprecated for this model" (also Opus 4.7+/Sonnet 5/Fable)](https://github.com/mem0ai/mem0/issues/7417) | 0 |
| [#7416 FAISS filtered search returns fewer than top_k results because over-fetched candidates are cut before filtering](https://github.com/mem0ai/mem0/issues/7416) | 0 |
| [#7413 Weaviate vector store: identify Mem0 with the X-Weaviate-Client-Integration header](https://github.com/mem0ai/mem0/issues/7413) | 0 |
| [#7399 docs: Gemini LLM examples still use retired gemini-2.0-flash IDs](https://github.com/mem0ai/mem0/issues/7399) | 1 |
| [#7398 Bundle the ollama embedder in the self-hosted server image](https://github.com/mem0ai/mem0/issues/7398) | 1 |
| [#7397 Self-hosted server: no health endpoint; dashboard healthcheck stays green while the API is down](https://github.com/mem0ai/mem0/issues/7397) | 0 |
| [#7396 Self-hosted server: let the official SDK's MemoryClient work against it (platform API compatibility)](https://github.com/mem0ai/mem0/issues/7396) | 0 |
| [#7393 test_rejects_symlink_outside_bundle fails on Windows without symlink privilege](https://github.com/mem0ai/mem0/issues/7393) | 1 |
| [#7391 feat(vector-store): add NeuG as an optional vector store backend (native vector + full-text + graph)](https://github.com/mem0ai/mem0/issues/7391) | 0 |
| [#7383 PGVector.list() has no ORDER BY, so getAll() silently returns an arbitrary subset past topK (TS OSS)](https://github.com/mem0ai/mem0/issues/7383) | 6 |
| [#7377 feat(plugins): add native GitHub Copilot CLI integration](https://github.com/mem0ai/mem0/issues/7377) | 1 |
| [#7376 RFC: memory export interop — portable bundles with proof and chain of custody](https://github.com/mem0ai/mem0/issues/7376) | 7 |
| [#7360 AWS Bedrock: non-tool Amazon Nova path sends Converse but parses with the invoke_model parser, so generate_response returns "Error parsing response"](https://github.com/mem0ai/mem0/issues/7360) | 5 |
| [#7356 Upgrade mem0-ts to OpenAI SDK v5](https://github.com/mem0ai/mem0/issues/7356) | 1 |
| [#7355 mem0 TypeScript ignores env-specified proxy settings (http_proxy, HTTPS_PROXY) when talking to model providers](https://github.com/mem0ai/mem0/issues/7355) | 2 |
| [#7352 docs: Python multimodal examples recreate clients with vision disabled](https://github.com/mem0ai/mem0/issues/7352) | 0 |
| [#7347 bug(vector_stores/azure-ai-search): telemetry helpers operate on the memory index — a user's memory is silently re-scoped to the telemetry id](https://github.com/mem0ai/mem0/issues/7347) | 4 |
| [#7346 Claude Code plugin reports "API key missing" after a successful `mem0 login` — `plugin_sync` only updates pre-existing entries](https://github.com/mem0ai/mem0/issues/7346) | 2 |
| [#7342 Windows: Cursor plugin 0.2.13 spawns hung Git Bash (mintty) windows on Read hooks](https://github.com/mem0ai/mem0/issues/7342) | 3 |
| [#7336 [Bug] AWS Bedrock: legacy amazon (Titan) responses always parse to '' — _parse_response reads a 'completion' field Titan never returns](https://github.com/mem0ai/mem0/issues/7336) | 7 |
| [#7333 bug(server): configured LLM API key appears unset in dashboard](https://github.com/mem0ai/mem0/issues/7333) | 2 |
| [#7317 _extract_count recurses into non-dict model_dump(), allocating ~2GB before silently returning None](https://github.com/mem0ai/mem0/issues/7317) | 3 |
| [#7314 PGVector destructor closes externally supplied connection_pool](https://github.com/mem0ai/mem0/issues/7314) | 1 |
| [#7313 Docs: BaseEmbedderConfig says openai_base_url defaults to api.openai.com, but two env vars come first](https://github.com/mem0ai/mem0/issues/7313) | 2 |
| [#7302 Deepseek Harness: canceled recall marks undelivered memories as seen](https://github.com/mem0ai/mem0/issues/7302) | 4 |
| [#7294 [mem0-ts] PGVector store has no 'error' listener on its pg Client — server-side connection termination crashes the host process, and the client never reconnects](https://github.com/mem0ai/mem0/issues/7294) | 2 |
| [#7284 DeepSeek Harness: fix first-turn recall and plugin activation for 0.3.1](https://github.com/mem0ai/mem0/issues/7284) | 0 |
| [#7283 Faithfulness check before memory write , interested in contributing a pluggable verification hook](https://github.com/mem0ai/mem0/issues/7283) | 13 |
| [#7277 spaCy model auto-download runs pip/uv inside the first add()/search(); SystemExit escapes `except Exception` and crashes the call on every retry](https://github.com/mem0ai/mem0/issues/7277) | 4 |
| [#7260 bug(server): no rate limiting on LLM-calling endpoints (/memories, /search, /generate-instructions)](https://github.com/mem0ai/mem0/issues/7260) | 6 |
| [#7256 bug(vector_stores/faiss): empty payload bypasses client-side filters (returns True)](https://github.com/mem0ai/mem0/issues/7256) | 6 |
| [#7255 bug(vector_stores/azure_mysql): filter values still double-encoded with json.dumps (string filters never match)](https://github.com/mem0ai/mem0/issues/7255) | 1 |
| [#7250 bug(vector_stores/weaviate): search score hardcoded for cosine; create_col distance unused](https://github.com/mem0ai/mem0/issues/7250) | 2 |
| [#7249 bug(vector_stores/redis): search score hardcoded for cosine, breaks L2 ranking](https://github.com/mem0ai/mem0/issues/7249) | 3 |
| [#7235 Pre-publication review: our re-scoring of Mem0's published LoCoMo answers under alternative judge prompts (corrections welcome)](https://github.com/mem0ai/mem0/issues/7235) | 0 |
| [#7232 bug(vector_stores/vertex_ai): search score hardcoded for cosine, breaks L2-style indexes](https://github.com/mem0ai/mem0/issues/7232) | 6 |
| [#7229 bug(vector_stores/valkey): search score hardcoded for cosine, breaks L2 ranking](https://github.com/mem0ai/mem0/issues/7229) | 5 |
| [#7227 CLI config JSON should use explicit UTF-8 encoding](https://github.com/mem0ai/mem0/issues/7227) | 2 |
| [#7226 Entity-index cleanup is skipped in any process that has not written entities, so deletions leave permanent stale links](https://github.com/mem0ai/mem0/issues/7226) | 5 |
| [#7214 bug(vector_stores/opensearch): enhanced metadata filters (gte/lte/in/OR/NOT/contains) are silently dropped — search runs unfiltered](https://github.com/mem0ai/mem0/issues/7214) | 2 |
| [#7212 Bug: No built-in support for Chinese LLM providers (Qwen, Zhipu, Moonshot)](https://github.com/mem0ai/mem0/issues/7212) | 1 |
| [#7211 bug(vector-stores): Azure AI Search indexing errors silently ignored due to flawed hasattr status_code check](https://github.com/mem0ai/mem0/issues/7211) | 4 |
| [#7209 GCP service account project_id JSON read uses locale default encoding](https://github.com/mem0ai/mem0/issues/7209) | 2 |
| [#7207 [HTTPXodus] Consider migrating from `httpx` to `httpx2` (the actively maintained fork)](https://github.com/mem0ai/mem0/issues/7207) | 1 |
| [#7206 bug(vector_stores/valkey): enhanced metadata filters silently become literal TAG matches](https://github.com/mem0ai/mem0/issues/7206) | 1 |
| [#7202 Skill examples and LLM.md call search()/get_all() with top-level user_id, which raises ValueError](https://github.com/mem0ai/mem0/issues/7202) | 4 |
| [#7201 Python V3 add returns failed fallback vector inserts as successful memories](https://github.com/mem0ai/mem0/issues/7201) | 4 |
| [#7198 Empty '## Summary' section in extraction prompt triggers upstream content-filter empty responses](https://github.com/mem0ai/mem0/issues/7198) | 0 |
| [#7197 OPENROUTER_API_KEY env var hijacks explicitly configured OpenAI-compatible endpoint](https://github.com/mem0ai/mem0/issues/7197) | 1 |
| [#7196 SQLite 'database is locked' under concurrent sessions / heartbeat reads](https://github.com/mem0ai/mem0/issues/7196) | 1 |
| [#7195 Message buffer FIFO eviction pollutes extraction context with stale cross-session content](https://github.com/mem0ai/mem0/issues/7195) | 1 |
| [#7187 bug(vector_stores/supabase): advanced metadata filters are translated as equality](https://github.com/mem0ai/mem0/issues/7187) | 2 |
| [#7186 [feature] opencode plugin: config knobs for startup context size (injection top_k / startup framing toggle)](https://github.com/mem0ai/mem0/issues/7186) | 0 |
