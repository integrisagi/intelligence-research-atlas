# PLAYBOOK — The Rules

Thirty rules distilled from the whole corpus. Each: one imperative, a two-line rationale, and a link to the deep finding that grounds it. **R-numbers are append-only** — extend, never renumber.

Groups: [Structure](#structure) · [Interfaces](#interfaces) · [Concurrency & Resources](#concurrency--resources) · [Data](#data) · [Process](#process) · [Pre-ship checklist](#the-pre-ship-checklist) · [Hall of shame](#anti-pattern-hall-of-shame)

---

## Structure

**R1 — Enforce dependency direction with a machine, deny-by-default.**
Layering that lives in docs decays; layering that fails the build survives thousands of contributors. → [02.F1](02_structural-principles/findings.md)

**R2 — Deny by default for imports, permissions, and capabilities; fail closed.**
Every grant becomes an explicit, auditable line; unregistered requests terminate, never no-op. → [02.F12](02_structural-principles/findings.md)

**R3 — Extract shared modules only on the second real consumer.**
Speculative abstraction is the leading cause of modular rot. → [02.F10](02_structural-principles/findings.md)

**R4 — Make the bundle the dependency graph: explicit entry files.**
Only imported code ships; entry-file diffs are the reviewable unit of product surface. → [02.F11](02_structural-principles/findings.md)

**R5 — Prefer composition; treat every include as a coupling budget.**
Deep hierarchies make lifetimes illegible; headers dominate rebuild cost at scale. → [02.F7](02_structural-principles/findings.md)

## Interfaces

**R6 — Every seam is a versioned contract generated from one artifact.**
IDL/schema/declaration in, both sides generated — the contract cannot drift. → [02.F2](02_structural-principles/findings.md)

**R7 — Choose the error model once, project-wide; encode it in tooling.**
Mixed error models multiply control-flow states per call site. → [02.F8](02_structural-principles/findings.md)

**R8 — Services = interface + runtime token + constructor injection; child containers scope lifecycles.**
Injected deps are substitutable in tests and per-window scoping falls out free. → [02.F3](02_structural-principles/findings.md)

**R9 — Public API is one reviewable surface; experiments quarantine behind opt-in flags banned from release.**
Stability becomes a process property, not a hope. → [vscode.md §7](01_codebase-anatomy/vscode.md)

**R10 — Write the containment rationale before the architecture: what happens when this breaks?**
Designs evaluated against failure produce different structures than designs evaluated against success. → [01.F1](01_codebase-anatomy/findings.md)

## Concurrency & Resources

**R11 — Mutable objects have one home sequence; ownership transfers by message.**
Sequence-based ownership eliminates data races by construction, not discipline. → [02.F9](02_structural-principles/findings.md)

**R12 — One scheduler per process, tasks declared with traits (priority, blocking-ness).**
A single pool with metadata can globally prioritize; ad-hoc threads cannot. → [02.F9](02_structural-principles/findings.md)

**R13 — Volatile code runs in sacrificial workers: no shared UI, no startup cost, crash survivable.**
An OS process is the only boundary that contains hangs and crashes without cooperation. → [02.F4](02_structural-principles/findings.md)

**R14 — Restart within budget, then stop and diagnose.**
Sliding-window restart counts separate transient faults from broken components; no crash loops. → [02.F5](02_structural-principles/findings.md)

**R15 — One dispose contract, store-then-forget ownership, leak tracker with creation stacks in dev.**
The boilerplate you skip is the leak you debug in production. → [02.F6](02_structural-principles/findings.md)

**R16 — Measure the resource envelope at boot; derive every pool, cache, and batch size from it.**
Hardcoded defaults are worst-case guesses; the envelope is the actual constraint. → [05.F4](05_adaptive-systems/findings.md), [patterns P2](05_adaptive-systems/patterns.md)

**R17 — Broadcast typed pressure signals (moderate = drop caches, critical = drop everything); components own their response.**
One cheap probe fans out to N subsystems; eviction policy stays local where the knowledge is. → [05.F1](05_adaptive-systems/findings.md), [patterns P1](05_adaptive-systems/patterns.md)

**R18 — Every inter-stage queue is bounded; backpressure lands at the source.**
Unbounded buffering converts overload into OOM; pausing intake converts it into latency. → [05.F8](05_adaptive-systems/findings.md), [patterns P4](05_adaptive-systems/patterns.md)

**R19 — Caches are bounded by cost (bytes), admit by demonstrated frequency.**
A scan destroys a count-bounded LRU; 8 bytes of sketch protects the hot set. → [05.F10](05_adaptive-systems/findings.md)

## Data

**R20 — Event time travels end to end; watermarks make reprocessing reproducible.**
Processing time is nondeterministic under retries; event time makes pipeline changes testable. → [04.F3](04_data-pipelines/findings.md)

**R21 — Persisted/transmitted data has a versioned schema with declared compatibility, checked in CI.**
A breaking change becomes a rejected registration instead of a production incident. → [04.F9](04_data-pipelines/findings.md), [02.F13](02_structural-principles/findings.md)

**R22 — One log-centric path; replay history instead of maintaining dual batch/stream logic.**
Two code paths for one result guarantee divergence. → [04.F6](04_data-pipelines/findings.md)

**R23 — Sinks are idempotent: at-least-once delivery + unique-per-work-unit output.**
Retries are routine at scale; uniqueness makes them harmless by construction. → [04.F5](04_data-pipelines/findings.md)

**R24 — Data quality gates run in the promotion path — fail the deploy, not the dashboard.**
Tests-as-queries catch bad upstream data at the boundary. → [04.F13](04_data-pipelines/findings.md)

## Process

**R25 — Review standard: "better, not perfect," one-business-day latency, small self-contained changes.**
The latency SLO is what makes the strict checklist affordable. → [03.F1](03_engineering-workflow/findings.md)–[F3](03_engineering-workflow/findings.md)

**R26 — Trunk + feature flags; flag hygiene (review-for-delete) is a scheduled task.**
Daily integration bounds merge cost; forgotten flags become permanent configuration branching. → [03.F6](03_engineering-workflow/findings.md)–[F7](03_engineering-workflow/findings.md)

**R27 — Test pyramid ~80/15/5; presubmit gates only fast, hermetic tests.**
Presubmit latency multiplies across every change per day; postsubmit catches the long tail with an owner. → [03.F8](03_engineering-workflow/findings.md)–[F11](03_engineering-workflow/findings.md)

**R28 — Reliability has a budget: SLO → error budget → releases halt; canary with a control; blameless postmortems.**
The budget replaces the velocity-vs-reliability argument with a number both sides read. → [03.F13](03_engineering-workflow/findings.md)–[F16](03_engineering-workflow/findings.md)

**R29 — Design doc before big code: context, goals, non-goals, the design, alternatives considered.**
Async written review parallelizes senior judgment and preserves decision context. → [03.F18](03_engineering-workflow/findings.md)

**R30 — Measure performance against a canonical scenario and ship the debug view.**
Unstandardized metrics are noise; in-product views make regressions one-command triage. → [01.F9](01_codebase-anatomy/findings.md)

---

## The pre-ship checklist

Answer these ten before declaring work done. Each links to the rule that motivates it.

1. Can a machine (lint/build) verify my dependency direction, or did I only document it? — [R1]
2. Does every new cross-boundary API exist as one contract artifact? — [R6]
3. Are new dependencies injected (mockable) rather than reached as globals? — [R8]
4. What happens when this crashes or hangs — is the volatile part isolated? — [R13]
5. Is recovery bounded (restart budget), and can this process be SIGKILLed at any time? — [R14]
6. Is every queue bounded, and where exactly does backpressure land? — [R18]
7. Do pools/caches/batches derive from the measured envelope rather than hardcoded numbers? — [R16]
8. Is risky behavior behind a flag with a safe default, and does the flag have a deletion date? — [R26]
9. Is there a fast hermetic test that would fail if this code were broken? — [R27]
10. Can I name the canonical scenario my performance claims were measured on? — [R30]

## Anti-pattern hall of shame

| Anti-pattern | Why it's poison | Rule violated |
|---|---|---|
| Global mutable state / convenience singletons | Lifecycles go global; tests go brittle; two instances become impossible | R8 |
| Unbounded queue "just for now" | Overload becomes OOM instead of latency | R18 |
| Retry without jitter or budget | 243× load amplification; retry storms | [05.F11](05_adaptive-systems/findings.md), [patterns P6](05_adaptive-systems/patterns.md) |
| Silent catch / swallow | Errors become valueless signals; failures surface far from cause | R7 |
| Deep inheritance hierarchies | Lifetime and ownership illegible across boundaries | R5 |
| Speculative abstraction layer | Wrong assumptions accrete on a module nobody uses | R3 |
| Threshold controller without damping | Self-sustained oscillation: actuation perturbs the signal | [05.F13](05_adaptive-systems/findings.md) |
| Feature flags that never die | Permanent branching-by-configuration | R26 |
| Per-hop timeouts without propagation | Invisible multiplication of retries and latency | [patterns P8](05_adaptive-systems/patterns.md) |
| Optimizing without a canonical scenario | Noise; regressions undetectable | R30 |
| Hardcoded worker/cache counts | Wrong on every machine but yours | R16 |
| `# Do NOT add X` comments with no enforcement | Suggestions rot; machines don't | R1 |
