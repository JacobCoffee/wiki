# BiggerTasks

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Contents**

# Jython 2.3 

## Builtins 

yield is always a keyword. **\[done\]**

enumerate() built-in added. **\[done\]**

int() will now return a long instead of raising [OverflowError](./OverflowError.html) if a number is too large.

built-in types support extending slicing syntax.

list.insert() changed to be consistent with negative slice indexing. **\[done\]**

list.index() takes optional start, stop arguments. **\[done\]**

Dictionaries gained a pop() method and .fromkeys() class method. **\[done\]**

dict() constructor takes keyword arguments. **\[done. also applied in 2.2\]**

assert no longer checks [debug] flag.

Many type objects are now callable. **\[possibly done\]**

## PEPs 

[PEP 218](http://www.python.org/dev/peps/pep-0218/): A Standard Set Datatype

[PEP 263](http://www.python.org/dev/peps/pep-0263): Defining Python Source Code Encodings

[PEP 273](http://www.python.org/dev/peps/pep-0273): Importing Modules from Zip Archives **\[done\]**

[PEP 278](http://www.python.org/dev/peps/pep-0278): Universal Newline Support **\[done\]**

[PEP 285](http://www.python.org/dev/peps/pep-0285): A Boolean Type

[PEP 307](http://www.python.org/dev/peps/pep-0307): Pickle Enhancements

Reference: [What\'s New in Python 2.3](http://www.python.org/doc/2.3/whatsnew/)

# Jython 2.4 

Built-in set, frozenset

Unifying int/long

Generator expressions

Function/method decorators

Multi-line imports

Reference: [What\'s New in Python 2.4](http://www.python.org/doc/2.4/whatsnew/)

# Jython 2.5 

Conditional expressions

\'with\' statement

Absolute & relative imports

Unified try/except/finally

New generator features

Exceptions as new-style classes

The [index] method

Reference: [What\'s New in Python 2.5](http://www.python.org/doc/2.5/whatsnew/)

# Replace jythonc 

jythonc doesn\'t handle generators and is difficult to debug and improve. The current thinking is to add capabilites to jython itself to generate bytecode from py files and run those statically compiled items rather than jythonc\'s approach of making Java classes that work like the base Python code. See [http://thread.gmane.org/gmane.comp.lang.jython.devel/1429/focus=1430](http://thread.gmane.org/gmane.comp.lang.jython.devel/1429/focus=1430) for the general idea.

# Solidify Import System 

Jython adds to Python\'s import system to handle loading from Java\'s classpath and to load from jar files. It\'s not exactly clear what modifications are in place and what techniques are best for adding jar files to the path at runtime and things like that. An informational JEP explaining what\'s been added and how things relate to both the Python and Jython sides would be nice.

Brett Cannon has been working on rewriting all of Python\'s import machinery in Python; see [http://svn.python.org/view/sandbox/trunk/import_in_py/](http://svn.python.org/view/sandbox/trunk/import_in_py/) for the code.

# Complete Java to Python naming integration 

Java allows a method and field of the same name to exist in the same class. Python only has a single namespace for these items. This leads to methods being hidden in a Java instance in Jython if the instance has a field of the same name. In addition, the bean convenience methods that map object.getField() in Java to object.field in Jython lead to collisions. See [http://thread.gmane.org/gmane.comp.lang.jython.user/4919/](http://thread.gmane.org/gmane.comp.lang.jython.user/4919/) and [http://jython.org/bugs/1509095](http://jython.org/bugs/1509095). A standard system for renaming fields and methods to avoid collisions and a JEP explaining the whole thing would be most welcome.
