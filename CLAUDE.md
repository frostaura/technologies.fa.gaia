# technologies.fa.gaia — Gaia

## What this product is
FrostAura's spec-driven AI development toolkit, shipped as **three installable plugins** — `foundation` (the context layer: establishing it across a whole tree, authoring, memory, session close-out, auditing, repo durability), `engineering` (delivery) and `product` — for **both** Claude Code and GitHub Copilot. The plugins carry the skills and agent definitions that encode FrostAura's delivery method (intake → architecture → planning → engineering → testing → release), and they are **self-contained**: the plan is the session's native todo list, and everything durable is files in the consuming repository. Gaia is simultaneously the tool FrostAura uses and a public developer product. It began as the Labs program `ai.toolkit.gaia`, whose research question — can a spec-driven, role-decomposed agent workflow with an enforced completion contract deliver software more reliably than ad-hoc prompting — was answered yes in practice. As a Technologies product, no Labs rule (research question, stealth, graduation gate) binds it.

The repository also holds a small .NET 10 MCP server, whose deployment target is `https://gaia.frostaura.net/mcp`, which exposes **third-party consumer integrations** as agent tools and a REST API. **The server and the plugins are separate concerns and neither requires the other.** Its only integration is Woolworths South Africa grocery, migrated whole from the retired `technologies.fa.integrations`. Whether that endpoint is serving, which image it runs, and whether any shipped plugin wires it are all state, and belongs to [`MEMORY.md`](MEMORY.md) — check there before assuming either way. That the two live in one repository under one brand is a real coherence question, recorded as open in `MEMORY.md`, not settled here.

## Stack & repo
`github.com/frostaura/technologies.fa.gaia` (public). **.NET 10 only — no database, no ORM, no frontend, no persistence of any kind.** The server is stateless by design: no credential store, no data directory. This is a declared deviation from the mandated stack, recorded with its why in [`memory/decisions.md`](memory/decisions.md) — and it stays declared even though this repo ships the `fa-engineering-default-tech-stack` skill that holds every other project to that stack.

Layout: `plugins/{foundation,engineering,product}/` hold the shipped skill and agent definitions; `src/Gaia.Mcp.Server/` holds the MCP server (`Integrations/` for the provider-neutral seam and each provider, `Tools/` for the `[McpServerToolType]` classes — the Woolworths tools plus the `ExampleTools` and `SamplingTools` demos); `src/Gaia.Mcp.Tests/` holds the xUnit suite; `.claude-plugin/` and `.github/plugin/` hold the two marketplace manifests. `scripts/` at the repository root holds repository tooling that is **not shipped** (`validate-plugins.py`) — distinct from `plugins/foundation/scripts/`, which is. Every plugin carries `skills/`, `agents/` and `references/`; only `foundation` additionally carries `scripts/` (the shipped `context-audit.py`).

## Owner & key people
Dean Martin (founder). Gaia is the delivery substrate for every other FrostAura project, which makes its blast radius larger than its LOC suggests.

## Milestones
1. **Two-ecosystem distribution** — installable and working in both Claude Code and GitHub Copilot from a published marketplace.
2. **Hosted MCP reliability** — the remote server handles other people's provider credentials in transit, so it must behave like a service, not a prototype.
3. **A real test suite** — see kill criteria; a delivery-discipline product with no tests of its own is a credibility problem, not just a quality one.

## Kill criteria
- The workflow stops being what FrostAura actually builds with. Gaia's whole justification is that it is dogfooded; the day it is not, it is dead weight.
- The hosted MCP cannot be operated to service standards and no one is willing to move it to a division that can.
- Maintaining plugin parity across two ecosystems costs more than the second ecosystem returns.

## Conventions & invariants
- **Every skill and agent is named `fa-<plugin>-<name>`, and a skill's directory name must equal its frontmatter `name`.** The loader matches on the directory; a mismatch silently produces a skill that cannot be invoked. Renaming one therefore means moving the directory, editing the frontmatter and repairing every cross-reference in the same pass.
- **One procedure with variants is one skill with references, not several skills.** Per-stack baselines and per-lane test procedures live under a single skill's `references/` and are loaded only when that variant is in front of the agent. A new sibling skill has to own a trigger of its own, because every description is paid for by every session — see the next rule.
- **A description states what, when and the boundary — never how.** All installed descriptions share one listing budget, and a client over it drops descriptions while still listing the names. `validate-plugins.py --budget` prints the total; it should fall with each release, not rise.
- **The method is the skills; an agent needs a reason a skill cannot give.** An agent definition earns a file only for a context of its own (an orchestrator, or a worker fanned out over disjoint scopes), for independence (a judge that did not write what it judges), or for a tool restriction. One orchestrator per plugin plus its independent judge is the ceiling; a role whose body is "follow skill X" is that skill with a hand-off in front of it.
- **A skill's `description` is a trigger, not a summary.** It is the only thing that decides whether the skill ever fires. This is not stylistic: a generation of these files shipped with frontmatter whose opening `---` was missing, which made every description parse as the literal string `name: <skill>` — inert, while still looking present in a listing.
- **Markdown links never escape the plugin root, but scripts are referenced with `${CLAUDE_PLUGIN_ROOT}`.** Both rules hold at once: the first governs relative links between skills and references, the second is how a skill invokes a file under `plugins/<name>/scripts/`.
- **The plugins are the product.** A change to a skill or agent definition ships to every installed user on the next resolve — treat plugin content edits with production seriousness. `src/` is not supporting infrastructure for them; it is an independent service that happens to share the repository.
- **A push to `main` is a release.** Installs float on `ref: main` rather than a tag ([`memory/decisions-distribution.md`](memory/decisions-distribution.md)), so any breaking change to a skill or agent contract lands on users the moment it is pushed.
- **The completion contract is the point, and only the skills enforce it.** Tasks cannot complete with unresolved blockers, missing proof, or unsatisfied gates; no server refuses a breach any more ([`memory/decisions.md`](memory/decisions.md)). Do not add an escape hatch to make a workflow feel smoother — the friction is the feature, and weaker enforcement is a reason to write it more literally, not less.
- **Never reintroduce a hosted store for plans, memory or lessons.** It was removed deliberately, and the plugins' independence from any server is a property worth protecting.
- **The two marketplace manifests must agree.** `.claude-plugin/marketplace.json` and `.github/plugin/marketplace.json` describe the same product to two ecosystems, and every plugin additionally has a byte-identical duplicate `plugin.json` at two paths. `scripts/validate-plugins.py` asserts both, along with every definition's frontmatter, name and links, and the `Validate Plugins` workflow runs it on every push and pull request — run it locally before pushing, because a push to `main` is already a release by the time CI goes red.
- **Hosted-service disclosure is a commitment.** The README states that the plugins send nothing anywhere and the server stores nothing at all — no credentials, no data, no session reuse. Do not add persistence of any kind, or credential caching of any kind, without changing that statement in the same change.
- **The integration invariants are inherited, load-bearing, and non-obvious.** Add cart items one at a time — the upstream batch endpoint discards the whole batch if any one product is unavailable, and returns HTTP 200 while doing it. Never trust an upstream status code; inspect the body. Search and preview must stay anonymous. MCP errors must be `McpException` or the SDK replaces the text with a generic message. Full reasoning and the captured endpoint contract: [`docs/integrations/`](docs/integrations/architecture.md).
- **Same-named reference docs are per-plugin variants, not copies.** The plugin format forbids links escaping the plugin root, so `delivery-policy.md` and `ownership-and-conventions.md` each exist in more than one plugin's `references/` — but each is tailored to its plugin, and no `.md` file under `plugins/` is byte-duplicated. When shared doctrine changes in one, carry the change into every same-named sibling where that doctrine appears; never sync them wholesale, which would overwrite the per-plugin content. Whether the variants are intentional is open in `MEMORY.md`.

## Build / test / run
| Task | Command |
| --- | --- |
| Build | `dotnet build Gaia.slnx` — on the founder's Mac prefix every `dotnet` command with `MSBuildEnableWorkloadResolver=false`, or it fails with MSB4242 (`memory/gotchas.md`) |
| Test | `dotnet test Gaia.slnx` — runs `src/Gaia.Mcp.Tests`; how far back a green result means anything is in `memory/gotchas.md` |
| Run (HTTP) | `dotnet run --project src/Gaia.Mcp.Server` — the web host is the default; serves `/mcp` and `/api` |
| Run (stdio) | `MCP_TRANSPORT=stdio dotnet run --project src/Gaia.Mcp.Server` — without the variable `Program.cs` starts the HTTP web host instead, so a stdio client gets no MCP server on its pipe at all |

The MCP server image is published to Docker Hub as `<namespace>/technologies.fa.gaia` (`:latest` plus a tag per commit SHA) by `.github/workflows/build-gaia-mcp.yml`. The namespace comes from a CI secret, so the full reference is not discoverable from the repo alone; what it resolved to is in `MEMORY.md`.

## Where docs live
The README is the entry point and is deliberately an **install-and-first-run document, not a catalog** — a hand-maintained roster in it goes stale faster than anyone maintains it, so skills are listed only in `docs/catalog.md`, which opens by dating itself and pointing at `/plugin` as the live roster. `docs/development.md` is the contributor layer: releases and the version sites, manifest agreement, local-clone installs, authoring invariants and the pre-ship checks. `AGENTS.md` is an **interop pointer at this file and carries no policy of its own** — if it starts explaining rules rather than pointing at them, delete the explanation. Any status, version or count claimed in any of them is `MEMORY.md`'s to confirm; read it before trusting one.

## Never do this here
The invariants above are not repeated here; these are the damaging actions they do not already name.

- Never store, log, cache or echo back a caller's provider credential, and never expose the server over plain HTTP — TLS is the only thing protecting credentials in transit.
- Never put a checkout or payment step behind an automated call; this service fills a cart and stops, deliberately.
- Never change the MCP session mode without re-running the header-credential probe in `memory/gotchas.md`.

## Upkeep

This file, `MEMORY.md`, its `memory/` topic store, and the skills that fire at this level are kept current **as changes land**, not in a later cleanup pass. `MEMORY.md` is required here exactly as this file is, and it cascades downward on identical terms — an instruction file with no `MEMORY.md` beside it is a defect, not a shortcut: the rules are stated and reality is left unstated, so the next agent infers status instead of reading it. Both files, or neither.

- **Memory — always.** Update the topic files at the end of any session that shipped, decided, discovered, abandoned or unblocked something; re-cut the `description:` of any topic whose signal moved, then regenerate `MEMORY.md` from the topic files rather than editing it — `python3 .claude/scripts/audit-tree.py --no-git --fix-index --scope Technologies/projects/technologies.fa.gaia` from the tree root (it regenerates this index only; the roster row in `Technologies/projects/memory/state.md` is edited by hand in the same pass); restamp `last_verified:` only for what you actually re-inspected. Record decisions *with their why* — a decision without its rationale is reversed by the next agent, who sees only its cost.
- **This file — only when a rule changed.** A new convention, command or invariant earns an edit. A status change does not; it belongs in the memory store.
- **Skills — when *how* the work is done changed.** Fix or delete a skill whose commands or thresholds no longer exist; a stale skill is worse than a missing one because it fires with authority. A procedure that would be correct in a repository with nothing to do with this tree belongs upstream in a plugin, never forked into this tree.
- **Scratch — always.** Empty `.tmp/` before the session ends, promoting anything that still mattered first.

None of these four are assessed by search. Read the scope's files end to end before changing any of them. Drift is not caused by neglect over months; it is caused by good sessions that ended without a close-out.
