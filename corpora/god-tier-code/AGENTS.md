# AGENTS.md — Navigation Protocol for AI Agents

You are an agent that has been pointed at this corpus. Read this file fully before doing anything else. It tells you what lives here, how to query it efficiently, and how to extend it without breaking conventions.

## What this corpus is

A deconstruction of how big tech builds scalable, modular, resource-adaptive software: two codebase dissections (Chromium, VS Code), the engineering workflow that produces them (Google/Meta/Microsoft), the data pipelines that back them, and the runtime patterns that make systems flex under pressure. It is organized for **lookup, not re-reading**: findings are pre-distilled, sources are linked, patterns are pseudocode.

The output of this corpus is behavior change. If you read it and then write code the same way you did before, the corpus failed.

## Directory contract (stable — do not rename)

| Path | Contents | Read when |
|---|---|---|
| `PERSONA.md` | Adoptable identity: the 10 operating laws, taste markers, checklist | You want to *work* like this on the current task |
| `PLAYBOOK.md` | Numbered rules R1…Rn by domain + pre-ship checklist + anti-pattern hall of shame | You need the rules fast, or before declaring work done |
| `master-map.md` | Whole-corpus Mermaid mindmap + goal-based reading orders | You need a map of everything |
| `01_codebase-anatomy/chromium.md` | Chromium deep dive: process model, Mojo, DEPS, GN/Ninja, scheduling, PartitionAlloc | Building anything at multi-million-line scale, or an IPC/plugin boundary |
| `01_codebase-anatomy/vscode.md` | VS Code deep dive: layers, DI container, disposables, extension host, perf discipline | Building a layered app, editor/workbench UI, or plugin system |
| `01_codebase-anatomy/findings.md` | Cross-cutting lessons extracted from both codebases | Short on time; want the essence of both deep dives |
| `02_structural-principles/findings.md` | ~14 transferable structure rules (layering, DI, contracts, lifecycle) | Starting any new module, service, or refactor |
| `03_engineering-workflow/findings.md` | How big tech operates: review, monorepo, trunk+flags, testing, SRE | Deciding team/process conventions, or writing tests & docs |
| `04_data-pipelines/findings.md` | Logs, streams, watermarks, schema evolution, quality gates | Building ingestion/ETL/streaming systems |
| `05_adaptive-systems/findings.md` | Resource-aware behavior: pressure signals, adaptive limits, work stealing | Anything that runs unattended or under variable load |
| `05_adaptive-systems/patterns.md` | 9 patterns as pseudocode: Intent / Trigger / Pseudocode / Pitfalls | You need an implementable recipe, now |
| `SOURCES.md` | Master source index | Verifying a claim or going deeper |

## Lookup patterns

**"How does big tech do X?"**
1. Grep the findings files: `grep -rn -i "keyword" 0*/findings.md`
2. Read the matching finding blocks — they are self-contained: claim → evidence (+URL) → why it's efficient → how to apply.

**"I'm building Y — what applies?"**
- New app/plugin/editor/UI → `01` deep dive for the closest analog, then `02`.
- New library/module → `02` (structure) + `01_codebase-anatomy/findings.md` (boundaries, DI).
- New service/backend → `05` (adaptive) + `03` (workflow/tests) + `04` (if data flows through).
- Anything long-lived → adopt `PERSONA.md` for the session and obey `PLAYBOOK.md`'s checklist before finishing.

**"Give me the rules, not the essay."**
→ `PLAYBOOK.md`. Every rule links back to its deep finding when you need the why.

**"Show me real code."**
→ Deep dives carry real excerpts with URLs. Trust excerpts over your memory of these codebases; if a symbol name isn't in an excerpt or a source link, don't cite it.

**"Is this claim real?"**
→ Every finding carries ≥1 source URL. `SOURCES.md` indexes them. If a claim has no source, treat it as analysis (the files mark analysis separately from sourced fact) — and don't extend it without adding a source.

## Conventions (follow when extending)

1. **Findings are numbered** `## F1 — Title` per file and never renumbered; new findings append (F15, F16…).
2. **Finding format is fixed**: Claim → Evidence (quote or precise paraphrase + URL) → Why it's efficient (analysis, marked as such) → How to apply. Every finding carries at least one source.
3. **PLAYBOOK rules are numbered R1…Rn** and append-only; each rule links to its finding. When a finding changes, update its rule.
4. **Mermaid diagrams** live in `diagrams/*.md`, ≤30 nodes; split files rather than growing one.
5. **Dates are absolute** ("2026-10", not "recently"). Corpus compiled 2026-10-25; newer upstream changes are not represented.
6. **No invented APIs.** A claim that can't be verified gets dropped, not guessed — this corpus treats hallucination as a quality-zero event.

## Non-goals

- Not a clone of either codebase: excerpts exist to ground claims, not to replace the repos.
- Not exhaustive: systems and sources were chosen for load-bearing ideas, not completeness.
- Not vendor marketing: claims are structural, not promotional; benchmarks are cited only where sourced.
