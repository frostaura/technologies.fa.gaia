---
name: technologies-fa-gaia-questions
description: "Mostly founder-owned: does the hosted service run at all, and on what image; one repo, two products; six Technologies rules it does not yet follow since the move; ref:main vs tags; unassigned: are per-plugin reference variants intended."
type: question
last_verified: 2026-11-20
---

# Open questions

Every item here except §6 is **founder-owned**. Placement, brand and public-distribution calls are
parent-controlled under `decision-rights.md`; an agent recommends and escalates, it does not
decide. The Woolworths exposure has its own home and is not restated here:
[`questions-woolworths.md`](questions-woolworths.md).

1. **Is the hosted service serving at all, and on what image?** Owner: founder — he holds the
   Docker Hub, Portainer and Cloudflared access, and nothing in this repository can answer it.
   The endpoint is not serving (the reading and its dates are in [`state.md`](state.md)), so the
   first question is whether it runs at all. CI has no deploy step, so the 2026-09-16 push built a
   v14 image and deployed nothing. Until
   someone checks the running `tools/list`, the version is *unknown*, not stale — and the obvious
   shortcut does **not** work: the server advertises `13.0.0` on `initialize` from source, so a
   freshly built `14.3.2` image reports `13.0.0` too ([`watch.md`](watch.md)). Only the tool set
   distinguishes them.

2. **This repository ships two unrelated products.** A developer-delivery plugin suite and a
   grocery integration gateway share a repo, a CHANGELOG, a version line and a hostname. Three
   honest exits: leave it and say so in the README; split the server into its own repository; or
   reframe Gaia deliberately as both. The published `foundation` MCP wiring (§5) already couples
   them in the shipped product without anyone having decided it. Owner: founder.

3. **Which Technologies division rules should bind it?** Placement itself is settled: the founder
   moved it from Labs on 2026-11-20 ([`state.md`](state.md)). It arrived shaped by Labs, and
   departs from these Technologies rules (re-read 2026-11-20). Sanction each or correct it:
   - **Repo shape:** no `Makefile`, no `docker-compose.yml`, server at `src/Gaia.Mcp.Server`.
   - **Numbered doc taxonomy:** no `UC-`, `ARCH-` or `TEST-` file under `docs/`.
   - **Deploy chain:** CI publishes to Docker Hub and stops; the deploy is recorded nowhere.
   - **Stack deviation as an open decision with an owner:** recorded as settled ([`decisions.md`](decisions.md)).
   - **Project schema:** `../CLAUDE.md` keeps Labs' owner, milestones and kill-criteria sections
     (kill criterion 2 still imagines a move) and has no *Dependencies* or *Skills* section.
   - **Revenue mandate:** free and MIT, so it reaches no paying user; is it an internal command system?
   Owner: founder; the schema item is a context-authoring pass once he rules.

4. **`ref: main` or tags for plugin refs?** Floating installs are dangerous for a public user
   base: a breaking change reaches every fetching install at push time, with no version a user
   can pin to and — because the release path creates no tags at all ([`state.md`](state.md)) —
   nothing to roll back to. Owner: founder. Decided either way, the README should say which.

5. **Should the integration be wired into any plugin at all?** It now is: the re-wiring commit
   published in v14 on 2026-09-16, contradicting the v13.0.0 reasoning without ever arguing with
   it. If the answer is yes it wants its own opt-in plugin rather than the context layer; if no,
   the revert is a further release. Either way the README's "the plugins send nothing anywhere"
   disclosure is currently untrue for `foundation`. Owner: founder.

6. **Are the same-named `references/` docs meant to be per-plugin variants?** `delivery-policy.md`
   (engineering, product) and `ownership-and-conventions.md` (all three) now differ in content and
   title per plugin. If intended, the `CLAUDE.md` invariant stands as rewritten 2026-10-22 (carry
   shared doctrine, never sync wholesale); if drift, one source needs choosing. Owner: unassigned.
