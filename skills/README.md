# skills/ — 官方 Agent Skill

`ludo-atlas/` 是本库的官方 Agent Skill：把《Ludo Atlas 游戏开发全景手册》做成 AI 助手可调用的路由层——不复制正文，按需把助手引到对应手册页。

## 结构

```text
ludo-atlas/
├── SKILL.md                 # 技能定义（触发条件、取页方式、路由表、红线）
├── references/index.md      # 全量页面索引（逐页站点路径）
└── scripts/build_index.py   # 索引重生成脚本（内容更新后重跑）
```

## 安装

- **Claude Code**：复制 `ludo-atlas/` 到 `~/.claude/skills/`（或项目内 `.claude/skills/`）。
- **Hermes / OpenClaw / Codex 等**：复制到对应技能目录；或把 `SKILL.md` 加入项目规则/系统提示。
- **不安装也能用**：让助手直接打开 https://github.com/HuanMoovo/ludo-atlas/tree/main/skills/ludo-atlas 。

安装后的效果：任务里出现立项、选引擎、做某类型、上架、避坑等内容时，助手会按路由表去取对应页面；中文问答走中文站，英文问答走 `/en/`。

## 校验与维护

- 索引重新生成：`python skills/ludo-atlas/scripts/build_index.py`。
- 站点与仓库链接由 CI（Link Check）持续复验；索引不手改。
