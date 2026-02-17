# Distutils/Terminology

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python terminology 

## General Python terminology 

If you're reading this document, you probably have a good idea of what modules, extensions, and so forth are. Nevertheless, just to be sure that everyone is operating from a common starting point, we offer the following glossary of common Python terms:

**module**

- the basic unit of code reusability in Python: a block of code imported by some other code. Three types of modules concern us here: pure Python modules, extension modules, and packages.

**pure Python module**

- a module written in Python and contained in a single .py file (and possibly associated .pyc and/or .pyo files). Sometimes referred to as a "pure module."

**extension module**

- a module written in the low-level language of the Python implementation: C/C++ for Python, Java for Jython. Typically contained in a single dynamically loadable pre-compiled file, e.g. a shared object (.so) file for Python extensions on Unix, a DLL (given the .pyd extension) for Python extensions on Windows, or a Java class file for Jython extensions. (Note that currently, the Distutils only handles C/C++ extensions for Python.)

**package**

- a module that contains other modules; typically contained in a directory in the filesystem and distinguished from other directories by the presence of a file [init].py.

**root package**

- the root of the hierarchy of packages. (This isn't really a package, since it doesn't have an [init].py file. But we have to call it something.) The vast majority of the standard library is in the root package, as are many small, standalone third-party modules that don't belong to a larger module collection. Unlike regular packages, modules in the root package can be found in many directories: in fact, every directory listed in sys.path contributes modules to the root package.

## Distutils-specific terminology 

The following terms apply more specifically to the domain of distributing Python modules using the Distutils:

**module distribution**

- a collection of Python modules distributed together as a single downloadable resource, usually a file, and meant to be installed. A single module distribution may contain zero, one, or many Python packages or modules. Sometimes, \*package\* is improperly used as a synonymous of module distribution, in the broader sense of container of modules (suited for installation or distribution) or in the software package sense, but this use is ambiguous and should be avoided. An acceptable shorter form for \*module distribution\* is \*distribution\*.

**pure module distribution**

- a module distribution that contains only pure Python modules and packages. Sometimes referred to as a "pure distribution."

**non-pure module distribution**

- a module distribution that contains at least one extension module. Sometimes referred to as a "non-pure distribution."

**distribution root**

- the top-level directory of your source tree (or source distribution); the directory where setup.py exists. Generally setup.py will be run from this directory.

**project**

- a given set of software and the process and/or community which produces that software. A project is usually identified by a name which should try be unique to avoid confusion with other projects.

**release**

- a set of one or more distributions of a project, each sharing the same version but which may vary in target platforms, features\...

To show how these terms fit, we can use the Mercurial project as an example.

The project publishes, for its 1.4.2 version release, a set of different distributions.

There\'s one source distribution (mercurial-1.4.2.tar.gz), a windows specific distribution using an executable format (mercurial-1.4.2.exe) and two OSX specific distributions, targeted at different OS versions (Mercurial-1.4.2-py2.6-macosx10.6.zip and Mercurial-1.4.2-py2.5-macosx10.5.zip).

## Further discussion 

Discussion goes here?

Rafael: One practical solution to the current use of **package** as synonymous of **distribution** in informal language may be adding further qualification to existing terms, so the term becomes legal.

The proposal would be changing **package** into **module package** and **(module) distribution** into **distribution package**. That would allow either maintain the existing **package** vs **distribution** terms or qualifying package as **distribution package** or **module package** when more context is needed.
