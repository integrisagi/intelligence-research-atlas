# Big-Tech Code Structure & Systems Deconstruction

A research corpus deconstructing how big tech actually builds scalable, modular, resource-adaptive software — Chromium, VS Code, Google/Meta engineering workflow, data pipelines, and adaptive systems — distilled into numbered findings, adoptable rules, and an agent persona.

**Coverage window:** sources as of October 2026.
**Compiled:** 2026-10-25.
**Grounding law:** every finding carries at least one verified source (design doc, official docs, paper, or real source file). Claims that could not be verified were dropped, not guessed.

## Why this exists

AI-generated code usually stops at "the model thinks it's right". This corpus exists so a future agent (or a future you) can stop guessing and build the way systems that run at planetary scale are actually built:

- **Findings** — the load-bearing structural decisions, each with evidence, why it's efficient, and how to apply it.
- **Deep dives** — two codebases (Chromium, VS Code) dissected layer by layer.
- **PLAYBOOK** — the whole corpus compressed into numbered rules plus a pre-ship checklist.
- **PERSONA** — an adoptable identity that makes an agent work this way by default.

## Folder layout (agent-optimized)

```
corpora/god-tier-code/
├── README.md                     ← you are here (human overview)
├── AGENTS.md                     ← navigation protocol for AI agents
├── PERSONA.md                    ← adoptable "Big-Tech Systems Engineer" identity
├── PLAYBOOK.md                   ← numbered rules R1…Rn + pre-ship checklist
├── master-map.md                 ← whole-corpus Mermaid mindmap + reading orders
├── SOURCES.md                    ← master source index
├── 01_codebase-anatomy/          ← Chromium + VS Code deep dives, cross-cutting findings
├── 02_structural-principles/     ← transferable structure rules (layering, DI, boundaries)
├── 03_engineering-workflow/      ← how Google/Meta/Microsoft operate (review, monorepo, SRE)
├── 04_data-pipelines/            ← how big tech moves data (logs, streams, schemas, quality)
└── 05_adaptive-systems/          ← resource-aware behavior + 9 pseudocode patterns
```

## Where to start

- **Want the rules?** → [`PLAYBOOK.md`](PLAYBOOK.md)
- **Want the mindset?** → [`PERSONA.md`](PERSONA.md)
- **AI agent?** → read [`AGENTS.md`](AGENTS.md) first.
- **Building a modular app or library?** → `01_codebase-anatomy/` then `02_structural-principles/`
- **Running a service that must not fall over?** → `05_adaptive-systems/`
- **Moving data at scale?** → `04_data-pipelines/`
- **Need the big picture?** → [`master-map.md`](master-map.md)

## The one-paragraph summary

Big tech's edge is not talent density; it is **structure**: dependency direction treated as law and enforced by machines (DEPS files, lint rules) rather than by hope; every seam an explicit contract (Mojo interfaces, DI services, frozen extension APIs, data schemas); failure isolated behind process boundaries; work shaped for review and reuse (small CLs, monorepo, design docs, error budgets); and runtime behavior that flexes with available resources instead of falling over (memory-pressure signals, adaptive concurrency limits, backpressure, graceful degradation). None of this is magic. Every piece is a small rule applied relentlessly — and every piece is transferable to any codebase, including the one an agent is about to write. This corpus documents those pieces.
