# Mathematical Foundations — Distilled Findings

Each finding: **Claim → Evidence → Why it matters for building intelligence**. Paper IDs refer to `papers.md` in this folder.

---

## F1 — Understanding IS compression

**Claim:** Learning, in brains and machines, is fundamentally the discovery of short descriptions of the world. Prediction quality is bounded by how well you compress.

**Evidence:** Shannon (1948) made "information" measurable; Kolmogorov (1965) and Solomonoff (1964) tied prediction to shortest programs; Rissanen's MDL (1978) made it a model-selection criterion; Tishby's information bottleneck (1999) made it a representation-learning objective. Modern LLM training minimizes cross-entropy — literally an expected code length under the model.

**Why it matters:** Every loss curve is a compression curve. Evaluating models in bits-per-character, framing pretraining as compression, and data-filtering-as-den oising all fall out of this view. If you build intelligence, you are building a compressor whether you admit it or not.

---

## F2 — No learning without inductive bias

**Claim:** Generalization is impossible from data alone; it comes from structural assumptions baked into the learner that happen to match the world.

**Evidence:** Wolpert's No Free Lunch (1996) proves averaged over all worlds no learner wins; VC theory (1971) quantifies how capacity and sample size interact; CNNs (weight sharing), equivariant nets (Cohen & Welling 2016), and transformers (sequence bias, positional structure) succeed because their priors match natural data's symmetries.

**Why it matters:** Architecture choice = hypothesis about the world. When designing a system, decide which biases you encode (locality? translation? causal order?) — that decision dominates data volume.

---

## F3 — Universality is cheap; depth is exponential

**Claim:** A single wide layer can represent anything, but deep compositional functions need exponentially more width if you forbid depth.

**Evidence:** Universal approximation (Hornik et al. 1989) guarantees sufficiency of one hidden layer; Poole et al. (2016) / Raghu et al. (2017) show depth buys exponential expressivity for compositional structure; empirical loss-landscape work (Li et al. 2018) adds the optimization side — deep networks are only trainable when geometry cooperates (residual connections).

**Why it matters:** Hierarchy is not a fashion — it is a complexity-theoretic necessity for compositional worlds (language, vision, planning). Shallow-but-wide is a losing strategy.

---

## F4 — Overparameterization helps, and classical theory was wrong about it

**Claim:** Models far past the interpolation threshold (able to memorize everything) generalize better, not worse.

**Evidence:** Zhang et al. (2017) showed deep nets perfectly fit random labels — capacity cannot be the whole story; Belkin et al. (2019) and Nakkiran et al. (2019) mapped double descent; implicit regularization of SGD selects "simple" functions among the infinitely many that fit.

**Why it matters:** Justifies training enormous models on modest data; warns that the interpolation-peak region (model size just barely fits data) is a danger zone. Also underlies why grokking (F10) exists.

---

## F5 — Two training regimes: lazy (kernel) vs rich (feature learning)

**Claim:** Gradient descent can behave as kernel regression (features barely move) or as true feature learning; only the latter produces the deep-learning magic.

**Evidence:** Jacot et al. (2018) derived the Neural Tangent Kernel — infinite-width training becomes exact kernel regression; Chizat & Bach (2019) named lazy vs rich regimes and showed initialization scale controls which you are in; Lyu et al. (2024) connected grokking to escaping the lazy regime.

**Why it matters:** If you over-initialize or over-regularize toward stability, you get a kernel machine — smooth but no feature discovery. Feature learning requires living with richer, riskier dynamics.

---

## F6 — Good representations sit at an information bottleneck

**Claim:** Learning good features means throwing away almost everything about the input while preserving what predicts (and can act on) the future.

**Evidence:** Tishby et al. (1999) formalized optimal compression-relevance tradeoffs; Shwartz-Ziv & Tishby (2017) claimed fit-then-compress phases; Saxe et al. (2018) rebutted the universality of those phases (ReLU nets compress little); neural collapse (Papyan et al. 2020) and 2025 work unifying collapse with the IB give the idea firmer geometric footing.

**Why it matters:** Use IB as a design principle (auxiliary compression losses, VIB, representation regularization) — not as settled law. The debate itself (2017–2018) is a masterclass in how theory should interact with empirics.

---

## F7 — The loss landscape is non-convex but geometrically benign (with the right architecture)

**Claim:** High-dimensional training landscapes are riddled with saddle points but contain connected, flat, low-loss valleys — SGD navigates them fine if skip connections keep geometry tame.

**Evidence:** Li et al. (2018) visualized landscapes: chaotic without residuals, convex-looking valleys with them; mode-connectivity results show minima are connected by low-loss paths; NTK theory (2018) shows the infinite-width landscape is effectively quadratic.

**Why it matters:** Residual streams (ResNet → transformer) are why 100+ layer stacks train at all. If your novel architecture lacks identity-path geometry, expect optimization pain regardless of expressivity.

---

## F8 — Scaling follows smooth power laws (until data binds)

**Claim:** Loss falls as a power of parameters × data × compute, predictable across 6+ orders of magnitude; the sweet spot equalizes parameter and token scaling (~20 tokens/param).

**Evidence:** Kaplan et al. (2020) established the power laws; Hoffmann et al. (2022, Chinchilla) corrected the token/parameter balance and outperformed GPT-3 with 4× fewer parameters; Muennighoff et al. (2023) showed data repetition collapses returns past ~4 epochs; 2025–2026 work derives scaling laws mechanistically from superposition and pushes toward a full limit theory of foundation models.

**Why it matters:** Pretraining economics is now an engineering optimization problem. Compute-optimal recipes (Chinchilla) governed 2022–2024; the frontier questions are data quality/quantity (unique tokens running out) and post-training scaling (domain 03, F7/F8).

---

## F9 — Emergence: thresholds, or an artifact of the yardstick?

**Claim:** Some abilities (multi-step arithmetic, instruction following) appear sharply above a scale threshold — but many "emergent" jumps dissolve under smooth metrics.

**Evidence:** Wei et al. (2022) catalogued emergent abilities across benchmarks; Schaeffer et al. (2023) showed discontinuous metrics (exact-match) manufacture cliffs that accuracy/log-likelihood show as smooth; mechanistic work (induction heads, domain 03) shows genuine internal phase changes can also occur.

**Why it matters:** Two lessons: (1) measure with smooth metrics or you will hallucinate capability jumps; (2) real internal phase transitions do happen — monitor mechanisms, not just benchmarks, before promising capabilities at scale N.

---

## F10 — Grokking: networks memorize first, understand later — and you can engineer which one you get

**Claim:** Trained past overfitting, networks can snap from memorization to exact, generalizing algorithms; the transition is driven by weight-norm scale and circuit formation, and per 2025 results also by train/test distribution shift.

**Evidence:** Power et al. (2022) discovered it; Liu et al. (Omnigrok, 2023) showed weight-norm control (weight decay accelerates generalization); Nanda et al. (2023) reverse-engineered the full transition — memorizing lookup → Fourier-based modular-arithmetic circuit; Lyu et al. (2024) tied it to lazy→rich escape; 2025 papers reframe it statistically (distribution shift) and document grokking in 7B pretraining (OLMoE).

**Why it matters**: Weight decay and long training are generalization instruments, not afterthoughts. If a small model "refuses" to generalize, the fix may be more training time + stronger norm control + data distribution coverage — not more parameters.

---

## F11 — The same mathematical patterns recur in nature, brains, and neural networks

**Claim:** Power laws, scale-free topology, criticality, symmetry, and renormalization-style multi-scale structure are universals across physical, biological, and artificial learning systems.

**Evidence:** Watts–Strogatz (1998) small-world and Barabási–Albert (1999) scale-free networks describe cortex connectivity AND language graphs (Zipf); Bak et al. (1987) self-organized criticality anticipates neuronal avalanches (Beggs & Plenz 2003, domain 04); Mehta & Schwab (2014) map deep stacks to the renormalization group; Kaplan (2020) adds learning-curve power laws; Cohen & Welling (2016) show symmetry priors transfer from physics to learning.

**Why it matters:** When choosing priors for a new architecture, steal from the patterns nature already converged on: heavy-tailed distributions, multi-scale abstraction, sparse codes, near-critical dynamics. These are the universe's default settings for complex systems.

---

## F12 — Learning has phase transitions (statistical mechanics of intelligence)

**Claim:** Training exhibits thermodynamics-like phenomena — capacity thresholds, sharp transitions, avalanches — suggesting learning is a physical process in a statistical-mechanical sense.

**Evidence:** Gardner (1988) computed capacity volumes of perceptron space; Hopfield (1982) networks have sharp storage capacity (n ≈ 0.14·#units); grokking and emergence are modern transition instances; 2025 physics-inspired "glass relaxation" theory of grokking.

**Why it matters:** Expect discontinuities when scaling ANY learning system — smooth averages hide sharp per-run transitions. Budget experiments around thresholds (capacity, data coverage, initialization scale).

---

## F13 — Intelligence has formal definitions — use them as design targets

**Claim:** Beyond benchmarks, intelligence can be defined mathematically, and the definitions expose what current systems lack.

**Evidence:** Legg & Hutter (2007): intelligence = goal-achieving ability across all computable environments (Solomonoff-weighted) — maximally general, uncomputable; Chollet (2019): intelligence = skill-acquisition efficiency over novel problems given priors/experience — measurable (ARC), and LLMs score far below humans until 2024–2025 hybrid systems (domain 05).

**Why it matters:** If you optimize skill (benchmarks), you get skill, not intelligence. Decide explicitly which definition your system targets; design for sample efficiency and transfer if you target Chollet-intelligence.

---

## F14 — Energy-based views unify memory, learning, and inference

**Claim:** Framing learning as minimizing an energy function unifies Hopfield memory, Boltzmann machines, predictive coding, and (via variational free energy) Bayesian brains — and energy views are returning in modern architectures.

**Evidence:** Hopfield (1982) content-addressable memory as energy minima; Ackley/Hinton/Sejnowski (1985) learning by contrasting data/model energies; Friston's free-energy principle generalizes to perception-action loops (domain 04); modern associative-memory transformers explicitly reuse Hopfield dynamics (domain 05).

**Why it matters:** If you are designing new intelligence substrate, energy-based formulation gives you memory + inference + learning under one objective — a path around backprop's biological implausibility (domain 04, F6).
