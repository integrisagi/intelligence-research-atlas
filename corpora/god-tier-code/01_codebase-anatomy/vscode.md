# VS Code — Deconstruction of a Modular, Extensible Product

How Microsoft structures VS Code so a layered TypeScript core serves desktop, web, and remote from one codebase, with ~100 built-in extensions and a third-party ecosystem that cannot destabilize the editor. Every claim carries a source URL; analysis ("why this is efficient") is marked as such. Finding IDs (`V1`–`V24`) are stable for cross-referencing.

**Compiled:** 2026-10-25, from `microsoft/vscode` main (October 2026 state). **Verification gaps at the end.**

---

## 1. The core is explicitly layered — five named layers

The wiki's opening defines the whole architecture: "Visual Studio Code consists of a layered and modular `core` that can be extended using extensions. Extensions are run in a separate process referred to as the `extension host`." The core lives under `src/vs/`; built-in extensions under `extensions/`. ([Source-Code-Organization wiki](https://github.com/microsoft/vscode/wiki/Source-Code-Organization)) — `V1`

Five layers, quoted verbatim from the wiki (`V2`):

| Layer | Wiki description |
|---|---|
| `base` | "Provides general utilities and user interface building blocks that can be used in any other layer." |
| `platform` | "Defines service injection support and the base services for VS Code that are shared across layers such as `workbench` and `code`. Should not include `editor` or `workbench` specific services or code." |
| `editor` | "Monaco Editor Core." |
| `workbench` | "Hosts the Monaco Editor Core, notebooks, and custom editors and provides the framework for panels like the Explorer, Status Bar, or Menu Bar…" |
| `code` | "The entry point to the desktop app that stitches everything together, this includes the Electron main file, shared process, and the CLI for example." (plus `server`: "the entry point to our server app for remote development") |

**Inside each layer, code is organized by target runtime environment** (`V3`): "inside each layer the code is organised by the target runtime environment. This ensures that only the runtime specific APIs are used" — `common` ("only requires basic JavaScript APIs and run in all the other target environments"), `browser`, `node`, `electron-main` ("may use code from: `common`, `node`, `electron-utility`"), etc.

> **Why this is efficient (analysis):** each layer adds capability and nothing below knows anything above — so lower layers stay portable (the editor runs standalone as Monaco; base runs in a web worker) and higher layers stay replaceable. Environment coupling becomes a property of a *directory*, not scattered conditionals — which is how one codebase ships to Electron and the browser.
>
> **Steal it:** name your layers in a wiki page matching the directory tree, so reviewers can classify any file instantly; split runtime-specific code by directory prefix with a documented allowed-import chain.

## 2. Layering is machine-checked law, with a "do not relax" banner

The rule lives in a custom ESLint rule (`local/code-import-patterns`) inside [eslint.config.js](https://raw.githubusercontent.com/microsoft/vscode/main/eslint.config.js). Each directory pattern ("target") whitelists exactly what it may import ("restrictions") — a **whitelist, not a blacklist** (`V4`):

```js
{
    'target': 'src/vs/base/~',
    'restrictions': [ 'vs/base/~' ]
},
{
    'target': 'src/vs/platform/*/~',
    'restrictions': [ 'vs/base/~', 'vs/base/parts/*/~', 'vs/platform/*/~', ... ]
},
{
    'target': 'src/vs/editor/~',
    'restrictions': [ 'vs/base/~', 'vs/base/parts/*/~', 'vs/platform/*/~', 'vs/editor/~', ... ]
},
```

And the banner above the table:

```js
// !!! Do not relax these rules !!!
//
// A path ending in /~ has a special meaning. It indicates a template position
// which will be substituted with one or more layers.
//
// When /~ is used in the target, the rule will be expanded to 14 distinct rules.
```

The rule implementation ([.eslint-plugin-local/code-layering.ts](https://raw.githubusercontent.com/microsoft/vscode/main/.eslint-plugin-local/code-layering.ts)) reports violations as: `layerbreaker: 'Bad layering. You are not allowed to access {{from}} from here, allowed layers are: [{{allowed}}]'` — with `docs.url` pointing at the architecture wiki (`V5`).

> **Why this is efficient (analysis):** whitelist semantics mean adding a new import path never accidentally grants access; the `~` template expands one entry across all runtime-environment folders, so the environment rules of §1 are enforced by the same mechanism. One declarative table replaces thousands of review conversations, and the error message teaches the architecture at the moment of violation.
>
> **Steal it:** encode architecture as a `target → allowed imports` table in CI lint; put the "do not relax" banner in the file; make lint errors link the architecture doc. (Compare Chromium's DEPS: `chromium.md` §4 — same law, different grammar.)

## 3. Dependency injection: constructor injection with runtime service tokens

- The wiki states the design directly: "the code is organised around services of which most are defined in the `platform` layer. Services get to its clients via `constructor injection`." And: "a service definition is two parts: (1) the interface of a service, and (2) a service identifier — the latter is required because TypeScript doesn't use nominal but structural typing." ([wiki](https://github.com/microsoft/vscode/wiki/Source-Code-Organization)) — `V6`
- `createDecorator` is "the *only* valid way to create a ServiceIdentifier," and the `IInstantiationService` documents its ownership contract precisely — `createChild` returns a disposable child that "inherits all current services and adds/overwrites the given services"; `dispose()` will "dispose all services that this instantiation service has created … dispose all its children but not its parent … NOT dispose services-instances that this service has been created with" ([instantiation.ts](https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/instantiation/common/instantiation.ts)) — `V7`

```ts
/**
 * The *only* valid way to create a {{ServiceIdentifier}}.
 */
export function createDecorator<T>(serviceId: string): ServiceIdentifier<T> {

    if (_util.serviceIds.has(serviceId)) {
        return _util.serviceIds.get(serviceId)!;
    }

    const id = function (target: Function, key: string, index: number) {
        if (arguments.length !== 3) {
            throw new Error('@IServiceName-decorator can only be used to decorate a parameter');
        }
        storeServiceDependency(id, target, index);
    } as ServiceIdentifier<T>;
```

- **Startup-cost policy is a registration argument** (`V8`) — [extensions.ts](https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/instantiation/common/extensions.ts):

```ts
export const enum InstantiationType {
    /**
     * Instantiate this service as soon as a consumer depends on it. _Note_ that this
     * is more costly as some upfront work is done that is likely not needed
     */
    Eager = 0,

    /**
     * Instantiate this service as soon as a consumer uses it. This is the _better_
     * way of registering a service.
     */
    Delayed = 1
}
```

- **Delayed services are literally a Proxy over an idle-time value** (`V9`): "return a proxy object that's backed by an idle value. That strategy is to instantiate services in our idle time or when actually needed but not when injected into a consumer," with "empty events" queued and replayed when the service isn't instantiated yet ([instantiationService.ts](https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/instantiation/common/instantiationService.ts)).

> **Why this is efficient (analysis):** because TS types are erased at runtime, decorators give each interface a stable token — consumers import interfaces, never implementations, which is what keeps workbench importable by `code` and mockable by tests. Child containers give per-window and per-editor service scoping with tree-structured disposal. The Proxy-over-idle trick means thousands of registered services cost nothing until touched — laziness is the container's job, not every consumer's boilerplate.
>
> **Steal it:** pair every DI interface with a runtime token; make lazy-vs-eager an explicit registration argument documented with which is "the better way"; wrap cold services in a Proxy that defers construction to idle/first-access.

## 4. Lifecycle ownership: `IDisposable`, stores, and leak forensics

- The contract is one method, with concrete examples ([lifecycle.ts](https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/base/common/lifecycle.ts)) (`V10`):

```ts
/**
 * An object that performs a cleanup operation when `.dispose()` is called.
 *
 * Some examples of how disposables are used:
 *
 * - An event listener that removes itself when `.dispose()` is called.
 * - A resource such as a file system watcher that cleans up the resource when `.dispose()` is called.
 * - The return value from registering a provider. When `.dispose()` is called, the provider is unregistered.
 */
export interface IDisposable {
    dispose(): void;
}
```

  A built-in tracker defines the leak: "a disposable is considered leaked if it is not disposed or not registered as the child of another disposable" — and a GC-based tracker logs `[LEAKED DISPOSABLE]` with the creation stack (`V10`).
- Ownership discipline (`V11`): the `Disposable` base class owns a private store; `_register` throws `'Cannot register a disposable on itself!'`; `DisposableStore` is "the preferred way to manage multiple disposables … safer to work with than an `IDisposable[]`," and after dispose, "any future disposables added to this object will be disposed of on `add`." Escape hatches are explicit and greppable: `markAsSingleton` ("indicates that the given object is a singleton which does not need to be disposed") and `MutableDisposable.clearAndLeak()` ("clears the value, but does not dispose it").

> **Why this is efficient (analysis):** the store-then-forget pattern (every listener you acquire goes into a store; cleanup happens top-down) eliminates the per-listener try/finally boilerplate that produces leaks. One uniform interface lets containers dispose entire subtrees deterministically, and the dev-mode tracker converts "who leaked?" archaeology into a stack trace at the allocation site.
>
> **Steal it:** adopt a base class with a `_register` sink plus a store type that stays safe after dispose; require explicit `markAsSingleton`/`leak()` for the two legitimate exceptions; ship a stack-on-create tracker in dev builds.

## 5. Events: a callable with lazy creation and leak telemetry

`Event<T>` is "an event with zero or more parameters that can be subscribed to. The event is a function itself," optionally taking a disposables sink; `Emitter` exposes it with a documented sample ([event.ts](https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/base/common/event.ts)) (`V12`):

```ts
export interface Event<T> {
    (listener: (e: T) => unknown, thisArgs?: any, disposables?: IDisposable[] | DisposableStore): IDisposable;
}
```

Subscription machinery is lazy (`get event(): Event<T> { this._event ??= (callback, ...) => {...} }`) and carries first-class leak forensics: "potential listener LEAK detected, having N listeners already. MOST frequent listener (…)", `ListenerRefusalError` ("REFUSES to accept new listeners because it exceeded its threshold by far"), warnings "whenever an emitter with listeners is disposed. That is a sign of code smell," and buffered-event leak warnings.

> **Why this is efficient (analysis):** an `Event` costs nothing until someone subscribes (lazy `??=`); the `disposables` parameter makes register-and-cleanup one call; and because emitters are everywhere, threshold warnings catch the listener-count leaks that naive emitter APIs make invisible. (The contrast with Node's EventEmitter is analysis from these facts, not a quoted design note — see gaps.)
>
> **Steal it:** model events as lazily-created callables, accept a disposable sink in the subscribe signature, add dev-only threshold warnings on listener growth.

## 6. Process architecture: isolation for everything volatile

- **The extension host is the crash boundary by design** (`V13`): hosts come in local/web/remote configurations; the docs state the rationale verbatim — "VS Code aims to deliver a stable and high performance editor to users, and misbehaving extensions should not impact the user experience. The Extension Host in VS Code prevents extensions from: * impacting startup performance * slowing down UI operations * modifying the UI." ([extension-host docs](https://code.visualstudio.com/api/advanced-topics/extension-host))
- **The host is spawned and watched** (`V14`): on desktop it's an Electron `WindowUtilityProcess` spawned by `ExtensionHostStarter` in the main process; the manager tracks `ResponsiveState` and surfaces it, rather than letting the UI silently hang.
- **Crash recovery is budgeted, then human-in-the-loop** (`V15`): `ExtensionHostCrashTracker` — `_TIME_LIMIT = 5 * 60 * 1000; _CRASH_LIMIT = 3` — restarts automatically within budget; beyond 3 crashes in 5 minutes VS Code stops and offers "Start Extension Bisect" / "Restart Extension Host" instead of crash-looping ([abstractExtensionService.ts](https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/services/extensions/common/abstractExtensionService.ts)).
- **Every heavy subsystem gets its own process + supervisor** (`V16`): the shared process hosts extension management/telemetry/request services (crash reported to the focused window); the pty host runs terminals behind a heartbeat — restarting on exit or unresponsiveness, capped at `MaxRestarts = 5`, then "ptyHost terminated unexpectedly with code N, giving up" ([ptyHostService.ts](https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/terminal/node/ptyHostService.ts)); the file watcher is likewise a separate process.

```ts
export class ExtensionHostCrashTracker {

    private static _TIME_LIMIT = 5 * 60 * 1000; // 5 minutes
    private static _CRASH_LIMIT = 3;
    ...
    public shouldAutomaticallyRestart(): boolean {
        this._removeOldCrashes();
        return (this._recentCrashes.length < ExtensionHostCrashTracker._CRASH_LIMIT);
    }
}
```

> **Why this is efficient (analysis):** out-of-process execution is the ultimate module boundary — CPU spikes, crashes, and hangs are contained to a sacrificial process while the UI keeps its frame budget. The bounded-restart pattern distinguishes one-off crashes (transparent recovery) from a permanently broken component (stop, tell the user, bisect to the culprit) — the same supervisor shape as Chromium's renderer respawn (§1 of `chromium.md`) with an added crash-loop budget.
>
> **Steal it:** put untrusted/volatile plugins in a worker process behind RPC with three guarantees (no UI access, no startup cost, survivable crash); supervise native/heavy subsystems with health signals + capped restarts; expose worker health as explicit state instead of hanging silently.

## 7. The API is a contract with a published no-breakage guarantee

- **One reviewable surface** (`V17`): the stable API is a single `vscode.d.ts` (~21,241 lines measured); experimental API lives in 184 `vscode.proposed.<name>.d.ts` files. The workflow README ([vscode-dts/README.md](https://raw.githubusercontent.com/microsoft/vscode/main/src/vscode-dts/README.md)): "don't forget that extension using proposed API cannot be published"; proposals must be enforced at runtime with `checkProposedApiEnabled`; and "production CI runs this check as the first step of `core-ci` … fails on a stale or missing registry rather than repairing it."
- **The process is explicit** (`V18`): "we iterate, both internally and externally, on API proposals before making any APIs stable"; "you cannot publish an extension that uses a proposed API. We may likely make breaking changes in the next release and we never want to break existing extensions"; finalization moves the API "from `vscode.proposed.d.ts` … into `vscode.d.ts`." The guidelines state the contract: "Breakage — we DO NOT want to break API. Therefore be careful and conservative when proposing new API. It needs to hold up in the long term." ([Extension-API-process](https://github.com/microsoft/vscode/wiki/Extension-API-process), [Extension-API-guidelines](https://github.com/microsoft/vscode/wiki/Extension-API-guidelines))

> **Why this is efficient (analysis):** backward compatibility becomes a process property, not a hope — unstable code is physically separated, cannot reach production extensions, and every shipped API change is a visible line-diff in one file. The marketplace gate enforces the contract externally.
>
> **Steal it:** publish your public API as one reviewable declaration surface; quarantine experiments in opt-in files banned from release artifacts until finalized.

## 8. The plugin surface is declarative; loading is lazy by default

**Claim** (`V19`): extensions declare `contributes` — "a set of JSON declarations that you make in the `contributes` field of the `package.json` Extension Manifest" (commands, menus, views, languages, grammars, themes, …) — and activation events decide when any code loads: "to support lazy activation of Visual Studio Code extensions (plug-ins), your extension controls when it should be loaded through a set of Activation Events"; "it is best practice to activate only when a user needs your extension"; the Markdown extension "should only be loaded when a user opens a Markdown file." ([contribution-points](https://github.com/microsoft/vscode-docs/blob/main/api/references/contribution-points.md), [activation-events](https://github.com/microsoft/vscode-docs/blob/main/api/references/activation-events.md))

> **Why this is efficient (analysis):** static JSON contributions can be read and rendered (menus, grammars, views) before any extension code runs — the cost of an installed extension is *data*, not code. "Installed" defaults to "not yet running."
>
> **Steal it:** split plugins into a declarative manifest (parsed cheaply for UI integration) plus imperative code that loads only on a declared trigger.

## 9. Startup performance is an engineered subsystem, not an aspiration

- **Named phases with blocking semantics** (`V20`) — [workbench lifecycle.ts](https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/services/lifecycle/common/lifecycle.ts): `Starting` ("doing work in this phase blocks an editor from showing to the user, so please rather consider to use `Restored` phase"), `Ready`, `Restored` ("views, panels and editors have restored"), `Eventually` ("the last phase … some time has passed (2-5 seconds)").
- **Idle scheduling as a primitive** (`V21`): `runWhenGlobalIdle` wraps `requestIdleCallback` with a `setTimeout` fallback; `IdleValue` computes lazily at idle or on first access — "everything is initialized eventually," with a deterministic sync fallback.
- **Measurement is gated on a canonical scenario** (`V22`): `StartupTimings._isStandardStartup` checks "new window (no reload) * workspace is trusted * just one window * explorer viewlet visible * one text editor (…) * cached data present (not rejected, not created)" before recording metrics; a built-in "Startup Performance" editor exposes all marks ([startupTimings.ts](https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/contrib/performance/browser/startupTimings.ts)).

> **Why this is efficient (analysis):** the phases convert "fast startup" into a scheduling API — contributions declare the latest phase they need, and the framework serializes only what must block first paint. Gating metrics on a standard scenario makes the trend line meaningful, and in-product perf views turn regressions into one-command triage.
>
> **Steal it:** define named boot phases with documented blocking semantics; centralize idle-deferral in one tested primitive; measure only canonical scenarios and expose raw marks in a debug view.

## 10. Extension everything; dead code doesn't ship

- **Core features are extensions** (`V23`): ~100 built-in extension folders include `git`, `typescript-language-features`, `css/html/json/markdown-language-features`, `npm`, `emmet`, `github-authentication`. The internal-contribution principle: "at its core, the workbench does not have direct dependencies to all these contributions. Instead, we use an internal (as opposed to real extension API) mechanism to contribute these contributions to the workbench," and "an editor can be crafted without them which results in the feature brought in being removed." ([wiki](https://github.com/microsoft/vscode/wiki/Source-Code-Organization))
- **Entry files gate the bundle** (`V24`): "only code that is referenced from the main entry files is loaded into the product. If you have a file that is otherwise not referenced in your code, make sure to add the import to your `.contribution.ts` file." Desktop/web sharing is three files: `workbench.common.main.ts`, `workbench.web.main.ts`, `workbench.desktop.main.ts`.

> **Why this is efficient (analysis):** features-as-extensions inherit lazy activation (§8), process isolation (§6), and removable-by-construction coupling — and that is exactly how the same editor core becomes the standalone Monaco Editor. Explicit entry files make the bundle the dependency graph: features cannot ship by accident, and web/desktop divergence is three small files instead of scattered ifdefs.
>
> **Steal it:** eat your own plugin API — put new features behind the same extension mechanism third parties use, with internal access through one documented API file per contribution; make feature inclusion require an import in a named entry list.

---

## What to steal — one screen

| VS Code decision | One-line essence | Deep dive |
|---|---|---|
| Five named layers | base → platform → editor → workbench → code; nothing looks up | §1 |
| Runtime dirs per layer | `common`/`browser`/`node`/… make environment coupling a directory | §1 |
| ESLint layer whitelist | Architecture = `target → allowed imports` table, "do not relax" | §2 |
| DI with runtime tokens | Interfaces + `createDecorator` tokens; child containers scope lifecycles | §3 |
| `InstantiationType` | Lazy-vs-eager is one registration argument; Proxy defers real cost | §3 |
| `IDisposable` discipline | Store-then-forget ownership; leak tracker with creation stacks | §4 |
| `Event<T>` | Lazy callable events with disposable sinks + leak telemetry | §5 |
| Extension host process | Untrusted code in a sacrificial process; responsive-state surfaced | §6 |
| Bounded crash restarts | 3 crashes / 5 min, then bisect — no crash loops | §6 |
| One API surface | Stable `vscode.d.ts` vs 184 opt-in proposal files; no-breakage guarantee | §7 |
| Declarative contributions | Manifest = data (rendered without code); activation = lazy loading | §8 |
| Boot phases + idle | Starting/Ready/Restored/Eventually; `runWhenIdle` with sync fallback | §9 |
| Entry-file gating | Only imported code ships; three entry files for desktop/web | §10 |

## Verification gaps (read before citing)

- `InstantiationType.Active` does **not** exist on current main (only `Eager`/`Delayed`); a historical variant could not be verified — treat as historical.
- The old `timerService.ts` startup-phase names 404 on main; the verified source for phases is `LifecyclePhase` in workbench `lifecycle.ts`.
- No verbatim "we don't use Node EventEmitter because…" doc exists; the comparison in §5 is analysis from verified facts (lazy `_event`, disposables parameter, leak detection).
- Historical timelines of features moving out of core were not verified from primary sources (current state is verified).
- The phrase "API throttling" was not found in docs; the verified rationale list is "impacting startup performance / slowing down UI operations / modifying the UI."
- The `~` layer-expansion count ("14 distinct rules") is quoted from the source comment but not independently counted.
- VS Code version numbers: not central to any claim; cite the repo state as "main, October 2026."

## Sources

- https://github.com/microsoft/vscode/wiki/Source-Code-Organization — §1, §3, §10 (layers, environments, DI, entry files)
- https://raw.githubusercontent.com/microsoft/vscode/main/eslint.config.js — §2 (`V4` excerpt)
- https://raw.githubusercontent.com/microsoft/vscode/main/.eslint-plugin-local/code-layering.ts — §2 (`V5`)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/instantiation/common/instantiation.ts — §3 (`V6`–`V7` excerpt)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/instantiation/common/extensions.ts — §3 (`V8` excerpt)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/instantiation/common/instantiationService.ts — §3 (`V9` excerpt)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/base/common/lifecycle.ts — §4 (`V10`–`V11` excerpt)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/base/common/event.ts — §5 (`V12` excerpt)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/base/common/async.ts — §9 (`V21`)
- https://code.visualstudio.com/api/advanced-topics/extension-host — §6 (`V13`)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/extensions/electron-main/extensionHostStarter.ts — §6 (`V14`)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/services/extensions/common/extensionHostManager.ts — §6 (`V14`)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/services/extensions/common/abstractExtensionService.ts — §6 (`V15` excerpt)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/services/extensions/electron-browser/nativeExtensionService.ts — §6 (`V15`)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/code/electron-main/app.ts — §6 (`V16`)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/code/electron-utility/sharedProcess/sharedProcessMain.ts — §6 (`V16`)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/terminal/node/ptyHostService.ts — §6 (`V16` excerpt)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vscode-dts/README.md — §7 (`V17`)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vscode-dts/vscode.d.ts — §7 (stable surface, line count measured)
- https://api.github.com/repos/microsoft/vscode/contents/src/vscode-dts — §7 (184 proposal files counted)
- https://github.com/microsoft/vscode/wiki/Extension-API-process — §7 (`V18`)
- https://github.com/microsoft/vscode/wiki/Extension-API-guidelines — §7 (`V18`)
- https://github.com/microsoft/vscode-docs/blob/main/api/references/contribution-points.md — §8 (`V19`)
- https://github.com/microsoft/vscode-docs/blob/main/api/references/activation-events.md — §8 (`V19`)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/services/lifecycle/common/lifecycle.ts — §9 (`V20` excerpt)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/contrib/performance/browser/startupTimings.ts — §9 (`V22` excerpt)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/contrib/performance/browser/perfviewEditor.ts — §9 (`V22`)
- https://github.com/microsoft/vscode/wiki/Performance-Issues — §9 (`V22`)
- https://api.github.com/repos/microsoft/vscode/contents/extensions — §10 (`V23` folder listing)
