# Codebase Anatomy — Cross-Cutting Findings

What Chromium and VS Code agree on, extracted from the two deep dives ([chromium.md](chromium.md), [vscode.md](vscode.md)). These are the load-bearing lessons; each cites the deep-dive section and, through it, the primary source. Compiled 2026-10-25.

---

## F1 — Both giants state their reason for boundaries, and it is containment, not correctness

**Claim:** The founding architectural documents justify structure by assuming failure: "nearly impossible to build a rendering engine that never crashes or hangs … nearly impossible … perfectly secure" (Chromium); "misbehaving extensions should not impact the user experience" (VS Code).

**Evidence:** [chromium.md §1–2](chromium.md) — `C1`, `C13` of the VS Code dive ([vscode.md §6](vscode.md) — `V13`).

**Why it's efficient:** A rationale of containment cannot be eroded by optimism. Designs evaluated against "what happens when this breaks?" produce different structures than designs evaluated against "does this work?"

**How to apply:** Write the containment rationale into your architecture doc before writing the architecture.

---

## F2 — Dependency direction is enforced by machines, in both codebases, in the same shape

**Claim:** Chromium enforces layering with DEPS files (`-chrome`, `-components`, `specific_include_rules`, `new_usages_require_review = True`); VS Code with an ESLint whitelist table (`target → restrictions`, "!!! Do not relax these rules !!!"). Both are deny-by-default.

**Evidence:** [chromium.md §4](chromium.md) — `C12`; [vscode.md §2](vscode.md) — `V4`–`V5`.

**Why it's efficient:** Architecture that lives only in review conversation decays; a forbidden import that fails the build survives thousands of contributors. Whitelist semantics mean new paths never accidentally grant access.

**How to apply:** Express your layering as a machine-checked deny-by-default table in CI. This is the single highest-leverage move in either codebase.

---

## F3 — Every seam is an explicit contract generated from one source

**Claim:** Chromium: cross-process APIs are Mojom IDL files with sandbox attributes, generating both sides. VS Code: services are interface + runtime token (`createDecorator`), and the whole public extension API is one reviewable `vscode.d.ts` (21,241 lines) with 184 opt-in proposal files.

**Evidence:** [chromium.md §3](chromium.md) — `C9`–`C10`; [vscode.md §3, §7](vscode.md) — `V6`, `V17`.

**Why it's efficient:** One artifact generating all sides cannot drift; contracts make seams auditable (capability brokering) and diffable (API review as line changes).

**How to apply:** Define cross-boundary APIs in one IDL/schema/declaration file; generate or check the rest. Ban implementation imports across the seam.

---

## F4 — Volatile code lives in sacrificial processes with bounded recovery

**Claim:** Chromium respawns crashed renderers ("sad tab"); VS Code runs extensions/terminals/watching in utility processes, restarts the extension host up to 3 crashes per 5 minutes then offers bisect, and restarts the pty host capped at 5 with heartbeat detection.

**Evidence:** [chromium.md §1](chromium.md) — `C4`; [vscode.md §6](vscode.md) — `V13`–`V16`.

**Why it's efficient:** Process isolation caps the blast radius of any bug by construction; bounded restarts distinguish transient failures (recover silently) from broken components (stop and diagnose) — no crash loops.

**How to apply:** Put plugins/native/heavy subsystems behind RPC in workers; supervise with health signals and a sliding-window restart budget.

---

## F5 — Laziness is a framework feature, not consumer boilerplate

**Claim:** Chromium: `TaskPriority::BEST_EFFORT` and one pool with declared traits. VS Code: `InstantiationType.Delayed` services are Proxies over idle-time values; boot phases (`Starting/Ready/Restored/Eventually`) document what blocks first paint; `runWhenIdle` with a sync fallback.

**Evidence:** [chromium.md §6](chromium.md) — `C16`; [vscode.md §3, §9](vscode.md) — `V8`–`V9`, `V20`–`V21`.

**Why it's efficient:** Declaring cost/priority once, at registration, lets the scheduler optimize globally; consumers never write lazy-init boilerplate or race at init.

**How to apply:** Make eager-vs-lazy an explicit registration argument; define named boot phases; centralize idle deferral in one tested primitive.

---

## F6 — Resource pressure is a typed signal; components own their response

**Claim:** Chromium's `MemoryPressureLevel` (NONE/MODERATE/CRITICAL) broadcasts a coarse contract — "individual modules will implement their own policy" — and each subsystem sheds what it can recreate cheaply first.

**Evidence:** [chromium.md §7](chromium.md) — `C18` (enum and header quotes from `base/memory/memory_pressure_level.h`, `memory_pressure_listener.h`).

**Why it's efficient:** A minimal typed signal scales to arbitrary subscribers without a central controller knowing component internals; ownership of eviction policy stays local.

**How to apply:** Broadcast moderate/critical pressure; let each cache/buffer class register its own shed policy. See `05_adaptive-systems/patterns.md`.

---

## F7 — Reuse is governed: two consumers, no upward deps, no speculative layers

**Claim:** Chromium's components layer requires "code must be needed in at least 2 places," forbids upward dependencies and cycles, and "prefer[s] fewer top level components." VS Code achieves the same via "eat your own plugin API": even Git and TypeScript support are extensions, and core exposes internal contributions through one documented API file.

**Evidence:** [chromium.md §9](chromium.md) — `C23`; [vscode.md §10](vscode.md) — `V23`.

**Why it's efficient:** The two-consumer rule prevents speculative abstraction (the #1 source of modular rot); eating your own plugin API keeps the extension surface honest because first-party features exercise it.

**How to apply:** Extract shared modules only on the second real consumer; forbid upward deps mechanically; route first-party features through the same plugin mechanism third parties use.

---

## F8 — The error model and coupling budget are chosen once, project-wide

**Claim:** Chromium: exceptions banned and disabled at compile time, composition preferred over inheritance, forward declarations preferred over includes — each an explicit, motivated deviation written into the style guide. VS Code: one event system, one disposable contract, one DI pattern — every subsystem uses the same primitives.

**Evidence:** [chromium.md §8](chromium.md) — `C21`–`C22`; [vscode.md §4–5](vscode.md) — `V10`–`V12`.

**Why it's efficient:** Uniform primitives mean every contributor reads every subsystem the same way; deciding once in tooling (compiler flags, lint) keeps conformance out of review debates. At scale, header/import coupling dominates rebuild cost and legibility.

**How to apply:** Pick the error model, event pattern, and ownership pattern once; encode them in tooling; write motivated deviations into your guide so the reasoning survives.

---

## F9 — Performance is measured against a canonical scenario, and the data ships in-product

**Claim:** VS Code's `StartupTimings._isStandardStartup` gates metrics on a checklist (new window, trusted workspace, one editor, cached data …) and a built-in "Startup Performance" editor exposes raw marks; Chromium measures IPC (Mojo "roughly 1/3 faster with 1/3 fewer context switches") before migrating.

**Evidence:** [vscode.md §9](vscode.md) — `V22`; [chromium.md §3](chromium.md) — `C8`.

**Why it's efficient:** Unstandardized metrics are noise; a canonical scenario makes trend lines meaningful, and shipping the viewer turns regressions into one-command triage.

**How to apply:** Define the canonical scenario for any perf metric you track; expose the raw data in a debug view.

---

## F10 — Dead code doesn't ship: inclusion is explicit

**Claim:** VS Code: "only code that is referenced from the main entry files is loaded into the product"; web/desktop divergence is three entry files. Chromium: the same principle at build-graph level — component build vs static build over identical sources, with components sized "several dozen to several hundred files."

**Evidence:** [vscode.md §10](vscode.md) — `V24`; [chromium.md §5](chromium.md) — `C14`.

**Why it's efficient:** Making the entry list the reviewable unit of product surface means features can't ship by accident and platform divergence is visible in one place.

**How to apply:** Require an explicit import in a named entry file for anything to reach the bundle; review entry-file diffs as product-surface changes.
