# Neuroscience of Intelligence — Distilled Findings

Paper references point to `papers.md` in this folder.

---

## F1 — Neurons that fire together wire together: local learning builds global structure

**Claim:** The brain's primary plasticity rule is local correlation (Hebbian), and from it emerge assemblies, maps, and effective codes — sophisticated global structure from a one-line local rule.

**Evidence:** Hebb (1949, domain 02); Oja (1982, domain 01) showed Hebbian + normalization ⇒ PCA; Olshausen & Field (1996) showed sparse-coding objectives reproduce V1 receptive fields.

**Why it matters:** Biology computes statistics with local rules — no global loss function, no error backprop through a deep stack. Local-rule learning (Hebbian, anti-Hebbian, predictive-coding local errors) is the enabling technology for neuromorphic hardware and lifelong learning systems that cannot afford end-to-end backprop.

---

## F2 — Dopamine IS the TD error: the brain runs reinforcement learning

**Claim:** Midbrain dopamine neurons broadcast a reward-prediction error mathematically identical to the temporal-difference error of RL — the same algorithm, wet and dry.

**Evidence:** Schultz, Dayan & Montague (1997): phasic dopamine responds to unpredicted reward, omitted when predicted reward fails to appear; matches TD error dynamics in detail; drug addiction and reward-hacking in RL agents both exploit the same circuit.

**Why it matters:** Validation that RL is not merely "inspired by" brains — it IS the brain's evaluation subsystem. When engineering reward (RLHF, RLVR, domain 03), expect biological pathologies: reward hacking ≈ addiction, over-training on proxy reward ≈ dopamine dysregulation.

---

## F3 — The brain is a prediction machine: perception as controlled hallucination

**Claim:** Cortex implements hierarchical predictive coding — higher areas predict lower areas' input; only prediction errors propagate up; perception is the model's hallucination corrected by errors.

**Evidence:** Rao & Ballard (1999) explain extra-classical receptive-field effects with predictive coding; the free-energy principle (Friston, see domain 01 F14) generalizes it to perception, action, and learning under one variational objective; self-supervised losses (InfoNCE, masked prediction, domain 02/03) are engineering descendants.

**Why it matters:** Strongest convergence result in neuro-AI: next-token prediction loss and cortical predictive coding are the same design pattern at different substrates. Predictive-coding local errors are also a live backprop alternative (Salvatori et al. 2025 survey).

---

## F4 — Sparse, distributed, high-dimensional coding — twice over

**Claim:** Both brains and transformers represent concepts as sparse patterns across many units, packing more concepts than neurons via geometric cleverness.

**Evidence:** V1 sparse codes from natural statistics (Olshausen & Field 1996); cortex population responses maintain high-dimensional smooth manifolds with near-power-law eigenspectra (Stringer et al. 2019); transformer superposition — more features than dimensions, polysemantic neurons (Elhage et al. 2022, domain 03).

**Why it matters:** Convergent evolution across substrates suggests sparse distributed coding is near-optimal for capacity/generalization tradeoffs. If designing representations or memory formats, default to sparse high-dimensional codes; use dictionary learning (SAEs) to audit them.

---

## F5 — Hippocampus: relational maps, grid codes, replay — the memory subsystem design

**Claim:** The brain's memory system is not storage but structured simulation: cognitive maps, metric coordinate codes, and offline replay that re-instates and re-combines experience.

**Evidence:** O'Keefe & Nadel (1978) place cells / cognitive maps; Hafting et al. (2005) hexagonal grid cells; Wilson & McNaughton (1994) sleep replay; Mattar & Daw (2018): replay is PRIORITIZED by expected usefulness; Banino et al. (2018): grid-like codes emerge in RL agents trained to navigate.

**Why it matters:** The blueprint for agent memory: episodic store + spatial/relational indexing + prioritized replay for consolidation and planning. DQN's replay buffer was the first loan; agentic systems are still under-collecting on this design (domain 05).

---

## F6 — Sleep is training infrastructure: consolidation by renormalization

**Claim:** Offline periods actively consolidate — global synaptic downscaling preserves relative strengths while restoring capacity, and replay selectively strengthens what matters.

**Evidence:** Tononi & Cirelli (2006) synaptic homeostasis hypothesis; Wilson & McNaughton (1994), Foster & Wilson (2006) replay directionality; parallel to ML: weight decay, distillation, and model merging as consolidation.

**Why it matters:** Continual-learning systems should schedule consolidation phases (replay + renormalization + pruning) between acquisition phases — systems that only ever accumulate weights degrade (catastrophic forgetting). "Sleep" for your agents is a real design pattern.

---

## F7 — Global workspace: bottlenecked broadcast as an architecture

**Claim:** Flexible cognition arises when many parallel specialists compete for a limited-capacity global workspace whose contents broadcast back to all — serial access atop parallel processing.

**Evidence:** Baars (1988) and Dehaene et al. (2003) neuronal workspace; Goyal & Bengio (2020) translate GWT into deep-learning inductive biases; echoes in MoE routing (specialists + router-broadcast) and LLM context windows as a shared scratchpad.

**Why it matters:** A ready-made pattern for multi-agent LLM systems: specialists + arbiter + shared context. Also a candidate theory of conscious access — useful both as architecture and as a lens on system "attention".

---

## F8 — Brains operate at criticality: the edge of chaos

**Claim:** Cortical dynamics sit near a critical point between order and chaos, maximizing dynamic range, information transmission, and memory capacity — a self-organized optimal regime.

**Evidence:** Neuronal avalanches follow power laws (Beggs & Plenz 2003); computational studies show near-critical branching maximizes sensitivity/dynamic range (Kinouchi & Copelli 2006); parallel physics: self-organized criticality (Bak et al. 1987, domain 01).

**Why it matters:** Initialization/dynamics lore in deep learning (edge-of-chaos RNNs, signal propagation) is the same mathematics. If your recurrent/feedback system is either too stable (dead) or too chaotic (untrainable), tune toward criticality deliberately.

---

## F9 — The brain's wiring is small-world and modular — topology is compute

**Claim:** The connectome's architecture — local clusters, short global paths, modules with hubs — is itself a computational strategy optimizing segregated vs integrated processing.

**Evidence:** Bassett & Bullmore (2006) small-world brain networks; network science foundations (Watts–Strogatz 1998, domain 01); MoE/agent topologies rediscover the pattern (routers = hubs).

**Why it matters:** When distributing an AI system across modules or machines, small-world design (dense local, sparse global) is the default-robust topology; also a maintenance principle: keep interfaces narrow (like white-matter bundles).

---

## F10 — Backprop's biological gap has working alternatives

**Claim:** Exact backprop is biologically implausible (weight transport problem), but multiple mechanisms approximate it plausibly — the brain likely does error-driven learning some other way, and so can future hardware.

**Evidence:** Feedback alignment: random fixed feedback still trains deep nets (Lillicrap et al. 2016); dendritic compartments carry layer-local errors approximating backprop (Sacramento et al. 2017); predictive coding converges to backprop-like gradients with local updates (Salvatori et al. 2025).

**Why it matters:** For energy-efficient / lifelong / analog substrates (neuromorphic, optical, biological), local learning rules are the enabling constraint — this research line is the toolbox.

---

## F11 — Neuromodulation is global state control — hyperparameters as signals

**Claim:** Beyond point-to-point computation, brains broadcast scalars (dopamine, acetylcholine, norepinephrine, serotonin) that gate plasticity, gain, and uncertainty handling across whole systems — a separate, slower control channel.

**Evidence:** Yu & Dayan (2005): ACh encodes expected, NE unexpected uncertainty; dopamine gates learning rate and exploration (Schultz 1997); Wang et al. (2018): prefrontal meta-learning modulated by these systems.

**Why it matters:** In ML terms: learned global conditioning — adaptive optimizers, learned exploration schedules, context-dependent gain (as in hypernetworks and meta-learning). Multi-agent designs should include a dedicated, low-bandwidth state-control channel rather than burying mode-switches in weights.

---

## F12 — Representational geometry is the shared language of brains and networks

**Claim:** Comparing representations by their geometry (distances, manifolds, spectra) reveals deep correspondences between neural populations and artificial networks — the same compressions keep appearing.

**Evidence:** Kriegeskorte et al. (2008) RSA methodology; later work mapping CNN layers to visual cortex (Yamins et al. 2014 era); Stringer et al. (2019) population geometry; neural collapse in classifiers (domain 01) and superposition in transformers (domain 03) as geometry universals.

**Why it matters:** RSA-style comparison is a practical tool: benchmark your model's internal geometry against known-good systems (brain or model), detect pathological representations early, and choose regularizers that shape geometry (not just loss).

---

## F13 — Marr's three levels keep AI research honest

**Claim:** Every intelligence claim must specify its level — computational (what problem is solved), algorithmic (what procedure), implementational (what substrate) — and conflating levels produces bad science and bad engineering.

**Evidence:** Marr (1982); recurring modern confusions: benchmark scores (computational claims) treated as evidence about algorithms ("the model reasons") or substrate ("emergent consciousness"); IIT (2004) illustrates formal elegance failing empirical grounding.

**Why it matters:** Use Marr as a review discipline: when a paper claims an ability, ask which level the evidence actually supports. When designing systems, decide the computational problem FIRST — most failed architectures are level-mismatches (right problem, wrong bias).

---

## F14 — The street runs both ways: neuro→AI and AI→neuro

**Claim:** Every major AI breakthrough has a neuroscience loan in its past, and AI models now serve as testable hypotheses about the brain — the loop is accelerating.

**Evidence:** Neuro→AI: Hubel–Wiesel→CNNs, dopamine→TD/RL, replay→DQN, hippocampus→memory architectures, Wang et al. (2018) prefrontal→meta-learning. AI→neuro: RSA + CNNs as cortical models, deep nets predicting neural activity, Hassabis et al. (2017) agenda; Marblestone et al. (2016) integration map.

**Why it matters:** Treat this corpus as a two-way toolkit: before building a component, check the neuro literature for a proven mechanism; before theorizing about brains, build the model and test it. The fastest path to novel intelligence runs through this loop deliberately, not accidentally.
