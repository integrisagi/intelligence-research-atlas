# Master Mindmap — The Whole Corpus

One map of everything in this atlas. Five domains branch from the root; leaves are the major ideas (details live in each domain's findings).

```mermaid
mindmap
  root((Intelligence<br/>Research<br/>Atlas))
    01 Mathematical Foundations
      Information theory
        Shannon entropy 1948
        Kolmogorov complexity 1965
        MDL - Rissanen 1978
      Learning theory
        VC dimension 1971
        PAC learning 1984
        No Free Lunch 1996
      Deep learning theory
        Zhang 2017 - random labels
        Double descent 2019
        Lazy vs rich regimes
        Loss landscape geometry
      Scaling science
        Kaplan power laws 2020
        Chinchilla 20 tok/param 2022
        Superposition mechanism 2025
        Limit theory 2026
      Phase changes
        Emergence - Wei 2022
        Mirage critique - Schaeffer 2023
        Grokking - Power 2022
        Grokking circuit - Nanda 2023
      Recurring patterns
        Power laws
        Scale-free networks
        Criticality - edge of chaos
        Symmetry and equivariance
        Renormalization = depth
      Formal intelligence
        AIXI - Hutter
        Legg-Hutter definition
        Chollet skill-acquisition efficiency
    02 Deep Learning Canon
      Origins
        Perceptron 1958
        Backprop 1986
        Vanishing gradients 1991
      Architecture primitives
        CNN weight sharing 1989
        LSTM gating 1997
        Residuals 2015
        Normalization 2015
        MoE sparsity 2017
      Representation learning
        word2vec 2013
        InfoNCE 2018
        SimCLR MoCo 2020
        CLIP multimodal 2021
      Generative modeling
        VAE 2013
        GAN 2014
        Diffusion 2015 to 2020
      Reinforcement learning
        Q-learning 1992
        DQN replay 2015
        AlphaGo 2016
        AlphaZero MuZero 2017-20
      The 2012 conjunction
        AlexNet
        GPUs
        ImageNet data
    03 LLM Architecture and Training
      Architecture
        Transformer 2017
        RoPE positions 2021
        FlashAttention 2022
        MoE frontier - DeepSeek V3
      Pretraining
        GPT-1 2 3
        BERT masking
        In-context learning 2020
        Chinchilla-optimal recipes
      Alignment
        RLHF - InstructGPT 2022
        Constitutional AI 2022
        DPO 2023
        LIMA - 1K examples
      Reasoning
        Chain-of-thought 2022
        Self-consistency ToT
        GRPO 2024
        DeepSeek-R1 RLVR 2025
        s1 budget forcing 2025
      Test-time compute
        Snell optimal scaling 2024
        Illusion of Thinking 2025
      Interpretability
        Induction heads 2022
        Superposition 2022
        SAE features 2023
        Circuit tracing 2025
      Engineering
        LoRA 2021
        RAG 2020
        Nucleus sampling
        Evaluation crisis
    04 Neuroscience of Intelligence
      Learning rules
        Hebbian assemblies
        Dopamine = TD error
        Feedback alignment
        Dendritic error propagation
      Prediction
        Predictive coding 1999
        Free energy principle
        Active inference
      Memory
        Hippocampal maps
        Grid cells
        Sleep replay
        Synaptic homeostasis
      Codes and geometry
        Sparse coding
        Population geometry
        RSA analysis
      Architecture
        Canonical microcircuit
        Global workspace
        Small-world topology
        Criticality - avalanches
      Meta
        Marr levels
        Prefrontal meta-learning
        Neuro-AI two-way street
    05 Frontiers - New Intelligence
      World models
        Dreamer 2019-23
        JEPA 2022-24
        MuZero planning
      Post-transformer
        Mamba SSM 2023
        KAN 2024
        xLSTM 2024
        TTT and Titans 2024-25
        Diffusion LLMs 2025
      Biological substrates
        Spiking networks
        Liquid time-constant
        Neuromorphic Loihi
      Hybrid and open-ended
        Neuro-symbolic
        Novelty search POET
        Evolution strategies
      Agents
        ReAct Reflexion
        Voyager skills
        Toolformer MCP
        Multi-agent swarms
      Self-improvement
        STaR bootstrap
        R1-Zero pure RL
        Absolute Zero 2025
      Oversight
        Debate 2018
        Scalable oversight
        Weak-to-strong 2023
        ARC-AGI benchmark
```

**How to use this map:** pick a leaf, then jump to the corresponding domain folder — `findings.md` files contain the full claim-evidence-implication treatment, and `papers.md` files carry the citations.
