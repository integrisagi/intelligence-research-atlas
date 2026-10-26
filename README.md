# Research Atlas — Two Corpora, Kept Separate

Two research corpora in one public repo, **kept isolated from each other** — and from any personal assistant's own system. Each corpus has its own folder, its own index, and its own agent navigation file. Nothing at the top level tells an agent to adopt either corpus's persona or rules.

Use one corpus at a time. Point a future agent at exactly one corpus folder, not at this repo root.

---

## The two corpora

### 1. Intelligence Atlas — what intelligence is

`corpora/intelligence-atlas/`

The load-bearing ideas behind AI, LLMs, neuroscience, and the mathematics of learning — distilled, mapped, and citable.

- **63 findings** (14 maths + 10 deep learning + 12 LLM + 14 neuroscience + 13 frontiers)
- **138+ unique papers** (184 entries across the five volumes; several papers appear in more than one volume, which is how the cross-domain connections show up)
- **13 diagrams** (Mermaid, render in GitHub / Obsidian)
- **6 PDF volumes, 51 pages**
- **Machine-readable index:** `corpora/intelligence-atlas/index/papers-master.json`
- **Compiled:** 2026-10-25

Its one-sentence takeaway: intelligence — biological or artificial — is compression. Its five load-bearing connections are compression as the universal objective, dopamine as the TD error, memory as an active process, search + learned priors beating either alone, and sparse distributed coding, twice over.

Start there: `corpora/intelligence-atlas/00_master-atlas/reading-order.md`
Its own presentation: `corpora/intelligence-atlas/docs/presentation.html`
Its own agent navigation file (for use *inside that corpus only*): `corpora/intelligence-atlas/AGENTS.md`

### 2. God-Tier Code — how the best code is actually built

`corpora/god-tier-code/`

A deconstruction of how big tech actually builds scalable, modular, resource-adaptive software — Chromium, VS Code, Google/Meta engineering workflow, data pipelines, and adaptive systems.

- **73 corpus findings** (10 codebase anatomy + 14 structural principles + 22 workflow + 13 data pipelines + 14 adaptive systems), distilled from **110 verified research findings** (Chromium C1–C24, VS Code V1–V24, workflow/pipelines W1–W35, adaptive D1–D27)
- **30 playbook rules** (R1–R30) + a 10-question pre-ship checklist + an anti-pattern hall of shame
- **9 adaptive patterns** (P1–P9, pseudocode only — not runnable implementations, by design)
- **7 Mermaid diagrams**, all under the 30-node limit
- **~24,700 words** across 22 markdown files, plus a build report
- **Compiled:** 2026-10-25

Its one-sentence takeaway: big tech's edge is not talent density, it is structure — dependency direction enforced by machines, every seam an explicit contract, failure isolated behind process boundaries, and runtime behaviour that flexes with available resources instead of falling over.

Start there: `corpora/god-tier-code/PLAYBOOK.md`, then `corpora/god-tier-code/master-map.md`
Its own agent navigation file (for use *inside that corpus only*): `corpora/god-tier-code/AGENTS.md`
Its own adoptable persona (load it only for a session you explicitly want to work this way): `corpora/god-tier-code/PERSONA.md`

---

## Repo map

```
.
├── README.md                          ← you are here (human overview only)
├── LICENSE                            ← CC BY 4.0 for the distilled text/diagrams
├── docs/
│   └── combined-presentation.html     ← 16-slide overview of both corpora
│   └── combined-presentation.md
├── corpora/
│   ├── intelligence-atlas/            ← Corpus 1, self-contained
│   │   ├── AGENTS.md                  ← navigation for Corpus 1 only
│   │   ├── INDEX.md
│   │   ├── 00_master-atlas/
│   │   ├── 01_mathematical-foundations/
│   │   ├── 02_deep-learning-canon/
│   │   ├── 03_llm-architecture-training/
│   │   ├── 04_neuroscience-of-intelligence/
│   │   ├── 05_frontiers-new-intelligence/
│   │   ├── index/papers-master.json
│   │   ├── pdf/                       ← 6 volumes
│   │   ├── tools/
│   │   └── docs/                      ← Corpus 1 presentation
│   └── god-tier-code/                 ← Corpus 2, self-contained
│       ├── AGENTS.md                  ← navigation for Corpus 2 only
│       ├── PERSONA.md                 ← adoptable persona, Corpus 2 only
│       ├── PLAYBOOK.md
│       ├── master-map.md
│       ├── SOURCES.md
│       ├── BUILD_REPORT.md
│       ├── 01_codebase-anatomy/
│       ├── 02_structural-principles/
│       ├── 03_engineering-workflow/
│       ├── 04_data-pipelines/
│       └── 05_adaptive-systems/
```

## Isolation rules — read this before using either corpus

1. **No shared agent file.** There is no `AGENTS.md` at the repo root, on purpose. Each corpus's `AGENTS.md` applies only inside its own folder.
2. **No shared persona.** The god-tier-code `PERSONA.md` is not this repo's persona, and it is not any assistant's persona. Load it only for a session you explicitly want to work that way, then drop it.
3. **No cross-links between corpora.** Neither corpus links into the other (except this human README, which only points at folder names). Findings, rules, and numbering are per-corpus and append-only — never renumber either corpus to fit the other.
4. **No session material in this repo.** The GLM session transcript and raw session log that accompanied the god-tier-code export are *not* published here. They contain internal session details, not research, and publishing them would break isolation. The research corpus alone is public; the transcript stays private with its author.
5. **Compiled snapshots.** Both corpora are snapshots of October 2026. Upstream codebases (Chromium main, VS Code main) and the research frontier move daily; newer changes are not represented.

## How to use a corpus

- **Human:** read its own README first, then its playbook / reading order.
- **Agent, for one task:** point it at exactly one corpus folder and tell it to read that folder's `AGENTS.md` first. Do not point it at the repo root and expect it to choose — the root deliberately gives no agent instructions.
- **Extending a corpus:** follow that corpus's own conventions (numbered findings append-only, every new finding carries a source, diagrams ≤30 nodes, never hand-edit PDFs in the atlas). Rebuild its index with its own tools where it has them.

## Licence

The distilled text, findings, diagrams, and index data written for these corpora are licensed under **CC BY 4.0** (see `LICENSE`). You may share and adapt them with attribution to tirunara.

Original papers, code excerpts, figures, and trademarks remain the property of their respective authors and publishers; these corpora summarise, cite, and excerpt them to ground claims, they do not republish them.

---

*Compiled 2026-10-25. Two maps, kept separate on purpose: one for what intelligence is, one for how the best code is built. Use each where it belongs, verify against the cited sources before building on any single claim, and extend each corpus inside its own folder.*
