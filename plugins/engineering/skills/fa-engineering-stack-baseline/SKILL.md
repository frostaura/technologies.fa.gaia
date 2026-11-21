---
name: fa-engineering-stack-baseline
description: Provides the per-stack repository baseline — a lint and format gate that fails rather than reports, one runnable test command, and a command surface CI calls verbatim — for JavaScript/TypeScript web, .NET HTTP API, .NET MAUI, Flutter and Python repositories, plus MAUI device build and deploy. Use it when a repository has no enforced lint, no single test command, a CI job that guards nothing, or before feature work that needs a gate; and before installing a MAUI build on an emulator, simulator or device. It never chooses the stack — that is `fa-engineering-default-tech-stack`.
license: MIT
---

# Stack Baseline

## Scope and when to use

Use this skill to bring a repository up to a foundation that lint, test and CI can stand
on, without rewriting choices it already made. The procedure is the same for every stack;
the contract — which files, which commands, which traps — is per stack and lives in one
reference each. **Read only the reference for the stack in front of you.**

Use this skill when:

- a repository has no enforced lint or format gate, or one that only warns
- tests exist but there is no single canonical way to run them, or CI runs something else
- a new application is being bootstrapped from an empty or near-empty tree
- feature work is about to start and there is nothing to gate it with
- a MAUI build must be installed or launched on an emulator, simulator or physical device

Do not use this skill when:

- the stack itself is still undecided — choosing between stacks belongs to `fa-engineering-default-tech-stack`
- the gap is the container stack (compose file, `.env.example`, a service that will not come up) — that is `fa-engineering-containerization`
- the gap is React component or design-system quality — that is `fa-engineering-ui`
- the repository's stack has no reference below; apply the shared procedure and say so, rather than borrowing another stack's contract

## Pick the reference

| Repository is | Read |
|---|---|
| React, Next, Vite, Svelte, Astro or Node/TypeScript | [`references/web-ts.md`](references/web-ts.md) |
| ASP.NET Core, minimal-API or another .NET service | [`references/dotnet-api.md`](references/dotnet-api.md) |
| .NET MAUI client app | [`references/dotnet-maui.md`](references/dotnet-maui.md) |
| …and a build must reach an emulator, simulator or device | [`references/dotnet-maui-device-build-and-deploy.md`](references/dotnet-maui-device-build-and-deploy.md) |
| Flutter / Dart app | [`references/flutter.md`](references/flutter.md) |
| Python | [`references/python.md`](references/python.md) |

A repository that holds more than one stack (a web frontend beside a .NET API) reads one
reference per stack and runs the passes concurrently — they share no files.

## Required inputs

- the repository tree, its manifest(s), and any existing lint, format and test configuration
- the current CI workflow and what it actually runs today
- whether the repository ships an HTTP surface that needs a compose stack

## Owned outputs

- an enforced lint and format configuration the build fails on
- one canonical command surface, mirrored by CI rather than duplicated by it
- a runnable test lane on the repository's own runner
- run-and-test instructions updated in the repository's own QA runbook

## Core workflow

1. Inventory what already exists — manifest scripts, lint config, runner, SDK pin, CI jobs — before proposing anything.
2. Open the one reference that matches the stack and audit the repository against its baseline table.
3. Close only the gaps the audit found. **Prefer the repository's established conventions over every default a reference names**: a second linter or runner beside a working one produces two disagreeing verdicts, not a higher floor.
4. Wire CI to the same command surface a contributor runs, so green CI proves something about local runs.
5. Update the repository's QA runbook, then hand planning the list of gates the baseline now earns.

## Anti-patterns

- do not migrate a working runner, formatter or package manager to a preferred one as part of a baseline pass
- do not let CI become the only place the real commands live
- do not add caching or speed work before the lanes are reliable
- do not load every stack reference "for context"; each is a full contract and only one applies

## Handoff and downstream impact

- give planning the gates this baseline earns (`lint`, `build`, `test`, and `e2e` where a browser harness exists)
- give implementation the canonical command surface, so diffs are verified the way CI will verify them
- give `fa-engineering-testing` a working harness, not an intention to add one
- give `fa-engineering-containerization` a build that is already trustworthy before it is put in an image

## Completion checklist

- one command each for lint, build and test, and CI calls them rather than reimplementing them
- the repository's own conventions survived the pass; only real gaps were filled
- the QA runbook matches the commands that now exist, and planning has the gate list
- the stack reference's own completion checklist is satisfied

## References

- [Web (JavaScript/TypeScript)](references/web-ts.md)
- [.NET HTTP API](references/dotnet-api.md)
- [.NET MAUI](references/dotnet-maui.md)
- [.NET MAUI device build and deploy](references/dotnet-maui-device-build-and-deploy.md)
- [Flutter](references/flutter.md)
- [Python](references/python.md)
- [Gaia delivery policy](../../references/delivery-policy.md)
- [Gaia ownership and conventions](../../references/ownership-and-conventions.md)
- [Default tech stack routing](../fa-engineering-default-tech-stack/SKILL.md)
