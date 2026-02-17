# IntermediatesGuide

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# The Python intermediate\'s guide: Python packages confusion reducer 

This page assumes

- that you are an experienced software developer, but fairly new to Python,

- that you have mastered enough of Python\'s language constructs and standard library (*\"core packages\"*) to have ventured beyond these into the wider world of Python *extension packages*, and

- that you were confused by what you found.

The aim of this page is to reduce this confusion in a few important spots.

Some recurring sources of such confusion are these:

- Outdated information on Q&A sites (Python has a long history!)

- [Python2 vs. Python3 differences](http://docs.python.org/3/whatsnew/3.0.html)

- Many packages have names different from that of the namespace you will `import` when you use them

- Some closely related packages have widely different names

- Too many packages to choose from for the same purpose

- Understatement: Many packages with zero-point-something version numbers have been stable and mature for years

*Disclaimer:* The primary author of this page is a Python intermediate himself. If an expert could check/correct the statements and then remove this message, that would be most helpful. If this message is still present, beware of errors.

------------------------------------------------------------------------

## Python3 versus Python2 

You should use Python 3 going forward. As of January 2020 [Python 2 will be in EOL (End Of Life) status](https://www.python.org/dev/peps/pep-0373/) and receive no further official support. After that date, there will be no further updates nor bugfixes. Since this end-of-life date has been planned for nearly a decade (the first end-of-life date was slated to happen in 2014, and was pushed back to 2020), and nearly all popular libraries [have already ported their code](https://python3statement.org/), Python 2.x is well on its way to obsolescence. As such, we can only recommend learning and using Python 3.

## Package installation 

- [PyPI](http://pypi.python.org) is for Python what [CPAN](http://www.cpan.org/) is for Perl and what [CTAN](http://ctan.org/) is for TeX: an almost comprehensive catalog of the freely available reusable components.

- For downloading and installing PyPI packages and keeping a set of such installations up to date, [pip](http://www.pip-installer.org) is far more powerful than `easy_install` and should almost always be preferred.

## Multiple isolated Python environments 

By default, packages are installed *into* the local Python installation. They become a part of it and will be available to any Python program on that computer. This can become inconvenient: Sometimes you need different versions of a package for different applications or a certain package must *not* be available for some.

One could avoid this by installing packages elsewhere and manipulating the `PYTHONPATH` environment variable appropriately, but this is inconvenient as well, because packages often depend on many other packages and so this approach can produce immense confustion and giant `PYTHONPATH` lists.

A *virtual environment* behaves like a copy of the Python installation\'s directory tree (with or without the `site-packages` subtree). One can have a separate virtual environment for each project or application to isolate them from each other and install only the required packages into each.

- [venv](http://docs.python.org/3/library/venv.html) implements virtual environments for Python3. It is a core package and technically subtly superior to virtualenv.

You should use a virtual environment for any team project and for any package you intend to distribute.

## Creating a package installer or application installer 

Since Python 2.0, there is a convention that any reusable package or distributable application should have a top level file `setup.py` that implements a command line tool for installation and configuration. This file will

- declare the metadata of the package (name, version, etc.)
- declare the constituent parts of the package (pure Python modules,
  - extension modules in some other language, data files, etc.)
- declare the dependencies of the package:
  - other python packages that must be installed (and the required versions) and other binary libraries required for linking the extension modules after those have been compiled

See the documentation of [distutils](http://docs.python.org/3/distutils/) from the standard library. Distutils will not only make `setup.py` easy to write, it will also provide it with functionality for *creating* the distributable package file in the first place.

In contrast to some other platforms it is common in Python that neither a reusable package nor a distributable application come packaged with all the additional reusable packages they depend on. Rather, the dependencies are only *declared* in `setup.py` and an installer program such as [pip](http://www.pip-installer.org) will download and install additional packages (that are yet missing or the version of which is inappropriate) automatically.

Confusingly, there are multiple frameworks that are used to support `setup.py`:

- `distutils` is a core package (i.e., part of the standard library). Usage: `import distutils`

- `setuptools` is an extension package to extend distutils. Usage: `import setuptools`

- `distribute` was forked off the `setuptools` project. Usage is also `import setuptools`

- `distutils2` was forked off the `distribute` project (by the same team) with the intention to create what could eventually become a new core package, but was later abandoned.

- `distribute` was merged back into `setuptools`.

- `distlib` is an alternative attempt towards a new core package.

- `bento` is an independent alternative framework.

So what should you use? First, be aware that many packages on PyPI will `import setuptools}, so you need to have {{{setuptools` or `distribute` installed in any case. Second, for an up-to-date answer for your own development, see the [summary on stackoverflow](http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2) and the [Python Packaging User Guide recommendation](https://python-packaging-user-guide.readthedocs.org).

## GUI programming 

There is a surprising range of toolkits for building desktop GUIs with Python. One of them, [tkinter](http://docs.python.org/3/library/tkinter.html), is a core package consisting of Python bindings for TCL/TK\'s tk plus additional widgets (in [tkinter.ttk](http://docs.python.org/3/library/tkinter.ttk.html) and [tkinter.tix](http://docs.python.org/3/library/tkinter.tix.html)). tkinter is platform-independent and easy to program for simple GUIs.

For larger applications, you might prefer [a more extensive GUI toolkit](GuiProgramming).

## Web development 

There is a surprising range of frameworks for building web applications with Python. Several of them are quite good. They follow fairly different objectives (such as being slim vs. extensive or regarding the development style they imply). Among these, [Django](https://www.djangoproject.com/) has the largest and most active community by far.

## Object-relational mapping 

There are at least two mature, powerful, and widely used solutions for O/R mapping:

- [sqlalchemy](http://www.sqlalchemy.org/)

- [Django](https://www.djangoproject.com/)\'s persistence framework

Although Django is a web development framework, some people also use it for non-web software in order to make use of its persistence framework.
