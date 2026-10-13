# Ludo Atlas · Reverse Engineering (Unorthodox) · Toolchain

> In one line: tools divide the work into four jobs — "look, run, extract, connect". Get fluent with one tool in each category before talking about expanding.
> All links point to official repositories or official websites; for licensing and compliance boundaries see Reverse Engineering (Unorthodox) §1.

---

## 1. Which Ones to Install First (Minimal Start)

| Purpose | First choice | Notes |
| --- | --- | --- |
| Disassembly and decompilation | [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | Free, multi-architecture, with scripting and collaboration |
| Dynamic debugging | [x64dbg](https://github.com/x64dbg/x64dbg) | The open-source debugger on Windows |
| Memory research | [Cheat Engine](https://github.com/cheat-engine/cheat-engine) | Value scanning and memory inspection; commonly used for single-player practice |
| File identification | [Detect It Easy](https://github.com/horsicq/Detect-It-Easy) | Identify file type, compiler and packer |
| Hex editing | [ImHex](https://github.com/WerWolv/ImHex) | Ships a pattern language, good for inspecting structures in bulk |

## 2. Static Analysis (Disassembly and Decompilation)

- **[Ghidra](https://github.com/NationalSecurityAgency/ghidra)**: the NSA's open-source reverse engineering suite — disassembly plus decompilation, with script extensions and multi-user collaboration.
- **[radare2](https://github.com/radareorg/radare2) / [rizin](https://github.com/rizinorg/rizin)**: command-line reverse engineering frameworks; rizin is the community fork — pair it with **[Cutter](https://github.com/rizinorg/cutter)** for a graphical interface.
- **[IDA](https://hex-rays.com)** (Hex-Rays): the industry standard, commercial software; IDA Free has feature limits, enough for learning for a while.
- **[Binary Ninja](https://binary.ninja)**: a commercial platform whose strength is its API and automation — suited to batch analysis.
- **[RetDec](https://github.com/avast/retdec)**: an LLVM-based multi-architecture decompiler.
- **[dnSpyEx](https://github.com/dnSpyEx/dnSpy) / [ILSpy](https://github.com/icsharpcode/ILSpy)**: .NET decompilation; dnSpyEx can also debug directly.
- **[jadx](https://github.com/skylot/jadx) / [Apktool](https://github.com/iBotPeaches/Apktool)**: Android DEX decompilation and APK unpacking and repacking.
- **[Capstone](https://github.com/capstone-engine/capstone)**: a disassembly engine library — embed disassembly capability into your own tools.

## 3. Dynamic Debugging and Instrumentation

- **[x64dbg](https://github.com/x64dbg/x64dbg)**: a Windows x86/x64 debugger with breakpoints, single-stepping, memory and call stacks all at hand.
- **[Cheat Engine](https://github.com/cheat-engine/cheat-engine)**: memory scanning plus debugging; the de facto standard for value research in single-player games. Practice only on your own work or on teaching targets.
- **[Frida](https://github.com/frida/frida)**: a dynamic instrumentation framework, cross-platform; hook functions and change behavior with JavaScript.
- **[System Informer](https://github.com/winsiderss/systeminformer)**: processes, handles, network and memory at a glance (formerly Process Hacker).

## 4. Networking and Protocols

- **[mitmproxy](https://github.com/mitmproxy/mitmproxy)**: a scriptable HTTP(S) man-in-the-middle proxy — inspect requests, modify responses.
- **[Wireshark](https://github.com/wireshark/wireshark)**: network protocol analysis, packet capture and decoding.

## 5. Asset Extraction (by Engine)

| Engine | Tool | Purpose |
| --- | --- | --- |
| Unity | [AssetRipper](https://github.com/AssetRipper/AssetRipper) | Export models, textures, audio and scenes |
| Unity | [AssetStudio](https://github.com/Perfare/AssetStudio) | Browse and export assets (the original is archived; community forks are maintained) |
| Unity | [UABEA](https://github.com/nesrak1/UABEA) | AssetBundle viewing and editing |
| Unity | [UnityPy](https://github.com/K0lb3/UnityPy) | A Python library, good for batch processing and automation |
| Unity | [Il2CppDumper](https://github.com/Perfare/Il2CppDumper) / [Il2CppInspector](https://github.com/djkaty/Il2CppInspector) | IL2CPP metadata recovery: types, methods, address offsets |
| Unreal | [FModel](https://github.com/4sval/FModel) | Asset browsing and export (graphical interface) |
| Unreal | [RE-UE4SS](https://github.com/UE4SS-RE/RE-UE4SS) | Scripting system and mod injection (Lua) |
| Unreal | [UAssetGUI](https://github.com/atenfyr/UAssetGUI) | Manually view and edit assets |
| Unreal | [CUE4Parse](https://github.com/FabianFG/CUE4Parse) | Parsing library (C#); the parsing core behind FModel |
| Godot | [GDRE Tools](https://github.com/GDRETools/gdsdecomp) | Project decompilation and recovery (gdsdecomp) |
| GameMaker | [UndertaleModTool](https://github.com/krzys-h/UndertaleModTool) | Decompilation and data editing |
| Ren'Py | [unrpyc](https://github.com/CensoredUsername/unrpyc) | Script decompilation |

## 6. Mod Frameworks (Infrastructure for Compliant Extensions)

- **[BepInEx](https://github.com/BepInEx/BepInEx)**: a plug-in framework for Unity and .NET games; common infrastructure across the PC mod ecosystem.
- **[MelonLoader](https://github.com/LavaGang/MelonLoader)**: a mod loader for Unity games, supporting Il2Cpp and Mono.

## 7. Retro and Emulators (for Archaeology)

- **[Mesen2](https://github.com/SourMesen/Mesen2)**: a high-accuracy emulator for NES / SNES / GB and more, with a built-in debugger and memory viewer.
- **[BizHawk](https://github.com/TASEmulators/BizHawk)**: a multi-system emulator with a mature debugging and Lua toolchain; a mainstay of the TAS community.
- **[mGBA](https://github.com/mgba-emu/mgba)**: a GBA emulator with a GDB debugging interface.

## 8. Binary Analysis Frameworks (Advanced)

- **[angr](https://github.com/angr/angr)**: a symbolic execution and program analysis framework (Python).
- **[Unicorn](https://github.com/unicorn-engine/unicorn)**: a CPU emulation framework, often used for unpacking and automated analysis.
- **[Detours](https://github.com/microsoft/Detours)**: Microsoft's API hooking library — a building block for understanding and implementing hooks.

## 9. AI Assistance: Plugging Agents In

- **[REA (morluto/rea)](https://github.com/morluto/rea)**: a reverse engineering MCP for agents, chaining the analysis of binaries, applications and runtime behavior into reusable workflows and working alongside tools such as Ghidra.
- General-purpose coding agents can also drive the command-line tools above directly (Ghidra headless mode, rizin, Frida CLI); for ways to combine them see the AI Workflows Handbook.

## 10. Learning Resources

- [wtsxDev/reverse-engineering](https://github.com/wtsxDev/reverse-engineering): a collection of learning resources and tutorials.
- [mytechnotalent/Reverse-Engineering](https://github.com/mytechnotalent/Reverse-Engineering): free hands-on tutorials that start from x86 and ARM assembly.
- [michalmalik/linux-re-101](https://github.com/michalmalik/linux-re-101): an index of resources for reverse engineering on Linux.
- [Kanxue Forum](https://bbs.kanxue.com): a Chinese-language security and reverse engineering community (forum, courses and competition news).

---

> Companions: this section's Open-Source Projects and Hands-On Path; for the full disclaimer see Reverse Engineering (Unorthodox) §1.
