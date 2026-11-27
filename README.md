<p align="center">
  <img src="https://github.com/frostaura/technologies.fa.gaia/blob/main/README.icon.png?raw=true" alt="Gaia" width="300" />
</p>

<h1 align="center"><b>Gaia</b></h1>
<h3 align="center">full-stack apps. enterprise-grade. maintainable. customizable.</h3>
<p align="center"><i>A team of AI agents that plans, builds and checks software with you — a free, open-source add-on for Claude Code, GitHub Copilot, and Claude Desktop.</i></p>

---

<p align="center">
  <a href="./CHANGELOG.md"><img src="https://img.shields.io/badge/Version-15.0.0-purple.svg" alt="Version 15.0.0" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" /></a>
  <a href="https://github.com/features/copilot"><img src="https://img.shields.io/badge/GitHub-Copilot-blue.svg" alt="GitHub Copilot" /></a>
  <a href="https://www.claude.com/product/claude-code"><img src="https://img.shields.io/badge/Claude-Code-orange.svg" alt="Claude Code" /></a>
  <a href="https://gaia.frostaura.net"><img src="https://img.shields.io/badge/MCP-remote-green.svg" alt="Remote MCP" /></a>
  <a href="https://dotnet.microsoft.com/"><img src="https://img.shields.io/badge/.NET-MCP%20server-512BD4.svg" alt=".NET MCP server" /></a>
</p>

---

## What is Gaia?

AI assistants are good at writing code and poor at finishing projects. Left alone, they skip the planning, forget what was decided last week, and announce that something works without checking.

Gaia gives your assistant the working habits of a careful software team. You describe what you want in plain language; Gaia has the assistant **write down what it is going to build, plan the work, build it, test it, and prove it is done** — in that order, and without skipping the checks. This way of working is often called *spec-driven development*: the written description comes first, and the code has to match it.

It does two things:

1. **It helps your assistant understand your project.** Gaia writes short guide and note files into your folders — what each part is for, the rules to follow, what has been decided and why. Your assistant reads them at the start of every session, so it stops rediscovering your project from scratch. We call this the **context layer**.
2. **It runs the work from idea to release.** Requirements, design, planning, building, testing and release checks each have a defined procedure, and a task cannot be called finished while a check is failing or evidence is missing.

Gaia is not an app and not a service. It is a set of instructions your assistant loads — nothing to sign up for, nothing to host, and everything it writes is ordinary files in your own project, saved alongside your code.

### Who is it for?

- **Developers** who want an assistant that plans and verifies instead of guessing.
- **Founders and small teams** who want to go from an idea to working, maintainable software without assembling a process first.
- **Anyone with a pile of projects** an AI assistant keeps misunderstanding.

You do not need to be an expert to start — if you can install an add-on and type a request, you can use it. You will get more from it if you can read what it produces.

### What is in the box

Gaia comes as three add-ons ("plugins"). Install only the ones you need.

| Plugin | In plain words | What it covers |
| --- | --- | --- |
| **`foundation`** | Helps your assistant understand and remember your project. | The context layer — creating, updating and auditing the guide and note files across your folders — plus writing new skills, agents and plans. Required by the other two. |
| **`engineering`** | Builds software properly, start to finish. | Design, planning, implementation, user interface, testing, packaging, deployment, and starting templates for common languages. |
| **`product`** | Works out whether a product idea is worth building. | A step-by-step process for consumer apps and games sold as a one-off purchase or with in-app purchases, from researching the idea through launch and beyond — with a profitability check at every step. |

> There is deliberately **no skill list in this README** — it rots faster than anyone maintains it. The live roster is `/plugin` in your client; a dated snapshot lives in [`docs/catalog.md`](./docs/catalog.md).

This repository also contains a small, separate **.NET MCP server** ([`src/`](./src)) that lets an assistant use third-party consumer services as tools. It is independent of the plugins: neither needs the other, and most people can ignore it.

---

## What you need

- **One supported AI assistant:** [Claude Code](https://www.claude.com/product/claude-code), [GitHub Copilot](https://github.com/features/copilot) (CLI), or Claude Desktop / claude.ai / Cowork.
- **A folder to work in** — an existing project, several projects, or an empty folder for a new one.

That is all. There is no Gaia account, no API key and no server to run.

---

## Install

**Install `foundation` first.** The other two plugins rely on it, and nothing installs it for you automatically.

### Claude Code

Type these into Claude Code:

```bash
/plugin marketplace add frostaura/technologies.fa.gaia

/plugin install foundation@frostaura
/plugin install engineering@frostaura
/plugin install product@frostaura
```

### GitHub Copilot

Run these in your terminal:

```bash
copilot plugin marketplace add frostaura/technologies.fa.gaia

copilot plugin install foundation@frostaura
copilot plugin install engineering@frostaura
copilot plugin install product@frostaura
```

### Claude Desktop, claude.ai and Cowork

Add this marketplace from its repository URL — `https://github.com/frostaura/technologies.fa.gaia` — then install the plugins you want. The exact path differs by surface and changes as the product moves, so follow [Anthropic's plugin documentation](https://code.claude.com/docs/en/plugins) rather than a click-path copied into a README.

> **Which assistant should I use?** Gaia works in all of them, but it is fastest in **Claude Code**, where it can hand parts of a job to several helper agents working at the same time. Desktop and claude.ai chat do not run helper agents, so the same steps run one after another instead — same result, slower. The skills say so wherever it changes what you get.

---

## Start here

The first thing to ask for in a new place — one project, a large repository, or a folder full of unrelated projects:

> **"Optimize this directory tree — establish the Gaia context layer across everything in it."**

This reads your folders and writes the guide and note files that let your assistant understand all of it, not just the one file it was pointed at. (The skill behind it is `fa-foundation-optimize-directory-tree`.)

It is **not a one-off setup step**. Run it again whenever your projects have moved on. It looks at what is on disk and decides which of three jobs is needed:

- **Establish** — nothing is there yet, so it writes the guide and note files wherever they are useful, records what projects exist, and writes the design documentation your projects never had, worked out from their source code.
- **Maintain** — the files exist but the projects have changed, so it rechecks every statement against what the projects have actually become.
- **Sweep** — tidy up: remove what went out of date, merge what overlaps, delete what no longer applies. **This is the one a healthy project runs most often, and deletion is a normal outcome, not data loss.**

Good to know before you run it:

- **It tells you its plan first.** Before writing anything it lists what it will look at, roughly how many files it will write, and where — then waits for your go-ahead. It skips the wait only if you explicitly told it to work on its own, or if nobody is there to answer; the plan is stated either way. It never commits anything to version control for you.
- **`foundation` alone** is enough for the guide and note files. Writing design documentation for existing projects **also needs `engineering`** installed.
- **In Claude Code** it works on several folders at once. **In Desktop or claude.ai chat** it does the same work one folder at a time.

---

## Use it

Open any project and tell your assistant what you want, in your own words:

> **"Create a REST API for a blog with posts and comments."**

Gaia clarifies the request, writes the design into a `docs/` folder, plans the work, builds it, tests it, and confirms the release checks pass — one step leading to the next, without you directing each one.

### Without supervision (Copilot CLI)

To let it run from start to finish without stopping to ask permission:

```bash
copilot -p "Create a REST API for a blog with posts and comments" --yolo
```

`--yolo` lets the assistant change files and run commands unprompted, so use it in a folder you are happy for it to change.

### Is my product idea worth building?

The `product` plugin is for consumer apps and games that earn money from a one-off purchase or from in-app / in-game purchases (not subscriptions or business software). Start it with a description of the idea and the goal:

```bash
/fa-product-manager premium one-off puzzle game for iOS + Steam, ~$200k net in year one
```

…or simply describe the goal in a sentence. It works through ten stages, from market research to launch and ongoing operation. Every stage is drafted, challenged by an independent reviewer, and measured against one shared set of numbers — what a customer costs to win against what they are worth after store fees. A stage that does not add up is sent back or stopped, so you get an honest **go, rework or stop** answer rather than encouragement.

---

## A few terms, in plain words

| Term | What it means here |
| --- | --- |
| **Plugin** | An add-on your AI assistant installs. Gaia's plugins contain only written instructions — no program runs on your machine. |
| **Skill** | One written procedure for one kind of job, such as "plan this work" or "test this change". The assistant picks it up when the job calls for it. |
| **Agent** | An AI helper given one role — for example, a reviewer that checks work it did not write. |
| **Context layer** | The guide files (`CLAUDE.md` / `AGENTS.md`) and note files (`MEMORY.md`, `memory/`) Gaia keeps in your folders so the assistant knows your project. |
| **Gate** | A check that must pass before work moves on — tests green, evidence recorded, numbers adding up. |
| **MCP server** | A standard way to give an AI assistant extra tools. Only relevant if you use the optional server in [`src/`](./src). |

---

## Docs

| Document | What is in it |
| --- | --- |
| [`docs/catalog.md`](./docs/catalog.md) | Dated snapshot of every plugin, skill and agent. The live roster is always `/plugin`. |
| [`docs/development.md`](./docs/development.md) | Working on Gaia itself: releases and the 12 version sites, the two marketplace manifests, local-clone installs, authoring invariants, the pre-ship checks, contributing. |
| [`CHANGELOG.md`](./CHANGELOG.md) | Every user-visible change, lockstep across the three plugins. |
| [`src/README.md`](./src/README.md) | The .NET MCP server — integration tools, transports, credentials. |
| [`docs/integrations/`](./docs/integrations/architecture.md) | How the integrations work: the credential model, the captured upstream contract, use cases, and the end-to-end QA procedure. |
| [`CLAUDE.md`](./CLAUDE.md) | How agents should work in this repository. |

---

## Data & privacy

**The plugins send nothing anywhere.** They are skill and agent definitions that run inside your assistant. Your plan lives in your assistant's own todo list, and your memory lives in `MEMORY.md` and `memory/` files inside your repository. There is no hosted store, no account, and nothing segregated by project name because nothing leaves your machine.

**The MCP server stores nothing either.** It is stateless by design: it holds no database and no credential store, so a compromise of the host leaks no standing access to anyone's account.

- **Never stored, logged, or echoed:** your provider credentials. You supply them per request — as HTTP headers over streamable HTTP, or in the process environment over stdio — and they live only for the duration of that one call.
- **Sent onward:** only what the tool you invoked requires, and only to that tool's provider.
- **Sessions are per-operation:** sign in, do the work, sign out. Sessions are never pooled or cached, so one caller's session can never serve another's call.

Because credentials travel in headers, **never expose this server over plain HTTP** — TLS is the only thing protecting them. The server source lives in [`src/Gaia.Mcp.Server`](./src/Gaia.Mcp.Server).

---

<p align="center">
  <i>"In Greek mythology, Gaia is the personification of Earth and the ancestral mother of all life."</i>
</p>
