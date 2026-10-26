# Chromium Layering & DEPS Enforcement

Dependency direction is law, enforced mechanically by DEPS files (deep dive: `../chromium.md` §4, §9).

```mermaid
graph TD
    CH["chrome/<br/>the product (embedder)"]
    SE["services/<br/>core system services<br/>//services"]
    CO2["components/services/<br/>shared non-core services"]
    CS["chrome/services/<br/>chrome-only services"]
    CO["components/<br/>governed sharing layer<br/>≥2 consumers, no upward deps"]
    PU["content/public/<br/>the stable seam (Content API)"]
    CT["content/<br/>web platform + multi-process machinery<br/>never depends on chrome"]
    BA["base/<br/>primitives, threading, memory"]

    CH --> SE
    CH --> CO
    CH --> PU
    CO --> PU
    PU --> CT
    CT --> BA
    CO --> BA
    SE --> BA

    style PU fill:#2d5, color:#fff
    style CH fill:#d52, color:#fff
```

The DEPS grammar (deny-by-default, top-down):

```
"-"  deny path prefix        "+allow path prefix"
specific_include_rules = { regex-per-file: [rules] }
new_usages_require_review = True
```

Layering invariants, each a checkable rule:
1. content/ never includes chrome/ ("Do NOT add chrome to the list below").
2. components/ cannot depend on higher layers; no cycles.
3. Intra-layer reach-through banned: `-chrome` inside chrome/ forces explicit subdir declarations.
4. blink access only via `third_party/blink/public/*` — the public/ carve-out pattern again.
5. Test files get their own allowances via `specific_include_rules` regex keys.
