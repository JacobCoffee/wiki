# Firebird

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Firebird 

URL

:   [https://firebirdsql.org](https://firebirdsql.org/)

licence
:   Interbase Public License, Initial Developer Public License

platforms
:   Unix, Win 32/x64, Mac OS X

## Pros 

- Powerful and stable cross-platform database

- Extensive SQL standards support

- Python driver binary distribution available for : Mageia ,Fedora, Redhat , FreeBSD (Debian, Ubuntu will come soon) but you can to compile and install easily for other platforms : [here](http://mapopa.blogspot.ro/2012/04/i-love-pip-install.html) is the Howto install it on Ubuntu with pip.

------------------------------------------------------------------------

## DB API 2.0 Drivers 

#### Python 2.x-3.x Driver (Official Stable) 

Pure python ctypes based driver (fbclient library is required) is located in svn repository (All official driver development is done in this repository) In addition to feature set of the standard Python DB API, fdb also exposes nearly the entire native client API of the database engine, including two-phase commit, server-side events, and an administrative API.

URL

:   [https://firebirdsql.org/en/python-driver/](https://firebirdsql.org/en/python-driver/)

GIT

:   [https://github.com/FirebirdSQL/fdb](https://github.com/FirebirdSQL/fdb)

pypi

:   [https://pypi.python.org/pypi/fdb/](https://pypi.python.org/pypi/fdb/)

Documentation

:   [https://pythonhosted.org/fdb/](https://pythonhosted.org/fdb/)

Python versions
:   2.7 - 3.x

It was tested with cpython

#### Pure Python 3.x Driver 

New pure python 3.x driver (no C compiler needed or fbclient library) development is located on github repository

URL

:   [https://github.com/nakagami/pyfirebirdsql](https://github.com/nakagami/pyfirebirdsql)

pypi

:   [https://pypi.python.org/pypi/firebirdsql/](https://pypi.python.org/pypi/firebirdsql/)

Documentation

:   [https://nakagami.github.com/pyfirebirdsql/](https://nakagami.github.com/pyfirebirdsql/)

Python versions
:   3.x

It was tested with cpython , jython, ironpython and pypy
