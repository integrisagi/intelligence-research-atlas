# The Big-Tech Release Pipeline

How code reaches users at Google/Meta/Microsoft scale (findings: `../findings.md` F6–F7, F13, F16–F17, F21–F22).

```mermaid
graph LR
    D["Design doc / RFC<br/>(F18–F19)"] --> C["Small CL / PR<br/>+ tests (F3, F8–F9)"]
    C --> R["Review: better &gt; perfect<br/>1-day SLO (F1–F2)"]
    R --> P["Presubmit: fast + hermetic only<br/>(F8, F11)"]
    P --> T["Trunk / master<br/>commit ≥ daily (F6)"]
    T --> F["Feature flag default OFF<br/>(F6–F7)"]
    F --> K["Canary: 1–5% + control compare<br/>auto-rollback (F16)"]
    K -->|"metrics OK"| S["Staged rollout<br/>tiered % → 100% (F7, F21)"]
    K -->|"deviation"| X["Pause + rollback<br/>error budget protects (F13)"]
    S --> ST["Stable train<br/>fixed calendar (F17, F22)"]
```

The three decouplings that make this pipeline work:
1. **Deploy ≠ release** — flags (Gatekeeper, FeatureList) let code ship dark and expose per-cohort (F6–F7).
2. **Release ≠ feature readiness** — the fixed train means missing a deadline costs weeks, not a slipped branch (F17, F22).
3. **Velocity ≠ risk** — the error budget is the shared number that decides whether to ship or freeze (F13).
