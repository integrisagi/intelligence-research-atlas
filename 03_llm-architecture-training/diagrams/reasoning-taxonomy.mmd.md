# Diagram — Reasoning & Test-Time Compute: A Taxonomy

```mermaid
graph TD
    ROOT["Test-time reasoning<br/>for LLMs"]

    ROOT --> PROMPT["Prompt-side elicitation<br/>(no extra samples)"]
    ROOT --> SAMPLE["Sample-side scaling<br/>(more parallel compute)"]
    ROOT --> SEARCH["Search-side scaling<br/>(structured exploration)"]
    ROOT --> TRAIN["Training-side origins<br/>(where it comes from)"]

    PROMPT --> COT["Chain-of-Thought 2022<br/>'think step by step'"]
    PROMPT --> DECOMP["Decomposition:<br/>least-to-most, plan-and-solve"]

    SAMPLE --> SC["Self-Consistency 2023<br/>sample k paths → vote"]
    SAMPLE --> VERIFIER["Generate-and-verify:<br/>outcome/step reward models<br/](o1/R1 style filtering)"]

    SEARCH --> TOT["Tree of Thoughts 2023<br/>LLM-value-guided BFS/DFS"]
    SEARCH --> MCTS["MCTS over tokens/steps<br/>(AlphaZero template in text)"]
    SEARCH --> AGENT["Agent loops: ReAct, Reflexion<br/>act → observe → reconsider"]

    TRAIN --> RLVR["RLVR: DeepSeek-R1 2025<br/>emergent self-verification<br/>& reflection from pure RL"]
    TRAIN --> DISTILL["R1-distillation into<br/>small open models"]
    TRAIN --> STIR["Self-improvement: STaR 2022<br/>(see domain 05)"]

    SEARCH -.->|"needs"| VERIFIER
    RLVR -.->|"dramatically improves"| SAMPLE
    RLVR -.->|"enables longer"| COT

    style RLVR fill:#f0fdf4,stroke:#15803d
    style LIMIT2[fill:#fef2f2]::hidden
```

**Two failure modes to remember** (from findings F6): (1) complexity collapse — accuracy falls off a cliff past a task-dependent depth; (2) effort collapse — models "give up" as problems near their frontier (Apple 2025). Search + verifiers + tool offload (exact arithmetic, code execution) are the practical mitigations.
