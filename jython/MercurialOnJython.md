# MercurialOnJython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Jason Briggs did some investigation of Hg on Jython ([http://blog.headius.com/2007/08/business-case-for-supporting-jython.html](http://blog.headius.com/2007/08/business-case-for-supporting-jython.html)), apparently this requires implementing at least:

- bz2 - part of UpgradeTo25CPythonLib, we might be able to use [http://www.kohsuke.org/bzip2/](http://www.kohsuke.org/bzip2/)
- cx_bsdiff - Source code here, [http://sourceforge.net/projects/cx-bsdiff/](http://sourceforge.net/projects/cx-bsdiff/) with more documentation at [http://starship.python.net/crew/atuining/cx_bsdiff/](http://starship.python.net/crew/atuining/cx_bsdiff/)
