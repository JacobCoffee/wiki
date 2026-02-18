# Packaging/Sprints/DocumentationSprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## 1. Packaging Sprint 2/3 April 2011 

### 1.1. Schedule 

Start at 9:00am EST on Saturday and Sunday.

### 1.2. Participants 

- Kelsey Hightower(Lead) - Atlanta (online) (2/3)
- Elson Rodriguez - Atlanta (online) (2/3)
- Tarek Ziade - Mountain View (online) (3)
- Guillermo López-Anglada - Frankfurt am Main (online) (3)
- Rafael Villar Burke - Madrid (online) (3)
- Piotr Dobrogost - Milanówek, Poland (online) (3)

You can participate online by joining the #distutils channel on [freenode](http://freenode.net/) and adding your name above.

### 1.3. Sprint Goals 

- ![(./)](/wiki/europython/img/checkmark.png%20"(./)") remove all distutils2 occurrences and replace them with packaging.

- ![(./)](/wiki/europython/img/checkmark.png%20"(./)") fix some spelling and grammar errors

- ![\<!\>](/wiki/europython/img/attention.png "<!>") make docs conform to the python documentation style guide (%50)

- ![\<!\>](/wiki/europython/img/attention.png "<!>") clean up Sphinx syntax and reStructuredText usage (%50)

- ![(./)](/wiki/europython/img/checkmark.png%20"(./)") fix Sphinx errors and warnings

- ![(./)](/wiki/europython/img/checkmark.png%20"(./)") start to re-work the doc that lives outside the packaging folder, that refers to installing/building stuff

- ![(./)](/wiki/europython/img/checkmark.png%20"(./)") reorganize the doc into sections:

  - end-users
  - developers
  - package managers

### 1.4. Requirements 

Clone Tarek\'s cpython fork from Bitbucket and brush up on reStructuredText and Sphinx.

#### 1.4.1. Hg repository 

hg clone [https://bitbucket.org/tarek/cpython](https://bitbucket.org/tarek/cpython) Most work will take place under the cpython/Doc/packaging/ directory.

#### 1.4.2. Markup and doc generation 

Docs are written using reStructuredText markup and auto-generated using Sphinx.

- [Sphinx](http://sphinx.pocoo.org/)

- [reStructuredText](http://docutils.sourceforge.net/rst.html)

### 1.5. Hosting 

Most sprinters will be working remotely, feel free to meetup in small groups and update details here.

### 1.6. Updates 

### 1.7. Sprint Report Day 1 

Today was pretty productive as we managed to get the docs building without errors or warnings using the cpython method of building the docs.

#### 1.7.1. Major Changes 

- removed Doc/packaging/conf.py
  - docs will be built using the standard cpython build process, this local sphinx conf.py is no longer required
- removed updated pkgutil.rst doc from Doc/packaging/
  - relocate under Doc/library/pkgutil.rst?
- disabled use of the Sphinx autodoc plugin (automodule, autoclass, etc)
  - Seems we cannot use the autodoc plugin without some changes to how we build cpython docs. We mainly need sphinx Python 3 support so features like automodule works.
- docs have been split up between 3 directories:
  - enduser
  - developer
  - packager
- changed the labels within Doc/packaging/ to use \_packaging as a prefix.
  - make it clear we are referencing packaging and not distutils

  - label names must be unique in the entire documentation source

           .. _metadata becomes .. _packaging-metadata
- added the index directive at the top of all docs under Doc/packaging/packaging/
  - prevents duplicate objects, distutils and packaging conflict when generating the index.

           .. index:: module: packaging
- used sed to search and replace occurrences of distutils, distutils2, and Distutils2
  - s/Disutils2/Packaging/g
  - s/distutils2/packaging/g
  - s/distutils/packaging/g

### 1.8. Sprint Report Day 2 

Today we had some new contributors to packaging, Guillermo López-Anglada and Piotr Dobrogost. Piotr Dobrogost made his first commit to cpython and Guillermo did a comprehensive review and edit of the enduser docs including the pysetup tutorial.

The rest of the sprinters focused on Sphinx/reST improvements, conforming to the Python documentation style guide, and basic spelling and grammar fixes. At this point, the packaging docs are now officially part of the cpython documentation tree. There is more work required to get the content of these docs up to par, but we are headed in the right direction.

#### 1.8.1. Major Changes 

- most text regarding \'a work in progress\' has been deleted.
- tutorial for pysetup has been added to the enduser docs
- lots of python documentation style guide fixes
- added a packaging.rst file under Doc/library and added an entry to it in
  - Doc/library/python.rst
- improved the enduser, and packager docs for readability (wording, spelling, etc)
