"""Extract Mermaid class/sequence diagrams from design pattern docs and list patterns."""
from __future__ import annotations

import re
from pathlib import Path

DOCS = Path(r"d:\workspace\tutorials\design_patterns\docs")
OUT_MMD = Path(r"d:\workspace\tutorials\design_patterns\static\9000_summary\_mmd")
OUT_MMD.mkdir(parents=True, exist_ok=True)

# Include docs with numeric prefix 1000..2800
files = sorted(
    p
    for p in DOCS.glob("*.md")
    if re.match(r"^[12]\d{3}_", p.name)
    and int(p.name[:4]) <= 2800
)

title_re = re.compile(r"^#\s+(.+)$", re.M)
mermaid_re = re.compile(r"```mermaid\s*\n(.*?)```", re.S)


def first_diagram(text: str, kind: str) -> str | None:
    for block in mermaid_re.findall(text):
        if kind in block:
            return block.strip() + "\n"
    return None


# Minimal fallbacks when a page has no sequence / class mermaid
MINIMAL_CLASS = """classDiagram
    class Pattern
"""

MINIMAL_SEQ = """sequenceDiagram
    Actor Client
    participant Obj
    Client->>Obj: request()
    Obj-->>Client: result
"""

manifest: list[dict] = []

for path in files:
    num = path.name[:4]
    stem = path.stem  # e.g. 1000_singleton
    text = path.read_text(encoding="utf-8")
    title_m = title_re.search(text)
    title = title_m.group(1).strip() if title_m else stem

    class_src = first_diagram(text, "classDiagram")
    seq_src = first_diagram(text, "sequenceDiagram")

    # Comparison / special pages without GoF mermaid: skip auto mermaid, mark for static copy
    special_pngs: list[tuple[str, str]] = []
    if stem == "1910_bridge_vs_abstract_factory":
        special_pngs = [
            ("class", "structure.png"),
            ("extra", "when_to_choose.png"),
        ]
        class_src = None
        seq_src = None
    elif stem == "2310_strategy_vs_bridge":
        special_pngs = [
            ("class", "strategy_shape.png"),
            ("extra", "bridge_shape.png"),
        ]
        class_src = None
        seq_src = None
    elif stem == "1510_python_decorator":
        # no diagrams — use minimal placeholders
        class_src = class_src or MINIMAL_CLASS
        seq_src = seq_src or MINIMAL_SEQ
    elif stem == "1200_factory_method":
        # may only have SVG asset; still try mermaid else minimal
        if not class_src:
            class_src = MINIMAL_CLASS
        if not seq_src:
            seq_src = MINIMAL_SEQ

    entry = {
        "stem": stem,
        "num": num,
        "title": title,
        "class_mmd": None,
        "seq_mmd": None,
        "special": special_pngs,
        "has_class": False,
        "has_seq": False,
    }

    if class_src:
        mmd_path = OUT_MMD / f"{stem}_class.mmd"
        mmd_path.write_text(class_src, encoding="utf-8")
        entry["class_mmd"] = str(mmd_path)
        entry["has_class"] = True

    if seq_src:
        # keep sequence minimal: strip long notes if huge? keep as-is for accuracy
        mmd_path = OUT_MMD / f"{stem}_sequence.mmd"
        mmd_path.write_text(seq_src, encoding="utf-8")
        entry["seq_mmd"] = str(mmd_path)
        entry["has_seq"] = True

    manifest.append(entry)
    print(f"{stem}: class={entry['has_class']} seq={entry['has_seq']} special={len(special_pngs)}")

# write manifest as simple lines for shell
lines = []
for e in manifest:
    if e["class_mmd"]:
        lines.append(f"CLASS|{e['stem']}|{e['class_mmd']}")
    if e["seq_mmd"]:
        lines.append(f"SEQ|{e['stem']}|{e['seq_mmd']}")
    for kind, name in e["special"]:
        lines.append(f"COPY|{e['stem']}|{kind}|{name}")

(OUT_MMD / "manifest.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
(OUT_MMD / "titles.txt").write_text(
    "\n".join(f"{e['stem']}|{e['title']}" for e in manifest) + "\n",
    encoding="utf-8",
)
print(f"Wrote {len(manifest)} patterns, {len(lines)} render jobs")
