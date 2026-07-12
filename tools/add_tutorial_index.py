"""Add 'On this page' indexes and back links to tutorial markdown files."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_FILES = {ROOT / "README.md"}

PARENT_INDEX = {
    "design_patterns/docs": ("Design Patterns Index", "index.md"),
    "design_patterns": ("Tutorials Index", "../README.md"),
    "python/docs": ("Python Index", "../README.md"),
    "python": ("Tutorials Index", "../README.md"),
    "git/docs": ("Git Index", "../README.md"),
    "git": ("Tutorials Index", "../README.md"),
    "mermaid/docs": ("Mermaid Index", "../README.md"),
    "mermaid": ("Tutorials Index", "../README.md"),
    "uml/docs": ("UML Index", "../README.md"),
    "uml": ("Tutorials Index", "../README.md"),
    "es/query": ("Elasticsearch Index", "../index.md"),
    "es": ("Tutorials Index", "../README.md"),
}


def slugify_heading(text: str) -> str:
    text = re.sub(r"\*\*|__|`", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text or "section"


def assign_slug(text: str, counts: dict[str, int | None]) -> str:
    base = slugify_heading(text)
    if base not in counts:
        counts[base] = None
        return base
    if counts[base] is None:
        counts[base] = 1
    else:
        counts[base] += 1
    return f"{base}-{counts[base]}"


def get_parent_info(path: Path) -> tuple[str, str] | None:
    rel = path.relative_to(ROOT).as_posix()
    parts = path.relative_to(ROOT).parts

    if rel.endswith("index.md"):
        if "design_patterns/docs" in rel or parts[0] == "es":
            return ("Tutorials Index", "../README.md")

    for key in sorted(PARENT_INDEX, key=len, reverse=True):
        if rel.startswith(key + "/") or rel == key or rel == key + ".md":
            if rel.endswith("README.md") and key.count("/") == 0:
                return PARENT_INDEX[key]
            if "/docs/" in rel or "/query/" in rel:
                for k in sorted(PARENT_INDEX, key=len, reverse=True):
                    if rel.startswith(k + "/"):
                        return PARENT_INDEX[k]
            return PARENT_INDEX.get(key)
    if len(parts) >= 2 and parts[1] == "docs":
        return (f"{parts[0].title()} Index", "../README.md")
    return None


def extract_headings(content: str) -> list[str]:
    headings: list[str] = []
    seen_title = False
    in_fence = False
    for line in content.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("# ") and not line.startswith("## "):
            if not seen_title:
                seen_title = True
                continue
            title = line[2:].strip()
            if title.lower() != "on this page":
                headings.append(title)
        elif line.startswith("## ") and not line.startswith("### "):
            title = line[3:].strip()
            if title.lower() != "on this page":
                headings.append(title)
    return headings


def build_toc(headings: list[str]) -> str:
    counts: dict[str, int | None] = {}
    lines = ["## On this page", ""]
    for heading in headings:
        if heading.lower() == "on this page":
            continue
        anchor = assign_slug(heading, counts)
        lines.append(f"- [{heading}](#{anchor})")
    lines.append("")
    return "\n".join(lines)


def build_back_link(label: str, href: str) -> str:
    return f'<p align="right">\n    <a href="{href}">Back to {label}</a>\n</p>'


def remove_existing_on_this_page(content: str) -> str:
    pattern = re.compile(
        r"## On this page\n(?:.*?\n)*?(?=\n## |\n---|\n<p align=\"right\">|\Z)",
        re.MULTILINE,
    )
    return pattern.sub("", content, count=1)


def remove_all_back_links(content: str) -> str:
    pattern = re.compile(
        r'\n<p align="right">\s*\n\s*<a href="[^"]+">Back to [^<]+</a>\s*\n</p>',
        re.MULTILINE,
    )
    return pattern.sub("", content)


def normalize_title_spacing(lines: list[str]) -> list[str]:
    if not lines or not lines[0].startswith("# "):
        return lines
    i = 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    return [lines[0], ""] + lines[i:]


def insert_index(content: str, path: Path) -> str | None:
    parent = get_parent_info(path)
    headings = extract_headings(content)
    if not headings and not parent:
        return None

    content = remove_existing_on_this_page(content)
    content = remove_all_back_links(content)

    lines = normalize_title_spacing(content.splitlines())
    if not lines or not lines[0].startswith("# "):
        return None

    blocks: list[str] = []
    if headings:
        blocks.extend(build_toc(headings).splitlines())
        blocks.append("")

    new_lines = lines[:2] + blocks + lines[2:]
    result = "\n".join(new_lines).rstrip()

    if parent:
        label, href = parent
        result += "\n\n" + build_back_link(label, href) + "\n"
    elif not result.endswith("\n"):
        result += "\n"

    if not result.endswith("\n"):
        result += "\n"
    return result


def main() -> None:
    updated: list[str] = []
    skipped: list[str] = []
    for path in sorted(ROOT.rglob("*.md")):
        if path in SKIP_FILES:
            continue
        rel = path.relative_to(ROOT)
        if rel.parts[0].startswith("."):
            continue

        original = path.read_text(encoding="utf-8")
        new_content = insert_index(original, path)
        if new_content is None:
            skipped.append(str(rel))
            continue
        if new_content != original:
            path.write_text(new_content, encoding="utf-8")
            updated.append(str(rel))

    print(f"Updated {len(updated)} files")
    for item in updated:
        print(f"  {item}")
    if skipped:
        print(f"Skipped {len(skipped)} files (no H2 headings or no title)")


if __name__ == "__main__":
    main()
