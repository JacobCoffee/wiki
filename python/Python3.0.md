# Python3.0

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page lists features that *Guido van Rossum himself* has mentioned as goals for Python 3.0. Parts of this page have been consolidated into PEP 3000 [\[5](./Python3(2e)0.html#e)\]

## Status 

Python 3.0 is currently (2008-07-12) in beta testing, and has much accumulated documentation. More official sources of information include:

- The development version of the Python 3.0 documentation: [http://docs.python.org/dev/3.0/](http://docs.python.org/dev/3.0/)

- PEPs covering changes for Python 3.0:
  - PEP 3000, \"Python 3000\": [http://www.python.org/dev/peps/pep-3000/](http://www.python.org/dev/peps/pep-3000/)

  - PEP 3100, \"Miscellaneous Python 3.0 Plans\": [http://www.python.org/dev/peps/pep-3100/](http://www.python.org/dev/peps/pep-3100/)

  - PEP 3099, \"Things that will Not Change in Python 3000\": [http://www.python.org/dev/peps/pep-3099/](http://www.python.org/dev/peps/pep-3099/)

  - PEP 3108, \"Standard Library Reorganization\": [http://www.python.org/dev/peps/pep-3108/](http://www.python.org/dev/peps/pep-3108/)

Unfortunately there does not appear to be a well-maintained single point of entry for someone to find all relevant changes that will occur in Python 3.0.

## Core Language Changes 

- Remove distinction between `int`{.backtick} and `long`{.backtick} types. [\[4](./Python3(2e)0.html#d)\]

- Make true division the default behavior. [\[4](./Python3(2e)0.html#d)\]

- Make all strings unicode [\[4](./Python3(2e)0.html#d)\], and have a separate `bytes`{.backtick} [\[2](./Python3(2e)0.html#b)\] type. [\[13](./Python3(2e)0.html#m)\]

- Make the `exec`{.backtick} statement a function again. [\[1](./Python3(2e)0.html#a)\]

- Remove old-style classes. [\[4](./Python3(2e)0.html#d)\]

- Replace the `print`{.backtick} statement with a function or functions. (e.g. `write(x, y, z), writeline(x, y, z)`{.backtick}) [\[1](./Python3(2e)0.html#a)\] [\[21](./Python3(2e)0.html#u)\]

- Make `as`{.backtick} a real keyword. [\[7](./Python3(2e)0.html#g)\]

- Add an attribute to exceptions for storing the traceback. [\[22](./Python3(2e)0.html#v)\]

- Remove `raise Exception, 'message'`{.backtick} syntax in favor of `raise Exception('message')`{.backtick}. [\[11](./Python3(2e)0.html#k)\] [\[20](./Python3(2e)0.html#t)\]

- Require that the first statement of a suite be on its own line. [\[1](./Python3(2e)0.html#a)\]

- Make `True`{.backtick} and `False`{.backtick} keywords. [\[6](./Python3(2e)0.html#f)\]

  - Reason: make assignment to them impossible.

- Raise an exception when making comparisons (other than equality and inequality) between two incongruent types. [\[24](./Python3(2e)0.html#x)\]

  - Reason: such comparisons do not make sense and are especially confusing to new users of Python.

- Require that all exceptions inherit a common base class. [\[9](./Python3(2e)0.html#i)\]

  - Reason: forces the use of classes as objects raised by exceptions and simplifies the implementation.

- Make the traceback a standard attribute of Exception instances [\[18](./Python3(2e)0.html#r)\]

  - Reason: inconvenient to pass the (type, value, traceback) triple that currently represents an exception around.

- Remove `` `x` ``. [\[1](./Python3(2e)0.html#a)\]

  - Instead: use `repr(x)`{.backtick}.

  - Reason: backticks are hard to read in many fonts and can be mangled by typesetting software.

- Remove the `<>`{.backtick} operator.

  - Instead: use `!=`{.backtick}.

- Remove support for string exceptions. [\[1](./Python3(2e)0.html#a)\]

  - Instead: use a class.

- Add a mechanism so that multiple exceptions can be caught using `except E1, E2, E3:`{.backtick}. For instance:

  :::: 
  ::: 
  ``` 
     1 except E1, E2, E3 as err:  # Store error variable
     2    ...
  ```
  :::
  ::::

  (Added by GvR, suggested by Bram Cohen.)

  - *JimD\'s suggested syntax:*

    :::: 
    ::: 
    ``` 
       1 except (E1, E2, E3), e:
       2    ...
       3 
       4 except E1, e:
       5    ...
    ```
    :::
    ::::

    The `except`{.backtick} code would then basically do the equivalent of `if issubclass(arg1, Exception) or isinstance(arg1, Exception): ... else if len(arg1): ...`{.backtick} (excepting, obviously, that this is implemented at a lower level in the C core). \--JimD

- Perhaps have optional declarations for static typing.
  - GvR suggested the syntax [\[17](./Python3(2e)0.html#q)\]: (but NOT for static typing - for declaring type information that would be checked at runtime, not compile time)

    :::: 
    ::: 
    ``` 
       1 def bar(low: int, high: int) -> float:
       2     ...
    ```
    :::
    ::::

  - Since some types only implement parts of an interface have \'strict\' and \'lax\' interfaces. Strict requires a complete implementation of the interface, lax requiring only a partial implementation with the rest being taken from interface defaults or ignored. This would require a new keyword/reserved word (strict) with lax mode being the default. This is to help duck typing. Ex:

    :::: 
    ::: 
    ``` 
       1 def baz(x as list, y as strict file):
       2     # x must only (be adapted to) implement part of the list interface
       3     # y must (be adapted to) implement the whole file interface
    ```
    :::
    ::::

  - Another proposal: Use -\> and =\> as type conversion operators (lax and strict, respectively).

    :::: 
    ::: 
    ``` 
       1 def qux(x -> list, y => file):
       2     # x must only (be adapted to) implement part of the list interface
       3     # y must (be adapted to) implement the whole file interface
    ```
    :::
    ::::

## Built-In Changes 

- Have `range()`{.backtick}, `zip()`{.backtick}, `dict.keys()`{.backtick}, `dict.items()`{.backtick}, and `dict.values()`{.backtick} return iterators.

- Move `compile()`{.backtick}, `intern()`{.backtick} and `id()`{.backtick} to the `sys`{.backtick} module. [\[1](./Python3(2e)0.html#a)\]

- Change `max()`{.backtick} and `min()`{.backtick} to consume iterators.

- Remove `coerce()`{.backtick} as it is obsolete. [\[1](./Python3(2e)0.html#a)\]

- Introduce `trunc()`{.backtick}, which would call the `__trunc__()`{.backtick} method on its argument.

  - Reason: used for objects like `float`{.backtick}s where calling `__int__()`{.backtick} has data loss but an integral representation is still desired. [\[25](./Python3(2e)0.html#y)\]

- Remove `dict.iteritems()`{.backtick}, `dict.iterkeys()`{.backtick}, and `dict.itervalues()`{.backtick}.

  - Instead: use `dict.items()`{.backtick}, `dict.keys()`{.backtick}, and `dict.values()`{.backtick} respectively.

- Remove `apply()`{.backtick}. [\[1](./Python3(2e)0.html#a)\]

  - Instead: use `f(*args, **kw)`{.backtick}.

- Remove `xrange()`{.backtick}. [\[1](./Python3(2e)0.html#a)\] [\[4](./Python3(2e)0.html#d)\]

  - Instead: use `range()`{.backtick}.

- Remove `reduce()`{.backtick}. [\[1](./Python3(2e)0.html#a)\]

  - Instead: use `functools.reduce()`{.backtick}.

- Remove `callable()`{.backtick}. [\[1](./Python3(2e)0.html#a)\]

  - Instead: use `hasattr`{.backtick} to check for `__call__`{.backtick} attribute.

- Remove `buffer()`{.backtick}. [\[1](./Python3(2e)0.html#a)\] [\[2](./Python3(2e)0.html#b)\]

  - Instead: use new `bytes`{.backtick} type.

- Remove `raw_input()`{.backtick}. [\[1](./Python3(2e)0.html#a)\]

  - Instead: use `input()`{.backtick}.

- Remove `input()`{.backtick}. [\[1](./Python3(2e)0.html#a)\]

  - Instead: use `eval(input())`{.backtick}.

- Remove `execfile()`{.backtick} and `reload()`{.backtick}. [\[1](./Python3(2e)0.html#a)\]

  - Instead: use `exec()`{.backtick}.

- Remove `basestring.find()`{.backtick} and `basestring.rfind()`{.backtick}. [\[23](./Python3(2e)0.html#w)\]

  - Instead: use `basestring.index()`{.backtick} and `basestring.rindex()`{.backtick} in a `try/except`{.backtick} block.

## Standard Library Changes 

- Remove `types`{.backtick} module.

  - Instead: use the types in `__builtins__`{.backtick}.

- Remove other deprecated modules. [\[3](./Python3(2e)0.html#c)\]

- Remove `sys.exc_type`{.backtick}. [\[1](./Python3(2e)0.html#a)\]

  - Instead: use `sys.exc_info`{.backtick}.

  - Reason: it is not thread safe.

- Reorganize standard library to have more package structure.
  - Reason: there are too many modules to keep a flat hierarchy.

## Open Issues 

- `L += x`{.backtick} and `L.extend(x)`{.backtick} are equivalent. *No, they are not. The former creates a new list without modifying the original list (which other people might have references to). The latter modifies the original list.*

- Can the parameter order of the `insert`{.backtick} method be changed so the the index parameter is optional and `list.append`{.backtick} may be removed?

- If only `Exception`{.backtick} subclasses can be `raise`{.backtick}d [\[9](./Python3(2e)0.html#i)\], should the `raise`{.backtick} statement be kept? Could `x(y).raise()`{.backtick} be used instead?

- Are `repr()`{.backtick} and `str()`{.backtick} both needed? [\[1](./Python3(2e)0.html#a)\]

- Should `globals()`{.backtick}, `locals()`{.backtick} and `vars()`{.backtick} be removed? [\[1](./Python3(2e)0.html#a)\]

- Should there be a keyword for allowing the shadowing of built-ins?

- Should injecting into another module\'s global namespace be prevented?

- If line continuations (`\`{.backtick}) are removed from the language [\[1](./Python3(2e)0.html#a)\], what should be done about the instances where statements do not allow parentheses? Furthermore, the Python style guide [\[11](./Python3(2e)0.html#k)\] recommends their usage in some cases.

- Should `__cmp__`{.backtick} (and possibly `cmp()`{.backtick}) be removed? [\[8](./Python3(2e)0.html#h)\]

  - Reason: [TOOWTDI](TOOWTDI) and rich comparisons are another way.

- Should list comprehensions be equivalent to passing a generator expression to `list()`{.backtick}?

  - Reason: they are essentially the same and it would remove edge-case differences between them.

- With a new string substitution scheme [\[14](./Python3(2e)0.html#n)\], will old-style (`%(var)s`{.backtick}) substitutions be removed?

- There are things in the `string`{.backtick} module that I think belong there, for example `string.letters`{.backtick} and `string.digits`{.backtick}. I don\'t think that all the string manipulations that we might include with the standard libraries need to be in the core interpreter (any more than I would condone putting the regular expression engine into the core). \-- JimD

- Should a `with`{.backtick} (or `using`{.backtick}) statement be added? [\[10](./Python3(2e)0.html#j)\] [\[19](./Python3(2e)0.html#s)\]

  :::: 
  ::: 
  ``` 
     1 with self:
     2     .foo = [1, 2, 3]
     3     .bar(4, .foo)
  ```
  :::
  ::::

## References 

- \[1\] Python Regrets: [http://www.python.org/doc/essays/ppt/regrets/PythonRegrets.pdf](http://www.python.org/doc/essays/ppt/regrets/PythonRegrets.pdf)

- \[2\] PEP 296 \-- Adding a bytes Object Type: [http://python.org/peps/pep-0296.html](http://python.org/peps/pep-0296.html)

  - PEP 296 is withdrawn by the author in favor of PEP 358.

- \[3\] PEP 4 \-- Deprecation of Standard Modules: [http://python.org/peps/pep-0004.html](http://python.org/peps/pep-0004.html)

- \[4\] [PyCon](PyCon) 2003 State of the Union Address: [http://www.python.org/doc/essays/ppt/pycon2003/pycon2003.ppt](http://www.python.org/doc/essays/ppt/pycon2003/pycon2003.ppt)

- \[5\] PEP 3000 \-- Python 3.0 Plans: [http://python.org/peps/pep-3000.html](http://python.org/peps/pep-3000.html)

- \[6\] Python-Dev \-- Constancy of None: [http://mail.python.org/pipermail/python-dev/2004-July/046294.html](http://mail.python.org/pipermail/python-dev/2004-July/046294.html)

- \[7\] Python-Dev \-- \"as\" to be a keyword?: [http://mail.python.org/pipermail/python-dev/2004-July/046316.html](http://mail.python.org/pipermail/python-dev/2004-July/046316.html)

- \[8\] Python-Dev \-- lists vs. tuples:

  - [http://mail.python.org/pipermail/python-dev/2003-March/034073.html](http://mail.python.org/pipermail/python-dev/2003-March/034073.html)

  - [http://mail.python.org/pipermail/python-dev/2003-March/034074.html](http://mail.python.org/pipermail/python-dev/2003-March/034074.html)

- \[9\] Python-Dev \-- Exceptional inheritance patterns: [http://mail.python.org/pipermail/python-dev/2004-August/047114.html](http://mail.python.org/pipermail/python-dev/2004-August/047114.html)

- \[10\] Python-Dev \-- With statement: [http://mail.python.org/pipermail/python-dev/2004-March/043545.html](http://mail.python.org/pipermail/python-dev/2004-March/043545.html)

- \[11\] PEP 8 \-- Style Guide for Python Code: [http://python.org/peps/pep-0008.html](http://python.org/peps/pep-0008.html)

- \[12\] [PythonThreeDotOh](PythonThreeDotOh)

- \[13\] PEP 332 \-- Byte vectors and String/Unicode Unification: [http://python.org/peps/pep-0332.html](http://python.org/peps/pep-0332.html)

- \[14\] PEP 292 \-- Simpler String Substitutions: [http://python.org/peps/pep-0292.html](http://python.org/peps/pep-0292.html)

- \[16\] PEP 246 \-- Object Adaption: [http://www.python.org/peps/pep-0246.html](http://www.python.org/peps/pep-0246.html)

- \[17\] Python-Dev \-- Decorators: vertical bar syntax: [http://mail.python.org/pipermail/python-dev/2004-August/047424.html](http://mail.python.org/pipermail/python-dev/2004-August/047424.html)

- \[18\] Python-Dev \-- anonymous blocks: [http://mail.python.org/pipermail/python-dev/2005-April/053060.html](http://mail.python.org/pipermail/python-dev/2005-April/053060.html)

- \[19\] PEP 340 \-- loose ends: [http://mail.python.org/pipermail/python-dev/2005-May/053252.html](http://mail.python.org/pipermail/python-dev/2005-May/053252.html)

- \[20\] Python-Dev \-- PEP 8: exception style: [http://mail.python.org/pipermail/python-dev/2005-August/055190.html](http://mail.python.org/pipermail/python-dev/2005-August/055190.html)

- \[21\] Python-Dev \-- Replacement for print in Python 3.0: [http://mail.python.org/pipermail/python-dev/2005-September/056154.html](http://mail.python.org/pipermail/python-dev/2005-September/056154.html)

- \[22\] Python-Dev \-- anonymous blocks: [http://mail.python.org/pipermail/python-dev/2005-April/053060.html](http://mail.python.org/pipermail/python-dev/2005-April/053060.html)

- \[23\] Python-Dev \-- Remove str.find in 3.0?: [http://mail.python.org/pipermail/python-dev/2005-August/055705.html](http://mail.python.org/pipermail/python-dev/2005-August/055705.html)

- \[24\] Python-Dev \-- Comparing heterogeneous types: [http://mail.python.org/pipermail/python-dev/2004-June/045111.html](http://mail.python.org/pipermail/python-dev/2004-June/045111.html)

- \[25\] Python-Dev \-- Fixing \_[PyEval](./PyEval.html)\_[SliceIndex](./SliceIndex.html) so that integer-like objects can be used: [http://mail.python.org/pipermail/python-dev/2005-February/051674.html](http://mail.python.org/pipermail/python-dev/2005-February/051674.html)
