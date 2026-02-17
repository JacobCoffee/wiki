# UpgradeTo25CPythonLib

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: 
### Buildbots

- [http://www.acm.uiuc.edu/jython-buildbot/waterfall](http://www.acm.uiuc.edu/jython-buildbot/waterfall)
- [http://bob.underboss.org:8080/](http://bob.underboss.org:8080/)
:::

::: 
### To Fix

- test_import_jy - ?
- Windows failures - files not being properly closed
:::

::: 
### Flaky/arch?

- test_socket - historically this is the case on SO_RCVBUF, SO_SNDBUF. particularly flakey on solaris buildbots
- test_select - flakey on FreeBSD hudson buildbot
:::

::: 
### Under Development

Or perhaps more accurately, the following *should* be under development.

- test_unicode
  - test_codecs_idna - no idna encoding (which needs unicodedata 3.2.0) [http://bugs.jython.org/issue1153](http://bugs.jython.org/issue1153)
- test_stringprep - [http://bugs.jython.org/issue1758320](http://bugs.jython.org/issue1758320)
- \_rawffi (for ctypes, ported from PyPy)
- bz2 (Georgy Berdyshev is looking at this. Leo User\'s bz2 module code is available from here: [http://underboss.org/\~pjenvey/jython/jythonx-bits.tar.bz2](http://underboss.org/~pjenvey/jython/jythonx-bits.tar.bz2) )
- multibytecodec (implies test_multibytecodec_support)
- unicodedata - need a Java implementation, not our current Jython workaround (too slow to load, on the order of a couple of seconds)
:::
