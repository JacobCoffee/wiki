# StringFormatting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# String Formatting 

The [section of the manual on String Formatting Operations](http://docs.python.org/lib/typesseq-strings.html) is hidden in the section on [Sequence types.](http://docs.python.org/lib/typesseq.html)

Tutorial on the new string formatting method `format()`{.backtick} in Python 3.0: [Py3kStringFormatting](../py3/Py3kStringFormatting)

## Direct Variable Reference 

A common trick you can use when writing strings is to refer directly to variables.

:::: 
::: 
``` 
   1 a = "hello, world!"
   2 x = 34
   3 y = 96
   4 
   5 print """
   6 a = %(a)s
   7 x,y = (%(x)s,%(y)s)
   8 """ % vars() # local variables
```
:::
::::

If you want to refer to global variables, you can replace `vars()` with `globals()`.

## Printing Percentages 

:::: 
::: 
``` 
   1 percent = lambda x:"%2.2f%%" % x
   2 
   3 print percent(35.3567) # prints "35.35%"
```
:::
::::

## Print strings without newlines and spaces 

You may find it tricky to print out a feed of numbers (as output from within a loop) on one line, without being separated by a space. An example could be output such as

    Processing...
    [1][2][3][4][5][6]
    Completed.

The standard `print`{.backtick} statement automatically inserts newlines. This can be overcome with

:::: 
::: 
``` 
   1 for i in range(10):
   2     print '['+str(i)+']',  # NOTE the trailing comma
```
:::
::::

but a space will get inserted between successive prints. One way to get around this is using `sys.stdout`{.backtick}:

:::: 
::: 
``` 
   1 import sys
   2 for i in range(10):
   3     sys.stdout.write('['+str(i)+']')
```
:::
::::

which will work properly.

## See Also 

[EscapingHtml](EscapingHtml), [WorkingWithTime](../archive/WorkingWithTime)

# Discussion 

You can also print a backspace (`'\b'`{.backtick}) to swallow the extra space. eg:

:::: 
::: 
``` 
   1 for i in range(10):
   2     print '\b%d' % i,
   3 # Prints: 0123456789
```
:::
::::

Unfortunately, this produces a mess if output is being directed to a file; it\'s best to avoid printing the space if you don\'t want it.

## Variable name substitution using format and eval 

I want to print out all member of `sys`{.backtick}, then what I need is

:::: 
::: 
``` 
   1 for member in dir(sys):
   2     print "sys." + member, "->", repr(getattr(sys, member))
```
:::
::::
