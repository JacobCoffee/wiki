# PythonPackagingTerminology

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: 
### Terminology Status

Currently, this is a **very** rough list of terms and definitions used in the Python packaging ecosystem and currently exists as a very loose first draft. More terms may be added (and a few terms might be spurious and can be removed). The definitions of terms has largely been culled from the Distutils and Setuptools/PEAK web sites. These terms are intended as a starting point for discussion on the distutils-sig mailing list for a more formalized set of terminology that may eventually be specified in a Python PEP.
:::

::: 
### Module

The basic unit of code reusability in Python. A block of code imported by some other code.
:::

::: 
### Pure Python module

A module written in Python and contained in a single .py file (and possibly associated .pyc and/or .pyo files). Sometimes referred to as a "pure module."
:::

::: 
### Extension Module

A module written in the low-level language of the Python implementation: C/C++ for Python, Java for Jython. Typically contained in a single dynamically loadable pre-compiled file, e.g. a shared object (.so) file for Python extensions on Unix, a DLL (given the .pyd extension) for Python extensions on Windows, or a Java class file for Jython extensions.
:::

::: 
### Package

A module that contains other modules. Typically contained in a directory in the filesystem and distinguished from other directories by the presence of a \_\_init\_\_.py file.

> - To-Do: Update this definition to reflect namespace packages?
:::

::: 
### Root Package

The root of the hierarchy of packages. (This isn't really a package, since it doesn't have an \_\_init\_\_.py file. But we have to call it something.) The vast majority of the standard library is in the root package, as are many small, standalone third-party modules that don't belong to a larger module collection. Unlike regular packages, modules in the root package can be found in many directories: in fact, every directory listed in sys.path contributes modules to the root package.

> - To-Do: definition taken from distutils. This terminology should perhaps be changed to \"Namespace Root\" (or something better)?
:::

::: 
### Module Distribution

A collection of Python modules distributed together as a single downloadable resource and meant to be installed en masse. Examples of some well-known module distributions are Numeric Python, PyXML, PIL (the Python Imaging Library), or mxBase. (This would be called a package, except that term is already taken in the Python context: a single module distribution may contain zero, one, or many Python packages.)
:::

::: 
### Pure Module Distribution

A module distribution that contains only pure Python modules and packages. Sometimes referred to as a "pure distribution."
:::

::: 
### Non-pure Module Distribution

A module distribution that contains at least one extension module. Sometimes referred to as a "non-pure distribution."
:::

::: 
### Distribution Root

The top-level directory of your source tree (or source distribution). The directory where setup.py exists. Generally setup.py will be run from this directory.
:::

::: 
### Distutils

Package included in the Python Standard Library for installing, building and distributing Python code.
:::

::: 
### Metadata for Python Software Packages

Metadata is data about the contents of a Python package.

The format and fields specified in version 1.0 is detailed in PEP 241 ([http://www.python.org/dev/peps/pep-0241/](http://www.python.org/dev/peps/pep-0241/)), and support for working with these fields was included in the distutils package which was added in Python 2.1.

Version 1.1 additiones were detailed in PEP 314 ([http://www.python.org/dev/peps/pep-0314/](http://www.python.org/dev/peps/pep-0314/)). This updated the fields to include \'Download-URL\', \'Requires\', \'Provides\' and \'Obsoletes\' fields. Support was added to the distutils package for this in Python 2.5. The simple dependency information fields for a distribution is generally not used, as the specific module requirements can be dynamic depending on the platform and installation context.

Version 1.2 was proposed in PEP 345 ([http://www.python.org/dev/peps/pep-0345/](http://www.python.org/dev/peps/pep-0345/)), but is still in the draft status and has not been approved not support for these fields implemented.
:::

::: 
### Setuptools

Setuptools is a collection of enhancements to the Python distutils (for Python 2.3.5 and up on most platforms; 64-bit platforms require a minimum of Python 2.4) that allow you to more easily build and distribute Python packages, especially ones that have dependencies on other packages.
:::

::: 
### easy_install

Easy Install is a python module (easy_install) bundled with setuptools that lets you automatically download, build, install, and manage Python packages.
:::

::: 
### pkg_resources

The pkg_resources module distributed with setuptools provides an API for Python libraries to access their resource files, and for extensible applications and frameworks to automatically discover plugins. It also provides runtime support for using C extensions that are inside zipfile-format eggs, support for merging packages that have separately-distributed modules or subpackages, and APIs for managing Python\'s current \"working set\" of active packages.
:::

::: 
### Eggs

The Egg PEAK page definition:

Eggs are a way of bundling additional information with a Python project, that allows the project\'s dependencies to be checked and satisfied at runtime, as well as allowing projects to provide plugins for other projects. There are several binary formats that embody eggs, but the most common is \'.egg\' zipfile format, because it\'s a convenient one for distributing projects. All of the formats support including package-specific data, project-wide metadata, C extensions, and Python code.

The PkgResources PEAK page definition:

Eggs are pluggable distributions in one of the three formats currently supported by pkg_resources. There are built eggs, development eggs, and egg links. Built eggs are directories or zipfiles whose name ends with .egg and follows the egg naming conventions, and contain an EGG-INFO subdirectory (zipped or otherwise). Development eggs are normal directories of Python code with one or more ProjectName.egg-info subdirectories. And egg links are \*.egg-link files that contain the name of a built or development egg, to support symbolic linking on platforms that do not have native symbolic links.

> - To-Do: There is a lot of confusion as to what an \"egg\" is. Some believe it refers to the additional metadata, others believe it is the binary format (the .egg file). e.g. is a source distribution that uses setuptools an egg?
:::

::: 
### Built Egg

A zipped file or directory whose name ends with .egg and follows the egg naming conventions, and contains an EGG-INFO subdirectory. Built eggs can contain binary data specific to a target platform.

> - To-Do: some call these \"binary eggs\", clarify between a binary egg and a built egg?
:::

::: 
### Development Egg

Normal directories of Python code with one or more ProjectName.egg-info subdirectories.

> - To-Do: is there a difference between a \"source egg\" and a \"development egg\"?
:::

::: 
### Egg Link

\*.egg-link files that contain the name of a built or development egg, to support symbolic linking on platforms that do not have native symbolic links.
:::

::: 
### Project

A library, framework, script, plugin, application, or collection of data or other resources, or some combination thereof. Projects are assumed to have \"relatively unique\" names, e.g. names registered with PyPI.
:::

::: 
### Release

A snapshot of a project at a particular point in time, denoted by a version identifier.
:::

::: 
### Distribution

A file or files that represent a particular release.
:::

::: 
### Importable Distribution

A file or directory that, if placed on sys.path, allows Python to import any modules contained within it.
:::

::: 
### Pluggable Distribution

An importable distribution whose filename unambiguously identifies its release (i.e. project and version), and whose contents unamabiguously specify what releases of other projects will satisfy its runtime requirements.
:::

::: 
### Extra

An \"extra\" is an optional feature of a release, that may impose additional runtime requirements. For example, if docutils PDF support required a PDF support library to be present, docutils could define its PDF support as an \"extra\", and list what other project releases need to be available in order to provide it.
:::

::: 
### Environment

A collection of distributions potentially available for importing, but not necessarily active. More than one distribution (i.e. release version) for a given project may be present in an environment.

> - To-Do: A shared egg cache can be specified in Buildout by using the \'eggs-directory\' option. This is often informally referred to as an \"egg cache\".
> - To-Do: Recommendations for where a \"global egg cache\" could possibly live within different operating systems?
:::

::: 
### Working Set

A collection of distributions available for importing. That is distributions that are on the on the sys.path. At most one distribution (release version) of a given project may be present in a working set, as otherwise there would be ambiguity as to what to import.

Working sets include all distributions available for importing, not just the sub-set of distributions which have actually been imported.
:::

::: 
### System Package

A package provided by in a format native to the operating system. e.g. rpm or dpkg file.
:::

::: 
### Installed Distribution

A distribution which is available for import without explicitly modifying the sys.path. An installed distribution is

> - To-Do: clarify this \... ?
:::

::: 
### Namespace Package

A namespace package is a package that only contains other packages and modules, with no direct contents of its own. Such packages can be split across multiple, separately-packaged distributions.
:::

::: 
### Buildout

Tool that provides support for creating applications, especially Python applications. It provides tools for assembling applications from multiple parts, Python or otherwise. An application may actually contain multiple programs, processes, and configuration settings.

Buildout is commonly used to install and manage working sets of Python distributions in the egg format.

> - To-Do: clarify the project name, since some refer to Buildout as \"zc.buildout\", the name of the Python package.
:::

::: 
### VirtualEnv

Tool to create isolated Python environments.

> - To-Do: The term environment differs between setuptools and virtualenv.
:::
