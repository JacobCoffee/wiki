# PythonBlogSoftware

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This is a list of web log (\"blog\") software written in Python, organised by category. Please feel free to add to the list or add details.

To start a feature comparison, use the following keys within braces:

a = authentication / authorization b = integrated admin backend for editors (CMS) c = comments h = caching k = pingback / traceback m = markup support n = notifications p = plugin architecture u = multi-user blog system (Twitter-like) r = RSS feed s = data export / import (schema migration) t = topics / categories

## Tools 

- [pyLJclient](http://pyljclient.sourceforge.net)

  - wxPython [LiveJournal](./LiveJournal.html) client

- [pyblogger](https://pyblogger.wordpress.com)

  - wrapper for the Blogger API

- [plagg](https://www.drbeat.li/py/plagg)

  - a RSS/Atom aggregator for (Py)Blosxom

## web2py Based 

- [Instant Press](https://code.google.com/p/instant-press/)

  - Instant Press is an open source CMS developed in the web2py framework. Instant Press is simple, easy to use and attractive.
    - Last Updated Dec 2010

- [Blogitizor](https://code.google.com/p/blogitizor)

  - A blog system developed with web2py. Offers posts, pages,caching, comments, file uploads, import your wordpress data.
    - Last Updated May 2010

- [PyPress](http://web2py.com/appliances/default/show/36)

  - Wordpress Clone made with web2py framework (can run on Google App Engine)

- [TechFuel blog](https://techfuel.net/zblog/default/web2py)

## web.py Based 

- [blog_my](https://www.daltonlp.com/blog_my)

## Zope Based 

- [COREBlog](https://coreblog.org/) // COREBlog was Zope based, COREBlog2 was Plone based, coreblog3 is currently developed and it\'s [Google App Engine](https://coreblog.org/aha) based.

- [Bitakora](https://www.codesyntax.com/bitakora/download)

- [Python Desktop Server](http://pyds.muensterland.org/) // This is a bad link

- [Squishdot](https://www.zope.org/Members/chrisw/Squishdot)

- [simpleblog](https://plone.org/products/simpleblog) [PyPI](https://pypi.python.org/pypi/Products.SimpleBlog/)

  - Zope/plone

- [quills](https://plone.org/products/quills) [PyPI](https://pypi.python.org/pypi/Products.Quills/)

  - Zope/plone

## Django Based 

- [Mumblr](https://github.com/hmarr/django-mumblr/) - utilises MongoDB for storage

  - last updated 2010-09-13

- [Zangetsu](https://svn.pardus.org.tr/projeler/zangetsu/)

  - last updated 2009 (?)

- [Demo](https://cekirdek.pardus.org.tr/~caglar/)

  - \"Gone with the wind\...\" - dead link.

- [Byteflow](http://trac.piranha.org.ua/) - {ckmrt}

  - last updated 2011-03-10 (active)

- [Blogmaker](https://code.google.com/p/blogmaker/) [PyPI](https://pypi.python.org/pypi/Blogmaker)

  - last updated 2009-12-09

- [App Engine Blog](https://developeradvocate.appspot.com/id/1005/AppEngineBlog-(%22AEB%22)-Version-1.1.0-Released)

  - last updated 2010-04-28

- [PyLucid CMS](https://www.pylucid.org) has a built in blog plugin [PyPI](https://pypi.python.org/pypi/PyLucid/) - {chmr}

  - last updated 2011-01-25 (active)

- [Hoydaa Blog](https://www.hoydaa.com/products/blog/) - An extensible Django based blogging software running on Google App Engine.

- [BlogEngine2](https://isotopesoftware.ca/software/blogengine2/) - Versatile blogging framework based on the [django-hotsauce](http://isotopesoftware.ca/software/django-hotsauce/) toolkit. - {achmnpst}

  - last updated 2017-02-15 (active)

  - [Source code](https://bitbucket.org/tkadm30/blogengine2)

- [collective](https://github.com/vicfryzel/collective) - Blog engine with minimal core feature set.

  - last updated 2011-01-08

- [Mezzanine](http://mezzanine.jupo.org/) - CMS with integrated Blog engine.

## TurboGears Based 

- [TurboBlog](https://turboblog.devjavu.com/) [PyPI](https://pypi.python.org/pypi/turboblog/)

- [Quoins - A TurboGears Blogging System](http://quoins.net/)

## Pocoo Libs Based 

- [Zine](http://zine.pocoo.org/) (formerly [Textpress](http://dev.pocoo.org/projects/textpress/))

  - An open source personal publishing platform that inherits many ideas of [WordPress](https://wordpress.com)

  - Written in Python and developed with a focus on security and usability

  - Built on top of Werkzeug, Jinja2 and SQLAlchemy, with [plugins](http://dev.pocoo.org/projects/zine/)

  - last released 2009-01-11

- [HgBlog](https://bitbucket.org/codekoala/hgblog/) [PyPI](https://pypi.python.org/pypi/hgblog/)

  - is a \"set of modifications to the Sphinx project to make it slightly more suitable as a blogging engine\". See also [its page on PyPI](https://pypi.python.org/pypi/hgblog/).

- [Blohg](https://blohg.org/) [PyPI](https://pypi.python.org/pypi/blohg/)

- [Simblin](https://github.com/eugenkiss/Simblin)

- [micro-blog](https://github.com/riquellopes/micro-blog)

## Snakelets Based 

- Frog running on [Snakelets](https://www.razorvine.net/projects/SnakeletsServer.html),

  - As of 20100607, there is only a [Wikipage discussing a Frog reimplementation](https://www.razorvine.net/projects/Frog.html). Frog and Snakelets are no longer publicly available.

  - calendar

  - image embedding or linking

  - multi-user

  - active article overview

  - permalinks

  - Unicode compatible

  - data as XML files on filesystem

  - CSS-based valid layout

## Static 

- [Crotal](https://crotal.org)

  - Generate Static site using jinja2 template engine, markdown syntax
  - Simple, Static and Fast
  - Easy to use
  - Incremental generation.
    - last updated 2014-02

- [Hyde](https://hyde.github.io)

  - Generate static HTML using jinja2 template, markdown syntax,\...
  - Based on Python and Django, heavily inspired by Jekyll
    - last updated 2011-05

- [Blug](https://github.com/jeffknupp/blug)

  - Static site generator for Markdown based posts, including RSS feed and sitemap generation

  - Deep microdata integration - automatic Google Author information support

  - Third party support: Disqus, Google Analytics, Clicky, [GitHub](./GitHub.html), Twitter, Facebook, Google+

  - Includes built-in pure Python web server optimized for static sites
    - last updated 2013-07

- [Blaag](https://bitbucket.org/haard/blaag/)

  - Minimalistic blogging software that generates static HTML from RST source
  - Uses Mercurial for version control
  - Disqus and Google Analytics integration
    - last update 2013-02

- [Tinkerer](https://github.com/vladris/tinkerer)

  - Based on Sphinx
  - Disqus comments, Google Analytics, RSS feed, search function, sidebar widgets

- [Acrylamid](https://github.com/posativ/acrylamid)

  - yet another static blog compiler with fast incremental builds
  - flexible, view-controller inspired configuration
  - Disqus comments, RSS/Atom Feeds, tags, pages, static content, various markup extensions

- [Thot](https://github.com/wmark/thot)

  - Supports YAML; Mako and Jinja2 for templating...
  - ... and several markup formats for input: Markdown, RST, Creole, Trac, plaintext, HTML
  - Can be used with Github for storing articles.
  - RSS/ATOM feed, sitemap.xml, tags and categories, scheduled publication, server-side hyphenation, LaTeX formulas

- [Nikola](https://getnikola.com/)

  - Creates static files with reStructuredText, Markdown, IPython Notebook (and more!) as input

  - Themeable with [Mako](https://www.makotemplates.org/) or [Jinja2](http://jinja.pocoo.org/)

  - Supports multi-language sites, image galleries, the creation of RSS feeds, syntax highlighting, DISQUS and other services for comments

  - Fast builds, thanks to [doit](https://python-doit.sf.net/) (doesn\'t rebuild the entire site at once)

- [mynt](https://github.com/uhnomoli/mynt)

  - Creates static files with markdown as input

  - Themeable with [Jinja2](http://jinja.pocoo.org/)

  - Supports multi-language site

- [Pelican](https://getpelican.com/)

  - Creates static files with reStructuredTest / markdown / [AsciiDoc](./AsciiDoc.html) as input

  - Themeable with [Jinja2](http://jinja.pocoo.org/)

  - Supports multi-language site

## Uncategorized 

- [Bloog](https://bloog.billkatz.com/)

  - Runs on Google App Engine
  - Exposes a REST API

- [Bloggart](https://github.com/Arachnid/bloggart)

  - Runs on Google App Engine

- [Snurf](https://snurf.bdash.net.nz/) // Homepage is down or has been moved

  - uses file-system or Subversion repository for data
  - generates static HTML, RSS and Atom files

- [Firedrop](https://zephyrfalcon.org/weblog/arch_Firedrop.html)

  - last updated 2004-02-14

- [Kaa](https://zephyrfalcon.org/weblog/arch_Kaa.html) [PyPI](https://pypi.python.org/pypi/Kaa/)

  - last updated 2004-04-23

- [Vellum](https://www.kryogenix.org/code/vellum/)

  - {chkmnpt}
  - support for formatted Python code in posts

- [PyBlosxom](https://pyblosxom.bluesock.org/) [PyPI](https://pypi.python.org/pypi/pyblosxom/)

  - {ckmprt}
  - really simple cgi blog with flat file blog posts.
  - lots of plugins.
  - pages load cross-site requests from pyblosxom.bluesock.org

- [NewsBruiser](https://newsbruiser.tigris.org/)

  - last updated 2008-04-27

- [Aether](https://www.logarithmic.net/pfh/aether)

- [Pixie](https://insom.me.uk/blog/2004/07/25/hello-goodbye-pixie/)

  - uses [Quixote](https://www.quixote.ca/)

- [bzero](https://www.myelin.co.nz/bzero/) [PyPI](https://pypi.python.org/pypi/bzero/)

- [Pylogger](https://www.sajjadzaidi.com/pylogger/)

  - Dead link.

- [Byline Server](https://www.pyrite.org/byline/index.html)

- [Leonardo](https://jtauber.com/leonardo)

  - provides a \"personal\" wiki and weblog (including Atom feed)
  - last updated 2009-11-15

- [Syncato](https://syncato.org/)

  - uses [webware](https://www.webwareforpython.org/) as an XML fragment management system

- [PubTal](https://www.owlfish.com/software/PubTal/)

- [Kukkaisvoima](https://23.fi/kukkaisvoima/) Simple one cgi file approach.

  - Multiple categories for one entry
  - No external dependencies outside Pythons standard library (no need for database engine etc.)
  - Comments
  - Nice archive pages for old entries
  - Search
  - RSS feed for all entries and for every category

- [Blogthon](https://www.blogthon.de)
