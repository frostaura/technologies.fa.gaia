---
name: technologies-fa-gaia-questions-roster
description: "Founder-owned, from the 2026-11-21 clean-up: which skills should go (create-plan, registry-audit, the fa-gaia-remote wiring), which should merge, and what to bring in — hooks, skills preloading on agents, plugin evals."
type: question
last_verified: 2026-11-21
---

# Open — what leaves the plugins and what joins

**What should leave the plugins, and what should come in?** Raised by the 2026-11-21 clean-up,
which did the consolidation that kept every procedure and left these for a ruling. Owner: founder.
- *Candidates to go:* `fa-foundation-create-plan` (the one skill outside the house template; a
  three-planner fan-out that overlaps the client's own plan mode and `fa-engineering-planning`);
  `fa-foundation-registry-audit` as a separate skill (the script's registry pass already runs
  inside `fa-foundation-context-audit`); the `fa-gaia-remote` wiring in `foundation` ([`questions.md`](questions.md) §5); the
  empty `mcpServers` in `product`; the `ExampleTools`/`SamplingTools` demos in the server.
- *Candidates to merge:* `fa-product-liveops` with `fa-product-portfolio-retrospective` (one stage,
  one agent); `fa-foundation-memory-maintenance` into `fa-foundation-context-authoring`.
- *Candidates to bring in:* a `SessionStart`/`Stop` hook in `foundation` that runs the audit
  script, so close-out stops depending on an agent remembering; `skills:` preloading on the stage
  agents instead of "Skills to invoke" prose; `plugin eval` cases for the triggers; a
  `userConfig` prompt if the Woolworths wiring stays; shorter agent descriptions (twenty at about
  950 characters each, loaded every session); a security-review and a database-migration skill
  for `engineering`, the two delivery steps it has no playbook for.
