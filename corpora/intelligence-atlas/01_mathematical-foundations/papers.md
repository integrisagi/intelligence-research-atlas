# Mathematical Foundations of Intelligence — The Canon

Papers that establish *why* learning works, *what* intelligence is formally, and *which* mathematical patterns recur across nature, brains, and neural networks. Cross-domain papers (Hopfield, Friston) also appear in domain 04 with neuroscience context.

---

### [1936] On Computable Numbers, with an Application to the Entscheidungsproblem — Alan Turing
- **Link**: https://doi.org/10.1112/plms/s2-42.1.230
- **Core idea**: Defines the Turing machine — the minimal formal model of computation — and proves some problems are undecidable.
- **Why it matters**: Establishes the ceiling of what any intelligence, biological or artificial, can compute; every result below inherits this frame.
- **Keywords**: computability, turing-machine, foundations

### [1943] A Logical Calculus of the Ideas Immanent in Nervous Activity — Warren McCulloch, Walter Pitts
- **Link**: https://doi.org/10.1007/BF02478259
- **Core idea**: Neurons as threshold logic units; networks of them compute any logical proposition.
- **Why it matters**: First proof that neural substrate ⇒ computation; the founding bridge between brain and mathematics.
- **Keywords**: mcculloch-pitts, threshold-logic, neuro-ai-bridge

### [1948] A Mathematical Theory of Communication — Claude Shannon
- **Link**: https://doi.org/10.1002/j.1538-7305.1948.tb01338.x
- **Core idea**: Information = reduction of uncertainty (entropy); source coding and channel coding theorems; the bit.
- **Why it matters**: The vocabulary of every loss function (cross-entropy = Shannon information) and of compression-as-understanding. The single most-used equation in LLM training.
- **Keywords**: information-theory, entropy, compression

### [1964] A Formal Theory of Inductive Inference — Ray Solomonoff
- **Link**: https://doi.org/10.1016/S0019-9958(64)90231-7
- **Core idea**: Predict the future by Bayesian mixture over all computable hypotheses, weighted by 2^(−description length) (algorithmic probability).
- **Why it matters**: The mathematically ideal — though uncomputable — learner; modern sequence models are its practical approximation.
- **Keywords**: solomonoff-induction, algorithmic-probability, prediction

### [1965] Three Approaches to the Quantitative Definition of Information — Andrey Kolmogorov
- **Link**: https://doi.org/10.1109/TIT.1965.1053769
- **Core idea**: Kolmogorov complexity: the length of the shortest program that outputs an object.
- **Why it matters**: "Understanding = compression" made precise; ties Occam's razor to computability.
- **Keywords**: kolmogorov-complexity, compression, occam

### [1978] Modeling by Shortest Data Description — Jorma Rissanen
- **Link**: https://doi.org/10.1016/0005-1098(78)90005-5
- **Core idea**: Minimum Description Length (MDL): prefer the model that compresses the data plus model code best.
- **Why it matters**: Practical model-selection principle uniting compression and generalization; ancestor of bits-per-byte evals.
- **Keywords**: mdl, model-selection, compression

### [1971] On the Uniform Convergence of Relative Frequencies to Probabilities (VC theory) — Vladimir Vapnik, Alexey Chervonenkis
- **Link**: https://doi.org/10.1137/S0040585X97975476 (theory overview)
- **Core idea**: Generalization is controlled by the capacity (VC dimension) of the hypothesis class, not just sample count.
- **Why it matters**: Classical generalization theory — and the benchmark modern deep learning spectacularly violated (see Zhang 2017), forcing new theory.
- **Keywords**: vc-dimension, generalization-theory, capacity

### [1982] Simplified Neuron Model as a Principal Component Analyzer — Erkki Oja
- **Link**: https://doi.org/10.1007/BF00275687
- **Core idea**: A single neuron with Hebbian plasticity plus normalization converges to the first principal component of its input.
- **Why it matters**: Local, biologically plausible rules can compute global statistics — dimensionality reduction for free.
- **Keywords**: pca, hebbian, unsupervised

### [1982] Neural Networks and Physical Systems with Emergent Collective Computational Abilities — John Hopfield
- **Link**: https://doi.org/10.1126/science.186.4566.4595
- **Core idea**: Recurrent binary networks as energy minima = content-addressable memory; physics (spin glasses) applied to neural systems.
- **Why it matters**: Founded the statistical-mechanics view of neural networks; modern "attention as associative memory" results trace here (Nobel Prize 2024, shared with Hinton).
- **Keywords**: hopfield, energy-based, associative-memory, statistical-mechanics

### [1984] A Theory of the Learnable — Leslie Valiant
- **Link**: https://doi.org/10.1145/1968.1972
- **Core idea**: PAC learning: learnable = efficiently learnable to arbitrary accuracy with high probability.
- **Why it matters**: Put learning itself on computational footing — learning has complexity classes like computation does.
- **Keywords**: pac-learning, learnability, complexity

### [1985] A Learning Algorithm for Boltzmann Machines — David Ackley, Geoffrey Hinton, Terrence Sejnowski
- **Link**: https://doi.org/10.1016/0005-1098(85)90020-5
- **Core idea**: Stochastic energy-based networks trained by contrasting data and model statistics.
- **Why it matters**: First usable learning rule for hidden-unit networks; ancestor of contrastive divergence, wake-sleep, and modern self-supervised losses.
- **Keywords**: boltzmann-machine, energy-based, unsupervised

### [1986] Learning Representations by Back-Propagating Errors — David Rumelhart, Geoffrey Hinton, Ronald Williams
- **Link**: https://www.nature.com/articles/323533a0
- **Core idea**: Compute gradients of error through layers via the chain rule, making internal representations trainable.
- **Why it matters**: The learning algorithm of the entire deep learning era; still how every LLM trains.
- **Keywords**: backpropagation, gradient-descent, representations

### [1988] The Space of Interactions in Neural Network Models (statistical mechanics of learning) — Elizabeth Gardner
- **Link**: https://doi.org/10.1088/0305-4470/21/1/030
- **Core idea**: Compute the volume of parameter space consistent with a training set — capacity thresholds and phase transitions in learning.
- **Why it matters**: Learning has thermodynamic phase transitions; this lens predicts grokking-like phenomena decades early.
- **Keywords**: statistical-mechanics, capacity, phase-transitions

### [1989] Multilayer Feedforward Networks Are Universal Approximators — Kurt Hornik, Maxwell Stinchcombe, Halbert White
- **Link**: https://doi.org/10.1016/0893-6080(89)90020-8
- **Core idea**: One hidden layer with enough units approximates any continuous function (independently: Cybenko 1989).
- **Why it matters**: Guarantees representational sufficiency — but says nothing about depth efficiency or learnability (see Poole 2017).
- **Keywords**: universal-approximation, expressivity

### [1995] An Information-Maximization Approach to Blind Separation and Blind Deconvolution — Anthony Bell, Terrence Sejnowski
- **Link**: https://doi.org/10.1162/neco.1995.7.6.1129
- **Core idea**: Maximize output entropy (InfoMax) and the network discovers independent sources — without labels.
- **Why it matters**: Information-theoretic self-supervision works; direct ancestor of contrastive and predictive self-supervised learning.
- **Keywords**: infomax, ica, self-supervised

### [1996] The Lack of A Priori Distinctions Between Learning Algorithms (No Free Lunch) — David Wolpert
- **Link**: https://doi.org/10.1162/neco.1996.8.7.1341
- **Core idea**: Averaged over all possible problems, no learner beats random guessing.
- **Why it matters**: Generalization must come from inductive bias matched to the world's structure — explains why architecture and priors matter.
- **Keywords**: no-free-lunch, inductive-bias

### [1998] Collective Dynamics of 'Small-World' Networks — Duncan Watts, Steven Strogatz
- **Link**: https://doi.org/10.1038/30918
- **Core idea**: Networks interpolating regular/random achieve high clustering with short path lengths (small-world).
- **Why it matters**: The architecture of brains, and increasingly of ML systems (MoE routing, agent swarms); a recurring mathematical pattern.
- **Keywords**: network-science, small-world, mathematical-patterns

### [1999] Emergence of Scaling in Random Networks — Albert-László Barabási, Réka Albert
- **Link**: https://doi.org/10.1126/science.286.5439.509
- **Core idea**: Growth + preferential attachment produces power-law degree distributions (scale-free networks).
- **Why it matters**: Power laws appear in language (Zipf), brains, and model scaling — one generating mechanism, many systems.
- **Keywords**: scale-free, power-laws, network-science

### [1987] Self-Organized Criticality: An Explanation of 1/f Noise — Per Bak, Chao Tang, Kurt Wiesenfeld
- **Link**: https://doi.org/10.1103/PhysRevLett.58.381
- **Core idea**: Driven dissipative systems self-tune to a critical point between order and chaos, producing scale-invariant avalanches.
- **Why it matters**: Candidate explanation for brain criticality (domain 04) and for why edge-of-chaos dynamics keep recurring in learning systems.
- **Keywords**: criticality, self-organization, power-laws

### [1999] The Information Bottleneck Method — Naftali Tishby, Fernando Pereira, William Bialek
- **Link**: https://doi.org/10.1109/ISIT.1999.770759
- **Core idea**: Optimal representations maximally compress X about irrelevant detail while preserving information about relevance variable Y; formally rate-distortion with a relevance constraint.
- **Why it matters**: The leading formal account of what a "good representation" is; frames deep learning as progressive information compression.
- **Keywords**: information-bottleneck, representations, rate-distortion

### [2014] An Exact Mapping Between the Variational Renormalization Group and Deep Learning — Pankaj Mehta, David Schwab
- **Link**: https://arxiv.org/abs/1410.3831
- **Core idea**: Stacked restricted Boltzmann machines perform the variational renormalization group exactly.
- **Why it matters**: Physics' tool for scale-dependent structure (RG) ≈ deep learning's stacked abstraction; concrete support for "deep = multi-scale".
- **Keywords**: renormalization, physics, multiscale, mathematical-patterns

### [2015] Deep Learning and the Information Bottleneck Principle — Naftali Tishby, Noga Zaslavsky
- **Link**: https://arxiv.org/abs/1503.02406
- **Core idea**: Deep networks should first fit (memorize) then compress representations — phases observed via mutual-information probes.
- **Why it matters**: Predicted a two-phase training dynamic later echoing in grokking (F10).
- **Keywords**: information-bottleneck, compression-phase

### [2016] Group Equivariant Convolutional Networks — Taco Cohen, Max Welling
- **Link**: https://arxiv.org/abs/1602.07576
- **Core idea**: Build symmetry (translation, rotation equivariance) into architecture rather than learning it from data.
- **Why it matters**: Symmetry is the strongest inductive bias physics knows; equivariant nets show architectural priors can replace data volume.
- **Keywords**: symmetry, equivariance, inductive-bias

### [2016] Exponential Expressivity in Deep Neural Networks through Transient Chaos — Ben Poole, Surya Ganguli, Maithra Raghu (with "On the Expressivity of Deep Neural Networks", Raghu et al. 2017)
- **Link**: https://arxiv.org/abs/1606.05340 (NeurIPS 2016); companion: https://arxiv.org/abs/1611.08087
- **Core idea**: Depth yields exponential gains in expressivity for representing compositional functions, beyond what width can buy.
- **Why it matters**: Why we stack layers instead of widening flat ones; why hierarchies (brains included) are deep.
- **Keywords**: expressivity, depth, compositionality

### [2017] Understanding Deep Learning Requires Rethinking Generalization — Chiyuan Zhang, Samy Bengio, Moritz Hardt, Benjamin Recht, Oriol Vinyals
- **Link**: https://arxiv.org/abs/1611.03530
- **Core idea**: Deep nets can fit random labels perfectly, so generalization cannot follow from classical capacity control alone.
- **Why it matters**: Broke VC-style theory of deep learning; opened implicit-regularization and double-descent research lines.
- **Keywords**: generalization, implicit-regularization, overparameterization

### [2017] Opening the Black Box of Deep Neural Networks via Information — Ravid Shwartz-Ziv, Naftali Tishby
- **Link**: https://arxiv.org/abs/1703.00810
- **Core idea**: Empirically observes the fit-then-compress information phases during SGD training.
- **Why it matters**: Made information-plane analysis famous — and triggered the field's sharpest theory debate.
- **Keywords**: information-bottleneck, empirical

### [2018] On the Information Bottleneck Theory of Deep Learning — Andrew Saxe et al.
- **Link**: https://arxiv.org/abs/1801.04540 (ICLR 2018)
- **Core idea**: Compression phases largely vanish with ReLU/unbounded activations and realistic datasets; IB theory is not the mechanism.
- **Why it matters**: The decisive rebuttal — science working; the field now treats IB as a design principle, not a law.
- **Keywords**: information-bottleneck, critique

### [2018] Neural Tangent Kernel: Convergence and Generalization in Neural Networks — Arthur Jacot, Franck Gabriel, Clément Hongler
- **Link**: https://arxiv.org/abs/1806.07572
- **Core idea**: In the infinite-width limit, training a network equals kernel regression with a fixed kernel (NTK).
- **Why it matters**: Makes one training regime exactly solvable — and marks its boundary: NTK-lazy networks do NOT learn features.
- **Keywords**: ntk, kernel-regime, theory

### [2019] On Lazy Training in Differentiable Programming — Lénaïc Chizat, Edouard Oyallon, Francis Bach
- **Link**: https://arxiv.org/abs/1906.11248
- **Core idea**: Two regimes: lazy (kernel-like, features fixed) vs rich (feature learning); initialization scale selects the regime.
- **Why it matters**: Feature learning — the rich regime — is what makes deep learning work; connects to grokking transitions.
- **Keywords**: lazy-vs-rich, feature-learning

### [2019] Reconciling Modern Machine-Learning Practice and the Classical Bias–Variance Trade-Off — Mikhail Belkin, Daniel Hsu, Siyuan Ma, Soumik Mandal
- **Link**: https://doi.org/10.1073/pnas.1803071116
- **Core idea**: Double descent: test error descends, peaks at the interpolation threshold, then descends again as overparameterization grows.
- **Why it matters**: The modern generalization curve; explains why billion-parameter models on "small" data behave well.
- **Keywords**: double-descent, overparameterization, generalization

### [2019] Deep Double Descent: Where Bigger Models and More Data Hurt — Preetum Nakkiran et al.
- **Link**: https://arxiv.org/abs/1912.02292
- **Core idea**: Double descent is ubiquitous across model size, data size, and training time in modern deep learning.
- **Why it matters**: Practical warning: more parameters/data can hurt before they help; scale results have regime boundaries.
- **Keywords**: double-descent, empirical

### [2018] Visualizing the Loss Landscape of Neural Nets — Hao Li, Zheng Xu, Gavin Taylor, Christoph Studer, Tom Goldstein
- **Link**: https://arxiv.org/abs/1712.09913 (NeurIPS 2018)
- **Core idea**: Filter-normalized visualization shows residual nets have trainable convex-ish valleys; without skip connections landscapes are chaotic.
- **Why it matters**: Explains why residual connections (ResNet, transformer) made depth trainable — geometry, not just gradients.
- **Keywords**: loss-landscape, optimization, residuals

### [2020] Neural Collapse: An Analysis of the Modes of Neural Network Classifiers — Vardan Papyan, X. Y. Han, David Donoho
- **Link**: https://doi.org/10.1073/pnas.2015509117
- **Core idea**: At training's end, last-layer features collapse to class means arranged as a simplex ETF — a sharp geometric universal.
- **Why it matters**: 2025 work unifies grokking and information bottleneck via neural collapse; a concrete geometry of "converged" learning.
- **Keywords**: neural-collapse, geometry, classifiers

### [2020] Scaling Laws for Neural Language Models — Jared Kaplan et al. (OpenAI)
- **Link**: https://arxiv.org/abs/2001.08361
- **Core idea**: Loss follows smooth power laws in parameters, data, and compute, across 6+ orders of magnitude.
- **Why it matters**: Made scaling a predictive engineering discipline: you can read next year's loss off this year's curves.
- **Keywords**: scaling-laws, power-laws, llm

### [2022] Training Compute-Optimal Large Language Models (Chinchilla) — Jordan Hoffmann et al. (DeepMind)
- **Link**: https://arxiv.org/abs/2203.15556
- **Core idea**: For fixed compute, parameters and tokens should scale equally (~20 tokens/parameter) — most 2021-era models were badly undertrained.
- **Why it matters**: The recipe behind every efficient model since (LLaMA etc.); GPT-3-sized results from 4× smaller models.
- **Keywords**: chinchilla, scaling-laws, compute-optimal

### [2022] Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets — Alethea Power et al.
- **Link**: https://arxiv.org/abs/2201.02177
- **Core idea**: Networks memorize quickly but suddenly generalize long after overfitting, when trained past the point of zero training loss.
- **Why it matters**: Separates memorization from understanding in time; a lab model of "aha moment" learning.
- **Keywords**: grokking, generalization, phase-transition

### [2022] Towards Understanding Grokking: An Effective Theory of Representation Learning — Ziming Liu, Ouail Kitouni, Mike Nolte, Eric Michaud, Max Tegmark, Mike Williams
- **Link**: https://arxiv.org/abs/2205.10343 (NeurIPS 2022)
- **Core idea**: Grokking = delayed generalization explained by a effective-theory of representation learning dynamics.
- **Why it matters**: First mechanistic theory; predicts when grokking happens from dataset properties.
- **Keywords**: grokking, theory

### [2023] Omnigrok: Grokking Beyond Algorithmic Data — Ziming Liu, Eric Michaud, Max Tegmark
- **Link**: https://arxiv.org/abs/2210.01117 (ICLR 2023)
- **Core idea**: Grokking occurs on image datasets too; driven by weight-norm scale — "LU mechanism": memorize large-norm, generalize small-norm.
- **Why it matters**: Grokking is general, and controllable via weight decay — a knob for generalization.
- **Keywords**: grokking, weight-decay

### [2023] Progress Measures for Grokking via Mechanistic Interpretability — Neel Nanda, Lawrence Chan, Tom Lieberum, Jess Smith, Jacob Steinhardt
- **Link**: https://arxiv.org/abs/2305.01677 (ICLR 2024)
- **Core idea**: Reverse-engineers a grokking network: it transitions from memorization to a generalizing Fourier/multiplication circuit; restricted-set "pre-grokking" progress measures predict the transition.
- **Why it matters**: The cleanest causal story of emergent generalization inside a network; mechanistic interpretability's flagship result.
- **Keywords**: grokking, mechanistic-interpretability, circuits

### [2024] Grokking as the Transition from Lazy to Rich Training Dynamics — Kaifeng Lyu, Zhiyuan Li, et al. (ICLR 2024)
- **Link**: https://arxiv.org/abs/2310.06110
- **Core idea**: Networks grok when they escape the lazy kernel regime into rich feature learning late in training.
- **Why it matters**: Unifies grokking with the NTK/lazy-rich framework — one theory for both phenomena.
- **Keywords**: grokking, lazy-vs-rich, theory

### [2025] Grokking Explained: A Statistical Phenomenon — (authors: see paper)
- **Link**: https://arxiv.org/abs/2502.01774
- **Core idea**: Grokking reinterpreted as a distribution shift between training and test data rather than an optimization mystery.
- **Why it matters**: The 2025 theory pivot: grokking may be statistical, not dynamical — with direct implications for what "generalization" means for LLM evals.
- **Keywords**: grokking, distribution-shift, theory-2025

### [2025] A Survey on Grokking — (survey; ACM Computing Surveys)
- **Link**: https://dl.acm.org/doi/10.1145/3814603
- **Core idea**: Systematizes all grokking explanations: norm-based, circuit-formation, statistical, physics-based (glass relaxation).
- **Why it matters**: Entry point to the whole grokking literature; includes 2025 evidence of grokking during 7B-parameter pretraining (OLMoE).
- **Keywords**: grokking, survey

### [2025] Superposition Yields Robust Neural Scaling — (NeurIPS 2025; Anthropic toy-model based)
- **Link**: https://neurips.cc/virtual/2025/poster/116346
- **Core idea**: Neural scaling laws arise mechanistically from superposition — networks storing more features than neurons in interference-prone ways.
- **Why it matters**: First mechanistic account of WHY scaling laws exist, linking interpretability (domain 03) with scaling theory.
- **Keywords**: scaling-laws, superposition, mechanism

### [2026] A Limit Theory of Foundation Models — (authors: see paper)
- **Link**: https://arxiv.org/abs/2604.24037
- **Core idea**: A rigorous mathematical limit theory for foundation models, extending scaling-law analysis to data quality and training strategies.
- **Why it matters**: Theoretical frontier (as of 2026): scaling laws are becoming a full limit theory rather than curve fits.
- **Keywords**: limit-theory, scaling-laws, theory-2026

### [2023] Scaling Data-Constrained Language Models — Niklas Muennighoff et al.
- **Link**: https://arxiv.org/abs/2305.16264
- **Core idea**: Repeating data helps up to ~4 epochs, then returns diminish sharply; unique tokens dominate value.
- **Why it matters**: The data side of scaling laws — governs planning when internet text runs out; motivates synthetic data and RL data loops.
- **Keywords**: data-scaling, epochs, chinchilla

### [2005/2012] Universal Artificial Intelligence / AIXI — Marcus Hutter (book); with Shane Legg
- **Link**: https://arxiv.org/abs/0909.0801 (Legg & Hutter, "Universal Intelligence: A Definition of Machine Intelligence", 2007)
- **Core idea**: Intelligence = expected reward maximization over all computable environments weighted by algorithmic probability (AIXI); uncomputable but defines the optimum.
- **Why it matters**: The formal reference point every practical intelligence (including LLMs) is measured against; Legg-Hutter gives the field's cleanest intelligence definition.
- **Keywords**: aixi, universal-intelligence, definitions

### [2019] On the Measure of Intelligence — François Chollet
- **Link**: https://arxiv.org/abs/1911.01547
- **Core idea**: Intelligence = skill-acquisition efficiency over novel tasks, not skill itself; introduces the ARC benchmark built on core knowledge priors.
- **Why it matters**: Corrects the benchmark-culture error (skill ≠ intelligence); ARC-AGI remains the reference test for generalization (domain 05).
- **Keywords**: intelligence-definition, arc, generalization

---

## Cross-references into other domains

- **Hopfield (1982), Boltzmann machines (1985)** → energy-based lineage continues in `04_neuroscience-of-intelligence` and `05_frontiers-new-intelligence`.
- **Kaplan (2020), Chinchilla (2022), emergence debates** → applied side in `03_llm-architecture-training`.
- **Beggs & Plenz (2003) neuronal avalanches** (criticality in brains) → `04_neuroscience-of-intelligence`.
- **Zipf's law / power laws in language** → discussed in findings F11; also `02_deep-learning-canon` (unigram baselines).
