# Diagram — Scaling, Emergence, and Grokking (three faces of phase changes)

```mermaid
graph TD
    subgraph SCALING["Scaling Laws — smooth power laws"]
        S1["Loss ∝ N^-α, D^-β, C^-γ<br/>(Kaplan 2020)"] --> S2["Compute-optimal balance<br/>~20 tokens / parameter<br/>(Chinchilla 2022)"]
        S2 --> S3["Data wall: value of repeats<br/>dies after ~4 epochs<br/>(Muennighoff 2023)"]
        S3 --> S4["Mechanistic origin:<br/>superposition of features<br/>(NeurIPS 2025)"]
    end

    subgraph EMERGENCE["Emergence — apparent thresholds"]
        E1["Ability absent at small scale"] --> E2{"Sharp jump above<br/>parameter threshold?"}
        E2 -- "Discontinuous metric<br/>(exact match)" --> E3["MIRAGE<br/>(Schaeffer 2023)<br/>smooth under log-likelihood"]
        E2 -- "Internal mechanism flips<br/>(e.g. induction heads)" --> E4["REAL phase transition<br/>(Wei 2022 + mechanistic work)"]
    end

    subgraph GROKKING["Grokking — generalization long after overfitting"]
        G1["Phase 1: MEMORIZE<br/>train loss → 0 fast"] --> G2["Plateau: test loss stays high<br/>(hours..days of extra training)"]
        G2 --> G3["Phase 2: SNAP<br/>circuit reorganizes<br/>(Nanda 2023: Fourier algorithm)"]
        G3 --> G4["Perfect generalization<br/>+ large weight decay effect<br/>(Omnigrok 2023)"]
    end

    SCALING ~~~ EMERGENCE
    EMERGENCE ~~~ GROKKING

    G4 -.->|"same phenomenon, macro scale"| E4
    S4 -.->|"features in superposition = raw material"| G3
```

**Key insight:** all three phenomena are the same physics wearing different clothes — a system smoothly compressing until some internal structure snaps into a qualitatively better configuration. The knobs differ (scale / metrics / training time + weight decay), the pattern repeats.
