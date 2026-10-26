# Diagram — The Neuroscience → AI Bridge

Brain mechanism on the left, engineered counterpart on the right. Solid arrows = "inspired"; dashed = "returned the favor."

```mermaid
graph LR
    subgraph BRAIN["Brain mechanisms"]
        DA["Dopamine neurons<br/>reward prediction error<br/>(Schultz 1997)"]
        RP["Hippocampal replay<br/>offline reactivation<br/>(Wilson 1994)"]
        PC["Predictive coding<br/>errors up / predictions down<br/>(Rao & Ballard 1999)"]
        SP["Sparse coding<br/>V1 receptive fields<br/>(Olshausen 1996)"]
        GC["Grid & place cells<br/>metric relational maps<br/>(Hafting 2005)"]
        GW["Global workspace<br/>bottleneck + broadcast<br/>(Dehaene 2003)"]
        CR["Criticality<br/>neuronal avalanches<br/>(Beggs & Plenz 2003)"]
        NM["Neuromodulation<br/>ACh / NE / DA gates<br/>(Yu & Dayan 2005)"]
        PF["Prefrontal meta-RL<br/>slow→fast learner<br/>(Wang 2018)"]
    end

    subgraph AI["AI counterparts"]
        TD["TD learning / RL<br/>Q-learning, RLHF, RLVR"]
        ER["Experience replay<br/>DQN buffers, prioritized replay"]
        SSL["Self-supervised losses<br/>masked & contrastive prediction"]
        SAE["Sparse autoencoders<br/>feature dictionaries"]
        AG["Agent memory & navigation<br/>vector stores, Banino 2018"]
        MOE["Router architectures<br/>MoE, shared-context agents"]
        EOCD["Edge-of-chaos dynamics<br/>init schemes, RNN tuning"]
        META["Meta-learning<br/>learned optimizers, conditioning"]
        ICL["In-context learning<br/>transformer ICL"]
    end

    DA --> TD
    RP --> ER
    PC --> SSL
    SP --> SAE
    GC --> AG
    GW --> MOE
    CR --> EOCD
    NM --> META
    PF --> ICL

    TD -.->|"dopamine dysfunction ≈ reward hacking"| DA
    SSL -.->|"ANNs predict neural activity<br/>(RSA: Kriegeskorte 2008)"| PC
    ICL -.->|"transformers as PFC hypothesis"| PF
```

**Reading:** every load-bearing AI component has a biological creditor. The return arrows are the 2020s twist: models are now good enough to serve as hypotheses about brains (findings F14).
