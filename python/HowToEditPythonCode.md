# HowToEditPythonCode

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# History 

Python was conceived in the late 1980s and its implementation was started in December 1989 by Guido van Rossum at CWI in Amsterdam. Python is a successor to the ABC programming language (itself inspired by SETL) capable of exception handling and interfacing with the Amoeba operating system. Van Rossum is Python\'s principal author, and was for many years known by the humorous title *Benevolent Dictator for Life* (BDFL). Python evolution is now guided by an elected Steering Committee.

------------------------------------------------------------------------

# Programming philosophy 

Python is a multi-paradigm programming language. Rather than forcing programmers to adopt a particular style of programming, it permits several styles: object-oriented programming and structured programming are fully supported, and there are a number of language features which support functional programming and aspect-oriented programming (including metaprogramming and \"by magic\" methods). Many other paradigms are supported using extensions, such as pyDBC and Contracts for Python which allow Design by Contract.

Rather than requiring all desired functionality to be built into the language\'s core, Python was designed to be highly extensible. New built-in modules can be easily written in C, C++ or Cython. Python can also be used as an extension language for existing modules and applications that need a programmable interface. This design, a small core language with a large standard library with an easily extensible interpreter, was intended by Van Rossum from the very start because of his frustrations with ABC (which espoused the opposite mindset).

------------------------------------------------------------------------

# Name and neologisms 

An important goal of the Python developers is making Python fun to use. This is reflected in the origin of the name (based on the television series Monty Python\'s Flying Circus), in the common practice of using Monty Python references in example code, and in an occasionally playful approach to tutorials and reference materials.\[24\]\[25\] For example, the metasyntactic variables often used in Python literature are spam and eggs, instead of the traditional foo and bar.

------------------------------------------------------------------------

# Usage 

Python is often used as a scripting language for web applications, e.g. via mod_wsgi for the Apache web server. With Web Server Gateway Interface, a standard API has been developed to facilitate these applications. Web application frameworks like Django, Pylons, [TurboGears](TurboGears), web2py, Flask, and Zope support developers in the design and maintenance of complex applications. Libraries like [NumPy](NumPy), [SciPy](SciPy), and Matplotlib allow Python to be used effectively in scientific computing.

------------------------------------------------------------------------

# Syntax and semantics 

Python was intended to be a highly readable language. It is designed to have an uncluttered visual layout, frequently using English keywords where other languages use punctuation. Python requires less boilerplate than traditional manifestly typed structured languages such as C or Pascal, and has a smaller number of syntactic exceptions and special cases than either of these. For a detailed description of the differences between 2.x and 3.x versions, see History of Python.

## Indentation 

Python uses whitespace indentation, rather than curly braces or keywords, to delimit blocks (a feature also known as the *off-side rule*). An increase in indentation comes after certain statements; a decrease in indentation signifies the end of the current block.

## Statements and control flow 

Python\'s statements include (among others):

- The ***if*** statement, which conditionally executes a block of code, along with ***else*** and ***elif*** (a contraction of else-if).

- The ***for*** statement, which iterates over an iterable object, capturing each element to a local variable for use by the attached block.

- The ***while*** statement, which executes a block of code as long as its condition is true.

- The ***try*** statement, which allows exceptions raised in its attached code block to be caught and handled by except clauses; it also ensures that clean-up code in a ***finally*** block will always be run regardless of how the block exits.

- The ***class*** statement, which executes a block of code and attaches its local namespace to a class, for use in object-oriented programming.

- The ***def*** statement, which defines a function or method.

- The ***with*** statement (from Python 2.5), which encloses a code block within a context manager (for example, acquiring a lock before the block of code is run, and releasing the lock afterward).

- The ***pass*** statement, which serves as a NOP and can be used in place of a code block.

- The ***assert*** statement, used during debugging to check for conditions that ought to apply.

- The ***yield*** statement, which returns a value from a generator function. (From Python 2.5, ***yield*** is also an operator. This form is used to implement coroutines \-- see below.)

## Expressions 

- In Python 3, the result of the division operator `/`{.backtick} with integer operands is always a floating-point value; the operator `//`{.backtick} may be used to perform integer division (the result truncated to an integer).

  - In Python 2, the `/`{.backtick} operator on integers performs integer division. Floating-point division on integers can be achieved by converting one of the integers to a float (e.g. `float(x) / y`{.backtick}), or, since 2.2, the behavior of Python 3 can be enabled using `from __future__ import division`.

- In Python, `==`{.backtick} compares by value, in contrast to Java, where it compares by reference. (Value comparisons in Java use the equals() method.) Python\'s `is`{.backtick} operator may be used to compare object identities (comparison by reference). Comparisons may be chained, for example `a <= b <= c`{.backtick}.

- Python uses the words **and**, **or**, **not** for its boolean operators rather than the symbolic `&&`{.backtick}, `||`{.backtick}, `!`{.backtick} used in C.

- Python has a type of expression known as a list comprehension. Python 2.4 extended list comprehensions into a more general expression known as a generator expression.

- Anonymous functions are implemented using lambda expressions; however, these are limited in that the body can only be a single expression.

- Conditional expressions in Python are written as `x if c else y`{.backtick} (different in order of operands from the ?: operator common to many other languages).

- Python makes a distinction between lists and tuples. Lists, written as `[1, 2, 3]`{.backtick}, are mutable, and cannot be used as the keys of dictionaries (dictionary keys must be immutable in Python). Tuples, written as `(1, 2, 3)`{.backtick}, are immutable and thus can be used as the keys of dictionaries, provided all elements of the tuple are immutable. The parentheses around the tuple are optional in some contexts. Tuples can appear on the left side of an equal sign; hence a statement like `x, y = y, x`{.backtick} can be used to swap two variables.

- Multiple string-formatting operations are supported. The original **%** operator provided behavior analogous to printf format strings in C, e.g. `foo=%s bar=%d" % ("blah", 2)`{.backtick} evaluates to `foo=blah bar=2`{.backtick}. String templates were introduced in Python 2.4. Python 3.0 brought in the string `format()`{.backtick} method, with syntax like `foo={0} bar={1}".format("blah", 2)`{.backtick}. Formatted string literals (\"F-strings\") were introduced in 3.6, with syntax like `f'foo={"blah"} bar={2}'`{.backtick}\"

- Python has various kinds of string literals:
  - Strings are delimited by single or double quotation marks. Unlike in Unix shells, Perl and Perl-influenced languages, single quotation marks and double quotation marks function identically. Both kinds of strings use the backslash (`\`{.backtick}) as an escape character and there is no implicit string interpolation such as \"\$foo\".

  - Triple-quoted strings, which begin and end with a series of three single or double quotation marks, may span multiple lines and function like here-documents in shells, Perl and Ruby.

## Methods 

Methods on objects are functions attached to the object\'s class; the syntax instance.method(argument) is, for normal methods and functions, syntactic sugar for Class.method(instance, argument). Python methods have an explicit self parameter to access instance data, in contrast to the implicit self in some other object-oriented programming languages (for example, Java, C++ or Ruby).

## Typing 

Python uses duck typing and has typed objects but untyped variable names. Type constraints are not checked at compile time; rather, operations on an object may fail, signifying that the given object is not of a suitable type. Despite being dynamically typed, Python is strongly typed, forbidding operations that are not well-defined (for example, adding a number to a string) rather than silently attempting to make sense of them.

## Mathematics 

Python defines the modulus operator so that the result of a % b is in the half-open interval \[0,b), where b is a positive integer. When b is negative, the result lies in the interval (b,0\]. However, this consequently affects how integer division is defined. To maintain the validity of the equation b \* (a // b) + a % b == a, integer division is defined to round towards minus infinity. Therefore 7 // 3 is 2, but (−7) // 3 is −3. This is different from many programming languages, where the result of integer division rounds towards zero, and Python\'s modulus operator is consequently defined in a way that can return negative numbers.

------------------------------------------------------------------------

# Implementations 

## CPython 

The mainstream Python implementation, known as CPython, is written in C meeting the C89 standard. CPython compiles Python programs into intermediate bytecode,\[65\] which are then executed by the virtual machine. It is distributed with a large standard library written in a mixture of C and Python. CPython ships in versions for many platforms, including Microsoft Windows and most modern Unix-like systems. CPython was intended from almost its very conception to be cross-platform; its use and development on esoteric platforms such as Amoeba, alongside more conventional ones like Unix and Mac OS, has greatly helped in this regard. Unofficial builds are also available for [Android](Android) and iOS.

## Alternative implementations 

Jython compiles the Python program into Java byte code, which can then be executed by every Java Virtual Machine implementation. This also enables the use of Java class library functions from the Python program. [IronPython](IronPython) follows a similar approach in order to run Python programs on the .NET Common Language Runtime. [PyPy](PyPy) is a fast self-hosting implementation of Python, written in Python, that can output several types of bytecode, object code and intermediate languages. There also exist compilers to high-level object languages, with either unrestricted Python, a restricted subset of Python, or a language similar to Python as the source language. [PyPy](PyPy) is of this type, compiling RPython to several languages; other examples include Pyjamas compiling to [JavaScript](./JavaScript.html); Shed Skin compiling to C++; and Cython and Pyrex compiling to C.

## Interpretational semantics 

Most Python implementations (including CPython) can function as a command-line interpreter, for which the user enters statements sequentially and receives the results immediately. In short, Python acts as a shell. While the semantics of the other modes of execution (bytecode compilation, or compilation to native code) preserve the sequential semantics, they offer a speed boost at the cost of interactivity, so they are usually only used outside of a command-line interaction (e.g., when importing a module).

Other shells add capabilities beyond those in the basic interpreter, including IDLE and IPython. While generally following the visual style of the Python shell, they implement features like auto-completion, retention of session state, and syntax highlighting.

------------------------------------------------------------------------

# Development 

Python\'s development is conducted largely through the Python Enhancement Proposal (PEP) process, described in [PEP 1](https://www.python.org/dev/peps/pep-0001/). PEPs are standardized design documents providing general information related to Python, including proposals, descriptions, design rationales, and explanations for language features. Outstanding PEPs are reviewed and commented upon on the python-dev mailing list, which is the primary forum for discussion about the language\'s development and approved by the Steering Council (see [PEP 13](https://www.python.org/dev/peps/pep-013) for the governance model); specific issues are discussed in the bug tracker maintained at [bugs.python.org](https://bugs.python.org). Development of the reference implementation takes place on the [GitHub cpython](https://github.com/python/cpython) repository.

CPython\'s public releases come in three types, distinguished by which part of the version number is incremented:

- backward-incompatible versions, where code is expected to break and must be manually ported. The first part of the version number is incremented. These releases happen infrequently---for example, version 3.0 was released 8 years after 2.0.
- major or \'feature\' releases, which are largely compatible but introduce new features. The second part of the version number is incremented. These releases are scheduled to occur roughly every 18 months, and each major version is supported by bugfixes for several years after its release.
- bugfix releases, which introduce no new features but fix bugs. The third and final part of the version number is incremented. These releases are made whenever a sufficient number of bugs have been fixed upstream since the last release, or roughly every 3 months. Security vulnerabilities are also patched in bugfix releases.

A number of alpha, beta, and release-candidates are also released as previews and for testing before the final release is made. Although there is a rough schedule for each release, this is often pushed back if the code is not ready. The development team monitor the state of the code by running the large unit test suite during development, and using the [BuildBot](BuildBot) continuous integration system.

# Standard library 

Python has a large standard library, commonly cited as one of Python\'s greatest strengths,\[81\] providing pre-written tools suited to many tasks. This is deliberate and has been described as a \"batteries included\" Python philosophy. The modules of the standard library can be augmented with custom modules written in either C or Python. Boost C++ Libraries includes a library, Boost.Python, to enable interoperability between C++ and Python. Because of the wide variety of tools provided by the standard library, combined with the ability to use a lower-level language such as C and C++, which is already capable of interfacing between other libraries, Python can be a powerful glue language between languages and tools.

The standard library is particularly well-tailored to writing Internet-facing applications, with a large number of standard formats and protocols (such as MIME and HTTP) already supported. Modules for creating graphical user interfaces, connecting to relational databases, arithmetic with arbitrary precision decimals, manipulating regular expressions, and doing unit testing are also included.

Some parts of the standard library are covered by specifications (for example, the WSGI implementation wsgiref follows PEP 333), but the majority of the modules are not. They are specified by their code, internal documentation, and test suite (if supplied). However, because most of the standard library is cross-platform Python code, there are only a few modules that must be altered or completely rewritten by alternative implementations.

For software testing, the standard library provides the unittest and doctest modules.

------------------------------------------------------------------------

# Influence on other languages 

Python\'s design and philosophy have influenced several programming languages, including:

- Pyrex and its derivative Cython are code translators that are targeted at writing fast C extensions for the CPython interpreter. The language is mostly Python with syntax extensions for C and C++ features. Both languages produce compilable C code as output.
- Boo uses indentation, a similar syntax, and a similar object model. However, Boo uses static typing and is closely integrated with the .NET framework.\[84\]
- Cobra uses indentation and similar syntax. Cobra\'s \"Acknowledgements\" document lists Python first among the languages that influenced it. However, Cobra directly supports design-by-contract, unit tests and optional static typing.
- \\ borrowed iterators, generators, and list comprehensions from Python.
- Go is described as incorporating the \"development speed of working in a dynamic language like Python\".
- Groovy was motivated by the desire to bring the Python design philosophy to Java.
- OCaml has an optional syntax, called twt (The Whitespace Thing), inspired by Python and Haskell.

------------------------------------------------------------------------
