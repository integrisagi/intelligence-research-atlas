# Where Structure Gets Enforced (It's Never in Code Review)

The pattern across both codebases: every structural law has a machine that enforces it (findings: `../findings.md` F1–F14).

```mermaid
graph TD
    subgraph Laws
        L1["Dependency direction"]
        L2["Capability grants"]
        L3["Schema evolution"]
        L4["API stability"]
        L5["Product surface"]
        L6["Resource response"]
    end
    subgraph Machines
        M1["DEPS / ESLint whitelist<br/>fails build or lint"]
        M2["Interface broker registry<br/>unregistered → terminate (fail closed)"]
        M3["Schema Registry compat check<br/>at registration, in CI"]
        M4["One .d.ts surface + CI registry check<br/>proposals banned from release"]
        M5["Entry-file imports<br/>only imported code ships"]
        M6["Typed pressure signal + local policies<br/>per-component shed"]
    end
    L1 --> M1
    L2 --> M2
    L3 --> M3
    L4 --> M4
    L5 --> M5
    L6 --> M6
```

The rule: **if a law has no machine, it is a suggestion.** Every finding in this corpus that survived at scale acquired an enforcement mechanism — deny-by-default grammar, whitelist table, registration check, bounded restart, typed signal. Code review is for judgment calls the machines can't express; everything else gets a machine.
