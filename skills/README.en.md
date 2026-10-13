# skills/ — the official Agent Skill

`ludo-atlas/` is the official Agent Skill of this repository: it turns the Ludo Atlas handbooks into a routing layer for AI coding agents — no content is copied; the agent is pointed to the right handbook page on demand.

## Structure

```text
ludo-atlas/
├── SKILL.md                 # skill definition (triggers, fetch patterns, routing table, red lines)
├── references/index.md      # full page index (site path per page)
└── scripts/build_index.py   # index regeneration script (re-run after content updates)
```

## Install

- **Claude Code**: copy `ludo-atlas/` into `~/.claude/skills/` (or `.claude/skills/` in a project).
- **Hermes / OpenClaw / Codex …**: copy it into the agent's skills directory, or add `SKILL.md` to project rules / system prompts.
- **No install needed**: just point your agent at https://github.com/HuanMoovo/ludo-atlas/tree/main/skills/ludo-atlas .

Once installed: when a task touches kickoff, engine choice, a genre, launch or pitfalls, the agent follows the routing table to fetch the right page; Chinese questions use the Chinese site, English ones use `/en/`.

## Check & maintenance

- Regenerate the index: `python skills/ludo-atlas/scripts/build_index.py`.
- Site and repository links are re-checked by CI (Link Check); do not hand-edit the index.
