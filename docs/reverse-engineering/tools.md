# Ludo Atlas · 邪修·逆向工程 · 工具链

> 一句话：工具按「看、跑、提、连」四件事分工。每一类先用熟一件，再谈扩充。
> 全部链接指向官方仓库或官网；许可与合规边界见《邪修·逆向工程》§1。

---

## 1. 先装哪几件（最小起步）

| 用途 | 首选 | 备注 |
| --- | --- | --- |
| 反汇编与反编译 | [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | 免费、多架构、带脚本与协作 |
| 动态调试 | [x64dbg](https://github.com/x64dbg/x64dbg) | Windows 下的开源调试器 |
| 内存研究 | [Cheat Engine](https://github.com/cheat-engine/cheat-engine) | 数值扫描与内存查看，单机练手常用 |
| 文件识别 | [Detect It Easy](https://github.com/horsicq/Detect-It-Easy) | 判断文件类型、编译器与壳 |
| 十六进制编辑 | [ImHex](https://github.com/WerWolv/ImHex) | 带模式语言，适合批量看结构 |

## 2. 静态分析（反汇编与反编译）

- **[Ghidra](https://github.com/NationalSecurityAgency/ghidra)**：NSA 开源的逆向套件，反汇编加反编译，支持脚本扩展与多用户协作。
- **[radare2](https://github.com/radareorg/radare2) / [rizin](https://github.com/rizinorg/rizin)**：命令行逆向框架；rizin 是社区分支，配 **[Cutter](https://github.com/rizinorg/cutter)** 获得图形界面。
- **[IDA](https://hex-rays.com)**（Hex-Rays）：工业标准，商业软件；IDA Free 有功能限制，学习够用一阵。
- **[Binary Ninja](https://binary.ninja)**：商业平台，强项在 API 与自动化，适合批量分析。
- **[RetDec](https://github.com/avast/retdec)**：LLVM 路线的多架构反编译器。
- **[dnSpyEx](https://github.com/dnSpyEx/dnSpy) / [ILSpy](https://github.com/icsharpcode/ILSpy)**：.NET 反编译；dnSpyEx 还能直接调试。
- **[jadx](https://github.com/skylot/jadx) / [Apktool](https://github.com/iBotPeaches/Apktool)**：安卓 DEX 反编译与 APK 拆包重打包。
- **[Capstone](https://github.com/capstone-engine/capstone)**：反汇编引擎库，把反汇编能力嵌进你自己的工具。

## 3. 动态调试与插桩

- **[x64dbg](https://github.com/x64dbg/x64dbg)**：Windows x86/x64 调试器，断点、单步、内存与调用栈一应俱全。
- **[Cheat Engine](https://github.com/cheat-engine/cheat-engine)**：内存扫描加调试，单机游戏数值研究的事实标准；只在自己的作品或教学靶场上练。
- **[Frida](https://github.com/frida/frida)**：动态插桩框架，跨平台，用 JavaScript 挂钩函数、改行为。
- **[System Informer](https://github.com/winsiderss/systeminformer)**：进程、句柄、网络与内存一览（原 Process Hacker）。

## 4. 网络与协议

- **[mitmproxy](https://github.com/mitmproxy/mitmproxy)**：可脚本化的 HTTP(S) 中间人代理，看请求、改响应。
- **[Wireshark](https://github.com/wireshark/wireshark)**：网络协议分析，抓包与解码。

## 5. 资源提取（按引擎）

| 引擎 | 工具 | 用途 |
| --- | --- | --- |
| Unity | [AssetRipper](https://github.com/AssetRipper/AssetRipper) | 导出模型、贴图、音频与场景 |
| Unity | [AssetStudio](https://github.com/Perfare/AssetStudio) | 浏览与导出资源（原版已归档，社区有维护分支） |
| Unity | [UABEA](https://github.com/nesrak1/UABEA) | AssetBundle 查看与编辑 |
| Unity | [UnityPy](https://github.com/K0lb3/UnityPy) | Python 库，适合批处理与自动化 |
| Unity | [Il2CppDumper](https://github.com/Perfare/Il2CppDumper) / [Il2CppInspector](https://github.com/djkaty/Il2CppInspector) | IL2CPP 元数据还原：类型、方法、地址偏移 |
| Unreal | [FModel](https://github.com/4sval/FModel) | 资源浏览与导出（图形界面） |
| Unreal | [RE-UE4SS](https://github.com/UE4SS-RE/RE-UE4SS) | 脚本系统与 Mod 注入（Lua） |
| Unreal | [UAssetGUI](https://github.com/atenfyr/UAssetGUI) | 手动查看与编辑资产 |
| Unreal | [CUE4Parse](https://github.com/FabianFG/CUE4Parse) | 解析库（C#），FModel 的解析核心 |
| Godot | [GDRE Tools](https://github.com/GDRETools/gdsdecomp) | 工程反编译与恢复（gdsdecomp） |
| GameMaker | [UndertaleModTool](https://github.com/krzys-h/UndertaleModTool) | 反编译与数据编辑 |
| Ren'Py | [unrpyc](https://github.com/CensoredUsername/unrpyc) | 脚本反编译 |

## 6. Mod 框架（合规扩展的基建）

- **[BepInEx](https://github.com/BepInEx/BepInEx)**：Unity 与 .NET 游戏的插件框架，PC Mod 生态的通行基建。
- **[MelonLoader](https://github.com/LavaGang/MelonLoader)**：Unity 游戏的 Mod 加载器，支持 Il2Cpp 与 Mono。

## 7. 复古与模拟器（考古专用）

- **[Mesen2](https://github.com/SourMesen/Mesen2)**：NES / SNES / GB 等高精度模拟器，自带调试器与内存查看。
- **[BizHawk](https://github.com/TASEmulators/BizHawk)**：多机种模拟器，调试与 Lua 工具链成熟，TAS 社区主力。
- **[mGBA](https://github.com/mgba-emu/mgba)**：GBA 模拟器，带 GDB 调试接口。

## 8. 二进制分析框架（进阶）

- **[angr](https://github.com/angr/angr)**：符号执行与程序分析框架（Python）。
- **[Unicorn](https://github.com/unicorn-engine/unicorn)**：CPU 模拟框架，常用于脱壳与自动化分析。
- **[Detours](https://github.com/microsoft/Detours)**：微软的 API 挂钩库，理解与实现挂钩的基础件。

## 9. AI 辅助：把智能体接进来

- **[REA（morluto/rea）](https://github.com/morluto/rea)**：面向智能体的逆向工程 MCP，把二进制、应用与运行时行为的分析串成可复用流程，与 Ghidra 等工具协同。
- 通用编码代理也能直接调用上述命令行工具（Ghidra 无头模式、rizin、Frida CLI）；组合方式见《AI 工作流手册》。

## 10. 学习资料

- [wtsxDev/reverse-engineering](https://github.com/wtsxDev/reverse-engineering)：学习资源与教程合集。
- [mytechnotalent/Reverse-Engineering](https://github.com/mytechnotalent/Reverse-Engineering)：从 x86 与 ARM 汇编起步的免费实践教程。
- [michalmalik/linux-re-101](https://github.com/michalmalik/linux-re-101)：Linux 平台逆向的资料索引。
- [看雪论坛](https://bbs.kanxue.com)：中文安全与逆向社区（论坛、课程与赛事信息）。

---

> 配套：本板块《开源项目》与《实操路线》；完整免责声明见《邪修·逆向工程》§1。
