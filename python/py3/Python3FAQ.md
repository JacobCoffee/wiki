# Python3FAQ

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# What\'s Python 3? 

Python 3 is a new version of the language that is incompatible with the 2.x line of releases. The language is mostly the same, but many details, especially how built-in objects like dictionaries and strings work, have changed considerably, and a lot of deprecated features have finally been removed. The standard library has also been reorganized in a few prominent places.

The aim of Python 3 is to clean up the language by removing little-used features and changing the language\'s semantics. Many such changes cannot be made without breaking compatibility with Python code written for older versions.

# What\'s Python 3000? 

Around 2000, the Python developers began to refer to \"Python 3000\" (or Py3K) as a mythical future version of Python that wouldn\'t have to be compatible with existing code. As the developers began to actually work on designing and implementing this redesigned version, it slowly was renamed into the more concrete \"version 3.0\", and from there to other 3.x versions.

# What changed in Python 3.0? 

Read [What\'s New in Python 3.0](http://docs.python.org/3.0/whatsnew/3.0.html), which lists the changes between Python 2.6+ and Python 3.0.

# What will happen to the Python 2.x versions? 

Being the last of the 2.x series, 2.7 will receive bugfix support until 2020. Support officially stops 1 January 2020, but the final release will occur in April of 2020. No further releases, nor bug fixes, are planned after this date.

If you rely on Python 2.x and don't plan to have completed the switch to Python 3 by the sunset deadline, you have until the end of 2019 to file any issues you would like to see fixed in the final release, 2.7.18, in April of 2020.

The penultimate Python 2.x release, 2.7.17, is [slated to be released](https://www.python.org/dev/peps/pep-0373/#id4) in October of 2019. [Release Candidate 1](https://www.python.org/downloads/release/python-2717rc1/) was made available on 9 October 2019. There will be some flexibility to fix any bugs or issues specifically introduced by the 2.7.17 release in January and February of 2020.

As users attempt to port packages to 3.x, they will surely report bugs in the compatibility and conversion tools, and Python 2.7 will incorporate the results of this feedback. As a result, new warnings will be added to the 3.0-compatibility mode, and new fixers will be added to the 2to3 conversion tool.

# How should I port existing Python 2.x code to Python 3.x? 

Python 2.6+ and 3.x include a tool called 2to3 that parses Python 2.x code and rewrites it to work in Python 3.x. 2to3 includes a large set of *fixers*, each one updating a particular language feature.

We suggest the following steps for porting a package to 3.x:

\* Have a test suite that exercises significant portions of your library or application\'s functionality, the more the better.

\* Run the test suite using Python 2.6+ and specifying the `-3`{.backtick} switch, which enables warnings about code that\'s incompatible with Python 3. Modify the code to avoid triggering the warnings.

\* Run the `2to3`{.backtick} script over the code. If `2to3`{.backtick} can\'t perform the conversion due to code constructs that can\'t be automatically translated, modify your 2.x code to use 3.x-compatible features.

\* Once `2to3`{.backtick} can convert your code without complaint, try running the test suite using the 3.x-transformed version. Examine any test failures and modify the 2.x code responsible to be 3.x-compatible until the test suite succeeds using the transformed version.

Consult [the 2to3 documentation](http://docs.python.org/3/library/2to3.html) for more information about the conversion tool, and [PortingPythonToPy3k](PortingPythonToPy3k) for more general suggestions.

One approach to distributing your 3.x package is to use 3.x\'s build_py_2to3 implementation of the build_py command. See `Demo/distutils/test2to3`{.backtick} for an example.

You will have a single lib.py, written in 2.x. When you install in 3.x, lib2to3 will convert it to 3.x in the build area, and then install the 3.x version.

That, of course, requires you to adjust lib.py in such a way that 2to3 will successfully and completely convert it. In two experiments, Martin von Loewis ported Django and Mark Hammond ported [PythonWin](PythonWin) to 3.0, and found that these adjustments were quite feasible. You look at what 2to3 does, find out what additional modifications need to be done, and apply them to the input of 2to3 so that

- 2to3 leaves these changes in place
- they either have no effect or still work correctly when run in 2.x.

[In this weblog posting](http://www.artima.com/weblogs/viewpost.jsp?thread=227041), Guido van Rossum strongly suggests not changing your APIs when porting to 3.0, because API changes will make it difficult for users to tell whether test suite failures are due to the 2.6+-\>3.0 transition or to the API changes.

[Early2to3Migrations](Early2to3Migrations) has links to some early attempts at porting packages to 3.x.

# How should I port existing C extensions to Python 3.x? 

Benjamin Peterson\'s [Porting Extension Modules to 3.0](http://docs.python.org/howto/cporting.html) describes some of the changes to Python\'s C API, and gives some tips for writing code that will compile with both 2.x and 3.0. The [draft in this wiki](PortingExtensionModulesToPy3k) may be more complete.

# How do I find out what packages have been ported to 3.x? 

Packages listed in the [Python Package Index](http://pypi.python.org) can indicate whether they support Python 3.x. You can view [a list of 3.x-compatible packages](http://pypi.python.org/pypi?:action=browse&c=533) by searching for the `"Programming Language :: Python :: 3"`{.backtick} classifier in the package index.

# My new release supports Python 3.x. How do I indicate that? 

If you\'re using your `setup.py`{.backtick} file to upload a package to the [Python Package Index](http://pypi.python.org), include `"Programming Language :: Python :: 3"`{.backtick} as one of the classifiers.

# I want to start learning/teaching Python. What version should I use? 

Support for Python 2.x will officially end on 1 January 2020. After that date, there will be no further updates nor bugfixes. Since this end-of-life date has been planned for nearly a decade (the first end-of-life date was slated to happen in 2014, and was pushed back to 2020), and nearly all popular libraries have already ported their code, Python 2.x is well on its way to obsolescence. As such, we can only recommend learning and teaching Python 3 - which is simpler and will remain relevant well into the future.

See the [BeginnersGuide](BeginnersGuide) for more information on getting started with Python.
