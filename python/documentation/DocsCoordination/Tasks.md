# DocsCoordination/Tasks

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Tasks 

for the documentation team

## Coding tasks 

for those who want to develop the toolset

**Get into the code**

- The first task for those who want to develop the toolset is to make themselves familiar with it. There are two documents, called `doctools/README`{.backtick} and `doctools/HACKING`{.backtick}, which give a short introduction how to use the command line tools and how the code is laid out. *Feel free to amend!*

**Improvement suggestions**

- I\'d like to ask all of you to look at the new built documentation and collect thoughts about it \-- not the content, but mainly the infrastructure such as navigational elements, accessibility etc.

  Note that the web application does use [JavaScript](./JavaScript.html) in some places, but only for better usability (hopefully). Users without [JavaScript](./JavaScript.html) may not lose any functionality. (This should be confirmed every now and then.)

### The TODO file 

The `doctools/TODO`{.backtick} file lists some things that should be done. At the moment, these are:

**discuss and debug comments system**

- The comments system is quite new and untested. How it deals with inline comments is not ideal.

**write a \"printable\" (PDF) builder (export to latex, most probably)**

- Of course, printable output was trivial for LaTeX sources. The Docutils do have a latex writer (two in fact) \-- if it is stable enough to be used, it has to be extended to support our extra node types. Else, some other conversion must be devised.

**prepare for databases other than sqlite for comments**

- Does sqlite scale well enough for our comments? Though I think so, we should be prepared to make it easy to substitute something like postgres.

**look at the old tools/ scripts, what functionality should be rewritten**

- There were quite a few tools in `Doc/tools/`{.backtick}, e.g. looking which modules were documented. Some of this functionality is obsolete now, some of it may be useful.

**Py-in-the-sky ideas**

- add search via Xapian? optionally have a contents tree view in the sidebar (AJAX based)?

## Content tasks 

**Roundup bugs**

- There are lots of bugs and feature requests in the Python issue tracker at [http://bugs.python.org/](http://bugs.python.org/), and even the occasional patch with category \"Documentation\". However, most of these are pretty big tasks though, such as (mostly obscure or advanced) features that are not documented, or documented not in the official docs, but some essay (new-style classes!). If you tackle an issue, mention the issue number in the commit message or in the patch email, and I will close the report accordingly.

**In the Wiki**

- There are also quite a few wiki pages concerning things missing from the documentation, see [MissingFromDocumentation](MissingFromDocumentation) and [CategoryDocumentation](CategoryDocumentation).

**Python 3000**

- The Python 3.0 docs are still quite out of date; many PEPs and changes mentioned in \"What\'s new in Python 3\" or Misc/NEWS are not documented yet. I\'ve read through the language

reference and done some things myself, but only inserted XXX comments for others.

- Similarly, the library reference is the place where code samples

must be read through and adapted to Python 3 syntax if applicable.
