# VS Code Layer & Process Map

Layer gradient + process isolation (deep dive: `../vscode.md` §1–6).

```mermaid
graph TD
    subgraph "core src/vs/ — one-way imports, lint-enforced"
        CODE["code/<br/>entry points, Electron main, CLI"] 
        WB["workbench/<br/>IDE shell: Explorer, panels, notebooks"]
        ED["editor/<br/>Monaco Editor Core"]
        PL["platform/<br/>DI + base services"]
        BA["base/<br/>utilities, lifecycle, events"]
        CODE --> WB
        WB --> ED
        WB --> PL
        ED --> PL
        PL --> BA
        ED --> BA
    end

    subgraph "separate processes — sacrificial isolation"
        MH["Main process<br/>windows, spawning, supervision"]
        EH["Extension host<br/>local / web / remote<br/>3 crashes / 5 min budget"]
        SH["Shared process<br/>extension mgmt, telemetry, request"]
        PTY["Pty host<br/>terminals; heartbeat; MaxRestarts=5"]
        WT["File watcher process"]
    end

    MH --- EH
    MH --- SH
    MH --- PTY
    MH --- WT

    EX["~100 built-in extensions/<br/>git, typescript-language-features, …<br/>declarative contributes + lazy activation"]
    EX -.runs in.-> EH
```

The two orthogonal rules that compose:
1. **Imports flow downhill** (`code-import-patterns` whitelist, "do not relax") — base never imports up; each layer whitelists what it may touch.
2. **Volatile code runs sideways** — extensions, terminals, file watching, telemetry all live in separate processes with health signals and bounded restarts, so a hang degrades one feature, never the UI.
