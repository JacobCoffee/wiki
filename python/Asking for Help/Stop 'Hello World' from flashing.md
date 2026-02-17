# Asking for Help/Stop 'Hello World' from flashing

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: How do I stop the console/terminal/command line prompt from closing on Windows? 

Ok so, Let\'s say I want to run a program with a simple Print(\"hello world\"). How do I stop the console/terminal/command line prompt from closing immediately after it prints? I read somewhere that I\'m supposed to find some editpythonprefs, but I don\'t know where it is\... I am on Windows 7, if that helps

------------------------------------------------------------------------

Are you running the program from the file manager or do you already have the console open when running the program (by typing `python hello.py`{.backtick}, for example)? If the former is involved, which I suspect is the case, you could prevent the program from finishing by inserting something like the following at the end:

:::: 
::: 
``` 
raw_input("Press Enter to exit.")
```
:::
::::

I found a [question](http://stackoverflow.com/questions/2322868/how-do-i-prevent-my-python-2-6-application-from-automatically-closing-once-reachi) about this by searching the Internet for \"prevent Python program from exiting on Windows\". You\'ll find other more complicated suggestions if you follow various links from that question, but sometimes the simplest solutions are the best (or are at least good enough).

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
