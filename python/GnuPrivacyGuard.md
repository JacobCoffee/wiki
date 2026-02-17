# GnuPrivacyGuard

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# General information 

[GNU Privacy Guard](http://www.gnupg.org) is a Free Software GNU GPLed implementation of the crypto standards OpenPGP and CMS (used by S/MIME). Also known as \"GnuPG\" or \"GPG\". There are a couple of principal ways to access GnuPG functions from Python programs:

1.  use the official GPGME library.
2.  run the gpg commands and pipe to them.

The GnuPG initiative recommends using GPGME because it provides a documented API.

# Accessing GnuPG via gpgme 

[GPGME](https://gnupg.org/software/gpgme/index.html) is the official library for accessing GNU Privacy Guard from programs. Although there are [python bindings for GPGME](https://pypi.org/project/gpg/) included within [PyPi](./PyPi.html) which could be installed with `pip`{.backtick}, this is not recommended by the GPG project and is unlikely to work since the [PyPi](./PyPi.html) library version would have to exactly match the version of GNUPG installed on your system. Instead either

- install and use the version available with your operating system (see table below)

or

- build gpgme and the associated language bindings and [install from source](https://git.gnupg.org/cgi-bin/gitweb.cgi?p=gpgme.git;a=blob_plain;f=INSTALL;hb=HEAD)

The manual is currently missing from the various python documentation repositories but there is an [online manual at adversary.org](https://files.au.adversary.org/crypto/gpgme-python-howto.html) ( ![/!\\](/wiki/europython/img/alert.png "/!\") bad HTTPS certificate at time of writing).

## per operating system install instructions 

The following commands should install gpgme\'s python library on various operating systems

::: {}
  ---------------------------------------------- ------------- ---------------------------
  **operating system**                           **package**   **example command**
  [alpine](https://alpinelinux.org/)     py3-gpgme     `apk add py3-gpgme`
  [debian](https://www.debian.org/)      python3-gpg   `apt install python3-gpg`
  MacOS ([homebrew](https://brew.sh/))   gpgme         `brew install gpgme`
  [Ubuntu](https://ubuntu.com/)          python3-gpg   `apt install python3-gpg`
  ---------------------------------------------- ------------- ---------------------------
:::

# Running gpg executables 

There are multiple libraries which drive the gpg binary as a program and interpret its output. This approach is older and more mature than the library but is not recommended and has lead to a number of vulnerabilities both in the python modules, related systems and other programs such as email programs which work in this way.

## pretty-bad-protocol

[pretty-bad-protocol](https://pypi.org/project/pretty-bad-protocol/) is a rewrite of python-gnupg with a more conservative coding approach. This library can be installed with:

`python -m pip install pretty-bad-protocol`

improvements over `python-gnupg`{.backtick} include whitelisting of `gpg`{.backtick} program output designed to protect against vulnerabilities caused by changes in the program output.

## python-gnupg

[python-gnupg](https://pypi.org/project/python-gnupg/) is the most widely used and recommended library. This library has had multiple vulnerabilities in the past, however it is under active development so currently known vulnerabilities are believed to have been fixed. It can be installed with:

`python -m pip install python-gnupg`

# history

Not mentioned in this history there are a number of other old libraries which were built to support access to GNU Privacy Guard. These probably should not be used in new projects.

## history of libraries that call the gpg program 

The original Python/GnuPG interface was written by [amk](http://amk.ca/). This was updated in 2005 by [SteveTraugott](SteveTraugott) to GPG.py 2005 using pipes) building on Richard Jones\' 1.3 update and adding more support for the decryption, signing, key management, bells, whistles, and so on which amk\'s original design implied. This was still a pure-python implementation for Python 2.2.1 requiring only gpg executable itself. This was \*not\* a drop-in replacement.

In parallel with the GnuPG interface a separate [GnuPGInterface](https://pypi.org/project/GnuPGInterface/) was released in 2002. This project has not been updated since 2006 and the project pages are now broken so it should no longer be used in new software. It concentrates on interacting with GnuPG via filehandles, providing access to control GnuPG via versatile and extensible means.

After four years from Steve Traugott\'s work, in July 2009 Vinay Sajip updated the module (now called gnupg.py to avoid confusion) and made it available (under the New BSD License) in tarballs on Google Code. The new version uses the subprocess module and so is easiest to use under Pythons \>= 2.4. A unittest harness was also included.

In 2013, in response to vulnerabilities in python-gnupg, a fork was made by Isis Lovecruft, this was initially available on [PyPi](./PyPi.html) as `gnupg`{.backtick} but has now been [renamed to pretty-bad-protocol](https://blog.patternsinthevoid.net/pretty-bad-protocolpeople.html) to avoid any confusion. This library has now completely rewritten the original and has not been vulnerable to some vulnerabilities which have been found in python-gnupg since.

## pgpme based libraries history 

GPGME was originally released as a C library. A library exposing the gpgme library to Python, [PyMe](http://pyme.sourceforge.net/) was released which provided bindings for this. [PyMe](./PyMe.html)\'s development model was based on GPGME + Python + SWIG (just like m2crypto is an OpenSSL + Python + SWIG) meaning that most of the functions and types were converted from C into Python automatically by SWIG. That library has [now been merged into GPGME](https://git.gnupg.org/cgi-bin/gitweb.cgi?p=gpgme.git;a=blob;f=lang/python/README;hb=HEAD) and is supposed to be maintained there.

[pygpgme](https://launchpad.net/pygpgme) ([PyGPGME on PyPi](https://pypi.org/project/pygpgme/)) was started by James Henstridge. Beside Python2 it supports Python 3 since v0.3 (March 2012). The wrapping is done using python\'s C interface directly without using a generator tool like SWIG. This project has not been updated since 2013 and should probably be considered obsolete.

# related libraries 

The following libraries work with GNU PG to provide other functions.

## pgp-mime (using the assuan protocol to gpgme-tool) 

[pgp-mime](http://pypi.python.org/pypi/pgp-mime/) makes it easy to construct, verify, and send signed and/or encrypted email. It uses a [pyassuan](http://pypi.python.org/pypi/pyassuan/)-based connection to [gpgme-tool](http://git.gnupg.org/cgi-bin/gitweb.cgi?p=gpgme.git;a=blob;f=src/gpgme-tool.c;hb=HEAD) for the cryptography, which is isolated in a `pgp_mime.crypt` module if you don\'t need the extra email-handling functionality. This currently uses gpgme by running `gpgme-tool` via `subprocess`.

This module was created in 2012 and does not seem to have been updated since then so may not be suitable for production use.
