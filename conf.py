"""Sphinx configuration for the Python Wiki."""

from __future__ import annotations

import os
from datetime import datetime

project = "Python Wiki"
copyright = f"{datetime.now().year}, Python Software Foundation"
author = "Python Community"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build", "_raw", "scripts", ".github", ".claude",
    "Thumbs.db", ".DS_Store", "venv", ".venv",
    "node_modules", "uv.lock", "pyproject.toml", "Makefile",
    "**/_attachments",
]

# Allow building a single wiki section: WIKI=python|psf|jython
_wiki_only = os.environ.get("WIKI")
if _wiki_only:
    _all_wikis = {"python", "psf", "jython"}
    for _w in _all_wikis - {_wiki_only}:
        exclude_patterns.append(f"{_w}/**")

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
    "replacements",
    "smartquotes",
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

html_context = {
    "source_type": "github",
    "source_user": "JacobCoffee",
    "source_repo": "wiki",
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
