# Adaptive Systems — Distilled Findings

How production code changes its own behavior based on the resources it gets: memory pressure, CPU quota, load. This is the "dynamic code" corpus — every finding is verified against official docs, papers, or source. Implementable versions of these live in [patterns.md](patterns.md). Compiled 2026-10-25.

---

## F1 — Memory pressure is a typed signal with a graded response

**Claim:** Chromium broadcasts pressure at three levels — NONE ("no problems"), MODERATE ("modules are advised to free buffers that are cheap to re-allocate and not immediately needed"), CRITICAL ("modules are advised to free all possible memory") — while "individual modules will implement their own policy." Android's `onTrimMemory` does the same keyed to kill-order position: at `TRIM_MEMORY_BACKGROUND` "release any resources that can be rebuilt quickly when the app returns to the foreground."

**Evidence:** [memory_pressure_level.h](https://raw.githubusercontent.com/chromium/chromium/main/base/memory/memory_pressure_level.h), [memory_pressure_listener.h](https://raw.githubusercontent.com/chromium/chromium/main/base/memory/memory_pressure_listener.h) (GetMemoryLimit maps NONE→100%, MODERATE→50%, CRITICAL→0%); [ComponentCallbacks2](https://developer.android.com/reference/android/content/ComponentCallbacks2).

**Why it's efficient:** A cheap signal converts OS OOM-kills into voluntary eviction — shedding half your cache beats being killed and cold-starting. One expensive probe (OS signals) fans out to N subsystems; each owns its eviction policy because only it knows what's cheap to rebuild.

**How to apply:** Expose a process-wide pressure bus with two actionable levels; register each cache/buffer with a "cheap-to-free" tier and an "everything" tier. → [patterns.md P1](patterns.md)

---

## F2 — Soft limits beat hard limits: degrade before you die

**Claim:** cgroups v2 has both: `memory.max` ("memory usage hard limit … the OOM killer is invoked in the cgroup") and `memory.high` ("memory usage throttle limit. If a cgroup's usage goes over the high boundary, the processes of the cgroup are throttled and put under heavy reclaim pressure … going over the high limit never invokes the OOM killer"). `memory.pressure` exposes PSI stall information.

**Evidence:** [kernel.org cgroup-v2 admin guide](https://docs.kernel.org/admin-guide/cgroup-v2.html).

**Why it's efficient:** The soft limit converts an impending kill into CPU-costed reclaim — the workload slows instead of losing state. "Degrade before die" is exactly the behavior an adaptive system wants; a hard-only setup skips straight to data loss.

**How to apply:** Run workloads with `memory.high` a few percent below `memory.max`; read `memory.pressure` stalls to trigger in-process cache shedding.

---

## F3 — Container-aware runtimes: honor the envelope you're given

**Claim:** Go 1.25's runtime "considers the CPU bandwidth limit of the cgroup containing the process" and "periodically updates GOMAXPROCS if … the cgroup CPU bandwidth limit change[s]." Before that, uber-go/automaxprocs fixed it at library level — its README shows a benchmark where matching a 2-core quota on a 24-core host gave 44,715 RPS / 26.38 ms P99.9 versus the default's 22,191 RPS / 76.19 ms. The JVM since JDK 10 detects containers by default (`UseContainerSupport`), computing "number_of_cpus() = cpu_quota() / cpu_period()" and sizing heap via `MaxRAMPercentage`.

**Evidence:** [go.dev/doc/go1.25](https://go.dev/doc/go1.25); [automaxprocs README](https://raw.githubusercontent.com/uber-go/automaxprocs/master/README.md); [JDK-8146115](https://bugs.openjdk.org/browse/JDK-8146115), [JDK-8196595](https://bugs.openjdk.org/browse/JDK-8196595).

**Why it's efficient:** A process on a 24-core host with a 2-core quota runs 24 threads into a 2-core pipe — the CFS quota runs out mid-period and every thread freezes until the next period. Uber's numbers are the cost of ignoring the envelope: same hardware, half the throughput, triple the tail latency, fixed by a one-line import.

**How to apply:** Derive every pooled-resource count (threads, workers, DB pool) from the cgroup quota, and re-derive periodically — limits change on live containers.

---

## F4 — The boot-time budget pattern: measure the environment once, derive everything

**Claim:** The recurring shape across Go, JVM, automaxprocs, and the browser APIs: at startup, read the actual resource envelope (cgroup files, `navigator` hints), then set every internal budget — thread counts, heap, cache size, batch size — as a function of that envelope.

**Evidence:** Synthesis of [go.dev/doc/go1.25](https://go.dev/doc/go1.25), [automaxprocs](https://raw.githubusercontent.com/uber-go/automaxprocs/master/README.md), [JDK-8196595](https://bugs.openjdk.org/browse/JDK-8196595), [cgroup-v2](https://docs.kernel.org/admin-guide/cgroup-v2.html), [hardwareConcurrency](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/hardwareConcurrency), [Device Memory](https://www.w3.org/TR/device-memory/).

**Why it's efficient:** Every internal pool is a guess about available resources; deriving it from the measured envelope replaces the worst-case guess with the actual constraint, at zero per-request cost.

**How to apply:** On boot compute `{cpu_limit, mem_limit}`; set `workers = f(cpu_limit)`, `caches = g(mem_limit) − headroom`, `batches = h(cpu_limit)`. → [patterns.md P2](patterns.md)

---

## F5 — Clients adapt to coarse device classes, not measured devices

**Claim:** `navigator.hardwareConcurrency` returns "the number of logical processors available" as a *hint* ("don't treat this as an absolute measurement") — MDN's example sizes a worker pool from it. The Device Memory API reports RAM in GiB "rounded to a single significant bit" to reduce fingerprinting; its example gates features: `if (mem && mem < 2) { // disable features }`. `performance.memory` exposed the page's own heap (`jsHeapSizeLimit`) for self-observation, now replaced by `performance.measureUserAgentSpecificMemory()`.

**Evidence:** [MDN hardwareConcurrency](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/hardwareConcurrency), [W3C Device Memory](https://www.w3.org/TR/device-memory/), [MDN performance.memory](https://developer.mozilla.org/en-US/docs/Web/API/Performance/memory).

**Why it's efficient:** One coarse integer classifies the device class, so payload size (images, bundles, prefetch depth, worker counts) is cut *before* the client pays the memory/CPU cost. Coarseness is the privacy tradeoff; adaptation only needs the coarse answer.

**How to apply:** Branch resource quality on a device class; always define a default for platforms that don't report it; watch your own heap growth to trigger internal compaction.

---

## F6 — Static concurrency limits fail; adapt from your own no-load latency

**Claim:** Netflix's concurrency-limits README: limits sized via Little's Law ("Limit = Average RPS × Average Latency") "quickly go out of date and the service falls over by becoming non-responsive as it is unable to gracefully shed excess load." The fix borrows from TCP Vegas: `GradientLimit` computes a gradient from minimum-RTT over current RTT — capped (`Math.max(0.5, Math.min(1.0, rttTolerance * rttNoLoad / rtt))`, "don't allow it to be reduced by more than half to avoid aggressive load-sheding due to outliers") — then `newLimit = estimatedLimit * gradient + queueSize` with a "queue of square root of the current limit."

**Evidence:** [concurrency-limits README](https://raw.githubusercontent.com/Netflix/concurrency-limits/master/README.md), [GradientLimit.java](https://raw.githubusercontent.com/Netflix/concurrency-limits/master/concurrency-limits-core/src/main/java/com/netflix/concurrency/limits/limit/GradientLimit.java).

**Why it's efficient:** The fixed-limit failure mode is a queue-latency explosion: at demand L+ε, the queue grows without bound — throughput doesn't rise, latency does, clients time out and retry into the same queue. minRTT is a built-in measurement of your own no-load system, so `rtt/minRTT` is a dimensionless queueing indicator needing no configured threshold.

**How to apply:** Replace `maxConcurrentRequests` constants with an adaptive limiter; treat rejection (429/UNAVAILABLE) as the designed overload response. → [patterns.md P3](patterns.md)

---

## F7 — Tail latency compounds: hedge and tie instead of provisioning away variance

**Claim:** The Tail at Scale (Dean & Barroso, CACM 2013): with per-server p99 = 1 s, "if a user request must collect responses from 100 such servers in parallel, then 63% of user requests will take more than one second." Hedged requests — a duplicate sent after the p95 delay, cancel on first response — cut a 1,000-key BigTable read's p99.9 "from 1,800ms to 74ms while sending just 2% more requests." Tied requests broadcast to replicas with "<1%" disk overhead; micro-partitioning ("an average of, say, 20 partitions per machine … shed load in roughly 5% increments") makes rebalancing cheap; selective replication copies observed-hot items.

**Evidence:** [The Tail at Scale PDF (barroso.org)](https://www.barroso.org/publications/TheTailAtScale.pdf), [research.google abstract](https://research.google/pubs/the-tail-at-scale/).

**Why it's efficient:** Tail probability compounds across fan-out, so eliminating per-node variance is impossible while redundancy is cheap — the paper's framing is "a predictably responsive whole out of less-predictable parts," by analogy to fault-tolerant computing.

**How to apply:** For idempotent reads with wide fan-out, hedge after the request-class p95 and cancel on first response; keep shard counts per machine in the tens; replicate only observed-hot slices. → [patterns.md P6](patterns.md)

---

## F8 — Backpressure: receiver-owned credit, demand signaling, pause at the boundary

**Claim:** HTTP/2 flow control is credit-based: "receivers advertise how many octets they are prepared to receive on a stream and for the entire connection"; "a sender MUST respect flow-control limits imposed by a receiver"; the window starts at 65,535 octets. Reactive Streams: "a Subscriber MUST signal demand via `Subscription.request(long n)`" so "backpressure is an integral part of this model in order to allow the queues which mediate between threads to be bounded." Kafka consumers can `pause()` ("suspend fetching from the requested partitions") and `resume()`.

**Evidence:** [RFC 9113 §5.2](https://httpwg.org/specs/rfc9113.html); [reactive-streams-jvm](https://github.com/reactive-streams/reactive-streams-jvm); [KafkaConsumer javadoc](https://kafka.apache.org/26/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html).

**Why it's efficient:** Credit-based flow control pushes the buffering decision to the endpoint that owns the memory — a slow consumer shrinks its window and data waits at the *sender* instead of piling in unbounded receive queues. Pause/resume shifts buffering to the broker's log, the component designed for it.

**How to apply:** Never bridge an async producer to a slow consumer with an unbounded queue; grant credit only as buffers drain; pause intake rather than buffering deeper. → [patterns.md P4](patterns.md); pipelines context: [data-pipelines F7–F8](../04_data-pipelines/findings.md)

---

## F9 — Work stealing beats central queues; pools should breathe

**Claim:** Go's scheduler: G (goroutine) / M (worker thread) / P (processor); each P has a local run queue; the runtime explicitly rejected a "centralized" design because it "would hurt scalability"; idle Ps "steal a half of" a random other P's local queue (per the canonical scheduler write-up). Java's ForkJoinPool differs "mainly by virtue of employing work-stealing," and its common pool's "threads are slowly reclaimed during periods of non-use, and reinstated upon subsequent use."

**Evidence:** [runtime/proc.go](https://raw.githubusercontent.com/golang/go/master/src/runtime/proc.go), [rakyll.org/scheduler](https://rakyll.org/scheduler/), [ForkJoinPool javadoc](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ForkJoinPool.html).

**Why it's efficient:** Local queues make the common case contention-free; stealing self-corrects imbalance only when a worker is actually idle. Elastic pools convert oversupply back into CPU/power savings instead of paying peak threads forever.

**How to apply:** Structure worker systems as local deques + occasional steal; share one elastic pool per process rather than one pool per library. → [patterns.md P7](patterns.md)

---

## F10 — Caches under pressure: admit by frequency, bound by cost

**Claim:** Caffeine's W-TinyLFU admits an entry through "a small admission LRU that evicts to a large Segmented LRU if accepted by the TinyLfu admission policy," using "a 4-bit CountMinSketch, growing at 8 bytes per cache entry"; the window/main split is "adaptively determined using a hill climbing optimization." Versus plain LRU: "in typical workloads LRU is not optimal and may have a poor hit rate in cases like full scans." Variable-size items use `weigher`/`maximumWeight` so the maximum is a budget in bytes, not an entry count.

**Evidence:** [Caffeine Efficiency wiki](https://github.com/ben-manes/caffeine/wiki/Efficiency), [Eviction wiki](https://github.com/ben-manes/caffeine/wiki/Eviction).

**Why it's efficient:** One scan destroys a plain LRU (it evicts everything hot); the frequency sketch admits only entries with demonstrated popularity at ~8 bytes/entry, and the hill-climbing window re-tunes the cache when the workload shifts. Cost-based weights make the bound honest when values differ 1000×.

**How to apply:** Bound caches by weight (bytes), not count; combine an admission sketch with a small recency window so scans can't flush hot data.

---

## F11 — Resilience is a trio: breaker, jittered backoff, retry budget

**Claim:** (1) The circuit breaker is an explicit state machine — Closed ("the proxy maintains a count of the number of recent failures … within a given time period"), Open ("the request … fails immediately"), Half-Open ("a limited number of requests … are allowed to pass through" — it "helps prevent a recovering service from suddenly being flooded"). (2) AWS: "if each layer retries independently, the load on the database will increase 243x"; "the no-jitter exponential backoff approach is the clear loser"; jitter "adds some amount of randomness to the backoff to spread the retries around in time." (3) Finagle's `RetryBudget` "allows for about 20% of the total requests to be immediately retried on top of 10 retries per second," and budgets must be shared across retry filters "to prevent retry storms."

**Evidence:** [Azure circuit-breaker pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker); [AWS: Timeouts, retries and backoff with jitter](https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter), [Exponential Backoff and Jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/); [Finagle client guide](https://twitter.github.io/finagle/guide/Clients.html).

**Why it's efficient:** Fail-fast frees the caller's threads instead of holding them through timeouts; jitter de-correlates clients so retries spread into a rate the service can drain; a percentage budget makes retries self-limiting exactly when success rate drops — a degraded dependency sees its original load, not 2–5×.

**How to apply:** Wrap every remote dependency in a windowed breaker with a degraded fallback; every retry needs growth + cap + full jitter; count all layers' retries against one shared bucket. → [patterns.md P6](patterns.md)

---

## F12 — Autoscaling: CPU/memory are lagging signals; act conservatively on bad data

**Claim:** Kubernetes HPA: `desiredReplicas = ceil(currentReplicas × currentMetricValue / desiredMetricValue)`, skipping action "if the ratio is sufficiently close to 1.0 (within a configurable tolerance, 0.1 by default)"; scale-down uses a 5-minute rolling-maximum stabilization window while scale-up uses 0 seconds; on missing metrics it recomputes "more conservatively, assuming those pods were consuming 100% of the desired value in case of a scale down," and a broken metrics pipeline blocks scale-down entirely.

**Evidence:** [kubernetes.io HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/).

**Why it's efficient:** CPU/memory reflect load that already arrived and take pod-start time to act on, so the design spends its damping budget on not overreacting: asymmetric windows scale out fast but recover slowly; conservative missing-data math biases toward not shrinking capacity on bad signals.

**How to apply:** Pair lagging resource metrics with leading ones (queue depth, in-flight requests); keep scale-up faster than scale-down unless cost is the binding constraint.

---

## F13 — Every feedback controller needs damping, or it oscillates

**Claim:** Production controllers damp themselves consistently: the HPA uses a 10% deadband plus asymmetric stabilization windows; Netflix's GradientLimit caps its gradient at 0.5 ("to avoid aggressive load-sheding due to outliers") and smooths decreases ("how aggressively the estimated limit can shrink when queuing has been detected"); Gradient2 requires queueing to persist across long-vs-short EWMA divergence before acting.

**Evidence:** [HPA](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/); [GradientLimit.java](https://raw.githubusercontent.com/Netflix/concurrency-limits/master/concurrency-limits-core/src/main/java/com/netflix/concurrency/limits/limit/GradientLimit.java).

**Why it's efficient:** An undamped threshold controller actuates at full magnitude on noise, and each actuation perturbs the system (capacity changes latency), creating self-sustained oscillation. Deadband + smoothing + asymmetric speed trade a little response time for a lot of stability — the same bargain in a pod autoscaler and a concurrency limiter.

**How to apply:** Any feedback loop you write needs: a deadband, a smoothing filter (EWMA) on the error signal, and asymmetric reaction speed (fast toward safety, slow returning). → [patterns.md P9](patterns.md)

---

## F14 — Shed, don't queue; and make crash-recovery the only recovery path

**Claim:** AWS's load-shedding guidance: "when a server approaches overload, it should start rejecting excess requests so that it can focus on the requests"; "the goal of load shedding is to keep latency low for the requests that the server decides to accept"; priorities are concrete — "the most important request that a server will receive is a ping request from a load balancer," and "the service should prioritize end() requests over start() requests." And crash-only software (Candea & Fox, 2003): "crash-only programs crash safely and recover quickly. There is only one way to stop such software—by crashing it—and only one way to bring it up—by initiating recovery"; their measurements show crash restarts faster than clean reboots (e.g., JBoss 39 s vs 47 s).

**Evidence:** [AWS: Using load shedding to avoid overload](https://builder.aws.com/content/3Eun1EEyX6p2e3VYNyRLSJzLuMV/using-load-shedding-to-avoid-overload); [Crash-Only Software (USENIX HotOS IX)](https://www.usenix.org/legacy/events/hotos03/tech/full_papers/candea/candea.pdf).

**Why it's efficient:** Accept-everything turns overload into context-switch/GC thrash where nothing finishes — and retries turn shedding's short rejections into a feedback loop if not designed ("an overload creates its own feedback loop that results in overload as a steady state"). Shedding by priority keeps throughput on what matters. Dual shutdown/startup paths are rarely exercised and rot; a single crash-recover path is on the hot path of every failure and stays fast — which also makes "kill the wedged component" safe and routine.

**How to apply:** Tag requests with priority at the edge; enforce admission before expensive work; return cheap stale/cached answers for shed-able classes; persist enough state that any process can be SIGKILLed and restarted at any time. → [patterns.md P5](patterns.md)
