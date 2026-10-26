# Structural Principles — Distilled Findings

The transferable structure rules extracted from the codebase dissections ([01_codebase-anatomy](../01_codebase-anatomy/)) and the workflow corpus ([03](../03_engineering-workflow/)). Each finding: claim → evidence (with source) → why it's efficient → how to apply. These are the rules `PLAYBOOK.md` compresses. Compiled 2026-10-25.

---

## F1 — Dependency direction is law, and law means machine-enforced

**Claim:** In both giant codebases, "lower layers never import higher layers" is not convention — it is a build/lint failure. Chromium: DEPS files with deny-by-default prefix rules and `new_usages_require_review = True`. VS Code: an ESLint whitelist table ("!!! Do not relax these rules !!!") mapping every directory to exactly what it may import.

**Evidence:** [chromium.md §4](../01_codebase-anatomy/chromium.md) (`C12` — content/DEPS, chrome/DEPS excerpts); [vscode.md §2](../01_codebase-anatomy/vscode.md) (`V4`–`V5` — eslint.config.js, code-layering.ts).

**Why it's efficient:** Architecture that lives in documentation decays; architecture that fails the build survives thousands of contributors. Whitelist semantics mean a new import path never accidentally grants access, and the lint error message teaches the architecture at the moment of violation.

**How to apply:** Encode layering as a `target → allowed imports` table checked in CI before anything else. If your stack lacks this, a ~50-line custom lint rule is enough to start.

---

## F2 — Every seam is a contract generated from one artifact

**Claim:** Cross-process APIs in Chromium are Mojom IDL files (sandbox attributes included) that generate both client and server bindings. VS Code's entire public API is one reviewable `vscode.d.ts`; experimental API lives in 184 opt-in proposal files that cannot reach production.

**Evidence:** [chromium.md §3, §7](../01_codebase-anatomy/chromium.md) (`C9`–`C10`); [vscode.md §7](../01_codebase-anatomy/vscode.md) (`V17`–`V18`); schema parallel: [data-pipelines F9](../04_data-pipelines/findings.md).

**Why it's efficient:** One source of truth for both sides cannot drift; contracts make boundaries auditable (capability brokering), diffable (API review = line changes), and versionable (compatibility enforced at registration).

**How to apply:** Define any cross-boundary API (process, service, plugin, persistence) in one IDL/schema/declaration file; generate or mechanically check everything else; ban implementation imports across the seam.

---

## F3 — Constructor injection over singletons and globals

**Claim:** VS Code organizes services around constructor injection with runtime service identifiers (`createDecorator` is "the *only* valid way to create a ServiceIdentifier"), child containers for scoped lifecycles, and a documented dispose contract. Chromium's component build doc warns that cross-component globals "will get duplicated which will wreak havoc."

**Evidence:** [vscode.md §3](../01_codebase-anatomy/vscode.md) (`V6`–`V7`); [chromium.md §5](../01_codebase-anatomy/chromium.md) (`C14`).

**Why it's efficient:** Injected dependencies are substitutable in tests and scoping containers, so per-window/per-editor service sets are trivial; singletons make lifecycles global and tests brittle. Globals also break once two instances of your "singleton" must coexist (two windows, two tenants, two processes).

**How to apply:** Every service: interface + injection token + constructor parameter. Register in a container that supports child scopes. Singletons only for genuinely global, stateless utilities — and say so in one place.

---

## F4 — Volatile code belongs in sacrificial processes

**Claim:** Chromium's two stated reasons for multi-process design are crash isolation and security sandboxing ("nearly impossible to build a rendering engine that never crashes or hangs … perfectly secure"). VS Code runs extensions in a dedicated host so "misbehaving extensions should not impact the user experience," preventing them from "impacting startup performance," "slowing down UI operations," and "modifying the UI."

**Evidence:** [chromium.md §1](../01_codebase-anatomy/chromium.md) (`C1`–`C2`); [vscode.md §6](../01_codebase-anatomy/vscode.md) (`V13`).

**Why it's efficient:** An OS process is the only module boundary that contains hangs, crashes, and memory corruption with zero cooperation from the buggy code. The UI keeps its frame budget no matter what the volatile subsystem does.

**How to apply:** Put untrusted input parsers, plugins, and native/heavy subsystems behind RPC in worker/utility processes. The host contract: no shared UI, no startup cost, crash survivable.

---

## F5 — Recovery is bounded: restart within budget, then stop and diagnose

**Claim:** Chromium respawns crashed renderers mechanically ("sad tab" + fresh process). VS Code's `ExtensionHostCrashTracker` auto-restarts until 3 crashes in 5 minutes, then stops and offers Extension Bisect; the pty host restarts on heartbeat loss capped at `MaxRestarts = 5`.

**Evidence:** [chromium.md §1](../01_codebase-anatomy/chromium.md) (`C4`); [vscode.md §6](../01_codebase-anatomy/vscode.md) (`V15`–`V16`).

**Why it's efficient:** Unbounded retries hide permanent breakage behind crash loops; a sliding-window budget separates transient faults (recover silently) from broken components (surface + bisect). Supervision is uniform: watch the channel, respawn on failure, count the crashes.

**How to apply:** Every restartable component gets a health signal, a restart counter with a time window, and a deterministic fallback flow that isolates the culprit.

---

## F6 — Lifecycle ownership is explicit: one dispose contract, stores, leak forensics

**Claim:** VS Code's `IDisposable` is a one-method contract; `Disposable` base classes own private stores; `_register` throws on self-registration; `DisposableStore` stays safe after dispose ("any future disposables added … will be disposed of on `add`"); leak trackers log `[LEAKED DISPOSABLE]` with the creation stack. Escape hatches (`markAsSingleton`, `clearAndLeak`) are explicit and greppable.

**Evidence:** [vscode.md §4](../01_codebase-anatomy/vscode.md) (`V10`–`V11`).

**Why it's efficient:** Store-then-forget ownership eliminates per-listener try/finally boilerplate — the code that leaks when forgotten. Creation-stack forensics turns leak debugging from production archaeology into a dev-mode stack trace.

**How to apply:** Adopt one ownership pattern (own + store + dispose top-down), one leak definition ("not disposed and not adopted"), and a dev-only tracker. Explicit opt-outs only.

---

## F7 — Composition over inheritance; treat includes as a coupling budget

**Claim:** Chromium's style guide: "multiple inheritance and virtual inheritance are permitted in Chromium code, but discouraged — consider whether composition could solve the problem instead"; and it "prefers forward declarations to `#includes` where possible" because that "can reduce compile times and result in fewer files needing recompilation when a header changes."

**Evidence:** [chromium.md §8](../01_codebase-anatomy/chromium.md) (`C22`).

**Why it's efficient:** Deep hierarchies make ownership and lifetime illegible across team boundaries; every include is a rebuild edge in a graph that millions of lines make expensive. Composition keeps behavior local and swappable.

**How to apply:** Default to composition; require justification for inheritance beyond interfaces. In compiled languages, minimize header coupling deliberately.

---

## F8 — Choose the error model and core primitives once, project-wide

**Claim:** Chromium: "exceptions are banned by the Google Style Guide and disabled in Chromium compiles" — so errors are values (`base::expected`) and CHECKs; the RTTI ban is explicitly tied to the component build, showing style and build were chosen as one design. VS Code: one event system (`Event<T>`/`Emitter` with disposable sinks and leak telemetry), one DI pattern, one disposable contract — everywhere.

**Evidence:** [chromium.md §8](../01_codebase-anatomy/chromium.md) (`C21`); [vscode.md §4–5](../01_codebase-anatomy/vscode.md) (`V10`–`V12`).

**Why it's efficient:** Uniform primitives mean any contributor can read any subsystem without relearning its idioms; tooling-enforced decisions stay out of review debates. Mixed error models (exceptions + error codes + null) multiply control-flow states per call site.

**How to apply:** Decide once: error model, event pattern, ownership pattern, async model. Encode in compiler flags/lint/templates. Write the motivation into the guide so it survives personnel change.

---

## F9 — One scheduler, declared traits; ownership transfers by message

**Claim:** Chromium: "exactly one instance per Chrome process" thread pool; `TaskTraits` "encapsulate information about a task that helps the thread pool make better scheduling decisions" (priority, may-block); "usage of locks is discouraged in Chrome. Sequences inherently provide thread-safety"; posting a task and its execution are in a happens-before relationship.

**Evidence:** [chromium.md §6](../01_codebase-anatomy/chromium.md) (`C15`–`C16`).

**Why it's efficient:** A single scheduler with declared task metadata can globally prioritize user-visible work and size concurrency to the machine; sequence-based ownership (one logical thread per object) eliminates data races and lock-ordering bugs by construction rather than discipline.

**How to apply:** Funnel background work through one pool with metadata (priority, blocking-ness); give mutable objects a home sequence and assert it; pass ownership by posting, not by sharing.

---

## F10 — Reuse is governed: two real consumers or it doesn't get extracted

**Claim:** Chromium's components layer: "code must be needed in at least 2 places"; "a component should not be added just to separate it from other code in the same layer"; "we prefer fewer top level components." VS Code: first-party features ship as extensions (git, TypeScript, language features) — "eat your own plugin API."

**Evidence:** [chromium.md §9](../01_codebase-anatomy/chromium.md) (`C23`); [vscode.md §10](../01_codebase-anatomy/vscode.md) (`V23`).

**Why it's efficient:** Speculative abstraction is the leading cause of modular rot — layers nobody use accrete wrong assumptions. The two-consumer rule forces abstractions to be extracted from real usage; dogfooding the plugin API keeps it honest because first-party features exercise it continuously.

**How to apply:** Extract on the second consumer, not the first guess. Route first-party features through the same extension/plugin mechanism third parties use.

---

## F11 — Dead code doesn't ship: inclusion is an explicit, reviewable act

**Claim:** VS Code: "only code that is referenced from the main entry files is loaded into the product"; desktop/web divergence is three entry files (`workbench.common/web.desktop.main.ts`). Chromium: component build (many shared libraries, dev) vs static build (one binary, release) over identical sources; components sized "several dozen to several hundred files."

**Evidence:** [vscode.md §10](../01_codebase-anatomy/vscode.md) (`V24`); [chromium.md §5](../01_codebase-anatomy/chromium.md) (`C14`).

**Why it's efficient:** When the entry list is the unit of product surface, features can't ship by accident, bundle bloat is reviewable as a diff, and dev/release shapes can differ without forking source.

**How to apply:** Require an explicit import in a named entry file for anything to reach the build; review entry-file changes as product decisions.

---

## F12 — Deny by default, everywhere

**Claim:** The pattern recurs at every scale: DEPS include rules (`-content` then `+content/public/common`); chrome/DEPS banning intra-chrome reach-through (`-chrome`); Chromium's `BrowserInterfaceBroker` terminating renderers that request unregistered interfaces ("results in a … termination of the renderer"); VS Code's import whitelist; VS Code's proposed-API gate (cannot be published).

**Evidence:** [chromium.md §3–4](../01_codebase-anatomy/chromium.md) (`C10`, `C12`); [vscode.md §2, §7](../01_codebase-anatomy/vscode.md) (`V4`, `V18`).

**Why it's efficient:** Deny-by-default means every capability grant is an explicit, auditable line — new access never happens by accident, and audits have a single place to look. Allowlist-by-default systems fail open under change.

**How to apply:** For permissions, imports, network egress, plugin capabilities: default deny, require an explicit registered grant, and fail closed (terminate/refuse) on unregistered requests.

---

## F13 — Schemas first: data crossing boundaries has a versioned, checked definition

**Claim:** Chromium's Mojom files define messages with type evolution in mind; VS Code freezes the extension API in `vscode.d.ts` with a published no-breakage guarantee ("We DO NOT want to break API"); the data world enforces the same idea via Schema Registry compatibility modes (BACKWARD/FORWARD/FULL, checked at registration).

**Evidence:** [chromium.md §3](../01_codebase-anatomy/chromium.md) (`C9`); [vscode.md §7](../01_codebase-anatomy/vscode.md) (`V18`); [data-pipelines F9](../04_data-pipelines/findings.md).

**Why it's efficient:** Schemas make evolution a checked, mechanical act — a breaking change becomes a rejected registration instead of a production incident. Producers and consumers can then deploy independently.

**How to apply:** Any persisted or transmitted structure gets a versioned schema with declared compatibility rules; wire the compatibility check into CI.

---

## F14 — Incrementalism is designed in: same code, many shapes; phased conversion

**Claim:** Chromium: component vs static builds flip on a GN flag over identical sources; servicification converts subsystems "piece-by-piece" with named strategies ("build on existing code, convert clients one-by-one"); in/out-of-process execution is a runtime choice with client code unchanged. Site isolation itself shipped in stages (Chrome 67 → 77 → 92) keyed to exposure and device constraints. Mojo hid the pipe endpoint's location precisely so components could move without client changes.

**Evidence:** [chromium.md §5, §9, §10, §2–3](../01_codebase-anatomy/chromium.md) (`C14`, `C24`, `C7`, `C8`).

**Why it's efficient:** Architectures that only support big-bang migration never get migrated; phased strategies with stable interfaces let a 40M-line system change while always shippable. Runtime shape (in-process vs not) as configuration decouples topology from code.

**How to apply:** Design seams so the same interface works local and remote; plan conversions in named phases; ship hardening in stages keyed to exposure; make topology a deployment decision, not a code change.
