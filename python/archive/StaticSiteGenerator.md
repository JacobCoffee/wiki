# StaticSiteGenerator

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Static site generator is a software that takes some **text + [templates](Templating)** as input and produces **html files** on the output. A picture:

       ┌──────┐   ┌───────────┐   ┌─────────────┐ **
       │ text │ + │ templates │ = │ .html files │
       └──────┘   └───────────┘   └─────────────┘

Generated site can be a blog, a [game list](https://osgameclones.com), [interactive demo](http://interactive.blockdiag.com) or anything else.

## Static site generators written in Python 

- [VenC](https://github.com/DenisSalem/VenC) - Markdown/Yaml static blog generator with multiple columns layout support. Aim to be light and easy to use. License is GNU/GPLv3

- [Clay](https://lucuma.github.io/Clay/) - Jinja2 for easy site prototyping, MIT.

- [Complexity](https://complexity.readthedocs.io/) - A refreshingly simple static site generator, for those who like to work in HTML.

- [Cyrax](https://github.com/piranha/cyrax) - poetic Jinja2 engine, used for [osgameclones](https://osgameclones.com).

- [html2text](https://github.com/aaronsw/html2text) - useful tool to convert HTML into Markdown.

- [Hyde](https://hyde.github.io) - Jinja2-based static web site generator, MIT, [source](https://github.com/hyde/hyde)

- [Mynt](https://mynt.uhnomoli.com) - Static website generator based on Markdown and Jinja2. BSD-3.

- [Nikola](https://getnikola.com) - Generator supporting reST, Markdown, IPyNB et al.; using Mako and Jinja2 for templates; supports multilingual sites, galleries, RSS feeds, DISQUS et al. for comments. Incremental builds. MIT license.

- [Obraz](https://obraz.pirx.ru) - Static blog-aware site generator mostly compatible with Jekyll, MIT

- [Poole](https://hg.sr.ht/~obensonne/poole) - static website generator, Markdown. GPL.

- [Pelican](https://github.com/getpelican/pelican/) - Uses Markdown or ReST for content and Jinja 2 for themes. Supports DVCS, Disqus. AGPL.

- [PubTal](https://www.owlfish.com/software/PubTal/) - [Templating#SimpleTAL](Templating#SimpleTAL)-based static site generator, BSD-3

- [rest2web](http://www.voidspace.org.uk/python/rest2web/) - Generates Websites from ReST contents, BSD

- [Sphinx](https://www.sphinx-doc.org) - Python\'s official documentation system that turns ReST into HTML, LaTeX, man pages, plaintext, and has many features for making site trees, inter-linking, and other documentation necessities (Jinja2 as default template engine). BSD.

- [staticninja](https://github.com/Ceasar/staticjinja) - MIT, Jinja2, auto-compile. That simple.

- [tahchee](https://pypi.python.org/pypi/Tahchee/1.0.0) - [Cheetah](Cheetah)-based static web site generator

- [tinkerer](https://github.com/vladris/tinkerer) - blogging engine/static website generator powered by Sphinx with polite-correct license list.

- [Urubu](https://urubu.jandecaluwe.com) - A micro CMS for static websites, with a focus on good navigation practices. AGPL.

These are outdated, but worth mentioning:

- [https://www.nthwave.net/elements](https://www.nthwave.net/elements) - powerful tool for experienced web developers from the year 2002, requires at least Python 2.2

See also [static blog generators](https://wiki.python.org/moin/PythonBlogSoftware#Static).

## Dead links for software archaeologists 

The following links have been moved from the section above for the reasons shown in in parentheses.

- [Blogofile](https://www.blogofile.com) - (Mako, Jinja2)-based generator with supports for (reStructuredText, Markdown, Textile), Git, Disqus, RSS feeds, plugins, and S3, very nice license with human touch. (Site no longer responds).

<!-- -->

- [Crotal](https://crotal.org) - (Jinja2)-A static site generator written in Python, using Jinja2 template engine, BSD (No DNS records).

- [wok](https://wok.mythmon.com) - MIT licensed, Jinja2, Markdown, reST, etc. (Site has no HTTPS support).

\*\* [ASCII [diagram](Diagrams) was drawn with Far Manager]
