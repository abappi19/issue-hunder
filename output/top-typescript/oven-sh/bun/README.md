# oven-sh/bun

Generated: 2026-09-28T16:04:44.001734+00:00

- Unassigned: 51+
- [View all unassigned issues](https://github.com/oven-sh/bun/issues?q=is%3Aissue%20is%3Aopen%20no%3Aassignee)

Most recently opened:

| Issue | Comments |
|---|---|
| [#44164 Bun.PLIST: parse/stringify Apple property lists (XML, binary, OpenStep) + .plist loader](https://github.com/oven-sh/bun/issues/44164) | 0 |
| [#44162 bun test --changed skips tests that import through package.json "imports" (#subpath) or a workspace package](https://github.com/oven-sh/bun/issues/44162) | 0 |
| [#44161 bun test --isolate: intermittent SIGSEGV in JSFinalizationRegistry::takeDeadHoldingsValue (0x70) on 1.4.2 Linux x64](https://github.com/oven-sh/bun/issues/44161) | 0 |
| [#44160 bun publish does not respect --dns-result-order=ipv4first](https://github.com/oven-sh/bun/issues/44160) | 0 |
| [#44159 bun upgrade fails if you have BUN_OPTIONS set](https://github.com/oven-sh/bun/issues/44159) | 0 |
| [#44158 --cpu-prof omits positionTicks for samples in DFG/FTL code, so a node's ticks sum to less than its hitCount](https://github.com/oven-sh/bun/issues/44158) | 0 |
| [#44157 node:sqlite / bun:sqlite: built without SQLITE_DEFAULT_MEMSTATUS=0, so reads from several workers contend on a global mutex](https://github.com/oven-sh/bun/issues/44157) | 0 |
| [#44156 worker_threads: allocating workers block on each other's GC marking; BUN_JSC_numberOfGCMarkers=1 halves 8-worker wall time](https://github.com/oven-sh/bun/issues/44156) | 2 |
| [#44148 node:tls: a write to this.rejectUnauthorized in checkServerIdentity does not change the verdict](https://github.com/oven-sh/bun/issues/44148) | 0 |
| [#44144 node:tls: the connect options lack minDHSize, singleUse and the http2 servername](https://github.com/oven-sh/bun/issues/44144) | 0 |
| [#44143 ws: finishRequest gets no `this` and no WebSocket argument](https://github.com/oven-sh/bun/issues/44143) | 0 |
| [#44142 ws, undici, node-fetch: checkServerIdentity is never called](https://github.com/oven-sh/bun/issues/44142) | 0 |
| [#44141 node:tls: a function assigned to tls.checkServerIdentity is never called](https://github.com/oven-sh/bun/issues/44141) | 0 |
| [#44140 node:tls: SNICallback gets the tls.Server as `this`, Node passes the TLSSocket](https://github.com/oven-sh/bun/issues/44140) | 0 |
| [#44138 Bun.Transpiler: exports.replace prints a module that does not parse when the module cannot declare the export name](https://github.com/oven-sh/bun/issues/44138) | 0 |
| [#44136 node:zlib: the rejectGarbageAfterEnd option is ignored](https://github.com/oven-sh/bun/issues/44136) | 0 |
| [#44134 Bun.WebView (webkit): navigate() sometimes never settles when the reply frame is over 8 KB (URL longer than ~8.15 KB)](https://github.com/oven-sh/bun/issues/44134) | 0 |
| [#44132 node:stream/iter: a stateful transform that yields the null flush signal throws ERR_INVALID_ARG_TYPE](https://github.com/oven-sh/bun/issues/44132) | 0 |
| [#44130 `Bun.file()` and in-memory `Blob` return the internal `INIT_TIMESTAMP` sentinel from `lastModified`](https://github.com/oven-sh/bun/issues/44130) | 1 |
| [#44127 ws: req.setHeader() in finishRequest does not replace a header of options.headers with an uppercase name](https://github.com/oven-sh/bun/issues/44127) | 0 |
| [#44125 node:os: os.cpus() throws "Failed to get CPU information" on model/speed/times when /proc/stat and /proc/cpuinfo disagree](https://github.com/oven-sh/bun/issues/44125) | 1 |
| [#44121 bun build: class renamed on name collision changes `.name`, even with `--keep-names`](https://github.com/oven-sh/bun/issues/44121) | 1 |
| [#44120 emitDecoratorMetadata ignores strictNullChecks: `X | undefined` / `X | null` serialized as `X` instead of `Object`](https://github.com/oven-sh/bun/issues/44120) | 1 |
| [#44116 Bun.SQL: a ShadowRealm that reads Bun.SQL takes over the query callbacks of every realm](https://github.com/oven-sh/bun/issues/44116) | 0 |
| [#44115 Bun.SQL: a dial that fails at once rejects with an Error that has no code](https://github.com/oven-sh/bun/issues/44115) | 0 |
| [#44114 bun test --isolate: two import() calls of one module in the same tick abort a build with assertions](https://github.com/oven-sh/bun/issues/44114) | 0 |
| [#44109 sharp file I/O crashes Bun with mprotect failed: 487 / Illegal instruction on Windows (WASM path)](https://github.com/oven-sh/bun/issues/44109) | 1 |
| [#44108 `ws`: differences from npm ws that remain on the built-in client and server sockets](https://github.com/oven-sh/bun/issues/44108) | 2 |
| [#44101 bun build --compile: a bare specifier required from an embedded module never resolves inside $bunfs](https://github.com/oven-sh/bun/issues/44101) | 1 |
| [#44098 ws: a finishRequest that calls req.end() later opens two connections](https://github.com/oven-sh/bun/issues/44098) | 0 |
| [#44096 naming.asset: "[dir]/[name].[ext]" embeds an extensionless file with a trailing dot](https://github.com/oven-sh/bun/issues/44096) | 1 |
| [#44095 bun build --compile: require() of an embedded JSON file asset evaluates it as JavaScript](https://github.com/oven-sh/bun/issues/44095) | 1 |
| [#44094 Bun.SQL (MySQL): two query texts get one statement cache key, and the second query runs the statement of the first](https://github.com/oven-sh/bun/issues/44094) | 0 |
| [#44092 test(sql): the fixture of "process should exit when idle" does not set allowPublicKeyRetrieval](https://github.com/oven-sh/bun/issues/44092) | 0 |
| [#44090 Windows: stable install-scoped aliases for --bun and run.bun](https://github.com/oven-sh/bun/issues/44090) | 1 |
| [#44088 bun:sqlite: fileControl items that #44089 leaves open](https://github.com/oven-sh/bun/issues/44088) | 0 |
| [#44084 node:sqlite StatementSync.get() ~1.5x slower than Node when returning table columns](https://github.com/oven-sh/bun/issues/44084) | 3 |
| [#44077 --cpu-prof and --cpu-prof-md count event-loop idle time as JavaScript self time](https://github.com/oven-sh/bun/issues/44077) | 1 |
| [#44075 macOS: dns.lookup/fetch ENOTFOUND for split-DNS names — DNSServiceGetAddrInfoEx ignores kDNSServiceAttrAllowFailover (follow-up to #40573)](https://github.com/oven-sh/bun/issues/44075) | 0 |
| [#44068 bun build --compile: __dirname/__filename in an included CommonJS entrypoint are inlined as the build directory, not the $bunfs path](https://github.com/oven-sh/bun/issues/44068) | 1 |
| [#44064 Bun.serve sends an empty body for a file on procfs or cgroupfs (st_size 0)](https://github.com/oven-sh/bun/issues/44064) | 0 |
| [#44063 bun build --compile: an embedded native addon is extracted alone, so a shared library next to it is not found (Library not loaded: @rpath/...)](https://github.com/oven-sh/bun/issues/44063) | 1 |
| [#44062 bun build --compile --asset keeps only the last path segment, but --help says it preserves the relative path](https://github.com/oven-sh/bun/issues/44062) | 1 |
| [#44053 bun build --compile: an --external package is resolved from process.cwd(), not from the executable's directory](https://github.com/oven-sh/bun/issues/44053) | 1 |
| [#44051 fs.watch on macOS stops reporting writes to a file that the writer keeps open (regression in 1.3.14)](https://github.com/oven-sh/bun/issues/44051) | 1 |
| [#44048 docs: html-static.mdx links to a removed source file (src/runtime/api/bun/html-rewriter.ts 404s)](https://github.com/oven-sh/bun/issues/44048) | 1 |
| [#44045 bun:test toMatchSnapshot() creates multi-megabyte files when snapshotting JSDOM nodes](https://github.com/oven-sh/bun/issues/44045) | 1 |
| [#44044 Bun.markdown: a chain of autolink candidates that fail at their right boundary takes quadratic time](https://github.com/oven-sh/bun/issues/44044) | 0 |
| [#44039 Bun.SQL: a graceful `close()` after `reserved.release()` does not wait for the queries of the reserved connection](https://github.com/oven-sh/bun/issues/44039) | 0 |
| [#44038 Bun.SQL: the query of `sql.file()` is rejected when a graceful `close()` follows in the same tick](https://github.com/oven-sh/bun/issues/44038) | 0 |
| [#44037 Bun.Image: decode HEIC/HEIF on Linux (dlopen system libheif)](https://github.com/oven-sh/bun/issues/44037) | 2 |
