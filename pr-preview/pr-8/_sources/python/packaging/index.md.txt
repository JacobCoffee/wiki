# Packaging

Python packaging has a long and tangled history. Distutils shipped in 1.6, setuptools added features (and complexity), distribute forked setuptools, distutils2 tried to start fresh, and eventually pip and the Python Packaging Authority brought some order to it all. This section captures that entire arc -- design documents, sprint notes, proposals, surveys, and tool-specific pages. A lot of it is historical, but it is useful history if you want to understand why packaging works the way it does today.

## Overviews and Tools

- [Packaging](Packaging) -- status page for the standard library `packaging` module (what distutils2 became, briefly, in Python 3.3)
- [Packaging subpages](Packaging/index) -- sprint notes and related proposals
- [Distutils](Distutils) -- the original packaging system, shipped with Python since 1.6
- [Distutils subpages](Distutils/index) -- proposals and related distutils documentation
- [Distutils2](Distutils2) -- the clean-room rewrite of distutils, developed outside the standard library
- [Distutils2 subpages](Distutils2/index) -- contributing guidelines, sprint setup, and related docs
- [Distribute](Distribute) -- the project that forked setuptools to rethink distutils' future
- [Distribute subpages](Distribute/index) -- additional distribute documentation
- [EasyInstall](EasyInstall) -- setuptools' `easy_install` command for remote package installation
- [SetuptoolsFeatures](SetuptoolsFeatures) -- mapping setuptools features to their distutils2/packaging equivalents
- [Virtualenv](Virtualenv) -- tool for creating isolated Python environments
- [buildout](buildout) -- Zope-originated build system for managing eggs and deployment
- [buildout subpages](buildout/index) -- additional buildout documentation

## PyPI (The Python Package Index)

- [PyPI](PyPI) -- overview of the Python Package Index
- [PyPI subpages](PyPI/index) -- additional PyPI documentation
- [A new pypi module](A%20new%20pypi%20module) -- draft PEP by Tarek Ziade for a `pypi` package in the standard library
- [CloudPyPI](CloudPyPI) -- canceled project to mirror PyPI on Amazon CloudFront (now unnecessary since PyPI uses Fastly)
- [CloudPyPI subpages](CloudPyPI/index) -- additional CloudPyPI documentation
- [PyPIComments](PyPIComments) -- discussion about per-package commenting and rating on PyPI
- [PyPISimple](PyPISimple) -- documentation for PyPI's Simple API
- [PyPITestingInfrastructure](PyPITestingInfrastructure) -- infrastructure for testing and analyzing PyPI packages
- [PipAndDistutils2](PipAndDistutils2) -- plans for pip to support distutils2/packaging alongside setuptools

## Sprints, BOFs, and Community Discussions

- [DistributeSprint](DistributeSprint) -- sprint to work on distutils PEPs
- [DistutilsBof](DistutilsBof) -- distutils birds-of-a-feather meeting notes
- [DistutilsMetadata](DistutilsMetadata) -- notes on distutils metadata (stub page)
- [DistutilsSprint](DistutilsSprint) -- distutils development sprint
- [DistutilsTesting](DistutilsTesting) -- discussion of functional testing for distutils
- [PackagingBOF](PackagingBOF) -- packaging birds-of-a-feather meeting summary
- [Packaging Survey](Packaging%20Survey) -- community survey about packaging workflows
- [PackagingPy2Porting](PackagingPy2Porting) -- strategy for backporting the `packaging` module to Python 2.4-3.2
- [SummerOfCode subpages](SummerOfCode/index) -- Google Summer of Code packaging projects

## Related Topics

- [DistributedProgramming](DistributedProgramming) -- guide to distributed computing in Python (CORBA, XML-RPC, SOAP, and more)

```{toctree}
:hidden:
:maxdepth: 1

CloudPyPI/index
Distribute/index
Distutils/index
Distutils2/index
Packaging/index
PyPI/index
SummerOfCode/index
buildout/index
A new pypi module
CloudPyPI
Distribute
DistributeSprint
DistributedProgramming
Distutils
Distutils2
DistutilsBof
DistutilsMetadata
DistutilsSprint
DistutilsTesting
EasyInstall
Packaging
Packaging Survey
PackagingBOF
PackagingPy2Porting
PipAndDistutils2
PyPI
PyPIComments
PyPISimple
PyPITestingInfrastructure
SetuptoolsFeatures
Virtualenv
buildout
```
