# GuiProgrammingShootout

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

To compare libraries, it is often useful to have the same problem implemented using different libraries.

This could be one medium size application (this has been discussed in comp.lang.python). But it could also be demo implementations of common GUI related tasks:

- certain effects using layout managers
- dynamic menus
- loading key bindings from a configuration file (and changing menu labels and tooltips accordingly)

This could actually be the start of a cookbook for each toolkit.

------------------------------------------------------------------------

### Opinions and other subjective material 

*The stuff below should probably be moved to another page. Factual errors (concerning Qt on Windows) have been addressed with a correction - the author probably meant to indicate that their contribution (particularly the \"not free\" remark) was just their opinion and simply forgot to attach their name to it.*

Not sure the right spot for this addition, but I\'m looking for a comparision of Python vs. REALBasic for GUI Application development TIA, \-- Dean [goodmansond@yahoo.com](mailto:goodmansond@yahoo.com)

- Python is free and open source and has hundreds more of (also free) libraries available. If you want a free (for Linux) GUI builder that is most similar to REALBasic & Visual Basic, see QT Designer and [PyQt](PyQt). To use QT Designer on Windows, see [BlackAdder](./BlackAdder.html), but it is not free then. For Windows development though, [WxPython](WxPython) is probably better than PyQt. [PyGtk](PyGtk) is also very nice.

  - For the record, from Qt 4 (and [PyQt4](PyQt4)) onwards, Qt (and [PyQt](PyQt)) is available under the GPL on Windows, too. See [this overview](http://www.trolltech.com/products/qt/licenses/licensing/opensource) for details. \-- [PaulBoddie](PaulBoddie)

I would also like to see a comparison of toolkits and GUI builders to Visual Basic. More than that I would like to see comparisons for migration paths from existing Visual Basic applications to various Python toolkits. This is sadly a real need out there for some of us. Cross platform is a must, so toolkits along the lines of wxPython are necessary when dealing with VB migration. TIA. \-- Jason [jtgalyon@gmail.com](mailto:jtgalyon@gmail.com)
