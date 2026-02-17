# Distribute

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Distribute is a project that tries to think about how distutils can evolve 

Interesting discussion are happening in distutils-SIG. You can read the threads

- [Initial thread](http://mail.python.org/pipermail/distutils-sig/2008-September/010031.html)

- [Guido answer, followed by other answers](http://mail.python.org/pipermail/distutils-sig/2008-September/010080.html)

This page tries to synthetizes these threads and see what could be done to improve package managment in Python.

It is not clear right now if a new development will happen outside distutils or not. But this page can be the place where we structure things and decide of the best plan.

Another great ressource to get the whole picture is [Kevin Teague\'s post](http://groups.google.com/group/django-developers/msg/5407cdb400157259) in Django Mailing list.

Chris Withers made a presentation called [Python Package Management Sucks](http://www.simplistix.co.uk/presentations/python_package_management_08/python_package_management_08.pdf) at [PyCon](PyCon) Uk in september 2008.

# Related Docs 

- [Functionality](http://wiki.python.org/moin/Distribute/Functionality)

- [DistributeSprint #1](./DistributeSprint(20).html#A1) : Starting a PEP series

- [Packaging Survey](./Packaging(20)Survey.html) : Survey for the Python Language Summit 2009

- [distutils-autoconf](./distutils(2d)autoconf.html) : Proposal by David

- [Defend Against Fruit Docs](https://github.com/teamfruit/defend_against_fruit/wiki): Continuous Deployment considerations and Python package management

# Related PEPs 

- a new package dedicated to PyPI handling [PEP 373](http://wiki.python.org/moin/A_new_pypi_module)

- mirroring protocol for PyPI : [PEP 374](./PEP(20)374.html)

# What do we have today ? 

## Distutils 

This is a really high-level view of Distutils. It is just made to understand its mechanisms, so if you are not used to it you can get it.

Right now in Python, Distutils provides a set of commands to create a distribution of your package. It uses a set of metadata that describes the package and build an archive with the source code. These metadata are described in [PEP 345](http://www.python.org/dev/peps/pep-0345/).

Distutils uses \"commands\" that can be combined to build various distributions. These commands are invoked through the command line, as long as the package provides the distutils-enable setup.py file, but that is conventionnaly the case:

    $ cd my_python_package
    $ python setup.py COMMAND

So basically, building a source distribution is done by calling \"sdist\":

    $ cd my_python_package
    $ python setup.py sdist

\"sdist\" calls other commands (\"low level\" commands) and builds an archive in the \"dist\" directory.

From there, someone who wants to install a package can get the source distribution, and run the \"install\" command:

    $ wget http://example.com/my_python_package.tgz
    $ tar -xzvf my_python_package.tgz
    $ cd my_python_package
    $ python setup.py install

This command will inject the package into Python\'s site-packages so it is installed.

There are other commands available to make various flavors to distribute your package. Binary distributions, and even OS-specific distributions, like RPM, that maps some metadata to the RPM system ones.

Distutils is also used to upload you package to PyPI or any website that implements the protocol. Some PyPI-enabled websites are starting to be launched. For instance plone.org is about to switch its products center to a PyPI-enabled system.

So developers sends their package like this

    $ python setup.py register sdist upload

This command registers the package to PyPI, builds a source archive, and upload it.

Python 2.6 has been changed so you can do it with any website and several accounts, like this for instance:

    $ python setup.py register sdist upload -r plone.org

## Setuptools 

Setuptools can be seen as an enhancement of Distutils. It does a lot of things, and this section will not present everything. You might want to read [Phillip\'s page on the project](http://peak.telecommunity.com/DevCenter/setuptools).

But basically it adds 4 major features a lot of people use:

- a new metadata called install_requires where you can list the names of the packages the package uses
- a namespaced package feature à la Java, that let you create several package under the same namespace, without having to distribute them in the same package.
- some new commands like:
  - \"develop\", that will let you link a package you are currently working in into you Python environnement
    - without having to install it for real. See it as a special symbolic link inside Python site-packages.
  - \"test\", that will let you link a tets runner to the package tests
- easy_install (described later)

### real-world example 

Zope used setuptools namespace feature to split its huge code base into small packages. For instance zope.interface is distributed as a single package and has its own developement cycle. In a way, Instead of downloading one 100MB package called Zope that contains the whole zope.\* source tree, you download 100 packages of 1MB. And zope.whatever can use the new version of zope.interface, without having to wait for a 6 months-based release of Zope.

So zope.whatever, declares in its setup.py environment zope.interface, with the right version:

    setup(name='zope.whatever',
          ...
          install_requires=['zope.interface>=1.2.4']
          ...
          )

This will tell Setuptools that zope.whatever needs zope.interface 1.2.4 or higher to work.

And if you try to install it, Setuptools will check if it is installed. If not it will try to get it at [PyPI](http://pypi.python.org) and instal it.

## Paver 

Paver subsumes the build tool portion of distutils/setuptools. It allows python programmers to use all of the setuptools/distutils commands but makes it easy to add new commands and modify the existing ones. Extensibility is easy in both the declarative portion of the files (adding new pieces of information about a package) and the imperative portion (adding new commands to perform.)

Converting a simple setup.py that only has declarations to a pavement.py file is trivial.

[http://www.blueskyonmars.com/projects/paver](http://www.blueskyonmars.com/projects/paver)

## Defend Against Fruit 

[Defend Against Fruit](http://teamfruit.github.io/defend_against_fruit/) is focused on providing a pragmatic, continuous deployment style build system for Python. Current Python build systems do not properly account for the needs of effective continuous deployment. This package extends the Python tooling to add the missing pieces.

With an eye to agile development principles and [fast-feedback](https://github.com/teamfruit/defend_against_fruit/wiki#fast-feedback-is-critical), we want a build system which satisfies the following goals:

- Every SCM change-set committed should result in a potentially shippable release candidate.
- When a defect is introduced, we want to immediately detect and isolate the offending SCM change-set. This is true even if the defect was introduced into a library we depend upon.
- Library management should be so easy as to never impede code changes, even in multi-component architecture.

For in-depth documentation with lots of pretty diagrams, [take a look at the wiki](https://github.com/teamfruit/defend_against_fruit/wiki).

## Other tools 

xxx

# What is good ? 

## Distutils 

xxx

## Setuptools 

xxx

## Other tools 

xxx

# What is wrong ? 

## Distutils 

The problems in distutils that where listed by people:

- the code is old, and undertested
- It does too many things !
- The layout and the metadata are not complete enough. For instance, it is not clear for an OS vendor what files should be put where in a FHS PoV
- when you distribute your application with distutils, you have to prepare yourself all the binary and os-specific versions. You can\'t just give a source distribution that can be understood by everyone. Either it is push completely inside the Python installation, either you provide OS-specific installers.
- documentation is weak and the code is hard to reverse engineer
- hard for end user to override dynamically selected defaults; e.g. it finds the \"right\" compiler, flags, libraries, and so on, but it is not always right
- no un-install
- No provisions for installing applications or \"private libraries\". private libraries are libraries meant to be used by an application but not wanting to export a public API.

## Setuptools 

xxx

## Other tools 

xxx

# What can we do today ? 

## Distutils 

- remove the log module and use logging

- remove old-style Python code (work in progress, see latest patch in bugs.python.org)

- finish the test coverage

- propose an independant tool in a PEP, that knows how to register and upload a package at a PyPI compatible server

  this is started here: [A new pypi module](./A(20)new(20)pypi(20)module.html)

## Setuptools 

xxx

## Other tools 

xxx

# What\'s next ? 

BUILDS is the code name of project for a \"Build Utilities, Installation Locations, & Distribution Standards\" (BUILDS) specification. As part of this specification, the [PythonPackagingTerminology](PythonPackagingTerminology) page documents the terms used in the Python packaging ecosystem.

Create a web resource that documents the existing Python packaging ecosystem, tools and practices to make it easier for people to learn about how they can better manage their Python packaging needs.

Design discussions:

- Split the concerns

- [Uninstall Command](./Distutils(2f)Proposals(2f)UninstallCommand.html)

- [OsVendorsRequirements](./OsVendorsRequirements.html)
