# Python Implementations

Python the language and Python the program are not the same thing. Several independent implementations exist, each targeting different runtimes or optimizing for different use cases. This section covers those implementations, plus tools for extending Python with C/C++ code or embedding Python inside other applications.

## Overview

- [PythonImplementations](PythonImplementations) — the comprehensive catalog of Python implementations, from CPython variants to entirely separate runtimes

## CPython

- [CPython](CPython) — the reference implementation, written in C, and what most people mean when they say "Python"
- [CPythonInterpreterInitialization](CPythonInterpreterInitialization) — how the CPython interpreter starts up internally
- [CPythonVmInternals](CPythonVmInternals) — a look inside the CPython virtual machine

## Alternative Implementations

- [PyPy](PyPy) — a Python implementation written in Python, featuring a JIT compiler and multiple backends
- [PyPyDonations](PyPyDonations) — donation tracking for the PyPy project
- [PyPySprint](PyPySprint) — sprint events focused on PyPy development
- [IronPython](IronPython) — Python for .NET and Mono, originally created by Jim Hugunin
- [BooLanguage](BooLanguage) — Boo, a Python-inspired language for the .NET CLI

## Embedding & Extending

- [Embedding and Extending](Embedding%20and%20Extending) — overview of embedding Python in other applications and writing C extensions
- [EmbeddingPythonTutorial](EmbeddingPythonTutorial) — step-by-step tutorial for embedding the Python interpreter
- [ExtensionTutorial](ExtensionTutorial) — tutorial for writing C extension modules
- [boost.python](boost.python) — Boost.Python, a C++ library for seamless interop between C++ and Python
- [Pyrex](Pyrex) — Pyrex, a language for writing Python extension modules (predecessor to Cython)
- [PyrexOnWindows](PyrexOnWindows) — getting Pyrex working on Windows
- [ctypes](ctypes) — the ctypes foreign function library for calling C code from Python

## Other Projects

- [BitPim](BitPim) — BitPim, a phone data management tool built with Python
- [Dabo](Dabo) — Dabo, a desktop application framework built on wxPython

```{toctree}
:hidden:
:maxdepth: 1

boost.python/index
BitPim
BooLanguage
CPython
CPythonInterpreterInitialization
CPythonVmInternals
Dabo
Embedding and Extending
EmbeddingPythonTutorial
ExtensionTutorial
IronPython
PyPy
PyPyDonations
PyPySprint
Pyrex
PyrexOnWindows
PythonImplementations
boost.python
ctypes
```
