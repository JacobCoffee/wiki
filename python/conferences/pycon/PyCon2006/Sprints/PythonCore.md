# PyCon2006/Sprints/PythonCore

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Possible Topics 

- Implementing PEPs
  - PEP 328 absolute/relative import

  - PEP 343 implementation (\'with:\')

  - PEP 308 implementation (\'x if y else z\')

  - PEP 302 suggestions (fix pydoc and traceback printing to support zipfiles, implement sys.meta_path objects for built-in, frozen, and sys.path importers; search for \"phase 2\" in the PEP for other ideas)

  - PEP 352 (exception hierarchy)

  - any other PEPs Guido might OK @ [PyCon](PyCon) (PEP 352, 357, etc.)
- AST work
  - export AST to Python
    - Basic pychecker functionality
  - rewrite peepholer to use AST instead of modifying bytecode directly (where applicable)
  - Finish work on ast-objects branch (it\'s leaking refs)
  - Clean up the Grammar file
- Patch/bug processing
  - Incorporate PEP content into the LaTeX docs

  - Bugs to look at: [777884](http://bugs.python.org/issue777884 "SF") (needs ruling from an XML/minidom maintainer)

  - Patches to look at: [686545](http://bugs.python.org/issue686545 "SF") (mailbox modification \-- SoC-supported work)

  - Bugs/patches left over from last Bug Day ([PythonBugDayStatus](./PythonBugDayStatus.html))

  - [BuildBot](BuildBot)-discovered bugs ([http://wiki.python.org/moin/BuildBot](http://wiki.python.org/moin/BuildBot) and [http://www.python.org/dev/buildbot/](http://www.python.org/dev/buildbot/))
- Build
  - Rewrite setup.py (for simplification and easier customization)
- Hash out bytes type
- Rewrite fileobject to avoid C stdio
- Implement final decision on outputting integers in different bases
- rewrite setup.py

# Attendees 

- Brett Cannon
- Thomas Wouters
- John Ehresman (probably)
