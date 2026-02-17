# NewUsersGuide

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Jython User Guide

::: 
Table of Contents

- [Intro](#intro)
  - [General Python Documentation](#general-python-documentation)
  - [Other Useful Links](#other-useful-links)
- [Invoking the Jython Interpreter](#invoking-the-jython-interpreter)
  - [Making Jython Scripts Executable](#making-jython-scripts-executable)
- [The Jython Registry](#the-jython-registry)
  - [Registry Properties](#registry-properties)
  - [Finding the Registry File](#finding-the-registry-file)
- [Interaction with Java Packages](#interaction-with-java-packages)
  - [Accessing Java from Jython](#accessing-java-from-jython)
  - [More Details](#more-details)
  - [Importing](#importing)
  - [Creating Class Instances](#creating-class-instances)
  - [Calling Java Methods and Functions](#calling-java-methods-and-functions)
  - [Overloaded Java Method Signatures](#overloaded-java-method-signatures)
  - [Naming Conflicts with Python Keywords](#naming-conflicts-with-python-keywords)
- [JavaBean Properties](#javabean-properties)
  - [Properties](#properties)
  - [Tuples](#tuples)
  - [Event Properties](#event-properties)
  - [Methods, Properties and Event Properties](#methods-properties-and-event-properties)
- [Java Arrays](#java-arrays)
- [Subclassing Java Classes in Jython](#subclassing-java-classes-in-jython)
  - [A Short Example](#a-short-example)
  - [Calling Methods in Your Superclass](#calling-methods-in-your-superclass)
  - [Example](#example)
  - [Example Continued](#example-continued)
  - [Invoking Your Superclass\'s Constructor](#invoking-your-superclass-s-constructor)
  - [Example](#id1)
- [Embedding Jython](#embedding-jython)
- [Java Reload (experimental) simple Support - JReload](#java-reload-experimental-simple-support-jreload)
  - [Example](#id2)
  - [Java Classes Unloading](#java-classes-unloading)
  - [Java 1.1](#java-1-1)
  - [JReload Example Source Files](#jreload-example-source-files)
- [Database connectivity in Jython](#database-connectivity-in-jython)
  - [Using a DataSource (or ConnectionPooledDataSource)](#using-a-datasource-or-connectionpooleddatasource)
  - [Using a JNDI lookup](#using-a-jndi-lookup)
  - [Getting a Cursor](#getting-a-cursor)
    - [SQL Server](#sql-server)
    - [Oracle](#oracle)
  - [Datatype mapping callbacks through DataHandler](#datatype-mapping-callbacks-through-datahandler)
    - [life cycle](#life-cycle)
    - [developer support](#developer-support)
    - [binding prepared statements](#binding-prepared-statements)
    - [building results](#building-results)
    - [callable statement support](#callable-statement-support)
  - [dbexts](#dbexts)
  - [Configuration file](#configuration-file)
  - [API](#api)
  - [Example session](#example-session)
:::

::::: 
### [Intro](#id3)

For a look at the Jython internal API see the generated [JavaDoc documentation](http://www.jython.org/docs/javadoc/index.html)

::: 
#### [General Python Documentation](#id4)

Since Jython is an implementation of Python for the JVM, most of the standard Python documentation applies. Look in the following places for general information:

- The [Python Tutorial](http://www.python.org/doc/tut/tut.html) (start here)
- The [Python Library Reference](http://www.python.org/doc/lib/lib.html). Although many of these modules are not yet implemented (those coded in C for CPython must be re-implemented in Java for Jython), those that are implemented follow the library reference as closely as possible.
- The [Python Language Reference](http://www.python.org/doc/current/ref/ref.html) (for language lawyers).
:::

::: 
#### [Other Useful Links](#id5)

- Jython and CPython are two different implementations of the same language. There are naturally some differences between the two implementations, sometimes reflecting undefined aspects of the Python language, sometimes reflecting quirks of the independent implementations.
- The [Jython FAQ](http://www.jython.org/Project/userfaq.html) may already contain the answer to your question.
- If it doesn\'t, then check [Jython-users mailing list archives](http://sourceforge.net/mailarchive/forum.php?forum_id=5586).
- If you are still stuck you can post a question to the [Jython-users mailing list](http://lists.sourceforge.net/lists/listinfo/jython-users)
:::
:::::

::::: 
### [Invoking the Jython Interpreter](#id6)

Jython is invoked using the \"jython\" script, a short script that invokes your local JVM, sets the Java property install.path to an appropriate value, and then runs the Java classfile org.python.util.jython.

jython \[options\] \[-jar jar \| -c cmd \| file \| -\] \[args\]

options
:   -i: Inspect interactively after running script; force prompts even if stdin is not a terminal. -S: Do not imply import site on initialization -Dprop=\[value\]: Set the jython property prop to value.

-jar jar
:   the program to run is read from the \_\_run\_\_.py file in the specified jar file

  ---------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------
  [[-c `cmd`{.variable}]]   program to run is passed in as the cmd string. This option terminates the options list file run file as the program script file
  ---------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------

- 

  program is read from standard-in (default; interactive mode is used if on a tty). This flag allows you to pipe a file into Jython and have it be treated correctly. For example:
  :   filter file \| jython -

args
:   arguments passed to the program in sys.argv\[1:\]

  ------------------------------- --------------------------------------
  [[\--help]]      print a usage message and exit
  [[\--version]]   print Jython version number and exit
  ------------------------------- --------------------------------------

:::: 
#### [Making Jython Scripts Executable](#id7)

To make a jython \".py\" file executable on a Unix system:

- Make sure that jython is on your standard PATH.
- Make the \".py\" file executable. Typically, this is done with the command chmod +x foo.py
- Add the following line to the top of the file:

#! /usr/bin/env jython

::: 
Note

\"#! \<\...\>/jython\" will generally not work to make your script executable. This is because \"jython\" is itself a script, and #! requires that the file to execute is a binary executable on most Unix variants. Using \"/usr/bin/env\" will get around this problem - and make your scripts more portable in the bargain.
:::
::::
:::::

::::: 
### [The Jython Registry](#id8)

Because there is no good platform-independent equivalent of the Windows Registry or Unix environment variables, Java has its own environment variable namespace. Jython aquires its namespace from the following sources (later sources override defaults found in earlier places):

- The Java system properties, typically passed in on the command line as options to the java interpreter.
- The Jython \"registry\" file, containing prop=value pairs. See below for the algorithm Jython uses to find the registry file.
- The user\'s personal registry file, containing similarly formated prop/value pairs. The user\'s registry file can be found at \"user.home\"+\"/.jython\"
- Jython properties specified on the command line as options to the jython class. See the -D option to the interpreter.

::: 
#### [Registry Properties](#id9)

The following properties are recognized by Jython. There may be others that aren\'t documented here; consult the comments in registry file for details.

python.path
:   Equivalent to CPython\'s PYTHONPATH environment variable

python.cachedir
:   The directory to use for caches - currently just package information. This directory must be writable by the user. If the directory is an absolute path, it is used as given, otherwise it is interpreted as relative to sys.prefix.

python.verbose
:   Sets the verbosity level for varying degrees of informative messages. Valid values in order of increasing verbosity are \"error\", \"warning\", \"message\", \"comment\", \"debug\"

python.security.respectJavaAccessibility
:   Normally, Jython can only provide access to public members of classes. However if this property is set to false and you are using Java 1.2 then Jython can access non-public fields, methods, and constructors.

python.jythonc.compiler
:   The Java compiler to use with the jythonc tool, which now generates Java source code. This should be the absolute path to a Java compiler, or the name of a compiler on your standard PATH.

python.jythonc.classpath
:   Extensions to the standard java.class.path property for use with jythonc. This is useful if you use Jikes as your compiler.

python.jythonc.compileropts
:   Options to pass to the Java compiler when using jythonc.

python.console
:   The name of a console class. An alternative console class that supports GNU readline can be installed with this property. Jython already include such a console class and it can be enabled by setting this property to org.python.util.ReadlineConsole

python.console.readlinelib
:   Allow a choice of backing implementation for GNU readline support. Can be either GnuReadline or Editline. This property is only used when python.console is set to org.python.util.ReadlineConsole.
:::

::: 
#### [Finding the Registry File](#id10)

To find the Jython registry file and set the Python values for sys.prefix, you must first locate a root directory.

- If a \"python.home\" exists, it is used as the root directory by default.
- If \"python.home\" does not exist, \"install.root\" is used.
- If neither of these exist, then Jython searches for the file \"jython.jar\" on the Java classpath, as defined in the system property java.class.path. (The actual file system isn\'t searched, only the paths defined on the classpath and one of them must literally include \"jython.jar\").

Once the root directory is found, sys.prefix and sys.exec_prefix are set to this, and sys.path has rootdir/Lib appended to it. The registry file used is then rootdir/registry.
:::
:::::

::::::::::: 
### [Interaction with Java Packages](#id11)

Most Jython applications will want to use the vast array of Java packages available. The following documentation helps you work with Java packages.

- Working with JavaBean properties, making all Java classes easier to use from Python.
- Special care is necessary to build and use Java arrays from Python.
- This document describes how to subclass Java classes in Python.
- The [jythonc](./jythonc(2e)html.html) utility compiles Python source code to real Java classes, and is used for building applets, servlets, beans, etc.
- Unloading of java classes and internalTablesImpl option.
- Reloading java classes.

::: 
#### [Accessing Java from Jython](#id12)

One of the goals of Jython is to make it as simple as possible to use existing Java libraries from Python. Example

The following example of an interactive session with Jython shows how a user could create an instance of the Java random number class (found in java.util.Random) and then interact with that instance.

    C:\jython>jython
    Jython 2.0 on java1.2.1
    Type "copyright", "credits" or "license" for more information.
    >>> from java.util import Random
    >>> r = Random()
    >>> r.nextInt()
    -790940041
    >>> for i in range(5):
    ...     print r.nextDouble()
    ...
    0.23347681506123852
    0.8526595592189546
    0.3647833839988137
    0.3384865260567278
    0.5514469740469587
    >>>
:::

::: 
#### [More Details](#id13)

Hopefully, this example should make it clear that there are very few differences between using Java packages and using Python packages when working under Jython. There are a few things to keep in mind.
:::

::: 
#### [Importing](#id14)

    Jython 2.0 on java1.2.1
    Type "copyright", "credits" or "license" for more information.
    >>> from java.util import *
    >>> Random
    <jclass java.util.Random at 31702169>
    >>> Hashtable
    <jclass java.util.Hashtable at 7538094>
    >>>
:::

::: 
#### [Creating Class Instances](#id15)

You can create an instance of a Java class exactly the way you would create an instance of a Python class. You must \"call\" the class with a set of arguments that is appropriate for one of the Java class\'s constructors. See the section below for more details on what constitutes appropriate arguments.
:::

::: 
#### [Calling Java Methods and Functions](#id16)

Java classes have both static and instance methods this makes them behave much like a cross between a Python module and class. As a user, you should rarely need to be concerned with this difference.

Java methods and functions are called just exactly like their Python counterparts. There is some automatic type coercion that goes on both for the types being passed in and for the value returned by the method. The following table shows how Python objects are coerced to Java objects when passed as arguments in a function call. The Java Types show the expected Java type for the argument, and the Allowed Python Types shows what Python objects can be converted to the given Java type. Notice the special behavior of String\'s when a java.lang.Object is expected. This behavior might change if it is shown to cause problems.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  Java Types                             Allowed Python Types
  -------------------------------------- --------------------------------------------------------------------------------------------------------------------------
  char                                   String (must have length 1)

  boolean                                Integer (true = nonzero)

  byte, short, int, long                 Integer

  float, double                          Float

  java.lang.String, byte\[\], char\[\]   String

  java.lang.Class Class or JavaClass     (only if class subclasses from exactly one Java class; mutiple inheritance from more than one Java class is now illegal)

  Foo\[\]                                Array (must contain objects of class or subclass of Foo)

  java.lang.Object                       String-\>java.lang.String, all others unchanged

  org.python.core.PyObject               All unchanged

  Foo                                    Instance-\>Foo (if Instance is subclass of Foo); JavaInstance -\> Foo (if JavaInstance is instance of Foo or subclass)
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------

Returned values from a Java method are also possibly coerced back to an object that is more readily usable in Python. The following table shows those coercions.

  -------------------------------------------------------------------------------------------------
  Java Type                                Returned Python Type
  ---------------------------------------- --------------------------------------------------------
  char                                     String (of length 1)

  boolean                                  Integer (true = 1, false = 0)

  byte, short, int, long                   Integer

  float, double                            Float

  java.lang.String                         String

  java.lang.Class                          JavaClass which represents given Java class

  Foo\[\]                                  Array (containing objects of class or subclass of Foo)

  org.python.core.PyObject (or subclass)   Unchanged

  Foo                                      JavaInstance which represents the Java Class Foo
  -------------------------------------------------------------------------------------------------
:::

:::: 
#### [Overloaded Java Method Signatures](#id17)

Java methods are allowed to be overloaded for different signatures (types and number of arguments). When different versions of the method differ in the number of arguments that they expect, the appropriate method can be easily determined from the number of arguments passed to the method.

When the difference is instead in the types of the arguments, more work is required. The possible signatures are sorted in a consistent order that should ensure the appropriate method is chosen first. TBD: document this order!

If you need to call a Java method with a particular signature and this is not happening in the easy way, you can use the following workaround:

Assume that foo has two methods, \"void foo(int x); void foo(byte x);\". To call the second method you could write the following:

    from java.lang import Byte
    foo(Byte(10))

I\'m not convinced that any better solution to this problem is possible.

::: 
Note

Look into IronPython\'s solution to this for ideas.
:::
::::

::: 
#### [Naming Conflicts with Python Keywords](#id18)

Because Java has a different set of keywords than Python, there are many Java classes that have method and function names that conflict with Python\'s keyword set. Where the intent can be unambiguously determined, no identifier mangling is necessary, such as when keywords are used as attributes on objects. Thus you can naturally write:

> java.lang.System.out.print(\"hi\")

or

> java.lang.Runtime.getRuntime().exec(cmd)

In the rare case where the conflict can\'t be resolved due to Python\'s grammar, you should modify the reserved word by appended an underscore to the end of it, e.g. print\_
:::
:::::::::::

::::::: 
### [JavaBean Properties](#id19)

::: 
#### [Properties](#id20)

Jython uses JavaBean properties to make it easier to interact with most Java classes. These properties can be used as normal object attributes, and can also be specified to the class constructor as keyword arguments (this idea is stolen from TkInter where it seems to work extremely well).

These properties are generated automatically using the JavaBean Introspector which identifies properties either from common design patterns, or from explicitly specified BeanInfo.

As a first example, consider the case where you wish to create a button that is disabled.

The first example shows how you would do this in the typical Java fashion:

b = awt.Button() b.setEnabled(0)

The second example shows how enabled can be set as a property:

b = awt.Button() b.enabled = 0

The final example sets this property at instantiation time using a keyword argument:

b = awt.Button(enabled=0)
:::

::: 
#### [Tuples](#id21)

If the value of a property is specified as a tuple, then the property will be created by applying the constructor for the type of the property to the tuple. This is particularly handy for specifying sizes:

frame = awt.Frame(size=(500,100))

It can also be handy for specifying color as an RGB triple:

frame.background = 255,255,0

will set the background color of the frame to yellow.
:::

::: 
#### [Event Properties](#id22)

In standard Java, the event handlers for a widget are specified by passing in an instance of a class that implements the appropriate interface. This is the only reasonable approach to take in a language that doesn\'t have first-class functions. In Jython, for every event listener supported by a class, there will be a property added to the class for each method supplied by the event listener class. These properties can be set to give a function to be called when the appropriate event occurs.

The standard Java style for setting an event listener is shown below:

    class action(awt.event.ActionListener):
        def actionPerformed(self,event):
            java.lang.System.exit(0)

    button = awt.Button("Close Me!")
    button.addActionListener(action())

This can be written in a more Pythonesque (and compact) style by using event properties as follows:

    def exit(event):
        java.lang.System.exit(0)

    button = awt.Button("Close Me!", actionPerformed=exit)
:::

::: 
#### [Methods, Properties and Event Properties](#id23)

Jython have only one namespace for these three class attributes. Java can be seen as having a unique namespace for each of the three types. As a consequense, there can be conflicts between methods, properties and event properties. These conflicts are resolved so that:

> properties \< event-properties \< fields \< methods

This means that a method will override a field with the same name. Some carefull handling of properties and static fields allow for the existence of, and access to, both an instance property and a static field with the same name.
:::
:::::::

::: 
### [Java Arrays](#id24)

Java Arrays in Jython - JArray Many Java methods require Java array objects as arguments. The way that these arguments are used means that they must correspond to fixed-length, mutable sequences, sometimes of primitive data types. The PyArray class is added to support these Java arrays and instances of this class will be automatically returned from any Java method call that produces an array. In addition, the \"jarray\" module is provided to allow users of Jython to create these arrays themselves, primarily for the purpose of passing them to a Java method.

The jarray module exports two functions:

array(sequence, type) zeros(length, type)

array will create a new array of the same length as the input sequence and will populate it with the values in sequence. zeros will create a new array of the given length filled with zeros (or null\'s if appropriate).

type can either be a single character typecode (using the same mappings as Python\'s array module) or it can be an instance of a JavaClass object. The valid typecodes are shown in the following table:

  -----------------------------------------------------------------------
  Character Typecode              Corresponding Java Type
  ------------------------------- ---------------------------------------
  z                               boolean

  c                               char

  b                               byte

  h                               short

  i                               int

  l                               long

  f                               float

  d                               double
  -----------------------------------------------------------------------

A quick example:

    from jarray import array
    a = array([ 1 ], 'i')
    print a
    from java.net import URL
    u = URL('http://jython.org')
    b = array([], URL)
    print b

You can use array to create multidimensional arrays from nested lists. The second argument to array determines what type the returned array contains, so in the case of an array of arrays of java.lang.Strings, the second argument is the class instance that represents the String\[\] type:

    nestedList = [ ['hi', 'there'], ['silly', 'person'] ]
    containedType = java.lang.Class.forName('[Ljava.lang.String;')
    multiArray = array(nestedList, containedType)
    # multiArray can be passed to Java methods that expect String[][]

(\'\[Ljava.lang.String;\' is the name of the String\[\] class. More information about array class names can be found in the API documentation for Class.forName().)
:::

::::::::: 
### [Subclassing Java Classes in Jython](#id25)

::: 
#### [A Short Example](#id26)

The example below should both demonstrate how this subclassing is performed and why it is useful. At first glance, the code looks exactly like subclassing any other Python class. The key difference in this example is that awt.event.ActionListener is a Java class, not a Python one. In the 4th line from the end, \"b.addListener(SpamListener())\", a Java method is being called that requires an instance of the Java class ActionListener. By providing a Python subclass of this Java class, everybody is happy.

    from java import awt

    class SpamListener(awt.event.ActionListener):
        def actionPerformed(self,event):
            if event.getActionCommand() == "Spam":
            print 'Spam and eggs!'

    f = awt.Frame("Subclassing Example")
    b = awt.Button("Spam")
    b.addActionListener(SpamListener())
    f.add(b, "Center")
    f.pack()
    f.setVisible(1)

Note: This example can be accomplished much more elegantly by using JavaBeans properties (and event properties).
:::

::: 
#### [Calling Methods in Your Superclass](#id27)

In Python, if I want to call the foo method in my superclass, I use the form:

    SuperClass.foo(self)

This works with the majority of methods, but protected methods cannot be called from subclasses in this way. Instead you have to use the \"self.super\_\_foo()\" call style.
:::

::: 
#### [Example](#id28)

The following example shows how the java.io.InputStream class can be effectively subclassed. What makes this class difficult is that the read method is overloaded for three different method signatures:

1.  abstract int read()
2.  int read(byte\[\])
3.  int read(byte\[\], int, int)

The first one of these methods must be overridden in a subclass. The other two versions can be ignored. Unfortunately, Python has no notion of method overloading based on type signatures (this might be related to the fact that Python doesn\'t have type signatures ;-) In order to implement a subclass of java.io.InputStream that overrides the \"read\" method, a Python method must be implemented that handles all three possible cases. The example below shows the easiest way to acheive this:

    from java.io import InputStream

    class InfiniteOnes(InputStream):
        def read(self, *args):
            if len(args) > 0:
            # int read(byte[])
            # int read(byte[], int, int)
                return apply(InputStream.read, (self,)+args)
            return 1

    io = InfiniteOnes()

    for i in range(10):
        print io.read(),
    print
:::

::: 
#### [Example Continued](#id29)

To continue the example above, this new instance of java.io.InputStream can be passed to any Java method that expects an InputStream as shown below:

    from java.io import DataInputStream

    dp = DataInputStream(io)
    dp.skipBytes(1000)
    print dp.readByte()
    print dp.readShort()
    print dp.readInt()
:::

::: 
#### [Invoking Your Superclass\'s Constructor](#id30)

You can explictly invoke your superclass\'s constructor using the standard Python syntax of explictly calling the \"\_\_init\_\_\" method on the superclass and passing in \"self\" as the first argument. If you wish to call your superclass\'s constructor, you must do so within your own \"\_\_init\_\_\" method. When your \"\_\_init\_\_\" method finishes, if your Java superclasses have not yet been explicitly initialized, their empty constructors will be called at this point.

It\'s important to realize that your superclass is not initialized until you either explictly call it\'s \"\_\_init\_\_\" method, or your own \"\_\_init\_\_\" method terminates. You must do one of these two things before accessing any methods in your superclass.
:::

::: 
#### [Example](#id31)

    from java.util import Random

    class rand(Random):
        def __init__(self, multiplier=1.0, seed=None):
            self.multiplier = multiplier
            if seed is None:
                Random.__init__(self)
            else:
                Random.__init__(self, seed)

        def nextDouble(self):
            return Random.nextDouble(self) * self.multiplier

    r = rand(100, 23)

    for i in range(10):
        print r.nextDouble()

This example shows how the superclass\'s constructor can be effectively called in order to explictly choose a non-empty version.
:::
:::::::::

::: 
### [Embedding Jython](#id32)

There are two options for embedding Jython in a Java application. You can make a real Java class out of a Python class, and then call it from your Java code, as previously described, or you can use the PythonInterpreter object

Information on the PythonInterpreter can be found in the JavaDoc documentation for [org.python.util.PythonInterpreter](http://www.jython.org/docs/javadoc/org/python/util/PythonInterpreter.html).

The following example demonstrates how to use the PythonInterpreter to execute a simple Python program.

The python program:

    import sys
    print sys
    a=42
    print a
    x=2+2
    print "x:",x

The java code required to execute the python program:

    import org.python.util.PythonInterpreter;
    import org.python.core.*;

    public class SimpleEmbedded {
        public static void main(String []args)
            throws PyException
        {
            PythonInterpreter interp =
                new PythonInterpreter();

            System.out.println("Hello, brave new world");
            interp.exec("import sys");
            interp.exec("print sys");

            interp.set("a", new PyInteger(42));
            interp.exec("print a");
            interp.exec("x = 2+2");
            PyObject x = interp.get("x");

            System.out.println("x: "+x);
            System.out.println("Goodbye, cruel world");
        }
    }
:::

::::::::::: 
### [Java Reload (experimental) simple Support - JReload](#id33)

Introduction and usage, plus some notes on java classes unloading and internalTablesImpl option

The \"jreload\" module is not the definitive word about java classes reloading under jython. It is still experimental and its interface may improve or change to become more pythonic.

\"jreload\" cannot cover all the possible reload-flavors, and its goal is to offer a simple interface for the most common cases, e.g. quick trial-and-error experimenting.

Java classes reloading in jython is not enabled by \"jreload\", some of the modifications occurred to jython run-time have made it possible. Now jython can deal with java classes with the same name (without clashes) and run-time supports unloading of java classes by different ways, which is a must feature for some uses of reloading

\[The expert user can now play directly with class-loaders and reloading as he would from java.\]

The main idea of the \"jreload\" interface is that of a load-set. A load-set is a package-like object that can host a complete hierarchy of java packages, which can be reloaded as a whole.

Why there is no support for reloading a single class? Java classes are loaded through class-loaders, actually there is no support in java to redefine an already loaded class through its class-loader. In order to reload a class one should create a new class-loader, but classes from different class-loaders cannot interoperate, so we need to reload all related classes through the new class-loader. Note: The normal python reload built-in does nothing for java classes and simply returns the old version.

The \"jreload\" module exports the following functions:

    makeLoadSet(name, path)
    reload(loadSet)

makeLoadSet creates and returns a new load-set with the given name. The created load-set will behave like a package and import statement related to it can be issued. name should be a valid python identifier like any python module name and should not clash with any module that has been or will be imported. Internally the created load-set will be added to sys.modules, the same way it happens to modules on import. You can issue the same makeLoadSet from many places, it is idempotent like modules imports are.

path should be a list of directory or jar paths. The created load-set will enable importing the classes present there. path should be disjoint from both sys.path and java classpath, otherwise one can get very confusing results.

For example: if a load-set \'X\' is created and its hierarchy contains java packages \'p\' and \'p.q\', then the following references can be used in import statements: \'X\', \'X.p\', \'X.p.q\'.

reload(loadSet) reloads all the classes in the package hierarchy hosted by loadSet and returns loadSet.

::: 
Note

The current version of \"jreload\" (jreload.\_\_version\_\_==\'0.3\') does not support removing or substituting jars on the fly.
:::

::::: 
#### [Example](#id34)

The following example should help make things clearer: (its files should be present in the jython Demo dir) \# Demo/jreload/example.jar contains example.Version (source) and example.PrintVer (source) \# Demo/jreload/\_xample contains a slightly modified version of example.Version (source)

    >>> import sys
    >>> import os
    >>> import jreload
    >>> def xp(name): return os.path.join(sys.prefix,'Demo/jreload/'+name)
    # builds a path under 'Demo/jreload'
    ...
    >>> X=jreload.makeLoadSet('X',[xp('.'),xp('example.jar')])
    >>> from X import example
    >>> dir(example)
    ['PrintVer', 'Version', '__name__']
    >>> X.example.Version
    <jclass example.Version at 6781345>
    >>> from X.example import * # works but in general import * from java
    pkgs is not for production code
    >>> v=Version(1)
    >>> PrintVer.print(v)
    version 1
    >>> os.rename(xp('_xample'),xp('example')) # _xample becomes example,
    hiding and "patching" jar contents
    >>> jreload.reload(X) # (re)loads example dir example.Version and
    jar example.PrintVer
    <java load-set X>
    >>> nv2=example.Version(2)
    >>> example.PrintVer.print(nv2)
    new version 2
    >>> PrintVer.print(nv2)
    Traceback (innermost last):
      File "<console>", line 1, in ?
    TypeError: print(): 1st arg can't be coerced to example.Version
    >>> example.PrintVer.print(v)
    Traceback (innermost last):
      File "<console>", line 1, in ?
    TypeError: print(): 1st arg can't be coerced to example.Version
    >>> os.rename(xp('example'),xp('_xample'))

::: 
Note

Differently from python packages reload, load-sets reload the complete hosted hierarchy.
:::

::: 
Note

Class versions across reloads are not interoperable.
:::

Like for python classes and python reload, old versions are kept around, if there are still references to them. But what happens if they are no longer used?
:::::

::: 
#### [Java Classes Unloading](#id35)

One would expect that no longer referenced java classes would be unloaded, but the situation is not that simple.

In order to give a python-class-like view on python side and for implementation reasons jython wraps java classes (in instances of org.python.core.PyJavaClass). Clearly the mapping from java classes to their wrapped version should be unique (e.g. to guarantee == and \'is\' semantic). So jython keeps this mapping in an internal table. This is also good because building the wrappers is expensive.

Note: Typically one should care about java classes unloading only for very dynamic applications, like IDEs or long-running apps, that would go out memory if old versions of reloaded classes would not be collected.

Clearly the entries somehow block unloading. On the other hand java classes unloading is just a memory consumption optimization (and as such is it presented in Java Language Specification). Actual jvms clearly support this. JPython simply kept the entries in the table forever but Jython and \"jreload\" try to make unloading possible.

Note: java never unloads system classes (java.\* etc) nor classes from classpath. Further Jython cannot unload sys.path java classes. So the whole unload issue makes sense only with \"jreload\" or custom class-loaders. Java 2 and jython internalTablesImpl option

Under java2 jython offers table implementations that exploit soft/weak references in order to discard entries (when this is OK) for unloading.

A possible policy would be to keep an entry as long as the corresponding java class is still referenced outside the table (both by java or jython code). But this one cannot be implemented. \[Tech.: One cannot add fields to final java class java.lang.Class!\] So entries are kept as long as the wrapped version is still in use. These implementations can be chosen trough python.options.internalTablesImpl registry option. Note: they only influence classes unloading, there is no need and reason to use them, unless one depends on class unloading to avoid memory leakage.

internalTablesImpl = weak \-- Sets implementation using weak-refs. Table entries for not referenced (outside the table) wrapped versions are \"discarded\" at garbage collection points. If a class or some of its instances are continuously passed from java to jython side, but no long-living reference to it is kept from jython side, this can imply a performance penalty (rebuilding the wrapped version is expensive). On the other hand this is a good setting for testing if unloading actually happens or some references hunting around prevent it.

\[Note: With jdk 1.3 java -verbose:class can help tracking class unloads, and System.gc forces class unloading. With jdk 1.2 java -verbose:gc should give some information on class unloading, but unloading of classes happen at unpredictable points and System.gc does not trigger it. Also weak-refs allow testing for unloading and gc.\]

internalTablesImpl = soft \--Sets implementation using soft-refs. Table entries for not referenced (outside the table) wrapped versions are \"discarded\" on memory shortage, given soft-reference definition. Soft-references behavior is not specified in full details, so the actual behavior will depend on the concrete jvm. But if actual (jvm) implementations are not too bad, this should be a good setting for production code, which relies on unloading to avoid out of memory failures.
:::

:::: 
#### [Java 1.1](#id36)

To be honest the unloading support that jython can offer under java 1.1 (given the absence of weak/soft-refs) is error-prone and anything serious would require \"too much\" caution, but this should not be a real issue. Support is offered only for \"jreload\" needs, in these forms:

\# Before reload(X) one can issue X.unload(). X.unload() discards all the entries for the old versions of the classes in X. This is safe only if all python subclasses and all instances of them have been destroyed. \# One can \"extract\" the information needed in order to discard the entries for the versions actually present in X at a later point (after a whole series of reloads):

> u_t1=X.unload \# extract unload info for time t1 versions \... reloads \... u_t1() \# discard entries for time t1 versions

u_t1() is safe only if at that point all subclasses/instances of the involved versions have been destroyed.

::: 
Note

these idioms work also with the standard internal tables implementation under java2, and for compatibility even with the weak/soft implementations.
:::
::::

::: 
#### [JReload Example Source Files](#id37)

Jar example.Version

    package example;

    public class Version {

     private int ver;

     public Version(int ver) {
      this.ver = ver;
     }

     public String toString() {
       return "version "+ver;
     }

    }

example.PrintVer

    package example;

    public class PrintVer {

     static public void print(Version ver) {
      System.out.println(ver);
     }

    }

New example.Version

    package example;

    public class Version {

     private int ver;

     public Version(int ver) {
      this.ver = ver;
     }

     public String toString() {
       return "new version "+ver;
     }

    }
:::
:::::::::::

::::::::::::::::::: 
### [Database connectivity in Jython](#id38)

The zxJDBC package provides a nearly 100% Python DB API 2.0 compliant interface for database connectivity in Jython. It is implemented entirely in Java and makes use of the JDBC API. This means any database capable of being accessed through JDBC, either directly or using the JDBC-ODBC bridge, can be manipulated using zxJDBC. Getting a Connection

First, make sure a valid JDBC driver is in your classpath. Then start Jython and import the zxJDBC connection factory. Using a Driver

The most common way to establish a connection is through a Driver. Simply supply the database, username, password and JDBC driver classname to the connect method. If your driver requires special arguments, pass them into the connect method as standard Python keyword arguments. You will be returned a connection object.

    Jython 2.1b1 on java1.4.0-beta3 (JIT: null)
    Type "copyright", "credits" or "license" for more information.
    >>> from com.ziclix.python.sql import zxJDBC
    >>> d, u, p, v = "jdbc:mysql://localhost/test", None, None,
    "org.gjt.mm.mysql.Driver"
    >>> db = zxJDBC.connect(d, u, p, v)
     optionally
    >>> db = zxJDBC.connect(d, u, p, v, CHARSET='iso_1')
    >>>

::: 
#### [Using a DataSource (or ConnectionPooledDataSource)](#id39)

The only required argument is the fully-qualified classname of the DataSource, all keywords will use JavaBeans reflection to set properties on the DataSource.

    Jython 2.1b1 on java1.4.0-beta3 (JIT: null)
    Type "copyright", "credits" or "license" for more information.
    >>> from com.ziclix.python.sql import zxJDBC
    >>> params = {}
    >>> params['serverName'] = 'localhost'
    >>> params['databaseName'] = 'ziclix'
    >>> params['user'] = None
    >>> params['password'] = None
    >>> params['port'] = 3306
    >>> db = apply(zxJDBC.connectx, ("org.gjt.mm.mysql.MysqlDataSource",),
    params)
    >>>
:::

::: 
#### [Using a JNDI lookup](#id40)

It is possible for zxJDBC to use a Connection found through a JNDI lookup. This is particularly useful in an application server (such as when using PyServlet). The bound object can be either a String, Connection, DataSource or ConnectionPooledDataSource. The lookup will figure out the instance type and access the Connection accordingly,

The only required argument is the JNDI lookup name. All keyword arguments will be converted to their proper Context field value if the keyword matches one of the constants. If a field name does not exist for the keyword, it will passed as declared. The resulting environment will be used to build the InitialContext.

This example uses the simple Sun FileSystem JNDI reference implementation. Please consult the JNDI implementation you intend to use for the InitialContextFactory classname as well as the connection URL.

    Jython 2.1b1 on java1.4.0-beta3 (JIT: null)
    Type "copyright", "credits" or "license" for more information.
    >>> from com.ziclix.python.sql import zxJDBC
    >>> jndiName = "/temp/jdbc/mysqldb"
    >>> factory = "com.sun.jndi.fscontext.RefFSContextFactory"
    >>> db = zxJDBC.lookup(jndiName, INITIAL_CONTEXT_FACTORY=factory)
    >>>
:::

:::::: 
#### [Getting a Cursor](#id41)

In order execute any operation, a cursor is required from the connection. There are two different kinds of cursors: static and dynamic.

The primary difference between the two is the way they manage the underlying ResultSet. In the static version, the entire ResultSet is iterated immediately, the data converted and stored with the cursor and the ResultSet closed. This allows the cursor to know the rowcount (not available otherwise within JDBC) and set the .rowcount attribute properly. The major disadvantage to this approach is the space/time constraints might be extraordinary.

The solution to the problem are dynamic cursors which keep a handle to the open ResultSet and iterate as required. This drastically decreases memory consumption and increases perceived response time because no work is done until asked. The drawback is the .rowcount attribute can never be accurately set.

To execute a query simply provide the SQL expression and call execute. The cursor now has a description attribute detailing the column information. To navigate the result set, call one of the fetch methods and a list of tuples will be returned.

    >>> c = db.cursor()   # this gets a static cursor
     or
    >>> c = db.cursor(1)  # this gets a dynamic cursor
    >>> c.execute("select count(*) c from player")
    >>> c.description
    [('c', 3, 17, None, 15, 0, 1)]
    >>> for a in c.fetchall():
    ...  print a
    ...
    (13569,)
    >>>

When finished, close the connections.

    >>> c.close()
    >>> db.close()
    >>>

To call a stored procedure or function provide the name and any params to callproc. The database engine must support stored procedures. The examples below have been tested with Oracle, SQLServer and Informix. Refer to the Python DP API spec for how OUT and INOUT parameters work.

::: 
Note

The name of the stored procedure can either be a string or tuple. This is NOT portable to other DB API implementations.
:::

::: 
##### [SQL Server](#id42)

``` doctest-block

>>> c = db.cursor() # open the database as in the examples above
>>> c.execute("use northwind")
>>> c.callproc(("northwind", "dbo", "SalesByCategory"), ["Seafood",
"1998"], maxrows=2)
>>> for a in c.description:
...  print a
...
('ProductName', -9, 40, None, None, None, 0)
('TotalPurchase', 3, 17, None, 38, 2, 1)
>>> for a in c.fetchall():
...  print a
...
('Boston Crab Meat', 5318.0)
('Carnarvon Tigers', 8497.0)
>>> c.nextset()
1
>>> print c.fetchall()
[(0,)]
>>> print c.description
[('@RETURN_VALUE', 4, -1, 4, 10, 0, 0)]
>>>
```
:::

::: 
##### [Oracle](#id43)

``` doctest-block

>>> c = db.cursor() # open the database as in the examples above
>>> c.execute("create or replace function funcout (y out varchar2)
return varchar2 is begin y := 'tested'; return 'returned'; end;")
>>> params = [None]
>>> c.callproc("funcout", params)
>>> print params
['tested']
>>> print c.description
[(None, 12.0, -1, None, None, None, 1)]
>>> print c.fetchall()
[('returned',)]
>>>
```

When finished, close the connections.

``` doctest-block

>>> c.close()
>>> db.close()
>>>
```

Standard extensions to the Python DB API

- connection.dbname: Same as DatabaseMetaData.getDatabaseProductName
- connection.dbversion: Same as DatabaseMetaData.getDatabaseProductVersion
- cursor.updatecount: The value obtained from calling Statement.getUpdateCount
- cursor.lastrowid: The value obtained from calling DataHandler.getRowId
- cursor.tables(qualifier,owner,table,type): Same as DatabaseMetaData.getTables
- cursor.columns(qualifier,owner,table,column): Same as DatabaseMetaData.getColumns
- cursor.foreignkeys(primary_qualifier,primary_owner,pimary_table, foreign_qualifier,foreign_owner,foreign_table): Same as DatabaseMetaData.getCrossReference
- cursor.primarykeys(qualifier,owner,table): Same as DatabaseMetaData.getPrimaryKeys
- cursor.procedures(qualifier,owner,procedure): Same as DatabaseMetaData.getProcedures
- cursor.procedurecolumns(qualifier,owner,procedure,column): Same as DatabaseMetaData.getProcedureColumns
- cursor.statistics(qualifier,owner,table,unique,accuracy): Same as DatabaseMetaData.getIndexInfo
:::
::::::

:::::::: 
#### [Datatype mapping callbacks through DataHandler](#id44)

The DataHandler interface has three methods for handling type mappings. They are called at two different times, one when fetching and the other when binding objects for use in a prepared statement. I have chosen this architecture for type binding because I noticed a number of discrepancies in how different JDBC drivers handled database types, in particular the additional types available in later JDBC versions.

::: 
##### [life cycle](#id45)

public void preExecute(Statement stmt) throws SQLException;
:   A callback prior to each execution of the statement. If the statement is a PreparedStatement (created when parameters are sent to the execute method), all the parameters will have been set.

public void postExecute(Statement stmt) throws SQLException;
:   A callback after successfully executing the statement. This is particularly useful for cases such as auto-incrementing columns where the statement knows the inserted value.
:::

::: 
##### [developer support](#id46)

public String getMetaDataName(String name);
:   A callback for determining the proper case of a name used in a DatabaseMetaData method, such as getTables(). This is particularly useful for Oracle which expects all names to be upper case.

public PyObject getRowId(Statement stmt) throws SQLException;
:   A callback for returning the row id of the last insert statement.
:::

::: 
##### [binding prepared statements](#id47)

public Object getJDBCObject(PyObject object, int type);
:   This method is called when a PreparedStatement is created through use of the execute method. When the parameters are being bound to the statement, the DataHandler gets a callback to map the type. This is only called if type bindings are present.

public Object getJDBCObject(PyObject object);
:   This method is called when no type bindings are present during the execution of a PreparedStatement.
:::

::: 
##### [building results](#id48)

public PyObject getPyObject(ResultSet set, int col, int type);
:   This method is called upon fetching data from the database. Given the JDBC type, return the appropriate PyObject subclass from the Java object at column col in the ResultSet set.
:::

::: 
##### [callable statement support](#id49)

    public PyObject getPyObject(CallableStatement stmt, int col, int type)
    throws SQLException;
       This method is called upon fetching data from the database after
       calling a stored procedure or function. Given the JDBC type, return
       the appropriate PyObject subclass from the Java object at column
       col in the CallableStatement.

    public void registerOut(CallableStatement statement, int index, int
    colType, int dataType, String dataTypeName) throws SQLException;
       This method is called to register an OUT or INOUT parameter on the
       stored procedure. The dataType comes from java.sql.Types while the
       dataTypeName is a vendor specific string.

    public String getProcedureName(PyObject catalog, PyObject schema,
    PyObject name);
       This method is called to build a stored procedure's name.

It is simple to use these callbacks to achieve the desired result for your database driver. In the majority of cases nothing needs to be done to get the correct datatype mapping. However, in the cases where drivers differ from the spec or handle values differently, the DataHandler callbacks should provide the solution. Example DataHandler for Informix booleans

One such case where a driver needs a special mapping is Informix booleans. The are represented as the characters \'t\' and \'f\' in the database and have their own type boolean. You can see from the example below, without the special DataHandler, the boolean type mapping fails.

    Jython 2.1b1 on java1.4.0-beta3 (JIT: null)
    Type "copyright", "credits" or "license" for more information.
    >>> from com.ziclix.python.sql import zxJDBC
    >>> zxJDBC.autocommit = 0
    >>> d, u, p, v = "database", "user", "password",
    "com.informix.jdbc.IfxDriver"
    >>> db = zxJDBC.connect(d, u, p, v)
    >>> c = db.cursor()
    >>> c.execute("create table g (a boolean)")
    >>> c.execute("insert into g values (?)", [1])
    Traceback (innermost last):
    File "<console>", line 1, in ?
    Error: No cast from integer to boolean. [SQLCode: -9634]
    >>> from com.ziclix.python.sql.informix import InformixDataHandler
    >>> c.datahandler = InformixDataHandler(c.datahandler)
    >>> c.execute("insert into g values (?)", [1], {0:zxJDBC.OTHER})
    >>>

As you can see, the default handler fails to convert the Python 1 into an Informix boolean because the IfxDriver treats booleans as JDBC type OTHER. The InformixDataHandler is intimately aware of the IfxDriver mappings and understands how to interpret Python values as booleans when the JDBC type is OTHER.

This functionality is also useful in handling the more advanced JDBC 2.0 types CLOB, BLOB and Array.

You can also implement the DataHandler from within Jython as in this simple example:

    >>> class PyHandler(DataHandler):
    >>>  def __init__(self, handler):
    >>>   self.handler = handler
    >>>  def getPyObject(self, set, col, datatype):
    >>>   return self.handler.getPyObject(set, col, datatype)
    >>>  def getJDBCObject(self, object, datatype):
    >>>   print "handling prepared statement"
    >>>   return self.handler.getJDBCObject(object, datatype)
    >>>
    >>> c.datahandler = PyHandler(c.datahandler)
    >>> c.execute("insert into g values (?)", [1])
    handling prepared statement
    >>>
:::
::::::::

::: 
#### [dbexts](#id50)

dbexts is a wrapper around DB API 2.0 compliant database modules. It currently supports zxJDBC and mxODBC but could easily be modified to support others. It allows developers to write scripts without knowledge of the implementation language of Python (either C or Java). It also greatly eases the burden of database coding as much of the functionality of the Python API is exposed through easier to use methods.
:::

::: 
#### [Configuration file](#id51)

dbexts needs a configuration file in order to create a connection. The configuration file has the following format:

\[default\] name=mysql

\[jdbc\] name=mysql url=jdbc:mysql://localhost/ziclix user= pwd= driver=org.gjt.mm.mysql.Driver datahandler=com.ziclix.python.sql.handler.MySQLDataHandler

\[jdbc\] name=ora url=jdbc:oracle:thin:@localhost:1521:ziclix user=ziclix pwd=ziclix driver=oracle.jdbc.driver.OracleDriver datahandler=com.ziclix.python.sql.handler.OracleDataHandler
:::

::: 
#### [API](#id52)

dbexts will default to looking for a file named \'dbexts.ini\' in the same directory as dbexts.py but can optionally be passed a filename to the cfg attribute.

    __init__(self, dbname=None, cfg=None, resultformatter=format_resultset,
    autocommit=1)
       The initialization method for the dbexts class. If dbname is None,
       the default connection, as specified in the cfg file will be used.

    isql(self, sql, params=None, bindings=None, maxrows=None)
       Interactively execute sql statement. If self.verbose is true, then
       the results (if any) are displayed using the result formatting
       method. If maxrows is specified, only maxrows are displayed.

    raw(self, sql, params=None, bindings=None, delim=None, comments=comments)
       Executes the sql statement with params and bindings as
       necessary. Returns a tuple consisting of (headers, results).

    schema(table, full=0, sort=1)
       Displays the schema (indicies, foreign keys, primary keys and
       columns) for the table parameter. If full is true, also compute
       the exported (or referenced) keys. If sort is true (the default),
       sort the column names.

       >>> d.schema("store")
       Table
         store

       Primary Keys
         store_id {store_3}

       Imported (Foreign) Keys
         location (city.city_id) {store_7}

       Exported (Referenced) Keys
         store_id (site_store.store_id) {site_store_8}

       Columns
         location           int(4), non-nullable
         store_id           serial(4), non-nullable
         store_name         varchar(32), non-nullable

       Indices
         unique index {523_8115} on (store_id)
         unique index {store_ix_1} on (store_name)
       >>>

    table(table=None, types=("TABLE",), owner=None, schema=None)
       If no table argument, displays a list of all tables. If a table
       argument, displays the columns of the given table.

    proc(self, proc=None, owner=None, schema=None)
       If no proc argument, displays a list of all procedures. If a proc
       argument, displays the parameters of the given procedure.

    bcp(src, table, where='(1=1)', parameters=[], selective=[], ignorelist=[],
       autobatch=0)
       Bulk Copy from one database/table to another. The current instance
       of dbexts is the source database to which the results of the query
       on the foreign database will be inserted. An optional where clause
       can narrow the number of rows to be copied.

The following are generally not called since isql and raw can handle almost all cases.

begin(self)
:   Creates a new cursor.

rollback(self)
:   Rollback all the statements since the creation of the cursor.

commit(self, cursor=None, maxrows=None)
:   Commit all the statements since the creation of the cursor.

display(self)
:   Display the results using the formatter.
:::

::: 
#### [Example session](#id53)

    Jython 2.1b1 on java1.4.0-beta3 (JIT: null)
    Type "copyright", "credits" or "license" for more information.
    >>> from dbexts import dbexts
    >>> d = dbexts()
    >>> d.isql("create table store (store_id int, store_name varchar(32),
    location int)")
    >>> d.isql("insert into store values (?, ?, ?)", [(1, "amazon.com", 3),
    (2, "egghead.com", 4)])
    >>> d.isql("insert into store values (?, ?, ?)", [(15, "800.com", 1),
    (19, "fogdog.com", 3)])
    >>> d.isql("insert into store values (?, ?, ?)", [(5, "nike.com", 4)])
    >>> d.isql("select * from store order by store_name")

    STORE_ID | STORE_NAME  | LOCATION
    ---------------------------------
    15       | 800.com     | 1
    1        | amazon.com  | 3
    2        | egghead.com | 4
    19       | fogdog.com  | 3
    5        | nike.com    | 4

    5 rows affected

    >>>
:::
:::::::::::::::::::
