# EnhancedPyPI

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Abstract 

This document provides:

- a list of enhancements to make Distutils packaging system support several index servers;
- changes to be made in the central server index implementation, a.k.a PyPI;

# Rationale 

The PyPI is playing a very important role in the standardization of Python package distribution since Python 2.4. Together with Distutils and the third-party library Setuptools, most Python programmers are releasing their packages in eggs, and are making them available in PyPI.

Web frameworks such as Plone and the underlying framework, are now entirely distributed in eggs, and use PyPI as the main place to publish them. Some tools like `zc.buildout` automate the build of Python application by looking for eggs in PyPI and downloading them.

This central approach is great for Python advocacy, and for the cohesion of the community of developers, but brings a few issues. The ones addressed in this document are:

- when PyPI is unreachable, developers are unable to build their application, unless they have a local PyPI cache;
- when people from a sub-community, like Plone, want to promote their work, they need to shout it out in several places, to make sure it has reach people focused on the given framework. These places are acting a bit like the PyPI, so a common releasing standard make things easier to automate.

This document provides a solution to transparently support several index servers. It is a very low risk and very simple to implement. It is also finalizing a feature that was primarily intended by Distutils and PyPI, but not easy to use as-is: making it a central server, but allowing people to register and upload their package elsewhere.

The rest of the document presents the actions to take, and the work to be done for it:

- making `.pypirc` support multiple servers

- making PyPI permissive for Trove classification

# Making .pypirc support multiple servers 

Right now, the `.pypirc` file is intended to keep username and password for registering a package. The file looks like

      [server-login]
      username:tarek
      password:secret

The default repository is PyPI, and when another repository has to be used, there are two options.

Either adding the repository url in the command line:

      $ python setup.py register -r http://example.com/repository

or adding it in the `.pypirc` file:

      [server-login]
      username:tarek2
      password:secret
      repository:http://example.com/repository

In both cases, if your username differs from a server to another, it is not possible to keep a username/password for each server. Furthermore the realm associated with the server is hardcoded to \"pypi\".

## Several sections in .pypirc 

A simple way to enhance it, is to be able to add several sections in `.pypirc`. The root section would be the `[distutils]` section, with a list of sections that represent a server.

For example:

      [distutils]
      index-servers =
        pypi
        my-other-server
        my-other-server-with-its-own-realm

      [pypi]
      repository:http://pypi.python.org/pypi/
      username:tarek2
      password:secret


      [my-other-server]
      username:tarek2
      password:secret
      repository:http://example.com/repository

      [my-other-server-with-its-own-realm]
      username:tarek3
      password:secret3
      repository:http://example2.com/repository
      realm:acme

When a user calls the `register` or the `upload` command, it will use the default server located in the `pypi` section, or the server given by the `-r` option:

    $ python setup.py register sdist upload -r http://example.com/repository       # registering and uploading at example.com
    $ python setup.py register sdist upload        # registering and uploading at PyPI

The `-r` option will also accept the name of the section:

    $ python setup.py register sdist upload -r my-other-server      # registering and uploading at example.com
    $ python setup.py register sdist upload -r pypi       # registering and uploading at PyPI

Default values in this file will be:

- `distutils:index-servers` : `"pypi"`

- `pypi:repository` : `http://pypi.python.org/pypi/`

Backward compatibility will be kept, and a file that uses the old format:

      [server-login]
      username:tarek2
      password:secret

\...will be translated as:

      [distutils]
      index-servers =
        pypi

      [pypi]
      username:tarek2
      password:secret

## Making PyPI permissive for Trove classification 

PyPI is based on a Trove classification, see [http://www.python.org/dev/peps/pep-0301/#distutils-trove-classification](http://www.python.org/dev/peps/pep-0301/#distutils-trove-classification). Another server may have its own trove classification though, that differs from PyPI. This is intended because the server can provide a \"package center\" that has its own domain-specific categories.

For example, a package might have this classification:

      Development Status :: 5 - Production/Stable
      Intended Audience :: Developers

But a slightly different one in another server. Let\'s say, the ACME company:

      ACME :: Visibility :: Public
      Development Status :: 5 - Production/Stable
      Intended Audience :: Developers

A permissive Trove classification would allow the registering of the package in both servers, even if the categories does not exist. For each unkown category a warning is popped at the prompt. The unknown category is not created on the server: each server keeps its own classifiers.

When registering it to several servers, the expected output would be::

            $ python setup.py register   # registering at PyPI
            ...
            Warning "ACME :: Visibility :: Public" classifier not found on the server
            200 - OK


            $ python setup.py register -r http://example.com/repository   # registering at example.com
            Warning "Development Status :: 5 - Production/Stable" classifier not found on the server
            Warning "Intended Audience :: Developers" classifier not found on the server
            200 - OK

This will allow visual checking when a typo is made. The package will then be available in each server, but only under the categories known to the server.
