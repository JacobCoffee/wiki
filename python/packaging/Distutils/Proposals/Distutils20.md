# Distutils/Proposals/Distutils20

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

There are various fixes and improvements that should form part of a 2.0 version of Distutils.

Note: many of these features are being implemented in [setuptools](http://peak.telecommunity.com/DevCenter/setuptools), which is where most distutils-related development is happening at this time (Sept 2005). I\'ve noted features that setuptools supports below \-- [IanBicking](IanBicking)

The ultimate goal:

- **Must be backwards-compatible with existing setup.py scripts.**

Quick things from [PyCon](PyCon):

- Some people want to run a build command (or whatever) programmatically; the only way to do this is to poke the right arguments into sys.argv. (Not true! Use `setup(script_args=[...])`{.backtick}! \--PJE)

- building tar archives could use the 2.3 tarfile module instead of requiring the platform have a tar command.

- bdist_py2exe, bdist_msi, other executable installers. *(setuptools allows external packages to add new setup.py commands, so commands like bdist_py2exe can be applied globally to all setup.py files; zpkg provides facilities to add new commands to distributions it builds)*

Other ideas:

- Some methods may trigger [PendingDeprecationWarning](./PendingDeprecationWarning.html)s

- Move various utility methods out of command implementations and onto the Distribution class.

- Implement the package database described by PEP [0262](http://www.python.org/dev/peps/pep-0262 "PEP").

- Consider always regenerating the MANIFEST from MANIFEST.in. *(setuptools can generate MANIFEST files more automatically, and triest to keep MANIFEST in proper shape)*

- Finish bdist_dpkg.py ([easy-deb](http://easy-deb.sourceforge.net/) is doing deb generation)

- Use optparse instead of fancy_getopt.py, and deprecate fancy_getopt.py.

- sdist: Include scripts, data automatically in the source distribution.

- Drop Python 1.5.2 compatibility. Keep Python 2.0 compatiblity. (2.3, 2.4 compatibility?) *(setuptools is currently only 2.3+ compatible; feature accomplished! ;)*

- Improve test coverage. (See the [DistutilsTesting](DistutilsTesting) page for ideas.)

- Finish the documentation! ([AnthonyBaxter](AnthonyBaxter) has worked on a reference guide; his text has been added to [Distributing Python Modules](http://docs.python.org/dist/dist.html) as the [API Reference](http://docs.python.org/dist/api-reference.html) chapter, but a lot more work is needed.)

- Package installation from PyPI (probably driven by the pythonmac-sig) *([EasyInstall](EasyInstall), included with setuptools, handles this)*

- Add more autoconf-like tests to the config command

- Make the design more extensible w.r.t. \'foreign\' module compilation, specifically:
  - Allow the integration of autoconf/make based build systems for C/C++ extensions
  - Allow \'Extension\' to be composed of components, each with their own build rules
  - Provide a means for scripts / modules to access installation parameters such as datafile directories

- Define more default commands to build documentation, run (unit) tests, etc. *(setuptools adds a test command, and can be extended easily with more commands; [buildutils](http://buildutils.lesscode.org/) adds some more development-related commands)*

- Look at setuptools by Phillip J. Eby and buildutils (on PyPI) for further improvements.
  - \-- [StefanSeefeld](./StefanSeefeld.html)

Wouldn\'t it be a good idea to look into [scons](http://scons.sf.net) and try to let both converge as far as practical ? \-- [StefanSeefeld](./StefanSeefeld.html)

Maybe some traditional package concepts:

- Uninstallation. Also getting rid of obsolete files when upgrading. *([PythonEggs](./PythonEggs.html) \-- part of setuptools \-- can be uninstalled more easily than a traditional package; however, tools still don\'t exist to properly automate this)*

- Dependencies. A simple implementation might simply check to see if another library is installed and warn the user if not (and maybe install from PyPI if that feature exists). Declaring (or worse, resolving) version dependencies or alternatives seems like overkill for now. *(setuptools handles dependencies)*

  - \-- [IanBicking](IanBicking)

    - (I agree with dependency specification, but suggest dependency resolution should be the responsibility of the repository/catalog and the binary package manager.)

- Generation of multiple binary packages for a source distribution (ala Debian)
  - (The Egenix tools is a good example of where this would be useful)

  <!-- -->

  - \-- Mark Alexander

- Easy installation of non-python data files that are stored inside Python packages. Twisted uses this for plugins, it\'s also useful for storing .glade files together with the code for GTK GUI apps, etc..
  - \-- Itamar Shtull-Trauring

- [SciPy](SciPy) has some setup.py scripts that extended distutils. It may be a good idea to look there for ideas.

- Allow MANIFEST and MANIFEST.in to be located in a directory other than the package root directory.
  - \-- Michiel de Hoon

- If you use a version management system that toggles the read/write bits (e.g. perforce), distutils happily copies the mode bits when it copies files down to the build directory (etc), and then chokes when it tries to clean up after itself. (or worse, skips important build steps so you end up with a broken release\...)
  - \-- [FredrikLundh](FredrikLundh)

- It would be great if installers generated by bdist_wininst supported a \'silent\' flag for automated installs. The silent mode would allow the package to be installed without user intervention.

  - \-- Phil Rittenhouse

  Benji York at [Zope Corporation](http://www.zope.com/) has done some work on this; hopefully he\'ll be able to finish and release it at some point.

- bdist_wininst currently runs the \'install\' command to a temporary directory, then zips up this directory, and then creates a program which will unpack the archive on the target system. It should become much smarter. Maybe only running \'build_ext\' on the source system, and running the full \'install\' on the target system.

- I would also like to do much more in Python than in C in the bdist_wininst created installer. Wasn\'t possible in Python 1.5.2, because this didn\'t even have the zipfile module.
  - \-- Thomas Heller

- Python packages should have a canonical way of having C/C++ headers, executable scripts, dynamic libraries (For Win32, OS X), documentation, examples, and other arbitrary data (like fonts, icons, etc.) associated with them in the same folder (or a closely related folder with identical permissions) as the package itself. We could use something like Apple\'s bundles for this purpose (sans versioning, most likely). If a package wants to put things in places such as /usr/local/bin, they should be symlinks to what is in this new structure.

- Multi-module installs (more than one importable thing that goes into site-packages) should be deprecated. If they want this behavior they should install a package and use a pth file. (Counterpoint 1: There is strong demand for installing both packages **and** modules with a single setup.py. \--PJE) (Counterpoint 2: This would prevent creating distributions that provide dependencies in addition to some top-level application. \--[FredDrake](FredDrake))

- Add the following fields to PEP [0241](http://www.python.org/dev/peps/pep-0241 "PEP") (PKG-INFO): Package-Name (the actual python-importable name of what was just installed), Depends (a list of other packages, by Package-Name, that this package depends on), Recommends (a list of other packages, by Package-Name, that enhance the functionality of this package when present). These headers make the REQUIRES and PROVIDES (how was PROVIDES useful anyways?) files from PEP [0262](http://www.python.org/dev/peps/pep-0262 "PEP") obsolete.

  - \[Comment by Hartmut Goebel:

  - Package-Name is s good idea, since this name may differ from the project/archive name.

  - For RPMs, PROVIDES/REQUIRES may describe any type of resource, even abstract ones like \'mta\'. Thus I suggest extending PEP [0262](http://www.python.org/dev/peps/pep-0262 "PEP") here instead of obsoleting these fields.

  - Depends is very similar to REQUIRES, so what should be the benefit of this change? I agree, these should go into PKG-INFO. \]

- Perhaps a better way of finding C/C++ libraries/headers that an extension depends on, include support for OS X frameworks. Make linking to frameworks less hackish.
  - \-- [BobIppolito](BobIppolito)

- Files that are used by a package, i.e. config and data files (possibly others), should be relocatable.
  - \--Moxo

- Why should files be relocatable when you can just make symlinks? What would you need that for?
  - \-- [BobIppolito](BobIppolito)

- What if you can\'t make symlinks? (Windows?)
  - \-- Marek Baczynski

- Why would you ever need to move files around on Windows? Where would they go? There\'s no /usr/local/include on Windows. Similar OS X, you would have two package databases (system and user). OS X has a use case for at least three (vendor, system, user), because putting anything in /System (the vendor root) unless you\'re Apple is a horrible idea.

  \-- [BobIppolito](BobIppolito)

- Files need to be relocatable on any platform simply because there may not be sufficient disk space where the package \"wants\" to go. This is partially the responsibility of the native package manager for bdist\* commands, but distutils needs to support it by providing for relative installation paths via PYTHONDIR, PACKAGEDIR, CONFIGDIR, DATADIR, etc., variables with reasonable defaults based on the target system. There\'s no reason to arbitrarily impose locations on a sysadmin that needs additional flexibility, or prevent users without root access from installing binary packages into a user-writable area.
  - \-- Mark Alexander

- Well it already has to support at least three package locations anyway (vendor, system, user), so surely you\'ll be able to jigger some site_config.py or environment variable to add whatever installation path you\'d like and create a new installation database there. What I\'m against is moving things once they\'re already installed, especially when you only move PART of a package (i.e. just data files, not code). You should of course be free to choose whichever installation root you\'d like, but I\'m totally against giving the user a supported method for move things around on their own without an uninstall/reinstall cycle or at least some software tool to do it for them. It\'s NOT worth the pain.

- I don\'t consider consolidation of PYTHONDIR/PACKAGEDIR/CONFIGDIR/DATADIR arbitrarily imposed, there\'s good reason to keep stuff together. For example, if they\'re always close to each other on the filesystem, the code could ALWAYS locate its data dir relatively without having to look in /usr/local/share or some such, even if it were wholly moved elsewhere (another volume, not mounted as / maybe). Makes things much easier to package into self-contained units (i.e. py2exe, bundlebuilder on OS X) and it makes sense for something like Win32, which doesn\'t really have anywhere sensible to put that stuff in the first place. If you REALLY REALLY want to put python data files in /usr/local/share somewhere, then it should be \"/usr/local/share/python%(Python-Version)s/data/%(Package-Name)s\" or something completely unambiguous and standard. You shouldn\'t have to guess.

  \-- [BobIppolito](BobIppolito)

- One of the greatest problems that exist with perl\'s CPAN is the inability to keep track of what it has installed, which means one cannot uninstall packages through CPAN. Windows installer and RPM\'s (and .deb\'s when they finally show up) built using Distutils do not suffer from this fortunately\... But \'bdist\' binary distribution does. Would it make sense if these were kept track of so that there could be an \"uninstall\"? \"make; make install;make clean\" is not attractive without \"make uninstall\". \-- Moxo

- Uninstallation is solved as soon as we have an installation database, which is part of what we\'re trying to do here.
  - \-- [BobIppolito](BobIppolito)

- Extend bdist_rpm for \'hardcoding\' the python interpreter into the RPM and generate different Package names depending on the interpreter. See [Changes for bdist_rpm](./Changes(20)for(20)bdist_rpm.html) for reasoning and codesnippets.

  - \-\-- Hartmut Goebel

- Zope Corporation is looking at having some better packaging tools, including support for dependencies and automated package composition. The initial implementation of [zpkg](http://www.zope.org/Members/fdrake/zpkgtools/) is available and has been used for recent Zope 3 and ZODB releases. There is also a [discussion document](http://dev.zope.org/Zope3/Zope3PackagingProposal) in the [Zope 3 wiki](http://dev.zope.org/Zope3/) which describes some of the goals of the **zpkg** application.

  - \-\-- [FredDrake](FredDrake)

  NB: Since this time, Zope Corporation has abandoned zpkg in favor of [zc.buildout](http://buildout.zope.org/) and setuptools.

- Include bdist_nsi [http://bdist-nsi.sourceforge.net/](http://bdist-nsi.sourceforge.net/) to have a complementary tool for creating smart win32 installers (silent install, MUI, internationalization, uninstall) on both linux and windows using the [Nullsoft Scriptable Install System](http://nsis.sourceforge.net/) (NSIS).

  - \-\-- jcg
