---
name: ai-toolkit-gaia-questions
description: "Mostly founder-owned: does the hosted service run at all, and on what image (only tools/list can tell); one repo, two products; placement reads as Technologies; ref:main vs tags; unassigned: are per-plugin reference variants intended."
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
   freshly built `14.3.1` image reports `13.0.0` too ([`watch.md`](watch.md)). Only the tool set
   distinguishes them.

2. **This repository ships two unrelated products.** A developer-delivery plugin suite and a
   grocery integration gateway share a repo, a CHANGELOG, a version line and a hostname. Three
   honest exits: leave it and say so in the README; split the server into its own repository; or
   reframe Gaia deliberately as both. The published `foundation` MCP wiring (§5) already couples
   them in the shipped product without anyone having decided it. Owner: founder.

3. **Placement still reads as `Technologies/`, not Labs.** This is a versioned, publicly
   distributed, multi-ecosystem developer product with a live hosted service, CI/CD, a support
   address and no research character left. A credential-handling gateway is an operations
   concern. It is also the only Labs program with a granted stealth exception — the signature
   of something that already graduated. **Strengthened 2026-09-16:** it is now demonstrably in
   live use on the founder's own desktop surface, at the published version ([`watch.md`](watch.md)), which retires the
   last argument that it had not graduated in practice. Owner: founder; parent-controlled, so
   this program recommends and does not move itself.

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
