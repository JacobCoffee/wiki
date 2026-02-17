# PyQt/GUI_Testing

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# GUI Testing 

The following list is a collection of resources that may be useful to people who want to test their PyQt user interfaces:

- [dogtail](https://gitlab.com/dogtail/dogtail) ([example code](https://gitlab.com/dogtail/dogtail/-/blob/master/examples/kwrite.py?ref_type=heads))

- [pytest](https://pytest.org) with the [pytest-qt](https://pypi.python.org/pypi/pytest-qt) plugin

  - [example](https://github.com/pytest-dev/pytest-qt/#pytest-qt)

- [Squish](http://www.froglogic.com/) (non-free)

The [Unit Testing](Unit_Testing) page deals with more general unit testing issues.

## Historical 

The following possibilities seem to be outdated (i.e., using old Python/PyQt versions, having broken weblinks or unmaintained libraries where the last release is more than five years ago). They are kept here for historical purpose and in the hope that one day some of these projects will be revived.

- [How to write unit tests for PyQt GUI widgets](http://www.voom.net/pyqt-qtest-example/) using only the open source modules included in [PyQt](PyQt) and Python

- [PyQt testing with nose](http://lists.idyll.org/pipermail/testing-in-python/2009-June/002024.html) - a thread from the python-testing mailing list which describes various options

  - [LDTP](http://ldtp.freedesktop.org/wiki/) uses accessibility libraries to perform GUI testing

    - Due to the conflicting libraries in use on Linux desktops (ATK vs. D-Bus) and the fact that D-Bus-based accessibility is often disabled for Qt applications, this may not be a workable option.

- [Hooq](http://gitorious.org/hooq/hooq) (see this [blog article](http://www.fredemmott.co.uk/blog/2010/01/18/Qt4%20GUI%20Testing%20with%20Hooq))

  - Another [blog article](http://shiqiyang.com/blog/?p=195) about using Hooq with PyQt4

- [PyGUIUnitTest: A GUI Testing Framework](http://www.pyzine.com/Issue007/Section_Articles/article_PyGUIUnittest.html)
