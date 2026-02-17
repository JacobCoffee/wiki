# Distutils/Projects

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# A list of Distutils-related Project 

Please add a listing to this page if you\'re working on Distutils (and help us reduce duplication of effort).

## PyPI 

The central repository of Python package metadata and distribution files. See: [CheeseShopDev](CheeseShopDev)

## Easy Install 

A Python package manager that downloads, builds, installs, upgrades, and switches between package versions automatically (using Python Eggs). See: [http://peak.telecommunity.com/DevCenter/EasyInstall](http://peak.telecommunity.com/DevCenter/EasyInstall)

## Python Eggs 

An effort to produce single-file distributions of packages similar to Java JARs. See: [http://peak.telecommunity.com/DevCenter/PythonEggs](http://peak.telecommunity.com/DevCenter/PythonEggs)

## Paver 

[Paver](http://www.blueskyonmars.com/projects/paver/): Easy Scripting for Software Projects

## PEPs for extending distutils / PyPI 

PEPs 262 \"Database of Installed Python Packages\" and 345 \"Metadata for Python Software Packages 1.2\" are currently open

## zpkgtools

A source-based packaging system. See: [http://www.zope.org/Members/fdrake/zpkgtools/](http://www.zope.org/Members/fdrake/zpkgtools/)

## stdeb

Build debian source packages using setuptools and the \"sdist\" distutils command. See: [http://github.com/astraw/stdeb](http://github.com/astraw/stdeb)

## Distribute 

[Distribute](Distribute) A community-driven project that aims to gather all requirements for a future distribution package.

## Defend Against Fruit 

[Defend Against Fruit](http://teamfruit.github.io/defend_against_fruit/): A continuous deployment focused extension to Distribute supporting [Artifactory Pro](http://www.jfrog.com/home/v_artifactorypro_overview) as a PyPI server. See: [http://teamfruit.github.io/defend_against_fruit/](http://teamfruit.github.io/defend_against_fruit/)

## Other efforts we know about 

- Ian Bicking is looking to clean up and extend the use of release_urls in PyPI for use in [Paste](http://pythonpaste.org).

- Maurice Ling is looking at implementing PEP 262 as an academic project.

- Geoffrey T. Dairiki has a bdist_deb command [http://bugs.python.org/1054967](http://bugs.python.org/1054967)

- [eGenix](http://www.egenix.com/) uses its own extensions to distutils in the various egenix-mx packages called mxSetup.py. Among other things this module contains support for building Unix libraries, limited autoconf support, uninstall command and a clever build_ext command that allows to disable building extensions/packages from the command line and also supports building optional extensions (depending on the availability of certain include and library files).
