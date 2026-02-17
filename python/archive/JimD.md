# JimD

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Jim Dennis 

### Is it a sin? 

A colleague has recently been thrust into Python programming because we needed to create our own tools around some of the Opsware tools and using their APIs. He recently posed a question: *Is it a sin to not to include `if __name__ == '__main__':` in a Python file?*

As we become accustomed to Python it\'s easy for us to take the `if __name__` convention for granted. My personal opinion is that it belongs in every .py file even if only to serve as a point of documentation (put a *pass* statement or print an error message if the file represents code which has no meaningful standalone purpose). However I still wouldn\'t call it a \"sin\" to omit it.

In my response I came up with the following guidelines for him:

`if __name__ == '__main__': ` should be in every Python file with the following possible exeptions:

- A script NOT ending in .py (can\'t be accidentally imported so it\'s not strictly needed)
- A module which is NOT marked executable (can\'t be accidentally executed as a script)

Notably, the construct is harmless in both these cases as well. Properly used its inclusion will prevent the two problems that might arise from changes to filenames or permissions.

What if you execute something which is purely a module? \"Nothing\" happens. (All the definition and initialization code is processed and then the interpreter drops off the end of the file). Appending a warning like: \"Nothing to do! This file should be imported.\" is harmlessly helpful in case someone makes the file executable and someone (possibly someone else) blindly executes it.

What if you import a script without an `if __name__` line in it? A bunch of unintended activity \... possibly terminating importing script (if sys.exit() was called, for example). This is the one really bad case \... and one which should serve as an object lesson to any Pythonista who imports code without understanding what it\'s supposed to be doing). Notably, the code has to be in a file with a .py extension and it has to be on the PYTHONPATH (sys.path) for this failure mode to occur.

Prepending the whole script with the `if __name__` test (and indenting the whole body of code) then renders that error harmless. It runs just fine, and importing it does \"nothing.\"

In fact one could even add: `if __name__ != '__main__':` to print an error and call `sys.exit(1)` if an attempt is made to import a script that\'s written purely as an executable. That\'s perfectly legal. There\'s nothing magical about `if __name__ ==` \... it works like any other Python conditional construct.

As I was working with Joe (my colleague) I pointed out that it\'s a bit dubious to write code which is purely executable with no re-usability. I\'ve only seen that for very short, one or two line, wrappers which import and call into other Python code. I also pointed out that one can use the `if __name__` suite to implement unit tests in files which are (otherwise) purely modules.

The key point here is that the purpose of the `if __name__` check is to separate reusable code (definitions of classes and functions, and initializations of variables) from actions (which use the re-usable functionality). Python\'s syntax encourages us to make parts of every script re-usable and it can encourage us to include unit tests localized to the same files containing code and class definitions.

Email: `<aswrguy AT SPAMFREE gmail DOT com>`

\...

------------------------------------------------------------------------

[CategoryHomepage](CategoryHomepage)
