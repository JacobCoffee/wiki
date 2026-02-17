"""Fix MoinMoin-encoded links in wiki markdown files after reorganization.

Handles:
- MoinMoin URL encoding: (20) -> space, (2f) -> /, (2d) -> -, (2e) -> .
- .html suffix stripping
- Relative path resolution from original file locations
- Rewriting links to use new organized paths
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Regex to detect MoinMoin-encoded sequences
MOIN_HEX_RE = re.compile(r"\([0-9a-fA-F]{2}\)")


def decode_moin(s: str) -> str:
    """Decode MoinMoin URL encoding in a string."""
    def _decode_hex(m: re.Match) -> str:
        hex_str = m.group(0)[1:-1]
        try:
            return chr(int(hex_str, 16))
        except ValueError:
            return m.group(0)
    return MOIN_HEX_RE.sub(_decode_hex, s)


def has_moin_encoding(s: str) -> bool:
    """Check if string contains MoinMoin URL encoding."""
    return bool(MOIN_HEX_RE.search(s))


def find_md_links(text: str) -> list[tuple[int, int, str, str]]:
    """Find markdown links, handling MoinMoin (XX) encoding in URLs.

    Returns list of (start, end, label, href) tuples.
    Uses character-by-character scanning to correctly handle parentheses.
    """
    results = []
    i = 0
    n = len(text)

    while i < n:
        # Find next [
        idx = text.find("[", i)
        if idx == -1:
            break

        # Find matching ]
        j = idx + 1
        bracket_depth = 1
        while j < n and bracket_depth > 0:
            if text[j] == "[":
                bracket_depth += 1
            elif text[j] == "]":
                bracket_depth -= 1
            j += 1

        if bracket_depth != 0:
            i = idx + 1
            continue

        label_end = j  # j is one past the ]
        label = text[idx + 1 : label_end - 1]

        # Must be followed by (
        if label_end >= n or text[label_end] != "(":
            i = label_end
            continue

        # Scan for matching ) - but allow (XX) hex sequences
        k = label_end + 1
        href_start = k
        paren_depth = 1

        while k < n and paren_depth > 0:
            ch = text[k]
            if ch == "(":
                # Check if this is a MoinMoin hex sequence (XX)
                if k + 3 < n and text[k + 3] == ")" and all(
                    c in "0123456789abcdefABCDEF" for c in text[k + 1 : k + 3]
                ):
                    # Skip over (XX) entirely
                    k += 4
                    continue
                paren_depth += 1
            elif ch == ")":
                paren_depth -= 1
                if paren_depth == 0:
                    break
            elif ch in ("\n", "\r"):
                # Links don't span lines
                break
            k += 1

        if paren_depth != 0:
            i = label_end
            continue

        href = text[href_start:k]
        results.append((idx, k + 1, label, href))
        i = k + 1

    return results


def build_reverse_map(redirects: dict[str, str]) -> dict[str, str]:
    """Build new_path -> old_path mapping."""
    return {v: k for k, v in redirects.items()}


def resolve_link(
    href: str,
    current_docname: str,
    redirects: dict[str, str],
    reverse_map: dict[str, str],
) -> str | None:
    """Resolve a MoinMoin-encoded link to its new path."""
    decoded = decode_moin(href)

    if decoded.endswith(".html"):
        decoded = decoded[:-5]
    if decoded.startswith("./"):
        decoded = decoded[2:]

    # Find the original location of the current file
    original_docname = reverse_map.get(current_docname, current_docname)
    original_dir = "/".join(original_docname.split("/")[:-1])
    wiki_prefix = original_docname.split("/")[0] if "/" in original_docname else ""

    # Build candidate docnames to look up (in priority order)
    candidates = []

    # 1. Relative to original directory
    if original_dir:
        candidates.append(f"{original_dir}/{decoded}")

    # 2. Wiki-root-relative (e.g., psf/ConductWG/Charter)
    if wiki_prefix:
        candidates.append(f"{wiki_prefix}/{decoded}")

    # 3. As-is (absolute path)
    candidates.append(decoded)

    # Look up each candidate in redirect map
    for candidate in candidates:
        if candidate in redirects:
            return redirects[candidate]

    # Check if already exists on disk
    for candidate in candidates:
        for suffix in (".md", "/index.md"):
            if (REPO_ROOT / (candidate + suffix)).exists():
                return candidate

    return None


def make_relative(from_docname: str, to_docname: str) -> str:
    """Create a relative path from one docname to another."""
    from_parts = from_docname.split("/")[:-1]
    to_parts = to_docname.split("/")

    common = 0
    for a, b in zip(from_parts, to_parts):
        if a == b:
            common += 1
        else:
            break

    ups = len(from_parts) - common
    rel_parts = [".."] * ups + to_parts[common:]
    return "/".join(rel_parts)


def fix_file(
    file_path: Path,
    redirects: dict[str, str],
    reverse_map: dict[str, str],
    stats: dict,
) -> bool:
    """Fix links in a single file. Returns True if modified."""
    try:
        text = file_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return False

    current_docname = str(file_path.relative_to(REPO_ROOT)).removesuffix(".md")
    links = find_md_links(text)

    replacements = []  # (start, end, new_text)

    for start, end, label, href in links:
        if href.startswith(("http://", "https://", "#", "mailto:", "ftp://")):
            continue

        needs_fix = has_moin_encoding(href) or (
            href.startswith("./") and href.endswith(".html")
        )
        if not needs_fix:
            continue

        new_docname = resolve_link(href, current_docname, redirects, reverse_map)
        if new_docname is None:
            stats["unresolved"] += 1
            stats["unresolved_links"].append(
                (str(file_path.relative_to(REPO_ROOT)), href)
            )
            continue

        rel_path = make_relative(current_docname, new_docname)
        replacements.append((start, end, f"[{label}]({rel_path})"))
        stats["fixed"] += 1

    if not replacements:
        return False

    # Apply replacements in reverse order to preserve offsets
    parts = []
    prev = 0
    for start, end, new_text in sorted(replacements, key=lambda x: x[0]):
        parts.append(text[prev:start])
        parts.append(new_text)
        prev = end
    parts.append(text[prev:])

    file_path.write_text("".join(parts), encoding="utf-8")
    return True


def main() -> None:
    redirects_path = REPO_ROOT / "_redirects.json"
    redirects: dict[str, str] = json.loads(redirects_path.read_text())
    reverse_map = build_reverse_map(redirects)

    print(f"Loaded {len(redirects)} redirects")

    stats = {"fixed": 0, "unresolved": 0, "files_modified": 0, "unresolved_links": []}

    for wiki in ("python", "psf", "jython"):
        base = REPO_ROOT / wiki
        if not base.exists():
            continue
        for md in sorted(base.rglob("*.md")):
            if "_attachments" in str(md) or "_exclude" in str(md):
                continue
            if fix_file(md, redirects, reverse_map, stats):
                stats["files_modified"] += 1

    print(f"\nResults:")
    print(f"  Files modified: {stats['files_modified']}")
    print(f"  Links fixed: {stats['fixed']}")
    print(f"  Links unresolved: {stats['unresolved']}")

    if stats["unresolved_links"]:
        print(f"\nUnresolved links (first 50):")
        for file, href in stats["unresolved_links"][:50]:
            print(f"  {file}: {href}")


if __name__ == "__main__":
    main()
