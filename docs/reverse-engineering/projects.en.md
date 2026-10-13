# Ludo Atlas · Reverse Engineering (Unorthodox) · Open-Source Projects

> The list is organized into three categories: decompilation and native ports, engine reimplementations, and learning resources and collections.
> All projects release only code and tools, never game assets; to use them you need to supply your own legal copy. For licensing and boundaries, see Reverse Engineering (Unorthodox) §1.

---

## 1. Decompilation and Native Ports (Turning a Finished Game Back into a Compilable Project)

These projects spend years "translating" the machine code of classic games back into readable, compilable source, then rebuild it on modern platforms. Reading one of them properly beats skimming ten toy projects: inside you find a complete architecture, toolchain and test system.

| Project | Game | Highlights |
| --- | --- | --- |
| [n64decomp/sm64](https://github.com/n64decomp/sm64) | Super Mario 64 | The template for decomp projects: naming conventions, matching workflow, documentation system |
| [zeldaret/oot](https://github.com/zeldaret/oot) | The Legend of Zelda: Ocarina of Time | How a large N64 project is organized |
| [zeldaret/mm](https://github.com/zeldaret/mm) | Majora's Mask | Building further on top of the Ocarina of Time toolchain |
| [zeldaret/tp](https://github.com/zeldaret/tp) / [zeldaret/tww](https://github.com/zeldaret/tww) | Twilight Princess / The Wind Waker | Project reconstruction for newer platforms |
| [HarbourMasters/Shipwright](https://github.com/HarbourMasters/Shipwright) | Ocarina of Time (Ship of Harkinian) | The full pipeline from decompilation to a native PC port |
| [HarbourMasters/2ship2harkinian](https://github.com/HarbourMasters/2ship2harkinian) | Majora's Mask | Reusing the same port framework |
| [Rubberduckycooly/Sonic-Mania-Decompilation](https://github.com/Rubberduckycooly/Sonic-Mania-Decompilation) | Sonic Mania | A decompilation case study for a modern-engine game |
| [snesrev/zelda3](https://github.com/snesrev/zelda3) | A Link to the Past | A solo-led, high-quality decompilation and port |
| [snesrev/smw](https://github.com/snesrev/smw) | Super Mario World | The decompilation route on the SNES |
| [open-goal/jak-project](https://github.com/open-goal/jak-project) | Jak and Daxter | A custom language and compiler (GOAL) built for an old platform; astonishing project scale |

Note: these projects usually state in their README that they do not provide game assets — you have to extract them yourself from a copy you legally own. Respect each project's license and naming conventions.

## 2. Engine Reimplementations (Keeping Old Games Playable with New Code)

The other route, complementary to decompilation: instead of restoring the original code, rebuild an engine from its behavior so the original assets keep running. Good for studying architectures that separate engine from content.

| Project | Game | Category |
| --- | --- | --- |
| [OpenMW/openmw](https://github.com/OpenMW/openmw) | The Elder Scrolls III: Morrowind | 3D RPG engine reimplementation |
| [Interkarma/daggerfall-unity](https://github.com/Interkarma/daggerfall-unity) | Daggerfall | Rebuilt on a modern engine |
| [exult/exult](https://github.com/exult/exult) | Ultima VII | Old-school RPG reimplementation |
| [OpenDiablo2/OpenDiablo2](https://github.com/OpenDiablo2/OpenDiablo2) | Diablo II | Data-driven reimplementation |
| [OpenRA/OpenRA](https://github.com/OpenRA/OpenRA) | Command & Conquer / Red Alert | RTS engine modernization |
| [OpenTTD/OpenTTD](https://github.com/OpenTTD/OpenTTD) | Transport Tycoon | The benchmark for industrial-grade long-term maintenance |
| [SFTtech/openage](https://github.com/SFTtech/openage) | Age of Empires II | A very long-cycle reimplementation project |
| [SupSuper/OpenXcom](https://github.com/SupSuper/OpenXcom) | X-COM | Tactics reimplementation |
| [bvschaik/julius](https://github.com/bvschaik/julius) / [augustus](https://github.com/Keriew/augustus) | Caesar III | City-builder mods and an enhanced fork |
| [OpenDune/OpenDune](https://github.com/OpenDune/OpenDune) | Dune II | A modern re-run of the RTS genre's founding title |
| [OpenRCT2/OpenRCT2](https://github.com/OpenRCT2/OpenRCT2) | RollerCoaster Tycoon 2 | Management-sim reimplementation |
| [CorsixTH/CorsixTH](https://github.com/CorsixTH/CorsixTH) | Theme Hospital | Lua-extension friendly |
| [yquake2/yquake2](https://github.com/yquake2/yquake2) | Quake II | A cleanup of the engine core |
| [Novum/vkQuake](https://github.com/Novum/vkQuake) | Quake | A testbed for Vulkan rendering |
| [Quake3e](https://github.com/ec-/Quake3e) | Quake III | A continuously maintained engine fork |
| [ZDoom/gzdoom](https://github.com/ZDoom/gzdoom) | Doom | The most active Doom engine fork |
| [FWGS/xash3d-fwgs](https://github.com/FWGS/xash3d-fwgs) | Half-Life (GoldSrc) | Engine behavior-compatibility research |
| [rwengine/openrw](https://github.com/rwengine/openrw) | GTA III | An attempt at an open-world reimplementation |
| [scummvm/scummvm](https://github.com/scummvm/scummvm) | Classic adventure game collection | One engine runs several hundred titles |
| [XProger/OpenLara](https://github.com/XProger/OpenLara) | Tomb Raider | A solo cross-platform engine experiment |
| [k4zmu2a/SpaceCadetPinball](https://github.com/k4zmu2a/SpaceCadetPinball) | 3D Pinball (bundled with Windows XP) | A template for reviving a small bundled system game |
| [djyt/cannonball](https://github.com/djyt/cannonball) | Sega OutRun | A modern rebuild of the arcade racing classic |
| [doukutsu-rs/doukutsu-rs](https://github.com/doukutsu-rs/doukutsu-rs) | Cave Story | A Rust reimplementation |
| [OpenKH/OpenKH](https://github.com/OpenKH/OpenKH) | Kingdom Hearts series | A combination of asset tools and engine research |

## 3. Learning Resources and Collections

- [wtsxDev/reverse-engineering](https://github.com/wtsxDev/reverse-engineering): a collection of learning resources and tutorials; start here to sweep the whole landscape.
- [mytechnotalent/Reverse-Engineering](https://github.com/mytechnotalent/Reverse-Engineering): free hands-on tutorials that start from x86 and ARM assembly.
- [michalmalik/linux-re-101](https://github.com/michalmalik/linux-re-101): an index of reverse-engineering material for the Linux platform.
- [Kanxue Forum](https://bbs.kanxue.com): a Chinese-language security and reverse-engineering community, with course material and event information.

## 4. How to Contribute to These Projects

- Start with documentation, tests and small fixes; read CONTRIBUTING first, then open your first pull request.
- These communities have strict rules about assets and naming (no bundled original material; function names must match the symbol tables), so search past issues before submitting.
- Low-quality generated patches get strict review in these projects; if you are unsure, open an issue and ask first.

---

> Companions: Toolchain and Hands-On Path in this section; for the full disclaimer, see Reverse Engineering (Unorthodox) §1.
