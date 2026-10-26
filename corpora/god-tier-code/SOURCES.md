# SOURCES — Master Source Index

Every source used by this corpus, grouped by module. All fetched October 2026. Format: URL → what it grounded. Where a fetch had caveats (localized page, redirect, paraphrase risk), the grounding file notes it in its verification-gaps section.

Grounding law: claims that could not be verified against these sources were dropped, not guessed. Each module lists its residual gaps.

---

## 01_codebase-anatomy/chromium.md

Chromium official docs and design documents:
- https://www.chromium.org/developers/design-documents/multi-process-architecture/ — multi-process rationale, process roles, memory tradeoff, crash recovery (§1)
- https://www.chromium.org/Home/chromium-security/site-isolation/ — site definition, Spectre rationale, staged adoption (§2)
- https://raw.githubusercontent.com/chromium/chromium/main/docs/process_model_and_site_isolation.md — soft process limits, Android process handling (§1)
- https://raw.githubusercontent.com/chromium/chromium/main/mojo/README.md — Mojo primitives, zero-copy, hidden endpoint, perf comparison (§3)
- https://raw.githubusercontent.com/chromium/chromium/main/docs/mojo_and_services.md — services, broker, ServiceSandbox, fail-closed binders (§3)
- https://raw.githubusercontent.com/chromium/chromium/main/content/README.md — content API, embedder contract, DEPS-enforced layering (§4)
- https://gn.googlesource.com/gn/+/refs/heads/main/README.md (+ docs/quick_start.md, docs/faq.md) — GN meta-build, explicit spec philosophy (§5)
- https://raw.githubusercontent.com/chromium/chromium/main/docs/component_build.md — component vs static, size guidance, globals warning (§5)
- https://raw.githubusercontent.com/chromium/chromium/main/docs/threading_and_tasks.md — sequences, locks discouraged, TaskTraits, happens-before (§6)
- https://raw.githubusercontent.com/chromium/chromium/main/base/allocator/partition_allocator/PartitionAlloc.md — allocator design, security guarantees (§7)
- https://raw.githubusercontent.com/chromium/chromium/main/styleguide/c++/c++.md (+ c++-features.md, c++-dos-and-donts.md) — composition, forward decls, exceptions ban (§8)
- https://raw.githubusercontent.com/chromium/chromium/main/components/README.md — two-consumer rule, no upward deps (§9)
- https://raw.githubusercontent.com/chromium/chromium/main/docs/servicification.md — service placement, phased conversion (§9)
- https://developer.chrome.com/docs/web-platform/chrome-release-channels — channel cadences, staged rollout (§10; served localized at fetch)
- https://raw.githubusercontent.com/chromium/chromium/main/testing/variations/README.md (+ base/feature_list.h) — field trials, FeatureList priority order (§10)

Real source files fetched:
- https://raw.githubusercontent.com/chromium/chromium/main/services/network/public/mojom/network_service.mojom — `[ServiceSandbox=...]` interface (§3)
- https://raw.githubusercontent.com/chromium/chromium/main/content/DEPS — deny-by-default rules, `new_usages_require_review` (§4)
- https://raw.githubusercontent.com/chromium/chromium/main/chrome/DEPS — intra-chrome ban, blink/public carve-out (§4)
- https://raw.githubusercontent.com/chromium/chromium/main/base/memory/memory_pressure_level.h — pressure enum (§7)
- https://raw.githubusercontent.com/chromium/chromium/main/base/memory/memory_pressure_listener.h — listener contract, GetMemoryLimit (§7)

## 01_codebase-anatomy/vscode.md

VS Code wiki and docs:
- https://github.com/microsoft/vscode/wiki/Source-Code-Organization — layers, runtime dirs, DI, entry files (§1, §3, §10)
- https://github.com/microsoft/vscode/wiki/Extension-API-process — proposal stages, no-publish rule (§7)
- https://github.com/microsoft/vscode/wiki/Extension-API-guidelines — "We DO NOT want to break API" (§7)
- https://github.com/microsoft/vscode/wiki/Performance-Issues — perf tooling usage (§9)
- https://code.visualstudio.com/api/advanced-topics/extension-host — host types, stability rationale (§6)
- https://github.com/microsoft/vscode-docs/blob/main/api/references/contribution-points.md — contributes surface (§8)
- https://github.com/microsoft/vscode-docs/blob/main/api/references/activation-events.md — lazy activation (§8)

Real source files fetched (microsoft/vscode main, October 2026):
- https://raw.githubusercontent.com/microsoft/vscode/main/eslint.config.js — layer whitelist, `~` templates, "Do not relax" (§2)
- https://raw.githubusercontent.com/microsoft/vscode/main/.eslint-plugin-local/code-layering.ts — layerbreaker message (§2)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/instantiation/common/instantiation.ts — createDecorator, dispose contract (§3)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/instantiation/common/extensions.ts — InstantiationType (§3)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/instantiation/common/instantiationService.ts — Proxy-over-idle delayed services (§3)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/base/common/lifecycle.ts — IDisposable, stores, trackers (§4)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/base/common/event.ts — Event/Emitter, leak telemetry (§5)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/base/common/async.ts — runWhenGlobalIdle, IdleValue (§9)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/extensions/electron-main/extensionHostStarter.ts — host spawning (§6)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/services/extensions/common/extensionHostManager.ts — responsive state (§6)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/services/extensions/common/abstractExtensionService.ts — CrashTracker (§6)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/services/extensions/electron-browser/nativeExtensionService.ts — auto-restart, bisect (§6)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/code/electron-main/app.ts — shared process setup (§6)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/code/electron-utility/sharedProcess/sharedProcessMain.ts — shared process services (§6)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/platform/terminal/node/ptyHostService.ts — heartbeat, MaxRestarts (§6)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vscode-dts/README.md — API proposal workflow (§7)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vscode-dts/vscode.d.ts — stable API surface (21,241 lines measured) (§7)
- https://api.github.com/repos/microsoft/vscode/contents/src/vscode-dts — 184 proposal files counted (§7)
- https://api.github.com/repos/microsoft/vscode/contents/extensions — ~100 built-in extensions counted (§10)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/services/lifecycle/common/lifecycle.ts — LifecyclePhase (§9)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/contrib/performance/browser/startupTimings.ts — standard-startup checklist (§9)
- https://raw.githubusercontent.com/microsoft/vscode/main/src/vs/workbench/contrib/performance/browser/perfviewEditor.ts — perf editor (§9)

## 02_structural-principles/findings.md

Synthesis — all evidence routes through the two deep dives above, plus:
- [04_data-pipelines F9](04_data-pipelines/findings.md) (schema contracts) and [05_adaptive-systems F1](05_adaptive-systems/findings.md) (pressure signals) via their sources below.

## 03_engineering-workflow/findings.md

- https://google.github.io/eng-practices/review/reviewer/standard.html — Standard of Code Review (F1)
- https://google.github.io/eng-practices/review/reviewer/looking-for.html — reviewer checklist (F2)
- https://google.github.io/eng-practices/review/reviewer/speed.html — one-day rule (F2)
- https://google.github.io/eng-practices/review/developer/small-cls.html — small CLs (F3)
- https://research.google/pubs/why-google-stores-billions-of-lines-of-code-in-a-single-repository/ — monorepo abstract (F4)
- http://web.archive.org/web/20240229134708/https://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext — Potvin & Levenberg full text (F4–F5; daily commit counts: treat with mild caution)
- https://trunkbaseddevelopment.com/ + /feature-flags/ — trunk definition, flag debt (F6)
- https://engineering.fb.com/2017/08/31/web/rapid-release-at-massive-scale/ — Meta Gatekeeper, continuous deploy (F7, F21)
- https://abseil.io/resources/swe-book/html/ch11.html — SWE at Google ch. 11: test sizes, hermeticity, 80/15/5 (F8–F9)
- https://abseil.io/resources/swe-book/html/ch23.html — ch. 23: flaky handling, presubmit/postsubmit, build cop (F10–F11)
- https://mike-bland.com/2011/10/18/test-certified.html — Test Certified first-hand account (F12)
- https://sre.google/sre-book/embracing-risk/ — error budgets (F13)
- https://sre.google/sre-book/postmortem-culture/ — blameless postmortems (F14)
- https://sre.google/sre-book/evolving-sre-engagement-model/ (+ workbook/engagement-model/, sre-book/reliable-product-launches/) — PRR (F15)
- https://sre.google/workbook/canarying-releases/ (+ sre-book/release-engineering/) — canarying (F16)
- https://blog.chromium.org/2021/03/speeding-up-release-cycle.html — 4-week train (F17)
- https://developer.chrome.com/blog/chrome-two-week-release — 2026 two-week cadence (F17; German-localized at fetch)
- https://www.industrialempathy.com/posts/design-docs-at-google/ — design docs (F18)
- https://rust-lang.github.io/rfcs/ — RFC process (F19)
- https://engineering.fb.com/2022/11/15/open-source/sapling-source-control-scalable/ — Sapling (F20)
- https://github.com/microsoft/vscode/wiki/Development-Process — monthly milestones, endgame (F22)

## 04_data-pipelines/findings.md

- https://kafka.apache.org/43/design/design (+ /intro) — partitioned log, consumer groups, replay, retention (F1–F2)
- https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time — event time, watermarks (F3)
- https://research.google/pubs/the-dataflow-model-a-practical-approach-to-balancing-correctness-latency-and-cost-in-massive-scale-unbounded-out-of-order-data-processing/ — Dataflow Model abstract (F4)
- https://sre.google/sre-book/data-processing-pipelines/ — exactly-once, stage/worker model (F5)
- https://www.oreilly.com/radar/questioning-the-lambda-architecture/ — Kreps, Kappa (F6)
- https://www.reactive-streams.org/ + https://github.com/reactive-streams/reactive-streams-jvm — demand signaling (F7)
- https://kafka.apache.org/35/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html (+ 3.0 javadoc) — pause/resume (F8)
- https://docs.confluent.io/platform/current/schema-registry/avro.html — compatibility modes (F9)
- https://docs.getdbt.com/docs/introduction — ELT model (F10)
- https://iceberg.apache.org/ — table formats (F11)
- https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/ + https://spark.apache.org/docs/latest/streaming/index.html — engine philosophies (F12)
- https://docs.getdbt.com/docs/build/data-tests + https://docs.greatexpectations.io/docs/core/introduction/gx_overview — quality gates (F13)

## 05_adaptive-systems/findings.md

- https://raw.githubusercontent.com/chromium/chromium/main/base/memory/memory_pressure_level.h + memory_pressure_listener.h — pressure levels (F1)
- https://developer.android.com/reference/android/content/ComponentCallbacks2 — onTrimMemory (F1)
- https://docs.kernel.org/admin-guide/cgroup-v2.html — cpu.max, memory.max/high, PSI (F2, F4)
- https://go.dev/doc/go1.25 — container-aware GOMAXPROCS (F3, F4)
- https://raw.githubusercontent.com/uber-go/automaxprocs/master/README.md — throttling stats, benchmark (F3, F4)
- https://bugs.openjdk.org/browse/JDK-8146115 + JDK-8196595 — JVM container awareness (F3, F4)
- https://developer.mozilla.org/en-US/docs/Web/API/Navigator/hardwareConcurrency — worker sizing (F5)
- https://www.w3.org/TR/device-memory/ — device classes (F5)
- https://developer.mozilla.org/en-US/docs/Web/API/Performance/memory — heap self-observation (F5)
- https://raw.githubusercontent.com/Netflix/concurrency-limits/master/README.md + concurrency-limits-core/.../GradientLimit.java — adaptive limits (F6, F13)
- https://www.barroso.org/publications/TheTailAtScale.pdf — The Tail at Scale, full text (F7)
- https://research.google/pubs/the-tail-at-scale/ — official abstract (F7)
- https://httpwg.org/specs/rfc9113.html — HTTP/2 flow control (F8)
- https://raw.githubusercontent.com/golang/go/master/src/runtime/proc.go + https://rakyll.org/scheduler/ — G-M-P scheduler (F9)
- https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ForkJoinPool.html — work stealing (F9)
- https://github.com/ben-manes/caffeine/wiki/Efficiency (+ Eviction) — W-TinyLFU (F10)
- https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker — breaker state machine (F11)
- https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter + https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/ — backoff with jitter (F11; Builders' Library URLs now redirect to builder.aws.com)
- https://twitter.github.io/finagle/guide/Clients.html — RetryBudget (F11)
- https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/ — HPA algorithm, damping (F12, F13)
- https://builder.aws.com/content/3Eun1EEyX6p2e3VYNyRLSJzLuMV/using-load-shedding-to-avoid-overload — load shedding (F14)
- https://www.usenix.org/legacy/events/hotos03/tech/full_papers/candea/candea.pdf — Crash-Only Software (F14)

## Known caveats (cross-module)

- Chromium "~40M lines" and per-renderer memory budgets: not officially sourced; not asserted in findings.
- The Chrome release-channel page was served in Hindi at fetch time; cadence facts are translations (flagged in chromium.md §10).
- Some `content/DEPS` surrounding comments may be fetcher-paraphrased; rule lines verbatim.
- "Bug farm" is a common misattribution to Kreps' Lambda article — not used as a quote anywhere in this corpus.
- Netflix's gradient formula is cited from `GradientLimit.java` source, not the README (the README lacks the formula as plain text).
- Tail-at-Scale quotes come from the author-hosted PDF (barroso.org) after cacm.acm.org returned 403 — identical CACM text.
- AWS Builders' Library URLs 301 to builder.aws.com; content unchanged.
