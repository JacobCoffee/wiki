# CodingProjectIdeas/PythonCore

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Python language / CPython interpreter ideas 

- Security audit of python. Using as many automated processes as possible.

- Clean up the porting ifdefs, including os and posixmodule

- Python speed up. Reduce memory usage, speedup startup time. The two main speed regressions of the 2.0, 2.1,2.2,2.3,2.4 releases. (438,453,499,771,880) syscalls vs 106 for latest perl. 0m0.031s, 0m0.029s, 0m0.037s, 0m0.059s, 0m0.057s real time to start vs 0m0.007s for the latest perl.

- Add a [MemoryUsageProfiler](MemoryUsageProfiler) to python. Currently it is almost impossible to figure out where memory is going in a large python program, especially if you have C extensions loaded. It\'d be nice to know where the memory is going, if there are circular references, or if objects are being held too long. See the [bcannon-sandboxing](http://svn.python.org/view/python/branches/bcannon-sandboxing/) branch in svn for an attempt at a proof-of-concept. There have been several attempts with varying success: [http://guppy-pe.sourceforge.net/](http://guppy-pe.sourceforge.net/) and [http://pysizer.8325.org/](http://pysizer.8325.org/)

- math speedups or IO speedups (I think the string-in-base-10 to an int was recently sped up, but there may be other similar locations)

- [SpeedUpInterpreterStartup](SpeedUpInterpreterStartup)

- [../PythonGarbageCollected](PythonGarbageCollected)

- [../RegisterVirtualMachine](RegisterVirtualMachine)

- Add regular code-coverage (both C and Python) to the build system (maybe even to Buildbot?)
  - Better introspection support for C functions: ability to expose arguments through inspect. Might require retrofitting existing extensions.

  - See [http://coverage.livinglogic.de/](http://coverage.livinglogic.de/)

- Provide more and better debugging of reference counting, garbage collection, and other memory issues for extension and embedding authors.

- Write tools that leverage the new compiler AST\-- tools to analyze code, walk the AST, modify it, allow a modified AST to be compiled back to bytecode. Work on PEP 267.
  - Re-implement the peephole optimizer to use the AST. (See [this](http://svn.python.org/projects/python/branches/tlee-ast-optimize/) branch)

- Create a practical statistical profiler designed for inclusion in core Python. (You might want to take a look at Andy Wingo\'s [statprof](http://wingolog.org/archives/2005/10/) profiler as a starting point. \-- [SkipMontanaro](SkipMontanaro)) Also/alternatively, create a thread-aware profiler \-- none of the current profilers are useful with multi threaded code.

- The development of the new [NumPy](http://numeric.scipy.org/) has led to good ideas for how to get a generic multidimensional array object into Python 2.6. Somebody willing to work with the NumPy developers to take the essential portions of NumPy and create a basearray (also called a dimarray) that could be included as a base-class multidimensional array object along with a general-purpose data-type object. This project has already been started but needs someone with time to help it along. See the [Array Interface](http://numpy.scipy.org/array_interface.shtml) description page for an SVN check-out. This project has large impact potential for Python.

- Improve Python threading performance, maybe remove [GlobalInterpreterLock](GlobalInterpreterLock) (GIL). (Note that the chance of getting a remove-the-GIL patch into core Python is near zero.) Reducing memory usage, and other resource usage will give a nice speedup.

- Improve cross-compiling support of Python interpreter.

- Deprecate .pyo files and come up with a way of specifying what optimizations have taken place within the bytecode. Would work well with also implementing a way to have user-defined optimizations take place at .pyc creation time.

- Auto-generate code (as much as is reasonably possible) to go from Python\'s parse tree to the AST (essentially generate a large chunk of [ast.c](http://svn.python.org/view/python/trunk/Python/ast.c).

- Bootstrap the pure Python implementation of import (found [here](http://svn.python.org/view/sandbox/trunk/import_in_py/), but a newer version lives [here](http://svn.python.org/view/python/branches/py3k/Lib/importlib/)) so that it can be used as the actual import mechanism instead of the C implementation.

- Try to speed up access to the built-in namespace. Various proposals in the past have come up about how to deal with shadowing of built-ins (including a new keyword).
