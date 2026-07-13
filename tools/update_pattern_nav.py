"""Merge prev/next and home/index footers in design pattern docs."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "design_patterns" / "docs"

OLD_FOOTER = re.compile(
    r"(?:<br/>\s*)?"
    r'<p align="right">\s*\n'
    r"(?P<nav>(?:\s*<a href=\"[^\"]+\">(?:Previous|Next)[^<]*</a>\s*)+)"
    r"\n</p>\s*\n"
    r'<p align="right">\s*\n'
    r'\s*<a href="../../README.md">Home</a>\s*\n'
    r"\s*&nbsp;\|\&nbsp;\s*\n"
    r'\s*<a href="index.md">Back to Design Patterns Index</a>\s*\n'
    r"</p>",
    re.MULTILINE,
)

LINK = re.compile(r'<a href="([^"]+)">([^<]+)</a>')


def format_nav_links(nav_block: str) -> str:
    links = LINK.findall(nav_block)
    lines = []
    for i, (href, label) in enumerate(links):
        if i:
            lines.append("        &nbsp;")
        lines.append(f'        <a href="{href}">{label}</a>')
    return "\n".join(lines)


def build_footer(nav_block: str) -> str:
    nav = format_nav_links(nav_block)
    return (
        "<br/>\n"
        "<p>\n"
        '    <span style="float: left;">\n'
        f"{nav}\n"
        "    </span>\n"
        '    <span style="float: right;">\n'
        '        <a href="../../README.md">Home</a>\n'
        "        &nbsp;|&nbsp;\n"
        '        <a href="index.md">Back to Design Patterns Index</a>\n'
        "    </span>\n"
        "</p>"
    )


def main() -> None:
    updated: list[str] = []
    for path in sorted(DOCS.glob("*.md")):
        if path.name == "index.md":
            continue
        content = path.read_text(encoding="utf-8")
        if 'style="float: left;"' in content:
            continue
        match = OLD_FOOTER.search(content)
        if not match:
            print(f"SKIP (no match): {path.name}")
            continue
        new_content = OLD_FOOTER.sub(build_footer(match.group("nav")), content, count=1)
        if new_content != content:
            path.write_text(new_content, encoding="utf-8")
            updated.append(path.name)
    print(f"Updated {len(updated)} files")
    for name in updated:
        print(f"  {name}")


if __name__ == "__main__":
    main()
