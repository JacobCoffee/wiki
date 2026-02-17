# ContentManagementSystems

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# 1. Content Management Systems 

A content management system (CMS) might be simply defined as a system which supports the publishing or sharing, editing or manipulation, searching and indexing, archival or versioning of content, frequently documents, typically using Web technologies. A more extensive definition can be found in the [Wikipedia topic entry](http://en.wikipedia.org/wiki/Content_management_system).

In plainer terms, content management systems are the applications used to manage Web sites where the writers, editors and users are able to upload, edit and manage content without needing to know too many of the technical details about how the site actually works.

Python-based products, although in the minority in the larger market of CMSs, possess several inherent advantages. Python\'s [Unicode](Unicode) capabilities, for example, make its derived products particularly popular in continental Europe and Asia, as compared to those based on PHP, Ruby, and so on.

## 1.1. Zope-based Solutions 

The most established Python-based content management systems are those derived from [Zope](Zope), notably [Plone](http://www.plone.org), [Nuxeo CPS](http://www.cps-project.org) (starting with v5 Nuxeo switched to Java as its development platform), [Silva](http://www.infrae.com/products/silva), [ZMS](http://www.zms-publishing.com) and [KARL](http://karlproject.org). These solutions have been used in large scale and high profile deployments over a number of years, and a range of organisations provide support and services for those solutions.

## 1.2. Non-Zope Solutions 

For those wanting non-Zope CMS solutions, there are a few options which may provide at least some of the features found in the more established solutions mentioned above, and the solutions mentioned below may be targeted more towards developers than individuals or organizations wishing to immediately deploy a complete and working solution.

- [ACRCms](https://bitbucket.org/axant/acrcms) Flexible Web CMS based on Turbogears and SQLAlchemy

- [BAOW](http://sourceforge.net/projects/peo/) is a lightweight content management system based on SQL database (Firebird/InterBase, MySQL, PostgreSQL, SQLite). v1.1 released: 2005-07-07

- [Django](http://www.djangoproject.com/) offers elementary support for content management (and was initially derived from the lower levels of a commercial content management system).

- [django-cms](http://www.django-cms.org/) written on top of django. Provides a full cms stack with the power of a webframework under it. Easily extendable.

- [ikaaro](http://www.hforge.org/ikaaro) offers content management functionality. v0.62.9 released: 2012-05-28

- [Kotti](http://pypi.python.org/pypi/Kotti) is a high-level, *Pythonic* web application framework, with a built-in CMS. Kotti is based on Pyramid and SQLAlchemy. v0.9.2 released: 2013-10-15

- [KPAX](http://www.vimeo.com/1098656) is a complete CMS solution based on [web2py](http://www.web2py.com). It provides wikis, blogs, news, rss feeds, surveys, assignments, web pages, versioning, group based roles, Central Authentication System, upload and downloading media streaming, embedded media player, wysiwyg editor, ajax search, customizable templates. Works with SQLite, MySQL, PostgreSQL, Oracle or MSSQL. Can be downloaded from the web2py [appliances repository](http://www.web2py.com/appliances)

- [Leonardo](http://leonardo.pyworks.org/) extensible content management system, architected in a REST-like style. Initially focused on providing for personal websites with a password-protected wiki and blog (including Atom feed). It can be run as CGI and uses the filesystem as a database. v0.7.0 released: 2006-03-09

- [Madpy](http://www.madpy.org/) is built on top of [apache](http://www.apache.org/) , [mod_python](http://www.modpython.org/) , [postgresql](http://www.postgresql.org/) and [cheetah templates](http://www.cheetahtemplate.org/). Supports creating content in more than one language, clean url\'s , url to object mapping and madata an MVC like mechanism.

- [MediaCore Video CMS](http://mediacore.com/) is an open source media focused content management system. It features video & audio support, [YouTube](./YouTube.html) & Vimeo integration, podcasting, iTunes RSS generation, user-submitted content, embedded media player, wysiwg edior, search, and is highly customizable. There is both a front-end for users and a back-end for administrators. It is built upon Pylons, SQLAlchemy, MYSQL and runs with Apache, Fast_CGI or Mod_WSGI.

- [Merengue](http://www.merengueproject.org/) is a fully featured CMS framework built on top of [Django framework](http://www.djangoproject.com/). It's not only a plug-and-play CMS but a framework to build CMS sites at top speed with clean and re-usable code.

- [Mezzanine](http://mezzanine.jupo.org) is a content management platform built using the Django framework. It is BSD licensed and designed to provide both a consistent interface for managing content, and a simple, extensible architecture that makes diving in and hacking on the code as easy as possible.

- [Opps CMS](http://www.oppsproject.org/) A Django-based CMS for the magazines, newspappers websites and portals with high-traffic, [Source](https://github.com/opps/opps)

- [PyLucid](http://www.pylucid.org) is a lightweight CMS written in Python WSGI. No shell account is needed. To run PyLucid you need a standard Web server with Python (at least v2.3), CGI and mySQLdb.

- [Pyplate](http://www.pyplate.com/) is a simple SQLite CMS containing most of the basic features needed to build simple web sites. Static page generation makes for great performance, and the UI makes admin tasks easy.

- [Quokka CMS](http://www.quokkaproject.org/) Flask and MongoDB powered CMS, [github](https://github.com/pythonhub/quokka).

- [Skeletonz](http://orangoo.com/skeletonz/) is simple, powerful, extensible, reliable. Has been in development since October 2005. Ajax based editor with spell checking & UTF-8 support. High performance: best result is around 600 request/sec. Open source, GNU GPL.

- [teeny_tiny_cms](http://cvs.sourceforge.net/viewcvs.py/webware-sandbox/Sandbox/fbar/teeny_tiny_cms/) runs on [Webware](./Webware.html) and uses SQLObject, SQLite and Docutils. Link is broken.

- [Tendenci](http://tendenci.org) is an open source CMS specifically developed for nonprofit and association websites. Tendenci is written in Python on a Django framework, includes a plugin builder for easily adding additional, custom plugins, and has all the features nonprofits need in a complex website including integration with merchant account for online payments, event calendar and event registration, membership management, job board, business directories, and more. Tendenci\'s public repository can be found on Github: [https://github.com/tendenci/tendenci](https://github.com/tendenci/tendenci).

### 1.2.1. Wiki Solutions 

Despite their simple beginnings, many wiki solutions offer many of the capabilities listed above. Numerous wiki projects have been written in Python. The following are the most widely deployed:

- [MoinMoin](MoinMoin) is the solution used to publish and manage the information on this page!

- [Trac](http://trac.edgewall.org/) provides a wiki within a larger solution for the management of software projects and project information \-- bug tracking, source browsing, and so on.

- See a more complete list of wiki solutions on the [PythonWikiEngines](PythonWikiEngines) page.

## 1.3. Editorial Notes 

The above lists should be arranged in ascending alphabetical order - please respect this when adding new solutions. When specifying release dates please use the format YYYY-MM-DD.
