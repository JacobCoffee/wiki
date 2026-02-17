#!/usr/bin/env python3
"""Convert MoinMoin static HTML wiki archive to Sphinx MyST Markdown.

Usage:
    python scripts/convert.py [--wiki python|psf|jython|all] [--raw-dir _raw] [--out-dir .]

Stages per file:
    1. Extract content from div#content, strip MoinMoin chrome
    2. Decode MoinMoin filename encoding ((20) -> space, (2f) -> /, etc.)
    3. Convert HTML to Markdown via pandoc
    4. Fix internal links to point to new .md paths
    5. Generate toctree index files per section
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import urllib.parse
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from bs4 import BeautifulSoup

WIKIS = ["python", "psf", "jython"]

# MoinMoin meta-pages to exclude from all wikis (English + translated variants)
META_PAGES = {
    # English
    "FindPage", "RecentChanges", "WordIndex", "TitleIndex",
    "AbandonedPages", "OrphanedPages", "EventStats", "PageSize", "PageHits",
    "InterWiki", "SystemInfo", "WikiSandBox", "SystemPagesInEnglishGroup",
    "WantedPages", "DesiredPages", "BadContent", "LocalBadContent",
    "LocalSpellingWords", "PythonCdRawPackageList",
    # German
    "WortIndex", "AufgegebeneSeiten", "GesuchteSeiten",
    # Scandinavian
    "OrdRegister", "OrdListe", "EfterladteSider",
    "SideSt(c3b8)rrelse",  # SideStørrelse - MoinMoin page size stats (Danish)
}

# MoinMoin meta-page prefixes (match encoded filenames starting with these)
META_PREFIXES_ENCODED = {
    "HelpOn",
    "HilfeZu",
    "HilfeZum",
    "SystemPagesIn",
    # Translated meta pages (encoded filenames)
    "(c396)vergivnaSidor",  # ÖvergivnaSidor
    "(c396)nskadeSidor",    # ÖnskadeSidor
    "(c398)nskedeSider",    # ØnskedeSider
    "SideStørrelse",
    "SidStorlek",
    "SeitenGr",             # SeitenGröße
    "SeitenZugriffe",
    "TitelIndex",
    "KategorieKategorie",
    "SidStørrelse",
}

# PSF wiki restricted pages (behind htpasswd auth, not public)
# Source: salt/moin/configs/psf-restricted.conf in python/psf-salt
PSF_RESTRICTED_STEMS = {
    "Action(20)Items",
    "AdminGroup",
    "BadContent",
    "Board",
    "BoardAgenda",
    "BoardGroup",
    "BudgetPlanning",
    "Certification",
    "Certification(20)Blackboard",
    "Certification(20)Proposal",
    "Conference(20)Coordinator(20)2009",
    "Current(20)Nominations",
    "Current(20)PSF(20)Staff(20)and(20)future(20)staff(20)goals",
    "MembersAgenda",
    "MembersGroup",
    "PSFInternalFAQ",
    "PrivatePage",
    "ProposedLogoForPyPI",
    "Secretary",
    "StrategicPlanning",
    "TmcGroup",
    "TrademarksCommittee",
}

# PSF restricted prefixes (pages under these parent pages)
PSF_RESTRICTED_PREFIXES = {
    "Board(2f)",
    "BoardAgenda(2f)",
    "Members(20)Meeting",
    "Membership(20)Map",
    "Nominations",
    "PSF(20)Domains",
    "PSF(20)SSL",
    "ProposalsForDiscussion(2f)",
    "Python(20)Logo(20)Font",
    "Staffing(20)Plan",
    "Streaming(20)PSF",
    "SumanaHarihareswara(2f)",
    "TrademarksCommittee(2f)",
}


def decode_moinmoin_filename(filename: str) -> str:
    """Decode MoinMoin (XX) hex encoding to actual characters.

    Examples:
        'Admin(2f)DNS.html' -> 'Admin/DNS'
        'A(20)new(20)module.html' -> 'A new module'
        'boost(2e)python.html' -> 'boost.python'
    """
    stem = filename.removesuffix(".html")
    decoded = re.sub(
        r"\(([0-9a-fA-F]{2,})\)",
        lambda m: bytes.fromhex(m.group(1)).decode("utf-8", errors="replace"),
        stem,
    )
    return decoded


def sanitize_path(decoded_name: str) -> str:
    """Make decoded name safe for filesystem paths."""
    sanitized = decoded_name.replace(":", "_").replace("?", "_").replace("*", "_")
    sanitized = sanitized.replace('"', "_").replace("<", "_").replace(">", "_").replace("|", "_")
    sanitized = re.sub(r"\s+", " ", sanitized).strip()
    return sanitized


def extract_content(html_path: Path) -> tuple[str, str]:
    """Extract (title, inner_html) from a MoinMoin page."""
    html = html_path.read_text("utf-8", errors="replace")
    soup = BeautifulSoup(html, "html.parser")

    # Title from <title> tag
    title_tag = soup.find("title")
    title = title_tag.text.rsplit(" - ", 1)[0].strip() if title_tag else html_path.stem

    # Content div
    content_div = soup.find("div", id="content")
    if not content_div:
        return title, ""

    # Remove MoinMoin artifacts
    for tag in content_div.find_all("span", class_="anchor"):
        tag.decompose()
    for tag in content_div.find_all("div", id="pagebottom"):
        tag.decompose()
    # Remove inline table of contents (Shibuya sidebar handles this)
    for tag in content_div.find_all("div", class_="table-of-contents"):
        tag.decompose()

    # Return inner HTML only (not the <div id="content"> wrapper)
    return title, content_div.decode_contents()


def html_to_markdown(html_content: str) -> str:
    """Convert HTML fragment to Markdown via pandoc."""
    result = subprocess.run(
        [
            "pandoc", "--from", "html",
            "--to", "markdown-header_attributes-link_attributes-fenced_code_attributes-inline_code_attributes",
            "--wrap", "none", "--no-highlight",
        ],
        input=html_content,
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        return f"<!-- pandoc error: {result.stderr.strip()} -->\n\n{html_content}"
    output = result.stdout
    # Strip any remaining pandoc attribute blocks that MyST can't parse
    output = re.sub(r"\{[.#][^}]*\}", "", output)
    return output


def build_filename_map(raw_dir: Path, wiki_name: str) -> dict[str, str]:
    """First pass: scan all HTML files, build old_filename -> new_path mapping."""
    mapping = {}
    wiki_path = raw_dir / wiki_name
    for html_file in sorted(wiki_path.glob("*.html")):
        old_name = html_file.name
        decoded = decode_moinmoin_filename(old_name)
        sanitized = sanitize_path(decoded)
        mapping[old_name] = sanitized
        # Also map the URL-decoded variant
        mapping[urllib.parse.quote(old_name, safe="")] = sanitized
    return mapping


def fix_links(markdown: str, wiki_name: str, filename_map: dict[str, str]) -> str:
    """Rewrite internal wiki links to point to new Markdown paths."""

    def replace_link(match: re.Match) -> str:
        text = match.group(1)
        url = match.group(2)

        # Skip external links, anchors, mailto
        if url.startswith(("http://", "https://", "mailto:", "#", "ftp://")):
            return match.group(0)

        # Separate anchor
        anchor = ""
        if "#" in url:
            url, anchor = url.rsplit("#", 1)
            anchor = "#" + anchor

        # Strip absolute wiki prefix
        for prefix in [f"/{wiki_name}/", f"/{wiki_name}"]:
            if url.startswith(prefix):
                url = url[len(prefix) :]
                break

        # Strip leading ./ or /
        url = url.lstrip("./")

        # Cross-wiki links
        for other_wiki in WIKIS:
            if url.startswith(f"{other_wiki}/") or url.startswith(f"/{other_wiki}/"):
                url = url.lstrip("/")
                other_name = url.split("/", 1)[1] if "/" in url else url
                if other_name in filename_map:
                    new_path = f"../{other_wiki}/{filename_map[other_name]}"
                    return f"[{text}]({new_path}{anchor})"
                return match.group(0)

        # URL-decode for lookup
        url_decoded = urllib.parse.unquote(url)

        # Try lookup in filename_map
        for candidate in [url, url_decoded, url + ".html", url_decoded + ".html"]:
            if candidate in filename_map:
                new_path = filename_map[candidate]
                return f"[{text}]({new_path}{anchor})"

        return match.group(0)

    return re.sub(r"\[([^\]]*)\]\(([^)]+)\)", replace_link, markdown)


def convert_file(
    html_file: Path,
    wiki_name: str,
    wiki_out: Path,
    filename_map: dict[str, str],
) -> str | None:
    """Convert a single HTML file to Markdown. Returns output path or None on skip."""
    title, html_content = extract_content(html_file)
    if not html_content.strip():
        return None

    markdown = html_to_markdown(html_content)
    markdown = fix_links(markdown, wiki_name, filename_map)

    # Prepend title and import notice
    import_notice = (
        "```{admonition} Legacy Wiki Page\n"
        ":class: note\n\n"
        "This page was migrated from the old MoinMoin-based wiki. "
        "Information may be outdated or no longer applicable. "
        "For current documentation, see [python.org](https://www.python.org).\n"
        "```\n\n"
    )
    markdown = f"# {title}\n\n{import_notice}{markdown}"

    # Determine output path
    new_name = filename_map.get(html_file.name, html_file.stem)
    out_path = wiki_out / (new_name + ".md")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(markdown, encoding="utf-8")
    return str(out_path)


def generate_indexes(wiki_out: Path, wiki_name: str, wiki_title: str) -> None:
    """Generate toctree index files for the wiki section."""
    # Collect all .md files relative to wiki_out
    md_files = sorted(wiki_out.rglob("*.md"))
    # Exclude any existing index.md files
    md_files = [f for f in md_files if f.name != "index.md"]

    # Group by directory
    dirs: dict[Path, list[Path]] = {}
    for md_file in md_files:
        parent = md_file.parent
        if parent not in dirs:
            dirs[parent] = []
        dirs[parent].append(md_file)

    # Generate index for each subdirectory
    for dir_path, files in dirs.items():
        if dir_path == wiki_out:
            continue  # Handle root separately
        rel = dir_path.relative_to(wiki_out)
        index_path = dir_path / "index.md"
        entries = "\n".join(sorted(f.stem for f in files))
        index_path.write_text(
            f"# {rel}\n\n```{{toctree}}\n:maxdepth: 1\n\n{entries}\n```\n",
            encoding="utf-8",
        )

    # Root index for this wiki section
    top_level_files = sorted(f.stem for f in dirs.get(wiki_out, []))
    subdirs = sorted(
        str(d.relative_to(wiki_out)) + "/index"
        for d in dirs
        if d != wiki_out
        and d.parent == wiki_out  # Only immediate subdirectories
    )
    all_entries = subdirs + top_level_files
    entries_str = "\n".join(all_entries)

    root_index = wiki_out / "index.md"
    root_index.write_text(
        f"# {wiki_title}\n\n```{{toctree}}\n:maxdepth: 1\n\n{entries_str}\n```\n",
        encoding="utf-8",
    )


def copy_attachments(raw_dir: Path, wiki_name: str, wiki_out: Path) -> None:
    """Copy attachment files from raw to output."""
    src = raw_dir / wiki_name / "attachments"
    if not src.exists():
        return
    dst = wiki_out / "_attachments"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def convert_wiki(wiki_name: str, raw_dir: Path, out_dir: Path) -> None:
    """Full conversion pipeline for one wiki section."""
    wiki_raw = raw_dir / wiki_name
    if not wiki_raw.exists():
        print(f"  Skipping {wiki_name}: {wiki_raw} not found")
        return

    wiki_out = out_dir / wiki_name
    wiki_out.mkdir(parents=True, exist_ok=True)

    html_files = sorted(wiki_raw.glob("*.html"))
    print(f"  Found {len(html_files)} HTML files")

    # Pass 1: Build filename map
    print("  Building filename map...")
    filename_map = build_filename_map(raw_dir, wiki_name)

    # Pass 2: Filter files, then convert in parallel
    print("  Filtering...")
    files_to_convert = []
    excluded = 0
    for html_file in html_files:
        stem = html_file.stem
        if stem in META_PAGES or any(stem.startswith(p) for p in META_PREFIXES_ENCODED):
            excluded += 1
            continue
        if wiki_name == "psf":
            if stem in PSF_RESTRICTED_STEMS or any(stem.startswith(p) for p in PSF_RESTRICTED_PREFIXES):
                excluded += 1
                continue
        files_to_convert.append(html_file)

    print(f"  Converting {len(files_to_convert)} files ({excluded} excluded)...")
    converted = 0
    skipped = 0
    import os
    workers = os.cpu_count() or 4
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(convert_file, f, wiki_name, wiki_out, filename_map): f
            for f in files_to_convert
        }
        for future in as_completed(futures):
            result = future.result()
            if result:
                converted += 1
            else:
                skipped += 1

    print(f"  Converted: {converted}, Skipped: {skipped}, Excluded: {excluded}")

    # Pass 3: Generate toctree indexes
    print("  Generating index files...")
    titles = {"python": "Python Wiki", "psf": "PSF Wiki", "jython": "Jython Wiki"}
    generate_indexes(wiki_out, wiki_name, titles.get(wiki_name, wiki_name))

    # Pass 4: Copy attachments
    print("  Copying attachments...")
    copy_attachments(raw_dir, wiki_name, wiki_out)

    print(f"  Done with {wiki_name}!")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert MoinMoin HTML to Sphinx Markdown")
    parser.add_argument("--wiki", default="all", help="Which wiki to convert (python|psf|jython|all)")
    parser.add_argument("--raw-dir", default="_raw", help="Path to raw HTML directory")
    parser.add_argument("--out-dir", default=".", help="Path to output directory (project root)")
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir).resolve()
    out_dir = Path(args.out_dir).resolve()

    if not raw_dir.exists():
        print(f"Error: Raw directory {raw_dir} not found. Run scripts/sync.sh first.")
        raise SystemExit(1)

    # Check pandoc
    try:
        subprocess.run(["pandoc", "--version"], capture_output=True, check=True)
    except FileNotFoundError:
        print("Error: pandoc not found. Install with: brew install pandoc")
        raise SystemExit(1)

    wikis = WIKIS if args.wiki == "all" else [args.wiki]

    for wiki_name in wikis:
        print(f"\n{'='*60}")
        print(f"Converting {wiki_name} wiki")
        print(f"{'='*60}")
        convert_wiki(wiki_name, raw_dir, out_dir)

    print(f"\nAll done! Build with: sphinx-build -b html {out_dir} {out_dir}/_build/html -j auto")


if __name__ == "__main__":
    main()
