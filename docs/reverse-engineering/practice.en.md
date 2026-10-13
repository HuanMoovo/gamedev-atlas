# Ludo Atlas · Reverse Engineering (Unorthodox) · Hands-On Path

> A four-week starter route, three mini experiments, and a list of common pitfalls. Every exercise uses only your own work, open-source games, or public training ranges.
> For the disclaimer, see Reverse Engineering (Unorthodox) §1; for tool setup, see Toolchain.

---

## 1. The Four-Week Route (3–5 Hours per Week)

### Week 1: Concepts and Preparation

- Fill in four concepts: number bases and endianness, file magic numbers, memory and addresses, and the call stack.
- Learn the structure of an executable file (PE or ELF, either is fine; drawing it yourself once beats reading about it ten times).
- Install the five-tool kit: Ghidra, x64dbg, Detect It Easy, ImHex and Cheat Engine.
- Acceptance: you can explain roughly what happens from double-clicking an exe to reaching main.

### Week 2: Static Analysis

- Open a small program you wrote yourself in Ghidra (one with a few functions and branches).
- Compile it once at each of the -O0 and -O2 optimization levels, and compare the disassemblies to find the differences.
- Acceptance: you can locate main and the target functions you wrote, and explain what the compiler did at each level.

### Week 3: Dynamic Debugging

- x64dbg: set breakpoints, single-step, watch registers and memory; break at the key branch in the Week 2 program.
- Cheat Engine: change a value in a small game you wrote yourself (or one from a training range), going from searching for the value all the way to finding the base address.
- Acceptance: you can write down where the value lives and why changing it changes the game.

### Week 4: Data and Assets

- Take apart a data file from an open-source game (a Godot open-source project, or an asset pack you made yourself).
- Write a Python script of about 30 lines that reads out one column of the data.
- Acceptance: the script runs, and you can explain what every field in the format means.

## 2. Three Mini Experiments (Follow-Along)

**Experiment 1: Patch Your Own Program**

1. Write a small program with a "full version / trial version" switch;
2. Find the decision branch in Ghidra;
3. Work out the bytes to change and write them back into a copy;
4. Run it and verify the behavior change.

Acceptance: you can write a three-line table: instruction before, instruction after, behavior difference.

**Experiment 2: Side-by-Side Reading at Function Level**

Pick an algorithm you know well (bubble sort, say), compile it once at each of -O0, -O1 and -O2, compare the three disassemblies, and say what each optimization level removed.
Acceptance: one summary line for each of the three disassemblies.

**Experiment 3: A Small Asset-Extraction Tool**

Write a small tool for an open-source game (or its sample assets): scan a directory, identify formats by file header, and export embedded images.
Acceptance: the tool gives correct results for two different formats.

## 3. Common Pitfalls

- **The target is too big**: wanting to take apart a big-budget title in week one. Set one concrete question first, such as "where does the gold in this save file live."
- **Gear collecting**: a pile of tools installed, none used for more than an hour. Get fluent with the five-tool kit before swapping in anything else.
- **Going on the offensive too early**: anti-debugging, packers and VM-based protection are a separate field; first practice on unprotected targets until it is second nature.
- **The three red lines**: no pirated assets, no circumventing technical protection measures, no cheat tools or crack distribution (for details see §1 and Legal, Patents & Competition).
- **Dismantling without notes**: use the three-line log; only by reviewing it a week later do you know what you actually learned.
- **Going in alone**: if you are stuck for more than two hours, change your angle, or take what you have tried to the community and ask.

## 4. Advanced Directions

- **Engine-specific work**: Unity (the IL2CPP route), Unreal (blueprints and assets), Godot (gdsdecomp); for tools, see Toolchain §5.
- **Security research**: CTF is the most systematic practice ground; the event calendar is at [CTFtime](https://ctftime.org), and challenge courses are at [pwn.college](https://pwn.college).
- **Protecting your own work**: integrity checks, code obfuscation, server-side authority; you have to know attack to know defense.
- **Fan translation and localization engineering**: text extraction, font replacement, backfill and regression; this connects to the processes in Localization.

---

> Companions: the Toolchain and Open-Source Projects pages in this section; for the full disclaimer, see Reverse Engineering (Unorthodox) §1.
