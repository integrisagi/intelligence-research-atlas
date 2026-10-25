# Diagram — The Predictive Processing / Active Inference Loop

```mermaid
graph TD
    subgraph HIERARCHY["Cortical hierarchy (3 levels shown)"]
        H1["High level<br/>abstract causes<br/>priors: context, goals"] -->|"predictions DOWN"| H2["Mid level<br/>objects & dynamics"]
        H2 -->|"predictions DOWN"| H3["Low level<br/>sensory features"]
        H3 -->|"prediction ERRORS UP"| H2
        H2 -->|"prediction ERRORS UP"| H1
    end

    SENS["Sensory input"] --> CMP["Compare: input vs prediction"]
    CMP -->|"mismatch"| H3
    H3 --- CMP

    H1 -.->|"precision weighting<br/>≈ uncertainty gating<br/>(ACh expected / NE unexpected — Yu & Dayan 2005)"| CMP

    MEM["Memory & context<br/>(hippocampal priors)"] --> H1

    subgraph ACTION["Active inference (Friston 2012)"]
        A1["Prediction error about<br/>future sensory states"] --> A2["Act to make prediction true<br/>(reflex arc logic)"]
        A2 --> ENV["Environment"]
        ENV --> SENS
    end

    H1 --> A1

    UPD["Weight updates<br/>minimize long-run surprise<br/>= free energy"] 
    H2 --> UPD
    UPD --> H1
```

**Parallels to keep in mind:**
- *Predictions down* ≈ generative model; *errors up* ≈ the only signal that travels — the brain's bandwidth budget is spent on surprise, exactly like loss-weighted training and attention.
- *Precision weighting* ≈ learned uncertainty / modality gating — when to trust which errors (cf. ACh/NE neuromodulation).
- *Active inference* closes perception into action: organisms reduce prediction error by ACTING on the world — the philosophical core of world-model agents (domain 05, Dreamer/JEPA/active-inference agents).
- *Weight updates* ≈ learning as slow free-energy minimization vs perception as fast inference — the same objective at two timescales (amortized inference in ML terms).
