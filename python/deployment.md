# deployment

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

One of the most-frequently asked questions of all time is this: \"I have a Python application I\'ve developed; how do I deliver it to my customer/friend/\...?\"

Here are typical answers:

- tar up the source and send it. It\'s reasonable to expect that the end-user\'s host will have Python installed. MacOS comes that way; most Linux distributions do; and Python is easy enough to install under Windows

- for Windows, use [MovablePython](MovablePython);

- for this purpose, [Pyrex](Pyrex) can be regarded as a language variant to Python itself;

- [Freeze](Freeze)

- [cx Freeze](./cx(20)Freeze.html)

- [py2app](./MacPython(2f)py2app.html) is for Macintosh

- [py2exe](./py2exe.html)

- [PyInstaller](PyInstaller) (supports Windows, Linux and soon Mac)

- [Esky](Esky) (adds a bootstrap executable and allows to auto-update your applications over the network or from local directory; supports Windows, Linux and Mac)

- [Pyarmor](Pyarmor) (obfuscate python scripts, bind obfuscated scripts to fixed machine or expire obfuscated scripts)

[FredrikLundh](FredrikLundh) [discussed](http://effbot.org/zone/python-compile.htm) some of these in 2003.

As of 2007, py2exe perhaps is second in use only to source distribution.
