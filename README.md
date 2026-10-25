# Intelligence Research Atlas

**The load-bearing ideas behind AI, LLMs, neuroscience, and the mathematics of learning — distilled, mapped, and citable.**

Not a dump of papers. Not a textbook. A working map: 63 distilled findings, 13 diagrams, and a machine-readable paper index, covering 1936 to October 2026 — so you (or an agent you point at this repo) don't have to re-read the field to build on it.

> **One-sentence takeaway:** Intelligence — biological or artificial — is compression. Everything else in this atlas is a different substrate's way of doing that one thing better.

---

## What is inside

| | Verified count |
|---|---|
| Domains | 5 + master atlas |
| Findings (claim → evidence → implication) | 63 |
| Paper entries across the five volumes | 184 entries |
| Diagrams (Mermaid, render in GitHub / Obsidian) | 13 |
| Compiled PDF volumes | 6, 51 pages total |
| Machine-readable index | `index/papers-master.json` |
| Compiled | 2026-10-25 |

**Honest count note:** 184 is the sum of the five volume tables. Several landmark papers appear in more than one volume, so the number of *unique* papers is 138+. That overlap is deliberate — it is how the cross-domain connections show up.

## The five load-bearing connections

If you remember nothing else, remember these five bridges. Each is developed in `00_master-atlas/cross-domain-map.md`.

1. **Compression is the universal objective** — Shannon entropy, LLM cross-entropy loss, and cortical free energy are the same quantity, minimised by different substrates.
2. **Dopamine is the TD error** — the brain's reward-prediction error is the algorithm behind Q-learning, RLHF, and RLVR. Its pathologies (reward hacking) mirror addiction.
3. **Memory is an active process, not a log** — hippocampal maps, grid codes, and replay are the blueprint for agent memory: episodic stores, indexing, and consolidation.
4. **Search + learned priors beats either alone** — AlphaGo's template returns as chain-of-thought, tree search, and reasoning models.
5. **Sparse distributed coding, twice over** — V1 sparse codes and transformer superposition converged on packing more concepts than units, and both needed dictionary methods to decode them.

## The five domains

| Domain | Folder | What it answers |
|---|---|---|
| 01 Mathematical foundations | `01_mathematical-foundations/` | Why does learning work at all? Compression, inductive bias, scaling laws, grokking, emergence. F1–F14 |
| 02 Deep learning canon | `02_deep-learning-canon/` | What mechanisms did the transformer era inherit? Perceptron → backprop → CNN/LSTM → RL → self-supervision. F1–F10 |
| 03 LLM architecture & training | `03_llm-architecture-training/` | How do you build, align, and reason with LLMs? Pretraining, RLHF, RLVR, test-time compute, interpretability. F1–F12 |
| 04 Neuroscience of intelligence | `04_neuroscience-of-intelligence/` | What blueprints does backprop lack? Dopamine, prediction, replay, sleep, global workspace, local learning. F1–F14 |
| 05 Frontiers: new intelligence | `05_frontiers-new-intelligence/` | What comes after next-token prediction? World models, active inference, post-transformer architectures, agents, oversight. F1–F13 |

Each domain folder contains the same four things: `papers.md` (the canon, one entry per paper), `findings.md` (the distilled findings), `papers.json` (machine-readable), and `diagrams/` (Mermaid).

## Start here — by goal

- **New to the corpus?** → `00_master-atlas/reading-order.md`, then `00_master-atlas/master-mindmap.md`
- **Building or fine-tuning an LLM?** → Domain 03 findings, then Domain 01 (F8–F10 on scaling)
- **Designing a new architecture?** → Domain 01 (F1–F5, F11), all of Domain 04, all of Domain 05, then the cross-domain map
- **Learning the neuroscience?** → Domain 04 in full, then Domain 01 (F11, F14)
- **Alignment and safety?** → Domain 03 (F3, F6, F12), Domain 05 (F12–F13)
- **The whole story, chronologically?** → `00_master-atlas/timeline.md`, then 02, 03, 01, 04, 05

## For humans

Read the PDFs in `pdf/` for a clean, typeset version — one volume per domain, plus an overview. The Markdown is the living version; the PDFs are build artifacts generated from it, so if the two ever disagree, the Markdown wins.

## For agents

This repo is built to be *looked up, not re-read*. Inside this repo — and only inside this repo — `AGENTS.md` is the navigation protocol for anyone or anything working with this corpus: lookup patterns, the stable directory contract, and the conventions for adding papers and findings without breaking the index.

> Note: that `AGENTS.md` belongs to this public repo. It is not instructions for any personal assistant outside it.

## What this atlas is not

- **Not exhaustive.** ~150 unique papers were chosen for load-bearing ideas, not completeness.
- **Not a textbook.** Derivations are omitted; maths is named and sourced, not proven.
- **Not current past its compile date.** Content after 2026-10-25 is not represented. Treat 2025–2026 claims — especially on reasoning, diffusion LMs, and ARC — as the frontier at that date, not settled law.
- **Not uncontested.** Emergence, the information bottleneck, and several frontier claims are debated in the literature, and the findings say so where that matters.

## Traps this corpus documents

Emergence claims that are metric artifacts. Reasoning models that collapse past a complexity frontier. Reward hacking in RLHF. Benchmark contamination. Objectives that actively mislead (novelty search). Knowing these before you build is half the work.

## How to contribute

Follow the repo's own conventions, so the index stays rebuildable:

1. Findings are numbered within a domain and never renumbered — new findings append.
2. Paper entries in `papers.md` use the strict format the parser expects (year, title, authors, link, core idea, why it matters, keywords).
3. After editing any `papers.md`, regenerate the index and PDFs from `tools/` — never hand-edit a PDF.
4. Every new finding must cite at least one paper entry that exists in `papers.md`.
5. Keep diagrams to ~30 nodes or fewer; split rather than grow one diagram.

## Licence

This atlas — the distilled findings, diagrams, and index text written for it — is licensed under **CC BY 4.0** (see `LICENSE`). You may share and adapt it with attribution to tirunara.

Original papers, figures, and trademarks remain the property of their respective authors and publishers; this repo summarises and cites them, it does not republish them.

---

*Compiled 2026-10-25. The atlas is a map of the field as it stood then — use it to navigate, verify against the cited papers before you build on any single claim, and extend it as the field moves.*
