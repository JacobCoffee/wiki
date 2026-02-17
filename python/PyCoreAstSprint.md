# PyCoreAstSprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# What We Are Going To Do 

Guido has requested that the AST branch please be finished for Python 2.5 . Sprint on the AST branch has also become a tradition since the first sprint at [PyCon](PyCon) 2003. Here is a rough list of what needs to be worked on:

\* applying patches from SF

\* Get generator expression working

\* Get decorators working

\* Work out bugs (including memory leaks)

\* Flesh out docs on AST

# Preparing 

To get ready for the sprint, get a CVS checkout of the \'ast-branch\'. How to do get a tagged branch, see the Python Dev FAQ @ [http://www.python.org/dev/devfaq.html](http://www.python.org/dev/devfaq.html) .

Once you have a checkout, read Python/compile.txt . That gives an overview of what files are involved and how the basic process works.

# Attendees 

\* Brett Cannon

\* Neal Norwitz (maybe)

\* LD Landis

\* John Ehresman (arriving early afternoon on Saturday)

\* Timothy Fitz

Q: Is a pythonite with very little hacking-CPython experience of any use? \-- Timothy Fitz

A: Sure! Part of the point of the sprints is to teach people about what is being sprinted on in hopes of them continuing to contribute long after the sprint is over. I just can\'t make any guarantees about entertainment value. =) \-- Brett C.

\* Chuck Fox \-- On memory leaks, I\'ve seen leaky behaviour when partially using the subprocess module while also using older methods from the os module to look at the same processes. I would be interested in investigating why this occurs.

------------------------------------------------------------------------

[CategoryPyCon2005](CategoryPyCon2005)
