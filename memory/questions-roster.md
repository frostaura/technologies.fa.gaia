---
name: technologies-fa-gaia-questions-roster
description: "Founder-owned, from the 2026-11-21 clean-up: which skills should go (create-plan, registry-audit, the fa-gaia-remote wiring), which should merge, and what to bring in — an audit hook, plugin evals, two missing delivery skills."
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
  script, so close-out stops depending on an agent remembering; whether `skills:` preloading resolves a bare skill name inside a plugin (the 15.0.0 orchestrators use it; a miss only logs a
  debug warning, so nobody has seen it work); `plugin eval` cases for the triggers; a
  `userConfig` prompt if the Woolworths wiring stays; a security-review and a database-migration skill
  for `engineering`, the two delivery steps it has no playbook for.
