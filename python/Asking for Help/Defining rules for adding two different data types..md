# Asking for Help/Defining rules for adding two different data types.

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: Defining rules for adding two different data types 

I\'m a beginner with Python and am trying to create a Complex number class. The problem I am having is as follows, if z is a complex number (or other special type) how can I find 1+z? I am able to handle z+1, but it would be much nicer to have the operation be commutative. Whenever I attempt to compute 1+z I receive a [TypeError](TypeError).

------------------------------------------------------------------------

You do know that Python has a complex number type? For example:

:::: 
::: 
``` 
1 + 1j
# gives (1+1j) - a complex number
```
:::
::::

However, you could certainly define your own for educational purposes. It sounds like you support addition where a complex number instance is on the left hand side of an addition operation, but not on the right hand side. What happens when Python tries to perform an addition operation is this:

1.  Python looks for a `__add__`{.backtick} method on the left hand side operand. If this isn\'t found or if it returns `NotImplemented`{.backtick} (the method doesn\'t want to add the right hand side operand to itself), then\...

2.  Python looks for a `__radd__`{.backtick} method on the right hand side operand. If this isn\'t found or doesn\'t want to use the left hand side operand, then you get a `TypeError`{.backtick}.

So perhaps your class needs to define the `__radd__`{.backtick} method. \-- [PaulBoddie](PaulBoddie) 2011-03-26 23:04:42

::: note
When *answering* questions, add the [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered) category when saving the page. This will move the link to this page from the questions section to the answers section on the [Asking for Help](./Asking(20)for(20)Help.html) page.
:::

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
