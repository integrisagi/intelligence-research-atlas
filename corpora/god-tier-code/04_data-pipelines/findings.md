# Data Pipelines — Distilled Findings

How big tech moves data at scale: the log abstraction, stream/batch unification, time semantics, schema contracts, and quality gates. Every finding carries at least one verified source. Analysis ("why it's efficient") is marked and kept separate from sourced fact.

Paper references point to `SOURCES.md` in the corpus root. Compiled 2026-10-25.

---

## F1 — The distributed log: per-partition ordering + consumer groups

**Claim:** Kafka models topics as totally ordered, replicated partitions; ordering is guaranteed only within a partition, and one partition is consumed by exactly one consumer per consumer group.

**Evidence:** "Our topic is divided into a set of totally ordered partitions" and "a Kafka partition is a replicated log"; partitions are "each of which is consumed by exactly one consumer within each subscribing consumer group at any given time" — [kafka.apache.org design](https://kafka.apache.org/43/design/design). Ordering: "Kafka guarantees that any consumer of a given topic-partition will always read that partition's events in exactly the same order as they were written" — [kafka.apache.org/intro](https://kafka.apache.org/intro)

**Why it's efficient:** Per-partition ordering is the design that lets ordering guarantees and horizontal scaling coexist — partition count is the parallelism knob, and local order survives where it matters.

**How to apply:** Key events so all records needing the same causal order land on one partition; design consumers to be partition-count-independent.

---

## F2 — Consumption decoupled from storage: replay is a consumer reset

**Claim:** Kafka does not delete on consumption; consumers control their offset, can rewind to reprocess history, and throughput is roughly independent of data size.

**Evidence:** "Instead of attempting to delete messages as soon as they are consumed, we can retain messages for a relatively long period"; "the consumer thus has significant control over this position and can rewind it to re-consume data"; "a consumer can deliberately rewind back to an old offset and re-consume data"; "the performance is completely decoupled from the data size" — [Kafka design](https://kafka.apache.org/43/design/design); "events are not deleted after consumption" — [intro](https://kafka.apache.org/intro)

**Why it's efficient:** Append-only logs turn "fix a downstream bug and reprocess" from an ETL archaeology project into a consumer reset — the foundation for Kappa-style reprocessing (F6).

**How to apply:** Set retention by worst-case reprocessing window (not by downstream consumption speed); keep consumer state keyed by offsets so replays are idempotent.

---

## F3 — Event time, processing time, and watermarks

**Claim:** Correct unbounded-stream computation must separate event time from processing time; watermarks bound how long you wait for late data.

**Evidence:** "Event time is the time that each individual event occurred on its producing device"; "processing time refers to the system time of the machine that is executing the respective operation"; "a Watermark(t) declares that event time has reached time t in that stream" (no more elements with timestamps ≤ t expected); "assuming all of the data has arrived, event time operations will behave as expected, and produce correct and consistent results" — [Flink docs, concepts/time](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time)

**Why it's efficient:** Processing time is nondeterministic under backpressure and retries; event time + watermarks make results reproducible across reprocessing runs — which is what makes pipeline changes testable.

**How to apply:** Timestamp at the producer with event time, carry it end to end, and expose watermark delay as a tunable completeness-vs-latency parameter per window.

---

## F4 — The Dataflow Model: correctness, latency, cost — pick explicitly

**Claim:** Akidau et al. (VLDB 2015) argue unbounded out-of-order data forces an explicit choice among correctness, latency, and cost, and provide the abstractions (event-time windowing, triggers, updates/retractions) to express those choices.

**Evidence:** "Unbounded, unordered, global-scale datasets are increasingly common in day-to-day business"; consumers "have evolved sophisticated requirements, such as event-time ordering and windowing by features of the data themselves"; "one can never fully optimize along all dimensions of correctness, latency, and cost for these types of input"; the field "must stop trying to groom unbounded datasets into finite pools of information that eventually become complete" — [research.google, The Dataflow Model](https://research.google/pubs/the-dataflow-model-a-practical-approach-to-balancing-correctness-latency-and-cost-in-massive-scale-unbounded-out-of-order-data-processing/)

**Why it's efficient:** The paper's lasting contribution is the vocabulary: once windowing/triggering/watermarks are first-class API concepts, "eventually complete" batch thinking stops leaking into streaming designs.

**How to apply:** For each streaming aggregation, write down its window, trigger, and late-data policy as explicit configuration rather than implicit framework defaults.

---

## F5 — Exactly-once effects come from guarded, idempotent stages

**Claim:** Large-scale pipelines achieve exactly-once semantics through stage-structured processing with uniqueness guarantees (leases, filename uniqueness, token validation) rather than naive retry.

**Evidence:** Pipelines ensure "correctness with exactly-once semantics"; "it's easy to guarantee that all work is executed, or at least reflected in permanent state, exactly once" using "a triple correctness guarantee: configuration, lease ownership, and filename uniqueness"; "the worker consumes work units from a previous stage and produces output units" — [SRE book, Data Processing Pipelines](https://sre.google/sre-book/data-processing-pipelines/)

**Why it's efficient:** At scale, retries are routine, so "at-least-once delivery + idempotent writes" is the only architecture that holds; unique output naming is the simplest, most robust idempotency primitive.

**How to apply:** Make every sink write deterministic, unique-per-work-unit output so re-execution is harmless by construction.

---

## F6 — Kappa beats Lambda: one log-centric path, reprocess on demand

**Claim:** Jay Kreps argued the Lambda Architecture (batch layer + speed layer over the same data) forces maintaining equivalent logic in two systems; Kappa runs everything on a stream processor and reprocesses from the retained log when logic changes.

**Evidence:** "The Lambda Architecture is an approach to building stream processing applications on top of MapReduce and Storm"; "maintaining code that needs to produce the same result in two complex distributed systems is exactly as painful" [as it seems]; Kappa: "maybe we could call this the Kappa Architecture, though it may be too simple of an idea to merit a Greek letter"; reprocessing: "when you want to do the reprocessing, start a second instance of your stream processing job that starts processing" from the beginning of the retained data, output "to a new output table"; stream systems can "handle the reprocessing by increasing the parallelism and replaying history very, very fast" — [Questioning the Lambda Architecture, O'Reilly Radar](https://www.oreilly.com/radar/questioning-the-lambda-architecture/) (note: Kreps does not use the phrase "bug farm" — common misattribution)

**Why it's efficient:** Dual code paths guarantee eventual divergence (two engines, two schedulers, two failure modes); one path makes every bug fix automatically apply to history at the next reprocess.

**How to apply:** Default to log + stream processor with replay; keep a batch path only where a genuine recompute-from-scratch constraint (e.g., billing audits) demands it.

---

## F7 — Backpressure is demand signaling, not bigger buffers

**Claim:** Reactive Streams standardizes non-blocking backpressure: consumers signal demand, so inter-stage queues stay bounded and receivers are never forced to buffer arbitrary amounts.

**Evidence:** "Reactive Streams is an initiative to provide a standard for asynchronous stream processing with non-blocking back pressure"; goal is "to govern the exchange of stream data across an asynchronous boundary" "while ensuring that the receiving side is not forced to buffer arbitrary amounts of data"; "backpressure is an integral part of this model in order to allow the queues which mediate between threads to be bounded"; rule 2.1: "a Subscriber MUST signal demand via Subscription.request(long n) to receive onNext signals" — [reactive-streams.org](https://www.reactive-streams.org/), [reactive-streams-jvm](https://github.com/reactive-streams/reactive-streams-jvm)

**Why it's efficient:** Without demand signaling, overload converts into unbounded in-memory buffering and OOM cascades; with it, overload degrades gracefully into latency, which systems recover from.

**How to apply:** Bound every inter-stage queue explicitly; push backpressure to the source (pause the fetcher) instead of buffering deeper in the pipeline.

---

## F8 — Pause the source instead of growing the buffer

**Claim:** Kafka lets a consumer pause fetching on specific partitions and resume later — backpressure applied at the ingestion boundary.

**Evidence:** pause() — "suspend fetching from the requested partitions"; resume() — "resume specified partitions which have been paused with pause(Collection)" — [KafkaConsumer javadoc 3.5](https://kafka.apache.org/35/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html); flow control: "using pause(Collection) and resume(Collection) to pause the consumption on the specified assigned partitions … including pausing 'from the ahead topic in order to get the lagging stream to catch up'" — [KafkaConsumer javadoc 3.0](https://kafka.apache.org/30/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html)

**Why it's efficient:** Pausing shifts buffering from consumer heap to the broker's log — the component designed for it — so consumer memory becomes a fixed cost instead of an overload failure point.

**How to apply:** When joining streams of unequal lag or draining slow sinks, pause per-partition rather than enlarging local buffers. (Pattern: `05_adaptive-systems/patterns.md`.)

---

## F9 — Schemas are contracts: compatibility enforced at registration

**Claim:** Confluent Schema Registry checks compatibility at registration time: BACKWARD (new consumers read old data), FORWARD (old consumers read new data), FULL (both), plus transitive variants; default is BACKWARD.

**Evidence:** "Backward - consumers using new schema can read data written with old schema (add optional fields, remove fields)"; "Forward - consumers using old schema can read data written with new schema (remove optional fields, add fields)"; "Full - both backward and forward compatible (add/remove optional fields only)"; "transitive - compatibility checked against all previous versions, not just the last one"; "the default compatibility mode is BACKWARD"; and defaults matter: "the new field favorite_color has the default value 'green'. This allows data encoded with the old schema to be read with the new one" — [Confluent Schema Registry docs](https://docs.confluent.io/platform/current/schema-registry/avro.html)

**Why it's efficient:** Enforcement at registration converts "breaking change" from a runtime incident into a rejected commit; forward compatibility is what lets producers and consumers deploy independently — the schema equivalent of the code-review gate (see `03_engineering-workflow/findings.md` F1).

**How to apply:** Set FULL_TRANSITIVE on shared topics, require defaults for new fields, and wire the compatibility check into CI so violations fail before merge.

---

## F10 — ETL → ELT: land raw, transform in-warehouse, under engineering discipline

**Claim:** The dbt model: load raw data into the platform first, transform with version-controlled SQL inside the warehouse, applying software-engineering practices (version control, tests, CI/CD) to the transformation layer.

**Evidence:** "dbt transforms raw warehouse data into trusted data products. You write simple SQL select statements, and dbt handles the heavy lifting by creating modular, maintainable data models"; "you can transform data directly in your cloud data platform"; "apply software engineering best practices like version control, testing, modularity, CI/CD, and documentation to analytics workflows" — [dbt docs introduction](https://docs.getdbt.com/docs/introduction)

**Why it's efficient:** Inverting ETL to ELT means raw data is never lossy-pre-transformed before its value is known; warehouse compute turns transformations into declarative, restartable operations instead of custom code.

**How to apply:** Land source data raw and immutable; express every transformation as version-controlled SQL with a model DAG; review transformation changes like code.

---

## F11 — Lakehouse table formats: schema-on-read with ACID guarantees

**Claim:** Apache Iceberg provides a table format over object storage with non-rewriting schema evolution and isolation/concurrency properties, letting many engines share tables safely.

**Evidence:** "Iceberg is a high-performance format for huge analytic tables"; "schema evolution just works. Adding a column won't bring back 'zombie' data"; "schema changes never require rewriting your table"; features include "serializable isolation" and "optimistic concurrency"; "Iceberg brings the reliability and simplicity of SQL tables to big data, while making it possible for engines like Spark, Trino, Flink, Presto, Hive and Impala to safely work with the same tables" — [iceberg.apache.org](https://iceberg.apache.org/)

**Why it's efficient:** Table formats reconcile flexible raw-file lakes with transactional warehouses by making the metadata layer (manifests, snapshots) the source of truth — schema flexibility and ACID come from the same place.

**How to apply:** Put a table format (Iceberg/Delta) under lake storage rather than raw paths; manage schema changes through its evolution primitives instead of in-place rewrites.

---

## F12 — Streaming-first vs micro-batch: choose by SLA, not fashion

**Claim:** Flink treats batch as a special case of streaming (bounded streams); Spark Structured Streaming's default engine is micro-batch (~100 ms end-to-end), with a continuous mode (~1 ms, at-least-once) since Spark 2.3.

**Evidence:** Flink executes batch programs "as a special case of streaming programs in BATCH ExecutionMode, where the streams are bounded" — [Flink docs, stateful stream processing](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/stateful-stream-processing/). Spark: "internally, by default, Structured Streaming queries are processed using a micro-batch processing engine, which processes data streams as a series of small batch jobs thereby achieving end-to-end latencies as low as 100 milliseconds and exactly-once fault-tolerance guarantees"; "since Spark 2.3, we have introduced a new low-latency processing mode called Continuous Processing, which can achieve end-to-end latencies as low as 1 millisecond with at-least-once guarantees" — [spark.apache.org streaming](https://spark.apache.org/docs/latest/streaming/index.html)

**Why it's efficient:** The philosophies differ in where the latency floor comes from: micro-batch buys throughput and simpler fault tolerance at a ~100 ms floor; record-at-a-time streaming pays scheduling cost for millisecond reaction.

**How to apply:** If consumers tolerate seconds, micro-batch is operationally cheaper; treat continuous mode as an opt-in for genuine real-time paths.

---

## F13 — Data quality gates: assertions as pipeline stages

**Claim:** dbt tests are SQL assertions (unique, not_null, accepted_values, relationships) run during development and in production; Great Expectations formalizes the same idea as verifiable expectations over data batches.

**Evidence:** "Data tests are assertions you make about your models and other resources in your dbt project"; "they are select statements that seek to grab 'failing' records, ones that disprove your assertion"; "if the data test returns zero failing rows, it passes"; run guidance: "you should run your data tests whenever you are writing new code … and whenever you run your transformations in production (to ensure that your assumptions about your source data are still valid)"; "we recommend that every model has a data test on a primary key, that is, a column that is unique and not_null" — [dbt docs, data tests](https://docs.getdbt.com/docs/build/data-tests); "an expectation is a verifiable assertion about data" — [Great Expectations overview](https://docs.greatexpectations.io/docs/core/introduction/gx_overview)

**Why it's efficient:** Tests-as-queries make data quality checkable in the same CI gate as code — a bad upstream change is caught at the pipeline boundary rather than by downstream stakeholders; the primary-key test is the highest-value single assertion.

**How to apply:** Add unique+not_null on every model's key; run tests in the promotion path (fail the deploy, not the dashboard); track test failures as pipeline incidents.
