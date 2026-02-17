# RPM

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

RPM is a package format used by Fedora, Red Hat and some other Linux distributions. So if you want to make your package available there, you need to know how to create RPMs.

Before Python 3 there was a `bdist_rpm`{.backtick} command, which had gone in `packaging`{.backtick} (Distutils2). If you\'re interested to know - ask Tarek (and don\'t forget to update the info here). Now there are two packages to help make .rpm out of Python package (setup.py?):

- Tarek\'s [pypi2rpm](https://bitbucket.org/tarek/pypi2rpm) - aims at providing the same features and much more

- [py2pack](http://pypi.python.org/pypi/py2pack) by Sascha Peilicke.

### Comparison 

- **Availability**

  - PyPI
    - py2pack - [version 0.2.11](http://pypi.python.org/pypi/py2pack/0.2.11) uploaded to PyPI on 2010-12-11

    - pypi2rpm - [version 0.1](http://pypi.python.org/pypi/pypi2rpm/0.1) uploaded on 2010-10-28
  - Fedora (because you want to use supported RPM package to build RPM\'s, obviously)
    - py2pack - [Yes](https://admin.fedoraproject.org/pkgdb/acls/name/python-py2pack)

    - pypi2rpm - No
