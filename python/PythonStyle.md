# PythonStyle

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Python style conventions are described in PEPs.

- [PEP 8](http://www.python.org/peps/pep-0008.html) \-- Style Guide for Python Code

- [PEP 257](http://www.python.org/peps/pep-0257.html) \-- Docstring Conventions

## Learning Python Style 

There are a lot of rules in PEP 8 and 257! Learn and document in steps.

The key is to use formatters and validators to ensure PEP 8 compliance. As your code is put through validators, you slowly learn all the intricate details of styling.

## Examples 

### Example Module 

:::: 
::: 
``` 
   1 """Short description of module.
   2 
   3 Blah blah blah. This is the long description of the module. More brief
   4 explanations.
   5 
   6 ClassNameA --  short description
   7 function_a --  short description
   8 function_b --  short description
   9 """
  10 
  11 import sys  # standard library imports
  12 import os
  13 
  14 import optparse  # related major package imports
  15 
  16 import eggs  # application specific imports
  17 import spam
  18 
  19 
  20 class ClassNameA:
  21     """What it is.
  22 
  23     Notes on what it is and how it does it.
  24 
  25     Lots to say, lots to say.  I'm unclear on whether we need two spaces
  26     between sentences or not.  72 characters wide.  Blah blah blah.
  27 
  28     Document methods in here, with a short explanation.
  29 
  30     eat_eggs --  does X
  31     eat_spam --  does Y
  32     """
  33 
  34     def __init__(self, green_eggs, green_spam):
  35         """Init ClassNameA with some eggs and spam."""
  36         foo()
  37         bar()
  38         baz()
  39 
  40     def eat_eggs(self):
  41         """One line documentation is like this."""
  42         foo()
  43         bar()
  44 
  45     def eat_spam(self):
  46         """Short explanation.
  47 
  48         Multi-line spam has a one line description at top, seperated by
  49         a space, and then more multi-line spam afterwards.  Note that
  50         the final triple-quote appears beneath.
  51         """
  52         baz()
  53 
  54     def _internal_use(self):
  55         # Eat eggs and spam.
  56         #
  57         # Docstrings are not necessary for non-public methods, but you
  58         # should have a comment that describes what the method does.
  59         # This comment should appear after the "def" line.
  60 
  61         self.eat_eggs()
  62         self.eat_spam()
  63 
  64 
  65 def function_a(eggs, ham):
  66     """A function_a is a foobar.
  67 
  68     Again, multi-line rules apply in here as well, the same way.  Note
  69     that we have two spaces between module-level class and function
  70     definitions.  That's PEP-8 at work.
  71     """
  72     foo()
  73     bar()
  74     baz()
  75 
  76 
  77 def function_b(eggs, ham):
  78     """A function_b is a foobar.
  79 
  80     Another one.  Still two spaces separating functions and classes.
  81     """
  82     foo()
  83     bar()
  84     baz()
```
:::
::::
