---
name: ludo-atlas
description: Game development knowledge base (Ludo Atlas / 游戏开发全景手册) — 140+ Chinese-first handbooks with a full English edition. Use when planning, scoping, designing, programming, testing, launching, or troubleshooting a game project; when choosing an engine (Godot, Unity, Unreal, GameMaker, Ren'Py, Bevy, web) or a genre (roguelite, city builder, farming sim, puzzle, visual novel...); or when learning any game development topic. Routes to genre handbooks, engine tracks, pipelines, publishing and legal, AI workflows, pitfalls, playbooks and ready-made templates.
license: CC BY-SA 4.0
---

# Ludo Atlas — 手册即 Skill

本 Skill 不复制正文，而是一层「路由 + 红线」：先在这里定位该看哪一页，再按 URL 取原文（中英双语）。

## 什么时候用

任何游戏开发任务：立项与范围、玩法与数值、引擎选型与实现、美术音频管线、制作排期、试玩测试、上架发行、法务合规、运营增长、AI 工作流。
典型触发：做游戏 / 立项 / GDD / 关卡 / 数值 / 引擎选型 / Godot / Unity / 原型 / 竖切 / 上架 Steam / 版号 / 独立游戏 / playtest。

## 怎么取页

- 站点：`https://huanmoovo.github.io/ludo-atlas` + 下表路径；英文版在路径前加 `/en/`。
- 路径前缀注意：`docs/` 子树带 `/docs/`（如 `/docs/genres/roguelite/`）；`/playbooks/`、`/resources/`、`/doc-templates/`、`/examples/` 不带。
- 仓库原文（raw Markdown）：`https://raw.githubusercontent.com/HuanMoovo/ludo-atlas/main/docs/genres/roguelite/README.md`（英文为 `README.en.md`）。
- 全量逐页索引：`references/index.md`。

## 路由表

| 你现在要做什么 | 去这里 |
| --- | --- |
| 不知道从哪开始 / 学习路线 | `/docs/start/` |
| 判断类型、看某类型的开发流程 | `/docs/genres/`（81 类，每类一页） |
| 选引擎 / 学某个引擎 | `/docs/engines/`（12 条轨道） |
| 设计、编程、美术音频、制作、关卡、引擎内幕、图形学 | `/docs/fundamentals/` |
| 构建、发布、测试、本地化、遥测、Mod、联机后端 | `/docs/pipelines/` |
| 用 AI 编码 / 智能体 / Skill / 合规披露 | `/docs/ai/` |
| 单人、小团队、工作室怎么干 | `/docs/teams/` |
| 上架、法务、运营、小游戏、主机、VR/AR、电竞 | `/docs/publishing/` |
| 排坑 / 看别人怎么翻车 | `/docs/pitfalls/`、`/docs/postmortems/` |
| 端到端起手流程（创意→Demo、竖切、上线） | `/playbooks/` |
| 要模板（一页纸、GDD、技术设计、里程碑） | `/doc-templates/` |
| 工具 / 素材 / 发行商 / 赛事入口 | `/resources/` |
| 术语中英对照 | `/GLOSSARY/` |

## 写任何计划前，记住这几条红线

1. **范围控制优先**：先砍范围再谈加质量；内容量在竖切（vertical slice）通过前不铺。
2. **原型先行**：不确定的玩法先纸面或一次性原型验证，再进正式代码。
3. **试玩尽早**：可玩版本越早给人玩越好，「自己觉得好玩」不算数。
4. **AI 有红线**：AI 产出必须人工验证；上线资产按平台要求披露（Steam 内容调查），细节见 `/docs/ai/`。
5. **数字留来源**：政策、费率、平台规则以引用页标注的核实时点为准，行动前查官方最新文档。

## 维护

- 链接可达性由仓库 CI（Link Check）持续复验；内容更新后重跑 `python skills/ludo-atlas/scripts/build_index.py` 重建索引。
- 手册许可：内容 CC BY-SA 4.0；引用时保留来源（Ludo Atlas · github.com/HuanMoovo/ludo-atlas）。
