# PyQt

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## About PyQt 

PyQt is one of the most popular Python bindings for the Qt cross-platform C++ framework. PyQt was developed by [Riverbank Computing Limited](http://www.riverbankcomputing.com). Qt itself is developed as part of the [Qt Project](http://qt.io). PyQt provides bindings for Qt 4 and Qt 5. PyQt is distributed under a [choice of licences](./PyQt(2f)PyQtLicensing.html): GPL version 3 or a commercial license.

PyQt is available in two editions: PyQt4 which will build against Qt 4.x and 5.x and PyQt5 which will only build against 5.x. Both editions can be built for Python 2 and 3. PyQt contains over 620 classes that cover graphical user interfaces, XML handling, network communication, SQL databases, Web browsing and other technologies available in Qt.

The latest iteration of PyQt is v5.11.3. It fully supports Qt 5.11.2.

PyQt4 runs on Windows, Linux, Mac OS X and various UNIX platforms. PyQt5 also runs on Android and iOS.

## PyQt Documentation 

Current documentation is available for [PyQt4](http://pyqt.sourceforge.net/Docs/PyQt4/) and [PyQt5](http://pyqt.sourceforge.net/Docs/PyQt5/).

A collection of links to books can be found on the [Books](./PyQt(2f)Books.html) page.

- Michael Herrmann\'s **[PyQt5 book](https://build-system.fman.io/pyqt5-book)** quickly shows how to create desktop applications. It includes a foreword by Phil Thompson, the creator of PyQt.

- **[Create GUI Applications with Python & Qt](https://www.learnpyqt.com/pyqt5-book)** by Martin Fitzpatrick, covers beginner and advanced PyQt5 topics. Includes chapters on multithreading, Model Views & databases, Qt stylesheets and data visualization.

- **[Beginning PyQt: A Hands-on Approach to GUI Programming](https://www.apress.com/gp/book/9781484258569)** by Joshua Willman, takes a practical approach to building PyQt5 GUI applications and covers a variety of different GUI-related topics.

## Tutorials 

A comprehensive list of tutorials can also be found on the [Tutorials](./PyQt(2f)Tutorials.html) page, which includes PyQt5 tutorials from the following sites:

- [fman build system](https://build-system.fman.io/pyqt5-tutorial)

- [Coders Legacy](https://coderslegacy.com/python/pyqt5-tutorial/)

- [Learn PyQt](https://www.learnpyqt.com)

On this Wiki, you can also find the following tutorials, now mostly of historical interest only:

- A tutorial presented by Jonathan Gardner at the 2003 Northwest Linux Fest is available at [JonathanGardnerPyQtTutorial](JonathanGardnerPyQtTutorial).

- A tutorial presented by Oleksandr Yakovlyev for embedding PyQt in C++/Qt application [EmbedingPyQtTutorial](EmbedingPyQtTutorial)

## Developing with PyQt and PyKDE 

- [Tutorials](./PyQt(2f)Tutorials.html) contains a list of tutorials and walkthroughs

- [Books](./PyQt(2f)Books.html) contains a list of books about Qt, PyQt, KDE and PyKDE

- [Development With PyQt](./PyQt(2f)DevelopmentWithPyQt.html) can be made even easier with some extra tools and information

- [Sample Code](./PyQt(2f)SampleCode.html) lists some pieces of code to solve some common programming problems

- [Overviews and Guides](./PyQt(2f)Overviews_and_Guides.html) provides in-depth information and detailed examples

- [Docs And Howtos](./PyQt(2f)DocsAndHowtos.html) contains links to API documentation and articles about developing with PyQt and PyKDE

- [Some Existing Applications](./PyQt(2f)SomeExistingApplications.html) written with PyQt and PyKDE

- [Third Party Packages and Modules](./PyQt(2f)Third_Party_Packages_and_Modules.html) for use with PyQt and PyKDE

- [GUI Testing](./PyQt(2f)GUI_Testing.html)

- [Videos](./PyQt(2f)PyQtVideos.html) about PyQt on various video sites

## PyQt Applications 

A list of applications that use PyQt as their UI layer can be found on the [Some Existing Applications](./PyQt(2f)SomeExistingApplications.html) page. This replaces the list previously found here.

Similarly, the [Third Party Packages and Modules](./PyQt(2f)Third_Party_Packages_and_Modules.html) page provides a list of resources that can be used to help build applications with certain features.

A collection of [Sample Code](./PyQt(2f)SampleCode.html) is also available to help with specific problems and use cases.

## Links to other resources 

The [official mailing list](https://www.riverbankcomputing.com/mailman/listinfo/pyqt) is a high signal-to-noise discussion list for PyQt users and developers.

Phil Thompson was [interviewed about PyQt](http://web.archive.org/web/20070208043017/http://dot.kde.org/1155075248/) for [KDE Dot News](http://dot.kde.org) in August 2006, and [profiled](http://web.archive.org/web/20010201180600/http://www.sunworld.com/sunworldonline/swol-05-2000/swol-05-regex_2.html) for *SunWorld Online* in 2000.

## Earlier Versions 

**This section describes PyQt version 3 (for Qt 3).**

PyQt implements around 300 classes and over 5,750 functions and methods including:

- a substantial set of GUI widgets

- classes for accessing SQL databases (ODBC, [MySQL](MySQL), [PostgreSQL](PostgreSQL), [Oracle](Oracle))

- QScintilla, [Scintilla-based](http://www.scintilla.org/) rich text editor widget

- data aware widgets that are automatically populated from a database

- an XML parser

- SVG support

- classes for embedding ActiveX controls on Windows (only in commercial version)

Earlier versions of PyQt included a graphical debugger called `eric`, written using PyQt, which can be used to debug PyQt and ordinary Python console applications. It\'s now available separately as `eric4` from [http://eric-ide.python-projects.org/index.html](http://eric-ide.python-projects.org/index.html).

PyQt includes `pyuic` which generates Python code from GUI designs created with Qt Designer. This makes PyQt very useful as a rapid prototyping tool for applications that will eventually be (partly or completely) implemented in C++ because the user interface designs can be re-used without modification.

------------------------------------------------------------------------

[CategoryPyGUI](CategoryPyGUI)
