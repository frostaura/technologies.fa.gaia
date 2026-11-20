---
name: technologies-fa-gaia-state
description: "Renamed from ai.toolkit.gaia and moved from Labs 2026-11-20; the founder shipped 14.3.2 for the rename the same night, which also delivered the audit fix. gaia.frostaura.net 530s, so foundation's MCP wiring fails every install."
type: state
last_verified: 2026-11-20
---

# Current state

**Renamed and moved on 2026-11-20, by founder decision.** `Labs/projects/ai.toolkit.gaia` became
`Technologies/projects/technologies.fa.gaia`: a Technologies product, no longer a Labs program.
The repository is `https://github.com/frostaura/technologies.fa.gaia`, and GitHub redirects the
old `frostaura/ai.toolkit.gaia` (`gh repo view` on the old name resolves to the new one). There is
no `~/src` clone; this iCloud clone is the only one.

**Published line: `14.3.2`, released by the founder late on 2026-11-20** (`ee873fd`, "release:
14.3.2 — repository renamed technologies.fa.gaia"). It repoints every product reference to the new
repo name: marketplace sources, all six `plugin.json` `repository` fields, the README install
commands and `docs/development.md`. Only `CHANGELOG.md` history still says `ai.toolkit.gaia`. It also
ships the context-audit fix `ade2b60`, which had been pushed unversioned at 14.3.1, so floating
installs now re-fetch it. `origin/main` carries only `main`; local `main` was fast-forwarded to it,
and this pass's context commit followed. Re-measure with `git rev-list --left-right --count
@{u}...HEAD` after a fetch, and never quote a count from here. A push is a release (`../CLAUDE.md`).

**The `foundation` MCP wiring is published.** Both copies of `plugins/foundation/plugin.json`
declare `fa-gaia-remote` → `https://gaia.frostaura.net/mcp` (re-read 2026-11-20). Unratified and
contradicting the README's disclosure — the single home for that is [`questions.md`](questions.md) §5.

**The hosted endpoint is not serving, and has not been since at least 2026-10-22.** On
2026-11-20 `curl -sI https://gaia.frostaura.net/api/health` and a bare POST to `/mcp` both
returned HTTP 530, and this session's `fa-gaia-remote` connection failed with Cloudflare error
1033 (tunnel not connected) — the same reading as 2026-10-22. Because of the wiring above,
every `foundation` install opens with a failed MCP connection. Cause unknown from here —
[`questions.md`](questions.md) §1.

**Version sites.** All twelve JSON sites agree at `14.3.2`, and the README badge matches (re-read
after `ee873fd`; the lockstep rule is in [`decisions-distribution.md`](decisions-distribution.md)). The
outlier, `src/Gaia.Mcp.Server/Program.cs` at `13.0.0`, is tracked in [`watch.md`](watch.md).
**Nothing past `v8.0.0` was ever tagged** (`git ls-remote --tags`, 2026-11-20), so there is
nothing to pin or roll back to.

**Verified on disk 2026-11-20.** Three plugins (`foundation` 10 skills · 3 agents,
`engineering` 16 · 6, `product` 14 · 11); all three `plugin.json` pairs `cmp`-identical.
`src/` is the .NET 10 MCP server — Woolworths only, MCP plus REST under `/api` — and
`src/Gaia.Mcp.Tests`, whose `dotnet test Gaia.slnx --no-restore` ran 12 passing xUnit tests
on SDK 10.0.302.

**CI builds; it never deploys.** `build-gaia-mcp.yml` has two jobs, `test` and `build-and-push`.
Since `ee873fd` the image is pushed as `<namespace>/technologies.fa.gaia` (it was `gaia-mcp`), with OCI
labels. Every earlier 2026-11-20 run was green, and the 14.3.2 run was still in progress when
this was written. Which image `gaia.frostaura.net` runs cannot be answered from here
([`questions.md`](questions.md) §1).
