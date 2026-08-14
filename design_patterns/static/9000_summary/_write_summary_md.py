"""Regenerate 9000_summary_design_patterns.md with doc + code links."""
from __future__ import annotations

import re
from pathlib import Path

DOCS = Path(r"d:\workspace\tutorials\design_patterns\docs")
PNG = Path(r"d:\workspace\tutorials\design_patterns\static\9000_summary")
OUT = DOCS / "9000_summary_design_patterns.md"
TITLES = Path(r"d:\workspace\tutorials\design_patterns\static\9000_summary\_mmd\titles.txt")

SKIP = {"1510_python_decorator"}

source_re = re.compile(r"Source:\s*\[`([^`]+)`\]\(([^)]+)\)")
title_re = re.compile(r"^#\s+(.+)$", re.M)


def anchor(title: str) -> str:
    a = title.lower()
    for ch in "`@":
        a = a.replace(ch, "")
    a = "".join(c if c.isalnum() or c in " -" else "" for c in a)
    a = a.replace(" ", "-")
    while "--" in a:
        a = a.replace("--", "-")
    return a.strip("-")


entries = []
for line in TITLES.read_text(encoding="utf-8").strip().splitlines():
    stem, title = line.split("|", 1)
    if stem in SKIP:
        continue
    md_path = DOCS / f"{stem}.md"
    text = md_path.read_text(encoding="utf-8") if md_path.exists() else ""
    m = source_re.search(text)
    code_name = m.group(1) if m else None
    code_href = m.group(2) if m else None  # relative from docs/, e.g. ../code/...
    entries.append(
        {
            "stem": stem,
            "title": title,
            "anchor": anchor(title),
            "doc": f"{stem}.md",
            "code_name": code_name,
            "code_href": code_href,
            "has_class": (PNG / f"{stem}_class.png").exists(),
            "has_seq": (PNG / f"{stem}_sequence.png").exists(),
        }
    )

parts = ["# Design Patterns Summary", "", "## On this page", ""]
for e in entries:
    parts.append(f"- [{e['title']}](#{e['anchor']})")
parts.append("")

for e in entries:
    parts.append(f"## {e['title']}")
    parts.append("")
    # links row
    links = [f"[Doc]({e['doc']})"]
    if e["code_name"] and e["code_href"]:
        links.append(f"[Code example]({e['code_href']})")
    parts.append(" · ".join(links))
    parts.append("")

    parts.append("### Class diagram")
    parts.append("")
    if e["has_class"]:
        parts.append(
            f'<p align="center"><img src="../static/9000_summary/{e["stem"]}_class.png" alt="{e["title"]} class diagram" width="85%"></p>'
        )
    else:
        parts.append("*(no class diagram)*")
    parts.append("")

    parts.append("### Sequence diagram")
    parts.append("")
    if e["has_seq"]:
        parts.append(
            f'<p align="center"><img src="../static/9000_summary/{e["stem"]}_sequence.png" alt="{e["title"]} sequence diagram" width="85%"></p>'
        )
    else:
        parts.append("*(no sequence diagram)*")
    parts.append("")
    parts.append("<br/>")
    parts.append("")

parts.extend(
    [
        "<br/>",
        "<p>",
        '    <span style="float: left;">',
        '        <a href="2800_chain_of_responsibility.md">Previous: Chain of Responsibility</a>',
        "    </span>",
        '    <span style="float: right;">',
        '        <a href="../../README.md">Home</a>',
        "        &nbsp;|&nbsp;",
        '        <a href="index.md">Back to Design Patterns Index</a>',
        "    </span>",
        "</p>",
        "",
    ]
)

OUT.write_text("\n".join(parts), encoding="utf-8")
with_code = sum(1 for e in entries if e["code_name"])
print(f"Wrote {OUT.name}: {len(entries)} patterns, {with_code} with code links")
for e in entries:
    flag = e["code_name"] or "-"
    print(f"  {e['stem']}: doc={e['doc']} code={flag}")
