# EmPy

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# EmPy 

## Introduction: Welcome to EmPy! 

[EmPy](http://www.alcyone.com/software/empy/) is a powerful, robust and mature [templating](../archive/Templating) system for inserting Python code in template text. EmPy takes a source document, processes it, and produces output. This is accomplished via expansions, which are signals to the EmPy system where to act and are indicated with markup. Markup is set off by a customizable prefix (by default the at sign, `@`{.backtick}). EmPy can expand arbitrary Python expressions, statements and control structures in this way, as well as a variety of additional special forms. The remaining textual data is sent to the output, allowing Python to be used in effect as a markup language.

EmPy also supports hooks, which can intercept and modify the behavior of a running interpreter; diversions, which allow recording and playback; filters, which can alter output and can be chained together. The system is highly configurable via command line options, configuration files, and environment variables. EmPy documents can also be imported as modules, and an extensive API is also available for embedding EmPy functionality in your own Python programs.

EmPy also has a supplemental library for additional non-essential features (`emlib`{.backtick}), a documentation building library used to create this documentation (`emdoc`{.backtick}), and an extensive help system (`emhelp`{.backtick}) which can be queried from the command line with the main executable `em.py`{.backtick} (`-h/--help`{.backtick}, `-H/--topics=TOPICS`{.backtick}). The base EmPy interpreter can function with only the `em.py`{.backtick}/`em`{.backtick} file/module available.

EmPy can be used in a variety of roles, including as a templating system, a text processing system (preprocessing and/or postprocessing), a simple macro processor, a frontend for a content management system, annotating documents, for literate programming, as a souped-up text encoding converter, a text beautifier (with macros and filters), and many other purposes.

## Markup overview 

Expressions are embedded in text with the `@(...)`{.backtick} notation; variations include conditional expressions with `@(...?...!...)`{.backtick} and the ability to handle thrown exceptions with `@(...$...)`{.backtick}. As a shortcut, simple variables and expressions can be abbreviated as `@variable`{.backtick}, `@object.attribute`{.backtick}, `@sequence[index]`{.backtick}, `@function(arguments...)`{.backtick}, and combinations. Functions can be called with expanded markup as arguments using `@function{markup}`{.backtick}. Full-fledged statements are embedded with `@`{.backtick}. Control flow in terms of conditional or repeated expansion is available with `@[...]`{.backtick}. A `@`{.backtick} followed by any whitespace character (including a newline) expands to nothing, allowing string concatenations and line continuations. Line comments are indicated with `@#...`{.backtick} including the trailing newline. `@*...*`{.backtick} allows inline comments. Output can be disabled and re-enabled with `@-...`{.backtick} and `@+...`{.backtick}, including the trailing newlines. Escapes are indicated with `@\...`{.backtick}; diacritics with `@^...`{.backtick}; icons with `@|...`{.backtick}; and emoji with `@:...:`{.backtick}. `@%...`{.backtick}, `@%!...`{.backtick}, `@%%...%%`{.backtick} and `@%%!...%%`{.backtick} indicate \"significators,\" which are distinctive forms of variable assignment intended to specify document metadata in a format easy to parse externally. In-place expressions are specified with `@$...$...$`{.backtick}. Context name and line number changes can be made with `@?...`{.backtick} and `@!...`{.backtick}, respectively. A set of markups (`@((...))`{.backtick}, `@[[...]]`{.backtick}, `@{}`{.backtick}, `@<...>`{.backtick}) are customizable by the user and can be used for any desired purpose. @`...`{.backtick} allows literal escaping of any EmPy markup. Output can be toggled on and off with `@+`{.backtick} and `@-`{.backtick}, respectively. And finally, a `@@`{.backtick} sequence (the prefix repeated once) expands to a single literal at sign.

The prefix defaults to `@`{.backtick} but can be changed with the command line option `-p/--prefix=CHAR`{.backtick} (*environment variable:* `EMPY_PREFIX`{.backtick}, *configuration variable:* `prefix`{.backtick}).

## Getting the software 

The official URL for the Web site is [http://www.alcyone.com/software/empy/](http://www.alcyone.com/software/empy/).

The latest version of the software is available in a tarball here: [http://www.alcyone.com/software/empy/empy-latest.tar.gz](http://www.alcyone.com/software/empy/empy-latest.tar.gz).

The software can be installed through PIP via this shell command:

`% python3 -m pip install empy`{.backtick}

For information about upgrading from 3.*x* to 4.*x*, see [http://www.alcyone.com/software/empy/ANNOUNCE.html#changes](http://www.alcyone.com/software/empy/ANNOUNCE.html#changes).

EmPy works with any modern version of Python. Python version 3.*x* is expected to be the default and all source file references to the Python interpreter (*e.g.*, the bangpath of the .py scripts) use `python3`{.backtick}. EmPy also has legacy support for versions of Python going back all the way to 2.4, with special emphasis on 2.7 regardless of its end-of-life status. It has no dependency requirements on any third-party modules and can run directly off of a stock Python interpreter.

EmPy will run on any operating system with a full-featured Python interpreter; this includes, but is probably not limited to, the operating systems Linux, Windows and macOS (Darwin). Using EmPy requires knowledge of the [Python language](https://www.python.org/).

EmPy is compatible with many different Python implementations, interpreter variants, packaging systems, and enhanced shells:

::: {}
  ------------------------------------------------------------------------------ ------------------------ --------------------------------------------------------------------------------
  **Variant**                                                                    **Supported versions**   **Description**
  [CPython](https://www.python.org/)                                     2.4 and up               Standard implementation in C
  [PyPy](https://www.pypy.org/)                                          2.7 and up               Implementation with just-in-time compiler
  [Stackless Python](https://github.com/stackless-dev/stackless/wiki/)   2.4 and up               Implementation supporting microthreading
  [IronPython](https://ironpython.net/)                                  2.7 and up               Implementation for .NET CLR and Mono
  [Jython](https://www.jython.org/)                                      2.5 to 2.7 (and up?)     Implementation for JVM
  [ActiveState Python](https://www.activestate.com/products/python/)     2.7 and up               Secure supply chain open source solution
  [eGenix PyRun](https://www.egenix.com/products/python/PyRun/)          2.5 and up               One-file, no-installation CPython environment
  [WinPython](https://winpython.github.io/)                              3.0 and up               Portable Scientific Python for Windows
  [PortablePython](https://portablepython.com/)                          2.7 and up               Minimalistic Python distribution for Windows
  [IDLE](https://docs.python.org/3/library/idle.html)                    all                      Python\'s Integrated Development and Learning Environment
  [IPython](https://ipython.org/)                                        all                      Powerful interactive shell; kernel for [Jupyter](https://jupyter.org/)
  ------------------------------------------------------------------------------ ------------------------ --------------------------------------------------------------------------------
:::

EmPy is also compatible with scaled-down implementations of Python, provided they support the set of standard modules that EmPy requires, namely:

- `codecs`{.backtick}

- `copy`{.backtick}

- `getopt`{.backtick}

- `os`{.backtick}

- `platform`{.backtick}

- `re`{.backtick}

- `sys`{.backtick}

- `unicodedata`{.backtick}

Only a few .py module file(s) are needed to use EmPy; they can be installed system-wide through a distribution package, via PIP, or just dropped into any desired directory in the `PYTHONPATH`{.backtick} (as a module) and/or `PATH`{.backtick} (as an executable). A minimal installation need only install the em.py file, either as an importable module or an executable, or both, depending on the user\'s needs.

EmPy also has optional support for several [third-party emoji modules](http://www.alcyone.com/software/empy/README.html#third-party-emoji-modules); see [Emoji markup](http://www.alcyone.com/software/empy/README.html#emoji-markup) for details.

The testing system included (the test.sh script and the tests and suites directories) is intended to run on Unix-like systems with a Bourne-like shell (*e.g.*, sh, bash, zsh, etc.). EmPy is routinely tested with all supported versions of all available interpreters.

If you find an incompatibility with your Python interpreter or operating system, [let me know](http://www.alcyone.com/software/empy/README.html#reporting-bugs).

## License 

This software is licensed under [BSD (3-Clause)](https://opensource.org/licenses/bsd-3-clause/).

## Note 

This is an excerpt of the [EmPy README](http://www.alcyone.com/software/empy/README.html), so consider it [InTheirOwnWords](../archive/InTheirOwnWords).
