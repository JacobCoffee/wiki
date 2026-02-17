# Asking for Help/How does the value from input() become a number, not a string? In 3.2?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: How does the value from input() become a number, not a string? In 3.2? 

At least in general for Python 2, not specifically about 3.2 where `input`{.backtick} is presumably the equivalent of `raw_input`{.backtick} in Python 2, the input is evaluated using the mechanism Python employs to evaluate expressions, so what happens is rather similar to what you would see at Python\'s interactive prompt except that only *expressions* are allowed, not *statements*.

So, if you provide a number in response to `input()`{.backtick}, such as\...

:::: 
::: 
``` 
34
```
:::
::::

\...`input`{.backtick} actually evaluates the string `"34"`{.backtick} and returns the number `34`{.backtick}. But `input`{.backtick} does more than evaluate numbers. For example:

:::: 
::: 
``` 
34 + 45
```
:::
::::

Here, `input`{.backtick} actually evaluates the string `"34 + 45"`{.backtick} and returns `79`{.backtick}. Note that `input`{.backtick} wants Python syntax, so if you want to just capture some text, you have to write a string in Python syntax:

:::: 
::: 
``` 
"ABC"
```
:::
::::

If you don\'t do this, then `input`{.backtick} will give an error.

    >>> input()
    ABC
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<string>", line 1, in <module>
    NameError: name 'ABC' is not defined

For just capturing strings, use `raw_input`{.backtick}. The `input`{.backtick} function is only recommended if you want to evaluate Python expressions read from input and if you can trust those expressions. Don\'t use `input`{.backtick} on data received from random people on the Internet, for example, as the code in the expressions can access other parts of your program just like your own code.

In 3.2, you would reproduce the functionality of `input`{.backtick} from Python 2 by combining `eval`{.backtick} with Python 3\'s `input`{.backtick} function:

:::: 
::: 
``` 
result = eval(input())
```
:::
::::

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
