# cppyy

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The [cppyy](http://cppyy.readthedocs.io) package provides fast, automatic, Python-C++ bindings, including run-time instantiation of C++ templates, cross-inheritance, callbacks, auto-casting, transparent use of smart pointers, etc., etc. Many C++ idioms are automatically recognized and \"pythonized\" (given a Python look-and-feel), allowing drop-in placement in Python idioms and integration with standard libraries such as [NumPy](NumPy) and ctypes. Most importantly it makes it possible to write higher-level (with ownership, threading, and application-specific rules) Python modules on top of C++ in pure Python, without the need to learn an intermediate language or language extension.

Cppyy works by integrating the Clang/LLVM-based [Cling C++ interpreter](https://github.com/vgvassilev/cling), providing interactive access to C/C++ from Python. It enables calling C++ from Python and calling Python from C++. Using precompiled modules, a class loader, and an everything-lazy implementation, cppyy is designed for automatic generation of Python bindings for large scale C++ programs. [PyPy](PyPy) supports cppyy natively for high performance, as described in this [PyHPC\'16](http://wlav.web.cern.ch/wlav/Cppyy_LavrijsenDutta_PyHPC16.pdf) paper.

An example session follows:

:::: 
::: 
``` 
   1 >>> import cppyy
   2 >>> cppyy.cppdef("""
   3 ... class MyClass {
   4 ... public:
   5 ...    MyClass(int i) : m_data(i) {}
   6 ...    virtual ~MyClass() {}
   7 ...    virtual int add_int(int i) { return m_data + i; }
   8 ...    int m_data;
   9 ... };""")                               # defines a new C++ class
  10 >>> from cppyy.gbl import MyClass        # bound on-the-fly
  11 >>> v = cppyy.gbl.std.vector[MyClass]()  # template generated
  12 >>> v += [MyClass(i) for i in range(2)]
  13 >>> len(v)
  14 2
  15 >>> for m in v:                          # idiomatically mapped
  16 ...    print(m.m_data)
  17 ...
  18 0
  19 1
  20 # create a C++ function on the fly and attach on the Python side
  21 >>> cppyy.cppdef("auto add_int = [](MyClass* m, int a) { return m->m_data + a; };")
  22 >>> MyClass.add_int = lambda self, i: cppyy.gbl.add_int(self, i)
  23 >>> for m in v:
  24 ...    print(m.add_int(1))
  25 ...
  26 1
  27 2
  28 # cross inheritence (CPython only for now)
  29 >>> class PyMyClass(MyClass):
  30 ...    def add_int(self, i):
  31 ...       return self.m_data + 2*i
  32 ...
  33 # helper on C++ side to show inheritence
  34 >>> cppyy.cppdef("int callback(MyClass* m, int i) { return m->add_int(i); }")
  35 >>> cppyy.gbl.callback(m, 2)             # calls C++ add_int
  36 3
  37 >>> cppyy.gbl.callback(PyMyClass(1), 2)  # calls Python-side override
  38 5
```
:::
::::

Source and wheels (for [ManyLinux](./ManyLinux.html), Mac, and Windows 32b and 64b) are available on PyPI. To install, run:

    $ python -m pip install cppyy

If you prefer conda, cpppy is also available from conda-forge for Linux and Mac:

    $ ﻿conda install -c conda-forge cppyy

Full details are in the cppyy documentation: [http://cppyy.readthedocs.io](http://cppyy.readthedocs.io)
