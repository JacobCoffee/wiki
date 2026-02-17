# Asking for Help/I want to right-click on data files in Windows XP and open them with a Python program.

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: I want to right-click on data files in Windows XP and open them with a Python program. 

When I try to do this, Windows tells me that the data file is not a valid Win32 application (of course it isn\'t!). Why is it that I can do this with other programs, but not with Python programs?

I find that it works with .bat files. If I right-click on a data file and open it with a .bat file that runs a .py file, that works. But it works only with one data file. If I make a .bat file containing:

my_prog.py %\*

I think that should work with multiple data files, but it doesn\'t: only one of the data filenames reaches the .bat file, and therefore only one reaches the Python program.

I\'m bewildered that I can\'t find any coverage of this issue on the Web, nor in the Python books that I have (Learning Python and Programming Python). Surely this is how any normal Windows user would expect to use a Python program (or any other program), but it doesn\'t work. It may well be Microsoft\'s fault that it doesn\'t work, but why no discussion of such a fundamental issue?

::: note
When *answering* questions, add the [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered) category when saving the page. This will move the link to this page from the questions section to the answers section on the [Asking for Help](./Asking(20)for(20)Help.html) page.
:::

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp)
