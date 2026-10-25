# Neuroscience of Intelligence — The Canon

Brain mechanisms that carry design lessons for artificial systems. Cross-domain classics (McCulloch–Pitts, Hopfield, Boltzmann machines, Oja, Hebb) live in domains 01–02 and are cross-referenced at the bottom.

---

### [1952] A Quantitative Description of Membrane Current and Its Application to Conduction and Excitation in Nerve — Alan Hodgkin, Andrew Huxley
- **Link**: https://doi.org/10.1113/jphysiol.1952.sp004764 (J. Physiol.)
- **Core idea**: Coupled differential equations reproducing the action potential from ion-channel dynamics.
- **Why it matters**: Proof that computation can be *derived* from biophysics — the template for mechanistic explanation that AI's interpretability now imitates.
- **Keywords**: hodgkin-huxley, biophysics, spiking

### [1962] Receptive Fields, Binocular Interaction and Functional Architecture in the Cat's Visual Cortex — David Hubel, Torsten Wiesel
- **Link**: https://doi.org/10.1113/jphysiol.1962.sp006837
- **Core idea**: Cortical neurons are arranged in hierarchical feature detectors — simple cells feed complex cells with invariance.
- **Why it matters**: The direct biological inspiration for CNNs (LeCun 1989) — hierarchy + feature + invariance was observed in cortex 27 years before AlexNet.
- **Keywords**: receptive-fields, hierarchy, vision, cnn-inspiration

### [1978] The Hippocampus as a Cognitive Map — John O'Keefe, Lynn Nadel
- **Link**: Oxford University Press (book; place cells: O'Keefe & Dostrovsky 1971)
- **Core idea**: Place cells encode location; hippocampus implements a map-like relational memory, not a warehouse.
- **Why it matters**: Memory as structured, relational, spatial — the design reference for vector stores, agent spatial reasoning, and episodic memory architectures.
- **Keywords**: hippocampus, place-cells, cognitive-maps, memory

### [1982] Vision: A Computational Investigation into the Human Representation and Processing of Visual Information — David Marr
- **Link**: MIT Press (book, posthumous 1982)
- **Core idea**: Any intelligent system must be understood at three levels — computation (what/why), algorithm (how), implementation (substrate) — and levels are separable.
- **Why it matters**: The discipline that keeps AI honest: transformer = one algorithmic answer; LLM scaling debates are arguments at Marr's computational level.
- **Keywords**: marr-levels, computational-theory, methodology

### [1994] Reactivation of Hippocampal Ensemble Memories During Sleep — Matthew Wilson, Bruce McNaughton
- **Link**: https://doi.org/10.1126/science.1851943 (Wilson & McNaughton 1994, Science)
- **Core idea**: Sequences of place-cell activity from waking experience are replayed during sleep.
- **Why it matters**: Offline consolidation as a computation — the biological justification for experience replay in RL (DQN) and for offline training phases generally.
- **Keywords**: replay, sleep, consolidation, hippocampus

### [1996] Emergence of Simple-Cell Receptive Field Properties by Learning a Sparse Code for Natural Images — Bruno Olshausen, David Field
- **Link**: https://doi.org/10.1038/381607a0 (Nature 381)
- **Core idea**: Optimizing for SPARSE codes of natural images reproduces V1 receptive fields — no teacher, no labels.
- **Why it matters**: The brain's sensory code is shaped by efficient coding of environmental statistics; the direct ancestor of sparse autoencoder features in LLM interpretability (domain 03, F8).
- **Keywords**: sparse-coding, efficient-coding, unsupervised, v1

### [1997] A Neural Substrate of Prediction and Reward (dopamine neurons) — Wolfram Schultz, Peter Dayan, Read Montague
- **Link**: https://doi.org/10.1126/science.275.5306.1593 (Science 275)
- **Core idea**: Dopamine neurons do not signal reward — they signal REWARD PREDICTION ERROR, exactly the TD error of Q-learning.
- **Why it matters**: The single most celebrated neuro↔AI bridge: a learning algorithm (TD, domain 02) was discovered in neurons before it was standard in machines (or rather, matched after) — reward prediction errors drive both.
- **Keywords**: dopamine, td-error, reinforcement-learning, prediction-error

### [1999] Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects — Rajesh Rao, Dana Ballard
- **Link**: https://doi.org/10.1038/1480 (Nature Neuroscience)
- **Core idea**: Cortex transmits prediction ERRORS up the hierarchy (feedback carries predictions); explains end-stopping and contextual effects.
- **Why it matters**: Bandwidth-efficient, learned, hierarchical inference — the brain runs a self-supervised predictive model; the blueprint for predictive-processing architectures and a candidate biologically plausible learning rule.
- **Keywords**: predictive-coding, hierarchy, feedback, prediction-error

### [2003] A Neural Global Workspace Theory of Conscious (and Unconscious) Processing — Stanislas Dehaene, Jean-Pierre Changeux (building on Baars' Global Workspace 1988)
- **Link**: https://doi.org/10.1016/S1053-8119(03)00067-7 (with Baars 2003 Neuron: "A neuronal global workspace model")
- **Core idea**: Conscious access = broadcasting of a winner-take-all selection through a global workspace — a shared, capacity-limited bottleneck routed to many processors.
- **Why it matters**: A concrete architecture pattern (bottleneck + broadcast) that inspired MoE-style routing, LLM context as workspace, and modular agent designs (Goyal & Bengio 2020).
- **Keywords**: global-workspace, consciousness, broadcast, bottleneck

### [2004] An Information-Theoretic Measure of Consciousness (Integrated Information Theory) — Giulio Tononi
- **Link**: https://doi.org/10.1186/1471-2202-5-42 (BMC Neuroscience)
- **Core idea**: Consciousness corresponds to integrated information (Φ) — the causal irreducibility of a system's parts.
- **Why it matters**: Influential formal program linking substrate structure to experience; CONTested (adversarial testing 2023 favored recurrent processing over IIT) — include as theory-design lesson: formal elegance ≠ empirical validity.
- **Keywords**: iit, consciousness, integrated-information

### [2004] Neuronal Circuits of the Neocortex: The Canonical Microcircuit — Rodney Douglas, Kevan Martin
- **Link**: https://doi.org/10.1146/annurev.neuro.26.041002.131126 (Annu. Rev. Neurosci.)
- **Core idea**: Cortex is a repeated canonical circuit (6 layers, characteristic recurrence and inhibition) whose connectivity is stereotyped across areas.
- **Why it matters**: Nature's answer to architecture reuse: one repeated block, specialized by input/output, prefigures layer-stacking universality (transformer blocks).
- **Keywords**: microcircuit, cortex, canonical-architecture

### [2005] Microstructure of a Spatial Map in the Entorhinal Cortex (grid cells) — Torkel Hafting, Marianne Fyhn, Sturla Molden, May-Britt Moser, Edvard Moser
- **Link**: https://doi.org/10.1038/nature03721 (Nature 436)
- **Core idea**: Entorhinal grid cells fire on hexagonal tessellations — a metric spatial code.
- **Why it matters**: Nobel-recognized discovery of an elegant internal coordinate system; grid-cell-like codes emerge in RL agents (Banino 2018) — convergent evolution of representation between brains and networks.
- **Keywords**: grid-cells, entorhinal, spatial-coding

### [2005] Uncertainty, Neuromodulation, and Attention (ACh & NE) — Angela Yu, Peter Dayan
- **Link**: https://doi.org/10.1016/j.neuron.2005.04.014 (Neuron 46)
- **Core idea**: Acetylcholine signals expected uncertainty; norepinephrine signals unexpected uncertainty — neuromodulators encode uncertainty types, gating learning and attention.
- **Why it matters**: Global state control as architecture: neuromodulation is a broadcast hyperparameter system — the biological template for meta-learners, adaptive optimizers, and context conditioning in ML.
- **Keywords**: neuromodulation, uncertainty, ach, ne, gain-control

### [2006] Small-World Brain Networks — Danielle Bassett, Ed Bullmore
- **Link**: https://doi.org/10.1016/j.brainresrev.2006.03.011 (and Watts–Strogatz 1998, domain 01)
- **Core idea**: Human brain graphs combine high local clustering with short global path lengths — optimal for segregated AND integrated processing.
- **Why it matters**: Network-architecture lesson for AI: mixture-of-experts routing, agent topologies, and MoE load-balancing are engineering rediscoveries of small-world design.
- **Keywords**: connectome, small-world, network-topology

### [2006] Neuronal Avalanches in Neocortical Circuits — John Beggs, Dietmar Plenz
- **Link**: https://doi.org/10.1523/JNEUROSCI.23-35-11167.2003 (J. Neurosci. 2003); see also Kinouchi & Copelli 2006, Nat. Phys.
- **Core idea**: Cortical activity propagates in power-law-distributed avalanches — signatures of operation near a critical point.
- **Why it matters**: Evidence the brain self-tunes to criticality (maximal dynamic range, information transmission) — matching self-organized criticality in physics (domain 01, F11) and edge-of-chaos results in RNN/attention dynamics.
- **Keywords**: criticality, avalanches, power-laws

### [2008**] Representational Similarity Analysis (RSA): Connecting Computational Models with Brains — Nikolaus Kriegeskorte, Marieke Mur, Peter Bandettini
- **Link**: https://doi.org/10.3389/neuro.06.039.2008 (Frontiers in Systems Neuroscience; concept formalizing Edelman 1998)
- **Core idea**: Compare representations via geometry of pairwise distances — model-agnostic comparison between brains, behavior, and machines.
- **Why it matters**: The measurement tool of representational convergence: CNN layers ↔ visual cortex correspondences (later Yamins et al. 2014) were established this way; reusable for comparing your model's internal geometry to anything.
- **Keywords**: rsa, representational-geometry, neuro-ai-comparison

### [2006] Sleep and Synaptic Homeostasis — Giulio Tononi, Chiara Cirelli
- **Link**: https://doi.org/10.1016/j.neuron.2006.04.016 (Neuron; hypothesis 2003–2006)
- **Core idea**: Sleep globally downscales synaptic strengths — renormalizing after a day of potentiation, preserving relative weights.
- **Why it matters**: A biological analogue of normalization and weight decay — "forget the noise, keep the signal"; a design hint for continual-learning systems that consolidate by re-normalizing.
- **Keywords**: sleep, homeostasis, synaptic-scaling

### [2018] Prioritized Memory Access Reveals Planning Networks in the Brain — Marcelo Mattar, Nathaniel Daw
- **Link**: https://doi.org/10.1038/s41593-018-0232-z (Nature Neuroscience)
- **Core idea**: What to replay is itself a computation: expected reward gain × shortcut-to-decision determine replay priority.
- **Why it matters**: Explains WHY experience replay works and when: prioritized replay is information-theoretically optimal curriculum — directly transferable to RL buffer design and agent memory management.
- **Keywords**: replay, planning, prioritization, rl-bridge

### [2017] Dendritic Error Backpropagation in Deep Cortical Microcircuits — João Sacramento, Rui Ponte Costa, Yoshua Bengio, Walter Senn
- **Link**: https://doi.org/10.1038/s41593-017-0020-0 (Nature Neuroscience)
- **Core idea**: Layer-specific dendritic compartments can carry error signals locally, approximating backprop in a biologically plausible cortical circuit.
- **Why it matters**: Existence proof that error-driven deep learning might be implementable in wetware — and a template for local-learning-rule hardware (neuromorphic, optical).
- **Keywords**: dendrites, local-learning, backprop-plausibility

### [2016] Random Feedback Weights Support Learning in Deep Neural Networks (feedback alignment) — Timothy Lillicrap, Daniel Cownden, Douglas Tweed, Colin Akerman
- **Link**: https://doi.org/10.1038/ncomms13276 (Nature Communications)
- **Core idea**: Backward weights need not be symmetric — networks adapt their forward weights to whatever feedback channel exists.
- **Why it matters**: Kills the "backprop is biologically impossible" objection in its simplest form; enables training on hardware where exact reverse passes are impractical.
- **Keywords**: feedback-alignment, local-learning, plausibility

### [2016] Towards an Integration of Deep Learning and Neuroscience — Adam Marblestone, Greg Wayne, Konrad Kording
- **Link**: https://doi.org/10.3389/fncom.2016.00094 (Frontiers in Computational Neuroscience)
- **Core idea**: Systematic map of what neuroscience could contribute to deep learning: memory, attention, continual learning — with the transfer direction specified.
- **Why it matters**: The reference agenda for neuro→AI borrowing; use as a checklist against your architecture design.
- **Keywords**: neuro-ai, integration, agenda

### [2017] Neuroscience-Inspired Artificial Intelligence — Demis Hassabis, Dharshan Kumaran, Courtney Summerfield, Matthew Botvinick
- **Link**: https://doi.org/10.1016/j.neuron.2017.06.011 (Neuron 95)
- **Core idea**: Historical and forward synthesis: reliving the neuro→AI pipeline that produced CNNs/RL/attention, and what remains untapped (meta-learning, memory consolidation).
- **Why it matters**: The manifesto of the field from DeepMind's cofounder — argues AGI likely requires re-engagement with brain mechanisms.
- **Keywords**: neuro-ai, manifesto, hassabis

### [2018] Prefrontal Cortex as a Meta-Reinforcement Learning System — Jane Wang, Zeb Kurth-Nelson, Dharshan Kumaran, ... Matthew Botvinick, Demis Hassabis
- **Link**: https://doi.org/10.1038/s41593-018-0147-8 (Nature Neuroscience 21)
- **Core idea**: The brain's prefrontal system implements meta-RL: slow synaptic learning (outside) shapes a fast in-context learner (inside) — and the same dynamics emerge in recurrent ANNs trained on task distributions.
- **Why it matters**: Unifies biological and artificial in-context learning: prefrontal meta-RL ≈ transformer ICL (domain 03, F7); tells you when learned recurrent state beats weight updates.
- **Keywords**: meta-learning, prefrontal, icl-parallel

### [2019] High-Dimensional Geometry of Population Responses — Stringer, C. et al. (Carsen Stringer, Marius Pachitariu, Nicholas Steinmetz, ... Kenneth Harris)
- **Link**: https://doi.org/10.1038/s41586-019-1346-5 ("High-dimensional geometry of population responses in visual cortex", Nature)
- **Core idea**: Cortical populations track many stimulus variables (near-power-law eigenspectrum) while remaining decodable — high-dimensional but smooth, no collapse.
- **Why it matters**: Empirical geometry that neural networks should match; connects to superposition (domain 03, F8) and neural collapse (domain 01) — three views of representation geometry across substrates.
- **Keywords**: population-geometry, manifold, representational-dimension

### [2020] Inductive Biases for Higher-Level Cognition — Anirudh Goyal, Yoshua Bengio
- **Link**: https://arxiv.org/abs/2011.09192
- **Core idea**: Transplant Global-Workspace-style inductive biases (bottleneck, modules, broadcast, attention control) into deep nets for combinatorial generalization.
- **Why it matters**: The most concrete GWT-to-architecture pipeline — directly relevant to modular/multi-agent LLM system design (domain 05).
- **Keywords**: global-workspace, inductive-bias, modularity

### [2025] A Survey on Neuro-Mimetic Deep Learning via Predictive Coding — Tommaso Salvatori et al.
- **Link**: arXiv (2025; PubMed-indexed — search "Salvatori predictive coding survey")
- **Core idea**: Comprehensive survey of predictive coding as a learning algorithm — approximating backprop with local errors, with efficiency gains on edge hardware.
- **Why it matters**: The 2025 state of a serious backprop alternative: local, online, event-friendly — candidate learning rule for neuromorphic and continually-learning systems (domain 05).
- **Keywords**: predictive-coding, survey, backprop-alternative, 2025

---

## Cross-references into other domains

- **McCulloch–Pitts (1943), Hopfield (1982), Boltzmann machines (1985), Oja (1982)** → domain 01 (mathematical foundations).
- **Hebb (1949), Q-learning TD (1992), DQN experience replay (2015)** → domain 02.
- **Free energy principle / active inference (Friston)** — mathematical treatment → domain 01 F14; agent applications → domain 05.
- **Superposition vs sparse coding; induction heads; interpretability** → domain 03.
