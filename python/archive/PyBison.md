# PyBison

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PyBison - Scott Hassan - 1997 

**PyBison** is a YACC (Yet Another Compiler Compiler) style parser. PyBison was written by Scott Hassan in 1997 and almost disappeared.

There are scattered references to it all over the web, which all seem to point to `http://coho.stanford.edu/~hassan/Python/pybison.tar.gz`, which forwards to the dead link `http://dotfunk.com/hassan/homepage/Python`

[ActiveState](../platforms/ActiveState) has a copy (version 0.1.0.0 as of 2005-08-19):

- [for linux-i686](http://ppm.activestate.com/PPMPackages/PyPPM/2.2/packages/PyBison-0.1.0.0.linux-i686.2.2.tar.gz)

- [win32](http://ppm.activestate.com/PPMPackages/PyPPM/2.2/packages/PyBison-0.1.0.0.win32.2.2.zip)

# PyBison - David McNab - 2004 

A *completely different* PyBison can be found at (version 0.1.8 as of 2006-06-22):

- [http://www.freenet.org.nz/python/pybison/](http://www.freenet.org.nz/python/pybison/)

This PyBison was designed and written by David McNab and has an OO model inspired by PLY ([http://www.dabeaz.com/ply/](http://www.dabeaz.com/ply/)). This PyBison has existed since April 2004. But this link is also dead.

PyBison takes input in the form of typical lex and yacc files (with some restrictions) and builds and compiles a C Python module based upon them. The compiled Python parser module calls into Python code to execute actions for each grammar production but all the lexical and parsing work happens in compiled code. The advantages of PyBison are having the full expressiveness of lex and yacc to describe your grammar and fast parser execution.

New link (as of 2013-11-28):

[http://freenet.mcnabhosting.com/python/pybison/](http://freenet.mcnabhosting.com/python/pybison/)
