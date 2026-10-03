# oven-sh/bun

Generated: 2026-10-03T09:42:38.239543+00:00

- Unassigned: 36+
- [View all unassigned issues](https://github.com/oven-sh/bun/issues?q=is%3Aissue%20is%3Aopen%20no%3Aassignee)

Most recently opened:

| Issue | Comments |
|---|---|
| [#44531 bun test: in CI mode a missing snapshot still creates a .snap file](https://github.com/oven-sh/bun/issues/44531) | 1 |
| [#44530 node:http2 client: a PUSH_PROMISE before its enablePush=false SETTINGS is ACKed ends the session](https://github.com/oven-sh/bun/issues/44530) | 0 |
| [#44525 node:buffer: hexSlice, utf8Write and the other per-encoding methods throw a TypeError with no code for a receiver that is not a Buffer](https://github.com/oven-sh/bun/issues/44525) | 0 |
| [#44523 Playwright mTLS test intermittently returns ERR_SOCKET_NOT_CONNECTED on Bun after node:tls fixes](https://github.com/oven-sh/bun/issues/44523) | 0 |
| [#44522 bun:test ignores custom Error.stack from Error.captureStackTrace / stack-string surgery (regression vs #32390 fix)](https://github.com/oven-sh/bun/issues/44522) | 1 |
| [#44517 node:tls: a close_notify alert during the handshake on a TCP socket reports ERR_SSL_SSL_HANDSHAKE_FAILURE, Node reports ECONNRESET](https://github.com/oven-sh/bun/issues/44517) | 0 |
| [#44511 fix(install): global remove leaves an unreachable optional dependency](https://github.com/oven-sh/bun/issues/44511) | 1 |
| [#44479 node:http2 client: close() on a request that was rejected before it got a stream id throws an uncaught "Invalid stream id"](https://github.com/oven-sh/bun/issues/44479) | 0 |
| [#44478 Bun.WebView (chrome backend): first navigate() on a fresh Chrome sometimes never settles on Windows, with no readiness signal](https://github.com/oven-sh/bun/issues/44478) | 0 |
| [#44472 Add support for Redis INCREX command](https://github.com/oven-sh/bun/issues/44472) | 0 |
| [#44463 TC39 decorators fail in the HMR runtime: missing bun:wrap helpers (source patch included)](https://github.com/oven-sh/bun/issues/44463) | 1 |
| [#44459 bun test: AGENT=<agent-name> disables AI agent detection, and AI_AGENT is ignored](https://github.com/oven-sh/bun/issues/44459) | 0 |
| [#44456 node:http2 client emits 'response' and 'stream' inside the frame dispatch, node on process.nextTick (differs over a JS transport)](https://github.com/oven-sh/bun/issues/44456) | 0 |
| [#44453 Node.js ws compatibility: server WebSocket (BunWebSocketMocked) is missing pause(), resume(), and isPaused](https://github.com/oven-sh/bun/issues/44453) | 0 |
| [#44450 node:http2 client: maxReservedRemoteStreams counts a pushed stream until it closes, node until its response HEADERS arrive](https://github.com/oven-sh/bun/issues/44450) | 0 |
| [#44444 Segfault in Bun.inspect on an AggregateError that contains itself](https://github.com/oven-sh/bun/issues/44444) | 0 |
| [#44430 node:http2: session.goaway(code, lastStreamID) does not close the open peer streams above lastStreamID](https://github.com/oven-sh/bun/issues/44430) | 0 |
| [#44429 Windows: a socket's data event is lost when bun:test's expect(promise).rejects waits on a postgres.js query](https://github.com/oven-sh/bun/issues/44429) | 0 |
| [#44428 fetch: four `Content-Encoding: deflate` bodies where Bun differs from Node or curl](https://github.com/oven-sh/bun/issues/44428) | 0 |
| [#44420 Transpiler deletes an expression statement that calls a function named declare](https://github.com/oven-sh/bun/issues/44420) | 0 |
| [#44418 docs: bun test "AI Agent Integration" omits how AGENT and RUNNER_DEBUG turn failures-only output off](https://github.com/oven-sh/bun/issues/44418) | 1 |
| [#44417 bun init never writes CLAUDE.md on Windows, even when Claude Code is on PATH](https://github.com/oven-sh/bun/issues/44417) | 0 |
| [#44416 bun init on Windows checks USER to find Cursor, so the Cursor rule file is usually not written](https://github.com/oven-sh/bun/issues/44416) | 0 |
| [#44408 node:zlib: destroy() of a zstd compressor with ZSTD_c_nbWorkers blocks the JS thread until the running job ends](https://github.com/oven-sh/bun/issues/44408) | 0 |
| [#44407 Numeric options accept NaN and silently use a placeholder (Bun.spawn maxBuffer, validate_integer_range callers)](https://github.com/oven-sh/bun/issues/44407) | 0 |
| [#44405 toMatchObject passes when an expected Date or Error differs (Bun.deepMatch returns true)](https://github.com/oven-sh/bun/issues/44405) | 0 |
| [#44401 A failed directory read is taken as the end of the directory in 16 loops outside pack and publish](https://github.com/oven-sh/bun/issues/44401) | 0 |
| [#44390 Windows: `bun test --parallel` worker segfaults (heap corruption seen in GC sweep, libuv pipe read on canary) in a suite that spawns child processes over pipes](https://github.com/oven-sh/bun/issues/44390) | 0 |
| [#44387 Bun.write(Bun.stdout, data) pads an appended file with NUL bytes when data is over 1024 bytes (fallocate on an O_APPEND fd)](https://github.com/oven-sh/bun/issues/44387) | 2 |
| [#44386 Intl.Segments.containing() includes the preceding grapheme at a leading surrogate](https://github.com/oven-sh/bun/issues/44386) | 0 |
| [#44385 fs.watch (macOS): opening or closing a watcher drops events for every other watcher while the FSEvents stream is rebuilt](https://github.com/oven-sh/bun/issues/44385) | 0 |
| [#44382 bun:test: the diff of a failed `toEqual()` prints the `Symbol.toStringTag` of an object on its own line](https://github.com/oven-sh/bun/issues/44382) | 0 |
| [#44381 bun:test: `toEqual()` passes for two different functions that are not plain JS functions, for example `expect(Array).toEqual(Object)`](https://github.com/oven-sh/bun/issues/44381) | 0 |
| [#44379 `process.env.TZ` reads `undefined` when `TZ` is set to an empty string](https://github.com/oven-sh/bun/issues/44379) | 0 |
| [#44367 bun-types: SQL `database` is documented to default to the username, but the mysql/mariadb adapters default to "mysql"/"mariadb"](https://github.com/oven-sh/bun/issues/44367) | 0 |
| [#44365 fetch: NODE_EXTRA_CA_CERTS doesn't trust a self-signed CA:FALSE leaf cert (Node does)](https://github.com/oven-sh/bun/issues/44365) | 1 |
