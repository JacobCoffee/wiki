# MacPython/NewPackageManager

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Notes about what we need to do 

Also see: [http://www.python.org/cgi-bin/moinmoin/DistUtils20](http://www.python.org/cgi-bin/moinmoin/DistUtils20)

## Extending PEP-241 ( http://www.python.org/peps/pep-0241.html ) 

As per Sarwat\'s suggestion for canonical version numbers, we do have somewhat of a solution that I was unaware of: the [StrictVersion](http://epydoc.sourceforge.net/stdlib/public/distutils.version.StrictVersion-class.html) and [LooseVersion](http://epydoc.sourceforge.net/stdlib/public/distutils.version.LooseVersion-class.html) classes in [distutils.version](http://epydoc.sourceforge.net/stdlib/public/distutils.version-module.html). [LooseVersion](http://epydoc.sourceforge.net/stdlib/public/distutils.version.LooseVersion-class.html) will pretty much allow us to compare arbitrary 1.0a2 vs 1.0b2 version numbers reliably. If they don\'t compare reliably or can not be parsed by [LooseVersion](http://epydoc.sourceforge.net/stdlib/public/distutils.version.LooseVersion-class.html), the package author is not following spec and should be smacked around ![:)](/wiki/europython/img/smile.png ":)")

We need more metadata, here\'s what we need:

- **Metadata-Version**: needs to be bumped above 1.0

- **Package-Name**: We need something that tells us what the actual name of the package or module is! Right now the name is arbitrary and doesn\'t need to relate to the name of the module in Python.

- **Depends**: (optional) A list of other packages, by Package-Name (which must by definition follow python module naming guidelines), that this package depends on.

- **Recommends**: (optional) A list of other packages, by Package-Name, that enhance the functionality of this package (i.e. Twisted recommends [PyCrypto](./PyCrypto.html) because it enables Conch (the SSH2 client/server))

I believe this will be sufficient. However it may be nice to be able to specify C or C++ libraries that a package wraps or depends on (but does not include). Ideas?

One thing, related to Package-Name, is that we should completely deprecate the practice where you can install a whole bunch of python modules flat in site-packages. If you have more than one file that belongs in site-packages, it should go in a separate folder and be referenced by a pth file. There should be a 1:1 relationship between the number of modules+packages in your site-packages, and the number of modules+packages that you installed.

## Discussion of PEP-243 ( http://www.python.org/peps/pep-0243.html ) 

PEP-243 proposes a central module repository system for source modules. We should say that the [PackMan](./PackMan.html) system will supplant this because (a) it could take advantage of a central module repository if available and (b) it\'s easier these days to host open source projects anyways (a la sourceforge). Speaking of sourceforge, we should have special integration for sourceforge downloads in [PackMan](./PackMan.html) (let the user choose a preferred mirror, display to the use who is sponsoring their download). It\'s possible that the scapegoat may choose to come to an arrangement with the package maintainers such that package maintainers will host the scapegoat-built binary packages on their site to make it more economical for scapegoats.

## Embrace and Extend PEP-262 ( http://www.python.org/peps/pep-0262.html ) 

PEP-262 is the holy grail for [PackMan](./PackMan.html), it allows us to develop a sane way to do package management, especially uninstallation.

For our platform, PEP-262 has one inherent deficiency: INSTALLDB (the location for receipts) is a fixed location and not a search path. I propose that we leverage sys.path in our quest to locate the installation receipt database, that way we can find /System/Library/\... /Library/\... /Network/Library/\... \~/Library/\... or whatever is appropriate for that particular installation of Python. The installation database could have a file name that would be unacceptable as a python package name, such as INSTALL-DB, this way it could not possibly be confused with an actual package.

I think that we can deprecate the REQUIRES and PROVIDES files by adding Depends, Package-Name, and Recommends to PKG-INFO. I don\'t think that the \"PROVIDES\" file makes a whole lot of sense, unless the strings used in provides means it corresponds to a definitive module interface. There is not currently any sort of registry or PEP for this kind of thing, so it\'s probably not at all useful. Since we have upgraded PEP-241, we should also upgrade the Package class in PEP-262 to include the new metadata.

# Notes for NewPackageManager 

- Read \"[Package Manager idea, adding URL scheme](http://mail.python.org/pipermail/pythonmac-sig/2003-October/thread.html#8891)\" thread on pythonmac-sig very carefully

- Needs to have a receipt database for each installation location (PEP-262 extension)

- Needs extra metadata from PKG-INFO (PEP-241 extension)

- Must work without mandatory crypto support see commentary started by [MichaelHudson](MichaelHudson)

- Should use hashes to be as secure as possible without crypto, where hashes of the [PackMan](./PackMan.html) database should be available at 3rd party sites (i.e. \"I Jack Jansen, trust that Bob\'s repository has a SHA-1 hash of \.....\") see \"check integrity\" comments by [JackJansen](JackJansen)

- Should leverage SSL certificates (when assigned by a trusted CA) whenever possible

- Should be able to cryptographically sign a package list (i.e. PGP / [ElGamal](./ElGamal.html) / etc.)

- Focus is on binary package installs, but source package installs should also be supported

- Need to deal with people installing packages themselves

- Move to distutils.version for comparisons

- Move arbitrary code out of the plist as much as possible, leave possibility for pre/post installation scripts (with ample warning)

- Support uninstall, maybe a rollback?

- External frameworks/libraries inside the packages?

- Data belonging to packages in a plain way, possibly another PEP

- Don\'t use .plist as the file suffix, that makes it impossible to bind an application to package manager databases

# Notes for NewPackageManager GUI 

- Needs to be a lot smarter, less clutter, more organization (think trees, don\'t differentiate between binary/source installs, filter out packages the user has acceptable versions of, etc.)

- Support uninstalls, receipt viewing, do we need rollback?

- Mechanism to manually \"trust\" or \"untrust\" databases

- Mechanism to save favorite databases (maybe have recent databases at the root of the tree)

- Lots of warnings about security, show \"padlock\" for secure databases

- Make it a responsive application, show a lot of progress indications

- Probably fork python to do most things and communicate over TCP or some such

- Try not to import modules to check versions

- [../PyObjC](./MacPython(2f)PyObjC.html) implementation would be awesome, should also do [WxPython](WxPython) implementation for win32?

- Allow user to install from local files (downloaded binary packages or source packages themselves)

- Lots of version checks so the user is unlikely to break something by accident (package X v1.0 isn\'t known to work with package Y v1.1 yet, are you sure you want to upgrade Y?)

- Display package dependencies, maybe (advanced) let user decide which of them to install.

- Download once, install on several machines. Maybe just have a download cache folder where it keeps tarballs (which are presumably uniquely named), the user could point this to a network drive?

- Search field

# Bug and Feature Requests 

The current PM has faulty scrolling\-\--if a pimp site has a package list that is longer than the viewing area, one cannot scroll to see the extra content (well, you *can* scroll, but the window pops right back to the top). Packages are accessible via the arrow keys, but the faulty scrolling is clearly a bug. Make sure the new manager gets tested on a site with a *long* list of packages.

The following requests are motivated by those of us maintaining multiple systems, one or more of which have *slow* net connections. These requests have been echoed by at least one other user on the Pythonmac-SIG, so I suspect many would make use of such features.

First, I\'d love to see package size information in the PM window. This way I can tell if it\'s realistic to download a package to a machine with a dialup connection.

Second, I\'d love to see useful progress info on the download and installation. If I check **Verbose**, the current PM tries to produce this, but unfortuately the resulting text window update is too slow and I\'ll typically not see *any* of the progress lines until the download is complete, at which point the window happily shows me every status line from the start to 100%.

Finally, I\'d love for there to be a way to save a package locally in a way allowing it to be moved to another machine and installed via PM there. (This would also be useful for backup purposes, so one could restore a particular Python setup.) Ideally I\'d like to grab the packages on my fast-connection machine, and install them on the slow-connection machine.
