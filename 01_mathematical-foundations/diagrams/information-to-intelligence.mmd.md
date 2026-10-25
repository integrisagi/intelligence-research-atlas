# Diagram — From Information Theory to Artificial Intelligence

How the mathematical lineage flows from 1948 information theory to modern LLM objectives. (Mermaid renders in Obsidian/GitHub.)

```mermaid
graph LR
    subgraph FOUNDATIONS["Foundations (1936–1965)"]
        TURING["Turing 1936<br/>Computability"]
        SHANNON["Shannon 1948<br/>Entropy & Coding"]
        KOLMO["Kolmogorov / Solomonoff<br/>Shortest program = understanding"]
        MDL["Rissanen 1978<br/>Minimum Description Length"]
    end

    subgraph LEARNING_THEORY["Learning Theory (1971–1996)"]
        VC["Vapnik–Chervonenkis<br/>Capacity control"]
        PAC["Valiant 1984<br/>PAC learnability"]
        NFL["Wolpert 1996<br/>No Free Lunch<br/>→ inductive bias required"]
    end

    subgraph DEEP_THEORY["Deep Learning Theory (2017–2026)"]
        ZHANG["Zhang 2017<br/>Random labels fit<br/>→ classical theory broke"]
        DD["Belkin 2019<br/>Double descent"]
        NTK["Jacot 2018 / Chizat 2019<br/>Lazy vs Rich regimes"]
        IB["Tishby 1999–2015<br/>Information Bottleneck"]
    end

    subgraph SCALING["Scaling Science (2020–2026)"]
        KAPLAN["Kaplan 2020<br/>Power laws"]
        CHIN["Chinchilla 2022<br/>20 tokens/param"]
        LIMIT["Limit theory<br/>2025–2026"]
    end

    subgraph PRACTICE["What LLMs Actually Do"]
        CE["Cross-entropy loss<br/>= expected code length"]
        COMPRESS["Pretraining<br/>= massive compression"]
        PREDICT["Next-token prediction<br/>= Solomonoff approximation"]
    end

    TURING --> KOLMO
    SHANNON --> MDL
    SHANNON --> CE
    KOLMO --> PREDICT
    MDL --> IB
    VC --> ZHANG
    PAC --> NFL
    NFL --> ZHANG
    ZHANG --> DD
    ZHANG --> NTK
    IB --> PREDICT
    DD --> KAPLAN
    KAPLAN --> CHIN
    CHIN --> LIMIT
    CE --> COMPRESS
    COMPRESS --> PREDICT
```

**Reading the map:** the top route (Shannon → MDL → IB) says *learning is compression*; the middle route (VC → Zhang → double descent) says *why deep nets surprised classical theory*; the bottom converges on scaling science, which turned compression into an engineering discipline.

Related: [scaling-emergence-grokking.mmd.md](scaling-emergence-grokking.mmd.md) · Cross-links to domain 03 (applied scaling) and domain 05 (AIXI-style definitions of intelligence).
