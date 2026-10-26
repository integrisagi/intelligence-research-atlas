# The Adaptive Loop

Every adaptive behavior in this corpus is the same loop with different sensors and actuators (findings: `../findings.md`, patterns: `../patterns.md`).

```mermaid
graph TD
    ENV["Environment<br/>cgroup limits · device class · load · memory pressure"]
    SENSE["Measure once at boot (P2)<br/>+ re-read periodically<br/>+ observe own RTT/queue/heap"]
    DAMP["Damp the signal (P9)<br/>EWMA · deadband 10% · asymmetric windows"]
    DECIDE["Decide (P3 · P5 · P8)<br/>gradient limit · priority shed · deadline check"]
    ACT["Actuate (P1 · P4 · P7)<br/>trim caches · pause intake · resize pool · reject 429"]
    RECOVER["Recover bounded (F5, F14)<br/>breaker half-open · crash-only restart"]

    ENV --> SENSE
    SENSE --> DAMP
    DAMP --> DECIDE
    DECIDE --> ACT
    ACT --> RECOVER
    RECOVER --> SENSE
    ACT -. "actuation perturbs the system —<br/>undamped loops oscillate (F13)" .-> SENSE
```

The four invariants across every verified system:
1. **Degrade before die** — soft limits, pressure levels, shedding: latency is recoverable, state loss is not (F1, F2, F14).
2. **Signals are typed and coarse** — NONE/MODERATE/CRITICAL, device classes, windowed failure counts. Precision lives in the component's local policy (F1, F5).
3. **Controllers are damped** — deadband + EWMA + asymmetric speed, or they oscillate themselves to death (F13).
4. **Rejection is designed** — 429 with `Retry-After`, jittered and budgeted, is the overload response; hidden queues are the bug (F6, F11, F14).
