# Combined Presentation — Two Corpora, Kept Separate
# 16 slides. Print docs/combined-presentation.html to PDF for a deck.

## Slide 1 — Title
Research Atlas: Two Corpora, Kept Separate
Corpus 1: what intelligence is. Corpus 2: how the best code is built.
Compiled 2026-10-25 · Public repo, CC BY 4.0

## Slide 2 — Why two corpora, not one blob
One corpus answers "what is intelligence?" The other answers "how do you build like big tech?"
Mixing them would blur numbering, sources, and rules. Keeping them in separate folders — each with its own AGENTS.md — lets a future agent load exactly one, and only one, for a task.

## Slide 3 — Corpus 1 thesis
Intelligence — biological or artificial — is compression.
Brains and networks build predictive world models and improve by minimising prediction error.
Shannon entropy ≈ cross-entropy loss ≈ cortical free energy.

## Slide 4 — Corpus 1: five connections
1. Compression is the universal objective
2. Dopamine is the TD error
3. Memory is active, not a log
4. Search + learned priors beats either alone
5. Sparse distributed coding, twice over

## Slide 5 — Corpus 1: what is inside
63 findings, 138+ unique papers, 13 diagrams, 6 PDF volumes (51 pages).
Maths, deep learning canon, LLM training, neuroscience, frontiers.
Start: reading-order.md, then the domain that matches your goal.

## Slide 6 — Corpus 1: traps it documents
Emergence as a metric artifact. Reward hacking. Contaminated benchmarks.
Reasoning that looks like search but isn't. Objectives that mislead.
Knowing these before you build is half the work.

## Slide 7 — Corpus 2 thesis
Big tech's edge is not talent density, it is structure.
Dependency direction enforced by machines. Every seam an explicit contract.
Failure isolated behind process boundaries. Runtime behaviour that flexes with resources.

## Slide 8 — Corpus 2: Chromium + VS Code
Two codebases, same four laws: machine-enforced dependency direction, contracts generated from one artifact, sacrificial-process isolation, typed resource signals with local policies.
When two giant systems converge independently, that is signal, not fashion.

## Slide 9 — Corpus 2: the PLAYBOOK
30 rules, R1–R30, in five groups: Structure, Interfaces, Concurrency & Resources, Data, Process.
Plus a 10-question pre-ship checklist and an anti-pattern hall of shame.
Rules link back to findings; findings link to sources.

## Slide 10 — Corpus 2: adaptive systems
9 pseudocode patterns, P1–P9: memory-pressure governor, boot-time resource budget, gradient concurrency limiter, bounded backpressure queue, priority shedder, breaker + hedged requests, work-stealing pool, deadline propagation, EWMA + hysteresis damping.
Pseudocode by design — control-shape accurate, not yet smoke-tested as runnable code.

## Slide 11 — Corpus 2: workflow + pipelines
Review standard "better, not perfect", small CLs, monorepo, trunk + flags, error budgets, release trains.
Data: one log-centric path, event time + watermarks, versioned schemas, quality gates in the promotion path.

## Slide 12 — How the two corpora fit together
Atlas tells you what to build towards. God-tier code tells you how to build it so it survives scale, review, and load.
Use the atlas to choose the architecture. Use the playbook to check the code before you ship it.

## Slide 13 — Isolation, in practice
No AGENTS.md at the repo root. No shared persona. No cross-links between corpora.
Each corpus's numbering is append-only and per-corpus.
The GLM session transcript and raw log are NOT in this repo — research only, session internals stay private.

## Slide 14 — How to use this repo
Human: read a corpus README, then its playbook / reading order.
Agent, for one task: point it at exactly one corpus folder, read that folder's AGENTS.md first.
Do not point an agent at the repo root and expect it to choose.

## Slide 15 — What is not here
Not exhaustive. Not current past October 2026. Not runnable adaptive code (patterns are pseudocode).
Not a textbook: derivations omitted, maths named and sourced, not proven.
Verify against cited sources before building on any single claim.

## Slide 16 — Close
Two maps, kept separate on purpose.
One for what intelligence is, one for how the best code is built.
Extend each inside its own folder, cite a source for every new finding, and keep the isolation intact.
