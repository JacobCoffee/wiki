#!/usr/bin/env python3
"""Generate redirects from old MoinMoin-encoded URLs to new decoded paths.

Old wiki URLs use hex encoding like (c384) for special characters:
    /jython/Aktuelle(c384)nderungen.html -> /jython/AktuelleÄnderungen

This script scans the raw HTML files, builds a mapping of encoded -> decoded
filenames, and merges them into _redirects.json for sphinxext.rediraffe.

Only generates redirects for pages that actually exist in the built site
(not excluded or deleted pages).

Usage:
    python scripts/gen_old_wiki_redirects.py [--dry-run] [--raw-dir .claude/raw]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

WIKIS = ["python", "psf", "jython"]


def decode_moinmoin_filename(filename: str) -> str:
    """Decode MoinMoin (XX) hex encoding to actual characters."""
    stem = filename.removesuffix(".html")
    return re.sub(
        r"\(([0-9a-fA-F]{2,})\)",
        lambda m: bytes.fromhex(m.group(1)).decode("utf-8", errors="replace"),
        stem,
    )


def sanitize_path(decoded_name: str) -> str:
    """Make decoded name safe for filesystem paths."""
    sanitized = decoded_name.replace(":", "_").replace("?", "_").replace("*", "_")
    sanitized = sanitized.replace('"', "_").replace("<", "_").replace(">", "_").replace("|", "_")
    sanitized = re.sub(r"\s+", " ", sanitized).strip()
    return sanitized


def has_encoding(name: str) -> bool:
    """Check if a filename contains MoinMoin hex encoding."""
    return bool(re.search(r"\([0-9a-fA-F]{2,}\)", name))


def main() -> None:
    dry_run = "--dry-run" in sys.argv
    raw_dir = Path(".claude/raw")

    for arg in sys.argv[1:]:
        if arg.startswith("--raw-dir="):
            raw_dir = Path(arg.split("=", 1)[1])
        elif arg == "--raw-dir":
            idx = sys.argv.index(arg)
            raw_dir = Path(sys.argv[idx + 1])

    if not raw_dir.exists():
        print(f"Raw directory {raw_dir} not found")
        raise SystemExit(1)

    # Load existing redirects
    redirects_path = Path("_redirects.json")
    if redirects_path.exists():
        existing = json.loads(redirects_path.read_text())
    else:
        existing = {}

    # Collect all current .md files for target validation
    current_pages = set()
    for wiki in WIKIS:
        wiki_path = Path(wiki)
        if wiki_path.exists():
            for md in wiki_path.rglob("*.md"):
                # Store without .md extension, relative to root
                current_pages.add(str(md.with_suffix("")))

    # Also check _exclude for pages that were reorganized (follow redirect chains)
    excluded_pages = set()
    exclude_path = Path("_exclude")
    if exclude_path.exists():
        for md in exclude_path.rglob("*.md"):
            rel = str(md.relative_to(exclude_path).with_suffix(""))
            excluded_pages.add(rel)

    new_redirects = {}
    skipped_no_target = 0
    skipped_same = 0

    for wiki in WIKIS:
        wiki_raw = raw_dir / wiki
        if not wiki_raw.exists():
            continue

        for html_file in sorted(wiki_raw.glob("*.html")):
            name = html_file.stem
            if not has_encoding(name):
                continue

            decoded = decode_moinmoin_filename(html_file.name)
            sanitized = sanitize_path(decoded)

            # The old URL path (what MoinMoin served)
            old_path = f"{wiki}/{name}"
            # The new path (decoded filename)
            new_path = f"{wiki}/{sanitized}"

            if old_path == new_path:
                skipped_same += 1
                continue

            # Check if the target exists in the current site
            if new_path in current_pages:
                new_redirects[old_path] = new_path
            elif new_path in existing:
                # Target was already redirected somewhere else (reorganization),
                # chain through to final destination
                new_redirects[old_path] = existing[new_path]
            else:
                skipped_no_target += 1

    print(f"Found {len(new_redirects)} old wiki redirects to add")
    print(f"Skipped {skipped_no_target} (target page doesn't exist)")
    print(f"Skipped {skipped_same} (encoding decoded to same name)")

    if dry_run:
        for old, new in sorted(new_redirects.items())[:20]:
            print(f"  {old} -> {new}")
        if len(new_redirects) > 20:
            print(f"  ... and {len(new_redirects) - 20} more")
        return

    # Merge with existing (old wiki redirects don't override reorganization redirects)
    merged = {**existing}
    added = 0
    for old, new in new_redirects.items():
        if old not in merged:
            merged[old] = new
            added += 1

    redirects_path.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {added} new redirects ({len(merged)} total in _redirects.json)")


if __name__ == "__main__":
    main()
