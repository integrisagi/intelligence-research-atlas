# INDEX — Intelligence Research Atlas

Master index of the corpus. Compiled **2026-10-25**. Coverage: **184 papers, 1936–2026**.
Machine-readable version: [`index/papers-master.json`](index/papers-master.json) (also per-domain `papers.json`).

## Domains at a glance

| # | Domain | Folder | Papers | Findings | PDF volume |
|---|--------|--------|--------|----------|------------|
| 00 | Overview & corpus maps | `00_master-atlas/` | — | 5 connections, 5 reading paths | [00-overview.pdf](pdf/00-overview.pdf) |
| 01 | Mathematical foundations | `01_mathematical-foundations/` | 47 | F1–F14 | [01-mathematical-foundations.pdf](pdf/01-mathematical-foundations.pdf) |
| 02 | Deep learning canon (1943–2017) | `02_deep-learning-canon/` | 27 | F1–F10 | [02-deep-learning-canon.pdf](pdf/02-deep-learning-canon.pdf) |
| 03 | LLM architecture & training (2017–2026) | `03_llm-architecture-training/` | 38 | F1–F12 | [03-llm-architecture-training.pdf](pdf/03-llm-architecture-training.pdf) |
| 04 | Neuroscience of intelligence | `04_neuroscience-of-intelligence/` | 26 | F1–F14 | [04-neuroscience-of-intelligence.pdf](pdf/04-neuroscience-of-intelligence.pdf) |
| 05 | Frontiers: new intelligence | `05_frontiers-new-intelligence/` | 46 | F1–F13 | [05-frontiers-new-intelligence.pdf](pdf/05-frontiers-new-intelligence.pdf) |

## Findings index (one line each)

**01 Mathematical foundations** — F1 understanding is compression · F2 no learning without inductive bias · F3 depth is exponentially efficient · F4 overparameterization helps (double descent) · F5 lazy vs rich regimes · F6 information bottleneck as design principle · F7 benign loss-landscape geometry via residuals · F8 scaling power laws & the data wall · F9 emergence vs metric mirage · F10 grokking engineering (weight decay, circuits, distribution shift) · F11 recurring patterns (power laws, criticality, symmetry, renormalization) · F12 learning has phase transitions · F13 formal definitions of intelligence (AIXI, Legg-Hutter, Chollet) · F14 energy-based unification.

**02 Deep learning canon** — F1 invention/winter/revival cycle · F2 architecture = crystallized inductive bias · F3 depth needs gates+norm+identity paths · F4 prediction-trained vectors contain semantics · F5 self-supervision unlocked all data · F6 adversarial objectives are unstable teachers · F7 deep RL runs on brain's tricks (replay, targets) · F8 search + learned evaluation beats either alone · F9 generative paradigm arc (VAE→GAN→diffusion) · F10 the 2012 conjunction (algorithm×data×compute).

**03 LLM architecture & training** — F1 transformer won by parallelism · F2 pretraining=capability, post-training=behavior · F3 RLHF failure modes & alternatives (DPO/GRPO) · F4 reasoning trainable by RLVR (R1) · F5 test-time compute = second scaling axis · F6 reasoning collapses past complexity frontiers · F7 in-context learning is induction-head circuits · F8 superposition: more concepts than neurons · F9 emergence claims need smooth metrics · F10 efficiency engineering (MoE/LoRA/FlashAttention/FP8) · F11 RAG separates knowing from storing · F12 evaluation crisis.

**04 Neuroscience** — F1 Hebbian local learning builds global structure · F2 dopamine IS the TD error · F3 brain = prediction machine (predictive coding) · F4 sparse high-dimensional coding twice over · F5 hippocampus = structured memory (maps, grid cells, prioritized replay) · F6 sleep = consolidation by renormalization · F7 global workspace (bottleneck+broadcast) · F8 brains at criticality · F9 small-world topology · F10 backprop alternatives (feedback alignment, dendrites, PC) · F11 neuromodulation = global state control · F12 representational geometry as shared language · F13 Marr's levels · F14 the two-way neuro↔AI street.

**05 Frontiers** — F1 world models: plan in imagination · F2 active inference unifies goal+curiosity · F3 attention = associative memory (Hopfield returns) · F4 post-transformer zoo = bias portfolio · F5 diffusion LMs break serial generation · F6 biological substrates = intelligence per watt · F7 neuro-symbolic owns compositionality · F8 novelty search beats deceptive objectives · F9 collective intelligence & protocols · F10 the settled 2026 agent stack · F11 self-improvement loops & their risks · F12 scalable oversight is measurable · F13 generality measurable via ARC — still unsolved.

## Diagram index

| Diagram | Location |
|---|---|
| Master mindmap (whole corpus) | [00_master-atlas/master-mindmap.md](00_master-atlas/master-mindmap.md) |
| Timeline 1943–2026 | [00_master-atlas/timeline.md](00_master-atlas/timeline.md) |
| Cross-domain concept map | [00_master-atlas/cross-domain-map.md](00_master-atlas/cross-domain-map.md) |
| Reading paths | [00_master-atlas/reading-order.md](00_master-atlas/reading-order.md) |
| Information theory → AI | [01/diagrams/information-to-intelligence.mmd.md](01_mathematical-foundations/diagrams/information-to-intelligence.mmd.md) |
| Scaling / emergence / grokking | [01/diagrams/scaling-emergence-grokking.mmd.md](01_mathematical-foundations/diagrams/scaling-emergence-grokking.mmd.md) |
| Architecture evolution 1943→2017 | [02/diagrams/architecture-evolution.mmd.md](02_deep-learning-canon/diagrams/architecture-evolution.mmd.md) |
| LLM training pipeline | [03/diagrams/llm-pipeline.mmd.md](03_llm-architecture-training/diagrams/llm-pipeline.mmd.md) |
| Reasoning & test-time compute taxonomy | [03/diagrams/reasoning-taxonomy.mmd.md](03_llm-architecture-training/diagrams/reasoning-taxonomy.mmd.md) |
| Neuroscience → AI bridge | [04/diagrams/neuro-ai-bridge.mmd.md](04_neuroscience-of-intelligence/diagrams/neuro-ai-bridge.mmd.md) |
| Predictive processing loop | [04/diagrams/predictive-processing-loop.mmd.md](04_neuroscience-of-intelligence/diagrams/predictive-processing-loop.mmd.md) |
| Paradigm landscape (beyond LLMs) | [05/diagrams/paradigm-map.mmd.md](05_frontiers-new-intelligence/diagrams/paradigm-map.mmd.md) |
| The 2026 agent stack | [05/diagrams/agent-stack.mmd.md](05_frontiers-new-intelligence/diagrams/agent-stack.mmd.md) |

## Maintenance

- Rebuild paper index after editing any `papers.md`: `python3 tools/build_index.py`
- Regenerate PDFs after content edits: `python3 tools/build_pdfs.py`
- Conventions for adding papers/findings: see [AGENTS.md](AGENTS.md)
