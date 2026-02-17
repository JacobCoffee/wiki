# IntegratingPythonWithOtherLanguages

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

\[Hint: The idea is to create pages for the stuff, not just link it.\]

# C/C++ 

There a various tools which make it easier to bridge the gap between Python and C/C++:

- [Pyrex](Pyrex) - write your extension module on Python ![(!)](/wiki/europython/img/idea.png "(!)")

- [Cython](http://cython.org/) \-- Cython \-- an improved version of Pyrex

- [CXX](http://cxx.sourceforge.net/) - PyCXX - helper lib for writing Python extensions in C++

- [ctypes](http://starship.python.net/crew/theller/ctypes/) is a Python module allowing to create and manipulate C data types in Python. These can then be passed to C-functions loaded from dynamic link libraries.

- [elmer](elmer) - compile and run python code from C, as if it was written in C

- [PicklingTools](http://www.picklingtools.com/) is a collection of libraries for exchanging Python Dictionaries between C++ and Python.

- [weave](weave) - include C code lines in Python program (deprecated in favor of Cython)

- [ackward](https://code.google.com/p/ackward/) exposes parts of Python\'s standard library as idiomatic C++

- [CFFI](http://cffi.readthedocs.org/) - interact with almost any C code from Python, based on C-like declarations that you can often copy-paste from header files or documentation.

### 0.1. C/C++ Binding Generators 

Tools to make C/C++ functions/methods accessible from Python by generating binding (Python extension or module) from header files.

- [boost.python](./boost(2e)python.html) - Expose C++ classes functions and objects to Python, and vice-versa, using just C++ compiler

- [PyAutoC](https://github.com/orangeduck/PyAutoC) - Automatically wrap C functions and structs, using just C compiler.

- [pwig](http://pwig.sourceforge.net/) is a SWIG extension for writing new language modules in Python.

- [PyBindGen](https://github.com/gjcarneiro/pybindgen) Python bindings code generator for pure C or C++ APIs. The generator is written in Python and has low complexity. The generated code is lean, efficient, and highly readable

- [shiboken](https://pyside.github.io/docs/shiboken/) - Binding Generator used to create [PySide](PySide) Python bindings for Qt

- [SIP](SIP) - similar to SWIG but specialised for Python and C++. Used to create [PyQt](PyQt), the [Qt](./Qt.html) API wrapper library

- [SWIG](http://www.swig.org/) - generate extension module from your .h files

- [pybind11](https://github.com/wjakob/pybind11) - Similar to Boost.Python, but with a lean header-only implementation for C++11-capable compilers.

- [pyclif](https://github.com/google/clif) - Google tool. Similar to SWIG, but user-friendly and targeted only C++11 well-written libs.

- [cppyy](cppyy) - Fast, automatic, Python-C++ bindings, including run-time template instantiations, cross-inheritance, auto-casting, etc.

- [Scapix Language Bridge](https://www.scapix.com/) - generates Python (and other languages) bindings directly from C++ headers.

------------------------------------------------------------------------

**Articles**

- Using Python as glue [SciPy Documentation](https://docs.scipy.org/doc/numpy/user/c-info.python-as-glue.html)

- Building Hybrid Systems with Boost.Python in [C/C++ User Journal](http://www.boost.org/doc/libs/develop/libs/python/doc/html/article.html) (2003)

- Integrating Python, C and C++, presented at the ACCU conference by Duncan Booth (2003)

- Embedding Python in Multi-Threaded C/C++ Applications in [LinuxJournal](http://www.linuxjournal.com/article.php?sid=3641) (2000)

------------------------------------------------------------------------

**Related**

- [AppsWithPythonScripting](AppsWithPythonScripting)

# Delphi 

- [Python4Delphi](Python4Delphi) - Python for Delphi is a set of free components that wrap up the Python Dll into Delphi. ([https://github.com/pyscripter/python4delphi](https://github.com/pyscripter/python4delphi))

# Fortran 

- [F2PY](F2PY) - Fortran to Python Interface Generator ([http://cens.ioc.ee/projects/f2py2e/](http://cens.ioc.ee/projects/f2py2e/))

- [PyFort](./PyFort.html) - The Python-Fortran connection tool ([http://pyfortran.sourceforge.net/](http://pyfortran.sourceforge.net/))

# Lisp 

- [CLPython](CLPython) - Python implemented in Common Lisp

- [Lython (archived page)](http://web.archive.org/web/20050207230521/http://www.caddr.com/code/lython/) - Lisp front-end for Python

- [Pymacs](http://pymacs.progiciels-bpi.ca/) - integration of Python with Emacs Lisp

# Prolog 

- [PyLog](PyLog) (actually two *different* products)

- [prolog](http://agave.ahsc.arizona.edu/~schcats/projects/) a simple interface to [SWI-Prolog](http://www.swi-prolog.org/)

- bedevere - Python wrapper to GNU Prolog [http://bedevere.sourceforge.net/](http://bedevere.sourceforge.net/)

- [pwig](http://pwig.sourceforge.net/) includes examples of wrapping Python for SWI-Prolog.

- [pyswip](http://code.google.com/p/pyswip/) is a ctypes based module that enables querying SWI-Prolog.

See also [http://www.google.com/search?hl=en&lr=&ie=ISO-8859-1&q=Python+prolog](http://www.google.com/search?hl=en&lr=&ie=ISO-8859-1&q=Python+prolog)

# Java 

- [Jython](Jython) - Python implemented in Java

- [JPype](JPype) - Allows Python to run java commands

- [Jepp](Jepp) - Java embedded Python

- [JCC](http://pypi.python.org/pypi/JCC/2.12) - a C++ code generator for calling Java from C++/Python

- [Javabridge](http://pypi.python.org/pypi/javabridge) - a package for running and interacting with the JVM from CPython

- [py4j](https://www.py4j.org/index.html) - Allows Python to run java commands.

- [voc](http://pybee.org/voc/) - Part of [BeeWare](./BeeWare.html) suite. Converts python code to Java bytecode.

- [p2j](https://github.com/chrishumphreys/p2j) - Converts Python code to Java. No longer developed.

# C#/.NET 

- [ActiveState](https://www.activestate.com/company/press/press-releases/activestate-supports-microsoft-net-framework/) supports Python .NET.

- [Python for .NET](https://pythonnet.github.io) is a near-seamless integration of the CPython runtime with the .NET Common Language Runtime (CLR).

- [IronPython](https://ironpython.net) is an implementation of Python for .net, which allows you to import .net class libraries seamlessly in Python.

# Perl 

See [http://www.faqts.com/knowledge_base/view.phtml/aid/17202/fid/1102](http://www.faqts.com/knowledge_base/view.phtml/aid/17202/fid/1102)

- [PyPerl](PyPerl) [http://search.cpan.org/dist/pyperl/](http://search.cpan.org/dist/pyperl/)

- [Inline::Python](http://search.cpan.org/search?query=Inline::Python&mode=all)

- [PyPerlish](PyPerlish) - Perl idioms in Python

For converting/porting Perl code to Python the tool \'Bridgekeeper\' [http://www.crazy-compilers.com/bridgekeeper/](http://www.crazy-compilers.com/bridgekeeper/) may be handy.

# PHP 

- PiP (Python in PHP) [http://www.csh.rit.edu/\~jon/projects/pip/](http://www.csh.rit.edu/~jon/projects/pip/)

- PHP \"Serialize\" in Python [http://hurring.com/scott/code/python/serialize/](http://hurring.com/scott/code/python/serialize/) (broken link; see the [Web Archive Wayback Machine](http://web.archive.org/web/20110807032037/http://hurring.com/scott/code/python/serialize/) for the latest working version)

# R 

- RPy [http://rpy.sourceforge.net](http://rpy.sourceforge.net/)

- RSPython [http://www.omegahat.net/RSPython](http://www.omegahat.net/RSPython)

# Objective-C 

- [http://pyobjc.sourceforge.net/](http://pyobjc.sourceforge.net/)

# Tcl 

- [elmer](elmer) - compile and run python code from Tcl, as if it was written in Tcl

- [TclPython](https://github.com/amykyta3/tclpython) - A package for Tcl that allows you to pass strings of Python code from a Tcl environment to a Python (Python 2.x or 3.x) interpreter.

- [Tcl and other languages](http://wiki.tcl.tk/1324) - Tcl\'s equivalent of this page.

# Lua 

- [LunaticPython](http://labix.org/lunatic-python) - a two-way bridge between Python and Lua.

- [Lupa](http://pypi.python.org/pypi/lupa) - fast wrapper for LuaJIT2 written in Cython.

- [Lux](http://www.equi4.com/lux/) - a mutant Lua emphasizing interoperation with Python, Perl, etc.

# OCaml 

- [Pycaml](http://pycaml.sourceforge.net/) - write Python extension modules in OCaml (instead of C), and use Python code and native libraries from OCaml programs.

# Eiffel and Haskell 

- Eiffel/Haskell [http://epolyglot.sourceforge.net/](http://epolyglot.sourceforge.net/) (last updated 2001)

- [PythonVsHaskell](PythonVsHaskell) has a section \"Using both Python & Haskell with ctypes\".

# Other (applications) 

- [LotusNotes](./LotusNotes.html) [http://www.dominopower.com/issuesprint/issue200008/command.html](http://www.dominopower.com/issuesprint/issue200008/command.html)

- [PostgreSQL](PostgreSQL) [http://www.linuxgazette.com/issue80/nielsen.html](http://www.linuxgazette.com/issue80/nielsen.html)

- [RenderMan](RenderMan) [http://www.lysator.liu.se/\~ture/terry.html](http://www.lysator.liu.se/~ture/terry.html)

- [CorbaPython](CorbaPython): for a generic solution to language integration

to name a few. There are much [more\...](http://www.google.com/search?q=Python+binding&hl=en)

# Other (standards and protocols) 

- XMLRPC and SOAP

- Yaml: [http://www.yaml.org](http://www.yaml.org/)

# See also 

Thinki: [UsingPythonWithOtherLanguages](http://web.archive.org/web/20071108024137/http://www.thinkware.se/cgi-bin/thinki.cgi/UsingPythonWithOtherLanguages)
