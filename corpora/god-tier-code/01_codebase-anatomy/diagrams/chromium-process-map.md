# Chromium Process Map

Process boundaries as failure + trust domains (deep dive: `../chromium.md` §1–3). Mojo connects everything; the endpoint's location is hidden, so any unit can move in-process ↔ out-of-process.

```mermaid
graph TD
    B["Browser Process<br/>UI + supervision + broker<br/>(the stable kernel)"]

    R1["Renderer 1<br/>site A (sandboxed)<br/>web content"]
    R2["Renderer 2<br/>site B (sandboxed)<br/>web content"]
    G["GPU Process<br/>compositing/raster"]
    N["Utility: Network Service<br/>[ServiceSandbox=kNetwork]"]
    S["Utility: Storage Service"]

    B -- "Mojo: BrowserInterfaceBroker<br/>deny-by-default binder registry" --> R1
    B -- Mojo --> R2
    B -- Mojo --> G
    B -- Mojo --> N
    B -- Mojo --> S

    R1 -."crash → sad tab → respawn".-> B
    R2 -."crash → sad tab → respawn".-> B
```

Key rules visible in the map:
- One process per **site** (eTLD+1), not per tab — the data-policy boundary is the trust boundary.
- Renderers are assumed compromised; cross-site data only enters with CORS permission.
- All renderer→browser interface requests pass the broker; an unregistered binder **terminates the renderer** (fail closed).
- Crash recovery is mechanical: watch the channel, respawn on failure.
