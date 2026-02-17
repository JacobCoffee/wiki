# MultiLineStringsInDocTest

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The [DocTest](DocTest) module requires special actions / processing for multi-line strings.

# Multi-Line Strings in commands 

Consider a function `get_html_title` designed to extract the title from an HTML page. Here is some python code to test the function:

:::: 
::: 
``` 
   1 >>> html = '''
   2 <html>
   3 <head>
   4 <title>This is the page title</title>
   5 </head>
   6 <body>
   7 This is the body
   8 </body>
   9 </html>
  10 '''
  11 >>> title = get_html_title(html)
  12 >>> assert(title == "This is the page title")
```
:::
::::

Putting this directly into a doctest results in an exception, such as:

    Failed example:
        html = '''
    Exception raised:
        Traceback (most recent call last):
          File "C:\Python24\lib\doctest.py", line 1243, in __run
            compileflags, 1) in test.globs
          File "<doctest sample.tests[1]>", line 1
             html = '''
                       ^
         SyntaxError: EOF while scanning triple-quoted string

The solution is to add the command continuation characters:

:::: 
::: 
``` 
   1 >>> html = '''
   2 ... <html>
   3 ... <head>
   4 ... <title>This is the page title</title>
   5 ... </head>
   6 ... <body>
   7 ... This is the body
   8 ... </body>
   9 ... </html>
  10 ... '''
  11 >>> title = get_html_title(html)
  12 >>> assert(title == "This is the page title")
```
:::
::::

# Multi-Line Strings in output 

Blank lines in the output need to be specially handled. For example, the following doctest will fail:

:::: 
::: 
``` 
   1 >>> test = "Here is a blank line\n\nBlank line is above"
   2 >>> print test
   3 Here is a blank line
   4 
   5 Blank line is above
```
:::
::::

This is because the blank line is used to seperate commands and comments. With Python 2.4, a `<BLANKLINE>` keyword was added, so the proper doctest is now:

:::: 
::: 
``` 
   1 >>> test = "Here is a blank line\n\nBlank line is above"
   2 >>> print test
   3 Here is a blank line
   4 <BLANKLINE>
   5 Blank line is above
```
:::
::::
