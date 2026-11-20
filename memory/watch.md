---
name: ai-toolkit-gaia-watch
description: "Shipped defects live in 14.3.1: server advertises 13.0.0; memory-maintenance description over the 1024 cap; audit script skips plugin skills; development.md blames iCloud for MSB4242; create-agent/skill route policy to AGENTS.md."
type: watch
last_verified: 2026-11-20
---

# Watch list

**Dogfooding — re-checked 2026-11-20**

- **The Claude desktop bundle runs the published line.** Its `foundation`, `engineering` and
  `product` read `14.3.1`, author FrostAura Technologies, and their skill and agent trees match
  this repo's `plugins/` file for file (re-compared 2026-11-20, `diff -rq` on `skills/`). The kill
  criterion ("stops being what FrostAura builds with") is not tripping.
- **The CLI channel is the root store's concern** — whether `fa-*` names resolve there is tracked
  in [`../../../../memory/plugin-roster-drift.md`](../../../../memory/plugin-roster-drift.md), not here.

**Shipped defects in the product itself — all live in published `14.3.1`**

- **A fourteenth version site, and it is wrong.** `src/Gaia.Mcp.Server/Program.cs` sets the
  `Implementation.Version` advertised on every MCP `initialize`; it reads `13.0.0`, last moved
  by the v13.0.0 commit. Neither the release loop in `../docs/development.md` nor any CI check
  names it. Two cheap exits, neither taken: fold it into the loop, or version the server
  independently (`../CLAUDE.md` already treats them as separate concerns).
- **`fa-foundation-memory-maintenance`'s `description` is 1,038 characters, over the 1,024 cap**
  that `docs/development.md` sets, measured with that doc's own check #4 (2026-11-20). Same
  length on `origin/main` since `c6e8e44` (2026-09-11). It still loads today; trimming it is a
  plugin change needing the lockstep bump.
- **`docs/development.md` (the `MSBuildEnableWorkloadResolver` paragraph) blames an
  iCloud-synced path** for the workload-resolver crash; the verified cause is the machine's broken
  workload set ([`gotchas.md`](gotchas.md)). A shipped contributor doc, so the fix is a release.
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

- **This repo is public and its context layer is not written as if it were** — `CLAUDE.md` names
  the owner, the decision topics name the parent's internal structure and a killed internal
  project, all pushed. Genericize deliberately, or accept it deliberately.
- **A 2 MB `README.icon.png` is committed at repo root**, referenced by absolute GitHub raw URL
  anyway. History is permanent; removing it now only stops it growing.
