# Catalog

> **Snapshot taken 2026-11-21 against `15.0.0`.** This page is a hand-maintained snapshot, not the source of truth. The **live roster is `/plugin` in your client** (Claude Code: `/plugin`; Copilot CLI: `copilot plugin list`) — it enumerates exactly what you have installed, at the version you have it. Where this page and your client disagree, your client is right. Anything not listed here may simply be newer than the date above.

Nothing routes off this page: skills fire from their own `description`, so you invoke a capability by describing the job, not by looking up a name. The names below exist for when you want to call one explicitly.

## Plugins

The method lives in the skills. An agent exists only where something needs a context of its own: an orchestrator per plugin, and a judge that did not write what it judges.

| Plugin | What it covers |
| --- | --- |
| **`foundation`** | The context layer and authoring base: establishing and maintaining instruction/memory files across a tree, auditing them, judging repository durability, and authoring new skills, agents and plans. Required by the other two. |
| **`engineering`** | Spec-driven software delivery end-to-end: intake, architecture documentation, planning, implementation, UI, testing, containerization and deploy — plus per-language repository baselines. |
| **`product`** | A money-gated lifecycle for consumer one-off / in-app-purchase products: discovery through launch and live-ops, every stage evaluated against one shared net-of-fee unit-economics model. |

## foundation — skills

| Skill | When it fires |
| --- | --- |
| `fa-foundation-optimize-directory-tree` | A tree has no context layer, or one that was never derived from what its projects actually are — establish it, maintain it against source, or sweep it lean. |
| `fa-foundation-context-authoring` | One scope's instruction file and `MEMORY.md` topic store, inside a cascade that already exists. |
| `fa-foundation-memory-maintenance` | One scope's memory store is structurally sound but stale and needs a deep refresh. |
| `fa-foundation-context-audit` | Sweep a whole repository's context layer for drift against inspected reality. |
| `fa-foundation-registry-audit` | Reconcile a registry of scopes against the directories that actually exist on disk, both directions. |
| `fa-foundation-session-close` | A session shipped, decided, discovered, abandoned or unblocked something and must be closed out. |
| `fa-foundation-repo-durability` | Establish whether a repository is genuinely durable and safe to push, by running commands rather than trusting a claim. |
| `fa-foundation-create-skill` | Author, revise or retire a `SKILL.md`. |
| `fa-foundation-create-agent` | Author, revise or retire an agent definition. |
| `fa-foundation-create-plan` | Research and outline a multi-step plan before work starts. |

## foundation — agents

| Agent | Role |
| --- | --- |
| `fa-foundation-context-auditor` | Reconciles **one** scope's context layer; invoked once per scope during a sweep. |
| `fa-foundation-repo-durability-auditor` | Judges durability and push-safety across one or many repositories. |

## engineering — skills

| Skill | When it fires |
| --- | --- |
| `fa-engineering-process` | Coordinating the end-to-end workflow, QA checkpoints and release gates inside a repository. |
| `fa-engineering-architecture` | Architecture docs must be written, aligned before structural change, or documented from source where no baseline exists. |
| `fa-engineering-planning` | Turning approved architecture into a branch-aware, gated task plan. |
| `fa-engineering-implementation` | Delivering planned tasks against existing repo conventions. |
| `fa-engineering-ui` | React UI work held to the design system and semantic tokens. |
| `fa-engineering-testing` | Formal validation across unit, integration, regression and evidence review — with browser end-to-end specs and the manual API and web regression lanes carried as references. |
| `fa-engineering-default-tech-stack` | Stack choice is open, or a new application's stack is being bootstrapped from scratch. |
| `fa-engineering-containerization` | Compose-first containerization for a service with an HTTP surface. |
| `fa-engineering-deploy-chain` | A CI workflow carries build-and-deploy jobs but nothing actually publishes or redeploys. |
| `fa-engineering-stack-baseline` | A repository has no enforced lint, no single test command or a CI job that guards nothing — one procedure, with a reference per stack: JS/TS web, .NET HTTP API, .NET MAUI (plus device build and deploy), Flutter, Python. |

## engineering — agents

| Agent | Role |
| --- | --- |
| `fa-engineering-delivery-lead` | Carries one request from raw ask to tested change in its own context, orchestrating the skills above and fanning independent branches out. |
| `fa-engineering-verifier` | The independent ready / not-ready / blocked call on work it did not write. Cannot edit files. |

## product — skills

| Skill | When it fires |
| --- | --- |
| `fa-product-process` | Coordinating the 10-stage money-gated lifecycle. |
| `fa-product-money-gate` | Evaluating a stage gate on net-of-fee economics: advance, loop back, or kill. |
| `fa-product-unit-economics-model` | Creating or re-running the single shared, versioned economics model. |
| `fa-product-discovery` | Stage 1 — trends, opportunity sourcing, demand signals, sizing. |
| `fa-product-ideation` | Stage 2 — divergent ideation down to one concept brief. |
| `fa-product-monetization-design` | Stage 3 — model, price ladder, catalogue, economy, funnel. |
| `fa-product-validation` | Stage 4 — falsifiable money hypotheses tested under a cost ceiling. |
| `fa-product-vertical-slice` | Stage 5 — the spec stack and a playable/usable slice. |
| `fa-product-production-hardening` | Stage 6 — content, localization, device matrix, anti-fraud, QA. |
| `fa-product-compliance` | Stage 7 — ratings, store submission, legal, kids/privacy, tax. |
| `fa-product-soft-launch` | Stage 8 — telemetry, always-green trunk, soft-launch geos. |
| `fa-product-gtm-launch` | Stage 9 — pricing lock, ASO, creators, paid UA, CAC vs LTV. |
| `fa-product-liveops` | Stage 10 — the steady-state revenue engine. |
| `fa-product-portfolio-retrospective` | Stage 10 closure — sunset, harvest, calibrate, recycle into discovery. |

## product — agents

| Agent | Role |
| --- | --- |
| `fa-product-manager` | Runs the 10 money-gated stages through their skills, owns the unit-economics model, merges review corrections and gates. |
| `fa-product-reviewer` | Adversarially reviews each stage's output; run as two or more independent instances. Read-only. |

---

Counts as of the snapshot date: **3 plugins · 34 skills · 6 agents**. The plugins are the product; the MCP server in [`../src/`](../src) is a separate concern and its tools are catalogued in [`../src/README.md`](../src/README.md), not here. Changes are recorded in [`CHANGELOG.md`](../CHANGELOG.md); maintenance of this page is described in [`development.md`](development.md).
