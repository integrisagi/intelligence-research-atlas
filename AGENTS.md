# AGENTS.md — Navigation Protocol for AI Agents

You are an agent that has been pointed at this corpus. Read this file fully before doing anything else. It tells you what lives here, how to query it efficiently, and how to extend it without breaking conventions.

## What this corpus is

A curated knowledge base of the major research (1943–2026) behind artificial intelligence, large language models, the neuroscience of intelligence, and the mathematics of learning. It is organized for **lookup, not re-reading**: findings are pre-distilled, papers are one-liners, diagrams are pre-built.

## Directory contract (stable — do not rename)

| Path | Contents | Read when |
|---|---|---|
| `00_master-atlas/master-mindmap.md` | Whole-corpus Mermaid mindmap | You need a map of everything |
| `00_master-atlas/timeline.md` | Chronology of milestones | You need "what happened when" |
| `00_master-atlas/cross-domain-map.md` | Graph linking neuro ↔ math ↔ AI concepts | You need cross-field connections |
| `00_master-atlas/reading-order.md` | Ranked reading paths by goal | Planning study or research |
| `01_mathematical-foundations/findings.md` | Information theory, learning theory, scaling laws, grokking, emergence | Reasoning about why/how learning works, choosing scale |
| `02_deep-learning-canon/findings.md` | 1943–2016 classics (perceptron → backprop → CNN/LSTM → RL → SSL) | You need foundational mechanisms |
| `03_llm-architecture-training/findings.md` | Transformers, pretraining, RLHF, reasoning models, interpretability (2017–2026) | Building, fine-tuning, or analyzing LLMs |
| `04_neuroscience-of-intelligence/findings.md` | Hebbian learning, dopamine/RL, predictive coding, memory/replay, criticality | Borrowing brain mechanisms |
| `05_frontiers-new-intelligence/findings.md` | World models, active inference, post-transformer architectures, agents, self-improvement | Designing novel intelligence |
| `index/papers-master.json` | All papers: id, title, authors, year, url, domain, contribution | Programmatic lookup / citation building |
| `pdf/*.pdf` | Six typeset volumes (one per domain + overview) | Human-readable deliverables |

## Lookup patterns

**"What does research say about X?"**
1. Grep `*/findings.md` for the concept: `grep -ril "concept" */findings.md`
2. Read the matching finding block(s) (they are self-contained: claim → evidence → implication → papers).
3. For citations, pull entries from `index/papers-master.json` (`jq '.[] | select(.keywords[] | contains("scaling"))'`).

**"I'm building Y — what applies?"**
- LLM/training decisions → 03 findings, then 01 (scaling/optimization).
- Novel architecture → 05 (paradigm map + diagrams/paradigm-map.md), then 04 for mechanisms worth stealing.
- Efficiency/parameters → 03 findings (LoRA, quantization, attention kernels, MoE).

**"Where are the diagrams?"**
Every domain has `diagrams/*.md` with Mermaid fenced blocks. They render in Obsidian and GitHub. The master maps are in `00_master-atlas/`.

## Conventions (follow when extending)

1. **Findings are numbered** `## F1 — Title` within each domain, and never renumbered; new findings append (F13, F14…).
2. **Paper entries** in `papers.md` use the strict format the parser expects:
   ```
   ### [YEAR] Title — Authors
   - **Link**: <url or venue>
   - **Core idea**: one sentence
   - **Why it matters**: one sentence
   - **Keywords**: comma,separated
   ```
   Then re-run `python3 tools/build_index.py` from the corpus root to regenerate `papers.json` + `index/papers-master.json`.
3. **Mermaid**: keep diagrams ≤ ~30 nodes; split into multiple files rather than growing one. Use `mindmap` for taxonomies, `graph LR/TD` for causal/flow relations, `timeline` for chronology.
4. **PDFs are build artifacts** — regenerate with `python3 tools/build_pdfs.py` after content edits; never hand-edit PDFs.
5. **Dates are absolute** (e.g. "2025-03", not "last year"). Corpus compiled 2026-10-25; content after that date is not represented.
6. **Claims carry evidence.** Any new finding must cite at least one paper entry that exists in `papers.md`.

## Non-goals

- Not a textbook: derivations are omitted; math is named and sourced, not proven.
- Not exhaustive: ~150 papers chosen for load-bearing ideas, not completeness.
- No vendor marketing: system reports (GPT-4, Gemini) are included as system-scale evidence, flagged as such.
