# oven-sh/bun

Generated: 2026-09-26T19:32:38.075464+00:00

- Unassigned: 43+
- [View all unassigned issues](https://github.com/oven-sh/bun/issues?q=is%3Aissue%20is%3Aopen%20no%3Aassignee)

Most recently opened:

| Issue | Comments |
|---|---|
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
| [#44034 node:http: a CONNECT or Upgrade socket that closes with unread data drops it and emits no 'end'](https://github.com/oven-sh/bun/issues/44034) | 0 |
| [#44033 Installing some packages on windows sometimes results in "bun: command not found: node" including node itself.](https://github.com/oven-sh/bun/issues/44033) | 3 |
| [#44030 A failed read of a child's memfd output is dropped](https://github.com/oven-sh/bun/issues/44030) | 0 |
| [#44029 Windows: a failed read of a child's stdout or stderr leaves the pipe open](https://github.com/oven-sh/bun/issues/44029) | 0 |
| [#44027 Bun.SQL MySQL: the docs say that queries are pipelined, the adapter writes one command at a time since v1.2.22](https://github.com/oven-sh/bun/issues/44027) | 1 |
| [#44025 Windows: `await expect(promise).resolves` after a relayed WebSocket close segfaults or hangs at 100% CPU](https://github.com/oven-sh/bun/issues/44025) | 1 |
| [#44020 `process.exit()` with no argument after an unhandled rejection exits with 0](https://github.com/oven-sh/bun/issues/44020) | 0 |
| [#44019 A default-mode unhandled rejection does not reach an `uncaughtException` listener](https://github.com/oven-sh/bun/issues/44019) | 0 |
| [#44018 An `exit` listener that throws replaces the exit code with 1](https://github.com/oven-sh/bun/issues/44018) | 0 |
| [#44009 Segfault in JSC GC marking (JSScope::visitChildren) in standalone executable (Claude Code), Bun v1.4.3 Linux x64](https://github.com/oven-sh/bun/issues/44009) | 2 |
| [#44005 fs.watch reports one 'rename' when an entry is removed and created again (Node reports two)](https://github.com/oven-sh/bun/issues/44005) | 1 |
| [#44002 `bun test` exits 0 and silently skips a nonexistent `./`-prefixed path when another path matches](https://github.com/oven-sh/bun/issues/44002) | 1 |
| [#44000 bun update <name> keeps the old lockfile row for URL/local tarball deps (stale integrity and dependency list)](https://github.com/oven-sh/bun/issues/44000) | 0 |
| [#43999 node:tls: a client that refuses the server still sends its TLS 1.3 client certificate while another TLS socket has unsent data](https://github.com/oven-sh/bun/issues/43999) | 0 |
| [#43998 fetch: the TLS 1.3 client certificate reaches a server that `checkServerIdentity` then refuses](https://github.com/oven-sh/bun/issues/43998) | 0 |
| [#43996 `Bun.write` stringifies input it does not support, so `Bun.write(path, img.png())` writes "[object Image]" and reports success](https://github.com/oven-sh/bun/issues/43996) | 1 |
| [#43993 sql(mysql): a statement text of 16 MiB or more rejects with no `code`](https://github.com/oven-sh/bun/issues/43993) | 0 |
| [#43992 Bun.SQL: a query that fails on the client rejects with a different value on each path](https://github.com/oven-sh/bun/issues/43992) | 0 |
| [#43983 prompt() returns null on a bare Enter when no default is given, so it cannot be told apart from end of input](https://github.com/oven-sh/bun/issues/43983) | 1 |
| [#43980 URL with path wrapped in ** renders to broken link](https://github.com/oven-sh/bun/issues/43980) | 1 |
| [#43977 Auto-install ignores the version pinned in package.json and bun.lock, loading the latest tag](https://github.com/oven-sh/bun/issues/43977) | 1 |
| [#43975 `bun update <pkg>` does not re-resolve packages whose `$pkg` override changed; lock stays stale and `bun install` / `--frozen-lockfile` do not notice](https://github.com/oven-sh/bun/issues/43975) | 2 |
| [#43971 Bun.serve: a request that ends in the checkpoint of an `error()` Response ends a stream that another reader holds](https://github.com/oven-sh/bun/issues/43971) | 1 |
| [#43970 Bun.serve: HEAD of a proxied `fetch()` Response holds the upstream request open, and `fetch()` stops after 256 requests](https://github.com/oven-sh/bun/issues/43970) | 0 |
| [#43961 `expect()`: `not.toHaveLength()` and `not.toBeEmpty()` pass for a `Blob` with no known size](https://github.com/oven-sh/bun/issues/43961) | 0 |
| [#43960 S3: a write of a sliced in-memory `Blob` uploads the whole `Blob`](https://github.com/oven-sh/bun/issues/43960) | 0 |
| [#43949 node:http2: stream.state.localWindowSize never changes](https://github.com/oven-sh/bun/issues/43949) | 0 |
| [#43939 `Bun.inspect()` prints `0.0 ZB` for a Request or Response whose file body is a slice or has no known size](https://github.com/oven-sh/bun/issues/43939) | 0 |
| [#43938 S3: `slice(-n)` fails with InvalidRange, and `slice(a)` sends a last byte position of 4503599627370494](https://github.com/oven-sh/bun/issues/43938) | 0 |
| [#43932 fs.watch on macOS: three differences from libuv in how FSEvents events are filtered](https://github.com/oven-sh/bun/issues/43932) | 0 |
| [#43931 APIs that read a Blob synchronously read an S3 file as empty](https://github.com/oven-sh/bun/issues/43931) | 0 |
| [#43930 `new Response(s3file.slice(a, b))` redirects to the whole object](https://github.com/oven-sh/bun/issues/43930) | 0 |
