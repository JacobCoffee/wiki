# Distutils/Metadata

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page describes the work done in order to change the Distutils Metadata.

PEP References :

- [PEP 241](http://www.python.org/dev/peps/pep-0241/) Metadata 1.0 for Python Software Packages

- [PEP 314](http://www.python.org/dev/peps/pep-0376/) Metadata 1.1 for Python Software Packages

- [PEP 345](http://www.python.org/dev/peps/pep-0345/) Draft Metadata 1.2 for Python Software Packages

We are working on a new version for PEP 345. Jim started a branch (jim-update-345)

what has been said:

- deprecate Requires/Provides/Obsolete.
- add install_requires
- deprecate the MANIFEST.in template system in favor of a more powerful package_data
- list all the arguments that are passed to vairous commands through setup.py that should land into the new metadata description
- see if we want to have a new \"python version\" metadata (it\'s a trove classifier right now)

## David Lyon\'s comments 

Package [MetaData](./MetaData.html) needs to include:

- the documentation file ie index.html / readme.txt etc\...

- name/location of the examples directory

- list of program executeables - (eg define the location of ez_install.exe) otherwise it\'s easy for programs to get lost.

- name/location of the configuration file (in the case of a [ConfigParser](ConfigParser) compatable config file)

- name/location of the tests directory

- name/location of data files

The above two are so that the files could be placed in the \"correct\" location.

For example.. in Windows.. config and data files should go to :

- \\Documents and Settings\\user\\Application Data\\program name

in linux\...

- /home/user/.program name

By making this information available in the metadata, it provides for a cross platform friendly system where the setup.py could conceivably copy all the files into the \"right\" locations.

A Package Manager program could conceivably make this information readily available to the user. Alternatively, in the most conservative case, IDLE, [PythonWin](PythonWin), Eclipse would be able to utilise this information and render it to the python user.

## Jim Fulton\'s comments 

Having looked at this and spoken to folks over the last few days I have a numbner of observations:

- It could be argued that Requires/Provides and install_requires are complementary. At worst, they talk about different things. It is probably still best to deprecate requires and provides as they are likely to be confusing.
  - (Note that I think it would be valuable to have some way of saying that a package provides a required feature that can be provided by multiple packages, and that could be required by other packages. This should probably be out of scope of the current effort.)
- I think that install_requires is the only thing that needs to be added. setuptools provides a number of additional features that people might find useful, but they can still use setuptools to provide those features.
- I don\'t think thet deprecating the existing MANIFEST.in template system needs to be in scope of this effort. I think we should take small incremental steps.
- The Python version dependency is already in PEP 345. (Incidentally, I was under the mis-impression that PEP 345 introduced Requires/Provides, but they were introduced in PEP 314.)
- To make progress, I don\'t think it is necessary to release distutils externally. I think it would be enough to get install_requires into Python 2.7 and, if possible 3.1. Since it is compatible with setuptools, people who want it in earlier Python versions can use setuptools as it is now. I\'m not opposed to someone making a separate distutils release, but I don\'t think the benefit is worth the effort.
- I do think it would be very valuable to get install_requires data into PyPI. This raises the question of what to do about dependencies of dependencies on different Python versions.
- I think we need a way to handle meta-data extensions. Two use cases:
  - extra down-stream meta data
  - entry points

## Tres Seaver\'s comments 

After working with Matthias Klose, I honestly cannot see any reason not to just appropriate the \'Requires:\', \'Obsoletes:\', and \'Provides:\' fields already implemented in PEP 314. There are no other \*real\* semantics for those fields besides the ones we want.

Note that we need to keep the \'PKG-INFO\' fieldnames / semantics distinct from the values passed to \'setup()\': in particular, the \'install_requires\' argument could easily map onto the \'Requires:\' field.

My proposal:

- Get the list of existing packages on PyPI which spell \'Requires:\', \'Provides:\', and \'Obsoletes:\', and look at the values which are present. See Martin v. Loewis\'s stats here:
  - [http://mail.python.org/pipermail/python-dev/2009-March/087885.html](http://mail.python.org/pipermail/python-dev/2009-March/087885.html)

- Update the not-yet-released PEP 345, documenting the desired semantics for the \'Requires:\', \'Provides:\', and \'Obsoletes:\' fields. In particular, note that the names in these fields are preferentially distutils projects, rather than package / module names. Document the semantics of the version strings according to the consensus proposal

  from [PyCon](PyCon) (the \'verlib.py\' version).

- Update distutils, adding an API for querying values stored in PKG-INFO fields (avoiding running \'setup.py\').

- Update setuptools such that its \'install_requires\' arguments get passed through to the \'distutils.core.Distribution\' constructor as \'requires\'.

- Update setuptools to do \"soft\" requirements on names found in PKG-INFO\'s \'Requires:\': if no distribution matches the project name, then fall back to assuming that it refers to a package / module.
