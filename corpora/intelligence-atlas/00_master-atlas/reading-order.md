# Reading Order — Paths Through the Atlas

Ranked reading paths by goal. Each entry: read `findings.md` first (20 min), then `papers.md` for whichever findings matter to you. Time estimates assume human reading; agents should ingest findings + targeted papers.

---

## Path A — "I want to build/fine-tune LLMs" (practitioner)

1. `03/findings.md` — the LLM stack end to end (pipeline, RLHF, RLVR, test-time compute) · **90 min**
2. `01/findings.md` F8–F10 — scaling laws, emergence, grokking (budgeting and expectations) · **30 min**
3. `03/papers.md` — pick your stack: LoRA, RAG, DPO/GRPO, FlashAttention, MoE · **targeted**
4. `05/findings.md` F11–F12 — agent stack + self-improvement (where systems are heading) · **30 min**

**Key papers to actually read in full:** Attention Is All You Need · InstructGPT · DeepSeek-R1 · Snell et al. 2024 · LIMA.

## Path B — "I want to design a new architecture / new type of intelligence"

1. `01/findings.md` F1–F3, F5, F11 — compression, bias, depth, regimes, recurring patterns · **45 min**
2. `04/findings.md` — mechanisms backprop lacks: replay, local learning, global workspace, criticality · **90 min**
3. `05/findings.md` — the paradigm map: world models, active inference, the architecture zoo · **60 min**
4. `00_master-atlas/cross-domain-map.md` — the five load-bearing connections · **15 min**

**Key papers:** Chinchilla · DreamerV3 · LeCun JEPA · Mamba · Ramsauer 2020 (Hopfield-as-attention) · Friston active inference · Wang et al. 2018 (meta-RL).

## Path C — "I want the neuroscience foundation"

1. `04/findings.md` F1–F3 — Hebbian learning, dopamine/TD, predictive processing · **45 min**
2. `04/findings.md` F4–F9 — codes, memory, sleep, workspace, criticality, topology · **60 min**
3. `04/papers.md` — Schultz 1997, Rao & Ballard 1999, Wilson & McNaughton 1994, Wang 2018 in full
4. `01/findings.md` F11, F14 — the mathematical mirrors (criticality, energy-based unification)

## Path D — "I care about alignment / safety"

1. `03/findings.md` F3, F6, F12 — RLHF failure modes, reasoning limits, evaluation crisis · **40 min**
2. `05/findings.md` F12–F13 — self-improvement loops, scalable oversight · **30 min**
3. Papers: Constitutional AI · AI Safety via Debate · Weak-to-Strong · Illusion of Thinking · circuit tracing (2025).

## Path E — "Give me the whole story, chronologically"

1. `00_master-atlas/timeline.md` — 80 years in one view · **15 min**
2. `02/findings.md` — the classics era · **60 min**
3. `03/findings.md` — the LLM era · **90 min**
4. `01/findings.md` — why any of it works · **75 min**
5. `04/findings.md` + `05/findings.md` — the biological lens and the frontier · **2.5 h**

---

## For AI agents (machine reading order)

1. `AGENTS.md` (conventions) → 2. `INDEX.md` (locate) → 3. target-domain `findings.md` → 4. `papers.json` / `index/papers-master.json` for citations → 5. domain `diagrams/` if spatial structure helps. Total context for full-corpus findings: ~45K tokens — feasible in one context window.
