# PythonImplementations

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python Implementations 

An \"implementation\" of Python should be taken to mean a program or environment which provides support for the execution of programs written in the Python language, as represented by the [CPython](CPython) reference implementation.

There have been and are several distinct software packages providing what we all recognize as Python, although some of those are more like distributions or variants of some existing implementation than a completely new implementation of the language.

## CPython Variants 

These are implementations based on the [CPython](CPython) runtime core (the de-facto reference Python implementation), but with extended behaviour or features in some aspects.

- [CrossTwine Linker](http://crosstwine.com/linker/python.html) - a combination of CPython and an add-on library offering improved performance (currently proprietary)

- [Stackless Python](StacklessPython) - CPython with an emphasis on concurrency using tasklets and channels (used by [dspython](https://www.develer.com/trac/dspython/) for the Nintendo DS)

- [Pyston](https://github.com/pyston/pyston) - a fork of CPython, originally developed at Dropbox but now by independent developers, performance-focused including bytecode quickening and a lightweight JIT.

- [Cinder](https://github.com/facebookincubator/cinder), a fork of CPython by Instagram, containing a number of optimizations like bytecode rewriting and a method-at-a-time JIT compiler.

- [Pyjion](https://github.com/tonybaloney/Pyjion), a JIT extension for CPython that compiles Python code to CIL (.NET) and executes it on the CLR.

- [unladen-swallow](http://code.google.com/p/unladen-swallow/) - \"an optimization branch of CPython, intended to be fully compatible and significantly faster\", originally considered for merging with CPython subject to [PEP 3146](http://www.python.org/dev/peps/pep-3146 "PEP"), but now unmaintained

- [S6](https://github.com/deepmind/s6), a JIT extension for CPython that also contains its own bytecode interpreter

- [wpython](http://code.google.com/p/wpython/) - a re-implementation of CPython using \"wordcode\" instead of bytecode

- [eGenix PyRun](http://www.egenix.com/products/python/PyRun/) - Python runtime (CPython + std library) compressed into a single 3-4MB binary

- [x-python](http://github.com/rocky/x-python/) - The C Python Interpreter written in Python; useful for educational purposes. There is also bytecode debugger for it

- [Falcon](https://github.com/rjpower/falcon) - a Python register machine shipped as an extension module

- [RegCPython](https://github.com/zq1997/RegCPython) - a fork of CPython with a register-based bytecode interpreter

### Reduced Python Variants 

These provide a subset of the full language + standard library, for use in embedded scenarios (see also the [EmbeddedPython](EmbeddedPython) topic)

- [MicroPython](https://micropython.org/) - Python for microcontrollers (runs on the pyboard and the BBC Microbit)

- [CircuitPython](https://circuitpython.org/) - Adafruit's branch of [MicroPython](./MicroPython.html)

Also look at the sections on Python compilers and extensions below, some of which would qualify as CPython variants.

## Other Implementations 

These are re-implementations of the Python language that do not depend on (or necessarily interact with) the [CPython](CPython) runtime core. Many of them reuse (a large part of) the standard library implementation.

Note that most of these projects have not yet achieved language compliance. However, many of these have goals and features or run in certain environments that make them interesting in their own regard. The only implementations that are known to be compatible with a given version of the language are [IronPython](IronPython), [Jython](Jython) and [PyPy](PyPy).

### Working Implementations 

The following implementations may be not comprehensive or even complete, but at the very least can be said to be working in that you can run typical programs with them already:

- [PyPy](https://pypy.org) - Python in Python, includes a tracing JIT compiler

- [Jython](Jython) - Python in Java for the Java platform

- [IronPython](IronPython) - Python in C# for the Common Language Runtime (CLR/.NET) and the [FePy](http://fepy.sourceforge.net/) project\'s [IronPython](IronPython) Community Edition (IPCE)

- [GraalPython](https://github.com/oracle/graalpython) - Python in Java, using the Graal just-in-time compiler and the Truffle interpreter implementation framework

- [Skybison](https://github.com/tekknolagi/skybison) - A C++ from scratch implementation of Python 3.8 using a moving GC, hidden classes and a template JIT.

- [Brython](http://www.brython.info/) - a way to run Python in the browser through translation to [JavaScript](./JavaScript.html)

- [CLPython](CLPython) - Python in Common Lisp

- [HotPy](http://www.dcs.gla.ac.uk/~marks/) - a virtual machine for Python supporting bytecode optimisation and translation (to native code) using type information gathered at runtime

- [pyjs](http://pyjs.org/) - (formally Pyjamas) a Python to [JavaScript](./JavaScript.html) compiler plus Web/GUI framework

- [PyMite](PyMite) - Python for embedded devices

- [pyvm](http://students.ceid.upatras.gr/~sxanth/pyvm-2.0/) - a Python-related virtual machine and software suite providing a nearly self-contained \"userspace\" system

- [RapydScript](https://github.com/atsepkov/RapydScript) - a Python-like language that compiles to [JavaScript](./JavaScript.html)

- [SNAPpy](http://www.synapse-wireless.com/documents/whte_paper/SNAP_WP_102108.pdf) - \"a subset of the Python language that has been optimized for use in low-power embedded devices\" (apparently proprietary)

- [tinypy](http://www.tinypy.org/) - a minimalist implementation of Python in 64K of code

- [Transcrypt](http://www.transcrypt.org/) - Python 3.6 to [JavaScript](./JavaScript.html) precompiler with lean and fast generated code, sourcemaps, built-in minification, optional static type-checking, JSX support

### Tentative Implementations 

The following implementations are apparent works in progress; they may not be able to run typical programs:

- [Berp](http://wiki.github.com/bjpop/berp/) - an implementation of Python 3 in Haskell, providing an interactive environment as well as a compiler

- [phpython](http://sourceforge.net/projects/phpython/) - a Python interpreter written in PHP

- [Pyjaco](http://pyjaco.org/) - a Python to [JavaScript](./JavaScript.html) compiler similar to Pyjs but more lightweight

- [Pystacho](http://code.google.com/p/pystachio/) is, like Skulpt, Python in [JavaScript](./JavaScript.html)

- [https://web.archive.org/web/20041206021225if\_/http://www.twistedmatrix.com/users/z3p/files/pyvm2.py](https://web.archive.org/web/20041206021225if_/http://www.twistedmatrix.com/users/z3p/files/pyvm2.py) - a CPython 2 bytecode interpreter written in Python 2, abandoned [mentioned on the PyPy mailing list in 2003](http://mail.python.org/pipermail/pypy-dev/2003-January/000048.html)

- [Skulpt](http://www.skulpt.org/) - Python in [JavaScript](./JavaScript.html)

- [Typhon](https://github.com/vic/typhon) - a [Rubinius](http://rubini.us/)-based implementation of Python

- [Violet](https://github.com/LiarPrincess/Violet) - a Swift implementation of Python

- [RustPython](https://rustpython.github.io/) - [RustPython](./RustPython.html) is a Python interpreter written in Rust. Aims at compatibility with Python 3.11+.

- [pocketpy](https://github.com/blueloveTH/pocketpy) - pocketpy is a lightweight (\~10000 LOC) Python interpreter for game scripting

## Extensions 

These are typically part of CPython (or some other implementation) but change the implementation\'s behaviour:

- [Psyco](http://psyco.sf.net) - a just-in-time specialising compiler for CPython, abandoned, works only for CPython 2.6.

## Compilers 

These compilers usually implement something close to Python, although some compilers may impose restrictions that alter the nature of the language:

- [Cython](http://cython.org/) - a widely used optimising Python-to-C compiler, CPython extension module generator, and wrapper language for binding external libraries. Interacts with CPython runtime and supports embedding CPython in stand-alone binaries.

- [Nuitka](http://nuitka.net/) - a Python-to-C++ compiler using libpython at runtime, attempting some compile-time and run-time optimisations. Interacts with CPython runtime.

- [MyPyC](https://github.com/mypyc/mypyc) compiles fully typed Python code to a C extension, based on mypy.

- [2c-python](http://code.google.com/p/2c-python/) - a static Python-to-C compiler, apparently translating CPython bytecode to C

- [Compyler](http://www.grant-olson.net/python/compyler) - an attempt to \"transliterate the bytecode into x86 assembly\" (now abandoned)

- [GCC Python Front-End](http://gcc.gnu.org/wiki/PythonFrontEnd) - an in-progress effort to compile Python code within the GCC infrastructure

- [Pyc](http://sourceforge.net/projects/pyc/) - performs static analysis in order to compile Python programs, uses similar techniques to Shed Skin

- [Shed Skin](http://code.google.com/p/shedskin/) - a Python-to-C++ compiler, restricted to an implicitly statically typed subset of the language for which it can automatically infer efficient types through whole-program analysis

- [unPython](http://code.google.com/p/unpython/) - a Python to C compiler using type annotations

- [VOC](https://pybee.org/project/projects/bridges/voc/) - A transpiler that converts Python bytecode into Java bytecode.

## Numerical Accelerators 

- [Numba](http://numba.pydata.org) - [NumPy](NumPy)-aware optimizing runtime compiler for Python

- [Pythran](https://pythran.readthedocs.io/en/latest/) - ahead of time compiler for a subset of Python with a focus on scientific computing

- [Copperhead](http://copperhead.github.com/) - purely functional data-parallel Python, compiles to multi-core and GPU backends

- [Parakeet](http://https://github.com/iskandr/parakeet) - runtime compiler for a numerical subset of Python

## Similar but Distinct Languages 

These languages don\'t attempt to be directly compatible even with a subset of Python, choosing to provide their own set of features:

- [Alore](http://www.alorelang.org/) - a compilable language with optional typing and Python/Ruby inspired syntax; an Alore-Python bridge is planned; development effort has been transferred to mypy (see below)

- [Cobra](Cobra)

- [Converge](http://convergepl.org/) - inspired by Python, Haskell, Icon and Smalltalk, provides macros which can be evaluated at compile-time

- [Delight](http://delight.sourceforge.net/) - based on the D programming language

- [Genie](http://live.gnome.org/Genie) - based on the same foundations (Gtk+, GNOME) as the Vala programming language, supposedly inspired by Boo

- [mypy](http://www.mypy-lang.org/) - Python with optional static typing and some local type inference

- [Mython](http://mython.org/) - an extensible variant of the Python programming language, apparently a front-end for CPython

- [Nim](http://nim-lang.org/) - statically typed, compiles to C, C++, and JS, features parameterised types, macros, and so on

- [Pythonect](http://www.pythonect.org/) - a dataflow-oriented language adopting the basic Python expression syntax, implemented in Python and integrated with the Python environment

- [Roket Secured Language](http://code.google.com/p/rsl-interpreter/) - an interpreter for a Python-like language for applications where \"restricted Python\" execution is desired

- [Serpent](http://serpent.sourceforge.net/) - inspired by Python, supporting real-time garbage collection and multiple virtual machines in separate threads [(more information)](https://www.cs.cmu.edu/~music/aura/serpent-info.htm)

- [Serpentine](https://gitlab.com/dboddie/DUCK/-/blob/master/Documents/Introduction_to_Serpentine.md) - a language with Python-like syntax for the Dalvik virtual machine

- [sneklang](https://sneklang.org/) - \"Snek is a tiny embeddable language targeting processors with only a few kB of flash and ram.\"

- [Starlark](https://github.com/bazelbuild/starlark/tree/master) - \"Starlark (formerly known as Skylark) is a language intended for use as a configuration language.\"

- [Wirbel](http://mathias-kettner.de/wirbel.html) - a compilable language with similar restrictions to Shed Skin (statically typed names, lists cannot mix elements of different types), no longer actively developed as of 2011-07-21

Comparisons:

- Comparisons of [Genie and Wirbel](http://jamiemcc.livejournal.com/12009.html?thread=225769#t225769) and [Genie and Python](http://bkhome.org/genie/) by the lead developer of the Puppy Linux distribution

- Some [Genie code samples](http://code.valaide.org/category/tags/genie) indicating the differences between that language and other Python variants

## Topic Guides 

- [EmbeddedPython](EmbeddedPython)

- [PythonDistributions](PythonDistributions)

## (Fun) Python Preprocessors 

There are even some tongue-in-cheek dialects of Python which you might find fun.

- [Like, Python](http://www.staringispolite.com/likepython/)

- [LOLPython](http://www.dalkescientific.com/writings/diary/archive/2007/06/01/lolpython.html)

## Academic Projects 

Python implementations and compilers have been the topic of various papers and theses. Those that have not apparently been developed further are listed here:

- [QGen : A Python to Qt/C++ translator](http://urn.nb.no/URN:NBN:no-10110) - a simple translator described in a master\'s thesis from 2004

- [Starkiller](http://mike.salib.com/writings/thesis/) - a Python to C++ translator described, along with a review of contemporary tools, in a master\'s thesis from 2004 ([author\'s site](http://mike.salib.com/))

------------------------------------------------------------------------

This page aims to replace one formerly maintained as \"[Cameron Laird\'s personal notes on varieties of Python implementation](http://phaseit.net/claird/comp.lang.python/python_varieties.html)\". Also of interest will be [IntegratingPythonWithOtherLanguages](IntegratingPythonWithOtherLanguages), which, among other variants, mentions *embeddings* of Python in other languages.

------------------------------------------------------------------------

[CategoryImplementations](CategoryImplementations)
