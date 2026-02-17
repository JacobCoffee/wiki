# SIP

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# SIP 

SIP is a tool for quickly writing Python modules that interface with C++ and C libraries. Its home page is at [http://riverbankcomputing.co.uk/software/sip/intro](http://riverbankcomputing.co.uk/software/sip/intro). It was written by Phil Thompson who is still actively maintaining it.

Full documentation can be found at [http://riverbankcomputing.co.uk/static/Docs/sip4/index.html](http://riverbankcomputing.co.uk/static/Docs/sip4/index.html).

SIP is used principally to support [PyQt](PyQt) and [PyKDE](PyKDE). Without it, it would be near impossible to manage the vast APIs these libraries provide.

Since v4.0 SIP can be used to interface Python with C libraries.

For earlier versions of SIP, a simple wrapper written in C++ was usually necessary. A proof of concept can be found with Jonathan Gardner\'s [sipPQ](sipPQ), a python module that interfaces directly with libpq, which is the C library used to interface with PostgreSQL. You can find this at [http://sourceforge.net/project/showfiles.php?group_id=61057](http://sourceforge.net/project/showfiles.php?group_id=61057).

------------------------------------------------------------------------

## More Details 

SIP is really the combination of four components.

1.  A template language resembling C++ class declarations that describes how the Python module will interface with the C++ library.
2.  A tool to convert the script into C++ code and Python modules.
3.  A module to support the resulting Python modules and allow the programmer access to some of the SIP internals for special cases.
4.  A pure Python build system that supports dozens of platform/compiler combinations.

------------------------------------------------------------------------

*Excerpt from [Programming With Sip](http://www.panix.com/~elflord/unix/siptute/):*

**Introduction**

This is by no means an authoritative discussion about SIP. Rather, it is a chronicle of the adventures and misadventures of a bumbling newbie trying to learn to use a great tool with little documentation. Some references that are essential in conjunction to this include:

- [PyQt](PyQt): an implementation of Python bindings for Qt. Reading the Sip files for these classes is instructive.

- [Official Sip 4 documentation](http://www.riverbankcomputing.co.uk/static/Docs/sip4/index.html) \| [Old documentation](http://www.controlvideo.de/sip/).

**A Note About Versions**

sip has changed from version to version. I\'m using python 2.2 and sip 3.0pre7. Depending on the verion you\'re using, sip will behave a little differently. The most notable addition to the new version of sip is support for classes that are wrapped inside namespaces.

------------------------------------------------------------------------

## ViM Syntax Script 

Jonathan Gardner has written an incomplete sip syntax script. You can use it when you are writing a sip script with the ViM editor.

[http://vim.sourceforge.net/scripts/script.php?script_id=659](http://vim.sourceforge.net/scripts/script.php?script_id=659)

## Tutorials & additional docs staff 

Googling the web on SIP tutorials brought up

- [http://www.controlvideo.de/sip/](http://www.controlvideo.de/sip/)

- [Official Documentation](http://www.riverbankcomputing.com/static/Docs/sip4/sipref.html)

- [http://www.panix.com/\~elflord/unix/siptute/index.html](http://www.panix.com/~elflord/unix/siptute/index.html)
