# EmptySubscriptListPEP

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

    PEP: XXX
    Title: Allow Empty Subscript List Without Parentheses
    Version: $Revision$
    Last-Modified: $Date$
    Author: Noam Raphael <spam.noam@gmail.com>
    Status: Draft
    Type: Standards Track
    Content-Type: text/x-rst
    Created: 09-Jun-2006
    Python-Version: 2.5?
    Post-History: 30-Aug-2002

::: 
### Abstract

This PEP suggests to allow the use of an empty subscript list, for example `x[]`, which is currently a syntax error. It is suggested that in such a case, an empty tuple will be passed as an argument to the \_\_getitem\_\_ and \_\_setitem\_\_ methods. This is consistent with the current behaviour of passing a tuple with n elements to those methods when a subscript list of length n is used, if it includes a comma.
:::

::: 
### Specification

The Python grammar specifies that inside the square brackets trailing an expression, a list of \"subscripts\", separated by commas, should be given. If the list consists of a single subscript without a trailing comma, a single object (an ellipsis, a slice or any other object) is passed to the resulting \_\_getitem\_\_ or \_\_setitem\_\_ call. If the list consists of many subscripts, or of a single subscript with a trailing comma, a tuple is passed to the resulting \_\_getitem\_\_ or \_\_setitem\_\_ call, with an item for each subscript.

Here is the formal definition of the grammar:

    trailer: '(' [arglist] ')' | '[' subscriptlist ']' | '.' NAME
    subscriptlist: subscript (',' subscript)* [',']
    subscript: '.' '.' '.' | test | [test] ':' [test] [sliceop]
    sliceop: ':' [test]

This PEP suggests to allow an empty subscript list, with nothing inside the square brackets. It will result in passing an empty tuple to the resulting \_\_getitem\_\_ or \_\_setitem\_\_ call.

The change in the grammar is to make \"subscriptlist\" in the first quoted line optional:

    trailer: '(' [arglist] ')' | '[' [subscriptlist] ']' | '.' NAME
:::

::: 
### Motivation

This suggestion allows you to refer to zero-dimensional arrays elegantly. In NumPy, you can have arrays with a different number of dimensions. In order to refer to a value in a two-dimensional array, you write `a[i, j]`. In order to refer to a value in a one-dimensional array, you write `a[i]`. You can also have a zero-dimensional array, which holds a single value (a scalar). To refer to its value, you currently need to write `a[()]`, which is unexpected - the user may not even know that when he writes `a[i, j]` he constructs a tuple, so he won\'t guess the `a[()]` syntax. If the suggestion is accepted, the user will be able to write `a[]` in order to refer to the value, as expected. It will even work without changing the NumPy package at all!

In the normal use of NumPy, you usually don\'t encounter zero-dimensional arrays. However, the author of this PEP is designing another library for managing multi-dimensional arrays of data. Its purpose is similar to that of a spreadsheet - to analyze data and preserve the relations between a source of a calculation and its destination. In such an environment you may have many multi-dimensional arrays - for example, the sales of several products over several time periods. But you may also have several zero-dimensional arrays, that is, single values - for example, the income tax rate. It is desired that the access to the zero-dimensional arrays will be consistent with the access to the multi-dimensional arrays. Just using the name of the zero-dimensional array to obtain its value isn\'t going to work - the array and the value it contains have to be distinguished.
:::

::: 
### Rationale

Passing an empty tuple to the \_\_getitem\_\_ or \_\_setitem\_\_ call was chosen because it is consistent with passing a tuple of n elements when a subscript list of n elements is used. Also, it will make NumPy and similar packages work as expected for zero-dimensional arrays without any changes.

Another hint for consistency: Currently, these equivalences hold:

    x[i, j, k]  <-->  x[(i, j, k)]
    x[i, j]     <-->  x[(i, j)]
    x[i, ]      <-->  x[(i, )]
    x[i]        <-->  x[(i)]

If this PEP is accepted, another equivalence will hold:

    x[]         <-->  x[()]
:::

::: 
### Backwards Compatibility

This change is fully backwards compatible, since it only assigns a meaning to a previously illegal syntax.
:::

::: 
### Reference Implementation

Available as SF Patch no. 1503556.

It passes the Python test suite, but currently doesn\'t provide additional tests or documentation.
:::

::: 
### Copyright

This document has been placed in the public domain.
:::
