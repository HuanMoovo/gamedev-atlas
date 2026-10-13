# Ludo Atlas · Reverse Engineering (Unorthodox) · Defense

> You only learn how to protect your own work once you can take other people's apart. This page gives game developers a defense checklist: from the release build to post-launch response.
> A premise to accept: single-player content cannot be absolutely protected; the goal of defense is to raise the cost, protect online fairness and payment, and protect the player experience.
> For the disclaimer, see Reverse Engineering (Unorthodox) §1; for the full legal background, see Legal, Patents & Competition.

---

## 1. Set Expectations Straight

- **Single-player content can inevitably be read**: data, textures and story all sit on the player's machine and can physically be extracted. What defense must do is not "block everything" but "make teardown and distribution cost more than they are worth".
- **The three things actually worth protecting**: online fairness (anti-cheat), payment and authorization (in-app purchases and licensing), and player experience (saves and achievements left intact, the mod ecosystem not caught in the crossfire).
- **Hostility is the worst solution**: treating every player as a suspect (heavy anti-debugging, bundled drivers) hurts word of mouth and performance, and often harms legitimate users by mistake.

## 2. Release-Build Hygiene

- Strip symbols and clear out development comments; don't ship development paths, test-server addresses or keys inside the package (the most common category in leak incidents).
- Write the version and build number into the artifact itself (for the method, see Build & Release); grade crash logs, and keep the debug surface out of public builds.
- Keep release and development builds strictly separate; turn off useless debug interfaces and remote commands.

## 3. Integrity Checks and Anti-Tampering (base layer)

- Hash and signature checks on assets and code: they won't stop an expert, but they stop bulk tools and scripts and significantly raise the cost of adaptation.
- Add checksums and version numbers to saves, and define a conflict strategy for cloud sync (for a more complete approach, see the accounts and state chapter of Multiplayer & Backend).
- Put key decisions server-side: online values, drops and settlements are computed on the server, with the client doing presentation only; on the protocol side, trust no client input.

## 4. Obfuscation and Packing (as needed)

- Commercial solutions (VMProtect, Themida, Denuvo and the like): high cost, and results depend on the genre; adding packing after launch hurts updates and compatibility.
- In-house obfuscation: name obfuscation and control-flow transformation, focused on covering hot modules rather than everything.
- Packing has a cost: crash logs become harder to read, and compatibility and performance take a hit; assess the support cost before deciding.

## 5. Anti-Cheat (online projects)

- A three-layer structure: client-side detection (integrity and hardening), server-side detection (behavior and statistics), community handling (reports, bans, economy rollbacks).
- Off-the-shelf solutions save a lot of engineering: integrate EAC, BattlEye and the like early; the standard in-house approach is server authority plus behavior analysis.
- Compliance and privacy: what detection collects, how long it is kept and who can see it must be written into the terms of service and privacy policy; in mainland China you also have to clear the compliance gates around data and minors.
- A five-step response plan: detection, confirmation, handling, rollback, announcement. Write the plan in advance, and you won't be caught off guard when something happens.

## 6. Mods and Community (turn rivals into friends)

- Official mod support is good defense: give people a legitimate channel for tinkering, and a slice of the grey channels' audience goes away. For tools and terms, see Modding & UGC.
- Spell out the boundaries of offline mode, self-hosted servers and single-player conversion in the terms of service; for community projects, communicate before you act.

## 7. After Launch

- Monitor anomalies: ledgers and drop distributions, win-rate outliers, crash clusters (for tools, see Telemetry & Analytics).
- Fast response matters more than a perfect plan; every public action is a chance to communicate with players.
- Tie update cadence to defense intensity: frequent updates are themselves a form of defense.

---

> Companions: this section's Toolchain and Hands-On Path; Modding & UGC, Build & Release, Telemetry & Analytics, Legal, Patents & Competition. The full disclaimer is in Reverse Engineering (Unorthodox) §1.
