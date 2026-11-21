---
name: technologies-fa-gaia-decisions-roster
description: "Shipped in 15.0.0, founder-merged: seven skills folded into references and twenty agents cut to six — an orchestrator per plugin plus an independent judge — because a crowded install dropped descriptions and role hand-offs bought nothing."
type: decision
last_verified: 2026-11-21
---

# Live decisions — the skill roster

- **Variants of one procedure are references under one skill** (2026-11-21, `15.0.0` — an
  agent's call on a scheduled run, ratified when the founder merged PR #60 the same day). The five stack baselines
  and the two test-execution lanes were demoted, not deleted. **Why:** each restated one shared
  procedure, and every description is charged to every session — with the full set installed, a
  client was already dropping `foundation`'s and most of `product`'s descriptions from its listing,
  which is the "inert while looking present" failure in a new form. **Why `product`'s fourteen and
  `foundation`'s ten were left alone:** `product`'s stage agents invoke their stage skill by name, so
  folding stages into one skill would make a leaf agent load the coordinator's playbook to find its
  own; `foundation`'s are distinct procedures with distinct triggers. Their descriptions were
  trimmed instead (the *how* clause cut, the triggers kept).
- **A description states what, when and the boundary; the how is the body's.** Every skill's
  "Use it by…" clause was cut, and `product`'s stage descriptions lost the enumeration of their
  playbook. 36.4k characters across 40 skills became 18.8k across 34. **Why not shorter still:** the
  triggers were the founder's wording and an unattended run should not rewrite them by hand.
- **Twenty agents became six: an orchestrator per plugin, plus the judge** (2026-11-21, same
  release). The founder's steer, given as a suggestion with the call left to the agent: agents are
  probably not needed at all, unless one orchestrates a skill set. Taken most of the way.
  `fa-engineering-delivery-lead` and `fa-product-manager` wear each phase's skill in turn;
  `fa-engineering-verifier` and `fa-product-reviewer` judge work they did not write and cannot
  edit; `fa-foundation-context-auditor` and `-repo-durability-auditor` stay as they were.
  **Why not zero:** three properties are structural and no skill provides them — a separate
  context, independence of the judge, and a tool restriction. The completion contract is enforced
  by nothing mechanical, so an author grading its own work is the one hand-off worth keeping.
  **Accepted cost:** the retired role bodies held decision trees and routing tables; only the
  loop-back edges were carried into the orchestrators, on the judgement that the skills hold the rest.
- **Retired names get no alias.** A skill directory left behind to redirect would cost the same
  listing entry the merge removed. Consuming instruction files cite capabilities with the skill
  name "as an example only", which is what makes a rename survivable; `CHANGELOG.md` carries the map.
- **The checks moved into CI as a script, not as `claude plugin validate`.** The runner has no
  Claude Code CLI. `scripts/validate-plugins.py` asserts the invariants that have actually broken
  here; the full manifest schema is still a by-hand `--strict` run before a release.
