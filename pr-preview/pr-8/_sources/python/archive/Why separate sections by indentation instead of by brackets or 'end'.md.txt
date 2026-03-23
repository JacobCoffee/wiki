# Why separate sections by indentation instead of by brackets or 'end'

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

SEE:**[Ten things people want to know about Python](Ten%20things%20people%20want%20to%20know%20about%20Python)**

Answer

:   - In order to separate blocks of code (like for loops, if blocks and function definitions) the compiler / interpreter needs something to tell it when a block ends. Curly braces and end statements are perfectly valid ways of providing this information for the compiler. For a human to be able to read the code indentation is a much better way of providing the visual cues about block structure. As indentation also contains all the information for the compiler, to use both would be redundant. As indentation is better for humans, it makes sense to use that for the compiler too. It has the advantage that Python programs tend to be uniformly and consistently indented, removing one hurdle to understanding other people\'s code. Python does not mandate how you indent (two spaces or four, tabs or spaces - but not both), just that you do it consistently. Those that get used to the Python way of doing things tend to start seeing curly braces as unnecessary line noise that clutters code. On the other hand, [\'the whitespace thing\'](./(27)the(20)whitespace(20)thing(27).html) is possibly the single biggest reason why some developers refuse to even try Python.

\[Folklore says that the [ABC](./ABC.html)ers in the \'80s experimentally determined that significant whitespace has measurable advantages. \'Anyone have documentation for this?\]

Additional observation::

- Among programmers using languages which ignore white space the prevailing conventions are to indent blocks of code to facilitate readability by humans. The exact details of such conventions vary (and are subject to considerable stylistic debate among some programmers). But the general features are ubiquitous, nearly universal: code is rendered mostly in an \"outline\" format \... with levels of lexical nesting denoted by increasing degrees of indentation. Python merely uses this (nearly universal) convention as part of its syntax which allows it to dispense with other block ending tokens. Some argue that this syntax helps avoid situations where the code doesn\'t match the apparent intent (when the indentation is subtly inconsistent with the lexical structure). As with the finer points of how code should be indented in white space agnostica languages, that is a point of endless discussion.
