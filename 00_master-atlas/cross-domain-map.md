# Cross-Domain Map — How the Five Domains Connect

One graph linking the core ideas across all five domains. Color-by-subgraph; arrows mean "informs / grounds / enables."

```mermaid
graph LR
    subgraph MATH["01 Mathematics"]
        ENTROPY["Entropy & compression<br/>Shannon 1948"]
        IB["Information bottleneck"]
        SCALE["Scaling power laws<br/>Kaplan - Chinchilla"]
        GROK["Grokking &<br/>phase transitions"]
        CRIT["Criticality &<br/>power-law patterns"]
        NFL["Inductive bias<br/>No Free Lunch"]
    end

    subgraph DL["02 Deep learning"]
        BACKPROP["Backprop"]
        ARCH["Architecture = bias<br/>CNN - LSTM - ResNet"]
        SSL["Self-supervised<br/>prediction"]
        RL["TD / Q-learning"]
        SEARCH["Search + evaluation<br/>AlphaGo - MuZero"]
    end

    subgraph LLM["03 LLMs"]
        TRF["Transformer"]
        ICL["In-context learning<br/>induction heads"]
        RLHF["RLHF / preferences"]
        RLVR["RLVR reasoning<br/>DeepSeek-R1"]
        TTC["Test-time compute<br/>Snell - s1"]
        INTERP["Interpretability<br/>superposition - SAEs"]
    end

    subgraph NEURO["04 Neuroscience"]
        PC["Predictive coding<br/>free energy"]
        DOP["Dopamine =<br/>TD error"]
        REPLAY["Hippocampal replay<br/>grid cells"]
        GW["Global workspace"]
        SPARSEB["Sparse coding"]
        NMOD["Neuromodulation<br/>uncertainty gating"]
    end

    subgraph FRONT["05 Frontiers"]
        WM["World models<br/>Dreamer - JEPA"]
        ACTINF["Active inference"]
        ZOO["Architecture zoo<br/>Mamba - KAN - TTT"]
        AGENTS["LLM agents<br/>memory - tools - reflection"]
        SELF["Self-improvement<br/>STaR - Absolute Zero"]
        OVERSIGHT["Scalable oversight<br/>debate - weak-to-strong"]
    end

    ENTROPY --> SSL
    ENTROPY --> PC
    IB --> SPARSEB
    SCALE --> TRF
    GROK --> ICL
    CRIT --> NEURO
    NFL --> ARCH
    BACKPROP --> TRF
    ARCH --> TRF
    SSL --> TRF
    RL --> RLHF
    RL --> RLVR
    SEARCH --> TTC
    DOP --> RL
    REPLAY --> RL
    PC --> SSL
    SPARSEB --> INTERP
    GW --> AGENTS
    NMOD --> SELF
    PC --> ACTINF
    TRF --> AGENTS
    WM --> ACTINF
    SEARCH --> WM
    RL --> SELF
    RLVR --> SELF
    ICL --> AGENTS
    INTERP --> OVERSIGHT
    SELF --> OVERSIGHT
    ZOO --> WM
```

## Five load-bearing connections (the TL;DR of the corpus)

1. **Shannon entropy ↔ cross-entropy loss ↔ free energy** (MATH → LLM/NEURO): the same quantity is minimized by the telegraph engineer, the LLM trainer, and (per Friston) the cortex. Compression is the universal objective.
2. **Dopamine ↔ Q-learning ↔ RLHF/RLVR** (NEURO → DL → LLM): the brain's reward-learning algorithm, formalized in machines, scaled with verifiable rewards to produce reasoning — and its pathologies (hacking, over-optimization) mirror addictions.
3. **Hippocampal replay ↔ experience replay ↔ agent memory** (NEURO → FRONT): memory is an active, prioritized, structuring process, not a log. Sleep ≈ consolidation phases for continual systems.
4. **AlphaGo's search ↔ test-time compute ↔ world models** (DL/LLM → FRONT): learned priors + explicit search at decision time — first in games, now in token space, next inside learned world models.
5. **Sparse coding ↔ superposition ↔ interpretability** (NEURO ↔ LLM): two substrates independently converged on packing more concepts than units via sparse geometry — and both needed dictionary methods to decode what they stored.
