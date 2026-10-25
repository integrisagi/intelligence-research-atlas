# Diagram — The 2026 Agent Stack (Practical)

What every serious LLM-agent system looks like, and which paper each component descends from.

```mermaid
graph LR
    subgraph CORE["Planner core"]
        LLM["LLM / reasoning model<br/>ReAct 2022, R1-style RL 2025"]
    end

    subgraph MEMORY["Memory layers"]
        EP["Episodic store<br/>memory streams<br/>(Generative Agents 2023)"]
        RAGI["Semantic index / RAG<br/>(Lewis 2020)"]
        SKILL["Skill library<br/>verified code artifacts<br/>(Voyager 2023)"]
    end

    subgraph TOOLS["Action surface"]
        MCP["Tool protocol / function calls<br/>(Toolformer 2023, MCP 2024)"]
        CODE["Code execution sandbox"]
        ENV["Environment / browser / APIs"]
    end

    subgraph LOOP["Inner loop"]
        REFLECT["Reflection & self-critique<br/>(Reflexion 2023)"]
    end

    subgraph OUTER["Outer loop"]
        MULTI["Multi-agent orchestration<br/>router + specialists"]
        VERIFY["Verification gate<br/>tests, verifiers, human review"]
    end

    LLM --> EP
    LLM --> RAGI
    LLM --> SKILL
    LLM --> MCP
    MCP --> CODE
    CODE --> ENV
    ENV -->|"observation"| REFLECT
    REFLECT -->|"lesson"| LLM
    LLM --> MULTI
    MULTI --> VERIFY
    VERIFY -->|"pass"| OUT["Ship / act"]
    VERIFY -->|"fail"| REFLECT

    SKILL -.->|"grows monotonically"| EP
    RAGI -.->|"weights = reasoning,<br/>index = facts (dom 03 F11)"| LLM
```

**Design notes (from findings F10):**
- Spend your novelty budget on the **memory format** (what gets stored after each episode) and the **verifier quality** — those two determine whether the system compounds or plateaus.
- Skills as code (Voyager pattern) beat skills as prose: they're executable, testable, and composable.
- The reflection loop is gradient-free self-improvement; RL fine-tuning (domain 03, F4) is the weight-side complement — use both, they compose.
