# WebBrowserProgramming

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Web Browser Programming in Python 

TODO: merge in and research these, found on comp.lang.python

Yes, Python can do it\... on Windows.

Two (examples) ways:

- [ActiveScripting](./ActiveScripting.html) ([PythonScript](./PythonScript.html)), included in [PyWin32](PyWin32)

- Gestalt (who mix Python, Ruby & [JavaScript](./JavaScript.html), via Silverlight)

TODO: Add mention of IPython Notebook which can be run remotely, easily on AWS, and used within your browser. The HTML client can also interact with [JavaScript](./JavaScript.html) and DOM, though this feature isn\'t quite merged yet. There\'s a lot being done on it, but it\'s already being used and probably should be mentioned here.

This topic covers ways in which python can be used in web browsers to control, create or manipulate the content within a user\'s web browser, or a web-based technology (such as [WebKit](http://webkit.org), the technology behind Safari, Midori, the OLPC Browser, Adobe AIR, Google Chrome and much more; XULrunner (the engine behind [Firefox](http://mozilla.com/firefox) and much more); MSHTML (the engine behind IE and [much more](http://en.wikipedia.org/wiki/Trident_(layout_engine)#Trident-based_applications)); and KDE\'s KHTMLPart.

To clarify what type of technology goes onto this page, some examples of types of technology that can and cannot be added to this section:

- Specifically excluded from the list is technology that simply generates static HTML content. So, an HTML pretty-printer library, as the resultant HTML simply uses the browser for \"display\" purposes rather than using the browser as an \"application execution environment\", is out. Such technologies can instead be found at [WebClientProgramming](WebClientProgramming).

- Plugins for Web Browsers that provide direct access to the DOM model of the web browser. In exactly the same way that most web browsers have [JavaScript](./JavaScript.html) by default as a language that can directly access the DOM model of the web browser, a plugin or other system that can do the same thing (with Python using `<script type="text/python" />`{.backtick} instead of [JavaScript](./JavaScript.html) using `<script language="javascript" />`{.backtick}) should be listed on this page.

- Python-based technology that auto-generates or compiles [JavaScript](./JavaScript.html) definitely counts, as the resultant [JavaScript](./JavaScript.html) would be executed by the web browser.

- Technology that simply *uses* [JavaScript](./JavaScript.html) or depends on [JavaScript](./JavaScript.html) libraries (such as mochikit, extjs or prototype) does not count, but a Python-based wrapper library around a [JavaScript](./JavaScript.html) engine definitely counts.

This latter example requires some further explanation: Pyjamas, for example, is a Python-to-[JavaScript](./JavaScript.html) compiler that can include inline [JavaScript](./JavaScript.html). So, although the input to Pyjamas is part Python, part [JavaScript](./JavaScript.html), the output is pure [JavaScript](./JavaScript.html) that runs in a web browser, and so any such \"mixed\" language libraries should be included on this page.

## Python-to-JavaScript Compilers 

These are tools that convert Python into [JavaScript](./JavaScript.html), that can then be run either stand-alone, using technology such as Spidermonkey, Google\'s V8 engine (for example, using [pyv8](http://code.google.com/p/pyv8)), or in a web browser (where, in order to be useful, the applications must of course interface with the DOM model of the browser, typically using an AJAX library).

The translation from Python to Javascript can be done by a Python program

- [Pyjaco](https://github.com/chrivers/pyjaco), the Python-to-Javascript Compiler is a python-based compiler that will compile most python code into fairly compact javascript. It uses a small (\~60KB) standard library to implement all the usual python types like list, dict, int, bool, etc. It supports classes, inheritance, keyword and variable arguments, and much more. It has a comprehensive test suite, and aims to be the most fun and efficient way to create web applications with Python.

- [Pyjamas](./Pyjamas.html) is a Python-to-[JavaScript](./JavaScript.html) compiler and AJAX-based Web Toolkit and Framework that allows users to write code in standard Python that will be run in a web browser, after translation to [JavaScript](./JavaScript.html). pyjs - the compiler - can also be used as a stand-alone [JavaScript](./JavaScript.html) compiler. There are three main modes: \--strict, providing as close to full strict python compatibility and interoperability as is both possible and has been contributed so far (which is quite a lot); -O, providing a subset of python functionality and providing much faster performance as a result; \--stupid-mode which falls back to javascript for certain operations, with the result that the output is much easier to read and to compare to the original python from which it was generated, but runs the risk of changing the meaning of the python application and requiring a deep understanding of how javascript operates (stupidly - hence the name of the mode).

- [Py2Js](Py2Js) is an unmaintained project that can still be downloaded [here](http://davidf.sjsoft.com/files/py2js). It is purely a Python-to-[JavaScript](./JavaScript.html) compiler/translator.

- [Py2js](http://mattpap.github.com/py2js/html/) is a maintained project that provides a Python-to-[JavaScript](./JavaScript.html) compiler.

- [PyCow](https://github.com/p2k/PyCow) is an unmaintained project to translate Python code to Javascript with Mootools

- [Fiddle Salad](http://fiddlesalad.com/python/) is a web development IDE with HTML and CSS that compiles Python to [JavaScript](./JavaScript.html)

- [Transcrypt](http://www.transcrypt.org) is a new tool, intended for professional use, to precompile Python 3.6 into compact, readable [JavaScript](./JavaScript.html). It allows for seamless integration with any [JavaScript](./JavaScript.html) library without gluecode or dataconversion. Compact downloads, kB\'s rather than MB\'s, runtine only 20kB. Load and execution speed the same as [JavaScript](./JavaScript.html). You can debug your application from the Python sourcecode, even it it\'s minified. Optional static typechecking and linting included. Possibility to embed JSX into the sourcecode for use with React. [Documentation](http://www.transcrypt.org/docs/html/index.html) with extensive examples using a diversity of [JavaScript](./JavaScript.html) libraries. Native [JavaScript](./JavaScript.html) code can be inserted anywhere in the Python source. Can be used in combination with Django or Bottle to have the same language on client and server side. Many [demo\'s](http://www.transcrypt.org/examples) are part of the distribution, including an iOS web app. Transcrypt can be pip-installed from [PyPi](./PyPi.html).

or by a Javascript program, with the Python code translated and run on the fly by the web browser

- [Skulpt](https://skulpt.org/) is a Python-to-[JavaScript](./JavaScript.html) compiler that is focussing on providing (only) full Python syntax. The demo includes a Python interpreter prompt, which is actually running in the user\'s web browser, not on a server, as pure [JavaScript](./JavaScript.html).

- [Brython](https://brython.info/index.html) is a Python 3 implementation that runs in a browser, providing \<script type=\"text/python\"\>\...\</script\>.

## Embedding Python inside Web Browsers 

This section describes projects where a Python interpreter itself has been embedded into the web browser. Instead of downloading the standard Python executable and libraries, these projects come with the CPython runtime and libraries pre-embedded (and, as such, are typically very large downloads).

- PyXPComExt has the full Python interpreter embedded. [PyXPCOMExt](http://pyxpcomext.mozdev.org/) is the interpreter as a XULRunner extension; [PyDOM](http://developer.mozilla.org/en/PyDOM) is a library that will almost certainly be needed, that allows you to manipulate the browser\'s DOM model using Python. The API is (almost) identical to that of [JavaScript](./JavaScript.html). Effectively, where browsers have built-in support for `lang="javascript"`{.backtick}, PyXPComExt adds `<script lang="python"> .... </script>`{.backtick} to Firefox.

- [AppCelerator](./AppCelerator.html)\'s [Titanium](http://www.appcelerator.com/platform/titanium-platform/) provides support for `<script type="text/python"> ... </script>`{.backtick}, using [IronPython](IronPython) and Silverlight.

- [Ironpython](http://ironpython.net/browser/) by itself also provides support for `<script type="text/python"> ... </script>`{.backtick}.

- [Firebreath](https://github.com/Nitrogenycs/firebreath-x) is an NPAPI plugin that extends access to the full features of DOM programming out to other programming languages, including python.

## Python Wrappers around Web \"Libraries\" and Browser Technology 

This section describes projects where you can (or have to) create your own web browser application in Python. It includes web browser \"engines\" that have Python interfaces to access, control and present web pages and web-relevant rich media content (such as Adobe Flash).

- [CefPython](http://code.google.com/p/cefpython/) provides python bindings for the Google Chrome browser by using [Chromium Embedded Framework](http://code.google.com/p/chromiumembedded/), a web browser control based on the Chromium project.

- [PythonWebKit](PythonWebKit) - [PythonWebKit](http://www.gnu.org/software/pythonwebkit) is a Python wrapper around [Webkit](http://webkit.org) that provides direct access to the DOM model. [PyWebKitGtk](./PyWebKitGtk.html) has been incorporated into the build, rather than being built separately. Unlike the patched version of [PyWebKitGtk](./PyWebKitGtk.html), [PythonWebKit](PythonWebKit) does not go via gobject to access DOM functions but instead calls the Webkit DOM functions direct.

- [PyWebKitGtk](./PyWebKitGtk.html) - [PyWebkitGtk](http://code.google.com/p/pywebkitgtk) is a Python wrapper around [Webkit](http://webkit.org) that embeds the Webkit \"engine\" as a GTK widget. The standard version of [PyWebKitGtk](./PyWebKitGtk.html) is unable to provide access to the DOM model, treating pywebkit as a hands-off widget that can be used to write your own Web Browser (see demobrowser.py). However, a [patch to webkit](https://bugs.webkit.org/show_bug.cgi?id=16401) and a corresponding patch to [PyWebKitGtk](./PyWebKitGtk.html) will soon bring DOM model manipulation to python: see [PyjamasDesktop](PyjamasDesktop) for details.

- [PyWebkitQt4](./PyWebkitQt4.html) is a python wrapper again around Webkit but this time as a Qt4 widget. An extremely limited subset of bindings to the DOM model have been added to [PyWebkitQt4](./PyWebkitQt4.html), along with the means to execute [JavaScript](./JavaScript.html) code snippets. Whilst in principle this sounds like a fantastic idea, in practice it is insane to work with, especially for event callbacks and for anything beyond the most absolute and basic DOM manipulation. [PyWebkitQt4](./PyWebkitQt4.html) is best avoided for significant DOM manipulation, or is best treated as nothing more than a means to display HTML (and other web-based media such as Flash and Java applications).

- PyKDE - KDE contains Python bindings to KHTMLPart (which is very similar to Webkit). This allows you to embed HTML into an application window. The Python bindings to the DOM model are slightly\... obtuse. to say the least, and PyKHTML - [PyKHTML](http://paul.giannaros.org/pykhtml/) makes them much more tolerable (see `dom.py`{.backtick}). However, there are limitations in PyKDE\'s DOM bindings (that many people will never encounter) that you should investigate thoroughly before utilising PyKDE for seriously heavy-duty DOM model manipulation. To avoid those limitations you should ensure that the entire KDE platform is compiled with C++ RTTI enabled (it is typically disabled by most distributions, by default).

- [WebKit](WebKit) with the Objective-C bindings (MacOS X users only). [Webkit](http://webkit.org) itself has Objective-C bindings, on MacOS X. MacOS X\'s Objective-C technology comes with automatic bindings to all major programming languages, including Python (using pyobjc). Consequently, you can directly manipulate the DOM model from Python. However, unlike the use of MSHTML, and unlike XULrunner and the patched version of [WebKit](WebKit), the Objective-C [WebKit](WebKit) bindings are limited to *just* the DOM model, and are limited to strict accordance with the W3C standards (rather than the de-facto standards defined by real-world [JavaScript](./JavaScript.html) usage). So, for example, `XMLHttpRequest`{.backtick} is not included in the Objective-C bindings (whereas it is in XULRunner); and the `embed`{.backtick} element takes width and height strictly as integers, rather than accepting `100px`{.backtick} and stripping off `px`{.backtick}.

- [HulaHop](http://wiki.laptop.org/go/HulaHop) provides Python access to DOM model manipulation - via XUL/Gecko Interfaces. [HulaHop](./HulaHop.html) is part of the OLPC Sugar Project, but is available stand-alone. It depends on python-xpcom (part of XULRunner). [HulaHop](./HulaHop.html) is being removed from Sugar and being replaced by [WebKit](WebKit).

- [PyWin32](PyWin32) comtypes can be used (with care!) to create an MSHTML IWebBrowser2 ActiveX window and thus provide access to the full DOM features of the MSHTML (Trident) engine. [PyjamasDesktop](PyjamasDesktop) uses this technique to create the [mshtml.py](http://pyjamas.svn.sourceforge.net/viewvc/pyjamas/trunk/pyjd/mshtml.py) port. Note that creation and use of `XMLHttpRequest`{.backtick} is also shown in [PyjamasDesktop](PyjamasDesktop)\'s `mshtml.py`{.backtick}.

- python-wxWebKit is beginning to provide Python access to DOM model manipulation - via python bindings that are auto-generated using SWIG. The goal of the project is to provide full access to the entire DOM model, and this goal is, as of May 2011, approximately 25% completed.

## Python Wrappers around Web Browser \"Test Suite\" Libraries 

This section describes projects where you can test web applications, initiated from the command-line with python bindings.

- [Selenium](http://seleniumhq.org), the browser test suite, has python bindings: [Install HOWTO](http://seleniumhq.org/docs/appendix_installing_python_driver_client.html). Selenium is a suite of tools to automate web app testing across many platforms.

- [Windmill](http://getwindmill.com) is a web testing tool designed to let you painlessly automate and debug your web application. Like selenium, it also has Python bindings.
