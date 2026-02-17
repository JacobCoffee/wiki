# JythonDeveloperGuide

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This is an introduction to developing Jython, just to get someone started. It doesn\'t cover the source code in any depth or discuss the design behind Jython. It\'s purely aimed at getting a development environment set up. It\'s definitely not complete so feel free to make it better!

## Mercurial 

NOTE: The source code of Jython is now mirrored to [Github](http://github.com/jythontools/jython), please see the next section \"GIT\" on how to contribute with pull requests.

- Check out a copy of the Jython source with [Mercurial](http://mercurial.selenic.com/), available on most \*nix systems or with Cygwin on Windows.

- You can use the command line tool `hg`{.backtick}, or [GUI clients are available](http://mercurial.selenic.com/wiki/OtherTools#Graphical_user_interfaces) on most platforms.

- [NetBeans](./NetBeans.html), Eclipse and other Java IDEs also integrate Mercurial support. Eclipse users should see [JythonDeveloperGuide/EclipseNotes](JythonDeveloperGuide/EclipseNotes).

- Browse the source code on the Web at [http://hg.python.org/jython](http://hg.python.org/jython) or at the official mirror on [BitBucket](./BitBucket.html), at [http://bitbucket.org/jython/jython](http://bitbucket.org/jython/jython).

- To obtain the a copy of the *current development* source, clone the repo via:

  - hg clone http://hg.python.org/jython

- It\'s easy to create your own fork of the repo on [BitBucket](./BitBucket.html), visit [http://bitbucket.org/jython/jython](http://bitbucket.org/jython/jython) and click on \'Fork\' \-\-- Please see the \"GIT\" section for our new GIT-based pull request process.

- Attach patches to issues in the [Jython bug tracker](http://bugs.jython.org/).

  - Also, you can upload them to [http://codereview.appspot.com](http://codereview.appspot.com) (the Jython repository is already registered).

## GIT 

- Jython\'s source code is mirrored to [https://github.com/jythontools/jython](https://github.com/jythontools/jython) (a background sync runs every 5 minutes from hg.python.org)

- You can use your [favorite GIT client](http://git-scm.com/downloads/guis) to clone the GIT repo, on the command line:

  - git clone https://github.com/jythontools/jython.git

- To submit patches, you should fork the github repo, create a special feature branch and submit a pull request on github.

- The Jython developers will review and merge your pull request into the [upstream Mercurial repo](http://hg.python.org/jython).

## IDE Support 

Because Jython is an Ant project, it\'s a bit tricky to configure an Integrated Development Environment (IDE) for it.

These notes should help:

- [JythonDeveloperGuide/EclipseNotes](JythonDeveloperGuide/EclipseNotes)

- [JythonDeveloperGuide/IntellijNotes](JythonDeveloperGuide/IntellijNotes)

- [JythonDeveloperGuide/IntellijTricks](JythonDeveloperGuide/IntellijTricks)

## Ant 

- [Ant](http://ant.apache.org/) is a Java-based tool used to build Jython from source.

- Eclipse users, see [Eclipse Ant notes](./JythonDeveloperGuide(2f)EclipseNotes.html#ANT)

- Download the latest version (Jython requires Ant 1.7 or later to build) and install it so Ant\'s `bin`{.backtick} directory is somewhere in your path.

- To build Jython, run `ant`{.backtick} in the top-level Jython directory (which contains the Ant file `build.xml`{.backtick}).

- The results of the build appear in the `dist`{.backtick} subdirectory.

## Tests 

The Jython build process generates an executable Bash script, `dist/bin/jython`{.backtick}, to make it easy to launch your build of Jython. It works on Unix-like platforms (including Mac OS X and Cygwin).

If you\'re using Windows without Cygwin, use the batch file `dist/bin/jython.bat`{.backtick} instead.

Now you\'re ready to run tests\...

- There are a couple different places to find test cases
  - Jython\'s `dist/Lib/test`{.backtick} (populated by the build process)

  - Jython\'s `bugtests`{.backtick} subdirectory (included with the development sources)

- Run a particular test, or the whole Python test suite with `ant regrtest`{.backtick}.

See [TestingJython](TestingJython) for some more details.

## Directory layout 

Note the following describes the current trunk/jython. If you are working from an older tag, src doesn\'t exist and src/com and src/org are moved up a level.

- `src/org`{.backtick} : top level package for python

- `src/com`{.backtick} : zxJDBC related sources

- `src/shell`{.backtick} : launcher scripts

- `src/templates`{.backtick}: java source generator & related templates, used to update portions of java classes elsewhere in the source tree

- `Demo`{.backtick} : demo sources for the website and such

- `Doc`{.backtick} : the website documentation (see [JythonDeveloperGuide/WebsiteBuilderSetup](./JythonDeveloperGuide(2f)WebsiteBuilderSetup.html) to build the [http://jython.org](http://jython.org) website)

- `Lib`{.backtick} : the python source files for Jython standard library implementations

- `Lib/test`{.backtick} : test cases

- `Misc`{.backtick} : random scripts which are not all used; some generate source

- `Tools`{.backtick} : JythonC and Freeze

- `lib-python/<version>`{.backtick} : Lib directory from the corresponding version of cpython

- `bugtests`{.backtick} : additional test cases covering bug reports

## Coding guidance 

- [JythonDeveloperGuide/PortingPythonModulesToJython](JythonDeveloperGuide/PortingPythonModulesToJython) : A good starting task for a Jython developer

- [CodingStandards](CodingStandards) : The standards for writing Java code for Jython

- [PatchGuidelines](PatchGuidelines) : How to make a patch for submission to the tracker

## How things work 

- [ImplementNewType](ImplementNewType) : Implementing a new type (a beginner\'s notes)

- [ImplementSequenceType](ImplementSequenceType) : Implementing a new sequence type

- [JythonModulesInJava](JythonModulesInJava) : How to write a Jython module in Java

- [PythonTypesInJava](PythonTypesInJava) : How to make a Jython type in Java (2.5 and later), mostly about the type exposer

- [JythonClassesInJava](JythonClassesInJava) : How to make a Jython class in Java (pre-2.2, deprecated)

- [JythonDeveloperGuide/AttributeLookupMethods](JythonDeveloperGuide/AttributeLookupMethods) : Some explanation for the different methods to lookup attributes on [PyObject](./PyObject.html).

- [JythonDeveloperGuide/ImplementingStrAndRepr](JythonDeveloperGuide/ImplementingStrAndRepr) : Tips for implementation of `__str__`{.backtick} and `__unicode__`{.backtick} in Java.

- [IntegerConversion](IntegerConversion) : Basics of converting [PyObject](./PyObject.html) numbers to Java primitives

- [JythonDeveloperGuide/UsingPyNewStringFromPythonCode](JythonDeveloperGuide/UsingPyNewStringFromPythonCode) : On the corner case of converting a Java String to a Python String.

- [GeneratedDerivedClasses](GeneratedDerivedClasses) : `gderived.py`, a tool used when implementing new types

- [BufferProtocol](BufferProtocol) : Design of a Jython equivalent to the CPython buffer protocol (buffer API)

- [MethodDispatch](MethodDispatch) : An explanation of Jython method dispatch mechanism.

## Other stuff 

- [WebsiteBuilderSetup](WebsiteBuilderSetup) : How to get the pieces setup to edit and build the Jython website

- [VersionTransition](VersionTransition) : Why some tests are excluded in going to a new version and how to go about fixing them

- [JythonDeveloperGuide/RegressionTestNotes](JythonDeveloperGuide/RegressionTestNotes) : Some notes the regression tests

- [JythonDeveloperGuide/PleaseAdoptMe](JythonDeveloperGuide/PleaseAdoptMe) : Tasks looking for volunteers

- [HowToReleaseJython](HowToReleaseJython) : Checklist for building a release and updating the website

- [SvnToHgMigration](SvnToHgMigration) : Notes on the migration to Mercurial

## Tasks 

- [PerformanceEnhancements](PerformanceEnhancements) : Ideas on how to speedup Jython

- [CodebaseCleanup](./CodebaseCleanup.html) : Tasks/general guidelines on keeping the codebase clean

### Porting external projects to Jython 

- [DjangoOnJython](DjangoOnJython)

- [MercurialOnJython](MercurialOnJython)

- [SqlAlchemyOnJython](SqlAlchemyOnJython)

- [SetuptoolsOnJython](SetuptoolsOnJython)

- [PylonsOnJython](PylonsOnJython)

- [TwistedOnJython](TwistedOnJython)
