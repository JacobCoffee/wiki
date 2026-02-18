# PyjamasDesktop

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

PyjamasDesktop is a cross-platform framework and applications widget set for the desktop. There are three back-ends: [WebKit](http://webkit.org), [python-xpcom](http://pyxpcomext.mozdev.org) and MSHTML. The XULrunner port uses python-xpcom and hulahop; the Webkit port uses [PyWebkitGtk](../gui/PyWebkitGtk) and the MSHTML port uses python win32 comtypes. PyjamasDesktop is similar to [KiWi](http://www.async.com.br/projects/kiwi) in that it provides an easy-to-use API, where you need not know - at all - that you are running PyGTK, XULrunner or MSHTML underneath.

PyjamasDesktop is actually a port of [PyJamas](http://code.google.com/p/pyjamas) which is a web toolkit, so you also have the option of running PyjamasDesktop applications as web applications - unmodified.

The \[[PyJamas](PyJamas)\] Widget set is exceptionally comprehensive and yet is easy to use, providing:

- Simple, Horizontal, Vertical, Docking, Decking, Popup, Stack, Tab, Grid, Flow, Table and HTML Panels
- Text Labels and HTML including full CSS Stylesheet support and full CSS properties
- Input, Password and Textarea input boxes
- List drop-downs including Multi-selection
- Buttons, Checkboxes and Radio-Buttons including groups.
- Form Submit Panel (providing file upload).
- Treeview, Menu and Menubar (vertical and horizontal).

Additional features, thanks to the underlying use of web engines, include:

- Full CSS Stylesheet functionality, both local, remote and direct and simple API manipulation.

- Option of executing javascript, for full and complete manipulation of the application.

- Loading of complete HTML Pages, both local and remote; full URL support.

- Plugin support for multimedia plugins such as Flash (obsoleting the need for gtk-mozplugin)

- Access to XML, XSLT and AJAX.

- Full SVG Canvas support, like [HippoCampus](./HippoCampus.html), if the web engine supports it (currently only XULRunner)

It\'s specifically worth noting that due to PyjamasDesktop\'s history, it purely provides the \"V\" in \"MVC\" applications design. To communicate with the \"C\" in \"MVC\", it is recommended that you keep to XML and HTTP, and use, for example, the JSONRPC proxy client included with the distribution. In this way, the same application front-end source code can be compiled with [PyJamas](PyJamas) (into Javascript/AJAX) - with no modifications - to run with exactly the same back-end HTTP server that your PyjamasDesktop application uses. However, as you have access to the full Python core (unlike in Pyjamas, which is restricted to AJAX), you do not have to follow these guidelines.

PyjamasDesktop has been merged into Pyjamas, so obtaining PyjamasDesktop, is here:

- [PyPi Pyjamas](http://pypi.python.org/pypi/Pyjamas)

- [webkit issue 16401](https://bugs.webkit.org/show_bug.cgi?id=16401)

- [pywebkitgtk issue 13](http://code.google.com/p/pywebkitgtk/issues/detail?id=13)

Pre-built AMD64 .deb packages for the webkit-glib and pywebkitgtk dependencies are here:

- [Packages for pywebkitgtk-1.0 and libwebkit-1.0-2](http://sourceforge.net/project/showfiles.php?group_id=236659)

Note that pywebkitgtk patched (or pre-built) is only required for the webkit back-end option. If the XULrunner option is to be used, then install XULrunner with python-xpcom, and python-hulahop (on debian systems: apt-get install python-xpcom hulahop). If the MSHTML engine is used, then only the python \"comtypes\" package, for win32 is required ([http://sf.net/projects/comtypes](http://sf.net/projects/comtypes))

Documentation

The Pyjamas API, which is identical for both [PyJamas](PyJamas) and PyjamasDesktop, is available here:

- [API Documentation](http://pyjs.org/api/)

Article and information is available here:

- [advogato article](http://advogato.org/article/981.html)

- [http://pyjs.org](http://pyjs.org)

[CategoryPyGUI](CategoryPyGUI)
