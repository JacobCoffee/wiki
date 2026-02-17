"""Sphinx configuration for the Python Wiki."""

from __future__ import annotations

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
exclude_patterns = ["_build", "_raw", "scripts", ".github", "Thumbs.db", ".DS_Store", "venv", ".venv"]

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
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_heading_anchors = 3

# Suppress warnings from converted MoinMoin content
suppress_warnings = [
    "myst.header",
    "myst.xref_missing",
    "myst.directive_unknown",
    "misc.highlighting_failure",
    "image.not_readable",
    "toc.not_included",
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

html_theme_options = {
    "accent_color": "blue",
    "github_url": "https://github.com/psf/wiki",
    "nav_links": [
        {"title": "Python Wiki", "url": "python/index"},
        {"title": "PSF Wiki", "url": "psf/index"},
        {"title": "Jython Wiki", "url": "jython/index"},
    ],
}
