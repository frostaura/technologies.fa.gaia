---
name: ai-toolkit-gaia-watch
description: "Shipped defects still live in 14.3.1: the MCP server advertises 13.0.0, the audit script never checks the plugin skills, create-agent/create-skill route policy into AGENTS.md, Playwright MCP is unpinned."
type: watch
last_verified: 2026-10-14
---

# Watch list

**Dogfooding — re-checked 2026-10-14**

- **The Claude desktop bundle runs the published line.** Its `foundation`, `engineering` and
  `product` read `14.3.1`, author FrostAura Technologies, and their skill and agent trees match
  this repo's `plugins/` file for file — the 13.0.0 lag recorded on 2026-09-16 closed when the
  bundle re-fetched after the push. The kill criterion ("stops being what FrostAura builds
  with") is not tripping.
- **The Claude Code CLI store still holds no FrostAura plugin** (`installed_plugins.json` lists
  only `claude-plugins-official` entries), so on that channel every `fa-*` name resolves to
  nothing — [`../../../../memory/plugin-roster-drift.md`](../../../../memory/plugin-roster-drift.md).
- **Repo and running service may disagree, and nothing here can tell** — CI builds without
  deploying ([`questions.md`](questions.md) §1).

**Shipped defects in the product itself — all live in published `14.3.1`**

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

- **v13 deliberately deleted 15 tracked files** (tasks/memory/evolve sources, stores, validator,
  schema docs, a resolved alert topic). A range comparison against an older ref shows them.
  **Expected and enumerated; never turn it into a restore.**
- **This repo is public and its context layer is not written as if it were** — `CLAUDE.md` names
  the owner, the decision topics name the parent's internal structure and a killed internal
  project, all pushed. Genericize deliberately, or accept it deliberately.
- **A 2 MB `README.icon.png` is committed at repo root**, referenced by absolute GitHub raw URL
  anyway. History is permanent; removing it now only stops it growing.
