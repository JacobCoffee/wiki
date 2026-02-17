# eric

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

eric is a full-featured Python IDE that is written in [PyQt](PyQt) using the QScintilla editor widget.

eric\'s homepage is at [https://eric-ide.python-projects.org/](https://eric-ide.python-projects.org/)

The Python Qt bindings project has gone through some evolution and now has a home page at [https://doc.qt.io/qtforpython-6](https://doc.qt.io/qtforpython-6). There is also a tracking page on the [Qt Wiki](https://wiki.qt.io/Qt_for_Python). Also see [https://qscintilla.com](https://qscintilla.com).

The following is a partial list of eric\'s features:

- Any number of editors with configurable syntax highlighting, code folding, auto indenting and brace highlighting.
- Integrated Project Management facility to organize your projects. The project browser shows all source files, all forms and all translations each on its own tab. The source browser has built in class browsing capabilities.
- An integrated, full featured python debugger.
- An interactive Python shell.
- An explorer window for walking through your directory structure with built in class browsing capabilities for Python files.
- Variable windows that display local and global variables in the current scope while debugging a program.
- An integrated interface to the Python Module \"unittest\".
- An integrated help viewer to display HTML help files. Alternatively you can choose to use Qt-Assistant to view help files.
- Display of the UI in different languages.
- The capability to start Qt-Designer and Qt-Linguist from within eric.
- The ability to compile Qt-Designer forms, to produce Qt-Linguist files and release them from within the IDE.

Working with eric3 is mostly intuitive but sometimes doubts come out. Below is a list of questions asked to the author and his answers:

------------------------------------------------------------------------

**Q.** Is it possible to save open files (also not from project) list during project save?

**A.** \"Project save \" saves the project file. To save an open file use one of the save actions/menu entries.

------------------------------------------------------------------------

**Q.** What are Project::Load/Save Session options for?

**A.** A session file contains information about the last debug/run action, about breakpoint, open editors \... This info is saved with the save session action and loaded with the load session action. In the configuration dialog you may enable automatic session loading, which loads a saved session upon opening a project.

------------------------------------------------------------------------

[CategoryIntegratedDevelopmentEnvironment](CategoryIntegratedDevelopmentEnvironment)
