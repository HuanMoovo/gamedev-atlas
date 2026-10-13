# Ludo Atlas · Reverse Engineering (Unorthodox)

> Positioning: a learning route that does not go through the front door. The front door is tutorials, documentation and source code; the unorthodox route is taking finished products apart to see how they actually run.
> Written for people who want to learn by taking things apart, people who make mods and ports, people who want to get old works running again, and people who need to protect their own works.
> As of October 2026; tools and projects update quickly, so check each repository's latest status and license before you start.

---

## 1. Disclaimer

This section is for **study, research and interoperability** purposes only: understanding how programs work, making legally owned works playable again, creating mods and Chinese localizations for works you are authorized to work on, and analyzing and hardening your own software.

- Comply with the laws of your jurisdiction (copyright law and the Regulations on the Protection of Computer Software, the US DMCA, EU software directives and so on), and respect software licenses and terms of service.
- Do not use these techniques to: distribute pirated copies and cracks, circumvent technological protection measures, create or distribute hacks and cheat tools, or gain unauthorized access to other people's systems.
- The tools and projects listed all point to their official repositories; this repository provides no downloads of copyright-protected resources and accepts no responsibility for how they are used.
- "Research use" does not automatically amount to a legal exemption; when you are not sure, consult a professional first. This page does not constitute legal advice.

For the full legal background, see [Legal, Patents & Competition](../publishing/legal/README.md).

## 2. Why It Is Worth Learning

Treating published works as teaching material is the sharpest blade a self-learner has — and the one that most demands restraint. Three concrete returns:

- **See how design lands in practice**: taking apart a save or a set of level data gets you to "how design becomes implementation" faster than reading three tutorials.
- **Technical archaeology**: the trade-offs old works made under tiny memory and compute budgets are a reference sample for the problems you cannot solve today just by throwing resources at them.
- **Interoperability and preservation**: getting old works running again on new platforms, mods, Chinese localizations and fixes all rest on "reading binaries written by someone else".

When it is worth pulling out: the thing you want to learn from has no source code; it has source code but is missing documentation; you need compatibility or migration; you are assessing the attack and defense surface of your own work when it is taken apart.

## 3. The Four Threads of This Section

| Thread | What you get | Entry point |
| --- | --- | --- |
| Teardown and learning | A from-zero practice route and mini-experiments within legal bounds | [Hands-On Path](practice.md) |
| Tools and ecosystem | Tool selection for disassembly, debugging, packet capture and asset extraction | [Toolchain](tools.md) |
| Projects and cases | A list of open-source projects: decompilation, engine reimplementation and more | [Open-Source Projects](projects.md) |
| Boundaries and compliance | What you can do and what you must not touch | This page §1 and Legal, Patents & Competition |

## 4. First-Week Checklist

1. **Pick safe targets only**: programs you wrote yourself, open-source games, works with official mod support, public teaching labs and CTF challenges.
2. **Install a minimal toolset**: a disassembler (Ghidra), a debugger (x64dbg), file identification (Detect It Easy), a hex editor (ImHex); use Cheat Engine to get started with game memory.
3. **Run three small experiments**: change one check in a program you wrote yourself; use Cheat Engine to change a single-player value (your own game or a teaching lab); read the disassembly of the same short piece of code side by side at -O0 and -O2.
4. **Use the three-line log**: for every experiment, write down the goal, the process and the findings. What the unorthodox route fears most is not difficulty, but aimlessness.

## 5. Target Aggressiveness (from safe to dangerous)

1. Your own works and open-source projects: take them apart freely; practice first.
2. Works with official open data (a mod toolchain, public file formats): follow the official terms.
3. Public teaching labs and reverse-engineering CTFs: legal and systematic.
4. General commercial products: static reading for research purposes is a grey area in most jurisdictions — read §1 and Legal, Patents & Competition first, then decide; never distribute extracted copyright-protected assets.
5. There is no item 5 here: online-game server sides and anti-cheat, bypassing other people's paid software, and distributing cracks are outside this section's scope.

## 6. Learning Map

- How to choose tools and how they divide by use: [Toolchain](tools.md)
- How far others have gotten: [Open-Source Projects](projects.md); decompilation projects (such as sm64, zelda3) are often the best textbook for "reading a large codebase"
- From zero to capable: a four-week route and three mini-experiments, in [Hands-On Path](practice.md)
- Related handbooks: Modding & UGC (legitimate extension and distribution), AI Workflows (agent-assisted analysis), Legal, Patents & Competition (boundary details), Pitfalls & Anti-patterns (pre-release checks)

---

> Companion reading: Modding & UGC · AI Workflows · Legal, Patents & Competition. All pages in this section are for study and research only; the full disclaimer is in §1.
