"""Sphinx configuration for the Python Wiki."""

from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).parent / "oauth"))
# Autodoc imports oauth/app.py which reads these at module level
os.environ.setdefault("GITHUB_CLIENT_ID", "docs-placeholder")
os.environ.setdefault("GITHUB_CLIENT_SECRET", "docs-placeholder")

project = "Python Wiki"
copyright = f"{datetime.now().year}, Python Software Foundation"
author = "Python Community"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxcontrib.openapi",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build", "_raw", "_exclude", "_redirects_html", "scripts", ".github", ".claude",
    "Thumbs.db", ".DS_Store", "venv", ".venv",
    "node_modules", "uv.lock", "pyproject.toml", "Makefile",
    "**/_attachments", "_extra", "oauth",
]

# Allow building a single wiki section or subsection:
#   WIKI=psf                       - build only the PSF wiki
#   WIKI=psf SECTION=PackagingWG   - build only psf/PackagingWG
#   WIKI=python SECTION=Advocacy   - build only python/Advocacy
_wiki_only = os.environ.get("WIKI")
if _wiki_only:
    _all_wikis = {"python", "psf", "jython"}
    for _w in _all_wikis - {_wiki_only}:
        exclude_patterns.append(f"{_w}/**")

    _section = os.environ.get("SECTION")
    if _section:
        # Exclude all sibling subdirectories and top-level pages in the wiki,
        # keeping only: the target section, the wiki's index.md, and root index.md
        from pathlib import Path

        _wiki_path = Path(_wiki_only)
        if _wiki_path.is_dir():
            # Exclude sibling subdirectories
            for _d in _wiki_path.iterdir():
                if _d.is_dir() and _d.name != _section and _d.name != "_attachments":
                    exclude_patterns.append(f"{_wiki_only}/{_d.name}/**")
            # Exclude top-level .md files except the wiki's own index
            for _f in _wiki_path.glob("*.md"):
                if _f.name != "index.md":
                    exclude_patterns.append(f"{_wiki_only}/{_f.name}")

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

master_doc = "index"
language = "en"

# -- MyST configuration ------------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",  # disabled: very slow on 3500+ files of converted wiki content
    # "replacements",  # disabled: converts .. to ellipsis inside link URLs, breaking 4786 relative links
    # "smartquotes",  # disabled: unnecessary for wiki content, marginal perf cost
    "strikethrough",
    "tasklist",
]
myst_heading_anchors = 0

# Suppress warnings from converted MoinMoin content
suppress_warnings = [
    "myst.header",
    "myst.xref_missing",
    "myst.directive_unknown",
    "myst.substitution",
    "toc.not_readable",
    "toc.excluded",
    "misc.highlighting_failure",
    "image.not_readable",
    "toc.not_included",
    "ref.doc",
    "docutils",
]

# -- Copy button settings ----------------------------------------------------
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True
copybutton_remove_prompts = True

# -- HTML output -------------------------------------------------------------
html_theme = "shibuya"
html_title = "Python Wiki"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_show_sourcelink = False
html_extra_path = ["_redirects_html", "_extra"]

html_context = {
    "source_type": "github",
    "source_user": "JacobCoffee",
    "source_repo": "wiki",
    "source_docs_path": "/",
}

html_theme_options = {
    "accent_color": "blue",
    "github_url": "https://github.com/JacobCoffee/wiki",
    "twitter_url": "https://x.com/ThePSF",
    "mastodon_url": "https://fosstodon.org/@ThePSF",
    "linkedin_url": "https://www.linkedin.com/company/thepsf",
    "nav_links": [
        {"title": "Python Wiki", "url": "python/index"},
        {"title": "PSF Wiki", "url": "psf/index"},
        {"title": "Jython Wiki", "url": "jython/index"},
    ],
}


# -- Redirects ---------------------------------------------------------------
# Static redirect HTML files live in _redirects_html/ and are copied into the
# build output via html_extra_path. To regenerate:
#   python scripts/gen_redirect_pages.py
# To update the source mapping:
#   python scripts/gen_old_wiki_redirects.py
