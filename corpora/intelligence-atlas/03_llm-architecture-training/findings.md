# LLM Architecture & Training — Distilled Findings

Paper references point to `papers.md` in this folder.

---

## F1 — The transformer won by parallelism, then by everything else

**Claim:** Attention displaced recurrence because it trains in parallel across sequence positions — and once scaled, attention's direct, length-1 information paths turned out to be what long reasoning needed.

**Evidence:** Vaswani et al. (2017) — 8-position parallelism era begins; Bahdanau (2014) attention as patch → core; LSTM's sequential bottleneck vs. TPU/GPU-friendly transformer; RoPE (2021) and FlashAttention (2022) resolved its positional and memory weaknesses.

**Why it matters:** Architecture choices are compute-ecology decisions: the winning architecture is the one that best converts available hardware into capability. Any new architecture (domain 05) must answer: what does it parallelize?

---

## F2 — Pretraining = capability; post-training = behavior

**Claim:** Nearly all knowledge and skill enters during self-supervised pretraining; alignment stages mainly select and format existing abilities.

**Evidence:** GPT-3 (2020) — in-context learning emerges from pretraining alone; LIMA (2023) — 1K examples suffice for chat behavior; R1-Zero (2025) shows RL *elicititing* (and sharpening) reasoning that pretraining made possible.

**Why it matters:** Budget accordingly: capability per dollar lives in pretraining data quality/quantity; behavior per dollar lives in post-training. Trying to teach facts via SFT is fighting the current.

---

## F3 — RLHF is a three-actor system with known failure modes

**Claim:** RLHF = preference data → reward model → policy optimization; each stage has characteristic pathologies, and the reward model is the single point of failure.

**Evidence:** Christiano et al. (2017) seeded it; InstructGPT (2022) operationalized it; reward hacking / over-optimization documented alongside; DPO (2023) removed the RM/PPO fragility for a direct loss; Constitutional AI (2022) replaced human labels with constitutions (RLAIF) for scalable, auditable supervision.

**Why it matters:** Whatever preference machinery you build, monitor reward-model drift, cap KL to the reference policy, and prefer direct/preference losses (DPO/GRPO-family) unless you need online exploration.

---

## F4 — Reasoning is trainable with verifiable rewards (RLVR) — the 2025 revolution

**Claim:** Reinforcement learning against checkable outcomes (math answers, code tests) — without human preference labels — elicits emergent reasoning: self-verification, backtracking, long coherent chains.

**Evidence:** DeepSeek-R1 (Nature 2025): pure-RL R1-Zero develops "aha" reflection moments; GRPO (2024) made this affordable; distillation transfers reasoning to small models; s1 (2025) shows mere budget-steering ("Wait…") on 1K examples recovers much of it.

**Why it matters:** The default path to strong reasoning systems in 2026: base model + RLVR + verifiable environments. The bottleneck moved from algorithms to ENVIRONMENT DESIGN (problem generators, verifiers, reward shaping against hacking).

---

## F5 — Test-time compute is a second scaling axis

**Claim:** Spending more compute at inference (more samples, longer chains, search, verification) buys capability at rates that can beat spending it on parameters.

**Evidence:** Self-consistency (2023) as naive version; Snell et al. (2024): optimized test-time search on a small model beats a 14× larger one; R1 allocates thinking depth by difficulty; s1's budget forcing as the minimalist control knob.

**Why it matters:** Product/system design now has a tunable capability dial (latency/cost ↔ quality). Compute-optimal INFERENCE planning (when to think long, when to answer directly) is a live engineering discipline.

---

## F6 — Reasoning models have real limits: collapse past a complexity frontier

**Claim:** Extended "thinking" degenerates on sufficiently complex problems — accuracy collapses, and effort itself declines near the frontier; much test-time behavior is pattern-matching dressed as search.

**Evidence:** Apple's Illusion of Thinking (2025): controlled-complexity puzzles show threshold collapse and "giving up" in token budgets; Dziri et al. (2023): transformers' native multi-step circuits compound error exponentially — chain-of-thought is a workaround that externalizes each step.

**Why it matters:** Do not assume reasoning models can handle arbitrary depth; decompose tasks, force tool use for exact steps (calculators, code), and evaluate on contamination-free procedural benchmarks (ARC-AGI class) before trusting scale narratives.

---

## F7 — In-context learning is a real mechanism (induction heads), not a trick

**Claim:** The ability to learn from examples IN THE PROMPT without weight updates is implemented by identifiable attention circuits that form during a sudden training-phase transition.

**Evidence:** Olsson et al. (2022): induction heads ([A][B] … [A] → [B]) appear via a sharp phase change and causally mediate ICL; grokking circuits (domain 01, F10) are the in-weights analogue.

**Why it matters:** ICL is the model's built-in learning algorithm — treat prompts as training data (order, format, and diversity matter statistically). Mechanistic knowledge lets you predict when ICL will fail (unfamiliar formats, conflicting patterns).

---

## F8 — Models store more concepts than they have neurons (superposition)

**Claim:** Networks represent many more features than dimensions using nearly-orthogonal directions; single neurons are polysemantic by necessity.

**Evidence:** Elhage et al. (2022) toy models: features in superposition, phase transitions in feature count; SAE dictionary learning (2023) recovers monosemantic features; millions of interpretable, steerable features extracted from production models (2024); 2025 circuit tracing observes computation flowing through them during live prompts.

**Why it matters:** Interpretability is now an engineering tool (steering, auditing, safety). Also the mechanistic root of scaling laws (domain 01) — capacity grows with interference-managed feature packing. If you build custom models, budget for feature-based monitoring.

---

## F9 — Emergence claims need smooth metrics and mechanism checks

**Claim:** Apparent capability cliffs are often metric artifacts; genuine internal phase changes exist but must be shown mechanistically.

**Evidence:** Wei et al. (2022) catalogued cliffs; Schaeffer et al. (2023) dissolved most under nonlinear metrics; induction-head phase change (F7) is the genuine counterpart.

**Why it matters:** For capability forecasting (and safety planning): demand log-likelihood curves + mechanism, not exact-match cliffs. For research: if you find a cliff, look for the circuit underneath it.

---

## F10 — Efficiency engineering is a first-class research area, not an afterthought

**Claim:** The frontier of capability-per-dollar moves as fast as the frontier of capability: sparsity, quantization, kernel design, and low-rank adaptation repeatedly deliver "free" multipliers.

**Evidence:** MoE (Shazeer 2017 → Switch → Mixtral → DeepSeek-V3: 671B params, 37B active); LoRA (2021); FlashAttention (2022) exact-but-IO-aware; FP8 training + Multi-head Latent Attention in V3 (2024) → frontier model for ~$5.6M.

**Why it matters:** Open ecosystems win through efficiency (LLaMA recipe, DeepSeek economics). A capable small team can compete by engineering multiplier stacking: sparse architecture × low precision × kernel fusion × test-time compute allocation.

---

## F11 — Knowledge lives badly in weights — retrieval separates knowing from storing

**Claim:** Parametric knowledge is stale, unattributable, and expensive to update; retrieval-augmented generation moves knowledge to an external index with better properties on all three axes.

**Evidence:** RAG (Lewis et al. 2020) matched fine-tuned knowledge tasks with a frozen model + index; hallucination-reduction and provenance become product requirements; long-context (RoPE-scaling) and RAG converge — context-as-cache vs. index-as-memory.

**Why it matters:** Architect systems as: weights = reasoning engine, external stores = facts, tools = exactness. This is also how agent memory systems (domain 05) are built in practice.

---

## F12 — The evaluation crisis is the meta-problem of 2025–2026

**Claim:** Benchmark saturation + data contamination + metric artifacts mean headline numbers no longer proxy capability; the field's rate-limiting problem is measurement.

**Evidence:** "Advances and Open Problems" survey (2025) across 27 models; Apple (2025) procedural puzzles; ARC-AGI's persistence as the "unsaturated" holdout; contamination analyses behind every benchmark.

**Why it matters:** When selecting or training models, weight contamination-resistant, procedurally-generated evaluations over leaderboards; build private evals reflecting your deployment distribution. Trust curves (smooth metrics over scale), not single numbers.
