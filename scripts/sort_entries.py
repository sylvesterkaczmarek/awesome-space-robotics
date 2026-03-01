#!/usr/bin/env python3

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"

TOP_ENTRY_RE = re.compile(r"^- \[(.+?)\]")
SUB_ENTRY_RE = re.compile(r"^  - \[")


def sort_key(entry_lines: list[str]) -> str:
    match = TOP_ENTRY_RE.match(entry_lines[0])
    if match:
        return match.group(1).lower()
    return entry_lines[0].lower()


def sort_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    result: list[str] = []
    entry_group: list[list[str]] = []
    current_entry: list[str] | None = None

    def flush_group() -> None:
        if not entry_group:
            return
        sorted_group = sorted(entry_group, key=sort_key)
        for entry in sorted_group:
            result.extend(entry)
        entry_group.clear()

    def flush_current() -> None:
        nonlocal current_entry
        if current_entry is not None:
            entry_group.append(current_entry)
            current_entry = None

    for line in lines:
        stripped = line.rstrip("\n")

        if TOP_ENTRY_RE.match(stripped):
            flush_current()
            current_entry = [line]
        elif SUB_ENTRY_RE.match(stripped) and current_entry is not None:
            current_entry.append(line)
        else:
            flush_current()
            flush_group()
            result.append(line)

    flush_current()
    flush_group()

    new_text = "".join(result)
    if new_text == text:
        return False

    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    md_files = sorted(SRC_DIR.rglob("*.md"))
    skip = {"SUMMARY.md", "README.md", "contributors.md"}
    md_files = [f for f in md_files if f.name not in skip]

    modified = []
    for path in md_files:
        if sort_file(path):
            modified.append(path)

    if modified:
        for path in modified:
            print(f"Sorted entries in {path.relative_to(REPO_ROOT)}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
