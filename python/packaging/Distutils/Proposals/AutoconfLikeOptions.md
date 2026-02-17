# Distutils/Proposals/AutoconfLikeOptions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# The problem 

Python modules using distutils and setuptools are known to make linux distributors unhappy, for various reasons. One of them is that distutils does not make possible to install softwares according to the FHS without a lot of effort. This document is only concerned with the requirements to fix this situation at a minimal cost for python developers.

## Example 

Generally, a python packaged with distutils will be installed as follows:

           python setup.py install --prefix=$PREFIX

This will install the package in \$PREFIX/lib/python-\$PYVER/site-packages on Linux, plus scripts into \$PREFIX/bin. The documentation, python source files (.py) and architecture dependent files (C extensions) are all installed in one directory, thus violating the FHS.

## Autoconf 

Many open source softwares are distributed using autoconf. The steps to install a package from sources are:

           ./configure --prefix=$PREFIX
           make
           make install

The make install step will do something very similar to the distutils install command. The main difference is additional options available from the configure script for customization:

           --bindir=DIR           user executables [EPREFIX/bin]
           --sbindir=DIR          system admin executables [EPREFIX/sbin]
           --libexecdir=DIR       program executables [EPREFIX/libexec]
           --sysconfdir=DIR       read-only single-machine data [PREFIX/etc]
           --sharedstatedir=DIR   modifiable architecture-independent data [PREFIX/com]
           --localstatedir=DIR    modifiable single-machine data [PREFIX/var]
           --libdir=DIR           object code libraries [EPREFIX/lib]
           --includedir=DIR       C header files [PREFIX/include]
           --oldincludedir=DIR    C header files for non-gcc [/usr/include]
           --datarootdir=DIR      read-only arch.-independent data root [PREFIX/share]
           --datadir=DIR          read-only architecture-independent data [DATAROOTDIR]
           --infodir=DIR          info documentation [DATAROOTDIR/info]
           --localedir=DIR        locale-dependent data [DATAROOTDIR/locale]
           --mandir=DIR           man documentation [DATAROOTDIR/man]
           --docdir=DIR           documentation root [DATAROOTDIR/doc/libsndfile]
           --htmldir=DIR          html documentation [DOCDIR]
           --dvidir=DIR           dvi documentation [DOCDIR]
           --pdfdir=DIR           pdf documentation [DOCDIR]
           --psdir=DIR            ps documentation [DOCDIR]

Each of this option can be set independently if desired - the autotools handle each category independently. This has several advantages:

- the options can be set such as to follow the FHS as much as possible
- no policy is implemented by the developer. It is the job of the package developer to set those paths accordingly
- different policies can be implemented. For example, distributions like gobolinux which do not follow the FHS at all happily use autoconf-based packages

## Solution 

The solution is easy, at least in principle. Instead of indistinctively installing everything at one location, distutils should be able to deal correctly with the following kind of options:

           python setup.py install --bindir=$BINDIR --sbindir=$SBINDIR

to install the software as desired. Note that distutils does NOT have to know how to install things as required as the FHS: distutils does not need to implement any policy. Some Linux distributions do not follow the FHS - and happily package autoconf-based packages as they want (example: gobolinux).

## Categories 

Here are categories which are necessary to build a Debian package:

- scripts/binaries: bindir concept
- architecture independent files (.py, .pyc): datadir
- architecture dependent files (.so, .pyo ?): libdir
- html doc (htmldir)
- pdf doc (pdfdir)
- man doc (mandir)

TODO: others - include path, header path, var path for log, etc\... Other distributions, OS ?

## Distutils implementation 

Obviously distutils should internally keep separate lists for each kind of files.

Other problems:

- how to tag those files: for .py, .so and binaries, this is already done. Needs work for documentation, log

- UI to set the installation directories: this should not be difficult

- How to retrieve the files within the package. I have no idea how this is done in a standard C program in autoconf (but this is much less of a

  problem in that case, I guess - in python, using [file] and co is oftenly used).
