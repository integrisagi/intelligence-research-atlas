# Deep Learning Canon — Distilled Findings

What the 1943–2016 classics established. Paper references point to `papers.md` in this folder.

---

## F1 — The field's founding cycle: invent → over-promise → winter → revive

**Claim:** Every neural era follows the same arc: a real capability gain, inflated expectations, a theoretical/compute wall, funding collapse — then a revival when compute or theory catches up.

**Evidence:** Perceptron (1958) → Minsky–Papert XOR proof (1969) → first winter. Backprop revival (1986) → vanishing gradients (Hochreiter 1991) + data/compute scarcity → second winter. AlexNet (2012) breaks the wall with GPUs + ImageNet scale.

**Why it matters:** Expect the current scaling era to hit its own wall (data limits, energy); the pattern says the revival will come from a mechanism currently "known but impractical" — keep a shelf of discarded-but-sound ideas (neuromorphic, symbolic hybrids, energy-based).

---

## F2 — Architecture is crystallized inductive bias

**Claim:** Every lasting architecture is a physical commitment to an assumption about data structure, and it wins exactly when the assumption holds.

**Evidence:** CNN = translation equivariance via weight sharing (LeCun 1989); LSTM = constant-error carousel against vanishing gradients (1997); residual nets = learnable perturbations around identity (He 2015); MoE = conditional computation matching sparse task decomposition (Shazeer 2017).

**Why it matters:** Design rule for new architectures: state the world-assumption explicitly, then build the cheapest structure enforcing it (domain 01, F2 — no free lunch made rigorous).

---

## F3 — Depth needs help: gates, normalization, and identity paths are non-negotiable

**Claim:** Raw deep stacks don't train; three inventions make depth trainable, and all three persist unchanged inside transformers.

**Evidence:** Gates (LSTM 1997) → selective information flow; normalization (BatchNorm 2015 → LayerNorm/RMSNorm) → stable activation statistics; residual connections (ResNet 2015) → tame loss-landscape geometry (domain 01, F7).

**Why it matters:** Checklist for any new architecture: does information have an unobstructed identity path? Are activation scales controlled? Can the system learn to ignore a layer (gate)? Miss one and depth punishes you.

---

## F4 — Prediction-trained vectors contain semantics

**Claim:** Training only to predict co-occurrence produces internal geometry where relationships are directions and analogies are parallelograms — meaning without labels.

**Evidence:** word2vec (Mikolov 2013) linear analogy structure; CLIP (Radford 2021) extends to cross-modal alignment — "a photo of" space shared with text; LLM embeddings (domain 03) are the direct descendants and now the substrate of retrieval and agents.

**Why it matters:** Embeddings are the connective tissue of modern AI systems (RAG, tool retrieval, memory). Their geometry is learned, not designed — probe it empirically (domain 03 interpretability).

---

## F5 — Self-supervision converted all data into training data

**Claim:** The right pretext task (contrast, predict, mask) turns unlabeled data into supervision, unlocking internet-scale pretraining.

**Evidence:** InfoNCE predictive coding (2018) → SimCLR/MoCo (2020) beat supervised transfer in vision; CLIP (2021) added language supervision and zero-shot transfer; masked language modeling (BERT, domain 03) is the NLP instance.

**Why it matters:** Labels were the bottleneck of classical ML; removing it is why foundation models exist. Any new modality (robotics, genomics, audio) should first ask: what's the self-supervised pretext?

---

## F6 — Adversarial and minimax objectives are powerful but unstable teachers

**Claim:** Setting two networks against each other extracts training signal without labels, at the cost of delicate dynamics.

**Evidence:** GANs (2014) produce sharp samples but suffer mode collapse and training games; the stable counterexamples — contrastive (InfoNCE) and diffusion — use fixed, non-adversarial objectives and won the generative race.

**Why it matters:** Prefer minimax only where self-play genuinely explores (games, debate, red-teaming — domain 05); for representation learning, fixed-objective beats adversary.

---

## F7 — Deep RL works when you bolt on the brain's tricks

**Claim:** Raw deep Q-learning is unstable; the stabilizers that made it work — replay buffers, target networks, reward clipping — are engineering analogues of hippocampal mechanisms.

**Evidence:** DQN (Mnih 2015) needed experience replay (cf. hippocampal replay, domain 04) and a slowly-updated target network (cf. stabilizing consolidated memories); later improvements (distributional, prioritized replay 2016) kept the neuro pattern.

**Why it matters:** When RL systems misbehave (as reasoning-model training sometimes does, domain 03), the levers are the same: buffer coverage, target stability, reward shaping. Neuroscience is a parts catalog for RL repairs.

---

## F8 — Search atop learned evaluation beats either alone

**Claim:** Combining a learned policy/value with explicit search at decision time yields superhuman competence that pure learning or pure search cannot reach at the same budget.

**Evidence:** AlphaGo (2016) — MCTS guided by networks; AlphaZero (2017) — same from self-play alone; MuZero (2020) — search in a LEARNED latent model, no given rules.

**Why it matters:** This is the exact template of 2024–2026 reasoning LLMs: learned prior + test-time search (chain-of-thought as MCTS-lite). Test-time compute scaling (domain 03, F8) is AlphaZero's lesson applied to language.

---

## F9 — Generative modeling's arc: likelihood → adversarial → compression → diffusion

**Claim:** The field cycled through paradigms (VAEs 2013, GANs 2014, flow/likelihood models, autoregressive) before converging on diffusion for continuous data and autoregression for discrete tokens — with diffusion now invading language too.

**Evidence**: VAE (Kingma & Welling 2013) introduced the ELBO; GAN (2014) sharpness without stability; diffusion (Sohl-Dickstein 2015 → DDPM 2020) stable training with excellent samples; 2025 diffusion LLMs (domain 05) bring parallel token generation to text.

**Why it matters:** Choose generative machinery by data type and inference needs: autoregressive = streaming/any-time, diffusion = parallel/iterative refinement, VAE = explicit latent space. Hybrids are the frontier.

---

## F10 — The 2012 explosion was a conjunction, not an algorithm jump

**Claim:** AlexNet's breakthrough required three simultaneous factors — algorithm (deep CNN + ReLU + dropout), data (ImageNet's 14M labels), compute (GPUs) — and the field's velocity ever since tracks the weakest of the three.

**Evidence**: The CNN idea existed since 1989 (LeNet); ImageNet (Fei-Fei Li's dataset, 2009) and GTX 580 GPUs (2012) were the missing legs; modern scaling-law planning (domain 01, F8) is the formalization of managing all three resources.

**Why it matters:** When predicting capability jumps (or designing a new system), model all three constraints: ideas are usually NOT the bottleneck — data and compute are. And post-2025, a fourth axis exists: inference-time compute (domain 03).
