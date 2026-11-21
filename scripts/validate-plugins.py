#!/usr/bin/env python3
"""Mechanical checks over plugins/ and the two marketplace manifests.

Repository tooling, not shipped in any plugin. Every check here is an invariant
CLAUDE.md states and nothing used to assert: the manifests agree, the plugin.json
pairs are byte-identical, every definition's frontmatter parses and is named for
its file, links stay inside their plugin and resolve, and no definition names a
skill or agent that does not exist.

    python3 scripts/validate-plugins.py            # exit 1 on any failure
    python3 scripts/validate-plugins.py --budget   # also print the description budget

Requires PyYAML.
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PLUGINS = ROOT / "plugins"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
# Agent Skills spec limits; Claude Code truncates description + when_to_use at 1,536.
DESC_MAX, NAME_MAX = 1024, 64
# Portable Agent Skills fields plus the Claude Code extensions a skill may carry.
SKILL_KEYS = {
    "name", "description", "license", "compatibility", "metadata", "allowed-tools",
    "when_to_use", "argument-hint", "arguments", "disable-model-invocation",
    "user-invocable", "disallowed-tools", "model", "effort", "context", "agent",
    "background", "hooks", "paths", "shell",
}
AGENT_KEYS = {
    "name", "description", "tools", "disallowedTools", "model", "maxTurns",
    "skills", "memory", "background", "effort", "isolation", "color",
    "omitClaudeMd", "autoCompactWindow",
}
# Loaded but ignored for an agent a plugin ships — carrying one is a silent no-op.
AGENT_IGNORED_IN_PLUGINS = {"hooks", "mcpServers", "permissionMode", "initialPrompt"}
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
REF_RE = re.compile(r"`(fa-(?:foundation|engineering|product)-[a-z0-9-]+)`")

errors = []


def err(path, msg):
    errors.append(f"{Path(path).relative_to(ROOT)}: {msg}")


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        err(path, "no frontmatter block opening on line 1 — the definition is inert")
        return None
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        err(path, f"frontmatter is not valid YAML: {str(e).splitlines()[0]}")
        return None
    if not isinstance(data, dict):
        err(path, "frontmatter is not a mapping")
        return None
    return data


def check_definition(path, expected, plugin, allowed, kind):
    fm = frontmatter(path)
    if fm is None:
        return None
    name, desc = fm.get("name"), fm.get("description")
    if name != expected:
        err(path, f"name {name!r} must equal {expected!r} or the {kind} cannot be invoked")
    if not isinstance(name, str) or not NAME_RE.match(name) or len(name) > NAME_MAX:
        err(path, f"name {name!r} is not 1-{NAME_MAX} chars of lowercase a-z, 0-9 and single hyphens")
    elif not name.startswith(f"fa-{plugin}-"):
        err(path, f"name must start with fa-{plugin}-")
    if not isinstance(desc, str) or not desc.strip():
        err(path, "description is missing or empty")
        desc = ""
    elif len(desc) > DESC_MAX:
        err(path, f"description is {len(desc)} chars; the cap is {DESC_MAX}")
    for key in fm:
        if kind == "agent" and key in AGENT_IGNORED_IN_PLUGINS:
            err(path, f"`{key}` is ignored for plugin-shipped agents — remove it")
        elif key not in allowed:
            err(path, f"unknown frontmatter key `{key}`")
    if kind == "skill" and "license" not in fm:
        err(path, "skill has no `license`")
    return len(desc)


def check_links(plugin_dir):
    for md in plugin_dir.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        text = re.sub(r"`[^`\n]*`", "", text)
        for target in LINK_RE.findall(text):
            if re.match(r"[a-z]+:|#", target):
                continue
            dest = (md.parent / target.split("#")[0]).resolve()
            if plugin_dir.resolve() not in dest.parents:
                err(md, f"link escapes the plugin root: {target}")
            elif not dest.exists():
                err(md, f"dead link: {target}")


def main():
    known, budget = set(), {}
    plugin_dirs = sorted(p for p in PLUGINS.iterdir() if p.is_dir())
    versions = {}
    for pdir in plugin_dirs:
        plugin = pdir.name
        a, b = pdir / "plugin.json", pdir / ".claude-plugin" / "plugin.json"
        if not a.is_file() or not b.is_file():
            err(pdir, "needs both plugin.json and .claude-plugin/plugin.json")
            continue
        if a.read_bytes() != b.read_bytes():
            err(a, "differs from .claude-plugin/plugin.json — the pair must be byte-identical")
        manifest = json.loads(a.read_text())
        versions[plugin] = manifest
        if manifest.get("name") != plugin:
            err(a, f"name {manifest.get('name')!r} must equal the directory {plugin!r}")
        for server, cfg in (manifest.get("mcpServers") or {}).items():
            if any(str(arg).endswith("@latest") for arg in cfg.get("args", [])):
                err(a, f"MCP server `{server}` runs an unpinned @latest package")
        total = 0
        for sdir in sorted((pdir / "skills").iterdir()):
            if not sdir.is_dir():
                continue
            skill = sdir / "SKILL.md"
            if not skill.is_file():
                err(sdir, "skill directory with no SKILL.md")
                continue
            known.add(sdir.name)
            n = check_definition(skill, sdir.name, plugin, SKILL_KEYS, "skill")
            total += n or 0
            if len(skill.read_text(encoding="utf-8").splitlines()) > 500:
                err(skill, "over 500 lines — move detail into references/")
        for agent in sorted((pdir / "agents").glob("*.md")):
            known.add(agent.stem)
            check_definition(agent, agent.stem, plugin, AGENT_KEYS, "agent")
            # A preloaded skill that does not exist is skipped with a debug-log
            # warning only, so the agent silently starts without its playbook.
            for skill in (frontmatter(agent) or {}).get("skills") or []:
                if not (pdir / "skills" / str(skill) / "SKILL.md").is_file():
                    err(agent, f"preloads `{skill}`, which is not a skill in this plugin")
        budget[plugin] = (total, sum(1 for _ in (pdir / "skills").glob("*/SKILL.md")))
        check_links(pdir)

    # A backticked fa-<plugin>-<name> anywhere under plugins/ must be a real definition.
    for md in PLUGINS.rglob("*.md"):
        for ref in sorted(set(REF_RE.findall(md.read_text(encoding="utf-8")))):
            if ref not in known:
                err(md, f"names `{ref}`, which is neither a skill nor an agent")

    # The two marketplace manifests describe one catalog.
    paths = [ROOT / ".claude-plugin" / "marketplace.json", ROOT / ".github" / "plugin" / "marketplace.json"]
    markets = [json.loads(p.read_text()) for p in paths]

    def shape(m):
        return {
            "name": m.get("name"), "owner": m.get("owner"), "metadata": m.get("metadata"),
            "plugins": [{k: v for k, v in p.items() if k != "source"} for p in m.get("plugins", [])],
        }

    if shape(markets[0]) != shape(markets[1]):
        err(paths[1], "disagrees with .claude-plugin/marketplace.json on something other than source form")
    for path, market in zip(paths, markets):
        listed = {p["name"]: p for p in market.get("plugins", [])}
        if set(listed) != set(versions):
            err(path, f"lists {sorted(listed)}; plugins/ holds {sorted(versions)}")
        for name, entry in listed.items():
            manifest = versions.get(name, {})
            for field in ("version", "description"):
                if entry.get(field) != manifest.get(field):
                    err(path, f"{name}: `{field}` differs from its plugin.json")
    if len({m.get("version") for m in versions.values()}) > 1:
        err(PLUGINS, "plugin versions are not in lockstep")

    if "--budget" in sys.argv:
        print("skill description characters loaded into every session's listing:")
        for plugin, (total, count) in budget.items():
            print(f"  {plugin:12s} {count:3d} skills  {total:6d} chars  (mean {total // max(count, 1)})")
        print(f"  {'total':12s} {sum(c for _, c in budget.values()):3d} skills  {sum(t for t, _ in budget.values()):6d} chars")

    if errors:
        print(f"{len(errors)} failure(s):", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return 1
    print(f"ok — {len(plugin_dirs)} plugins, {len(known)} definitions, manifests agree")
    return 0


if __name__ == "__main__":
    sys.exit(main())
