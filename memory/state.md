---
name: ai-toolkit-gaia-state
description: "Pushed 2026-11-20, local main level with origin; that push published the audit fix still at 14.3.1, so installs won't re-fetch it (14.3.2 owed). gaia.frostaura.net answers 530, so the unratified foundation MCP wiring fails every install."
type: state
last_verified: 2026-11-20
---

# Current state

**Published line: still `14.3.1`, but `origin/main` moved on 2026-11-20.** Re-probed late that
day with `git fetch --prune` and `git ls-remote`: only `main` exists on origin, and it
took the 2026-11-20 context commit `d20c3a4` and, that evening, the follow-up context commits —
pushed by the founder, not an agent; local `main` is level with it, clean, no stash. Re-measure with `git rev-list --left-right --count @{u}...HEAD` after a
fetch before acting; never quote a count from here. A push is a release (`../CLAUDE.md`,
*Conventions*).

**That push published the script fix `ade2b60` unversioned.** `context-audit.py` now skips
`fixtures/` and a bare `memory/` with no `*.md` beside no context file (a C# `Memory/`
namespace on a case-insensitive volume) — ported from the FrostAura tree's local script, which
hit both against the since-killed `ai.toolkit.harness`. It sits under `[Unreleased]` in
`CHANGELOG.md`, and every `plugin.json` still reads `14.3.1`. Because the `version` is the
re-fetch trigger, **installs already on 14.3.1 will not pick it up** until the lockstep `14.3.2`
bump lands — still owed, and the founder's release call.

**The `foundation` MCP wiring is published.** Both copies of `plugins/foundation/plugin.json`
declare `fa-gaia-remote` → `https://gaia.frostaura.net/mcp` (re-read 2026-11-20). Unratified and
contradicting the README's disclosure — the single home for that is [`questions.md`](questions.md) §5.

**The hosted endpoint is not serving, and has not been since at least 2026-10-22.** On
2026-11-20 `curl -sI https://gaia.frostaura.net/api/health` and a bare POST to `/mcp` both
returned HTTP 530, and this session's `fa-gaia-remote` connection failed with Cloudflare error
1033 (tunnel not connected) — the same reading as 2026-10-22. Because of the wiring above,
every `foundation` install opens with a failed MCP connection. Cause unknown from here —
[`questions.md`](questions.md) §1.

**Version sites.** All twelve JSON sites agree at `14.3.1` (re-read 2026-11-20; the lockstep
rule is in [`decisions-distribution.md`](decisions-distribution.md)); the one outlier,
`src/Gaia.Mcp.Server/Program.cs` at `13.0.0`, is tracked in [`watch.md`](watch.md).
**Nothing past `v8.0.0` was ever tagged** — locally or on origin (`git ls-remote --tags`,
2026-11-20) — so there is nothing to pin or roll back to.

**Verified on disk 2026-11-20.** Three plugins (`foundation` 10 skills · 3 agents,
`engineering` 16 · 6, `product` 14 · 11); all three `plugin.json` pairs `cmp`-identical.
`src/` is the .NET 10 MCP server — Woolworths only, MCP plus REST under `/api` — and
`src/Gaia.Mcp.Tests`, whose `dotnet test Gaia.slnx --no-restore` ran 12 passing xUnit tests
on SDK 10.0.302.

**CI builds; it never deploys.** `build-gaia-mcp.yml` has two jobs, `test` and
`build-and-push`; `gh run list` late on 2026-11-20 shows the runs for both 2026-11-20 pushes green — new
images built and pushed — and none between them and 2026-09-16. Which image `gaia.frostaura.net`
is running cannot be answered from here — [`questions.md`](questions.md) §1.