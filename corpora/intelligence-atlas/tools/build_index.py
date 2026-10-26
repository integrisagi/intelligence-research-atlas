#!/usr/bin/env python3
"""Build papers.json per domain + index/papers-master.json from papers.md files.

Run from anywhere: python3 tools/build_index.py   (paths resolve relative to corpus root)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOMAINS = [
    "01_mathematical-foundations",
    "02_deep-learning-canon",
    "03_llm-architecture-training",
    "04_neuroscience-of-intelligence",
    "05_frontiers-new-intelligence",
]

ENTRY_RE = re.compile(r"^###\s+\[(\d{4})")
FIELD_RE = re.compile(r"^- \*\*(.+?)\*\*:?\s+(.*)$")
FIELDS = ("Link", "Core idea", "Why it matters", "Keywords")


def parse_papers_md(path: Path):
    entries = []
    current = None
    last_field = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()

        m = ENTRY_RE.match(line)
        if m:
            if current:
                entries.append(current)
            head = line[len("### "):].strip()
            year = m.group(1)
            rest = head[head.index("]") + 1:].strip()
            # split title — authors on first em-dash
            if " — " in rest:
                title, authors = rest.split(" — ", 1)
            elif " -- " in rest:
                title, authors = rest.split(" -- ", 1)
            else:
                title, authors = rest, ""
            current = {
                "id": f"{path.parent.name[:2]}-{year}-{len(entries)+1:02d}",
                "domain": path.parent.name,
                "year": int(year),
                "title": title.strip(),
                "authors": authors.strip(),
            }
            last_field = None
            continue

        f = FIELD_RE.match(line)
        if f and current is not None:
            name, value = f.group(1).strip(), f.group(2).strip()
            # normalize "Core idea (1998 follow-up)" -> Core idea
            key = next((F for F in FIELDS if name == F or name.startswith(F)), None)
            if key:
                current[key.lower().replace(" ", "_")] = value
                last_field = key.lower().replace(" ", "_")
            continue

        # continuation lines append to the last field
        if current is not None and last_field and line and not line.startswith(("#", "---")):
            current[last_field] = (current.get(last_field, "") + " " + line.strip()).strip()

    if current:
        entries.append(current)

    # post-process keywords + drop cross-ref-only entries
    out = []
    for e in entries:
        kw = e.get("keywords", "")
        e["keywords"] = [k.strip() for k in kw.split(",") if k.strip()]
        out.append(e)
    return out


def main():
    master = []
    for d in DOMAINS:
        papers_md = ROOT / d / "papers.md"
        if not papers_md.exists():
            print(f"SKIP (missing): {papers_md}")
            continue
        entries = parse_papers_md(papers_md)
        out_path = ROOT / d / "papers.json"
        out_path.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"{d}: {len(entries)} papers -> {out_path.name}")
        master.extend(entries)

    master_path = ROOT / "index" / "papers-master.json"
    master_path.parent.mkdir(exist_ok=True)
    master_path.write_text(json.dumps(master, indent=2, ensure_ascii=False), encoding="utf-8")
    years = [e["year"] for e in master]
    print(f"TOTAL: {len(master)} papers ({min(years)}-{max(years)}) -> {master_path}")

    # sanity checks
    missing = [e["id"] for e in master if not e.get("core_idea") or not e.get("why_it_matters")]
    if missing:
        print("WARN entries missing core_idea/why_it_matters:", missing)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
