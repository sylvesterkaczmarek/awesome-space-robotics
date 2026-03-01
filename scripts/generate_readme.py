#!/usr/bin/env python3

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"
SUMMARY_FILE = SRC_DIR / "SUMMARY.md"
README_FILE = REPO_ROOT / "README.md"

BEGIN_MARKER = "<!-- BEGIN GENERATED CONTENT -->"
END_MARKER = "<!-- END GENERATED CONTENT -->"


def parse_summary() -> list[tuple[str, str, str]]:
    entries: list[tuple[str, str, str]] = []
    summary_text = SUMMARY_FILE.read_text(encoding="utf-8")

    for line in summary_text.splitlines():
        stripped = line.strip()

        if not stripped:
            continue

        if stripped.startswith("___"):
            entries.append(("separator", "", ""))
            continue

        part_match = re.match(r"^#\s+(.+)$", stripped)
        if part_match:
            entries.append(("part", part_match.group(1), ""))
            continue

        chapter_match = re.match(r"^-\s+\[(.+?)\]\((.+?)\)$", stripped)
        if chapter_match:
            title = chapter_match.group(1)
            path = chapter_match.group(2)
            entries.append(("chapter", title, path))
            continue

        link_match = re.match(r"^\[(.+?)\]\((.+?)\)$", stripped)
        if link_match:
            entries.append(("link", link_match.group(1), link_match.group(2)))
            continue

    return entries


def read_chapter_content(rel_path: str) -> str:
    file_path = SRC_DIR / rel_path
    if not file_path.exists():
        return ""

    text = file_path.read_text(encoding="utf-8").strip()
    lines = text.splitlines()

    if lines and lines[0].startswith("# "):
        lines = lines[1:]

    content = "\n".join(lines).strip()
    return content


def bump_headings(text: str, levels: int = 1) -> str:
    def replace_heading(match: re.Match) -> str:
        hashes = match.group(1)
        title = match.group(2)
        new_hashes = "#" * (len(hashes) + levels)
        return f"{new_hashes} {title}"

    return re.sub(r"^(#{1,6})\s+(.+)$", replace_heading, text, flags=re.MULTILINE)


def heading_to_anchor(text: str) -> str:
    return re.sub(r"[^\w\s-]", "", text.lower()).replace(" ", "-")


def generate_toc(entries: list[tuple[str, str, str]]) -> str:
    toc_lines: list[str] = []
    for entry_type, title, path in entries:
        if entry_type == "separator" or entry_type == "link":
            continue
        if entry_type == "part":
            anchor = heading_to_anchor(title)
            toc_lines.append(f"- [{title}](#{anchor})")
        elif entry_type == "chapter":
            content = read_chapter_content(path)
            if content:
                anchor = heading_to_anchor(title)
                toc_lines.append(f"  - [{title}](#{anchor})")
    return "\n".join(toc_lines)


def generate_content() -> str:
    entries = parse_summary()

    toc = generate_toc(entries)
    parts: list[str] = ["## Contents\n", toc, ""]

    for entry_type, title, path in entries:
        if entry_type == "separator":
            continue
        if entry_type == "link":
            continue
        if entry_type == "part":
            parts.append(f"## {title}\n")
            continue
        if entry_type == "chapter":
            content = read_chapter_content(path)
            if content:
                parts.append(f"### {title}\n")
                bumped = bump_headings(content, levels=2)
                parts.append(bumped)
                parts.append("")

    return "\n".join(parts).strip()


def main() -> int:
    if not README_FILE.exists():
        print(f"Error: {README_FILE} not found", file=sys.stderr)
        return 1

    old_content = README_FILE.read_text(encoding="utf-8")

    begin_idx = old_content.find(BEGIN_MARKER)
    end_idx = old_content.find(END_MARKER)

    if begin_idx == -1 or end_idx == -1:
        print(
            f"Error: markers not found in {README_FILE}. "
            f"Ensure both {BEGIN_MARKER!r} and {END_MARKER!r} are present.",
            file=sys.stderr,
        )
        return 1

    generated = generate_content()
    new_section = BEGIN_MARKER + "\n\n" + generated + "\n\n" + END_MARKER

    new_content = (
        old_content[:begin_idx] + new_section + old_content[end_idx + len(END_MARKER) :]
    )

    if new_content == old_content:
        return 0

    README_FILE.write_text(new_content, encoding="utf-8")
    print(f"Updated {README_FILE}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
