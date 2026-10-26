# Deep Learning Canon (1943–2016) — The Papers That Built the Field

The classics: from the first neuron model through backprop, CNNs, LSTMs, representation learning, and RL milestones — everything before the transformer (which lives in domain 03).

---

### [1949] The Organization of Behavior — Donald Hebb
- **Link**: Wiley (book)
- **Core idea**: "Neurons that fire together wire together" — cell assemblies form via correlated activity.
- **Why it matters**: The first learning rule; Oja's PCA (domain 01) and all Hebbian methods descend from it.
- **Keywords**: hebb, plasticity, cell-assemblies

### [1958] The Perceptron: A Probabilistic Model — Frank Rosenblatt
- **Link**: https://doi.org/10.1103/PhysRevLett.58.381 → correct: Psychological Review 65(6): https://doi.org/10.1037/h0042519
- **Core idea**: A learnable threshold neuron with a convergence proof for linearly separable data.
- **Why it matters**: First artificial neural network trained by a rule; launched (and, with Minsky, froze) the field.
- **Keywords**: perceptron, linear-models, origins

### [1969] Perceptrons — Marvin Minsky, Seymour Papert
- **Link**: MIT Press (book)
- **Core idea**: Proves single-layer perceptrons cannot compute XOR; (over-)read as killing neural networks.
- **Why it matters**: First AI winter trigger; its real lesson — depth or hidden layers are necessary — took 17 years to answer (backprop).
- **Keywords**: perceptrons-book, xor, ai-winter

### [1986] Learning Internal Representations by Error Propagation (PDP, vol. 1) — David Rumelhart, Geoffrey Hinton, Ronald Williams
- **Link**: MIT Press (chapter); companion: Rumelhart, Hinton & Williams, Nature 323 (1986)
- **Core idea**: Multilayer networks trained end-to-end by backpropagated error signals.
- **Why it matters**: Reopened the field; every gradient-trained system since (all of them) uses this.
- **Keywords**: backpropagation, pdp, representations

### [1989] Generalization and Network Design Strategies — Yann LeCun (constraint-based / weight sharing)
- **Link**: Technical report, University of Toronto
- **Core idea**: Weight sharing drastically cuts parameters and bakes in translation structure → convolution.
- **Core idea (1998 follow-up)**: "Gradient-Based Learning Applied to Document Recognition" (LeCun, Bottou, Bengio, Haffner, Proc. IEEE) industrialized it as LeNet-5.
- **Why it matters**: The convolutional prior — the strongest demonstration that architecture = inductive bias (domain 01, F2); banks read checks with this in the 1990s.
- **Keywords**: cnn, weight-sharing, lenet

### [1991] Untersuchungen zu dynamischen neuronalen Netzen (vanishing gradients) — Sepp Hochreiter (diploma thesis, advisor J. Schmidhuber)
- **Link**: http://www.idsia.ch/~juergen/fundamentaldeeplearningproblem.html (overview)
- **Core idea**: Gradients through deep/squashing activations decay or explode exponentially — the "fundamental deep learning problem."
- **Why it matters**: Named the obstacle that residuates every architecture decision for 25 years (LSTM, ReLU, residuals, normalization).
- **Keywords**: vanishing-gradients, depth-problem

### [1997] Long Short-Term Memory — Sepp Hochreiter, Jürgen Schmidhuber
- **Link**: https://doi.org/10.1162/neco.1997.9.8.1735
- **Core idea**: Gated memory cells let gradients persist across hundreds of timesteps.
- **Why it matters**: THE sequence model 1997–2017 (translation, speech); gates and state-carrying cells reincarnate as the transformer's residual stream with memory roles.
- **Keywords**: lstm, recurrence, memory, gating

### [1992] Q-Learning — Christopher Watkins, Peter Dayan
- **Link**: https://doi.org/10.1007/BF00992698 (Watkins & Dayan 1992, Machine Learning)
- **Core idea**: Learn action values by bootstrapping temporal-difference errors — no model of the world needed.
- **Why it matters**: The bridge to neuroscience: dopamine neurons compute exactly this signal (Schultz 1997, domain 04); foundation of all value-based RL.
- **Keywords**: q-learning, reinforcement-learning, td-error

### [2012] ImageNet Classification with Deep Convolutional Neural Networks — Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton
- **Link**: https://doi.org/10.1145/3065386 (NeurIPS 2012)
- **Core idea**: GPU-trained deep CNN cuts ImageNet error nearly in half (16.4% vs 26.2%).
- **Why it matters**: The big bang of the modern era — proof that scale (data × compute × depth) wins; ignited the decade of deep learning.
- **Keywords**: alexnet, imagenet, gpus, deep-learning-big-bang

### [2013] Distributed Representations of Words and Phrases (word2vec) — Tomas Mikolov et al.
- **Link**: https://arxiv.org/abs/1310.4546 (NeurIPS 2013)
- **Core idea**: Skip-gram with negative sampling learns vector embeddings where directions carry meaning (king − man + woman ≈ queen).
- **Why it matters**: Meaning as geometry — the first widely-used demonstration that prediction-trained vectors encode semantics; the "embedding" concept every LLM uses internally.
- **Keywords**: word2vec, embeddings, distributional-semantics

### [2013] Auto-Encoding Variational Bayes — Diederik Kingma, Max Welling
- **Link**: https://arxiv.org/abs/1312.6114 (ICLR 2014)
- **Core idea**: Variational inference made amenable by reparameterization; encoder/decoder learn probabilistic latent representations.
- **Why it matters**: Founded deep generative modeling; the ELBO objective returns in diffusion theory and in "analysis-by-synthesis" brain models (domain 04).
- **Keywords**: vae, generative, variational-inference

### [2014] Sequence to Sequence Learning with Neural Networks — Ilya Sutskever, Oriol Vinyals, Quoc Le
- **Link**: https://arxiv.org/abs/1409.3215 (NeurIPS 2014)
- **Core idea**: Encode a sentence into a fixed vector, then decode it into another language.
- **Why it matters**: Established the encoder-decoder paradigm — and its fixed-vector bottleneck, which attention (next entry) was invented to remove.
- **Keywords**: seq2seq, encoder-decoder, translation

### [2014] Neural Machine Translation by Jointly Learning to Align and Translate — Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio
- **Link**: https://arxiv.org/abs/1409.0473 (ICLR 2015)
- **Core idea**: Attention: the decoder dynamically looks back at all encoder states instead of one vector.
- **Why it matters**: Invented attention as a soft, differentiable lookup — the mechanism the transformer made foundational (domain 03).
- **Keywords**: attention, nmt, alignment

### [2014] Generative Adversarial Networks — Ian Goodfellow et al.
- **Link**: https://arxiv.org/abs/1406.2661 (NeurIPS 2014)
- **Core idea**: Generator and discriminator locked in adversarial minimax; sample generation without explicit likelihoods.
- **Why it matters**: Adversarial self-play as a learning signal — concept recycled in debate-based alignment and adversarial eval (domain 05); also the instability case study that made the field take training dynamics seriously.
- **Keywords**: gan, adversarial, generative

### [2014] Adam: A Method for Stochastic Optimization — Diederik Kingma, Jimmy Ba
- **Link**: https://arxiv.org/abs/1412.6980 (ICLR 2015)
- **Core idea**: Per-parameter adaptive moments; robust default step sizes.
- **Why it matters**: The optimization workhorse (with AdamW variant) behind essentially all deep learning including LLM pretraining.
- **Keywords**: adam, optimization, sgd

### [2015] Batch Normalization: Accelerating Deep Network Training — Sergey Ioffe, Christian Szegedy
- **Link**: https://arxiv.org/abs/1502.03167 (ICML 2015)
- **Core idea**: Normalize layer inputs per minibatch to stabilize activation statistics.
- **Why it matters**: Made very deep training stable; its successor LayerNorm/RMSNorm is a fixed component of every transformer block.
- **Keywords**: normalization, training-stability

### [2015] Deep Residual Learning for Image Recognition — Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun
- **Link**: https://arxiv.org/abs/1512.03385 (CVPR 2016)
- **Core idea**: Learn residual functions with identity shortcuts → 100+ layer networks trainable.
- **Why it matters**: The residual stream is the transformer's backbone; loss-landscape geometry (domain 01, F7) explains WHY it works. Arguably the most reused architectural idea in history.
- **Keywords**: resnet, residuals, skip-connections

### [2015] Human-Level Control Through Deep Reinforcement Learning — Volodymyr Mnih et al. (DeepMind)
- **Link**: https://doi.org/10.1038/nature14236 (Nature 518)
- **Core idea**: Deep Q-network: CNN + Q-learning + experience replay + target networks learns Atari from raw pixels.
- **Why it matters**: First human-level learning from raw perception; experience replay explicitly borrowed from hippocampal replay (domain 04) — the neuro-AI transfer landmark.
- **Keywords**: dqn, atari, experience-replay, deep-rl

### [2014] Neural Turing Machines — Alex Graves, Greg Wayne, Ivo Danihelka
- **Link**: https://arxiv.org/abs/1410.5401
- **Core idea**: Differentiable external memory addressed by content and location.
- **Why it matters**: Opened the external-memory line (DNC 2016) — memory as an architectural component rather than emergent state; feeds directly into RAG and agent memory design (domain 05).
- **Keywords**: ntm, external-memory, differentiable

### [2016] Mastering the Game of Go with Deep Neural Networks and Tree Search (AlphaGo) — David Silver et al. (DeepMind)
- **Link**: https://doi.org/10.1038/nature16961 (Nature 529)
- **Core idea**: Policy/value networks guided Monte-Carlo tree search; trained on human games then self-play.
- **Why it matters**: Search + learned evaluation beats pure scale; the template that returns in reasoning models (o1/R1 style test-time search, domain 03).
- **Keywords**: alphago, search, self-play, planning

### [2017] Mastering Chess and Shogi by Self-Play (AlphaZero) / [2020] MuZero — David Silver, Julian Schrittwieser et al.
- **Link**: https://doi.org/10.1038/s41586-020-03051-4 (MuZero, Nature 2020); arXiv 1712.01815 (AlphaZero)
- **Core idea**: AlphaZero: self-play alone reaches superhuman Go/chess/shogi. MuZero: learns a latent world model and plans in it — no rules given.
- **Why it matters**: MuZero is the proof-of-concept that LEARNED world models + planning scale — the thesis of modern world-model research (domain 05).
- **Keywords**: alphazero, muzero, self-play, world-models, planning

### [2018] Representation Learning with Contrastive Predictive Coding — Aaron van den Oord, Yazhe Li, Oriol Vinyals
- **Link**: https://arxiv.org/abs/1807.03748
- **Core idea**: InfoNCE: learn representations by identifying the true future among negatives — maximizes mutual information.
- **Why it matters**: The single loss behind SimCLR/MoCo/CLIP and many RL representation methods; predictive coding's engineering counterpart (domain 04).
- **Keywords**: infonce, contrastive, predictive

### [2020] A Simple Framework for Contrastive Learning of Visual Representations (SimCLR) — Ting Chen, Simon Kornblith, Mohammad Norouzi, Geoffrey Hinton
- **Link**: https://arxiv.org/abs/2002.05709 (ICML 2020)
- **Core idea**: Augment-crop-contrast with big batches and projection heads alone learns strong visual features.
- **Why it matters**: Showed the recipe, not the architecture, drives self-supervised vision; killed the label bottleneck for pretraining.
- **Keywords**: simclr, contrastive, self-supervised

### [2020] Momentum Contrast for Unsupervised Visual Representation Learning (MoCo) — Kaiming He et al.
- **Link**: https://arxiv.org/abs/1911.05722 (CVPR 2020)
- **Core idea**: Dictionary-as-queue with momentum encoder makes contrastive learning practical without huge batches.
- **Why it matters**: With SimCLR, established that contrastive pretraining transfers to detection/segmentation beyond supervised ImageNet pretraining — a capability transfer precedent for all foundation models.
- **Keywords**: moco, contrastive

### [2021] Learning Transferable Visual Models From Natural Language Supervision (CLIP) — Alec Radford et al. (OpenAI)
- **Link**: https://arxiv.org/abs/2103.00020 (ICML 2021)
- **Core idea**: Contrastively align images and text captions at web scale → zero-shot classification by prompting.
- **Why it matters**: Multimodal grounding; zero-shot transfer as a paradigm; the backbone of image generators' text encoders and multimodal LLMs.
- **Keywords**: clip, multimodal, zero-shot, grounding

### [2015] Deep Unsupervised Learning using Nonequilibrium Thermodynamics — Jascha Sohl-Dickstein et al.
- **Link**: https://arxiv.org/abs/1503.03585 (ICML 2015)
- **Core idea**: Generate by slowly destroying structure with diffusion, then learn to reverse the noising process.
- **Why it matters**: Planted diffusion; with DDPM (Ho et al. 2020, arXiv 2006.11239) became the dominant generative paradigm — and by 2025 a serious language-modeling paradigm (diffusion LLMs, domain 05).
- **Keywords**: diffusion, generative, nonequilibrium

### [2017] Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer — Noam Shazeer et al.
- **Link**: https://arxiv.org/abs/1701.06538 (ICLR 2017)
- **Core idea**: Route each token to a few expert FFNs — parameters grow without proportional compute.
- **Why it matters**: Decoupling parameters from FLOPs; the backbone of frontier open models (Mixtral, DeepSeek-V3, domain 03).
- **Keywords**: moe, sparsity, conditional-computation

---

## Notable omissions (deliberate)

- **Transformers, BERT, GPT, RLHF, reasoning models** → domain 03 (they ARE the LLM story).
- **Hopfield/Boltzmann, predictive coding, dopamine** → domain 04 (neuroscience).
- **MAML, NTM successors, world models beyond MuZero** → domain 05 (frontiers).
