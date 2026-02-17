# PyCon2006/Sprints/DocutilsSprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: 
Contents

- [Preliminaries](#preliminaries)
- [Sprinters](#sprinters)
- [Nested Inline Markup](#nested-inline-markup)
- [Plugins](#plugins)
- [Schedule](#schedule)
- [Topics](#topics)
- [Comments](#comments)
:::

::: 
### [Preliminaries](#id6)

The Docutils sprint at PyConTX2006 was held over 4 days, from 9:00 Monday February 27 through Thursday March 2 inclusive. There was no cost to attend the sprints beyond being present at PyCon. For introductory information and information about the other sprints going on at PyConTX2006, please see [PyCon2006/Sprints](). Also see the [Docutils home page](http://docutils.sourceforge.net) and the [reStructuredText home page](http://docutils.sourceforge.net/rst.html). The PyCon DC 2004 Docutils sprint details are here: [DocutilsSprint](DocutilsSprint).

Please feel free to add your comments here (prefered); I\'ll be notified of all changes to this page. If you can\'t edit the wiki, you can [email me](mailto:goodger@python.org).

If you cannot attend the Docutils sprints in person but would still like to follow the progress and/or participate, you can, via Internet Relay Chat ([irc.freenode.net, channel #docutils](irc://irc.freenode.net#docutils)).
:::

::: 
### [Sprinters](#id7)

Everyone is welcome! No prior Docutils hacking experience is required. Participants should be one or more of:

- experienced Python programmers
- interested in text/documentation processing
- users of Docutils/reStructuredText

Sprinters planning to attend:

- [David Goodger](mailto:goodger@python.org) (coach)
- [Felix Wiemann](mailto:Felix.Wiemann@ososo.de)
- [Thomas Drake](mailto:bistroy@mac.com) (Monday, Tuesday, Wednesday)
- [pythondrs@drstovallfoundation.com](mailto:pythondrs@drstovallfoundation.com) (I\'m ready anytime but I am on WinXP in Singapore Internet cafe)
- [John Gill](mailto:swfiua@gmail.com) (Monday, Tuesday)
- Facundo Batista

Please add your name to the list above or [email me](mailto:goodger@python.org).
:::

::: 
### [Nested Inline Markup](#id8)

Things that we may need to think about when adding nested inline markup:

    `foo :bar:`/baz` qux`   (inline start-string probably takes priority)
    ***foo** bar*
    ***foo* bar**
    ******************************foo******************************

The inline parser must determine whether a role contains literal or parsed text before it starts parsing the contents:

    :raw:`This *contains ``uninterpreted `markup`

We probably have to disallow (or at least deprecate) postfix notation for literal (or for all) roles, because of this:

    `contents`:raw:    // This happens to work
    `This *contains ``uninterpreted `markup`:raw:

In the latter case, the parser cannot know at the time it parses the role contents that they are literal
:::

::: 
### [Plugins](#id9)

Other projects with plugin mechanisms:

- [On Plug-ins and Extensible Architectures](http://www.acmqueue.org/modules.php?name=Content&pa=printer_friendly&pid=286&page=2)
- [The Firedrop Plugin System](http://www.voidspace.org.uk/python/firedrop_plugins.html)
- [Twisted Documentation: The Twisted Plugin System](http://twistedmatrix.com/users/warner/doc-latest/core/howto/plugin.html)
- [TurboGears Plugins](http://www.turbogears.org/docs/plugins/index.html)
- [The Firedrop2 Plugin System](http://www.voidspace.org.uk/python/firedrop2/plugins.html)
- [MoinDev/PluginConcept - MoinMoin](http://moinmoin.wikiwikiweb.de/MoinDev/PluginConcept)
:::

::: 
### [Schedule](#id10)

We will begin the sprint with an interactive overview of the Docutils architecture and codebase. Then we will determine sprint topics and get hacking! Sprinters are free to work alone, work in pairs (pair programming), or however they feel comfortable.
:::

::: 
### [Topics](#id11)

The topics below are in no particular order. Please feel free to add topics & comments.

- Python source reader (autodocumentation subsystem). Ideas:
  - [PEP 258](http://docutils.sf.net/docs/peps/pep-0258.html#python-source-reader)
  - [a detailed exploration of some ideas](http://docutils.sf.net/docs/dev/pysource.html)
  - [to-do items](http://docutils.sf.net/docs/dev/todo.html#python-source-reader)
- Writers (output formats):
  - DocPy (Python\'s dialect of LaTeX) writer completion. This would allow easier entry for documentation newbies, and \"make authorship more accessible\" ([initial implementation](http://docutils.sf.net/sandbox/edloper/docpy/)).
  - OpenDocument writer.
  - DocBook writer ([initial implementation in Oliver Rutherfurd\'s sandbox](http://docutils.sf.net/sandbox/oliverr/docbook/))
  - RTF writer
- [Large document issues](http://docutils.sf.net/docs/dev/todo.html#large-documents), including [formal elements](http://docutils.sf.net/docs/dev/todo.html#object-numbering-and-object-references)
- Nested inline markup
- [Math markup](http://docutils.sf.net/docs/dev/todo.html#math-markup).
- Documentation:
  - Complete \"[The Docutils Document Tree](http://docutils.sf.net/spec/doctree.html)\" reference.
- [Squash bugs!](http://docutils.sf.net/BUGS.html)
- Add internationalization to [footer boilerplate text](http://docutils.sf.net/docs/dev/todo.html#footer-boilerplate-text).
- [Adaptable file extensions](http://docutils.sf.net/docs/dev/todo.html#adaptable-file-extensions).

There are more ideas in the [Docutils to-do list](http://docutils.sf.net/docs/dev/todo.html).
:::

::: 
### [Comments](#id12)

Please feel free to add any comments you like below. Please include your name & email address for feedback; anonymous comments are OK too. I hope to see you at PyCon! \-- David Goodger

A source reader that several people (including myself) are using is [Pudge](http://pudge.lesscode.org), which has proven useful but also has lots of room for work. It provides quite a few features that aren\'t exactly reST-specific, but those are features that really fill it out into a useful tool, and are the kind of features that kind of complete the experience of using reST so that it really feels like a nice way to document code. A lot of its issues aren\'t about restructured-text per se, but if the project was really turned into a nice polished piece of work it would certainly help many of the people people who use restructured text. \-- Ian Bicking
:::
