---
name: ai-toolkit-gaia-state
description: "v14.3.1 is what origin serves; local main is ahead-only with an unversioned audit fix (14.3.2 bump owed). gaia.frostaura.net answered Cloudflare 1033 on 2026-10-22, so the unratified foundation MCP wiring fails on every install."
type: state
last_verified: 2026-10-22
---

# Current state

**Published line: `14.3.1`, last pushed 2026-09-16.** `origin/main`'s tip is the 2026-09-16
context commit; no plugin change has landed upstream since. Re-checked 2026-10-22 after a
`git fetch --prune`: only `main` remains on origin.

**Local topology (re-measured 2026-10-22, clean tree): `main` is ahead-only of `origin/main` — no
divergence, no deletions in the range.** The unpushed range is one script fix plus the
2026-10-14 store refresh. Re-measure with `git rev-list --left-right --count @{u}...HEAD`
before acting; never quote a count from here. The repo is public and installs float on
`ref: main`, so a push *is* a release.

**The unpushed script fix is unversioned on purpose.** `context-audit.py` now skips
`fixtures/` and a bare `memory/` with no `*.md` beside no context file (a C# `Memory/`
namespace on a case-insensitive volume) — ported from the FrostAura tree's local script, which
hit both against `ai.toolkit.harness`. It sits under `[Unreleased]` in `CHANGELOG.md`. Because
the `plugin.json` `version` is the re-fetch trigger, **pushing it without the lockstep `14.3.2`
bump ships code no install will pick up** — the bump is owed, and is the founder's release call.

**The `foundation` MCP wiring is published.** Both copies of `plugins/foundation/plugin.json`
declare `fa-gaia-remote` → `https://gaia.frostaura.net/mcp` (re-read 2026-10-22). Unratified and
contradicting the README's disclosure — the single home for that is [`questions.md`](questions.md) §5.

**The hosted endpoint was not serving on 2026-10-22.** `curl https://gaia.frostaura.net/api/health`
returned HTTP 530 with Cloudflare error 1033 (tunnel not connected), and this session's
`fa-gaia-remote` connection failed the same way. Because of the wiring above, every `foundation`
install now opens with a failed MCP connection. Cause unknown from here — [`questions.md`](questions.md) §1.

**Version sites.** All twelve JSON sites agree at `14.3.1` (re-read 2026-10-22; the lockstep
rule is in [`decisions-distribution.md`](decisions-distribution.md)); the one outlier,
`src/Gaia.Mcp.Server/Program.cs` at `13.0.0`, is tracked in [`watch.md`](watch.md).
**Nothing past `v8.0.0` was ever tagged**, so there is nothing to pin or roll back to.

**Verified on disk 2026-10-22.** Three plugins (`foundation` 10 skills · 3 agents,
`engineering` 16 · 6, `product` 14 · 11); all three `plugin.json` pairs `cmp`-identical.
`src/` is the .NET 10 MCP server — Woolworths only, MCP plus REST under `/api` — and
`src/Gaia.Mcp.Tests`, whose `dotnet test Gaia.slnx --no-restore` ran 12 passing xUnit tests,
0 warnings.

**CI builds; it never deploys.** `build-gaia-mcp.yml` has two jobs, `test` and
`build-and-push`; its last runs (2026-09-16) were recorded green, not re-checked. Which image `gaia.frostaura.net` is
running cannot be answered from here — [`questions.md`](questions.md) §1.

**Harmless debris:** local branch `system/deanm/research-scientist-edition`, upstream gone, already
merged into `main` (re-checked 2026-10-22) — deleting it loses nothing; the owner's call.
