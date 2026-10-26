# Adaptive Systems — The Patterns

Nine implementable patterns for code that reacts to the resources it gets. Each: **Intent → Trigger signals → Pseudocode → Pitfalls**, with links to the grounding findings in [findings.md](findings.md). Pseudocode is deliberately language-neutral; translate to your stack, keep the control shape.

---

## P1 — Memory-pressure governor

**Intent:** Shed cache memory voluntarily, in ordered tiers, before the OS kills you. (F1, F2)

**Trigger signals:** OS/host pressure level (Android `onTrimMemory`, Chromium pressure levels), cgroup `memory.pressure` PSI stalls, own RSS approaching `memory.high`, or in-process heap approaching its limit.

```
# registration — each component declares what it can give up, in order of cheapness
pressure_bus.register(cache, on_moderate = cache.trim_recreatable(),
                               on_critical = cache.clear_all())
pressure_bus.register(pool,  on_moderate = pool.shrink_to_half(),
                               on_critical = pool.shrink_to_min())

# host integration — map platform signals onto the two actionable levels
on_host_signal():
    if psi_memory_stalls_10s > threshold or level == MODERATE:
        bus.broadcast(MODERATE)      # free cheap-to-reallocate buffers → target ~50%
    if rss > memory.high or level == CRITICAL:
        bus.broadcast(CRITICAL)      # free everything freeable → target ~0%
```

**Pitfalls:** Don't evict what a returning user needs first (order by cost-to-reconstruct — F1). Deduplicate repeated notifications (`ignore_repeated_notifications` exists in Chromium for a reason). Keep eviction on the component's own thread; don't broadcast from arbitrary threads.

---

## P2 — Boot-time resource budget

**Intent:** Measure the actual resource envelope once at startup; derive every pool, cache, and batch size from it. (F3, F4)

**Trigger signals:** cgroup files (`cpu.max`, `memory.max`, `memory.high`), container env, `navigator.hardwareConcurrency` / `deviceMemory`.

```
boot():
    cpu = read_cgroup("cpu.max").max / read_cgroup("cpu.max").period   # quota/period
    if cpu is None: cpu = os.cpu_count()
    mem = read_cgroup("memory.max") or navigator.deviceMemory * 1 GiB

    WORKERS      = clamp(cpu, 1, 16)                    # f(cpu_limit)
    DB_POOL      = WORKERS * per_worker_connections
    CACHE_BYTES  = mem * 0.25 - explicit_headroom()     # g(mem_limit), leave room
    BATCH_SIZE   = max(64, min(4096, cpu * 256))        # h(cpu_limit)

    # limits can change on live containers — re-read periodically (Go 1.25 does)
    every(30s): re_read_cgroups(); adjust(WORKERS, CACHE_BYTES) with_damping(P9)
```

**Pitfalls:** The Uber benchmark is the cost of skipping this: 2× throughput, 3× better P99.9 lost on identical hardware (F3). Don't trust `os.cpu_count()` / host `/proc/cpuinfo` in containers. Leave explicit headroom — a budget of 100% of the envelope means the OOM killer manages your heap for you.

---

## P3 — Gradient-based adaptive concurrency limiter

**Intent:** Replace fixed `maxConcurrent` constants with a limit that tracks your own no-load latency. (F6, F13)

**Trigger signals:** your per-request RTT samples vs. the observed minimum RTT (no-load baseline).

```
state: min_rtt = +inf, limit = initial, in_flight = 0, queue = deque()

on_request_start():  if in_flight >= limit: reject(429)   # designed overload response
                     in_flight += 1
on_request_end(rtt): in_flight -= 1
                     min_rtt = min(min_rtt, rtt)          # no-load estimate (EWMA it too)
                     gradient = clamp(rtt_tolerance * min_rtt / rtt, 0.5, 1.0)
                     queue_allowance = floor(sqrt(limit))
                     new_limit = limit * gradient + queue_allowance
                     limit = decrease_smoothed(new_limit)  # never shrink fast (F13)
                     # growth: when gradient == 1.0 for a window, allow slow increase
```

**Pitfalls:** Cap the shrink (gradient floor 0.5) — one outlier must not halve capacity (F6). Smooth decreases; only grow slowly. Reject fast with a meaningful status (429/UNAVAILABLE) and a `Retry-After` — hidden queues "you don't know about yet" (F14) are worse than visible rejection.

---

## P4 — Bounded backpressure queue (credit-based)

**Intent:** Keep every inter-stage queue bounded by construction; push pressure to the source. (F8; pipelines F7–F8)

**Trigger signals:** queue depth vs. capacity; consumer drain rate.

```
producer → [bounded channel, capacity B] → consumer

consumer_loop():
    while True:
        credit = B - in_flight                      # receiver owns the window
        channel.grant(credit)
        item = channel.receive()                    # blocks when empty — sender waits
        process(item); in_flight -= 1

# source-level variant (Kafka shape):
if sink_lag > high_watermark: consumer.pause(partitions)
when drained:                  consumer.resume(partitions)
```

**Pitfalls:** Never `queue.put` into an unbounded list "just for now" — OOM is the failure mode, not slowness (F8). Per-stream AND per-connection windows (HTTP/2 does both) so one slow stream can't starve the rest. Pausing beats unsubscribing — you keep offsets and rebalance stability.

---

## P5 — Priority load shedder

**Intent:** Under overload, reject the cheapest-to-defer work early and keep latency low for what you accept. (F14)

**Trigger signals:** admission latency, in-flight count vs. adaptive limit (P3), queue depth.

```
priorities: P0 LB health checks  >  P1 finishing in-flight work (end > start)
            >  P2 interactive     >  P3 batch/crawler/off-peak

admit(request):
    if system_overloaded() and request.priority >= P3:
        if request is cacheable: return stale_or_cached(request)   # degrade, don't error
        return reject(503, retry_after=backoff_with_jitter)
    if system_critical() and request.priority >= P2: same...
    return serve(request)          # "keep latency low for the requests we accept"
```

**Pitfalls:** Rejection causes retries — without jitter and a retry budget (P6) shedding creates "its own feedback loop that results in overload as a steady state" (F14). Classify at the edge, before expensive work. Never shed health checks or you'll be marked dead while healthy.

---

## P6 — Circuit breaker + hedged requests + jittered retries

**Intent:** Fail fast on a broken dependency, probe recovery gently, and buy tail latency with cheap redundancy. (F11, F7)

**Trigger signals:** failure count in window (breaker); latency > p95 for the request class (hedge); retryable failure (backoff).

```
# breaker — explicit state machine
CLOSED:  count failures in sliding window; if > threshold → OPEN, start timer
OPEN:    fail immediately with fallback (cached/default); on timer expiry → HALF_OPEN
HALF_OPEN: let k probes through; any failure → OPEN again; all succeed → CLOSED

# hedged read (idempotent only)
send primary; after p95(class): send hedge (tagged low-priority/preemptible)
cancel outstanding on first response          # p99.9 1800ms → 74ms for +2% load (F7)

# retry — growth + cap + FULL jitter, one shared budget
delay = random_between(0, min(cap, base * 2**attempt))
allow retry only if retry_budget.try_spend()   # budget ≈ 20% of real traffic (F11)
```

**Pitfalls:** Thresholds must count failures within a time window, not lifetime ("automatically resets at periodic intervals" — F11). Hedging non-idempotent requests duplicates side effects. Retries without a shared budget multiply across layers — AWS's 243× example (F11). Never jitter: "the clear loser."

---

## P7 — Work-stealing pool with dynamic sizing

**Intent:** Balance load without central-queue contention; let the pool breathe with demand. (F9)

**Trigger signals:** per-worker queue depth imbalance; total demand vs. cpu budget (P2).

```
each worker: local deque; take from own deque first
idle worker: 1) global queue  2) steal HALF from a random victim  3) park
busy shift:  spin briefly before parking (wakeups are cheap; parking is cheaper)

sizing: target_workers = clamp(cpu_budget(P2), current_demand)
        grow fast on backlog, shrink slowly (P9 damping); reclaim idle threads
```

**Pitfalls:** One shared queue serializes every scheduling decision — Go's runtime explicitly rejected it ("would hurt scalability," F9). Steal-half (not steal-one) or a straggler just causes churn. For divide-and-conquer CPU work, steal from the back of the victim's deque while the owner takes from the front (ForkJoinPool shape).

---

## P8 — Deadline propagation

**Intent:** Every request carries its remaining deadline downstream; work that can't finish in time is cancelled or degraded *early*, at the cheapest point. (F11, F14; Chromium's declared priorities, `chromium.md` §6)

**Trigger signals:** request entry (start clock); each hop subtracts elapsed time.

```
request.deadline = now() + budget[request.priority]
ctx = {deadline: request.deadline, priority: request.priority}

downstream_call(ctx):
    if now() + p95(downstream) > ctx.deadline:
        return degrade(ctx)            # cached/stale/partial — before spending compute
    result = call(downstream, timeout = ctx.deadline - now(), priority=ctx.priority)
    # priority travels with the deadline: lower tiers get shed first at the far end (P5)
```

**Pitfalls:** A timeout at every hop without propagation multiplies retries invisibly (the 243× effect, F11). Cancel work on deadline expiry — abandoned-but-running tasks are the hidden queue (F14). Give load-balancer health checks the highest priority end-to-end (F14).

---

## P9 — EWMA + hysteresis smoother (the damping layer)

**Intent:** Any feedback loop (cache resizing, pool sizing, autoscaling, adaptive limits) must actuate on persistent error, not noise. (F13, F12)

**Trigger signals:** any raw, noisy measurement feeding a controller.

```
smooth:  ewma = α * sample + (1-α) * ewma          # α ≈ 0.1–0.3 for noisy metrics

decide:  if not in_band(ewma, target, deadband):   # deadband ≈ 10% (HPA default)
             action = controller(ewma)
         # asymmetric windows: fast toward safety, slow returning
         scale_up_window  = 0s
         scale_down_window = 300s rolling-max          # (HPA defaults, F12)

actuate: apply(action); record desired_state; only re-actuate on persistent error
```

**Pitfalls:** An undamped controller on a noisy signal oscillates — and each actuation perturbs the system (capacity changes latency), so the oscillation is self-sustaining (F13). Pick the deadband from measurement variance, not taste. Smoothing too heavily (tiny α) makes the controller blind to real shifts — Gradient2's long-vs-short EWMA divergence exists precisely to get both (F13).
