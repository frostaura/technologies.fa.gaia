# Agent Skills specification

The format specification for Agent Skills (the open standard at https://agentskills.io, which Claude Code follows), plus the Claude-Code-specific extensions. Canonical Claude Code doc: https://code.claude.com/docs/en/skills

## Directory structure

A skill is a directory containing, at minimum, a `SKILL.md` file:

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

## `SKILL.md` format

The `SKILL.md` file must contain YAML frontmatter followed by Markdown content.

### Frontmatter (portable spec fields)

| Field           | Required | Constraints                                                                                                       |
| --------------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| `name`          | Yes      | Max 64 characters. Lowercase letters, numbers, and hyphens only. Must not start or end with a hyphen.             |
| `description`   | Yes      | Max 1024 characters. Non-empty. Describes what the skill does and when to use it.                                 |
| `license`       | No       | License name or reference to a bundled license file.                                                              |
| `compatibility` | No       | Max 500 characters. Indicates environment requirements (intended product, system packages, network access, etc.). |
| `metadata`      | No       | Arbitrary key-value mapping for additional metadata.                                                              |
| `allowed-tools` | No       | Space-delimited list of pre-approved tools the skill may use. (Experimental)                                      |

Minimal example:

```yaml
---
name: skill-name
description: A description of what this skill does and when to use it.
---
```

Example with optional fields:

```yaml
---
name: pdf-processing
description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
license: Apache-2.0
metadata:
  author: example-org
---
```

#### `name` field

The required `name` field:

* Must be 1-64 characters
* May only contain unicode lowercase alphanumeric characters (`a-z`) and hyphens (`-`)
* Must not start or end with a hyphen (`-`)
* Must not contain consecutive hyphens (`--`)
* Must match the parent directory name

Valid: `pdf-processing`, `data-analysis`, `code-review`. Invalid: `PDF-Processing` (uppercase), `-pdf` (leading hyphen), `pdf--processing` (consecutive hyphens).

#### `description` field

The required `description` field:

* Must be 1-1024 characters
* Should describe both what the skill does and when to use it
* Should include specific keywords that help agents identify relevant tasks

Good: `Extracts text and tables from PDF files, fills PDF forms, and merges multiple PDFs. Use when working with PDF documents or when the user mentions PDFs, forms, or document extraction.`

Poor: `Helps with PDFs.`

**The cap is not the budget.** 1,024 characters is what a validator accepts; it is not what a session can afford. Every installed skill's `name` and `description` is loaded into every session's skill listing, the spec's own target for that metadata is about 100 tokens per skill, and Claude Code truncates `description` plus `when_to_use` at 1,536 characters per entry and **drops descriptions from the listing altogether when the installed set is too large** — leaving a skill that is listed by name, looks present, and has nothing to match a request against. So write what the skill provides, when it fires, and the boundary with its nearest neighbour; put the *how* in the body. Put the trigger first: a truncated description loses its tail. Measure the plugin's total, not just one description.

#### `license` field

Specifies the license applied to the skill. Keep it short — either the name of a license (`MIT`) or the name of a bundled license file (`Proprietary. LICENSE.txt has complete terms`).

#### `compatibility` field

* Must be 1-500 characters if provided
* Should only be included if the skill has specific environment requirements
* Can indicate intended product, required system packages, network access needs, etc. (e.g. `Requires git, docker, jq, and access to the internet`)

Most skills do not need the `compatibility` field.

#### `metadata` field

* A map from string keys to string values
* Clients can use this to store additional properties not defined by the Agent Skills spec
* Make key names reasonably unique to avoid accidental conflicts

#### `allowed-tools` field

* A space-delimited list of tools that are pre-approved to run
* Experimental; support varies between agent implementations. In Claude Code the grant applies for the turn that invokes the skill and clears on the next user message.

### Claude Code extensions

Claude Code accepts additional frontmatter fields on **skills** beyond the portable six — these are valid in Claude Code but rejected by strict spec validators (claude.ai skill uploads, the Skills API), so use them only in skills that ship exclusively to Claude Code:

| Field | Purpose |
| --- | --- |
| `argument-hint` | Autocomplete hint for expected arguments, e.g. `[issue-number]`. |
| `disable-model-invocation` | `true` = only the user can invoke (via `/name`); Claude never auto-loads it. For side-effectful workflows like deploys or commits. |
| `user-invocable` | `false` = only Claude can invoke; hidden from the `/` menu. For background knowledge that is not a meaningful user action. |
| `context: fork` | Runs the skill in its own forked subagent context instead of inline; `agent` selects the subagent type and `model` the model. |
| `disallowed-tools` | Tools removed from the pool while the skill is active. |
| `when_to_use` | Extra trigger text appended to `description` in the listing; the two share the 1,536-character truncation. |
| `arguments` | Named positional arguments, substituted in the body as `$name`. |
| `model`, `effort` | Model and reasoning effort (`low` … `max`) while the skill runs. Set only when the override is deliberate. |
| `paths` | Glob patterns, relative to the working directory, that scope the skill to matching files. |
| `hooks` | Hooks that live only while the skill is active. |
| `shell` | `bash` or `powershell` for the skill's injected commands. |

Unrecognized fields are ignored without error — which means a misspelt one fails silently.

Body substitutions Claude Code expands: `$ARGUMENTS`, `$ARGUMENTS[N]` / `$N`, `${CLAUDE_SESSION_ID}`, `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}`, and — in a plugin's skills only — `${CLAUDE_PLUGIN_ROOT}` (the installed version directory, replaced on every update, so never write state there) and `${CLAUDE_PLUGIN_DATA}` (kept across updates). A line of the form ``!`command` `` injects that command's output before the model reads the skill; a non-zero exit aborts the whole invocation, so append `|| true` to anything that may legitimately fail.

A skill with `context: fork` cannot see the conversation that invoked it, so its body must stand alone.

`commands/` is still loaded and merged into skills, but new work belongs in `skills/`.

These are **skill** fields — do not confuse them with sub-agent frontmatter, which has a different schema (see the agents specification in `fa-foundation-create-agent`). Staying within the portable six keeps a skill loadable everywhere; Claude Code accepts all six unchanged.

### Body content

The Markdown body after the frontmatter contains the skill instructions. There are no format restrictions. Write whatever helps agents perform the task effectively.

Recommended sections:

* Step-by-step instructions
* Examples of inputs and outputs
* Common edge cases

Note that the agent will load this entire file once it's decided to activate a skill. Consider splitting longer `SKILL.md` content into referenced files.

## Optional directories

### `scripts/`

Contains executable code that agents can run. Scripts should:

* Be self-contained or clearly document dependencies
* Include helpful error messages
* Handle edge cases gracefully

Supported languages depend on the agent implementation. Common options include Python, Bash, and JavaScript.

### `references/`

Contains additional documentation that agents can read when needed — detailed technical references, form templates, or domain-specific files (`finance.md`, `legal.md`, etc.).

Keep individual reference files focused. Agents load these on demand, so smaller files mean less use of context.

### `assets/`

Contains static resources:

* Templates (document templates, configuration templates)
* Images (diagrams, examples)
* Data files (lookup tables, schemas)

## Progressive disclosure

Skills should be structured for efficient use of context:

1. **Metadata** (~100 tokens): The `name` and `description` fields are loaded at startup for all skills
2. **Instructions** (< 5000 tokens recommended): The full `SKILL.md` body is loaded when the skill is activated
3. **Resources** (as needed): Files (e.g. those in `scripts/`, `references/`, or `assets/`) are loaded only when required

Keep your main `SKILL.md` under 500 lines. Move detailed reference material to separate files.

## File references

When referencing other files in a skill, use relative paths from the skill root, e.g. a link written as `[the reference guide](references/my-reference.md)` from `SKILL.md`, or `scripts/extract.py` for a script the skill runs.

Keep file references one level deep from `SKILL.md`. Avoid deeply nested reference chains. In a Claude Code plugin, links must stay inside the plugin directory — a path escaping the plugin root can never resolve after installation.

## Validation

Use the [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) reference library to validate a skill against the portable spec:

```bash
skills-ref validate ./my-skill
```

For Claude Code plugins, `claude plugin validate <plugin-dir>` checks skill frontmatter as part of plugin validation (`--strict` turns warnings into failures). `/skill-doctor` reports installed skills that never fire — the only direct evidence that a description is not working as a trigger.
