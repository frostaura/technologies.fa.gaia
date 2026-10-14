---
name: ai-toolkit-gaia-state
description: "v14.3.1 is what origin serves and the desktop bundle now runs; local main is ahead-only with an unversioned context-audit fix (14.3.2 bump owed before push). The foundation MCP wiring shipped unratified."
type: state
last_verified: 2026-10-14
---

# Current state

**Published line: `14.3.1`, last pushed 2026-09-16.** `origin/main`'s tip is the 2026-09-16
context commit; no plugin change has landed upstream since. Re-checked 2026-10-14 after a
`git fetch --prune` (which removed three long-dead remote branches): only `main` remains on origin.

**Local topology (2026-10-14): `main` is ahead-only of `origin/main` — no divergence, no
deletions in the range — and this pass did not push it.** The unpushed range is one script fix
plus this store's refresh. Re-measure with `git rev-list --left-right --count @{u}...HEAD`
before acting; never quote a count from here. The repo is public and installs float on
`ref: main`, so a push *is* a release.

**The unpushed script fix is unversioned on purpose.** `context-audit.py` now skips
`fixtures/` and a bare `memory/` with no `*.md` beside no context file (a C# `Memory/`
namespace on a case-insensitive volume) — ported from the FrostAura tree's local script, which
hit both against `ai.toolkit.harness`. It sits under `[Unreleased]` in `CHANGELOG.md`. Because
the `plugin.json` `version` is the re-fetch trigger, **pushing it without the lockstep `14.3.2`
bump ships code no install will pick up** — the bump is owed, and is the founder's release call.

**What v14 is.** `14.0.0` broke the memory contract: `MEMORY.md` is a derived index regenerated
from `memory/` topics by `--fix-index`, so a consuming repo's hand-written index reports stale
until regenerated once. `14.1`–`14.3.1` harden the regenerator and widen the audit.

**The `foundation` MCP wiring is published and unratified.** `plugins/foundation/plugin.json`
declares `fa-gaia-remote` → `https://gaia.frostaura.net/mcp`, from a 2026-08-24 commit with no
recorded why, reversing the v13.0.0 decision ([`decisions.md`](decisions.md)). The README's
"the plugins send nothing anywhere" is therefore untrue for `foundation`. Founder call —
[`questions.md`](questions.md) §5.

**Version sites.** Twelve JSON sites (six `plugin.json`, three rows in each marketplace
manifest) plus the README badge agree at `14.3.1`, by hand, with no CI check; `metadata.version`
in the manifests is the catalog version and stays put. A fourteenth site,
`src/Gaia.Mcp.Server/Program.cs`, still advertises `13.0.0` — [`watch.md`](watch.md).
**Nothing past `v8.0.0` was ever tagged**, so there is nothing to pin or roll back to.

**Verified on disk 2026-10-14.** Three plugins (`foundation` 10 skills · 3 agents,
`engineering` 16 · 6, `product` 14 · 11); all three `plugin.json` pairs `cmp`-identical.
`src/` is the .NET 10 MCP server — Woolworths only, MCP plus REST under `/api` — and
`src/Gaia.Mcp.Tests`, whose `dotnet test Gaia.slnx` runs and passes real xUnit assertions.

**CI builds; it never deploys.** `build-gaia-mcp.yml` has two jobs, `test` and
`build-and-push`; its last runs (2026-09-16) were green. Which image `gaia.frostaura.net` is
running cannot be answered from here — [`questions.md`](questions.md) §1.

**Harmless debris:** a local branch `system/deanm/research-scientist-edition` whose upstream is
gone; it is already merged into `main`, so deleting it loses nothing — the owner's call.
