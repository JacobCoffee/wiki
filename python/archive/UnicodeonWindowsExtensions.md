# UnicodeonWindowsExtensions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Add unicode returning versions of sys.argv and os.environ; unicode accepting functions for running processes like os.popen\*, os.system, os.exec\*. After experience implementing some of these, the implementer should look at ways to simplify coding functions that take either unicode or byte strings. The existing unicode method implementations such as open do not work in 32 bit unicode string builds so this could be fixed along with finding a way to make coding extension functions for either 16 or 32 bit wide unicode strings easier. \-- Neil

More ideas:

\- Allow unicode entries on sys.path (without converting them to ascii string internally). There\'s already a patch on SF for Python/import.c. \-- theller

\- Convert the \_winreg extension module to handle unicode without converting them. \-- theller
