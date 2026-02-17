# PipAndDistutils2

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[Pip](http://www.pip-installer.org/) is a popular installer and uninstaller of Python packages. Currently, pip depends on the third-party packaging extensions in [setuptools](http://peak.telecommunity.com/DevCenter/setuptools), or the [distribute](http://packages.python.org/distribute/) fork. The future of Python packaging is [distutils2](http://distutils2.notmyidea.org/) (\"packaging\" in the Python 3.3+ standard library), and pip should gain support for using distutils2/packaging as an alternative to setuptools/distribute (though setuptools/distribute support needs to be maintained as well for some time to come).

Possible areas of work for a proposal here:

- Adding support for installing distutils2-style projects (with setup.cfg and possibly no setup.py, [PEP 345](http://www.python.org/dev/peps/pep-0345/) metadata), by using the appropriate distutils2 APIs.

- Adding support for introspecting and uninstalling [PEP 376](http://www.python.org/dev/peps/pep-0376/)-style installed distributions, again using distutils2 APIs wherever possible.

- Charting areas of overlap between pip and distutils2 and modifying pip to optionally prefer distutils2 APIs, if available, for areas of functional overlap (e.g. finding candidate distributions for installation).

Work has been started under the [pip2](https://github.com/osupython/pip2) name.
