---
name: technologies-fa-gaia-watch
description: "Fixed on the unmerged 15.0.0 branch: three shipped defects. Still live: the server advertises 13.0.0; foundation wires an MCP endpoint that 530s; skill descriptions cost 18.8k chars a session. A restored host needs a republished image."
type: watch
last_verified: 2026-11-21
---

# Watch list

**Dogfooding — re-checked 2026-11-20**

- **The Claude desktop bundle ran the published line.** Its `foundation`, `engineering` and
  `product` read `14.3.1` (published until 14.3.2 that night), author FrostAura Technologies, and their skill and agent trees match
  this repo's `plugins/` file for file (re-compared 2026-11-20, `diff -rq` on `skills/`). The kill
  criterion ("stops being what FrostAura builds with") is not tripping.
- **The CLI channel is the root store's concern** — whether `fa-*` names resolve there is tracked
  in [`../../../../memory/plugin-roster-drift.md`](../../../../memory/plugin-roster-drift.md), not here.

**Shipped defects in the product itself**

- **A fourteenth version site, and it is wrong.** `src/Gaia.Mcp.Server/Program.cs` sets the
  `Implementation.Version` advertised on every MCP `initialize`; it reads `13.0.0`, last moved
  by the v13.0.0 commit. Neither the release loop in `../docs/development.md` nor any CI check
  names it. Two cheap exits, neither taken: fold it into the loop, or version the server
  independently (`../CLAUDE.md` already treats them as separate concerns).
- **`foundation` wires `fa-gaia-remote` at an endpoint that does not serve.** Observed 2026-11-21 in a
  cloud session with all three plugins installed: the server failed to connect (Cloudflare 1033), on
  every session start, for every install. Whether to wire it at all is founder-owned
  ([`questions.md`](questions.md) §5); until he rules, each user pays a failed connection for a
  grocery integration the context layer does not use.
- **The skill listing is still over budget in a crowded install.** 15.0.0 cut the 40 descriptions'
  36.4k characters to 18.8k across 34 (`python3 scripts/validate-plugins.py --budget`). Before the
  cut, a session with these three plugins plus a design plugin listed every `foundation` skill and
  eight `product` skills with no description at all. Nobody has re-measured after it — the client's
  total budget is undocumented, so the only evidence is a real session's listing or `/skill-doctor`.
- **Fixed on the 15.0.0 branch, live in published `14.3.2` until it merges:** `context-audit.py`
  skipping plugin skills; `create-skill` and `create-agent` routing policy to `AGENTS.md`; the
  unpinned Playwright MCP (now `@0.0.86` — a pin that needs moving by hand from here on).
- **The README's marketplace-add path for Claude Desktop / claude.ai / Cowork has never been
  confirmed end to end.** The plugins demonstrably load on that surface from a session-local
  bundle; the install mechanism is what is unconfirmed.

**Repository hygiene**

- **A restored `gaia.frostaura.net` must name the renamed image, and it must exist first.** CI
  publishes `frostaura/technologies.fa.gaia`; the old `gaia-mcp` repository was deleted on 2026-11-20,
  so a stack still naming it cannot pull, and a host that has it cached runs a pre-14.3.2 image forever.
  By the last check that night the new repository was deleted as well, so a restore waits on CI.
- **The CI runner is unpinned** (`ubuntu-latest` in both jobs). It moved to Ubuntu 26.04 and broke the
  public site's Playwright install on 2026-11-20; Gaia's jobs install no browser and were green after the
  move, so this is exposure, not a failure.
- **This repo is public and its context layer is not written as if it were** — `CLAUDE.md` names
  the owner, the decision topics name the parent's internal structure and a killed internal
  project, all pushed. Genericize deliberately, or accept it deliberately.
- **A 2 MB `README.icon.png` is committed at repo root**, referenced by absolute GitHub raw URL
  anyway. History is permanent; removing it now only stops it growing.
