# ClarkUpdike/ScrapBook

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### IOError When Pasting Code Into Console 

#### March 01, 2005 Update 

It seems to be related to running from the jar as opposed to the class directories.

#### Feb 28, 2005 

Using the latest build, I\'m getting IOError\'s when I try to paste multiple lines of code into the console.

Here it is working in the 2.1 console:

    C:\WINDOWS\SYSTEM32>jython_142
    Jython 2.1 on java1.4.2 (JIT: null)
    Type "copyright", "credits" or "license" for more information.
    >>> # 1 ##############################################################################################
    >>> # 2 ##############################################################################################
    >>> # 3 ##############################################################################################
    >>> # 4 ##############################################################################################
    >>> # 5 ##############################################################################################
    >>> # 6 ##############################################################################################
    >>> # 7 ##############################################################################################
    >>> # 8 ##############################################################################################
    >>> # 9 ##############################################################################################
    >>>
    >>>

Here is the same thing broken in the 2.2a console:

    C:\Documents and Settings\updikca1>jytip
    Jython 2.2a1 on java1.4.1_03 (JIT: null)
    Type "copyright", "credits" or "license" for more information.
    >>> # 1 ##############################################################################################
    Traceback (innermost last):
      (no code object) at line 0
    IOError: Not enough storage is available to process this command

    C:\Documents and Settings\updikca1># 2 #################################################################################
    #############
    '#' is not recognized as an internal or external command,
    <snip>

It\'s not entirely deterministic, but this case will work: {{}}

But adding one additional char will break it (at least for me).

Does anyone else experience this?
