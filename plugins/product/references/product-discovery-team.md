# Product Lifecycle — Architecture

The Gaia product plugin takes a CONSUMER software
product (one-off purchase or in-app / in-game purchase — never B2B seat-based
SaaS, never auto-renew without an explicit recorded in-scope decision) from idea
to a money-validated bet, through launch, and into live-ops. It runs a
**10-stage, money-gated lifecycle** in which every stage exits only on a
willingness-to-PAY gate.

## The 10-stage money-gated lifecycle

| # | Stage | Exit condition (gate) |
|---|---|---|
| 1 | Discovery | Opportunity Thesis + unit-economics model v0 + GO / NO-GO / PIVOT |
| 2 | Ideation | ONE concept with a committed monetization hypothesis; the rest killed or parked |
| 3 | Monetization design | Net LTV:CAC ≥ 3:1 with payback + cashflow check |
| 4 | Validation | Deflated WTP + ≥1 money-on-the-line signal; measured CPI replaces placeholder CAC |
| 5 | Vertical slice / MVP | Lovable core loop + live sandbox IAP granting an entitlement + clean funnel event |
| 6 | Production & hardening | Feature/content-complete with a production-grade IAP/entitlement path |
| 7 | Compliance & certification | Signed compliance certificate (ratings, loot-box law, privacy, tax, legal docs) |
| 8 | Soft-launch | Real retention AND real spend in cheap geos; multi-condition scale gate |
| 9 | Go-to-market & UA | Repeatable acquisition engine; positive defensible blended CAC:LTV |
| 10 | Live-ops & portfolio | Steady-state NET revenue engine; sunset / maintenance / sequel decision compounding back to Stage 1 |

Gates are pre-registered before evidence lands, scored NET of the platform fee
each channel actually pays plus refunds, chargebacks, fraud, and tax, and route
failures backward along explicit loop-back edges — or kill the bet. The gate
discipline is `fa-product-money-gate`; the lifecycle contract is
`fa-product-process`.

## Two agents, fourteen skills

The expertise for each stage is a **skill**; it is not a role. Two agents exist
because two things need a context of their own:

| Agent | Why it is an agent |
|---|---|
| `fa-product-manager` | Orchestrates the stage skills across a long run without filling the invoking session's context; the only writer of the shared model; gates and routes loop-backs |
| `fa-product-reviewer` | Judges an artifact it did not write, from a fresh context, with no write or execute tools; run as ≥2 independent instances |

The main session can also run the lifecycle directly by following
`fa-product-process`; the manager is that same procedure in its own context.

| Stage | Skill |
|---|---|
| 1 | `fa-product-discovery` |
| 2 | `fa-product-ideation` |
| 3 | `fa-product-monetization-design` |
| 4 | `fa-product-validation` |
| 5 | `fa-product-vertical-slice` |
| 6 | `fa-product-production-hardening` |
| 7 | `fa-product-compliance` |
| 8 | `fa-product-soft-launch` |
| 9 | `fa-product-gtm-launch` |
| 10 | `fa-product-liveops`, then `fa-product-portfolio-retrospective` |

## Produce → adversarial review → synthesis → gate

Every stage runs the same pattern:

1. **Produce** — the manager follows the stage skill. Tracks with no data
   dependency fan out as concurrent general-purpose subagents launched in a
   single message, each briefed with the stage skill's name, the run brief, the
   current model version, the pre-registered thresholds and its own disjoint
   output file. Long-running work (scans, experiments) runs in the background;
   the manager awaits only the results that gate the stage decision.
2. **Adversarial review** — ≥2 independent `fa-product-reviewer` instances,
   launched in parallel (never sequentially, never shown each other's output),
   attack the artifact for gross-instead-of-net economics, un-deflated WTP,
   moved goalposts, smuggled subscriptions, and unsupported claims, emitting
   traceable `CORRECTION from review:` notes. Reviewers never coordinate with
   each other and never rewrite the artifact.
3. **Synthesis** — the manager merges the tracks and the corrections into ONE
   coherent artifact, retaining every correction visibly and adding no new
   analysis at this step.
4. **Gate** — the manager applies `fa-product-money-gate`: PASS →
   auto-advance; FAIL on a fixable lever → loop-back to the stage that owns
   the lever; uneconomic after honest net math → kill.

Work is parallel-safe within a stage, never across a causal gate — the money
gate is a hard barrier. Only true dependencies serialize, and a plan that
serializes independent work is a defect. Concurrent artifact edits get disjoint
file scopes per agent — two agents in one scope overwrite each other;
overlapping scopes require isolated git worktrees merged deliberately. Parallel
branches are registered as sibling todo items with per-item gates, blockers,
and proof, so they complete independently.

## The shared unit-economics model

One versioned model (`fa-product-unit-economics-model`) is the passed state of the whole
lifecycle: initialized as v0 in Discovery, advanced whenever a measured input
(CPI, WTP, ARPPU, retention) replaces an assumption, and re-run at every gate.
The manager is its only writer; every stage reads it and returns measured
inputs; nobody re-derives it privately. All revenue in it is NET of store
commission (at the tier each actual channel pays), refunds, chargebacks, fraud,
and tax. The schema lives at
[`../skills/fa-product-unit-economics-model/references/model-schema.md`](../skills/fa-product-unit-economics-model/references/model-schema.md).

## Handoff out of the plugin

A validated bet leaves this plugin for software construction via the
engineering plugin (`fa-engineering-delivery-lead`). This plugin decides WHAT earns a build and proves it makes
money; it does not run final code delivery or release gating.
