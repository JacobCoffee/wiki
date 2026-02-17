#!/usr/bin/env python3
"""Strip pandoc-style attribute blocks ({.class}, {#id}, {key="val"}) from all .md files.

These are valid in pandoc markdown but cause MyST parser to spend enormous time
trying (and failing) to parse them as directive syntax, making Sphinx builds 10x slower.

Usage:
    python scripts/strip_attrs.py [--dry-run]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Matches pandoc attribute blocks like {.https}, {.nonexistent}, {#some-id},
# {height="300" width="600"}, {.class #id key=val}, etc.
# Does NOT match MyST directives like ```{admonition} or ```{toctree}
ATTR_PATTERN = re.compile(
    r"(?<!`)"           # not preceded by backtick (avoid ```{directive})
    r"\{"
    r"(?=[.#]|[a-z]+=)"  # must start with .class, #id, or key=
    r"[^}\n]+"
    r"\}"
)


def strip_file(path: Path, dry_run: bool = False) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    new_text, count = ATTR_PATTERN.subn("", text)
    if count > 0 and not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return count


def main() -> None:
    dry_run = "--dry-run" in sys.argv
    root = Path(".")
    total_files = 0
    total_attrs = 0

    for wiki in ("python", "psf", "jython"):
        wiki_path = root / wiki
        if not wiki_path.exists():
            continue
        for md_file in sorted(wiki_path.rglob("*.md")):
            count = strip_file(md_file, dry_run)
            if count:
                total_files += 1
                total_attrs += count
                if dry_run:
                    print(f"  {md_file}: {count} attributes")

    action = "Would strip" if dry_run else "Stripped"
    print(f"{action} {total_attrs} pandoc attributes from {total_files} files")


if __name__ == "__main__":
    main()
