---
name: technologies-fa-gaia-decisions-roster
description: "Unratified until merged: 15.0.0 folds five stack skills and two test-lane skills into references under two survivors, and cuts every description's how-clause, because a crowded install was dropping descriptions from the listing."
type: decision
last_verified: 2026-11-21
---

# Live decisions — the skill roster

- **Variants of one procedure are references under one skill** (2026-11-21, 15.0.0 branch — an
  agent's call on a scheduled run, unratified until the founder merges it). The five stack baselines
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
- **Retired names get no alias.** A skill directory left behind to redirect would cost the same
  listing entry the merge removed. Consuming instruction files cite capabilities with the skill
  name "as an example only", which is what makes a rename survivable; `CHANGELOG.md` carries the map.
- **The checks moved into CI as a script, not as `claude plugin validate`.** The runner has no
  Claude Code CLI. `scripts/validate-plugins.py` asserts the invariants that have actually broken
  here; the full manifest schema is still a by-hand `--strict` run before a release.
