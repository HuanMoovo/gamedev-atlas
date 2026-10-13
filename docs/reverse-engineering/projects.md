# Ludo Atlas · 邪修·逆向工程 · 开源项目

> 清单按三类组织：反编译与原生移植、引擎重实现、学习资源与合集。
> 所有项目只发布代码与工具，不附带游戏资源；使用时需自备合法副本。许可与边界见《邪修·逆向工程》§1。

---

## 1. 反编译与原生移植（把成品还原成可重编译的工程）

这类项目把经典作品的机器码逐年「翻译」回可读、可编译的源码，再在现代平台上重新构建。读懂一个，胜过泛读十个玩具项目：里面有完整的架构、工具链与测试体系。

| 项目 | 作品 | 看点 |
| --- | --- | --- |
| [n64decomp/sm64](https://github.com/n64decomp/sm64) | 超级马力欧 64 | 反编译项目的模板：命名规范、匹配流程、文档体系 |
| [zeldaret/oot](https://github.com/zeldaret/oot) | 塞尔达传说 时之笛 | 大型 N64 工程的组织方式 |
| [zeldaret/mm](https://github.com/zeldaret/mm) | 姆吉拉的假面 | 在时之笛工具链之上的再建设 |
| [zeldaret/tp](https://github.com/zeldaret/tp) / [zeldaret/tww](https://github.com/zeldaret/tww) | 黄昏公主 / 风之杖 | 较新平台的工程重建 |
| [HarbourMasters/Shipwright](https://github.com/HarbourMasters/Shipwright) | 时之笛（Ship of Harkinian） | 反编译到 PC 原生移植的整套流程 |
| [HarbourMasters/2ship2harkinian](https://github.com/HarbourMasters/2ship2harkinian) | 姆吉拉的假面 | 同一套移植框架的复用 |
| [Rubberduckycooly/Sonic-Mania-Decompilation](https://github.com/Rubberduckycooly/Sonic-Mania-Decompilation) | 索尼克狂欢 | 现代引擎游戏的反编译案例 |
| [snesrev/zelda3](https://github.com/snesrev/zelda3) | 众神的三角力量 | 单人主导的高质量反编译与移植 |
| [snesrev/smw](https://github.com/snesrev/smw) | 超级马力欧世界 | SNES 平台的反编译路线 |
| [open-goal/jak-project](https://github.com/open-goal/jak-project) | 杰克与达斯特 | 为老平台自研语言与编译器（GOAL），工程规模惊人 |

注意：这类项目通常在 README 里写明「不提供游戏资源」，你需要在合法拥有的副本上自行提取；请尊重各项目的许可与命名约定。

## 2. 引擎重实现（用新代码让老游戏继续可玩）

与反编译互补的另一条路：不还原原码，而是按行为重建一个引擎，让原版资源继续跑。适合研究「引擎与内容分离」的架构。

| 项目 | 作品 | 分类 |
| --- | --- | --- |
| [OpenMW/openmw](https://github.com/OpenMW/openmw) | 上古卷轴 3：晨风 | 3D RPG 引擎重实现 |
| [Interkarma/daggerfall-unity](https://github.com/Interkarma/daggerfall-unity) | 匕首雨 | 用现代引擎重建 |
| [exult/exult](https://github.com/exult/exult) | 创世纪 7 | 老 RPG 重实现 |
| [OpenDiablo2/OpenDiablo2](https://github.com/OpenDiablo2/OpenDiablo2) | 暗黑破坏神 2 | 数据驱动的重实现 |
| [OpenRA/OpenRA](https://github.com/OpenRA/OpenRA) | 命令与征服 / 红警 | RTS 引擎现代化 |
| [OpenTTD/OpenTTD](https://github.com/OpenTTD/OpenTTD) | 运输大亨 | 工业级长期维护样板 |
| [SFTtech/openage](https://github.com/SFTtech/openage) | 帝国时代 2 | 超长周期的重实现工程 |
| [SupSuper/OpenXcom](https://github.com/SupSuper/OpenXcom) | X-COM | 战棋重实现 |
| [bvschaik/julius](https://github.com/bvschaik/julius) / [augustus](https://github.com/Keriew/augustus) | 凯撒大帝 3 | 城建模组与增强分支 |
| [OpenDune/OpenDune](https://github.com/OpenDune/OpenDune) | 沙丘 2 | RTS 开山作的现代重跑 |
| [OpenRCT2/OpenRCT2](https://github.com/OpenRCT2/OpenRCT2) | 过山车大亨 2 | 模拟经营重实现 |
| [CorsixTH/CorsixTH](https://github.com/CorsixTH/CorsixTH) | 主题医院 | Lua 扩展友好 |
| [yquake2/yquake2](https://github.com/yquake2/yquake2) | 雷神之锤 2 | 引擎核心重整理 |
| [Novum/vkQuake](https://github.com/Novum/vkQuake) | 雷神之锤 | Vulkan 渲染实验田 |
| [Quake3e](https://github.com/ec-/Quake3e) | 雷神之锤 3 | 持续维护的引擎分支 |
| [ZDoom/gzdoom](https://github.com/ZDoom/gzdoom) | 毁灭战士 | 最活跃的 Doom 引擎分支 |
| [FWGS/xash3d-fwgs](https://github.com/FWGS/xash3d-fwgs) | 半条命（GoldSrc） | 引擎行为兼容研究 |
| [rwengine/openrw](https://github.com/rwengine/openrw) | GTA III | 开放世界重实现尝试 |
| [scummvm/scummvm](https://github.com/scummvm/scummvm) | 经典冒险游戏合集 | 一个引擎跑几百款作品 |
| [XProger/OpenLara](https://github.com/XProger/OpenLara) | 古墓丽影 | 单人跨平台引擎实验 |
| [k4zmu2a/SpaceCadetPinball](https://github.com/k4zmu2a/SpaceCadetPinball) | 弹球（XP 自带） | 系统小游戏复活样板 |
| [djyt/cannonball](https://github.com/djyt/cannonball) | 世嘉 OutRun | 街机赛车经典的现代重建 |
| [doukutsu-rs/doukutsu-rs](https://github.com/doukutsu-rs/doukutsu-rs) | 洞窟物语 | Rust 重实现 |
| [OpenKH/OpenKH](https://github.com/OpenKH/OpenKH) | 王国之心系列 | 资源工具与引擎研究的组合 |

## 3. 学习资源与合集

- [wtsxDev/reverse-engineering](https://github.com/wtsxDev/reverse-engineering)：学习资源与教程合集，先从这里扫一遍全景。
- [mytechnotalent/Reverse-Engineering](https://github.com/mytechnotalent/Reverse-Engineering)：从 x86 与 ARM 汇编起步的免费实践教程。
- [michalmalik/linux-re-101](https://github.com/michalmalik/linux-re-101)：Linux 平台逆向的资料索引。
- [看雪论坛](https://bbs.kanxue.com)：中文安全与逆向社区，教材与赛事信息齐全。

## 4. 怎么参与这些项目

- 从文档、测试与小的修复开始；先读 CONTRIBUTING，再提第一个 Pull Request。
- 这类社区对资源与命名有严格规矩（不附带原版素材、函数命名要对齐符号表），提交前先搜历史 Issue。
- 低质量生成补丁在这类项目里审核很严；拿不准就先开 Issue 问。

---

> 配套：本板块《工具链》与《实操路线》；完整免责声明见《邪修·逆向工程》§1。
