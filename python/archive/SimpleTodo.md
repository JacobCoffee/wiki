# SimpleTodo

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

These are straightforward, finite-effort coding or writing projects.

## Use Py_VISIT 

The `Py_VISIT()`{.backtick} macro in `objimpl.h`{.backtick} was introduced to make coding of most `tp_traverse`{.backtick} slots straightforward, uniform, and obviously correct. For example, see `cycle_traverse()`{.backtick} in `itertoolsmodule.c`{.backtick}. Most older modules that define `tp_traverse`{.backtick} copy/paste/edit the tedious callback dance by hand, and several even define their own work-alike macros. These should be rewritten to use the standard `Py_VISIT`{.backtick} macro.

## Use Py_CLEAR 

The `Py_CLEAR`{.backtick} macro in `object.h`{.backtick} was introduced to make coding of \"decref and NULL out a containee pointer\" operations safe. The reasons for why this is important but tricky to achieve are explained in a comment block before that macro in current trunk source. `tp_clear`{.backtick} and even `tp_dealloc`{.backtick} slot implementations should generally use `Py_CLEAR`{.backtick} now.

## Clean up 64-bit compiler warnings 

There are many 64-bit warnings produced by icc when using the -Wp64 flag. icc is freely available for a one month trial license. [NealNorwitz](./NealNorwitz.html) has a license and can make the warnings available on the web if anyone is interest in getting rid of these warnings. In addition, there is a patch to gcc to produce such warnings.

## Make modules Py_ssize_t clean 

Some modules don\'t use `Py_ssize_t`{.backtick}. They need a code review. Any module which declares an int (rather than a `Py_ssize_t`{.backtick}) for size and passes its address to `PyArgs_ParseTuple(args, "s#", &str, &size)`{.backtick} needs to be updated. An example of a module that has already been updated is `Modules/_codecsmodule.c`{.backtick}

## Check for consistent memory API usage 

[http://mail.python.org/pipermail/python-dev/2006-March/062848.html](http://mail.python.org/pipermail/python-dev/2006-March/062848.html)

Verify that if `PyMem_*`{.backtick} APIs are used to (re)allocate memory, that `PyMem_*`{.backtick} APIs are used to free memory. Same deal with `PyObject_*`{.backtick} APIs. (ie, ensure that `PyMem_*`{.backtick} and `PyObject_*`{.backtick} memory APIs aren\'t mixed.)

## Verify all int/long C APIs are correct 

With the conversion to use `Py_ssize_t`{.backtick}, it\'s important that we didn\'t miss any APIs. There are very few APIs which take (or return) a long. But there are still quite a few that take/return an int. All of these are believed to be correct, but more reviewers could help. Any API which returns an int is fine if the value is known to fit in 32 bits (like APIs that return a value between -2 and 2).

## Add Py_LOCAL, Py_LOCAL_INLINE declarations 

At the [NeedForSpeed](../performance/NeedForSpeed) sprint, these macros were added to use a faster calling convention on Windows. There are probably many modules where these macros could be used.

Currently these macros only make a difference on Windows. Are there other pragmas that could be used with GCC or other compilers?

## Use Py_MEMCPY 

Py_MEMCPY can be used instead of memcpy in cases where the copied blocks are often very short. While most platforms have highly optimized code for large transfers, the setup costs for memcpy are often quite high. MEMCPY solves this by doing short copies \"in line\".

Using this macro gave a 20% speed improvement to some string functions. Are there other uses of memcpy() in CPython that would also benefit?

## Create tests for sequences over 2GB 

It would be great if someone could try to put together some tests for bigmem machines. The tests should be broken up by those that require 2+ GB of memory, those that take 4+, etc. Many people won\'t have boxes with that much memory. Ultimately, the tests should be incorporated into the test suite with a special designation similar to -u all. I\'m thinking -G \# where \# is the size of RAM in GB.

The test cases should test all methods (don\'t forget slicing operations) at boundary points, particularly just before and after 2GB. Strings are probably the easiest. There\'s unicode too. lists, dicts are good but will take more than 16 GB of RAM, so those can be pushed out some.

See [http://python.org/sf/1471578](http://python.org/sf/1471578)

# Test suite improvements 

See \[[ImprovingLibTests](ImprovingLibTests)\].

# Wiki updates 

Update the [PerlPhrasebook](PerlPhrasebook) for the current state of Python and Perl.

Write a Java or Ruby phrasebook.

Clean up the organization of database-related pages in the wiki.
