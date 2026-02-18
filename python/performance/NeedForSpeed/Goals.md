# NeedForSpeed/Goals

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Sprint topics following the [NeedForSpeed]() theme**

You can add additional topics below. Please discuss the specific goals and possible approaches to these tasks!

## CPython 

- CPython 2.5 is slower than CPython 2.4. See [/Slowdown](Goals/Slowdown).

- Can floating point ops be sped-up by avoiding flag/exception checks at every step? Can some floating point ops be in-lined in ceval.c?
  - [TimPeters](../../people/TimPeters): By default, CPython does no flag or exception checks on float ops \-- the `PyFPE_START_PROTECT`{.backtick} and `PyFPE_END_PROTECT`{.backtick} macros normally have empty expansions. Inlining is possible but probably undesirable. Doing masses of fp ops in one gulp via the [NumPy](../../science/NumPy) (or whatever it\'s called now) extension is the sanest approach.

- Implement portions of the decimal module in C
  - [RichardJones](../../people/RichardJones): Looks like this has a good chance of being done in [SummerOfCode](../../soc/SummerOfCode).

    [RaymondHettinger](./RaymondHettinger.html): We can get them off to a good start by laying the groundwork (the C struct, some access macros, and implementing a couple of methods that they can use as a model).

    [GeorgBrandl](./GeorgBrandl.html): I\'ve created a skeleton C module since I was expecting to work on this.

- Build-out struct module to support fast, high-volume binary conversions \-- perhaps with regexp analogs such struct.compile() and struct.finditer()
  - [SeanReifschneider](../../people/SeanReifschneider): I am interested in working on this. First job would be figuring out how to best do this. Can/should it be any faster than a tight C loop that creates the required objects, I think that may dominate execution speed, but would appreciate input.

    [PietDelport](./PietDelport.html): This would be extremely useful in so many contexts. I can think of the following sources of inspiration:

    - Erlang\'s [bit syntax](http://www.erlang.org/doc/doc-5.4.12/doc/programming_examples/bit_syntax.html) feature

    - [Construct](http://pyconstruct.wikispaces.com/)

- Create a string subclass that provides lazy slicing without copying
  - [FredrikLundh](../../people/FredrikLundh): Creating the class is easy, but integrating it into Python is harder (most code that handles e.g. 8-bit strings assume a PyString). For Py3K, it would be quite interesting to \"instrument\" a Python interpreter, mapping all [PyString](./PyString.html) macros to functions, and gathering some kind of usage statistics.

    [TimPeters](../../people/TimPeters): Just noting a subtlety: PyString objects are always NUL-terminated, so that passing them to random C libraries doesn\'t require copying the guts. String slices won\'t have that property.

    [RaymondHettinger](./RaymondHettinger.html): I will search for a patch that Skip wrote for a possible implementation of str.partition() which returns a string subclass with pointers to the slices instead of a full copy. Any subsequent string ops lazily evaluate the slice into a full string.

- Allow selective removal of unused features such as profiling support
  - [SteveHolden](../../people/SteveHolden): this looks promising enough that I\'ll try to get my teeth into it. I\'ll take suggestions for other features we might look at for conditional removal.

- Faster parsing of strings and bytes into int, long, etc.
  - [TimPeters](../../people/TimPeters): part of that is algorithms, and part is the sheer depth of the call stack. The platform C library converts decimal strings to floats. There are two patches outstanding of special interest: [1335972](http://bugs.python.org/issue1335972 "SF") for string -\> short int (DONE), and [1442927](http://bugs.python.org/issue1442927 "SF") for string -\> long (DONE).

    [SeanReifschneider](../../people/SeanReifschneider): If the string is less than 9 bytes, can we just call strtol? Would that help? I suspect the check may cost too much, but maybe something in between like special-casing short strings to call strtol?

- Buffer for use with network I/O
  - Fredrik Lundh: Also see the stringobject comment below.

    [SeanReifschneider](../../people/SeanReifschneider): If we have buffering of network I/O, we can change readline() so that there is not a system-call for every character in the line. What about for file I/O?

- Build-out the collections module for optimized data structures:
  - ordered dictionary

  - alternate list implementation optimized for fast insertion and deletion

  - red/black tree

  - pivot tables

  - skip list

    [TimPeters](../../people/TimPeters): what does \"ordered dictionary\" mean? For example, sorted by key value, or sorted by insertion time?

    [PatrickObrien](./PatrickObrien.html): one definition of \"ordered dictionary\" is the order of insertion. The best Python implementation, including extensive unit tests, is available here: [source code](http://schevo.org/trac/browser/trunk/Schevo/schevo/lib/odict.py), [unit tests](http://schevo.org/trac/browser/Schevo/trunk/tests/test_odict.py?rev=2066) ([Anthon van der Neut](../../archive/Anthon%20van%20der%20Neut): unit tests seem to have been replaced by [doctests](http://schevo.org/trac/browser/trunk/Schevo/schevo/test/test_odict.py)).

    [OrenTirosh](./OrenTirosh.html): You can find several independent implementations of an order-preserving dictionary, nearly all of them called \"odict\". This kind of \"convergent evolution\" is a good hint that people want it.

    [WolfgangGrafen](./WolfgangGrafen.html): One of the first implementations of and most complete implementation of an ordered dictionary was my seqdict package at [seqdict](http://home.arcor.de/wolfgang.grafen/Python/Modules/Modules.html) together with a tutorial. I could help specifying/testing/implementating the std lib ready new version.

    [SeanReifschneider](../../people/SeanReifschneider): John Shipman has a skiplist implementation. [http://infohost.nmt.edu/tcc/help/lang/python/examples/pyskip/](http://infohost.nmt.edu/tcc/help/lang/python/examples/pyskip/) I\'ve gotten preliminary approval from Shipman about using his skiplist implementation in Python. I\'m following up with him.

    A redblack tree patch is at [1324770](http://bugs.python.org/issue1324770 "SF"), but I\'ve got no idea if it\'s in a usable state.

  - [radix/crit-bit trees](http://www.wikipedia.com/wiki/Radix_tree "WikiPedia")

    [PietDelport](./PietDelport.html): for string-like keys, these are simpler (no balancing required) and more efficient than comparison-based binary search trees, and have additional properties that make them particularly useful for hierarchial/overlapping keys (CIDR prefixes, routing/dispatch tables, textual indexes, timestamps\...).

- Create a 64 bit [PyInt](./PyInt.html) type (for 32 bit machines)

  - [FredrikLundh](../../people/FredrikLundh): [PyInt64](./PyInt64.html), I hope? Or a configuration option? Or a polymorphic-under-the-hood [PyLong](./PyLong.html) type ?

    [TimPeters](../../people/TimPeters): Guido would probably be happy if \"short\" Python ints were in fact 64 bits on all boxes; that\'s come up before.

- Optimize methods in stringobject.c/unicodeobject.c
  - [FredrikLundh](../../people/FredrikLundh): I\'d like to work on refactoring the string method implementations into a \"polymorphic\" (SRE-style) support library. This would let us share source code between 8-bit and Unicode strings, and make it easier to reuse code also for future array/buffer/bytes types (etc).

    [SeanReifschneider](../../people/SeanReifschneider): I\'d help with that. Adding rfind() to string was horribly painful because of the code duplication.

\* Comparing 8-bit and Unicode performance ([AndrewDalke](./AndrewDalke.html), [FredrikLundh](../../people/FredrikLundh))

- 8-bit repeat is a lot faster than Unicode:
  - handle single-character strings separately (use Py_UNICODE_FILL)
  - instead of repeating the original string, repeat the string that has already been built (use Py_UNICODE_COPY instead of memcpy)

\* Add itertools.imerge() and itertools.izip_longest()

- [RaymondHettinger](./RaymondHettinger.html): IIRC, the unsolved problem was how to save partially constructed frames without impacting the performance of recursive functions.

<!-- -->

- Other ideas for speeding up function calls. For example, [patch 1479611](http://www.python.org/sf/1479611).

- **DONE** See [ListOfPerformanceRelatedPatches](../../archive/ListOfPerformanceRelatedPatches) for the list. Are there any other patches in the [patch tracker](http://sourceforge.net/tracker/?group_id=5470&atid=305470) that are worth investigating? See [ListOfPerformanceRelatedPatches](../../archive/ListOfPerformanceRelatedPatches) for the list.

- Improve gzip\'s readline performance (e.g. [patch 1281707](http://www.python.org/sf/1281707)).

  - [BobIppolito](../../people/BobIppolito): This is implemented, but the patch had to be rewritten to gracefully handle files that happen to have some really long lines.

- Improve interpreter startup time, like in patch [921466](http://bugs.python.org/issue921466 "SF").

## Pure Python Projects 

- Improve [language shootout](http://dada.perl.it/shootout/python.html) submissions

  - [SteveHolden](../../people/SteveHolden): while this might be useful for PR purposes, does it actually win us much in terms of improving performance of existing programs? bearophile: I\'ve already done what I can, for some of those programs it\'s not easy to improve them even more (with or without Psyco). For some of them (concurrency, etc) more work can be done.

- Improve the API for timeit.py. Guido thinks that much of the intelligence in the command-line interface should be shifted to importable functions.

- Continue function call speed enhancements.
  - From Neal Norwitz on python-dev: I should probably check in my perf patch for speeding up function calls. It would be great if someone picked that up in the sprint and polished it off. The last version I posted should work in debug and normal modes, adds some simple profiling. i think the only thing that it didn\'t have that Martin requested was more inlining of PyCFunction\_[CallMethod](./CallMethod.html)(?). I\'m not sure if that would be faster or not.

- Update [PythonSpeed/PerformanceTips](../PythonSpeed/PerformanceTips)

## Twisted 

- Speed improvements to select and poll reactors
- Reactor based on /dev/epoll
- Better integration with psyco
- Improvements against twisted benchmark

## Psyco 

- Support for 64-bit CPUs (e.g. Opteron)

- Support for generator expressions

- Support for nested scopes

- Support for more dictionary operations

- Speedup float arithmetic

- Support for more built-ins (e.g. int(), long(), float(), etc.)

- Upgrade for python 2.5

- Better tools for profiling psyco-ness of application

- Investigate usefulness of IVM (with aim to producing a more streamlined dispatch loop)

- LLVM backend

- Virtualized longs (for long longs)

- Virtualized slots (Ability to cache [getattribute]() values)

## Py3000 

- Make a wishlist for possible performance gains in Py3.0

## Shared Memory Lib 

\* [MartinBlais](../../people/MartinBlais): I have had this idea in the back of my head for the longest time, to write a small C library to let non-related Python processes (i.e. not forked from one another) access a same shared memory location, even if it is just to share strings, in the manner of a shared dictionary. There is POSH, but it cannot do that, you have to fork from a single parent to use it, which means it won\'t work within certain contexts (i.e. apache prefork). There is memcached, but it uses sockets, I\'m sure shmem would be faster (and it\'s applicable in the case where sharing only within the host is good enough). Now, I understand that it\'s not directly on the Python interpreter itself, but it would provide a path to making certain kinds of Python applications faster (could EWT benefit from this?), so I\'m proposing it here anyway. I\'m thinking of the following steps:

- \- Write it in C, with a thin Python layer just to convert the strings - Only allow the following operations: get, set, del, list keys - Only allow storing strings into it

(I\'m a sucker, really, because that\'s mostly an excuse to play with shmem interfaces, which I haven\'t had the chance to do under Linux yet\...)
