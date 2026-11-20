---
name: technologies-fa-gaia-watch
description: "Shipped defects in 14.3.2: the server advertises 13.0.0; the audit script skips plugin skills; create-agent and create-skill route policy to AGENTS.md; Playwright MCP unpinned. A restored host needs a republished, renamed image."
type: watch
last_verified: 2026-11-20
---

# Watch list

**Dogfooding — re-checked 2026-11-20**

- **The Claude desktop bundle ran the published line.** Its `foundation`, `engineering` and
  `product` read `14.3.1` (published until 14.3.2 that night), author FrostAura Technologies, and their skill and agent trees match
  this repo's `plugins/` file for file (re-compared 2026-11-20, `diff -rq` on `skills/`). The kill
  criterion ("stops being what FrostAura builds with") is not tripping.
- **The CLI channel is the root store's concern** — whether `fa-*` names resolve there is tracked
  in [`../../../../memory/plugin-roster-drift.md`](../../../../memory/plugin-roster-drift.md), not here.

**Shipped defects in the product itself — all live in published `14.3.2`**

- **A fourteenth version site, and it is wrong.** `src/Gaia.Mcp.Server/Program.cs` sets the
  `Implementation.Version` advertised on every MCP `initialize`; it reads `13.0.0`, last moved
  by the v13.0.0 commit. Neither the release loop in `../docs/development.md` nor any CI check
  names it. Two cheap exits, neither taken: fold it into the loop, or version the server
  independently (`../CLAUDE.md` already treats them as separate concerns).
- **`context-audit.py` passes silently over the skills this repo ships.**
  `check_skill_indexes` enters a `skills/` directory only when its parent is `.claude` or
  `.github`; plugin skills live at `plugins/<name>/skills/`, so the frontmatter↔directory-name
  check — whose failure yields an uninvokable skill — never runs on them. Substitute: the
  by-hand loop in `../docs/development.md`, on every skill change.
- **`fa-foundation-create-agent` and `fa-foundation-create-skill` still route global policy into
  `AGENTS.md`**, against the interop-pointer doctrine this repo applies to its own. They teach
  users the wrong thing.
- **`npx @playwright/mcp@latest` is unpinned** in the engineering plugin's `plugin.json` (both
  copies), and the desktop bundle carries it — a supply-chain exposure on a real install.
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
