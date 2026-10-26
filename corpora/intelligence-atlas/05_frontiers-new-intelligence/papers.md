# Frontiers: New Types of Intelligence — The Canon

Papers that point *beyond* the current LLM recipe: learned world models, active inference, memory and meta-learning, post-transformer and biological substrates, neuro-symbolic hybrids, open-ended evolution, collective intelligence, LLM agents, self-improvement loops, and scalable oversight. Cross-domain anchors: Chollet (2019) lives in `01_mathematical-foundations` (ARC); MuZero in `02_deep-learning-canon`; ReAct, RAG, RLVR/R1 in `03_llm-architecture-training`.

---

## World models & planning

### [2012] Perceptions as Hypotheses: Saccades as Experiments — Karl Friston, Rick Adams, Laurent Perrinet, Michael Breakspear
- **Link**: https://doi.org/10.1098/rstb.2011.0426 (Phil. Trans. R. Soc. B)
- **Core idea**: Under active inference, perception and action both minimize the same free-energy functional — the brain literally acts to test its perceptual hypotheses.
- **Why it matters**: The founding statement that one objective (expected free energy) can drive perception, planning, and curiosity — a template for agents that need no separate reward function. Kept short here; neuroscience context in domain 04.
- **Keywords**: active-inference, free-energy, perception-action

### [2018] World Models — David Ha, Jürgen Schmidhuber
- **Link**: https://arxiv.org/abs/1803.10122 (NeurIPS 2018)
- **Core idea**: Train a tiny VAE world model and an RNN predictor of its latent dynamics, then evolve a small controller inside hallucinated dreams instead of the real environment.
- **Why it matters**: First striking demonstration that a *learned internal simulator* can be the training ground for behavior — the conceptual seed of Dreamer and of all latent-imagination agents.
- **Keywords**: world-models, dreaming, evolution, v-m-c

### [2019] Learning Latent Dynamics for Planning from Pixels (PlaNet) / [2020] Dream to Control (Dreamer) — Danijar Hafner, Timothy Lillicrap, et al.
- **Link**: https://arxiv.org/abs/1811.04551 (PlaNet, ICML 2019); https://arxiv.org/abs/1912.01603 (Dreamer, ICLR 2020)
- **Core idea**: PlaNet learns a recurrent state-space model from pixels and plans in it; Dreamer makes it sample-efficient by backpropagating value through imagined trajectories (latent imagination) with a replay of only real interactions.
- **Why it matters**: Converts RL from trial-and-error in reality to *learning inside a learned model* — the efficiency route to agents that cannot afford millions of real mistakes.
- **Keywords**: world-models, latent-planning, model-based-rl, dreamer

### [2020] Scaling Active Inference — Alex Tschantz, Beren Millidge, Anil K. Seth, Christopher L. Buckley
- **Link**: https://arxiv.org/abs/1911.10601 (PLoS Computational Biology)
- **Core idea**: Deep active-inference agents (expected free energy = extrinsic value + epistemic value) match or beat model-free RL on standard domains and solve tasks RL cannot without reward shaping.
- **Why it matters**: Shows active inference is an engineering-viable alternative to reward-based RL — intrinsic curiosity falls out of the objective rather than being bolted on.
- **Keywords**: active-inference, epistemic-value, curiosity, deep-rl

### [2023] Mastering Diverse Domains through World Models (DreamerV3) — Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap
- **Link**: https://arxiv.org/abs/2301.04104
- **Core idea**: A single fixed hyperparameter set masters 150+ tasks across benchmarks, and becomes the first agent to collect a Minecraft diamond from scratch, with no human data.
- **Why it matters**: First evidence that one world-model-based learner can scale across wildly different domains — a concrete counter-proposal to "one benchmark per specialized RL stack".
- **Keywords**: dreamer-v3, world-models, minecraft, generality

### [2022] A Path Towards Autonomous Machine Intelligence (JEPA position paper) — Yann LeCun
- **Link**: https://openreview.net/pdf?id=BZ5a1r-kVsf
- **Core idea**: An architecture blueprint (Joint Embedding Predictive Architecture) in which agents predict in *abstract representation space*, not pixels, using a hierarchy of world models plus a configurator and intrinsic cost.
- **Why it matters**: The most detailed published alternative to the generative-next-token path: prediction without generation, planning in latent space, energy-based inference — and it now anchors a real research program (I-JEPA, V-JEPA).
- **Keywords**: jepa, latent-prediction, world-models, position-paper

### [2023] Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture (I-JEPA) — Mahmoud Assran, Quentin Duval, Ishan Misra, et al. (Meta)
- **Link**: https://arxiv.org/abs/2301.08243 (CVPR 2023)
- **Core idea**: Predict representations of masked image regions from other regions, in embedding space — no pixel reconstruction, no hand-crafted augmentations.
- **Why it matters**: First large-scale working instance of LeCun's blueprint: representation learning by latent prediction beats generative and contrastive pipelines, validating "predict abstractions, not pixels".
- **Keywords**: i-jepa, self-supervised, latent-prediction

### [2024] Revisiting Feature Prediction for Learning Visual Representations from Video (V-JEPA) — Adrien Bardes, Quentin Garrido, Jean Ponce, et al. (Meta)
- **Link**: https://arxiv.org/abs/2404.08471
- **Core idea**: Extends JEPA to video: predict latent features of temporally masked frames; the model develops intuitive physics (object permanence, action prediction) without labels.
- **Why it matters**: Moves world models toward the pretraining-scale regime — a video-prediction substrate that downstream agents and robotics stacks can build on.
- **Keywords**: v-jepa, video, intuitive-physics, self-supervised

---

## Memory & meta-learning

### [2016] Hybrid Computing Using a Neural Network with Dynamic External Memory (DNC) — Alex Graves, Greg Wayne, Ivo Danihelka, et al. (DeepMind)
- **Link**: https://doi.org/10.1038/nature20101 (Nature)
- **Core idea**: A neural controller with a differentiable, addressable external memory matrix it learns to read, write, and allocate — inference and manipulation by pure gradient descent.
- **Why it matters**: Memory as an explicit architectural component (not emergent state) — the ancestor of RAG indexes, agent episodic stores, and test-time-memory architectures.
- **Keywords**: dnc, external-memory, differentiable-memory

### [2016] Learning to Reinforcement Learn — Jane X. Wang, Zeb Kurth-Nelson, Dhruva Tirumala, et al. (DeepMind)
- **Link**: https://arxiv.org/abs/1611.05763
- **Core idea**: An RNN meta-trained across many tasks learns implicit RL algorithms in its recurrent dynamics — including exploration strategies adapted to each new task at test time.
- **Why it matters**: Demonstrates that learning-to-learn can emerge in weights + activation state rather than hand-designed updates; the pre-LLM statement of "pretraining then adapting" for decision-making.
- **Keywords**: meta-rl, rnn, learning-to-learn

### [2016] HyperNetworks — David Ha, Andrew Dai, Quoc V. Le
- **Link**: https://arxiv.org/abs/1609.09106 (ICLR 2017)
- **Core idea**: One network generates the weights of another, so model structure itself becomes a learned, dynamically adaptable function of context.
- **Why it matters**: Weights stop being fixed parameters and become *state* — the conceptual root of fast weights, hypernetwork adapters, and test-time weight adaptation.
- **Keywords**: hypernetworks, weight-generation, fast-weights

### [2017] Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks (MAML) — Chelsea Finn, Pieter Abbeel, Sergey Levine
- **Link**: https://arxiv.org/abs/1703.03400 (ICML 2017)
- **Core idea**: Optimize initial parameters explicitly so that a few gradient steps on a new task yield good performance — learn an initialization, not a solution.
- **Why it matters**: The canonical formalization of "learn to adapt in k steps"; the reference point every sample-efficient-adaptation scheme (including LLM-tuning-as-meta-learning analogies) is measured against.
- **Keywords**: maml, meta-learning, few-shot-adaptation

### [2020] Hopfield Networks is All You Need — Hubert Ramsauer, Bernhard Schäfl, Johannes Lehner, et al. (Hochreiter group)
- **Link**: https://arxiv.org/abs/2008.02217 (ICLR 2021)
- **Core idea**: Transformer attention is mathematically equivalent to one update step of a modern (exponential-capacity) Hopfield network retrieving a stored pattern.
- **Why it matters**: Reframes attention as *associative memory retrieval* — connecting transformers to the Hopfield energy-based lineage (domain 01) and licensing energy-based, memory-centric alternatives to softmax attention.
- **Keywords**: hopfield, associative-memory, attention-theory, energy-based

---

## Post-transformer architectures

### [2001] The "Echo State" Approach to Analysing and Training Recurrent Neural Networks — Herbert Jaeger
- **Link**: GMD Report 148, German National Research Center for Information Technology
- **Core idea**: Keep a large random recurrent reservoir fixed and train only a linear readout — the "echo state" property makes the reservoir a fading memory of its input history.
- **Why it matters**: Established reservoir computing: dynamics as a fixed feature map, learning confined to a cheap output layer — the low-energy predecessor of today's frozen-backbone + small-adapter designs.
- **Keywords**: echo-state, reservoir-computing, rcc

### [2018] Neural Ordinary Differential Equations — Ricky T. Q. Chen, Yulia Rubanova, Jesse Bettencourt, David Duvenaud
- **Link**: https://arxiv.org/abs/1806.07366 (NeurIPS 2018)
- **Core idea**: Define network depth as a continuous ODE solved by standard numerical integrators, with gradients via the adjoint method at constant memory cost.
- **Why it matters**: Makes *continuous time* a first-class modeling axis — the mathematical basis for liquid networks and for architectures that trade discrete layers for physical-time dynamics.
- **Keywords**: neural-ode, continuous-time, adjoint-method

### [2023] RWKV: Reinventing RNNs for the Transformer Era — Bo Peng, Eric Alcaide, et al.
- **Link**: https://arxiv.org/abs/2305.13048 (EMNLP Findings 2023)
- **Core idea**: An RNN that can be trained in parallel like a transformer (linear attention reformulated as a recurrence) and runs in constant memory at inference.
- **Why it matters**: Proof that recurrence and parallel training are not mutually exclusive — a streaming, deployable alternative to quadratic attention born in the open-source community.
- **Keywords**: rwkv, rnn, linear-attention, streaming

### [2023] Hyena Hierarchy: Towards Larger Convolutional Language Models — Michael Poli, Stefano Massaroli, Eric Nguyen, et al.
- **Link**: https://arxiv.org/abs/2302.10866 (ICML 2023)
- **Core idea**: Replace attention with long implicit convolutions gated by a small MLP, yielding subquadratic scaling to hundreds of thousands of context tokens.
- **Why it matters**: Showed the attention kernel itself is replaceable at language-model scale — the long-convolution branch of the post-transformer zoo that Mamba later overshadowed.
- **Keywords**: hyena, long-convolutions, subquadratic

### [2023] Mamba: Linear-Time Sequence Modeling with Selective State Spaces — Albert Gu, Tri Dao
- **Link**: https://arxiv.org/abs/2312.00752
- **Core idea**: Make state-space parameters input-dependent (selective), so the model chooses what to remember or forget — transformer-class quality at linear time and constant per-token memory.
- **Why it matters**: The flagship non-transformer backbone: streaming/edge inference, million-token contexts, and DNA/audio modeling — and the template the whole 2024+ SSM ecosystem (Jamba, hybrid stacks) builds on.
- **Keywords**: mamba, state-space-models, selective, linear-time

### [2024] xLSTM: Extended Long Short-Term Memory — Maximilian Beck, Korbinian Pöppel, Markus Spanring, et al. (Hochreiter group)
- **Link**: https://arxiv.org/abs/2405.04517
- **Core idea**: Modernizes the LSTM with exponential gating and matrix memory (sLSTM, mLSTM), restoring the classic cell's competitiveness with transformers and Mamba.
- **Why it matters**: The recurrence line did not die in 2017 — a direct counter-demonstration that gated recurrence, properly upgraded, belongs in the architecture search space.
- **Keywords**: xlstm, recurrence, gated-memory

### [2024] KAN: Kolmogorov-Arnold Networks — Ziming Liu, Yixuan Wang, Sachin Vaidya, et al.
- **Link**: https://arxiv.org/abs/2404.19756
- **Core idea**: Put learnable activation functions on edges (B-splines) instead of fixed activations on nodes, exploiting the Kolmogorov-Arnold representation theorem.
- **Why it matters**: Small KANs discover symbolic, interpretable formulas where MLPs fit opaque surfaces — an architecture whose inductive bias points toward compositional and scientific discovery, not just benchmark loss.
- **Keywords**: kan, learnable-activations, symbolic, interpretability

### [2024] Learning to (Learn at Test Time): RNNs with Expressive Hidden States (TTT layers) — Yu Sun, Xinhao Li, Karan Dalal, et al. (Stanford)
- **Link**: https://arxiv.org/abs/2407.04620
- **Core idea**: Make the RNN hidden state itself a small neural network whose update rule is a step of self-supervised learning — the sequence layer literally trains its memory during the forward pass.
- **Why it matters**: Unifies fast weights, meta-learning, and long-context modeling: adaptation stops being a separate fine-tuning phase and becomes part of inference.
- **Keywords**: ttt, test-time-training, fast-weights, hidden-state

### [2025] Titans: Learning to Memorize at Test Time — Ali Behrouz et al. (Google)
- **Link**: https://arxiv.org/abs/2501.00663
- **Core idea**: A neural long-term memory module that *surprises-based* writes and forgets at test time, coordinated with short-term attention in a hybrid architecture that scales beyond 2M context.
- **Why it matters**: Memory management (what to store, when to forget) becomes an architectural, learned-in-place mechanism — a direct answer to the context-window economics of long-horizon agents.
- **Keywords**: titans, test-time-memory, surprise, long-context

### [2025] Large Language Diffusion Models (LLaDA) — Shen Nie, Fengqi Zhu, Chao Du, et al. (Ant Group, Renmin University)
- **Link**: https://arxiv.org/abs/2502.09992
- **Core idea**: An 8B-parameter diffusion LM trained from scratch with masked-diffusion pretraining and instruction tuning that rivals LLaMA3-8B on many benchmarks.
- **Why it matters**: First convincing evidence that the *generative paradigm itself* (any-order parallel denoising vs left-to-right factorization) is swappable at language-model scale, with built-in infilling and controllability.
- **Keywords**: llada, diffusion-lm, masked-diffusion, parallel-generation

### [2025] Commercial diffusion language models: Mercury and Gemini Diffusion — Inception Labs; Google DeepMind
- **Link**: https://www.inceptionlabs.ai/blog/introducing-mercury; https://deepmind.google/models/gemini-diffusion (ecosystem milestone, not a paper)
- **Core idea**: Mercury (2025-02) ships the first commercial-scale diffusion LLM at 1000+ tokens/sec on H100s; Gemini Diffusion (2025-05) is Google DeepMind's research-preview diffusion model with comparable speed.
- **Why it matters**: Parallel diffusion decoding turns generation speed from a serial-token constraint into a hardware-parallel one — the first deployed crack in autoregressive orthodoxy.
- **Keywords**: diffusion-lm, mercury, gemini-diffusion, commercial-milestone

### [2021] Liquid Time-Constant Networks — Ramin Hasani, Mathias Lechner, et al. (MIT)
- **Link**: https://arxiv.org/abs/2006.04439 (AAAI 2021)
- **Core idea**: Neural ODEs whose time constants are states, so each neuron adapts its own clock to the input — closed-form variants (CfC) make them cheap enough for deployment.
- **Why it matters**: Networks that natively handle irregular sampling and time-warped streams (robotics, wearables, edge sensing) — where fixed-clock discrete stacks waste computation.
- **Keywords**: liquid-networks, neural-ode, time-constants, edge

---

## Neuromorphic substrates

### [1997] Networks of Spiking Neurons: The Third Generation of Neural Network Models — Wolfgang Maass
- **Link**: https://doi.org/10.1016/S0893-6080(97)00011-7 (Neural Networks)
- **Core idea**: Neurons that communicate by discrete spikes are computationally more powerful than sigmoid units — even with the same analog noise — when time is used as a resource.
- **Why it matters**: The theoretical charter for event-driven, sparse, energy-cheap computation; every neuromorphic hardware claim descends from it. (Cross-ref domain 04 for the neuroscience side; not yet covered there as of 2026-10.)
- **Keywords**: spiking-neurons, third-generation, neuromorphic

### [2018] Loihi: A Neuromorphic Manycore Processor with On-Chip Learning — Mike Davies et al. (Intel)
- **Link**: IEEE Micro 38(1):82-99 (2018)
- **Core idea**: A 128-core chip with asynchronous spiking neurons and programmable on-chip plasticity rules, consuming milliwatts on workloads that cost GPUs watts.
- **Why it matters**: Physical proof that learning can run at 3-5 orders of magnitude lower energy than GPU training/inference — the hardware existence theorem for always-on embedded intelligence.
- **Keywords**: loihi, neuromorphic-hardware, on-chip-learning, efficiency

### [2023] SpikeGPT: Generative Pre-trained Language Model with Spiking Neural Networks — Rui-Jie Zhu, Qihang Zhao, Guoqi Li, Jason K. Eshraghian
- **Link**: https://arxiv.org/abs/2302.13939 (IJCAI 2023)
- **Core idea**: A GPT-style language model (up to 345M params) built on spiking RWKV neurons, generating text with binary event-driven activations at roughly 20x less energy than an equivalent dense model.
- **Why it matters**: The bridge paper: modern generative LLM architecture rendered in spiking form — connects the LLM world to neuromorphic hardware deployment rather than toy tasks.
- **Keywords**: spikegpt, spiking-lm, rwkv, energy-efficiency

---

## Neural-symbolic & programs

### [2018] DeepProbLog: Neural Probabilistic Logic Programming — Robin Manhaeve, Sebastijan Dumančić, Angelika Kimmig, Thomas Demeester, Luc De Raedt
- **Link**: https://arxiv.org/abs/1805.10860 (NeurIPS 2018)
- **Core idea**: Embed neural networks as probabilistic predicates inside a differentiable logic program, so gradients flow through logical inference itself.
- **Why it matters**: The cleanest mechanism for systematic compositionality: symbols guarantee rule structure while sub-symbolic nets supply perception — exactly the generalization pattern pure LLMs still miss.
- **Keywords**: deepproblog, neural-symbolic, probabilistic-logic

### [2019] The Neuro-Symbolic Concept Learner: Interpreting Scenes, Words, and Sentences from Natural Supervision — Jiayuan Mao, Chuang Gan, Pushmeet Kohli, Joshua Tenenbaum, Jiajun Wu
- **Link**: https://arxiv.org/abs/1904.12584 (ICLR 2019; NS-VQA)
- **Core idea**: A visual parser turns pixels into object programs, a semantic parser turns questions into symbolic programs, and answering is program execution — no program annotations.
- **Why it matters**: Demonstrates human-like data efficiency and zero-shot recombination on VQA by splitting perception (neural) from reasoning (symbolic) — the architecture pattern behind 2024-25 neuro-symbolic ARC solvers.
- **Keywords**: neuro-symbolic, program-induction, vqa, compositionality

---

## Evolution & open-endedness

### [2011] Abandoning Objectives: Evolution Through the Search for Novelty Alone — Joel Lehman, Kenneth O. Stanley
- **Link**: https://doi.org/10.1162/EVCO_a_00025 (Evolutionary Computation)
- **Core idea**: Searching only for behavioral novelty — with no objective function at all — sometimes finds solutions that objective-driven search never reaches (e.g., the deceptive-maze robot).
- **Why it matters**: Formalizes that objectives can actively mislead: stepping stones to intelligence may only be discoverable by open-ended, novelty-seeking search — a design principle for generating what we cannot specify.
- **Keywords**: novelty-search, open-endedness, deception, evolution

### [2017] Evolution Strategies as a Scalable Alternative to Reinforcement Learning — Tim Salimans, Jonathan Ho, Xi Chen, et al. (OpenAI)
- **Link**: https://arxiv.org/abs/1703.03864
- **Core idea**: Black-box evolution of policy parameters, parallelized across thousands of gradient-free workers, matches deep RL on MuJoCo while sidestepping backprop-through-time entirely.
- **Why it matters**: Learning without gradients is embarrassingly parallel and non-differentiable-stack-friendly — the fallback optimizer for world models, agents, and hardware where gradients do not flow.
- **Keywords**: evolution-strategies, gradient-free, scalable-rl

### [2019] Paired Open-Ended Trailblazer (POET) — Rui Wang, Joel Lehman, et al.
- **Link**: https://arxiv.org/abs/1901.01753
- **Core idea**: Endlessly generate new environments and their solvers together, transferring agents between paired challenges to keep difficulty at each learner's frontier.
- **Why it matters**: The first working engine of open-ended co-evolution of tasks and solutions — an automatic curriculum generator, and a concrete answer to "where does an endless training signal come from?".
- **Keywords**: poet, open-endedness, curriculum-generation, co-evolution

---

## Multi-agent & collective intelligence

### [2018] Emergence of Linguistic Communication from Referential Games — Angeliki Lazaridou, Alexander Peysakhovich, Marco Baroni (with 2016 antecedents)
- **Link**: https://arxiv.org/abs/1712.10364 (ICLR 2018)
- **Core idea**: Two agents invent a discrete language to solve referential games; grounded, compositional-ish protocols emerge from pure cooperation pressure, but drift toward non-human languages without inductive biases.
- **Why it matters**: The experimental base camp for emergent communication: tells you exactly which pressures (grounding, population, ease) make shared symbolic systems arise — and which make them alien.
- **Keywords**: emergent-communication, referential-games, multi-agent

### [2023] Generative Agents: Interactive Simulacra of Human Behavior — Joon Sung Park, Joseph O'Brien, Carrie Cai, et al. (Stanford)
- **Link**: https://arxiv.org/abs/2304.03442 (UIST 2023)
- **Core idea**: 25 LLM agents with memory streams, reflection, and planning in a sandbox town produce believable social behavior (party planning, relationship formation) evaluated by human raters.
- **Why it matters**: The founding demo of society-scale simulation: LLMs as substrate for social-science experiments, agent economies, and synthetic populations — collective intelligence built from generative individuals.
- **Keywords**: generative-agents, simulation, social-behavior, memory-streams

### [2024-2026] Multi-agent LLM ecosystems: swarms, MCP, agent-to-agent protocols — ecosystem development (no single paper)
- **Link**: https://modelcontextprotocol.io (MCP spec, Anthropic 2024; ecosystem docs)
- **Core idea**: A practical stack crystallizes around standard tool protocols (MCP, 2024), agent swarms/orchestration frameworks, and emerging agent-to-agent communication formats across vendors.
- **Why it matters**: Multi-agent intelligence is becoming *infrastructure* rather than research demo — standard interfaces let heterogeneous agents compose, which is the precondition for agent economies and collective systems that outgrow any single model.
- **Keywords**: multi-agent-llm, mcp, protocols, agent-swarms, ecosystem

---

## LLM agents & self-improvement

### [2022] STaR: Bootstrapping Reasoning With Reasoning — Eric Zelikman, Yuhuai Wu, Jesse Mu, Noah D. Goodman (Stanford)
- **Link**: https://arxiv.org/abs/2203.14465 (NeurIPS 2022)
- **Core idea**: Generate rationales, keep only those that produce correct final answers, fine-tune on them, and re-generate — reasoning ability bootstraps itself upward from a few seeds.
- **Why it matters**: The origin loop of LLM self-improvement: the STaR pattern (generate, filter by outcome, train, repeat) is the direct ancestor of rejection-sampling fine-tuning and RLVR-era reasoning training.
- **Keywords**: star, bootstrapping, rationale-generation, self-improvement

### [2023] Toolformer: Language Models Can Teach Themselves to Use Tools — Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, et al. (Meta)
- **Link**: https://arxiv.org/abs/2302.04761 (NeurIPS 2023)
- **Core idea**: A model self-annotates where inserting an API call (calculator, search, QA) would reduce its own perplexity, then fine-tunes on those insertions — tool use learned, not prompted.
- **Why it matters**: The model becomes the dispatcher that decides *when* computation should leave its weights — the learning-side foundation of function calling and of agents that offload exact work to tools.
- **Keywords**: toolformer, tool-use, api-calls, self-annotation

### [2023] Reflexion: Language Agents with Verbal Reinforcement Learning — Noah Shinn, Federico Cassano, Beck Labash, et al.
- **Link**: https://arxiv.org/abs/2303.11366 (NeurIPS 2023)
- **Core idea**: Agents that fail a task store a *verbal* self-diagnosis in episodic memory and retry with that lesson in context — episodic control implemented in language instead of weights.
- **Why it matters**: Cheap, gradient-free self-improvement: converting execution feedback into natural-language policy updates is now the standard inner loop of serious agent frameworks.
- **Keywords**: reflexion, verbal-rl, self-critique, episodic-memory

### [2023] Voyager: An Open-Ended Embodied Agent with Large Language Models — Guanzhi Wang, Yuqi Xie, Yunfan Jiang, et al. (NVIDIA, Caltech)
- **Link**: https://arxiv.org/abs/2305.16291 (TMLR 2024)
- **Core idea**: An LLM agent in Minecraft writes its own actions as code, verifies them, and stores verified skills in a growing skill library that compounds across tasks without any gradient updates.
- **Why it matters**: The skill-library pattern: continual learning as *accumulated executable artifacts* — the most copied mechanism for making agents improve monotonically in open worlds.
- **Keywords**: voyager, skill-library, code-as-action, minecraft, open-ended

### [2025] Absolute Zero: Reinforced Self-play Reasoning with Zero Data — Andrew Zhao, Yiran Wu, Yang Yue, et al. (Tsinghua LeapLab)
- **Link**: https://arxiv.org/abs/2505.03335 (NeurIPS 2025)
- **Core idea**: One model both *proposes* tasks (to maximize its own learnability) and solves them, verified by a code executor — AlphaZero-style self-play for reasoning with zero external data.
- **Why it matters**: A working escape from the human-data bottleneck: the training signal is generated and checked by machine, pointing at open-ended self-improvement loops (and their unsupervised-error risks).
- **Keywords**: absolute-zero, self-play, rlvr, zero-data, code-executor

### [2024] OpenAI o3 on ARC-AGI: reasoning models crack (part of) the generality benchmark — OpenAI (system milestone)
- **Link**: https://arcprize.org/blog/oai-o3-pub-breakthrough (announced 2024-12)
- **Core idea**: o3, trained with RL on verifiable tasks plus large test-time search, scored 75.7% (87.5% with 172x compute) on ARC-AGI-Pub — the first big jump on the benchmark that had resisted a decade of approaches.
- **Why it matters**: Evidence that Chollet's skill-acquisition framing (domain 01) responds to RL + test-time search — while costing enormous compute per task, showing "generality" and "efficiency" are still far from joint. System-scale evidence, flagged as such.
- **Keywords**: o3, arc-agi, system-report, test-time-search, rlvr

### [2025] ARC-AGI-2: the persistent holdout — ARC Prize Foundation (benchmark milestone)
- **Link**: https://arcprize.org/arc-agi-2 (announced 2025-03; see leaderboard)
- **Core idea**: A redesigned ARC suite targeting the efficiency gap — tasks tuned so humans still solve most while frontier reasoning models score in the single to low double digits at release.
- **Why it matters**: Even o3-class systems only partially crack ARC-AGI-1 at extreme cost, and ARC-AGI-2 re-opens the gap: a live yardstick separating "skill at scale" from general, *sample-efficient* intelligence (Chollet 2019, domain 01).
- **Keywords**: arc-agi-2, benchmark, sample-efficiency, generality-gap

---

## Alignment for stronger systems

### [2018] AI Safety via Debate — Geoffrey Irving, Paul Christiano, Dario Amodei (OpenAI)
- **Link**: https://arxiv.org/abs/1807.03764
- **Core idea**: Two adversarial AI debaters with a human judging only the transcript can, in principle, supervise capabilities beyond the judge's own — amplifying oversight instead of capability alone.
- **Why it matters**: The core mechanism candidate for supervising smarter-than-human systems: supervision scales with computation spent on debate, not with judge expertise.
- **Keywords**: debate, scalable-oversight, amplification

### [2022] Measuring Progress on Scalable Oversight for Large Language Models — Samuel R. Bowman et al.
- **Link**: https://arxiv.org/abs/2211.03540
- **Core idea**: A unified evaluation suite (weak-strong pairings, sandwiching, debate, market-making) for the concrete question: can weak overseers extract truthful behavior from stronger models?
- **Why it matters**: Turns oversight from philosophy into benchmark engineering — defines the measurable race between model capability and our ability to check it.
- **Keywords**: scalable-oversight, evaluation, weak-oversseer, sandwiching

### [2023] Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision — Collin Burns, Pavel Izmailov, Jan Hendrik Kirchner, et al. (OpenAI)
- **Link**: https://arxiv.org/abs/2312.09390
- **Core idea**: Fine-tuning a strong model on labels from a much weaker one recovers most of the strong model's capability — and sometimes beats the weak supervisor's own ceiling.
- **Why it matters**: Empirical hope that humans can keep steering superhuman models via weak signals (if generalization conditions hold) — the working hypothesis behind 2025-26 oversight plans for self-improving systems.
- **Keywords**: weak-to-strong, superalignment, generalization

---

## Cross-references

- **Chollet (2019) On the Measure of Intelligence / ARC** → domain 01; ARC system results (o3, ARC-AGI-2) live here.
- **MuZero (latent-model planning), AlphaGo/Zero self-play** → domain 02; the planning lineage Dreamer extends and the self-play lineage Absolute Zero cites.
- **ReAct, RAG, RLHF, DeepSeek-R1/RLVR, test-time-compute taxonomy** → domain 03; the agent stack (diagrams/agent-stack) composes them with this domain's papers.
- **Hopfield (1982), energy-based learning** → domain 01; Ramsauer 2020 and associative-memory architectures continue that line.
- **Predictive coding / free-energy neuroscience** → domain 04 (Friston); Tschantz 2020 is the engineering-side counterpart.
- **DNC external memory** ← flagged in domain 02 (memory line); extended here.
