# GeneratedDerivedClasses

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Generating the \*Derived classes 

These are notes on the use of `gderived.py`, a tool you need when implementing new types in Jython.

## Background 

Many of the Java classes that implement Python types have a counterpart class with the same name but with \"Derived\" appended. For example `PyString`{.backtick} is paired with `PyStringDerived`{.backtick}, `PyType`{.backtick} with `PyTypeDerived`{.backtick}, and so on. The `*Derived`{.backtick} classes are each a sub-class of their corresponding principal class. They come into play when you create a sub-class (in Python) and override (in Python) one or more methods whose base definition is exposed from the Java implementation. They ensure that this overriding (Python) method is the version invoked, even when the call is from Java.

There are two parts to this remarkable feature. One is in the implementation of the principal class itself, where the static exposed `new`{.backtick} method checks to see whether the actual (Python) type of the object being created is exactly the type that the principal class implements. If it is, then a new instance of the (Java) class is returned. If it is not exactly that class, an instance of the counterpart `*Derived`{.backtick} class is returned.

The second part of the feature is in the `*Derived`{.backtick} class. There, each exposed method may be overridden in a stylised way: it will check for the existence of a (Python) method redefining (the exposed name of) that method. If it fails to find one, it calls the version in the principal class (using the `super`{.backtick} keyword in Java). If it finds a Python re-definition, it invokes that using `PyObject.__call__()`{.backtick}.

The `*Derived`{.backtick} counterpart of each principal class is generated using the script `gderived.py` and a brief specification. The script is in the `src/templates` directory, together with several modules it imports, and it has to be run with that as the current directory. The specification corresponding to each principal class is in the same directory.

One of the imported modules is `gexposed.py`. This used to have a function in its own right, but it is superseded by the exposer (`org.python.expose.generate.Exposer`) and the corresponding Ant task. If you use the new exposer, even if you prohibit sub-classing with `@ExposedType(isBaseType=false)`, it will generate a reference to the sort of class `gderived.py` creates. The modern exposer is described in the article [PythonTypesInJava](PythonTypesInJava).

#### Author\'s note: 

At the time of starting these notes, there is no user guide to `gderived.py` and what it achieves. These notes stem from use of the tool and a certain amount of reverse-engineering. Please improve on them by correcting misunderstandings and omissions.

The work was done on a Windows 7 system, using Python 2.7 (without trying later versions, because of the vintage of the code). The choice of OS shows sometimes in the direction of slashes in pathnames, but that shouldn\'t confuse anyone. Although the motivation was to add a serious Python type (`bytearray`) to Jython, illustrations will be drawn from a facetiously-named type (`piranha`), with a Java implementation in `src/org/python/ethel/the/frog/Piranha.java`.

## gderived.py as a Command 

### The 2-argument Forms 

The most transparent form of the command is:

    python [--lazy] gderived.py <derived-spec> <output-file>

When using `gderived.py` in that way one is working with three user files:

**\<derived-spec\>**, the specification for the contents of the derived Java class. By convention, this has the extension `.derived`, and the Python name of the type being defined. The files for Jython types are in the src/templates folder along with the scripts, but anywhere seems to work with this form of the command, so we\'ll use `src/org/python/ethel/the/frog/piranha.derived` (note lower case type name `piranha`).

**\<output-file\>**, the file in which the generated class will be written. This has to be in the Jython source tree under `src/org/python`. If your code is not there, `gderived.py` seems to run correctly, but will get the Java package statement wrong. You can supply any filename you like, but the class it writes will be named by adding \"`Derived`\" to the name of the input class. For our example the output file is `src/org/python/ethel/the/frog/PiranhaDerived.java`.

And last but not least, **the class file that implements your type**. The input file is identified from the directory of the output file and the class name given in the text of \<derived-spec\> (see below). This therefore also has to be in the Jython source tree under `src/org/python`. For our example the input file is `src/org/python/ethel/the/frog/Piranha.java`.

The **\--lazy** option causes `gderived.py` only to generate the output file if the input file is newer.

### The 1-argument and 0-argument Forms 

A second form of the command is:

    python gderived.py [--lazy] [<derived-spec>]

When using `gderived.py` in that way one is working with the same three user files as above, and a configuration file `src/templates/mappings`. The entries in that file look like this:

    int.derived:org.python.core.PyIntegerDerived
    object.derived:org.python.core.PyObjectDerived
    random.derived:org.python.modules.random.PyRandomDerived
    ast_Assert.derived:org.python.antlr.ast.AssertDerived

In effect, this file allows `gderived.py` to look up the second argument given the first, although this second argument is now given in dotted notation. In this form, the specification file `<name>.derived` has to be in `src/templates` and the input and output classes will be found relative to `src`.

Finally, the \<derived-spec\> argument is optional. In the zero-argument form, `gderived.py` will process all of the entries in `src/templates/mappings`. It is essentially this form, with the \--lazy option, that implements the `template` Ant target in `build.xml`.

## The Specification file \<name\>.derived 

### Available Directives 

base_class

:   Define the name of the input class. **Do not qualify the class name with the package**: the script will work it out from the output file path, relative to `src`. E.g. `base_class: Piranha`

want_dict
:   Request creation of a dictionary in the derived class. If not specified, only a slots array is created.

require

:   \

define

:   \

ctr

:   arguments to the constructor, after the `subtype`{.backtick} argument. For example, in `_json.Scanner.derived`{.backtick} we have `ctr: PyObject context`{.backtick}, and this leads to the constructor `ScannerDerived(PyType subtype, PyObject context)`{.backtick} which calls `super(subtype, context)`{.backtick}

incl
:   Include all the methods from this base class,

unary1

:   \

binary

:   \

ibinary

:   \

no_toString: \[true\|false\]

:   If the parameter is **false** or the directive is not present, generated class will be given a custom `toString()` method that invokes `__repr__`{.backtick}. If **true**, or the directive is given without a parameter, the generated class will **not** be given a custom `toString()` method. Use this when you already have a satisfactory one in the base.

rest:
:   The rest of the file is Java code to insert (pretty much verbatim) into the derived class. Use this to provide your own custom overriding methods.

### Related Templates in gderived-defs 

## Examples of Use 

### Minimal Case 

#### Input Piranha.java 

Here is an example of a type defined in Java for access as a built-in in Jython. For information on the annotations and structure see [PythonTypesInJava](PythonTypesInJava).

:::: 
::: 
``` 
   1 package org.python.ethel.the.frog;
   2 
   3 import org.python.core.PyObject;
   4 import org.python.core.PyString;
   5 import org.python.core.PyType;
   6 import org.python.expose.ExposedMethod;
   7 import org.python.expose.ExposedNew;
   8 import org.python.expose.ExposedType;
   9 
  10 @ExposedType(name="piranha")
  11 public class Piranha extends PyObject {
  12 
  13     public static final PyType TYPE = PyType.fromClass(Piranha.class);
  14 
  15     public Piranha() { this(TYPE); }
  16 
  17     public Piranha(PyType subType) { super(subType); }
  18 
  19     @ExposedNew
  20     final void newPiranha(PyObject[] args, String[] keywords) {}
  21 
  22     @ExposedMethod(names={"theOperation", "theOtherOperation"})
  23     public int operation(int payment) { return payment*2; }
  24 }
```
:::
::::

#### Specification piranha.derived 

    base_class: Piranha

#### Output PiranhaDerived.java 

The command

    python gderived.py piranha.derived  ../org/python/ethel/the/frog/PiranhaDerived.java

issued with current directory `src/templates` produces

:::: 
::: 
``` 
   1 /* Generated file, do not modify.  See jython/src/templates/gderived.py. */
   2 package org.python.ethel.the.frog;
   3 
   4 import java.io.Serializable;
   5 import org.python.core.*;
   6 
   7 public class PiranhaDerived extends Piranha implements Slotted {
   8 
   9     public PyObject getSlot(int index) {
  10         return slots[index];
  11     }
  12 
  13     public void setSlot(int index,PyObject value) {
  14         slots[index]=value;
  15     }
  16 
  17     private PyObject[]slots;
  18 
  19     public String toString() {
  20         PyType self_type=getType();
  21         PyObject impl=self_type.lookup("__repr__");
  22         if (impl!=null) {
  23             PyObject res=impl.__get__(this,self_type).__call__();
  24             if (!(res instanceof PyString))
  25                 throw Py.TypeError(
  26                     "__repr__ returned non-string (type "+
  27                     res.getType().fastGetName()+")");
  28             return((PyString)res).toString();
  29         }
  30         return super.toString();
  31     }
  32 
  33 }
```
:::
::::

### Additional Features 

#### Input Piranha.java 

#### Specification piranha.derived 

#### Output PiranhaDerived.java 
