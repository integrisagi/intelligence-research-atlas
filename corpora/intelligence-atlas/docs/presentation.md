# Presentation — Intelligence Research Atlas
# Format: 14 slides. Render as a slide deck / PDF for the repo (docs/presentation.pdf)
# Each slide: title, 3–5 lines max, one visual or example. Speaker notes in italics.

## Slide 1 — Title
Intelligence Research Atlas
The load-bearing ideas behind AI, LLMs, neuroscience, and maths — distilled.
1936 → October 2026 · 63 findings · 13 diagrams · 6 PDF volumes
*Open with the promise: you don't have to re-read the field to build on it.*

## Slide 2 — The problem
The field is too big to hold in one head.
Thousands of papers. Leaderboards move weekly. Claims contradict each other.
Builders re-learn the same traps: metric artifacts, reward hacking, contaminated benchmarks.
*This atlas exists to compress the canon into what actually changes a decision.*

## Slide 3 — The thesis
Intelligence — biological or artificial — is compression.
Brains and networks both build predictive world models and improve by minimising prediction error.
Shannon entropy ≈ cross-entropy loss ≈ cortical free energy.
*Everything else is a substrate's way of doing compression better.*

## Slide 4 — The five connections (the whole atlas in one slide)
1. Compression is the universal objective
2. Dopamine is the TD error
3. Memory is active, not a log
4. Search + learned priors beats either alone
5. Sparse distributed coding, twice over
*If the audience remembers one slide, this is it.*

## Slide 5 — Maths: why learning works
Compression = understanding. No learning without inductive bias.
Depth is exponential, width is not. Lazy vs rich training. Scaling laws, then the data wall.
Grokking: memorise first, understand later — and you can engineer which one you get.
*Visual: scaling / emergence / grokking diagram, domain 01.*

## Slide 6 — Deep learning canon: what we inherited
1943–2017: perceptron → backprop → CNN/LSTM → RL → self-supervision.
Three non-negotiables for depth: gates, normalisation, identity paths.
The 2012 explosion was a conjunction: algorithm × data × compute — not one jump.
*Visual: architecture evolution diagram, domain 02.*

## Slide 7 — LLMs: the stack that won
Pretraining = capability. Post-training = behaviour.
RLHF aligns behaviour — and fails in known ways. RLVR (2025) trains reasoning with verifiable rewards.
Test-time compute is a second scaling axis: a dial you turn at inference, not just training.
*Visual: LLM training pipeline, domain 03.*

## Slide 8 — LLMs: the limits
Reasoning collapses past a complexity frontier. Knowledge lives badly in weights — retrieve it instead.
Superposition: more concepts than neurons. Evaluation is the meta-problem of 2025–26.
*Message: scale is not a strategy by itself; measurement and decomposition are.*

## Slide 9 — Neuroscience: the parts catalog backprop lacks
Dopamine = prediction error. Hippocampal replay = consolidation. Sleep = renormalisation.
Global workspace = bottleneck + broadcast. Local learning rules that work without backprop.
*Visual: neuro → AI bridge, domain 04. These are mechanisms to steal, not metaphors.*

## Slide 10 — Frontiers: what comes after next-token prediction
World models: plan in imagination, act in reality. Active inference: one objective for perception, action, curiosity.
Post-transformer zoo: Mamba, KAN, diffusion LMs, Titans — each encodes a different bias.
Neuro-symbolic hybrids own compositionality. Agents are now a stack, not a demo.
*Visual: paradigm map + agent stack, domain 05.*

## Slide 11 — The agent stack, settled (2026)
LLM / planner core → episodic + skill memory + RAG → tools → reflection → multi-agent orchestration → verification.
Spend your novelty budget on memory format and verifier quality — that is where systems actually differentiate.
*This is the most directly usable slide for builders.*

## Slide 12 — Traps to avoid
Emergence as a metric artifact. Reward hacking. Contaminated benchmarks.
Reasoning that looks like search but isn't. Objectives that mislead.
*Each trap is documented with its paper in the atlas — don't re-pay for it.*

## Slide 13 — How to use this repo
Humans: start with reading-order.md, read PDFs for depth.
Builders: pick your goal path (LLM / new architecture / neuroscience / safety).
Agents: the repo's AGENTS.md is the lookup protocol — findings first, papers.json for citations.
*Show the repo map live for 30 seconds.*

## Slide 14 — Close: what to build next
The atlas points one way: generality is still unsolved (ARC), and the cheapest new substrate to test is a random one with a trained readout.
Compression, replay, search, and verification — combined, not scaled alone — are the next bet.
Compiled 2026-10-25. Extend it: add a finding, cite a paper, rebuild the index.
*End on the repo link and the invitation to contribute.*
