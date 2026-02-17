# buildout/pycon2008 tutorial

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Eggs and Buildout Deployment in Python

::: figure
![](http://www.dfwpython.org/static/pycon/distutils-flow.png)

Figure 1: Data Flow within Distutils/Setuptools Usage
:::

Slides:

> Four-Part In-Depth Presentation Sequence (not presented in class)
>
> - [An Introduction to the Virtualenv Sandbox](http://dfwpython.org/static/pycon/0-python-virtualenv.pdf) ([.pdf](http://dfwpython.org/static/pycon/0-python-virtualenv.pdf), [.txt](http://dfwpython.org/static/pycon/0-python-virtualenv.txt))
> - [Distutils: Packaging, Metadata and Pushups](http://dfwpython.org/static/pycon/1-python-distutils.pdf) ([.pdf](http://dfwpython.org/static/pycon/1-python-distutils.pdf), [.txt](http://dfwpython.org/static/pycon/1-python-distutils.txt))
> - [SetupTools: Python Eggs, Dependencies and Plugins](http://dfwpython.org/static/pycon/2-python-setuptools.pdf) ([.pdf](http://dfwpython.org/static/pycon/2-python-setuptools.pdf), [.txt](http://dfwpython.org/static/pycon/2-python-setuptools.txt))
> - [Buildout: Precision Assembly, Repeatability, Islands](http://dfwpython.org/static/pycon/3-python-buildout.pdf) ([.pdf](http://dfwpython.org/static/pycon/3-python-buildout.pdf), [.txt](http://dfwpython.org/static/pycon/3-python-buildout.txt))
>
> Condensed Slide Set Used in Actual Tutorial
>
> - [Eggs and Buildout Deployment in Python](http://dfwpython.org/static/pycon/eggs-n-buildout.pdf) ([.pdf](http://dfwpython.org/static/pycon/eggs-n-buildout.pdf), [.txt](http://dfwpython.org/static/pycon/eggs-n-buildout.txt))
> - [Additional Topics of Tutorial](http://dfwpython.org/static/pycon/eggs-n-buildout-bonus.pdf) ([.pdf](http://dfwpython.org/static/pycon/eggs-n-buildout-bonus.pdf), [.txt](http://dfwpython.org/static/pycon/eggs-n-buildout-bonus.txt))

Exercises from Tutorial:

> 1.  Installing Tools for the Class
>
>     ::: line
>     \$ cd /tmp
>     :::
>
>     ::: line
>     \$ wget [http://peak.telecommunity.com/dist/ez_setup.py](http://peak.telecommunity.com/dist/ez_setup.py)
>     :::
>
>     ::: line
>     \$ sudo python ez_setup.py
>     :::
>
>     ::: line
>     \$ sudo easy_install virtualenv
>     :::
>
>     ::: line
>     \$ sudo easy_install zc.buildout
>     :::
>
> 2.  Instantiating a Sandbox or Two
>
>     ::: line
>     \$ virtualenv pycon -or-
>     :::
>
>     ::: line
>     \$ virtualenv \--no-site-packages pycon
>     :::
>
>     ::: line
>     \$ cd pycon
>     :::
>
>     ::: line
>     \$ bin/python
>     :::
>
>     ::: line
>     \$ source bin/activate -or- activate.bat
>     :::
>
>     ::: line
>     \$ deactivate
>     :::
>
>     - 
>
>       explore:
>
>       :   - directory tree
>           - *sys.path*
>
>     - for each kind of sandbox
>
> 3.  Processing Distributions
>
>     1.  Grab a source distribution
>
>         ::: line
>         \$ /sandbox/bin/easy_install \--editable \--build-directory . SQLObject==0.9.5
>         :::
>
>         ::: line
>         \$ /sandbox/bin/easy_install \--editable \--build-directory . SQLObject==dev
>         :::
>
>         Examine its directory structure and common files.
>
>     2.  Query the list of available distribution formats.
>
>         ::: line
>         \$ cd sqlobject
>         :::
>
>         ::: line
>         \$ /sandbox/bin/python setup.py sdist \--help-formats
>         :::
>
>         ::: line
>         \$ /sandbox/bin/python setup.py bdist \--help-formats
>         :::
>
>     3.  Build and package it as a binary distribution.
>
>         ::: line
>         \$ /sandbox/bin/python setup.py build
>         :::
>
>         ::: line
>         \$ /sandbox/bin/python setup.py install
>         :::
>
>         ::: line
>         \$ /sandbox/bin/python setup.py bdist \--formats=tar,egg,rpm
>         :::
>
>         Examine the run output and the table-of-contents of the distribution archive afterward. Note the way that metadata is stored.
>
>     4.  Repackage it as a source distribution
>
>         ::: line
>         \$ /sandbox/bin/python setup.py sdist \--formats=zip
>         :::
>
>         Examine the run output and the table-of-contents of the source archive. Note the different way that metadata is stored.
>
>     5.  Try to import it, then run the \"develop\" cmd and try again.
>
>         ::: line
>         \$ cd /sandbox
>         :::
>
>         ::: line
>         \$ /sandbox/bin/python
>         :::
>
>         ::: line
>         \$ import sqlobject
>         :::
>
>         ::: line
>         \$ cd /sandbox/sqlobject
>         :::
>
>         ::: line
>         \$ /sandbox/bin/python setup.py develop
>         :::
>
> 4.  Generating Scripts that Invokes Entrypoints
>
>     1.  Create a sandbox in which to work.
>
>         ::: line
>         \$ virtualenv \--no-site-packages pycon
>         :::
>
>         ::: line
>         \$ cd pycon
>         :::
>
>     2.  Create a distribution for a new egg that has two scripts.
>
>         ::: line
>         \# File: pycon/setup.py
>         :::
>
>         ::: line
>         from setuptools import setup
>         :::
>
>         ::: line
>         \
>         :::
>
>         ::: line
>         setup(name=\"myscript\",
>         :::
>
>         ::: line
>         version=\"1.0.0\",
>         :::
>
>         ::: line
>         py_module = \[\'myscript\'\],
>         :::
>
>         ::: line
>         entry_points={
>         :::
>
>         ::: line
>         \"console_scripts\": \[
>         :::
>
>         ::: line
>         \"alpha = myscript:alpha_cmd\",
>         :::
>
>         ::: line
>         \"beta = myscript:beta_cmd\"\]
>         :::
>
>         ::: line
>         },
>         :::
>
>         ::: line
>         )
>         :::
>
>         ::: line
>         \# File: pycon/myscript.py
>         :::
>
>         ::: line
>         def alpha_cmd():
>         :::
>
>         ::: line
>         print \"Hello from Alpha Centauri\"
>         :::
>
>         ::: line
>         \
>         :::
>
>         ::: line
>         class beta_cmd(object):
>         :::
>
>         ::: line
>         def \_\_init\_\_(self):
>         :::
>
>         ::: line
>         print \"Hello from Beta Centauri\"
>         :::
>
>     3.  Mark it a develop-egg and then add the egg as a \'myscript\' part.
>
>         ::: line
>         \# File: pycon/buildout.cfg
>         :::
>
>         ::: line
>         \[buildout\]
>         :::
>
>         ::: line
>         develop = .
>         :::
>
>         ::: line
>         parts = myscript
>         :::
>
>         ::: line
>         \
>         :::
>
>         ::: line
>         \[myscript\]
>         :::
>
>         ::: line
>         recipe = zc.recipe.egg
>         :::
>
>         ::: line
>         eggs = myscript
>         :::
>
>     4.  Run *buildout* and look in the bin/ directory for scripts.
>
> 5.  Create a simple buildout around an egg and experiment with it.
>
>     1.  Create an empty buildout area.
>
>         ::: line
>         \$ virtualenv \--no-site-packages pycon
>         :::
>
>         ::: line
>         \$ cd pycon
>         :::
>
>         ::: line
>         \$ buildout init
>         :::
>
>     2.  Put into it a simple egg by creating a \"buildout.cfg\" file:
>
>         ::: line
>         \[buildout\]
>         :::
>
>         ::: line
>         parts = mypython
>         :::
>
>         ::: line
>         prefer-final = true
>         :::
>
>         ::: line
>         \
>         :::
>
>         ::: line
>         \[mypython\]
>         :::
>
>         ::: line
>         recipe = zc.recipe.egg
>         :::
>
>         ::: line
>         interpreter = dbpython
>         :::
>
>         ::: line
>         eggs = SQLObject
>         :::
>
>     3.  Invoke \"bin/buildout\" and examine the output messages, the directory structure and the *dbpython* script.
>
>         Test for what version got installed and where it came from.
>
>         ::: line
>         \$ bin/dbpython
>         :::
>
>         ::: line
>         \>\>\> import sqlobject
>         :::
>
>         ::: line
>         \>\>\> sqlobject.\_\_file\_\_
>         :::
>
>         ::: line
>         \'/var/tmp/buildout/eggs/SQLObject-0.10.0-py2.5.egg/sqlobject/\_\_init\_\_.py\'
>         :::
>
>     4.  Force it to use a specific version of SQLObject.
>
>         ::: line
>         eggs = SQLObject==0.9
>         :::
>
>         Test for what version got installed and where it came from.
>
>         ::: line
>         \$ bin/dbpython
>         :::
>
>         ::: line
>         \>\>\> import sqlobject
>         :::
>
>         ::: line
>         \>\>\> sqlobject.\_\_file\_\_
>         :::
>
>         ::: line
>         \'/var/tmp/buildout/eggs/SQLObject-0.9.0-py2.5.egg/sqlobject/\_\_init\_\_.py\'
>         :::
>
>     5.  Remove that constraint and grab its source distribution.
>
>         ::: line
>         \$ bin/easy_install \--editable -b . SQLObject
>         :::
>
>         Alter \"buildout.cfg\" file to make it a development egg:
>
>         ::: line
>         develop = sqlobject
>         :::
>
>         Test for what version got installed and where it came from.
>
>         ::: line
>         \$ bin/dbpython
>         :::
>
>         ::: line
>         \>\>\> import sqlobject
>         :::
>
>         ::: line
>         \>\>\> sqlobject.\_\_file\_\_
>         :::
>
>         ::: line
>         \'/tmp/kkk/sqlobject/sqlobject/\_\_init\_\_.py\'
>         :::
