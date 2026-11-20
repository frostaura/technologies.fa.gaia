---
name: ai-toolkit-gaia-gotchas
description: "MSBuildEnableWorkloadResolver=false is mandatory on this Mac; the MCP session mode silently governs whether header credentials resolve; Woolworths returns HTTP 200 for every failure; audit this repo from the tree root, not its own."
type: gotcha
last_verified: 2026-11-20
---

# Gotchas

- **`MSBuildEnableWorkloadResolver=false` is mandatory on this Mac.** Without it every
  `dotnet build` fails with MSB4242 inside `SdkDirectoryWorkloadManifestProvider.GetManifests`
  (alongside MSB4014 and MSB4236) — the machine's SDK workload set `10.0.301.1` has missing
  manifests; the iCloud path is not the cause (re-proved 2026-11-20 on SDK 10.0.302). Nothing here
  uses workloads, so export it before any `dotnet` command. The shipped
  `docs/development.md` still blames the iCloud path ([`watch.md`](watch.md)); do not trust it.
- **A green `dotnet test` before v13.0.0 meant nothing.** `src/Gaia.Mcp.Tests` is now a real
  xUnit project in `Gaia.slnx`, but CI ran an empty gate for months — so any note, commit
  message or report written before that release treating green as evidence is wrong.
- **The MCP session mode silently governs whether header credentials work at all.** The
  integration tools read credentials from the inbound request headers via
  `IHttpContextAccessor`; `fa.integrations` ran stateless partly for this reason, while Gaia
  runs `StatefulForInitializeClients` so the sampling demo keeps working. Under the hybrid
  mode a tool call *does* still execute inside the caller's HTTP request — verified by probe,
  not reasoned about. **If the mode changes, re-verify:** send only `X-Woolworths-Username`
  and check that only the password is reported missing. The failure mode looks exactly like a
  caller-side configuration problem, which is why it costs hours.
- **Woolworths' HTTP-200-on-failure has a body to read and a search twin.** The rule (inspect
  the body, add one product per request) is in `../CLAUDE.md`; the body fields that carry the
  failure are `errorMessage`, `formexceptions` and `loggedInStatus`. The search
  `filters[visibility]` parameter must be sent **twice** (`all` and `web and app`,
  `WoolworthsSearchClient.cs`) or food results come back empty while non-food does not — which
  reads convincingly as a location-gated catalogue and is not. Full captured contract:
  `../docs/integrations/woolworths.md`.
- **The shipped audit reports this repo's own `CLAUDE.md` when run at this repo's root, and
  it is right to.** `MEMORY-TOPIC-NAME` on every topic, `MEMORY-INDEX-STALE` on `MEMORY.md` and
  `UPKEEP-UNSCOPED` on `CLAUDE.md` all fall out of the documented `--root` caveat (last re-run 2026-10-22): the expected topic slug and the expected
  `--scope` argument are derived from the scope's path *relative to the root given*, and this
  repo's context layer is authored for the FrostAura tree root, where the slug is
  `ai-toolkit-gaia-` and the scope is `Labs/projects/ai.toolkit.gaia`. Audit it from the tree
  root, not from here; never "fix" the frontmatter to satisfy a narrower run.
- **Probing a health endpoint: `ping` was removed in MCP spec 2026-07-28** and SDK 2.2.0
  rejects it with a 400. Probe with a legacy `initialize` POST instead — which is what the
  Dockerfile's HEALTHCHECK does.
- **MCP sampling, roots and logging are spec-deprecated as of 2026-07-28** (12-month window,
  SEP-2577). `sampling_summarize` exists to demonstrate sampling anyway, so MCP9005 is
  suppressed file-wide in `SamplingTools.cs` — deliberately, and only there.
