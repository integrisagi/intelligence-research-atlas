# Build Report — How This Corpus Was Made

**Session date:** 2026-10-25
**Built by:** ZCode (GLM Heavy-Lift Harness session, powered by GLM)
**Deliverable:** the folder this file lives in — the Big-Tech Code Structure & Systems Deconstruction corpus.

This file is the record of the chat that produced the corpus: what was asked, what was decided, what was done, and an honest assessment of the result.

---

## 1. The original ask (user's intent, condensed)

The user gets a large free token allocation (300M+) because they run AI agents, and noticed that most AI coding output stops at "the model thinks it's right." They wanted the opposite: **extensive research into how big tech giants actually build scalable, modular, interchangeable systems** — Chromium, VSCodium/VS Code, and the like — deconstructed into findings on *why* those structures are efficient, so that (a) future agents can be pointed at it and write "god tier" code, and (b) the user can see how big-tech code and data pipelines actually work. Explicit extra requirement: **include the dynamic code too — code that behaves according to the resources it gets.**

## 2. Decisions the user made along the way

Three scoping questions were asked during planning; the user's answers shaped everything:

| Question | User's choice | Effect |
|---|---|---|
| Breadth beyond the core program (Chromium + VSCode + workflow + pipelines + adaptive)? | **Core program, deep** — no Linux/LLVM/Kubernetes extras | Maximum depth on the five pillars |
| Wire the distilled rulebook for agents to auto-find it? | **Corpus only** — everything self-contained in the folder, no root-level AGENTS.md router | Nothing outside `glm/` was created except a one-line pointer in the project README |
| Form of the dynamic-code section? | **Patterns + pseudocode** — no runnable implementations/test step | `05_adaptive-systems/patterns.md` is pseudocode-only |

The plan was rejected twice before approval — first because the user wanted **one folder** holding everything, then clarified: folder inside `glm-harness`, internal organization was my call. I kept the structured module layout (best for agent lookup, matching the house style of the sibling `intelligence-research/` corpus) with PERSONA.md and PLAYBOOK.md at the top level. That plan was approved and executed exactly.

## 3. What was done, turn by turn

1. **Workspace reconnaissance** — read `glm-harness/README.md`, `SYSTEM.md`, and the sibling `intelligence-research/` corpus to learn the house conventions: numbered findings (`F1 — Title`, Claim → Evidence → Why it matters), AGENTS.md navigation protocols, Mermaid diagrams, sources-per-claim, anti-hallucination rules (SYSTEM.md's "anti-AI spam laws").
2. **Planning** — three AskUserQuestion scoping rounds, two plan revisions (see §2), final plan approved.
3. **Research** — four background research agents launched in parallel (two had to be relaunched after hitting the user concurrency limit of two simultaneous agents; the harness queued them as slots freed):
   - **Wave A — Chromium:** 24 verified findings (C1–C24) from chromium.org design docs, GN docs, and real source files (`content/DEPS`, `chrome/DEPS`, `network_service.mojom`, `memory_pressure_level.h`).
   - **Wave B — VS Code:** 24 verified findings (V1–V24) from the vscode wiki plus real source fetched from `microsoft/vscode` main: `eslint.config.js`, `instantiation.ts`, `lifecycle.ts`, `event.ts`, `ptyHostService.ts`, `startupTimings.ts`, and more (13 code excerpts).
   - **Wave C — workflow + pipelines:** 35 verified findings (W1–W35): Google eng-practices, the CACM monorepo paper (archived full text), SRE book chapters, Meta engineering posts, Kafka design docs, the Dataflow Model abstract, Kreps' Kappa article, dbt/Iceberg/Reactive Streams docs.
   - **Wave D — adaptive systems:** 27 verified findings (D1–D27): Chromium pressure headers, Android onTrimMemory, cgroups v2 kernel docs, Go 1.25 release notes, automaxprocs, OpenJDK container bugs, Netflix `GradientLimit.java`, The Tail at Scale (author-hosted PDF after CACM returned 403), HTTP/2 flow control (RFC 9113), Go runtime/proc.go, Caffeine wiki, Azure circuit-breaker docs, AWS backoff-with-jitter, K8s HPA, AWS load shedding, the Crash-Only Software paper.
4. **Synthesis** — every module file written in the main context from the wave results: two deep dives (chromium.md, vscode.md), five findings files (F1–F10/14/22/13/14 per file), nine pseudocode patterns (P1–P9), and the distillations: PLAYBOOK.md (rules R1–R30 + pre-ship checklist + hall of shame), PERSONA.md, master-map.md, SOURCES.md.
5. **QA pass** — automated checks: AGENTS.md's documented lookup grep actually resolves; all finding/rule/pattern numbering sequential; every relative markdown link resolves (two broken links found in SOURCES.md and fixed); all Mermaid diagrams ≤30 nodes; anchor targets verified.
6. **Wrap-up** — one-line pointer added to the project README; a memory note saved so future sessions find the corpus.

**Rough token burn:** ~13.5M tokens across the four research subagents alone, plus main-context synthesis — this is what the harness's free allocation is for.

## 4. The corpus in numbers

- 20 markdown files, ~24,300 words
- 110 research findings (C, V, W, D series) → 73 corpus findings (F) → 30 playbook rules (R) → 9 patterns (P)
- 7 Mermaid diagrams, all under the 30-node limit
- ~120 unique source URLs in SOURCES.md, each mapped to what it grounded
- Every finding: Claim → Evidence (+URL) → Why it's efficient → How to apply. Unverified claims were dropped, not guessed; each file ends with a "verification gaps" section.

## 5. What I think — honest assessment

**Strengths:**
- The grounding discipline held. Every load-bearing claim traces to a fetched source, and the gaps sections honestly mark what didn't verify (e.g., the "~40M lines" Chromium figure is officially unsourced and is flagged as framing; the Chrome release-channel page was served in Hindi at fetch time and cadence facts are marked as translations).
- The cross-codebase convergence is the real payload: Chromium (C++) and VS Code (TypeScript) independently arrived at the same four laws — machine-enforced dependency direction, contracts generated from one artifact, sacrificial-process isolation, and typed/coarse resource signals with local policies. When two 100M-line-scale systems converge, that's signal, not fashion.
- The playbook is genuinely usable by an agent: ten checklist questions, imperative rules, links back to evidence.

**Limitations, stated plainly:**
- The dynamic-code section is pseudocode by design (user's choice) — the patterns are control-shape-accurate but untested. A future pass could make P1–P9 runnable with smoke tests.
- Depth follows the sources that were fetchable. Chromium's renderer internals, GPU process details, and PartitionAlloc adoption scope are thinner than the layering/IPC story because those design docs 404'd or weren't machine-readable this session.
- A few quotes carry fetch caveats (localized pages, paraphrased DEPS comments) — all flagged inline, but worth knowing before quoting them publicly.
- The corpus is a snapshot of October 2026 upstream state; VS Code main and Chromium main move daily.

**What I'd do next if asked:**
1. Make the nine adaptive patterns runnable + smoke-tested (the natural "phase 2").
2. Add a third deep dive (Linux kernel or Kubernetes would contrast the two app codebases with a systems one).
3. Compile the corpus into a typeset PDF volume, mirroring `intelligence-research/`'s `tools/build_pdfs.py` flow.
4. If the user changes their mind on the router decision, add a two-line AGENTS.md at the glm-harness root pointing future agents into `glm/`.

## 6. How to use this corpus

- **Human, first contact:** `README.md` → `master-map.md` reading orders.
- **Agent, any session:** read `AGENTS.md` first (it's the protocol), then grep findings for the task's keywords.
- **Behavior change for a task:** load `PERSONA.md` at session start; run `PLAYBOOK.md`'s pre-ship checklist before declaring done.
- **Extending:** follow the conventions in `AGENTS.md` — findings append-only, sources mandatory, unverified claims dropped.
