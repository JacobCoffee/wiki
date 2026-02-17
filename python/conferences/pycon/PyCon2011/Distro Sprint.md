# PyCon2011/Distro Sprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Attendees 

- Debian/Ubuntu (Matthias Klose, Barry Warsaw)
- Fedora (Toshio Kuratomi)
- David Cournapeau (bento maintainer, contributor to scipy and numpy)
- Tarek Ziadé (distutils2)
- Thomas Wouters
- Martin v. Löwis
- Allison Randal (Ubuntu)

# Agenda 

### Day 1 

- [Status of porting third party modules to python3](./PyCon2011(2f)Distro(20)Sprint.html#Status_of_python3_third-party_modules_1)

- [Setuptools](./PyCon2011(2f)Distro(20)Sprint.html#setuptools)

- [duplicate named modules](./PyCon2011(2f)Distro(20)Sprint.html#Duplicate_named_modules)

- [multiple versions](./PyCon2011(2f)Distro(20)Sprint.html#Multiple_versions_1)

- [Numpy](./PyCon2011(2f)Distro(20)Sprint.html#Numpy)

- [Namespace package](./PyCon2011(2f)Distro(20)Sprint.html#Namespace_packages)

- [Licensing issue](./PyCon2011(2f)Distro(20)Sprint.html#Licensing_issue)

### Day 2 

- [Bento & distutils2 discussion](./PyCon2011(2f)Distro(20)Sprint.html#Bento_.26_distutils2_discussion)

- [Byte/unicode issues on python3](./PyCon2011(2f)Distro(20)Sprint.html#Byte.2Funicode_issueson_python3)

### Pending 

- Status of python3 itself
- Status of python3 third-party modules (cont)
- Help consolidating information
- Distros get community help to port modules to python3
- unicode/byte problems in python3 on POSIX systems
  - surrogateescape
  - import non_ascii
- openssl and GPL mixing
- Talk to virtualenv guys
  - multiple versions (cont)
  - Larry Hastings (trying to merge to Core)
  - Carl JM

# Day 1 

## Status of python3 third-party modules 1 

Brief discussion on this topic. Deferred further discussion for two reasons:

1.  bento maintainer and distutils2 maintainers present for tonight. Talk to them about issues which concern them.
2.  Allison Randal not present tonight

### Have to engage upstreams 

How do we market to upstream that we (distro maintainers) want to help create patches for python3?

#### gtk/gnome 

- port to pygi as the method of going to python3

- api changes are [largely simple](https://code.launchpad.net/~pitti/computer-janitor/pygi/+merge/46779). Changes of case in the method names, etc. Few widgets are not so simple.

- Not sure about things like libpanel (where there isn\'t a panel with applets in gnome3 and therefore no pygi for it)

## setuptools

- Talked with distutils2/distribute and bento devs
- bento devs: want to know egg Format for metadata and for zip file.
  - tarek \-- zip file format is no more.
  - metadata format is defined in PEPs 376
    - This obsoletes all the past formats.
    - distribute will get PEP 376 format to read package information
    - distribute will not get PEP 376 to write the new format
      - This means that setuptools.pkg_resources will be able to
        - read the metadata and version information in the new format but won\'t be able to install packages that other tools can use.
- Distutils2 will be placed into the python-3.3 packaging/ module directory
  - So it will be distutils2 as a backport package and packaging inside the stdlib.
- Bento packaging for distributions \-- still moving rapidly so it\'s okay if distros
  - package it but not seen as necessary yet.
- 2to3 is slow. Large code bases like numpy/scipy take a long time to run.
  - bento uses dependencies and timestamps so we only rebuild changed files.
    - If this was added to the core build env it would help people porting to
      - python3 because the iterative programming cycle, fixing bugs in a python2 codebase that\'s translated to python3 would go from having to run 2to3 over the whole codebase to only over the changed files. Makes it less painful to fix bugs.
  - lib2to3cache written by someone in numpy to cache results to make it faster

### Actions 

- Assign someone to look into making the invocation of 2to3 from distutils/distutils2 faster \-- dependency tracking, caching, do not rebuild unless necessary. These speedups would help make porting a package to work with both python2 and python3 less painful.

## Multiple versions 1 

### Goals 

- Should **not** support single application that needs multiple versions

- Should support app Foo that needs module Bar version 1 and app Baz
  - that needs app Baz version 2

- we need to be able to install multiple versions of the python package
  - on the filesystem without conflicts

- we need to be able to specify which version to use with import

- we still want import foo to continue working

Any solution has two parts \-- what do we do in python and what do we do in the distros.

### A current solution 

- Use setuptools \--single-version-externally-managed for installing the version that will work with import foo

- Use setuptools multiple version install for the other one. This installs the python module into the egg-info directory itself.

- An application that needs the previous version of the python module needs to define \_\_requires\_\_ = \[\'foo \< X \> Y\'\] so that it finds the old version of the module before the first import of pkg_resources.

#### Caveats 

- This is problematic when the code is being imported by a script in /usr/bin that is already importing pkg_resources. For instance, /usr/bin/nosetests.
  - The workaround is to copy the script to an area the user has control over and modify it to require foo as well.

- When the script is being launched by something else, you have to get the \_\_requires\_\_ into the \_\_main\_\_ namespace

  - for instance, with mod_wsgi scripts you need something like:

        import __main__
        __main__.__requires__ = ['foo < 2']

### A new ENVVAR specifying config files 

- Config files specifying the version ranges of packages that you depend on.
- On startup, python reads these config files to determine how import will behave.
- Need to specify these package version requirements before python starts to process imports
- Config files are specified via a colon separated list in a python envvar or on the command line.
  - Multiple config files are needed so that you can specify information from multiple apps
    - (for instance, mod_wsgi could be running multiple apps. It should be possible to use one config file for each app and merge the mappings as long as there are no conflicts in versions).
  - Recommendation to distro packagers \-- only a single config file (or none) for a program
  - We do not parse the dependencies that are in the egginfo in addition because the
    - information there is not supposed to be required according to distutils and this makes it required. However, this does mean that we\'re specifying certain requirements twice. (Note: Only the ones where we\'re installing multiple versions onto the system).
- then python uses that to map from the version to a location on the filesystem

#### Why not just use PYTHONPATH? 

The location of the package will need to depend on both the python package name and its version. For instance: `/usr/lib/python2.7/site-packages/foo-1.0/foo` This location specifies and exact version. PYTHONPATH would require us to specify that exact version as well: `PYTHONPATH=/usr/lib/python2.7/site-packages/foo-1.0/foo`. This will break the moment we upgrade to a different version of foo even if it\'s API compatible. Using a config file means that we get a range of versions.

### Use a symlink farm 

- When an application (or python package) foo requires a specific version of a package, symlink the specific versions in `/usr/lib/python2.7-imports/foo/`. Then modify foo (either via a wrapper script that sets PYTHONPATH or modifying sys.path directly in the python script) to set that path as the first place to look for packages. That way it will be looked in before site-packages.

#### Questions 

- What, if anything, should core python know about this directory structure?
  - At the moment we think nothing
- Should the python docs suggest a standard location?
  - See the [Action section](./PyCon2011(2f)Distro(20)Sprint.html#Actions)
- How do we make this \"easy enough\" for users to also use (for instance, if they\'re writing an app that needs an old version)?
  - Possibly tie into virtualenv so that virtualenv can easily find the different versions that we have installed on the system.

### Actions 

- We think that the [symlink](./PyCon2011(2f)Distro(20)Sprint.html#Use_a_symlink_farm) idea will work and be the least invasive. Our action is to try implementing this in packaging and create any tooling that is needed (Tooling may be overengineering).

- We need to talk to Larry Hastings at [PyCon](PyCon) since he\'s adding some virtualenv features into python core. Object of discussion is to figure out how to make it easier for users to access the different versions of the packages that users might need.

- Depending on the above, write PEP for anything needing support from python itself.
  - Maybe write an informational PEP for distros to be pointed at if some of this is not required support from python itself.

## Duplicate named modules 

Problem, sometimes there\'s more than one python module that shares the same name. then we have to get someone to rename modules.

- A service that watches for pypi uploads and then compares the
  - files against the files in the distro. If the files are in another distro package, the distros could send an email to the new uploader that they should change the name.

- Get RSS feed for file uploads for [http://pypi.python.org/pypi/](http://pypi.python.org/pypi/)

- service downloads the files and checks the filelists against what the distro provides

- distros can send mail when a new upload starts conflicts with existing packages

- At the moment, no one wants to work on this type of service, largely because of the next item.

- This is a social problem; would love to find some better solution

### Actions 

- No actions without someone who has time and inclination to work on this. We\'re still trying to think of a better solution.

## Numpy 

Quick questions about packaging best practices and the FHS.

- Can change headers install location to be somewhere different.
  - But need to also change a function to find the new installation location.
- Numpy and scipy could be built with blas/lapack and not atlas but it\'s
  - preferred if blas and lapack actually point to libatlas. numpy uses cblas in some places. Dynamic loading thing, not compilation.

## Namespace packages 

Some questions about how namespace packages will affect python

- Do they make import performance worse when nfs home directories are involved because of the .pth files?
- Maybe work needs to be done on python\'s import to make it better?
  - Identify performance problems that we need to care about
  - Write importhook proof of concept
  - Then write a PEP and bounce it off Barry then python-dev
  - Possibility \-- specify the semantics that we need from the importer then rip out things that aren\'t
    - needed/backwards compatibility in the current import code (for instance, import from zip file).

## Licensing issue 

Paul Hildebrandt asked about meeting with Matthias Klose and Van about licensing concerns for Lib/profile.py and Lib/pstat.py. Unfortunately, van was not around and Paul was worried it would have to wait another year for resolution (next [PyCon](PyCon)).

### Action 

- Toshio sent email to Tom Callaway to see if Tom thought the licensing could cause issues. If so, that could be enough for Paul to get it brought to the right people\'s attention to remove the possibly problematic clause.

## Day 2 

### Bento & distutils2 discussion 

- David showed Toshio, Barry, and Tarek how Bento works
  - Takes ideas from autotools for what configuration is available, has declarative config file (similar to distutils2) for simple things, and has good support for extending in a simple manner.
- Discussion of distutils2 extension points and how bento could be integrated in as an alternative builder.
- distutils2 Command class is still in need of work or perhaps replacement.
- Command class has received some work to:
  - Take out old code, etc and use stdlib modules instead (arg parsing =\> stdlib, for instance).

  - Have hooks to use different compilers and compiler flags depending on what we\'re building/building for

  - Want more hooks
- What is the API provided for hooks?
  - hook that is called after metadata is read =\> (Distribution object, cfg file metadata)

  - hook that is called pre and post every distutils2 Command \<= (Distribution object, Command object)

#### Action 

- David and Tarek will continue talking about the Command class. Working on what the command class needs to look like to support numpy, scipy, bento in a reasonable manner.

### Byte/unicode issues on python3 

#### Surrogate escape 

##### Problem 

We now have surrogateescape being used to deal with undecodable bytes on system interfaces (for instance, os.listdir, os.environ). Strings that are decoded using this throw a traceback when printed output to files (or otherwise leaving python\'s control) unless we explicitly change the errors method to use surrogateescape (to reencode the data properly). The question is how is this better than the python2 byte str which would sometimes traceback when implicitly being converted to unicode.

##### Rationale 

Talked to Martin and came up with the idea that as long as the surrogateescaped string remains within python or output to the same sort of system interfaces as it was created with (os.environ, open and other filesystem interfaces) there are no tracebacks, things simply work. Programmers are going to have to deal with undecodable bytes when they transfer it to a different type of interface (outputing into a file, printing to the terminal) anyway, so a traceback is appropriate at that point.

The best practice for programmers needs to evolve. Programmers will need to convert between surrogateescaped strings and strings escaped in a unicode compatible manner (xmlescaped byte value, etc). The two options that seem immediately present are to convert immediately upon getting the values (then the programmers can check that their code uses system interfaces) and if they have those, then they can transform the strings at that time. If they think that they are going to use those strings in other system interfaces (like grabbing the filename in os.listdir, then opening that file and reading its contents) they\'ll need to keep the surrogateescaped filename around somehow so it will be more appropriate for them to either stay with the surrogateescape format or store two versions of the filename.

#### Import of non_ascii module names 

#### Action 

- Talk about whether we have common concerns about non_ascii module names
