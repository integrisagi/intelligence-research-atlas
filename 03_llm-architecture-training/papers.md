# LLM Architecture & Training (2017–2026) — The Canon

The complete LLM stack: architecture, pretraining, alignment, reasoning, efficiency, and interpretability.

---

### [2017] Attention Is All You Need — Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan Gomez, Łukasz Kaiser, Illia Polosukhin
- **Link**: https://arxiv.org/abs/1706.03762 (NeurIPS 2017)
- **Core idea**: Drop recurrence entirely; stacked multi-head self-attention + FFN with positional encodings, trained fully in parallel.
- **Why it matters**: The substrate of every LLM; parallelism over sequence position is what made internet-scale training tractable.
- **Keywords**: transformer, attention, architecture

### [2018] BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding — Jacob Devlin et al. (Google)
- **Link**: https://arxiv.org/abs/1810.04805 (NAACL 2019)
- **Core idea**: Masked-language-model pretraining, bidirectional, then fine-tune per task.
- **Why it matters**: Pretrain-then-adapt became the NLP paradigm; held every GLUE record on release.
- **Keywords**: bert, masked-lm, pretraining

### [2018] Improving Language Understanding by Generative Pre-Training (GPT-1) — Alec Radford et al. (OpenAI)
- **Link**: https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf
- **Core idea**: Unidirectional (causal) LM pretraining + light task heads.
- **Why it matters**: Chose generation over masking — the path that scaled into GPT-2/3 and everything since.
- **Keywords**: gpt, causal-lm, pretraining

### [2019] Language Models are Unsupervised Multitask Learners (GPT-2) — Alec Radford et al. (OpenAI)
- **Link**: https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- **Core idea**: 1.5B parameters, web text (WebText) → coherent multi-paragraph text, zero-shot task behavior.
- **Why it matters**: First public evidence that scale alone induces task abilities without supervision — staged release foreshadowed the capability-safety debate.
- **Keywords**: gpt-2, zero-shot, scaling

### [2020] Language Models are Few-Shot Learners (GPT-3) — Tom Brown et al. (OpenAI)
- **Link**: https://arxiv.org/abs/2005.14165 (NeurIPS 2020)
- **Core idea**: 175B parameters; in-context learning — tasks solved via prompts/examples with NO weight updates.
- **Why it matters**: In-context learning is the property that turned LLMs into a general-purpose interface; launched the entire prompt-based ecosystem.
- **Keywords**: gpt-3, in-context-learning, few-shot, scaling

### [2020] Scaling Laws for Neural Language Models — Jared Kaplan et al.
- **Link**: https://arxiv.org/abs/2001.08361
- **Core idea**: See domain 01 — power-law loss across N, D, C.
- **Why it matters**: GPT-3's training budget was set by this curve; scaling became engineering.
- **Keywords**: scaling-laws

### [2022] Training Compute-Optimal Large Language Models (Chinchilla) — Jordan Hoffmann et al.
- **Link**: https://arxiv.org/abs/2203.15556
- **Core idea**: See domain 01 — ~20 tokens/parameter at fixed compute.
- **Why it matters**: Explained GPT-3-class models as undertrained; rewrote every lab's training recipe.
- **Keywords**: chinchilla, compute-optimal

### [2020] Exploring the Limits of Transfer Learning? (T5: Text-to-Text Transfer Transformer) — Colin Raffel et al.
- **Link**: https://arxiv.org/abs/1910.10683 (JMLR 2020)
- **Core idea**: Cast every NLP task as text-to-text; systematic ablations of scale/data/Architectures.
- **Why it matters**: The field's cleanest ablation study; unified interface precursor to instruction models.
- **Keywords**: t5, text-to-text, ablations

### [2022] Training language models to follow instructions with human feedback (InstructGPT) — Long Ouyang et al. (OpenAI)
- **Link**: https://arxiv.org/abs/2203.02155
- **Core idea**: SFT on demonstrations → RLHF (PPO) with a learned reward model from pairwise human preferences.
- **Why it matters**: The RLHF pipeline; ChatGPT's recipe. Aligned models differ from base models through this stage, not pretraining.
- **Keywords**: rlhf, instructgpt, alignment, ppo

### [2017] Deep Reinforcement Learning from Human Preferences — Paul Christiano et al.
- **Link**: https://arxiv.org/abs/1706.03741 (NeurIPS 2017)
- **Core idea**: Learn reward from human preference comparisons instead of hand-crafted rewards.
- **Why it matters**: The conceptual seed of RLHF, seven years before ChatGPT; also the seed of reward-hacking concerns.
- **Keywords**: rlhf, preferences, reward-model

### [2022] Constitutional AI: Harmlessness from AI Feedback — Yuntao Bai et al. (Anthropic)
- **Link**: https://arxiv.org/abs/2212.08073
- **Core idea**: Replace human preference labels with AI feedback guided by an explicit written constitution + chain-of-thought critique.
- **Why it matters**: RLAIF — supervision that scales with compute rather than human labelers; alignment-as-specified-principles.
- **Keywords**: constitutional-ai, rlaif, alignment

### [2023] LIMA: Less Is More for Alignment — Zhou et al.
- **Link**: https://arxiv.org/abs/2305.11206 (NeurIPS 2023)
- **Core idea**: 1,000 curated SFT examples on a strong base ≈ RLHF-level chat quality.
- **Why it matters**: Alignment is mostly SURFACE behavior elicitation — the knowledge comes from pretraining; contradicting "alignment teaches capabilities."
- **Keywords**: lima, sft, surface-alignment

### [2022] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models — Jason Wei et al. (Google)
- **Link**: https://arxiv.org/abs/2201.11903 (NeurIPS 2022)
- **Core idea**: Few-shot exemplars WITH intermediate steps dramatically unlock math/logic at large scale.
- **Why it matters**: Reasoning as a prompting-recoverable ability; token-space computation begins here → o1/R1.
- **Keywords**: chain-of-thought, reasoning, prompting

### [2022] Large Language Models are Zero-Shot Reasoners (“Let’s think step by step”) — Takeshi Kojima et al.
- **Link**: https://arxiv.org/abs/2205.11916 (NeurIPS 2022)
- **Core idea**: A single zero-shot phrase triggers stepwise reasoning — no exemplars.
- **Why it matters**: Reasoning capacity was already in the weights; prompting merely allocates tokens to it.
- **Keywords**: zero-shot-cot, reasoning

### [2023] Self-Consistency Improves Chain of Thought Reasoning — Xuezhi Wang et al.
- **Link**: https://arxiv.org/abs/2203.11171 (ICLR 2023)
- **Core idea**: Sample many reasoning paths, majority-vote answers.
- **Why it matters**: Simplest test-time-compute scaling; the "ensemble over thoughts" ancestor of search-based reasoning.
- **Keywords**: self-consistency, test-time-compute

### [2022] ReAct: Synergizing Reasoning and Acting in Language Models — Shunyu Yao et al.
- **Link**: https://arxiv.org/abs/2210.03629 (ICLR 2023)
- **Core idea**: Interleave chain-of-thought with tool/environment actions; reasoning plans actions, observations update reasoning.
- **Why it matters**: The agent loop — nearly every deployed agent framework (tool use, browsing, code agents) is ReAct-shaped.
- **Keywords**: react, agents, tool-use

### [2023] Tree of Thoughts: Deliberate Problem Solving with LLMs — Shunyu Yao et al. (Princeton/DeepMind)
- **Link**: https://arxiv.org/abs/2305.10601 (NeurIPS 2023)
- **Core idea**: Explore a TREE of thought branches with LLM-guided search (BFS/DFS), value judgments, backtracking.
- **Why it matters**: Explicit search over reasoning — MuZero's template in token space; big gains on planning-type tasks.
- **Keywords**: tree-of-thoughts, search, planning

### [2020] Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (RAG) — Patrick Lewis et al.
- **Link**: https://arxiv.org/abs/2005.11401 (NeurIPS 2020)
- **Core idea**: Differentiable retrieval into a non-parametric memory (vector index) fused with generation.
- **Why it matters**: Separates knowledge from weights — cheaper updates, fewer hallucinations, provenance; the backbone of enterprise LLM deployment.
- **Keywords**: rag, retrieval, memory

### [2021] LoRA: Low-Rank Adaptation of Large Language Models — Edward Hu et al.
- **Link**: https://arxiv.org/abs/2106.09685 (ICLR 2022)
- **Core idea**: Freeze weights; learn low-rank update matrices — adapter quality at a fraction of memory.
- **Why it matters**: Fine-tuning democratized (consumer GPUs); weight-deltas as shareable artifacts; the substrate of open-model customization.
- **Keywords**: lora, peft, fine-tuning

### [2022] FlashAttention: Fast and Memory-Efficient Exact Attention — Tri Dao et al.
- **Link**: https://arxiv.org/abs/2205.14135 (NeurIPS 2022)
- **Core idea**: IO-aware exact attention — tiling that never materializes the N×N matrix.
- **Why it matters**: Attention memory wall broken via systems thinking; enabled long-context training; template for kernel-level AI engineering (FlashAttention-2/3).
- **Keywords**: flashattention, kernels, efficiency

### [2021] RoFormer: Rotary Position Embedding (RoPE) — Jianlin Su et al.
- **Link**: https://arxiv.org/abs/2104.09864
- **Core idea**: Rotate query/key vectors by position-dependent angles — relative positions via complex-rotation structure.
- **Why it matters**: The default positional scheme of modern LLMs; RoPE-scaling tricks (NTK, YaRN) drive long-context extension.
- **Keywords**: rope, positional-encoding, long-context

### [2022] Switch Transformers: Scaling to Trillion Parameter Models — William Fedus, Barret Zohar, Noam Shazeer
- **Link**: https://arxiv.org/abs/2101.03961 (JMLR 2022)
- **Core idea**: Simplified top-1 MoE routing; trillion parameters with stable training.
- **Why it matters**: MoE made routine; with Mixtral (2024) and DeepSeek-V3 (2024), sparse routing became the open-frontier default — capability per training-FLOP.
- **Keywords**: moe, switch, conditional-computation

### [2024] DeepSeek-V3 Technical Report — DeepSeek-AI
- **Link**: https://arxiv.org/abs/2412.19437
- **Core idea**: 671B-total/37B-active MoE; Multi-head Latent Attention; FP8 training; 14.8T tokens for ~2.8M H800-GPU-hours (~$5.6M).
- **Why it matters**: Frontier capability at 1/20th the cost of Western equivalents; engineering recipe ( MLA, FP8, complementary-triangle MoE load balancing) now the open standard.
- **Keywords**: deepseek, moe, efficiency, fp8

### [2023] LLaMA: Open and Efficient Foundation Language Models — Hugo Touvron et al. (Meta)
- **Link**: https://arxiv.org/abs/2302.13971
- **Core idea**: Chinchilla-optimal small models (7–65B) trained on curated public data match much larger models.
- **Why it matters**: Open weights + efficient recipe → the entire open-ecosystem (Alpaca, Vicuna, Mistral lineage); weights-as-artifacts era.
- **Keywords**: llama, open-weights, chinchilla

### [2023] Direct Preference Optimization (DPO) — Rafael Rafailov et al.
- **Link**: https://arxiv.org/abs/2305.18290 (NeurIPS 2023)
- **Core idea**: Optimize preferences directly with a classification-style loss — no reward model, no PPO.
- **Why it matters**: RLHF-quality alignment with supervised-training simplicity; default in open post-training stacks.
- **Keywords**: dpo, preference-optimization

### [2024] DeepSeekMath: Pushing the Limits of Mathematical Reasoning (GRPO) — Zhihong Shao et al.
- **Link**: https://arxiv.org/abs/2402.03300
- **Core idea**: Group Relative Policy Optimization — PPO without a separate critic; advantages from group-relative rewards.
- **Why it matters**: The RL algorithm that made reasoning-RL cheap enough to run at scale; foundation of R1.
- **Keywords**: grpo, rl, reasoning

### [2025] DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning — Daya Guo et al. (Nature, October 2025)
- **Link**: https://doi.org/10.1038/s41586-025-09422-z
- **Core idea**: Pure RL with verifiable rewards (no SFT data, GRPO) elicits emergent reasoning behaviors — self-verification, reflection, long chains; test-time compute allocated by problem difficulty.
- **Why it matters**: The defining result of 2025: reasoning is TRAINABLE BY RL ALONE at scale; R1-distill series moved open models to frontier reasoning; second scaling axis (inference compute) mainstreamed.
- **Keywords**: deepseek-r1, rlvr, reasoning, test-time-compute

### [2024] Scaling LLM Test-Time Compute Optimally Can Be More Effective than Scaling Model Parameters — Charlie Snell, Jaehoon Lee, Sanjeev Raghavan, Avirup Sil (UC Berkeley)
- **Link**: https://arxiv.org/abs/2408.03314 (ICLR 2025)
- **Core idea**: On hard math, a small model + optimized test-time search beats a 14× larger model.
- **Why it matters**: Compute-optimal inference — a NEW scaling law axis; the theoretical spine of 2025's reasoning-model economics.
- **Keywords**: test-time-compute, inference-scaling

### [2025] s1: Simple Test-Time Scaling — Muennighoff et al. (Stanford)
- **Link**: https://arxiv.org/abs/2501.19393
- **Core idea**: 1K curated examples + "budget forcing" (extend/suppress "Wait" tokens) makes a 32B model rival far larger reasoning models.
- **Why it matters**: Test-time compute control reduced to token-budget steering — embarrassingly effective; reasoning supervision needs are tiny.
- **Keywords**: s1, budget-forcing, test-time-compute

### [2025] The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models — Parshin Shojaee et al. (Apple)
- **Link**: https://arxiv.org/abs/2506.06941
- **Core idea**: On puzzle environments with controlled complexity, reasoning models' accuracy collapses beyond a complexity threshold; effort declines as problems near the frontier.
- **Why it matters**: The strongest 2025 critique of "thinking" — pattern-matching vs. true search; frames the evaluation frontier (procedural, contamination-free benchmarks like ARC-AGI).
- **Keywords**: illusion-of-thinking, evaluation, limits

### [2022] In-Context Learning and Induction Heads — Catherine Olsson et al. (Anthropic)
- **Link**: https://arxiv.org/abs/2209.11895 (Transformer Circuits)
- **Core idea**: Identifies induction heads — two-attention-head circuits implementing "copy pattern A→B, complete A→? with B" — as the mechanism behind much in-context learning; forms during a training phase change.
- **Why it matters**: First circuit-level account of an emergent capability; mechanistic interpretability's flagship (with Nanda's grokking circuit, domain 01).
- **Keywords**: induction-heads, circuits, interpretability, icl

### [2022] Toy Models of Superposition — Nelson Elhage et al. (Anthropic)
- **Link**: https://transformer-circuits.pub/2022/toy-models/index.html
- **Core idea**: Networks store MORE features than neurons via nearly-orthogonal directions — polysemantic neurons are a consequence, not a bug.
- **Why it matters**: Explains why interpretability is hard AND why scaling works (superposition ↔ scaling laws, domain 01 F8/2025 mechanism); foundation of sparse-autoencoder feature research.
- **Keywords**: superposition, features, interpretability

### [2023] Towards Monosemanticity: Decomposing Language Models With Dictionary Learning — Trenton Bricken et al. (Anthropic)
- **Link**: https://transformer-circuits.pub/2023/monosemanticity/index.html
- **Core idea**: Sparse autoencoders extract monosemantic features (e.g., "Golden Gate Bridge", "code errors") from polysemantic layers.
- **Why it matters**: Made features concrete and steerable (feature activation = behavior control); scaling monosemanticity (Templeton et al. 2024) extracted millions of features from Claude — interpretability became an engineering discipline.
- **Keywords**: sae, features, monosemanticity, steering

### [2025] On the Biology of a Large Language Model (circuit tracing) — Anthropic Interpretability Team
- **Link**: https://www.anthropic.com/research/tracing-thoughts-language-model
- **Core idea**: Attribution graphs trace how individual prompts flow through features and circuits in Claude — planning in poems, multi-step reasoning observed directly.
- **Why it matters**: (As of 2026) the state of the art in opening the black box; moves interpretability from "what's stored" to "how it computes" — the microscope for F9's emergence questions.
- **Keywords**: circuit-tracing, interpretability, attribution

### [2023] Faith and Fate: Limits of Transformers on Compositionality — Nouha Dziri et al.
- **Link**: https://arxiv.org/abs/2305.18654 (NeurIPS 2023)
- **Core idea**: On multi-step compositional tasks transformers form parallel "shortcut" circuits whose error compounds exponentially with depth — they don't do serial abstraction natively.
- **Why it matters**: Explains why chain-of-thought (externalizing steps into tokens) is necessary, not stylistic; motivates search and tool use.
- **Keywords**: compositionality, limits, shortcuts

### [2020] The Curious Case of Neural Text Degeneration (nucleus sampling) — Ari Holtzman et al.
- **Link**: https://arxiv.org/abs/1904.09751 (ICLR 2020)
- **Core idea**: Greedy/beam text is degenerate; sampling from the nucleus (top-p mass) is human-like.
- **Why it matters**: Sampling strategy is cognition-relevant: model distribution's tail matters; still the default decoding knob in every deployed LLM.
- **Keywords**: decoding, nucleus-sampling

### [2023] GPT-4 Technical Report — OpenAI
- **Link**: https://arxiv.org/abs/2303.08774
- **Core idea**: Multimodal, scaled-up transformer; passes professional exams; (details withheld).
- **Why it matters**: System-scale evidence of continued scaling returns + multimodality; began the closed-frontier era (benchmarks-first disclosure).
- **Keywords**: gpt-4, system-report, multimodal

### [2025] Advances and Open Problems for LLMs (survey) — (authors: see paper)
- **Link**: https://arxiv.org/abs/2503.22732
- **Core idea**: Analyzes 27 top models (2023–2025): reasoning saturation, data constraints, efficiency frontiers, evaluation crisis.
- **Why it matters**: Best single map of the field's state as of early 2025 — use as the "what's actually open" reference.
- **Keywords**: survey, open-problems, llm-2025

---

## Cross-references

- **Scaling/emergence/grokking theory** → domain 01 (F8–F10).
- **World models, agents, self-improvement, post-transformer architectures** → domain 05.
- **Experience replay ↔ hippocampus, dopamine ↔ RL** → domain 04.
