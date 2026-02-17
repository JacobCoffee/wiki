# StandardLibraryBackports

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The following modules on the Python package index make standard library functionality from later versions of Python available in earlier versions (not all of them are technically backports - some existed on PyPI before being adopted wholesale into the standard library).

- [selectors34](https://pypi.python.org/pypi/selectors34) (Python 3.4+ selectors for 2.6, 2.7 and 3.3)

- faulthandler (Python 3.3+ faulhandler for 2.x and earlier versions of 3.x)

- configparser (Python 3.2+ configparser for 2.x)

- subprocess32 (provides equivalent functionality to the standard library\'s subprocess module as of Python 3.2)

- unittest2 (provides equivalent functionality to the standard library\'s unittest module as of Python 2.7/3.2)

- contextlib2 (provides [ExitStack](./ExitStack.html), in the standard library\'s contextlib module as of Python 3.3)

- funcsigs (in the standard library\'s inspect module as of Python 3.3)

- futures (in the standard library as concurrent.futures as of Python 3.2)

- mock (in the standard library as unittest.mock as of Python 3.3)

- cdecimal (default implementation for the standard library\'s decimal module as of Python 3.3)

- enum34 (in the standard library as enum as of Python 3.3)

- singledispatch (in the standard library\'s functools module as of Python 3.4)

- logutils (logging functionality added in 2.7 and 3.2+, such as `dictConfig`{.backtick} / `QueueHandler`{.backtick} / `QueueListener`{.backtick})

- argparse (included in the standard library since Python 2.7/3.2)

The following modules on PyPI inspired later standard library additions, but have different APIs:

- flufl.enum (initial inspiration for what became the standard library\'s )
- ipaddr (initial inspiration for the standard library\'s ipaddress module as of Python 3.3)
