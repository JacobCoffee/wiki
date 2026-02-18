# Why is Python slower than the xxx language

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

SEE:**[Ten things people want to know about Python](Ten%20things%20people%20want%20to%20know%20about%20Python)**for more details.

Answer

:   - \'Faster\' requires a bit of thought in practice. Language implementations, instead of language syntax, have a speed that can be measured on benchmarks. Python implementations can vary quite a bit, although dynamically typed languages usually perform slower than statically typed ones on standard benchmarks. As a practical matter, a profiler is necessary to understand performance. Python usually runs plenty fast.

First, the language implementations have speed, Python as a language is a set of rules (its syntax and semantics) and so doesn\'t have a \'speed\'. Only a specific language implementation can have a measurable speed, and then we can only compare performance with a specific implementation of another language. In general you can\'t compare the speed of one language to another - you can only compare implementations.

- With Python there are several implementations - CPython (with or without Psyco, a specializing compiler for CPython), [IronPython](../implementations/IronPython), Jython, [PyPy](../implementations/PyPy) - plus several partial implementations that implement a subset of Python (Tinypy) or can even compile a subset of Python to C++ (Shedskin). If you say Python is slow, which specific implementation are you talking about?

  Having said that, as a dynamic language Python will typically perform slower for specific benchmarks than standard implementations of some other languages (although it is faster than plenty of others). As a dynamic language a lot of information about the program can only be determined at runtime. This means that a lot of common compiler tricks, that rely on knowing the type of objects at compile time, can\'t work. Despite this there are a lot of things that can be done to improve the performance of dynamic languages (beyond the performance of statically typed languages many believe), several of which have been done before in virtual machines like Strongtalk and are being explored for Python in the [PyPy](../implementations/PyPy) JIT tracing compiler. Finally, using an execution profiler, such as the Python profile or cprofile module, provides the critical information for speeding up execution. Most programs spend the majority of execution time in calls to operating system libraries and execution trade-offs are less intuitive. For example, many small requests for data across a network are much slower than a single, larger request. In practice, Python code execution is fast enough.
