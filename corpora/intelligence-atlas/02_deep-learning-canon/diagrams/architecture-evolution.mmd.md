# Diagram — Architecture Evolution: 1943 → 2017

Each node is an architectural idea; arrows mean "enabled" or "fixed a limitation of."

```mermaid
graph LR
    MP["McCulloch–Pitts 1943<br/>neuron = logic gate"] --> PERC["Perceptron 1958<br/>learnable weights"]
    PERC --> XOR["Minsky–Papert 1969<br/>XOR limits → winter"]
    XOR -.->|"17 years later"| BP["Backprop 1986<br/>hidden layers trainable"]
    BP --> CNN["LeNet 1989–98<br/>weight sharing = vision prior"]
    BP --> VG["Vanishing gradients 1991<br/>depth problem named"]
    VG --> LSTM["LSTM 1997<br/>gated memory cells"]
    CNN --> ALEX["AlexNet 2012<br/>+ GPUs + ImageNet"]
    ALEX --> RES["ResNet 2015<br/>identity paths → 100+ layers"]
    ALEX --> BN["BatchNorm 2015<br/>stable statistics"]
    LSTM --> S2S["Seq2Seq 2014<br/>encoder–decoder"]
    S2S --> ATT["Bahdanau Attention 2014<br/>dynamic alignment"]
    RES --> TRF["Transformer 2017 → domain 03"]
    BN --> TRF
    ATT --> TRF
    ALEX --> DQN["DQN 2015<br/>RL from pixels + replay"]
    DQN --> AG["AlphaGo 2016 / AlphaZero / MuZero"]
    AG -.->|"search + learned prior<br/>= 2024-26 reasoning LLMs"| TRF
    ALEX --> SSL["SimCLR/CLIP 2020-21<br/>self-supervised + multimodal"]
    SSL --> TRF
```

**Pattern to notice:** only four architectural primitives survived into the transformer era — **weight sharing, gating, normalization, identity paths** — plus attention as the fifth. Everything else was scaffolding. (See findings F2/F3.)
