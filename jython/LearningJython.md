# LearningJython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Jython Course Outline

+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Author:    | Dave Kuhlman                                                                                                                                                                                                                                              |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Address:   | ``` address                                                                                                                                                                                                                                               |
|            |                                                                                                                                                                                                                                                           |
|            | dkuhlman@rexx.com                                                                                                                                                                                                                                         |
|            | http://www.rexx.com/~dkuhlman                                                                                                                                                                                                                             |
|            | ```                                                                                                                                                                                                                                                       |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Revision:  | 1.1b                                                                                                                                                                                                                                                      |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Date:      | May 9, 2008                                                                                                                                                                                                                                               |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Copyright: | Copyright (c) 2006 Dave Kuhlman. All Rights Reserved. This software is subject to the provisions of the MIT License [http://www.opensource.org/licenses/mit-license.php](http://www.opensource.org/licenses/mit-license.php). |
+------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

::: 
Abstract

This document provides an outline of an introductory course on programming in Jython and connecting Jython to Java
:::

::: 
Contents

- [1   How-to Write Jython Code](#how-to-write-jython-code)
- [2   Installing and Running Jython](#installing-and-running-jython)
  - [2.1   Install Jython](#install-jython)
  - [2.2   Configuration](#configuration)
    - [2.2.1   Command-line options](#command-line-options)
    - [2.2.2   Jython configuration files](#jython-configuration-files)
    - [2.2.3   Checking configuration values](#checking-configuration-values)
    - [2.2.4   Classpath and python path](#classpath-and-python-path)
  - [2.3   Running Jython](#running-jython)
  - [2.4   Installing Jython/Python packages](#installing-jython-python-packages)
- [3   Integrating Java into Jython/Python](#integrating-java-into-jython-python)
  - [3.1   Calling existing Java code](#calling-existing-java-code)
  - [3.2   Extending a Java class in Jython](#extending-a-java-class-in-jython)
  - [3.3   Emulating Jython classes in Java](#emulating-jython-classes-in-java)
  - [3.4   Preparing Java code to be called from Jython](#preparing-java-code-to-be-called-from-jython)
    - [3.4.1   Adding doc strings to a Java class](#adding-doc-strings-to-a-java-class)
    - [3.4.2   Working with Jython arguments](#working-with-jython-arguments)
    - [3.4.3   Sub-classing a Java class](#sub-classing-a-java-class)
    - [3.4.4   Emulating Jython Dictionaries, Sequences, Etc.](#emulating-jython-dictionaries-sequences-etc)
      - [3.4.4.1   Solution #1 \-- Emulating a dictionary](#solution-1-emulating-a-dictionary)
      - [3.4.4.2   Solution #2 \-- Extending PyDictionary](#solution-2-extending-pydictionary)
    - [3.4.5   Emulating Jython object attribute access](#emulating-jython-object-attribute-access)
  - [3.5   Extending a built-in Jython class in Java](#extending-a-built-in-jython-class-in-java)
  - [3.6   jarray \-- Creating and passing Java arrays to Java](#jarray-creating-and-passing-java-arrays-to-java)
- [4   Integrating Jython/Python into Java](#integrating-jython-python-into-java)
  - [4.1   Calling Jython from Java](#calling-jython-from-java)
    - [4.1.1   Run Jython code on an interpreter embedded in Java](#run-jython-code-on-an-interpreter-embedded-in-java)
    - [4.1.2   How to run Jython code on an interpreter embedded in Java](#how-to-run-jython-code-on-an-interpreter-embedded-in-java)
      - [4.1.2.1   Example \-- a possible organization on disk](#example-a-possible-organization-on-disk)
      - [4.1.2.2   Example \-- the Jython classes](#example-the-jython-classes)
      - [4.1.2.3   Example \-- A Java interface class](#example-a-java-interface-class)
      - [4.1.2.4   Example \-- another interface class](#example-another-interface-class)
      - [4.1.2.5   Example \-- the factory class](#example-the-factory-class)
      - [4.1.2.6   Example \-- the Java consumer code](#example-the-java-consumer-code)
    - [4.1.3   Additional support for running Jython code on an interpreter embedded in Java](#additional-support-for-running-jython-code-on-an-interpreter-embedded-in-java)
  - [4.2   Embedding Jython into Java](#embedding-jython-into-java)
    - [4.2.1   Why embedded Jython](#why-embedded-jython)
    - [4.2.2   Embedding Jython into Java is simple](#embedding-jython-into-java-is-simple)
    - [4.2.3   Passing values into a Jython script](#passing-values-into-a-jython-script)
    - [4.2.4   Initializing the interpreter](#initializing-the-interpreter)
      - [4.2.4.1   An interpreter with an initial system state](#an-interpreter-with-an-initial-system-state)
      - [4.2.4.2   A system state and a custom class loader](#a-system-state-and-a-custom-class-loader)
    - [4.2.5   Retrieving values from a Jython script](#retrieving-values-from-a-jython-script)
    - [4.2.6   There are also a few complexities](#there-are-also-a-few-complexities)
    - [4.2.7   Exposing transparent objects](#exposing-transparent-objects)
    - [4.2.8   Exposing opaque objects](#exposing-opaque-objects)
    - [4.2.9   Type conversion](#type-conversion)
    - [4.2.10   Using a custom class loader](#using-a-custom-class-loader)
    - [4.2.11   Embedding a Jython console](#embedding-a-jython-console)
  - [4.3   Embedding Jython with the Java Scripting Engine](#embedding-jython-with-the-java-scripting-engine)
    - [4.3.1   Installing script engine support](#installing-script-engine-support)
    - [4.3.2   Using script engine support](#using-script-engine-support)
  - [4.4   Compiling Jython code with jythonc](#compiling-jython-code-with-jythonc)
    - [4.4.1   Introduction to jythonc](#introduction-to-jythonc)
    - [4.4.2   How to run jythonc](#how-to-run-jythonc)
    - [4.4.3   Calling Jython from Java using jythonc](#calling-jython-from-java-using-jythonc)
- [5   Deployment and Distribution](#deployment-and-distribution)
  - [5.1   Building jars - some samples](#building-jars-some-samples)
    - [5.1.1   Add Jython install stuff to our jar](#add-jython-install-stuff-to-our-jar)
    - [5.1.2   Add modules and paths to the jar file](#add-modules-and-paths-to-the-jar-file)
    - [5.1.3   Run the script/jar](#run-the-script-jar)
    - [5.1.4   A more self-contained jar file](#a-more-self-contained-jar-file)
    - [5.1.5   A summary](#a-summary)
- [6   Integrating, Embedding, and Extending \-- A Summary](#integrating-embedding-and-extending-a-summary)
- [7   Jython+Java \-- Other Advanced Topics](#jython-java-other-advanced-topics)
  - [7.1   Event handling](#event-handling)
  - [7.2   XML](#xml)
    - [7.2.1   jaxp](#jaxp)
    - [7.2.2   Xerces](#xerces)
    - [7.2.3   dom4j](#dom4j)
      - [7.2.3.1   Installation and setup](#installation-and-setup)
      - [7.2.3.2   Examples etc](#examples-etc)
    - [7.2.4   XMLBeans](#xmlbeans)
      - [7.2.4.1   Installation](#installation)
      - [7.2.4.2   An example](#an-example)
  - [7.3   Database access](#database-access)
    - [7.3.1   JDBC](#jdbc)
    - [7.3.2   zxJDBC](#zxjdbc)
- [8   Additional Exercises](#additional-exercises)
- [9   References and Sources](#references-and-sources)
:::

::: 
### [1   How-to Write Jython Code](#id6)

Jython is Python. That\'s one of its big advantages: you get two for the price of one. If your learn Python, then you have also learned Jython, and vice versa. If you already know Python, then you know Jython.

But, if you do not know Python **or** Jython, then here are good training aids:

- [Python documentation \-- http://python.org/doc/](http://python.org/doc/)
- [Python tutorial \-- http://docs.python.org/tut/tut.html](http://docs.python.org/tut/tut.html)
- [BeginnersGuide/NonProgrammers \-- http://wiki.python.org/moin/BeginnersGuide/NonProgrammers](http://wiki.python.org/moin/BeginnersGuide/NonProgrammers)
- [BeginnersGuide/Programmers \-- http://wiki.python.org/moin/BeginnersGuide/Programmers](http://wiki.python.org/moin/BeginnersGuide/Programmers)
:::

::::::::::: 
### [2   Installing and Running Jython](#id7)

::: 
#### [2.1   Install Jython](#id8)

You will need Java installed, of course. And, since you are likely to want to use Jython class libraries from Jython, it is also likely that you will want the Java SDK. **Important**: If more than one version of Java is installed on your machine, make sure that when you install Jython, you use the version of Java for which the SDK is installed and the version of Java that you will be using when you run Jython.

Download the Jython installation jar file \-- You can find the Jython distribution here: [Jython downloads \-- http://jython.org/Project/download.html](http://jython.org/Project/download.html).

Install Jython \-- Follow the instructions at: [Installing Jython \-- http://wiki.python.org/jython/InstallingJython](http://wiki.python.org/jython/InstallingJython):

    $ java -jar jython_installer-2.2.1.jar

Command line history \-- On MS Windows, command line history for the Jython interactive interpreter comes built-in. On Linux, to get command line history, command line editing, and readline support, follow the instructions here: [ReadlineSetup \-- http://wiki.python.org/jython/ReadlineSetup](http://wiki.python.org/jython/ReadlineSetup).

Standalone mode \-- You can also create a self-contained Jython jar file. Run the standard installer (above), then you come to the \"Installation type\" page, select \"Standalone\". For more on this, see: [Standalone mode \-- http://www.jython.org/Project/installation.html#standalone-mode](http://www.jython.org/Project/installation.html#standalone-mode)
:::

::::::: 
#### [2.2   Configuration](#id9)

There are several places to configure Jython.

::: 
##### [2.2.1   Command-line options](#id10)

To display the options for `jython`, type:

    $ jython --help
:::

::: 
##### [2.2.2   Jython configuration files](#id11)

For explanation of configuration options and values, see:

- The comments in the (default) registry file.
- [The Jython Registry \-- http://wiki.python.org/jython/UserGuide#the-jython-registry](http://www.jython.org/docs/registry.html).
:::

::: 
##### [2.2.3   Checking configuration values](#id12)

From within the Jython interactive interpreter or from within your Jython application, you can display the values of configuration properties.

To get the system properties as a dictionary-like object, do:

    >>> from java.lang import System
    >>> props = System.getProperties()

Of particular interest are the following:

- `props['java.class.path']` \-- Location of the Jython jar file.
- `props['java.library.path']` \-- Locations of Java class libraries.

Other properties are in sys.registry:

    >>> import sys
    >>> r = sys.registry
    >>> for k in r:
    ... print k, r[k]

Here is a script that you may find useful when interactively inspecting system properties:

    >>> from java.lang import System
    >>> props = System.getProperties()
    >>> names = []
    >>> for name in props.keys():
    ... names.append(name)
    ...
    >>> names.sort() # now you can list the keys in alpha order
    >>> for val in props['java.class.path'].split(':'):
    ... print val
    ...
    /home/dkuhlman/a1/Python/Jython/Tmp1/Jython-2.1/jython.jar
    /usr/share/jython/jython.jar
:::

::: 
##### [2.2.4   Classpath and python path](#id13)

Jython can pick up Java class files from locations on either the Jython/Python path (see `sys.path`) or the Java classpath. Set these with the following:

- The Python/Jython path can be set in your registry file. See registry variable `python.path`.

  Or, at runtime, you could do:

      >>> import sys
      >>> sys.path.append('/path/to/module')

  But, you must do the above *before* trying to import the module.

- Set the classpath by setting the CLASSPATH environment variable. Note that (on my Linux machine, at least) the CLASSPATH environment variable is picked up and added to the Java `-classpath` flag.

A few rules about CLASSPATH and python.path:

- `sys.path` in the registry file \-- Add here to enable importing from Java classes (.java), Java class libraries (.jar), and Jython/Python (.py).
- CLASSPATH \-- Add paths to this environment variable in order to enable importing from Java classes (.java) and Java class libraries (.jar), but not Jython/Python (.py).
:::
:::::::

::: 
#### [2.3   Running Jython](#id14)

The Jython interactive, command-line interpreter: `jython`.

Jython IDEs (interactive development environments) \-- There is a Jython plug-in for Eclipse. See: [http://pydev.sourceforge.net/](http://pydev.sourceforge.net/).

Exercises \-- Start the Jython interpreter. Then do each of the following:

- Print \"hello\".
- Define an empty class.
- Import a Python/Jython file containing a class definition. Create an instance of that class.
- Import a module from the standard Python/Jython library, for example, `re` or `os.path`. Use a method from that module.
- Import a Java class, for example, `java.util.Vector`. Create and use an instance of that class.

Running Jython scripts:

- From the command line, run a script with `jython`. For example:

      $ jython myscript.py

- For help, run:

      $ jython --help

- For debugging, use something similar to the following:

      import pdb
      pdb.run('main()')

  Or:

      import pdb
      pdb.set_trace()

  For example:

      def main():
          util101()

      if __name__ == '__main__':
          import pdb; pdb.set_trace()
          main()

- To \"set a breakpoint\" in your code so that it will drop into debugger, either (1) use the `b` command at the `pdb` prompt or (2) add the following to your code at the location where you wish to drop into the debugger:

      import pdb; pdb.set_trace()

  For more information on the Python debugger, see [The Python Debugger](http://docs.python.org/lib/module-pdb.html) in the Python standard documentation, or while in the debugger, type `help`.

- To make a script both \"run-able\" and \"import-able\", use the following idiom:

      if __name__ == '__main__':
          main()

Don\'t forget to include a doc string at the top of your module for documentation.

Exercise \-- Create a small Jython script:

- Include a class in your script that creates an instance of `java.util.Vector`.
- Make the script both \"run-able\" and \"import-able\".
- From the Jython interpreter, import the script and create an instance of the class.
- From the command line, use `jython` to run the script.
- Add `pdb` debugging to your script. Run the script again from the command line. Step through several lines of code.
:::

::: 
#### [2.4   Installing Jython/Python packages](#id15)

Some Jython packages will be distributed as a Java jar file. If that is the case, add the jar file to your classpath.

If the package is distributed as a standard Python package with a `setup.py` installer file and *if* there are no C/C++ files in the package, then you might try something like the following:

    $ python setup.py install --prefix /path/to/install/directory

And, then put that install directory on your classpath.
:::
:::::::::::

:::::::::::::::: 
### [3   Integrating Java into Jython/Python](#id16)

::: 
#### [3.1   Calling existing Java code](#id17)

In order to call Java code from Jython do the following:

1.  Import the Java module.
2.  Use the Java module to create an instance/object.
3.  Call functions and objects in it.

It works the way you would hope and expect it to. Here is an example:

    >>> from java.util import Vector
    >>> v = Vector()
    >>> dir(v)
    ['__init__', 'add', 'addAll', 'addElement', 'capacity', 'class', 'clear', 'clone', 'contains', 'containsAll', 'copyInto', 'elementAt', 'elements', 'empty', 'ensureCapacity', 'equals', 'firstElement', 'get', 'getClass', 'hashCode', 'indexOf', 'insertElementAt', 'isEmpty', 'iterator', 'lastElement', 'lastIndexOf', 'listIterator', 'notify', 'notifyAll', 'remove', 'removeAll', 'removeAllElements', 'removeElement', 'removeElementAt', 'retainAll', 'set', 'setElementAt', 'setSize', 'size', 'subList', 'toArray', 'toString', 'trimToSize', 'wait']
    >>>
    >>> v.add('aaa')
    1
    >>> v.add('bbb')
    1
    >>> for val in v:
    ... print val
    ...
    aaa
    bbb

In some cases you will need to pass Java objects to Java methods.

Special treatment for some overloaded Java methods \-- Explicitly create and pass Jython objects. For more on this, see: [Overloaded Java Method Signatures](http://www.jython.org/Project/userguide.html#overloaded-java-method-signatures) \-- [http://www.jython.org/Project/userguide.html#overloaded-java-method-signatures](http://www.jython.org/Project/userguide.html#overloaded-java-method-signatures).

Often you can use Python/Jython style and idioms to process Java objects. For example: the Jython `for` statement can be applied to Java collection objects.

Exercise \-- Use the class `java.util.Hashtable` to create a dictionary with several keys and values, then print out the keys and their values. Solution:

    >>> from java.util import Hashtable
    >>> impl_language = Hashtable()
    >>> impl_language.put('jython', 'java')
    >>> impl_language.put('python', 'c')
    >>> for key in impl_language.keys():
    ... print '%s is implemented in %s' % (key, impl_language[key])
    ...
    python is implemented in c
    jython is implemented in java
:::

::: 
#### [3.2   Extending a Java class in Jython](#id18)

You can import and then extend (sub-class) a Java class.

Example \-- This sample extends the Java filestream class by adding a method that converts all characters to upper case::

    import sys
    from java.io import FileOutputStream

    class UppercaseFileOutputStream(FileOutputStream):
        def write_upper(self, text):
            text = text.upper()
            self.write(text)

    def test(outfilename):
        fos = UppercaseFileOutputStream(outfilename)
        for idx in range(10):
            fos.write_upper('This is line # %d\n' % idx)
        fos.close()
        infile = open(outfilename, 'r')
        for line in infile:
            line = line.rstrip()
            print 'Line: %s' % line

    def main():
        args = sys.argv[1:]
        if len(args) != 1:
            print 'usage: extend_fileoutputstream.py <infilename>'
            sys.exit(1)
        test(args[0])

    if __name__ == '__main__':
        main()
:::

::: 
#### [3.3   Emulating Jython classes in Java](#id19)

You can make a Java class \"act like\" one of the built-in Jython classes. In order to do so, you would implement one or more of Jython\'s special methods. You can find descriptions of the special methods in the \"Python Reference Manual\": [3.4 Special method names \-- http://docs.python.org/ref/specialnames.html](http://docs.python.org/ref/specialnames.html).

Example: This module implements a class that acts like a sequence in certain ways, specifically (1) it responds to the `len()` operator by returning a length; (2) it supports an `append` method; and (3) it supports the use of the `[]` operator to get a value:

    import java.util.Vector;

    // Implement selected part of the Jython container interface.
    public class CustomContainer {

        private Vector data;

        public CustomContainer() {
            data = new Vector();
        }

        // Implement the len() operator.
        public int __len__() {
            return data.size();
        }

        // Implement the append() method.
        public int append(String item) {
            data.add(item);
            return 1;
        }

        // Implement the [] operator.
        public String __getitem__(int index) {
            return (String)data.elementAt(index);
        }
    }

And here is an example of the use of this custom container class:

    $ jython
    Jython 2.2.1rc1 on java1.4.2_10
    Type "copyright", "credits" or "license" for more information.
    >>>
    >>> import CustomContainer as cc
    >>> container = cc()
    >>> container.append('item number one')
    1
    >>> container.append('item number two')
    1
    >>> container.append('item number three')
    1
    >>> len(container)
    3
    >>> for index in range(len(container)):
    ... print container[index]
    ...
    item number one
    item number two
    item number three

Notes:

- A more powerful solution, depending on your needs, would be for `CustomContainer` to inherit from `java.util.Vector`. See section [Emulating Jython Dictionaries, Sequences, Etc.](#emulating-jython-dictionaries-sequences-etc) for an example.
:::

:::::::::: 
#### [3.4   Preparing Java code to be called from Jython](#id20)

Another view: Java is the extension language for Jython.

No special work is required. Jython can call normal Java classes.

Need to pay attention to data types, for example, on the Jython side. Use an explicit cast, for example, `float(5)`.

For additional help, see:

- [Overview of Jython Documentation](http://www.jython.org/docs/index.html)
- The Jython API [with frames](http://www.jython.org/docs/javadoc/index.html) or [without frames](http://www.jython.org/docs/javadoc/overview-summary.html).

You can also customize a Java class to make it more \"Jythonic\".

::: 
##### [3.4.1   Adding doc strings to a Java class](#id21)

This first, simple example adds doc strings:

    // Showme.java

    import org.python.core.*;

    public class ShowMe
    {
        public static PyString __doc__ =
            new PyString("Simple Jython extension #1");

        public String name;

        public ShowMe(String newName)
        {
            name = newName;
        }
        public static PyString __doc__set_name = new PyString(
            "Set the name attribute");
        public void set_name(String newName)
        {
            name = newName;
        }
        public static PyString __doc__get_name = new PyString(
            "Get the name attribute");
        public String get_name()
        {
            return name;
        }

        public static PyString __doc__Show = new PyString(
            "Show the name attribute");
        public void Show()
        {
            System.out.println("My name is \"" + name + "\".");
        }
    }

Notes:

- Doc strings for the class and methods are defined with public static Strings. You can, alternatively, use PyString.
- For more complex control over doc strings (for example, in a Java files that contains multiple classes) your class can implement the `ClassDictInit` interface and implement the `classDictInit` method. See \"Jython for Java Programmers\", pp. 276 ff.
:::

::: 
##### [3.4.2   Working with Jython arguments](#id22)

The `ArgParser` class helps us handle Jython keyword arguments. If helps us write Java methods that support the analog of Jython\'s `*args` and `**kwargs` in Java methods.

How to do it \-- An overview:

1.  Define your Java method with the following prototype:

        public PyObject foo(PyObject[] args, String[] keywords);

2.  Parse the arguments with class `ArgParser`.

3.  Access individual arguments with `ArgParser` methods `getInt()`, `getString()`, `getList()`, and `getPyObject()`.

4.  Since both `args` and `keywords` are arrays, check the number of arguments actually passed with `args.length` and `keywords.length`.

For more information, see: [Jython API Documentation: org.python.core Class ArgParser \-- http://www.jython.org/docs/javadoc/org/python/core/ArgParser.html](http://www.jython.org/docs/javadoc/org/python/core/ArgParser.html).

Exercise \-- (1) Write a Java class containing a method that prints all its arguments and all the keyword arguments passed to it. (2) Then call that method from Jython.

Solution:

    // DemoArgs.java

    import org.python.core.*;

    public class DemoArgs
    {
        public static PyString __doc__ =
            new PyString("Demonstrate the use of complex arguments.");

        public String name;
        public String value;

        public DemoArgs(String newName, String newValue)
        {
            name = newName;
            value = newValue;
        }

        public static PyString __doc__set_name = new PyString(
            "Set the name attribute");
        public void set_name(PyObject[] args, String[] kwargs)
        {
            System.out.println("length(args): " +
                args.length +
                " length(kwargs): " +
                kwargs.length
                );
            ArgParser ap = new ArgParser("set_name", args, kwargs,
                new String[] {"name", "value"});
            String newName = ap.getString(0, "");
            String newValue = ap.getString(1, "<empty>");
            if (!newName.equals(""))
            {
                name = newName;
            }
            value = newValue;
        }
        public static PyString __doc__get_name = new PyString(
            "Get the name attribute");
        public String get_name()
        {
            return name;
        }

        public static PyString __doc__get_value = new PyString(
            "Get the value attribute");
        public String get_value()
        {
            return value;
        }

        public static PyString __doc__Show = new PyString(
            "Show the name and value attributes");
        public void Show()
        {
            System.out.println("My name is \"" + name +
                "\" and my value is \"" + value + "\".");
        }
    }

Compile the above file with `javac` or some other Java compiler. To do so, you will need to add `jython.jar` to your `CLASSPATH`.

Notes:

- Use class `ArgParser` to capture the arguments.
- Use `ArgParser` methods `getInt`, `getString`, `getPyObject`, and `getList` to retrieve arguments.
- Notice that in method `get_name`, we print the length of the args and kwargs. This demonstrates that you can check the length of these arrays and can throw an exception if, for example, too few arguments are passed.

Also see the Jython FAQ: [5.3 Supporting \*args and \*\*kw in Java methods \-- http://jython.org/Project/userfaq.html#supporting-args-and-kw-in-java-methods](http://jython.org/Project/userfaq.html#supporting-args-and-kw-in-java-methods).
:::

::: 
##### [3.4.3   Sub-classing a Java class](#id23)

Notice that, in Jython, we can extend a class written in Java:

    import DemoArgs

    class Fancy(DemoArgs):
        def __init__(self, name, value):
            DemoArgs.__init__(self, name, value)
        def ShowFancy(self):
            print "I'm fancy and my name is %s and my value is %s" % \
                (self.name, self.value)

    def test():
        f = Fancy('dave', 'funny')
        f.ShowFancy()
        f.set_name('daniel', 'cute')
        f.ShowFancy()

    test()

When you run the above, you should see something like the following:

    $ jython tmp.py
    I'm fancy and my name is dave and my value is funny
    length(args): 2 length(kwargs): 0
    I'm fancy and my name is daniel and my value is cute
:::

::::: 
##### [3.4.4   Emulating Jython Dictionaries, Sequences, Etc.](#id24)

Extend class org.python.core.PyObject and its sub-classes. See: [org.python.core Class PyObject](http://www.jython.org/docs/javadoc/org/python/core/PyObject.html).

Implement the following methods:

    __getitem__()
    __finditem()
    __setitem__()
    __delitem__()
    ...

`getitem()` vs. `finditem()`:

- If the index is not found or out of range, `finditem()` returns null, whereas `__getitem()` should throw an exception.
- The Jython API documentation says to override `finditem()` and not `getitem()`. See: [org.python.core Class PyObject](http://www.jython.org/docs/javadoc/org/python/core/PyObject.html).

See [3.3.5 Emulating container types \-- http://docs.python.org/ref/sequence-types.html](http://docs.python.org/ref/sequence-types.html) in the Python Reference Manual for more information on customizing dictionaries and sequences.

Exercise \-- (1) Write a Java class that emulates or imitates a Jython dictionary. (2) In addition, each access method should print a message. (3) Test your Java class from Jython by creating an instance of it, then setting and retrieving a key-value pair.

::: 
###### [3.4.4.1   Solution #1 \-- Emulating a dictionary](#id25)

This solution is for educational purposes only (see [Solution #2 \-- Extending PyDictionary](#solution-2-extending-pydictionary)):

    // TestDict.java

    import org.python.core.*;
    import java.util.*;

    public class TestDict
    {
     public Hashtable data;

     public TestDict()
     {
      data = new Hashtable();
     }
     public void __setitem__(String key, String value)
     {
      data.put(key, value);
      System.out.println("Added key \"" + key + "\" value: \"" +
             value + "\"");
     }
     public String __getitem__(String key)
     {
      if (data.containsKey(key))
      {
       String value = (String)data.get(key);
       System.out.println("Found key \"" + key + "\" value: \"" +
             value + "\"");
       return value;
      }
      else
      {
       throw new PyException(Py.KeyError, "The key does not exit.");
      }
     }
     public boolean __contains__(String key)
     {
      if (data.containsKey(key))
      {
       System.out.println("Found key \"" + key + "\"");
       return true;
      }
      else
      {
       System.out.println("Did not find key \"" + key + "\"");
       return false;
      }
     }
    }

Notes:

- The above class implements a limited part of the Jython dictionary protocol, in particular `__setitem__`, `__getitem__`, and `__contains__`.

- This above solution also illustrates how to throw (\"raise\" in Jython terms) an exception from Java that can be caught in Jython. Here is an example of catching that exception on the Jython side:

      >>> try:
      ... x = b['xyz']
      ... except KeyError, e:
      ... print '*** error: %s' % e
      ...
      *** error: The key does not exit.

- The Jython FAQ recommends that your Jython class extends PyObject. (see [5. Extending Jython \-- http://jython.org/Project/userfaq.html#extending-jython](http://jython.org/Project/userfaq.html#extending-jython)) I\'ve found that it is not strictly necessary to extend `PyObect` in your Java class (the one that emulates a Jython built-in). **But, if you do**, you will need to follow the signature of the methods that implement operators (for example `__setitem__`, `__getitem__`, etc) exactly. To learn those signatures, see the API documentation in the `Doc/` directory under your Jython installation.

Here is an example that uses the above solution:

    # test_TestDict.py

    import TestDict

    def test():
        d = TestDict()
        d['aa'] = 'AAAA'
        d['bb'] = 'BBBB'
        d['cc'] = 'CCCC'
        print d.data
        if 'bb' in d:
            print 'present'

    test()

And, here is the result of running this test:

    $ jython test_TestDict.py
    Added key "aa" value: "AAAA"
    Added key "bb" value: "BBBB"
    Added key "cc" value: "CCCC"
    
    Found key "bb"
    present
:::

::: 
###### [3.4.4.2   Solution #2 \-- Extending PyDictionary](#id26)

This solution shows how you most likely would start if you wanted to extend the dictionary type or implement a custom dictionary type:

    // TestDictSub.java

    import org.python.core.*;
    import java.util.*;

    public class TestDictSub extends PyDictionary
    {
        public void __setitem__(PyObject key, PyObject value)
        {
            super.__setitem__(key, value);
            System.out.println("Added key \"" + key + "\" value: \"" +
                               value + "\"");
        }
        public PyObject __getitem__(PyObject key)
        {
            if (super.__contains__(key))
            {
                PyObject value = super.__getitem__(key);
                System.out.println("Found key \"" + key + "\" value: \"" +
                               value + "\"");
                return value;
            }
            else
            {
                throw new PyException(Py.KeyError, "The key does not exit.");
            }
        }
    }

Notes:

- This class inherits the methods in the PyDictionary class. It overrides several of those methods, specifically `__setitem__` and `__getitem__`.
- The Java class could also extend the dictionary type by implementing additional, new methods.

Also see the Jython FAQ: [5.1 Java classes that emulate Jython Dictionaries and Sequences \-- http://jython.org/Project/userfaq.html#java-classes-that-emulate-jython-dictionaries-and-sequences](http://jython.org/Project/userfaq.html#java-classes-that-emulate-jython-dictionaries-and-sequences).
:::
:::::

::: 
##### [3.4.5   Emulating Jython object attribute access](#id27)

We can implement and override object attribute access in a Java class. And, we can emulate other Jython built-in types.

Extend class org.python.core.PyObject and its sub-classes.

Implement the following methods, among others:

    __findattr_ex__()
    __setattr__()
    __delattr__()
    __finditem__()
    Etc.

`__findattr_ex__()` is called *only if* an attribute is not found in an object.

Exercise \-- (1) Write a Java class that supports access to attributes. (2) In addition, each access method should print a message. (3) Test your Java class from Jython by creating an instance of it, then setting and getting an attribute.

Solution:

    // TestAttrAccess.java

    import org.python.core.*;
    import java.util.*;

    public class TestAttrAccess extends PyObject
    {
        PyDictionary localdict = new PyDictionary();

        public PyObject __findattr_ex__(String name)
        {
            PyString pyname = new PyString(name);
            System.out.println("Finding attr for: \"" + name + "\"");
            if (localdict.__contains__(pyname)) {
                return localdict.__getitem__(pyname);
            }
            else
            {
                return new PyString("[no attr]");
            }
        }
        public void __setattr__(String name, PyObject value)
        {
            PyString pyname = new PyString(name);
            System.out.println("Setting attr for: \"" + name + "\"");
            localdict.__setitem__(pyname, value);
        }
    }

Notes:

- Test this solution with the following:

      import TestAttrAccess

      def test():
          a = TestAttrAccess()
          a.bbb = 3344
          print a.bbb
          # Try to access a nonexistent attribute.
          print a.ccc

      test()

- Arguments to `__findattr_ex__` and `__finditem__` must be interned strings. Literal strings are automatically interned. For other strings, use `intern(s)`.

Exercise \-- (1) Write a Java class that emulates a Jython dictionary, but intercepts key access to items in the dictionary. Print a message when each access is attempted.

Solution:

    // TestDictSub.java

    import org.python.core.*;
    import java.util.*;

    public class TestDictSub extends PyDictionary
    {
        public PyObject __finditem__(PyObject key)
        {
            System.out.println("Getting item for: \"" + key + "\"");
            PyObject objkey = key;
            if (super.__contains__(objkey))
            {
                PyObject value = super.__finditem__(objkey);
                System.out.println(
      "Found key \"" + key + "\" value: \"" +
                    value + "\"");
                return value;
            }
            else
            {
                throw new PyException(Py.KeyError,
      "The key does not exit.");
            }
        }
    }

Notes:

- Here is a test for the above code:

      import TestDictSub as TDS

      def test():
          a = TDS()
          a['aaa'] = 123
          a['bbb'] = 456
          print a['aaa']
          print a['ccc']

      test()

- We implement `__finditem__()` rather than `__getitem__()`. See the notes for Class PyObject in the [Jython API documentation \-- http://jython.org/docs/javadoc/index.html](http://jython.org/docs/javadoc/index.html)

Also see the Jython FAQ: [5.2 Emulating Jython object attribute access with a Java class \-- http://jython.org/Project/userfaq.html#emulating-jython-object-attribute-access-with-a-java-class](http://jython.org/Project/userfaq.html#emulating-jython-object-attribute-access-with-a-java-class).
:::
::::::::::

::: 
#### [3.5   Extending a built-in Jython class in Java](#id28)

In Java, you can inherit from an extend the built-in Jython classes.

Some of the classes that you can consider extending are:

- PyDictionary
- PyInteger
- PyList
- PyString
- PyStringMap
- PyTuple

An example that extends the `PyDictionary` class is in section [Solution #2 \-- Extending PyDictionary](#solution-2-extending-pydictionary).
:::

::: 
#### [3.6   jarray \-- Creating and passing Java arrays to Java](#id29)

Why you might want to do this \-- Suppose that you want to pass an array to a Java method. Furthermore, suppose that Java method is going to modify the contents of your array. If you pass in a Jython list, Jython creates a wrapper for your list, and any modifications made by Java will not be return to Jython.

In this situation, you will want to use `jarray` to create Java arrays. For more on Java arrays, see: [Jython User Guide: Java Arrays \-- http://jython.org/Project/userguide.html#java-arrays](http://jython.org/Project/userguide.html#java-arrays).

Here is an example of a Java class that modifies the contents of an array. You can use it to demonstrate the need for jarry:

    import java.util.Vector;

    public class TestJarray {

     private Integer data[];

     public void setdata(Integer newdata[]) {
      data = newdata;
     }

     public void changedata() throws ArrayIndexOutOfBoundsException {
      data[0] = new Integer(99);
     }

     public Integer[] getdata() {
      return data;
     }

    }

And, here is a Jython program that tests it:

    import jarray
    import java.lang.Integer
    import TestJarray

    def test():
        print '1.', '-' * 30
        a1 = TestJarray()
        b1 = [11, 22, 33]
        a1.setdata(b1)
        a1.changedata()
        c1 = a1.getdata()
        print 'a1:', a1
        print 'b1:', b1
        print 'c1:', c1
        print '2.', '-' * 30
        a2 = TestJarray()
        b2 = [11, 22, 33]
        b2j = jarray.array(b2, java.lang.Integer)
        a2.setdata(b2j)
        a2.changedata()
        c2 = a2.getdata()
        print 'a2:', a2
        print 'b2:', b2
        print 'b2j:', b2j
        print 'c2:', c2

    test()

This is the output from running the above Jython script:

    $ jython test_jarray.py
    1. ------------------------------
    a1: TestJarray@7e9a288b
    b1: [11, 22, 33]
    c1: array(java.lang.Integer,[99, 22, 33])
    2. ------------------------------
    a2: TestJarray@1cb5c12e
    b2: [11, 22, 33]
    b2j: array(java.lang.Integer,[99, 22, 33])
    c2: array(java.lang.Integer,[99, 22, 33])

Notes:

- The Jython list (`b1`) that we pass to Java remains unchanged, because it is \"wrapped\" by Jython.
- The `jarray` (`b2j`) that we pass to Java is modified.

Here are a few examples.

A simple array of ints:

    >>> jarray.array([11, 22, 33], 'i')
    array('i',[11, 22, 33])

An array of floats:

    >>> jarray.array([11.0, 22.0, 33.0], 'f')
    array('f',[11.0, 22.0, 33.0])

An array of strings:

    >>> jarray.array(['aaa', 'bbb', 'ccc'], java.lang.String)
    array(java.lang.String,['aaa', 'bbb', 'ccc'])

The following examples create two-dimensional arrays.

An array of arrays of ints:

    >>> jarray.array([[11, 22], [33, 44]], java.lang.Class.forName("[I"))
    array([I,[array('i',[11, 22]) , array('i',[33, 44]) ])

An array of arrays of strings:

    >>> jarray.array([ ['aaa', 'bbb'], ['ccc', 'ddd'] ], java.lang.Class.forName('[Ljava.lang.String;'))
    array([Ljava.lang.String;,[array(java.lang.String,['aaa', 'bbb']) , array(java.lang.String,['ccc', 'ddd']) ])

It is also possible to create 3-D arrays \-- A three dimensional array of ints and another of floats:

    >>> a = [[11, 22], [33, 44]]
    >>> b = [[55, 66], [77, 88]]
    >>> c = [a, b]
    >>> c
    [[[11, 22], [33, 44]], [[55, 66], [77, 88]]]
    >>> jarray.array(c, java.lang.Class.forName("[[I"))
    array([[I,[array([I,[array('i',[11, 22]) , array('i',[33, 44]) ]) , array([I,[array('i',[55, 66]) , array('i',[77, 88]) ]) ])
    >>> jarray.array(c, java.lang.Class.forName("[[F"))
    array([[F,[array([F,[array('f',[11.0, 22.0]) , array('f',[33.0, 44.0]) ]) , array([F,[array('f',[55.0, 66.0]) , array('f',[77.0, 88.0]) ]) ])

Here are a few notes:

> From the language spec, 3rd edition:
>
> > Every array also has a class; the method getClass, when invoked for an array object, will return a class object (of class Class) that represents the class of the array.
> >
> > The classes for arrays have strange names that are not valid identifiers; for example, the class for an array of int components has the name \"\[I\" and so the value of the expression:
> >
> > > int\[\].class.getName()
> >
> > is the string \"\[I\"; see the specification of Class.getName for details.
>
> From API spec for Class.getName:
>
> > If this class object represents a class of arrays, then the internal form of the name consists of the name of the element type preceded by one or more \'\[\' characters representing the depth of the array nesting. The encoding of element type names is as follows:
> >
> >     Element Type Encoding
> >     boolean Z
> >     byte B
> >     char C
> >     class or interface Lclassname;
> >     double D
> >     float F
> >     int I
> >     long J
> >     short S
> >
> > The class or interface name classname is the binary name of the class specified above.

References:

- [Jython User Guide: Java Arrays \-- http://jython.org/Project/userguide.html#java-arrays](http://jython.org/Project/userguide.html#java-arrays)
- [The Java Language Specification, Third Edition: Types, Values, and Variables \-- http://java.sun.com/docs/books/jls/third_edition/html/typesValues.html](http://java.sun.com/docs/books/jls/third_edition/html/typesValues.html)
- [Java Platform, Standard Edition 6 API Specification \-- http://java.sun.com/javase/6/docs/api/](http://java.sun.com/javase/6/docs/api/)
:::
::::::::::::::::

:::::::::::::::::::::::::::::::::: 
### [4   Integrating Jython/Python into Java](#id30)

:::::::::::: 
#### [4.1   Calling Jython from Java](#id31)

::: 
##### [4.1.1   Run Jython code on an interpreter embedded in Java](#id32)

`jythonc` is currently unsupported and is deprecated, although it might reappear in some future version of Jython. So, using `jythonc` to compile your Jython code to Java for use in your Java code may not appeal to you. An embedded Jython interpreter may be a solution.

Overview \-- Here is the general approach:

1.  Create a Jython interpreter object.

2.  Insert (set) values in your embedded interpreter, if needed.

3.  Use that interpreter to either:

    1.  Run several lines of code that import and use your Jython module, *or*
    2.  Run a small wrapper script that imports and uses your Jython modules.

4.  Retrieve values from your embedded interpreter, if necessary.

Each of these topics has been covered above.

Disadvantages of this approach:

- It\'s a little clumsy. Requires a small amount of Java code.

Advantages of this approach:

- `jythonc` is not required. `jythonc` is deprecated and is not planned for Jython 2.3.
- No need for a separate compile step.
- No need to *re-compile* your script each time it is modified.
:::

::::::::: 
##### [4.1.2   How to run Jython code on an interpreter embedded in Java](#id33)

Resources \-- For instructions on how to call Jython code from Java, see:

- [Accessing Jython from Java Without Using jythonc http://wiki.python.org/jython/JythonMonthly/Articles/September2006/1](http://wiki.python.org/jython/JythonMonthly/Articles/September2006/1)
- [Simple and Efficient Jython Object Factories http://wiki.python.org/jython/JythonMonthly/Articles/October2006/3](http://wiki.python.org/jython/JythonMonthly/Articles/October2006/3) \-- Note that the following examples were developed from this document.

Description \-- In order to implement this approach, here is what you will do:

- Implement one or more Jython/Python modules containing one or more classes. Or, perhaps this code already exists.
- Create a Java interface for each Jython class that you want to expose to Java. The interface should describe each method that you wish to expose to Java.
- Create a single Java \"factory\" class:
  - The constructor (1) creates a Jython interpreter; (2) runs a script that imports the Jython modules containing the Jython classes; (3) retrieves and saves the Jython classes from the intrepreter.
  - Implement one \"createX\" method for each Jython/Python class/type to be used from Java.
- Implement the Java code that uses the Jython classes. This Java code will typically do the following:
  1.  Create a factory object.
  2.  Call the \"createX\" methods to create Java objects that give access to the Jython classes.
  3.  Call the Jython methods through these Jython \"proxies\".

::: 
###### [4.1.2.1   Example \-- a possible organization on disk](#id34)

    |-- Employee.py # The Jython classes
    |-- jyinterface
    | |-- Main.java # The client code
    | |-- factories
    | | |-- EmployeeFactory.java # The factory
    | `-- interfaces
    | |-- DependentType.java # A Java interface
    | `-- EmployeeType.java # A Java interface

Notes:

- The Jython classes (in this case, Employee.py) can go anywhere on your Jython/Python path. See `python.path` in your registry file: [The Jython Registry \-- http://jython.org/Project/userguide.html#the-jython-registry](http://jython.org/Project/userguide.html#the-jython-registry).
- Layout for the Java code follows normal Java rules for packages.
:::

::: 
###### [4.1.2.2   Example \-- the Jython classes](#id35)

These are the Jython classes that we wish to expose to and call from Java:

    # Employee.py

    from jyinterface.interfaces import EmployeeType
    from jyinterface.interfaces import DependentType


    class Employee(EmployeeType):
        def __init__(self, first, last, id):
            self.first = first
            self.last = last
            self.id = id
            deps = self.create_dependents()
            self.deps = deps

        def create_dependents(self):
            d1 = Dependent('Sally', 'Serious', 11)
            d2 = Dependent('Larry', 'Lighthearted', 12)
            return [d1, d2]

        def getEmployeeFirst(self):
            return self.first

        def getEmployeeLast(self):
            return self.last

        def getEmployeeId(self):
            return self.id

        def getDependents(self):
            return self.deps

        def addDependent(self, dependent):
            self.deps.append(dependent)


    class Dependent(DependentType):
        def __init__(self, first, last, id):
            self.first = first
            self.last = last
            self.id = id

        def getDependentFirst(self):
            return '<<%s>>' % self.first

        def getDependentLast(self):
            return '<<%s>>' % self.last

        def getDependentId(self):
            return self.id * 4
:::

::: 
###### [4.1.2.3   Example \-- A Java interface class](#id36)

This (jyinterface/interfaces/EmployeeType.java) describes the interface to our Java (client) code:

    // EmployeeType.java

    package jyinterface.interfaces;
    import org.python.core.PyList;
    import jyinterface.interfaces.DependentType;


    public interface EmployeeType {
        public String getEmployeeFirst();
        public String getEmployeeLast();
        public String getEmployeeId();
        public PyList getDependents();
        public void addDependent(DependentType dependent);
    }
:::

::: 
###### [4.1.2.4   Example \-- another interface class](#id37)

This (jyinterface/interfaces/DependentType.java) is another interface. It describes and helps to expose another Jython class.

    // DependentType.java

    package jyinterface.interfaces;

    public interface DependentType {
         public String getDependentFirst();
         public String getDependentLast();
         public Integer getDependentId();
    }

Notes:

- We only describe the portions of the interface that we wish to expose to Java. It is likely that this will be a proper subset of the methods in our Jython class.
:::

::: 
###### [4.1.2.5   Example \-- the factory class](#id38)

This (jyinterface/factories/EmployeeFactory.java) is the factory that creates (proxy) instances of our Jython classes. These instances are Java instances with an underlying Jython implementation:

    // EmployeeFactory.java

    package jyinterface.factory;

    import jyinterface.interfaces.EmployeeType;
    import jyinterface.interfaces.DependentType;
    import org.python.core.PyObject;
    import org.python.core.PyString;
    import org.python.core.PyInteger;
    import org.python.util.PythonInterpreter;

    public class EmployeeFactory {

        public EmployeeFactory() {
            String cmd = "from Employee import Employee\nfrom Employee import Dependent";
            PythonInterpreter interpreter = new PythonInterpreter();
            //interpreter.exec("from Employee import Employee");
            //interpreter.exec("from Employee import Dependent");
            interpreter.exec(cmd);
            jyEmployeeClass = interpreter.get("Employee");
            jyDependentClass = interpreter.get("Dependent");
        }

        public EmployeeType createEmployee(String first, String last, String id) {
            PyObject employeeObj = jyEmployeeClass.__call__(
                new PyString(first),
                new PyString(last),
                new PyString(id));
            return (EmployeeType)employeeObj.__tojava__(EmployeeType.class);
        }

        public DependentType createDependent(String first, String last, int id) {
            PyObject dependentObj = jyDependentClass.__call__(
                new PyString(first),
                new PyString(last),
                new PyInteger(id));
            return (DependentType)dependentObj.__tojava__(DependentType.class);
        }

        private PyObject jyEmployeeClass;
        private PyObject jyDependentClass;
    }

Notes:

- The Jython interpreter is created only once, when the factory object is created.
- The Java classes that are proxies for the Jython classes exposed to Java (jyEmployeeClass amd jyDependentClass) are also only created once.
- Each \"creater\" method (createEmployee and createDependent) uses the `__call__` method to create an instance. This is the same as using `obj = Employee()`, for example, in Jython. Then the result is converted to a Java object and returned.
:::

::: 
###### [4.1.2.6   Example \-- the Java consumer code](#id39)

This (jyinterface/Main.java) is the Java code that uses our Jython classes:

    // Main.java

    package jyinterface;

    import jyinterface.factories.EmployeeFactory;
    import jyinterface.interfaces.EmployeeType;
    import jyinterface.interfaces.DependentType;
    import org.python.core.PyObject;
    import org.python.core.PyList;

    public class Main {

        private static void printEmployee(EmployeeType employee) {
            System.out.println("Name: " + employee.getEmployeeFirst() + " "
                    + employee.getEmployeeLast());
            System.out.println("Id: " + employee.getEmployeeId());
            PyList deplist = employee.getDependents();
            int count = deplist.__len__();
            System.out.println("count: " + count);
            for (int idx = 0; idx < count; idx++) {
                PyObject obj = deplist.__getitem__(idx);
                DependentType dep = (DependentType)obj.__tojava__(DependentType.class);
                printDependent(dep);
            }
        }

        private static void printDependent(DependentType dependent) {
            System.out.println("Dep Name: " + dependent.getDependentFirst() + " "
                    + dependent.getDependentLast());
            System.out.println("Dep Id: " + dependent.getDependentId());
        }

        public static void main(String[] args) {
            EmployeeFactory factory = new EmployeeFactory();
            EmployeeType emp = factory.createEmployee("Josh", "Juneau", "1");
            printEmployee(emp);
            printEmployee(factory.createEmployee("Charlie", "Groves", "2"));
            System.out.println("------------------");
            DependentType dependent = factory.createDependent(
                "Dave", "Kuhlman", 4);
            printDependent(dependent);
            System.out.println("------------------");
            emp.addDependent(dependent);
            printEmployee(emp);
        }
    }

Notes:

- This client code creates a factory object, then uses that factory object to create several Java objects that are proxies for the Jython Employee and Dependent objects.

- Then the client code calls several of the methods that are implemented in the Jython code and exposed to Java through the Java interfaces.

- On the Java side, we apply operators to a list object (and other Jython built-in types) by calling their methods directly, for example:

  - `len()` \-- `obj.__len__()`
  - `obj[idx]` \-- `obj.__getitem__(idx)`

  For descriptions of these \"special\" methods, see the following section in the Python language reference: [3.4 Special method names \-- http://docs.python.org/ref/specialnames.html](http://docs.python.org/ref/specialnames.html).

- On the Java side, we use a Jython object by

  1.  Retrieving it as a generic `PyObject`.

  2.  Converting it to a Java object with:

          obj.__tojava__(XXType.class)

      where `XXType` is the Java interface that describes the Jython object.

  3.  Casting the object to the appropriate Java type.

  4.  Calling its \"Java\" methods.

- We can pass a Jython object back to Jython from Java. Notice the call to method `addDependent()`.
:::
:::::::::

::: 
##### [4.1.3   Additional support for running Jython code on an interpreter embedded in Java](#id40)

In what follows, we provide and describe scripts that assist in using the above strategy.

- `generate_interfaces.py` \-- Does some of the work of generating the Java interface files and the Java factory. You will still have to edit the generated files (for example, to fill in type information). But, it may save you a good deal of typing. You can find it here: [Jython/Java interface generator \-- http://www.rexx.com/\~dkuhlman/JythonInterfaceGenerator-1.0a.tar.gz](http://www.rexx.com/~dkuhlman/JythonInterfaceGenerator-1.0a.tar.gz).
:::
::::::::::::

:::::::::::::::: 
#### [4.2   Embedding Jython into Java](#id41)

::: 
##### [4.2.1   Why embedded Jython](#id42)

There are several reasons and purposes for embedding the Jython interpreter into your Java application:

- You want to offer your users the flexibility and power of customizing and extending your application. An embedded Jython interpreter enables them to run Jython scripts in your application and to communicate with it.
- You have existing Jython code, and you want to use that code in your Java application. Note that this is a capability that might have been handled by using the `jythonc` compiler to compile your Jython script into Java code, but `jythonc` is deprecated. For an example of this technique and information on how to do it, see section [Calling Jython from Java](#calling-jython-from-java).

Also see: [Jython User Guide: Embedding Jython - http://jython.org/Project/userguide.html#embedding-jython](http://jython.org/Project/userguide.html#embedding-jython).
:::

::: 
##### [4.2.2   Embedding Jython into Java is simple](#id43)

Embedding the Jython interpreter can be as simple as this:

    // File: SimpleEmbedded.java
    import org.python.util.PythonInterpreter;
    import org.python.core.*;
    import java.io.*;

    public class SimpleEmbedded
    {
        public static void main(String[]args) throws PyException, IOException
        {
            BufferedReader terminal;
            PythonInterpreter interp;
            terminal = new BufferedReader(new InputStreamReader(System.in));
            System.out.println ("Hello");
            interp = new PythonInterpreter();
            interp.exec("import sys");
            interp.exec("print sys");
            interp.set("a", new PyInteger(42));
            interp.exec("print a");
            interp.exec("x = 2+2");
            PyObject x = interp.get("x");
            System.out.println("x: " + x);
            PyObject localvars = interp.getLocals();
            interp.set("localvars", localvars);
            String codeString = "";
            String prompt = ">> ";
            while (true)
            {
                System.out.print (prompt);
                try
                {
                    codeString = terminal.readLine();
                    if (codeString.equals("exit"))
                    {
                        System.exit(0);
                        break;
                    }
                    interp.exec(codeString);
                }
                catch (IOException e)
                {
                    e.printStackTrace();
                }
            }
            System.out.println("Goodbye");
        }
    }
:::

::: 
##### [4.2.3   Passing values into a Jython script](#id44)

Notice the call `interp.set("a", new PyInteger (42));` in the above example.

You can also retrieve the dictionary object representing the namespace for the interpreter, then retrieve objects from that dictionary. Example:

    PyDictionary namespace = interp.getLocals();
    PyObject obj = namespace.__getitem__("x");
    Integer x = obj.__tojava__(Integer.class);
:::

::::: 
##### [4.2.4   Initializing the interpreter](#id45)

You can also create a Jython interpreter with an initial global namespace:

    // File: TestInterp01.java

    import org.python.util.PythonInterpreter;
    import org.python.core.*;
    import java.io.*;

    public class TestInterp01
    {
        public static void main(String[]args) throws PyException, IOException
        {
            PythonInterpreter interp;
            PyString key;
            PyInteger value;
            System.out.println ("Hello");
            PyDictionary table = new PyDictionary();
            key = new PyString("aaa");
            value = new PyInteger(111);
            table.__setitem__(key, value);
            key = new PyString("bbb");
            value = new PyInteger(222);
            table.__setitem__(key, value);
            interp = new PythonInterpreter(table);
            interp.exec("print 'aaa:', aaa");
            interp.exec("print 'bbb:', bbb");
        }
    }

::: 
###### [4.2.4.1   An interpreter with an initial system state](#id46)

And, you can create an interpreter with an initial system state:

    // File: TestInterp02.java

    import org.python.util.PythonInterpreter;
    import org.python.core.*;
    import java.io.*;

    public class TestInterp02
    {
        public static void main(String[]args) throws PyException, IOException
        {
            PythonInterpreter interp;
            PyString key;
            PyInteger value;
            System.out.println ("Hello");
            PyDictionary table = new PyDictionary();
            key = new PyString("aaa");
            value = new PyInteger(111);
            table.__setitem__(key, value);
            key = new PyString("bbb");
            value = new PyInteger(222);
            table.__setitem__(key, value);
            PySystemState state = new PySystemState();
            interp = new PythonInterpreter(table, state);
            interp.exec("print 'aaa:', aaa");
            interp.exec("print 'bbb:', bbb");
        }
    }
:::

::: 
###### [4.2.4.2   A system state and a custom class loader](#id47)

This is of interest because the system state can be used to provide a custom class loader:

    PyDictionary table = new PyDictionary();
    RestrictedClassLoader classLoader = new RestrictedClassLoader();
    PySystemState state = new PySystemState();
    state.setClassLoader(classLoader);
    PythonInterpreter interp = new PythonInterpreter(table, state);

And here is a sample class loader. This one merely restricts the classes that can be loaded to a small set:

    // RestrictedClassLoader.java

    import java.util.ArrayList;

    class RestrictedClassLoader extends ClassLoader {
        ArrayList<String> goodnames;
        public RestrictedClassLoader () {
            goodnames = new Vector();
            goodnames.add("Goodclass1");
            goodnames.add("Goodclass2");
            goodnames.add("Goodclass3");
            goodnames.add("Goodclass4");
        }

        public Class findClass(String name) throws ClassNotFoundException {
            for (String item : goodnames)
            {
                if (item.equals(name))
                {
                    return super.findClass(name);
                }
            }
            throw new ClassNotFoundException("class loading restricted. " +
                name + " not allowed.");
        }
    }
:::
:::::

::: 
##### [4.2.5   Retrieving values from a Jython script](#id48)

Notice the call `PyObject x = interp.get("x");` in the above example.

You can also retrieve the dictionary object representing the namespace for the interpreter, then add and modify the names and their values in that dictionary. Example:

    PyDictionary namespace = interp.getLocals();
    PyInteger value = new PyInteger(144);
    namespace.__setitem__("x", value);
:::

::: 
##### [4.2.6   There are also a few complexities](#id49)

You will want to *selectively* expose capabilities from your Java application to scripts run by/on the embedded Jython interpreter.

You will want to protect your application from malicious or erroneous scripts.

Here are a few suggestions:

- Describe your possible classes of users (those who will write scripts) with respect to (1) trusted vs. untrusted and (2) error tolerant vs. non-tolerant.
- For users who are trusted and error tolerant, provide transparent objects from your application.
- For users who are trusted and not error tolerant, provide opaque objects, i.e. wrappers for real objects from your application.
- For users who are not trusted, implement a security policy, *or* do not expose a scripting interface at all.
:::

::: 
##### [4.2.7   Exposing transparent objects](#id50)

Java application objects and values can be passed through to scripts executed or evaluated by the embedded interpreter.

Some mechanisms for passing objects:

- `set` and `get` \-- Use these to set or retrieve values in the local namespace for the scripts that your embedded interpreter will run or has run.
- `setLocals` and `getLocals` \-- Using these methods, you can pass or retrieve the entire namespace. If you are inserting values to be used (or shared) by scripts, you may want to retrieve and, possibly, copy the initial namespace. Remember that is a Jython dictionary, so modifying it without copying may affect other scripts running in the same interpreter.
:::

::: 
##### [4.2.8   Exposing opaque objects](#id51)

This is similar to the strategy for transparent objects, except that you must implement wrapper classes, then provide instances of these classes instead of instances of transparent objects.
:::

::: 
##### [4.2.9   Type conversion](#id52)

Mostly, Jython takes care of this for you.

However, at times it may help to know what conversions are performed.

And, you can also perform explicit conversions.
:::

::: 
##### [4.2.10   Using a custom class loader](#id53)

You can control access to Java classes with a custom class loader. There is an example in section [A system state and a custom class loader](#a-system-state-and-a-custom-class-loader).
:::

::: 
##### [4.2.11   Embedding a Jython console](#id54)

This example shows how to embed a Jython interactive console into a Java program:

    import org.python.util.InteractiveConsole;
    import java.util.Properties;
    import java.io.*;

    public class interactive_console1 {
        protected InteractiveConsole interp;

        public interactive_console1() {
            if (System.getProperty("python.home") == null) {
                System.setProperty("python.home", "");
            }
            InteractiveConsole.initialize(System.getProperties(),
                                          null, new String[0]);
            interp = new InteractiveConsole();
        }

        public static void main(String[] args) {
            interactive_console1 con = new interactive_console1();
            con.startConsole();
        }

        public void startConsole() {
            interp.interact("Hello from console.");
        }
    }

Notes:

- For more information see: [API information on Class InteractiveConsole \-- http://jython.org/docs/javadoc/org/python/util/InteractiveConsole.html](http://jython.org/docs/javadoc/org/python/util/InteractiveConsole.html).
:::
::::::::::::::::

::::: 
#### [4.3   Embedding Jython with the Java Scripting Engine](#id55)

A scripting engine is an alternative way to execute Jython scripts from within Java.

::: 
##### [4.3.1   Installing script engine support](#id56)

Scripting engine support is here: [scripting Project home \-- https://scripting.dev.java.net/](https://scripting.dev.java.net/)

I downloaded the ScriptEngine support using CVS.

To build support for Jython, I did the following:

    $ cd ${ENGINE_ROOT}/scripting/engines/jython/make/
    $ ant

Then add the following to your CLASSPATH:

    ${ENGINE_ROOT}/scripting/engines/jython/build/jython-engine.jar
:::

::: 
##### [4.3.2   Using script engine support](#id57)

Here is a simple example that (1) displays information about existing script engines and (2) runs several lines of Jython code:

    // File: ScriptEngine1.java

    import java.io.*;
    import java.util.*;
    import javax.script.ScriptEngineManager;
    import javax.script.ScriptEngineFactory;
    import javax.script.ScriptEngine;
    import javax.script.ScriptException;


    public class ScriptEngine1
    {
        public static void main(String[]args) throws IOException, ScriptException
        {
            listEngines(); // Note 1
            ScriptEngineManager mgr = new ScriptEngineManager(); // Note 2
            ScriptEngine eng = mgr.getEngineByName("python");
            System.out.println("eng: " + String.valueOf(eng));
            eng.put("var1", new Integer(257)); // Note 3
            eng.eval("print 'var1: %s' % var1");
            eng.eval("import sys"); // Note 4
            eng.eval("print sys.version");
        }

        public static void listEngines(){ // Note 1
            ScriptEngineManager mgr = new ScriptEngineManager();
            List<ScriptEngineFactory> factories =
                    mgr.getEngineFactories();
            for (ScriptEngineFactory factory: factories) {
                System.out.println("ScriptEngineFactory Info");
                String engName = factory.getEngineName();
                String engVersion = factory.getEngineVersion();
                String langName = factory.getLanguageName();
                String langVersion = factory.getLanguageVersion();
                System.out.println("\tScript Engine: " + engName + ":" +
                                   engVersion);
                List<String> engNames = factory.getNames();
                for(String name: engNames) {
                    System.out.println("\tEngine Alias: " + name);
                }
                System.out.println("\tLanguage: " + langName + ":" +
                                   langVersion);
            }
        }
    }

Notes:

1.  Funtion `listEngines` iterates over each of the available script engines and prints out a bit of information about each one.
2.  We retrieve the Jython script engine.
3.  From Java, we set a variable in the engine/Jython environment, then evaluate a Jython script that prints the value of the variable.
4.  We evaluate several lines of code that import the `sys` module and displays the Jython version number.

This is the result of running the above Java program:

    $ javac ScriptEngine1.java
    $ java ScriptEngine1
    ScriptEngineFactory Info
            Script Engine: jython:2.2b1
            Engine Alias: jython
            Engine Alias: python
            Language: python:2.2b1
    ScriptEngineFactory Info
            Script Engine: Mozilla Rhino:1.6 release 2
            Engine Alias: js
            Engine Alias: rhino
            Engine Alias: JavaScript
            Engine Alias: javascript
            Engine Alias: ECMAScript
            Engine Alias: ecmascript
            Language: ECMAScript:1.6
    eng: com.sun.script.jython.JythonScriptEngine@3caf7a1f
    var1: 257
    2.2.1
:::
:::::

:::::: 
#### [4.4   Compiling Jython code with jythonc](#id58)

::: 
##### [4.4.1   Introduction to jythonc](#id59)

`jythonc` is currently unsupported and is deprecated, although it might reappear in some future version of Jython. Here is a message on this from the jython-users email list:

    Subject: Re: [Jython-users] What will replace jythonc in 2.3
    Date: Thu, 29 Nov 2007 09:29:10 -0500
    From jython-users-bounces@lists.sourceforge.net Thu Nov 29 06:29:17 2007
    From: "Frank Wierzbicki" <fwierzbicki@gmail.com>
    To: "Chris Fenton" <chrisf@fagmed.uit.no>
    Cc: jython-users@lists.sourceforge.net

    On Nov 29, 2007 8:23 AM, Chris Fenton <chrisf@fagmed.uit.no> wrote:
    > I use jythonc regularly to distribute webstart apps for my fellow
    > biologists.
    > If jythonc disappears what is the obvious replacement for generating jars.

    The next Jython is some way off -- but we are aware that there are a
    number of use cases that need to be covered one way or another when
    the old jythonc disappears. Some of them won't require a jythonc at
    all -- I suspect that we can come up with a reasonable jarring
    strategy w/o jythonc. I think we will find that some of the use cases
    are best served by a new version of jythonc -- but one that will be
    based on the same code as the "regular" compiler. This is all tbd
    though -- first we have to get our 2.5 features straightened out on
    the basic compiler.

    -Frank

What `jythonc` does:

- Generates Java code from a Jython class.
- Compiles the generated Java code.
- Packages the compiled Java code in a jar file.

What `jythonc` is (sometimes) used for:

- To generate Java code so that classes written in Jython can be used from Java. But, see section [Calling Jython from Java](#calling-jython-from-java) for an alternative technique.
- To package an application in a jar file for deployment. But, see section [Deployment and Distribution](#deployment-and-distribution) for an alternative technique.
:::

::: 
##### [4.4.2   How to run jythonc](#id60)

Here are examples.

Create a self-contained jar file with `jythonc`:

    $ jythonc -j hello.jar -a TestHello.py

Create java class files that can be imported into Java:

    $ jythonc hello.jar
:::

::: 
##### [4.4.3   Calling Jython from Java using jythonc](#id61)

Preparing Jython code for `jythonc` \-- Create Java compatible Jython modules:

- The Jython class must inherit from a Java class.
- The name of the Jython module and the class in it must be the same. For example, class `Foo` must be in a module named `Foo.py`.
- Add `@sig` directives to methods that you want to be able to call from Java.

Another view: Jython is the extension language for Java.

What is `jythonc` and what is its status?

> \"jythonc transforms Python source code into Java source code then invokes a Java compiler to turn it into .class files. This allows Python to be integrated into Java in several places that regular Jython currently doesn\'t support. It also processes special annotations in docstrings on methods in Python code to determine the static type information to expose when turning a dynmically typed Python method into a statically typed Java method.
>
> \"jythonc is unmaintained and will not be present in Jython-2.3. While jythonc handles all of the language features present in Jython 2.2, it doesn\'t support 2.3 features such as generators. As such, it is not recommended that new Jython projects make use of jythonc. It is only included in Jython-2.2 to support older users of jythonc and to allow access to a few features that are only provided by jythonc at the moment:
>
> 1.  Running in a JVM with a classloader that will not load dynamically created classes
> 2.  Declaring Java method signatures in Python code
> 3.  Loading Python classes dynamically from Java with Class.forName
>
> \"While all of these features are planned for Jython-2.3, they are currently only available from jythonc. Most uses of the second feature, adding method declarations to docstrings, can be handled by declaring a Java interface to implement with a Python class. Each method in the Python implementation takes the types of the Java method it implements. Exposing the Python class as an instance of that type to Java code can be done as explained in Accessing Jython from Java Without Using jythonc and its followup, Simple and Efficient Jython Object Factories.\"
>
> > (See [http://www.jython.org/Project/jythonc.html](http://www.jython.org/Project/jythonc.html))

You can extend Java classes in your Jython code.

You can add (J)Python protocols to Java classes.

You will need to describe the signature of methods in order to make them callable from Java (in addition to Jython).

What `jythonc` does \-- `jythonc` translates `.py` files into `.java` source code files, then compiles these to `.class` files.

With `jythonc`, you can also:

- Compile Jython (.py) to Java class files (.class).

- Compile Jython to Java source, then stop without compiling to `.class` files.

- Create standalone jar file containing your Jython code and that can be run on machines on which Java is installed but not Jython.

- Use a Java compiler different from the default: `javac`. See the help from `jythonc`:

      --compiler path
      -C path
          Use a different compiler than `standard' javac. If this is set to
          `NONE' then compile ends with .java. Alternatively, you can set the
          property python.jpythonc.compiler in the registry.

  This option can also be set in your Jython registry file.

Java compatible classes - In order to implement a Java compatible class (that is, one that acts like a native Java class and can be called from Java), your Jython code must follow these rules:

- Inherit from a Java class or interface.
- Include only one class per module.
- Give the Jython class and the source file that contains it the same name.
- Place all code inside that Jython class.
- Include method signature hints (called sig-strings) \-- Add a `@sig` line in the doc-string for each method.

How to use jythonc:

- Type `jythonc --help` for help:

      $ jythonc --help

- Compile your Jython code with:

      jythonc mymodule.py

Some notes:

- When your run `jythonc`, by default, the `.java` files are placed in a sub-directory `./jpywork`. You can override this with the `--workdir` command line option. From `jythonc --help`:

      --workdir directory
      -w directory
          Specify working directory for compiler (default is ./jpywork)

- When you run this resulting code from Java, the directory `./jpywork` and the Jython jar file must be on your classpath.

Example \-- The following Jython code extends a Java class. Compile it with `jythonc`:

    # Foo.py

    import java

    class Foo(java.util.Date):
        def __init__(self):
            self.count = 0
        def bar(self, incr=1):
            """@sig void bar(int incr)"""
            self.count += incr
            return self.count
        def toString(self):
            cnt = self.bar()
            return "Foo[" + java.util.Date.toString(self) + " " + `cnt` + "]"

Example, continued \-- Here is Java code to test the above. Compile it with `javac` and run it:

    // FooTest.java

    public class FooTest {
         public static void main(String[] args) {
             Foo foo = new Foo();
             System.out.println(foo);
             foo.bar();
             foo.bar(43);
             System.out.println(foo);
         }
    }

Notes:

- You will need to add `jpywork` on your classpath. So, you can compile and run it as follows:

      $ jythonc Foo.py
      $ javac -cp jpywork:$CLASSPATH FooTest.java
      $ java -cp jpywork:$CLASSPATH FooTest

In order to implement a Java compatible class (that is, one that acts like a native Java class and can be called from Java), your Jython code must follow these rules:

- Inherit from a Java class or interface. If you do not need to inherit any additional capability, inherit from `java.lang.Object`.
- Include method signature hints (called sig-strings).
- Give the Jython class and the source file it is in the same name.

Here is another simple example:

    """simpleclass.py

    This is a simple class to demonstrate the use of jythonc.
    """

    import java.lang.Object

    class simpleclass(java.lang.Object):
        def __init__(self, name='The Horse With No Name'):
     """public simpleclass(String name)
     """
     self.name = name
     self.size = -1
        def set_name(self, name):
            """@sig public void set_name(String name)
            """
            self.name = name
        def set_size(self, size):
            """@sig public void set_size(int size)
            """
            self.size = size
        def show(self):
            """@sig public String show()
            """
            return 'name: %s size: %s' % (self.name, self.size, )

    def test():
        sc = simpleclass()
        s1 = sc.show()
        print "1.", s1
        sc.set_name("dave")
        sc.set_size(4321)
        s1 = sc.show()
        print "2.", s1

    if __name__ == '__main__':
        test()

And, a Java test harness for this simple example:

    // simpleclasstest.java

    public class simpleclasstest {
        public static void main(String[] args) {
            String s1;
            simpleclass sc = new simpleclass();
            s1 = sc.show();
            System.out.println("1. " + s1);
            sc.set_name("dave");
            sc.set_size(4321);
            s1 = sc.show();
            System.out.println("2. " + s1);
        }
    }

Notes:

- Compile and run with something like the following:

      $ jythonc simpleclass.py
      $ javac -cp jpywork:$CLASSPATH simpleclasstest.java
      $ java -cp jpywork:$CLASSPATH simpleclasstest
      1. name: The Horse With No Name size: -1
      2. name: dave size: 4321

- You will need to put `jpywork` on your `CLASSPATH`.

- In order to produce a Java compatible class, our Jython class must inherit from a Java class. In this case, we use `java.lang.Object`, because we do not need to inherit any behavior.

- The methods `set_name`, `set_size`, and `show` each have sig-strings.

In the following example, we create a stand-alone Jar file, that is, one that can be executed as a script on a machine where Jython is not installed. Here is the Jython script:

    # test_jythonc.py

    import sys

    def test(words):
        msgs = ['hi', 'bye']
        for word in words:
            msgs.append(word)
        for msg in msgs:
            print msg

    def main():
        args = sys.argv[1:]
        test(args)

    if __name__ == '__main__':
        main()

Compile and build a Jar file with the following:

    $ jythonc --all --jar mytest.jar test_jythonc.py

Run it as follows:

    $ java -jar mytest.jar hello goodbye
    hi
    bye
    hello
    goodbye

Notes:

- Note that our Jython script contains no class. `jythonc` will create a public class and a public static main function for us.
- The `--jar` flag tells `jythonc` that we want the results placed in a Jar file (as opposed to placing it in the work directory `./jpywork`).
- The `--all` flag tells `jythonc` to include all Jython support in the Jar file, making it stand-alone. This enables us to run it on a system where Java is installed but Jython is not.

And the following example builds a standalone jar file from our `simpleclass.py` module, above:

    $ jythonc -j simpleclass.jar -a simpleclass.py
    $ java -jar simpleclass.jar
    1. name: The Horse With No Name size: -1
    2. name: dave size: 4321
:::
::::::
::::::::::::::::::::::::::::::::::

::::::::: 
### [5   Deployment and Distribution](#id62)

Suppose we would like to package our Jython application in a Java jar file, then deploy our application by distributing that jar file so that our users can run it. And, furthermore, suppose we would like our users to be able to run our Jython application on machines where Jython is *not* installed.

This section explains how to do that. This explanation is also at: [Distributing Jython Scripts \-- http://wiki.python.org/jython/JythonFaq/DistributingJythonScripts](http://wiki.python.org/jython/JythonFaq/DistributingJythonScripts).

So, this boils down to:

- Having your scripts (`*.py`) inside standalone jython.jar in the /lib directory

- Having all the classes (`*.class`) in the /org or /com directory

- Having all the jar files you need on the classpath (including standalone `jython.jar`)

- Start java with the `-jar` option. For example:

      $ java -jar jython.jar {optional .py file}

:::::::: 
#### [5.1   Building jars - some samples](#id63)

The following examples assume that you want to build and run your Jython application from a jar file in a way that is \'\'\'not\'\'\' dependent on files in your Jython installation. This will enable your users to run your Jython application (packaged in a jar file) without installing Jython. They will, of course, need Java installed on their machines.

The following example scripts were developed on Linux (and the bash shell), but with minor modifications, you should be able to do the same thing in an MS DOS box on MS Windows. I use the zip/unzip tools available from Info-Zip ([http://www.info-zip.org/](http://www.info-zip.org/)), but other tools that support the zip format should also work.

::: 
##### [5.1.1   Add Jython install stuff to our jar](#id64)

To build our jar, we first make a copy of jython.jar, then add the contents of the `Lib/` directory to it:

    $ cd $JYTHON_HOME
    $ cp jython.jar jythonlib.jar
    $ zip -r jythonlib.jar Lib

Note also that the Jython installer enables you to create a stand-alone jar file.
:::

::: 
##### [5.1.2   Add modules and paths to the jar file](#id65)

Then we copy this expanded jar file, and add modules that are specific to our application. I\'m also going to add a path to an additional jar file to the manifest:

    $ cd $MY_APP_DIRECTORY
    $ cp $JYTHON_HOME/jythonlib.jar myapp.jar
    $ zip myapp.jar Lib/showobjs.py
    # Add path to additional jar file.
    $ jar ufm myapp.jar othermanifest.mf

Where, othermanifest.mf contains the following:

    Class-Path: ./otherjar.jar
:::

::: 
##### [5.1.3   Run the script/jar](#id66)

Now I have a self-contained jar file that I can run by executing the following:

    $ java -jar myapp.jar testmyapp.py

The file `testmyapp.py` imports modules that I have added to `myapp.jar` and `otherjar.jar`, then starts my application.
:::

::: 
##### [5.1.4   A more self-contained jar file](#id67)

Now suppose you want to package your \"start-up\" script in the (main) jar itself. In order to do so, follow the above instructions plus:

- Rename (or copy) your start-up script to `__run__.py`. Add it to the (main) jar file at the root. (On Linux/UNIX you could also do this by using the `ln -s` command to create a symbolic link.) For example, you might do something like this:

      $ zip myapp.jar __run__.py

- Add the path to your jar to your CLASSPATH environment variable.

Now you can run your application with the following:

    $ java org.python.util.jython -jar myapp.jar

Notice how, when we start the application, we specify the jython class (`org.python.util.jython`) on the command line. That starts the Jython interpreter, which looks for and runs our `__run__.py` script.

Alternatively, instead of adding your standalone jar to the `CLASSPATH` environment variable, you can use the `-cp` or `-classpath` command line options:

    $ java -cp myapp.jar org.python.util.jython -jar myapp.jar

And, a shorter form which does the same thing is this:

    $ java -jar myapp.jar -jar myapp.jar

This works because Java and Jython *both* have `-jar` options. The first `-jar` tells Java to run Jython, and the second `-jar` tells Jython to run the `__run__.py` in the jar file.
:::

::: 
##### [5.1.5   A summary](#id68)

Create the basic jar:

    $ cd $JYTHON_HOME
    $ cp jython.jar jythonlib.jar
    $ zip -r jythonlib.jar Lib

Add other modules to the jar:

    $ cd $MY_APP_DIRECTORY
    $ cp $JYTHON_HOME/jythonlib.jar myapp.jar
    $ zip myapp.jar Lib/showobjs.py
    # Add path to additional jar file.
    $ jar ufm myapp.jar othermanifest.mf

For a more self-contained jar, add the `__run__.py` module:

    # Copy or rename your start-up script.
    $ cp mymainscript.py __run__.py
    # Add your start-up script (__run__.py) ot the jar.
    $ zip myapp.jar __run__.py
    # Add path to main jar to the CLASSPATH environment variable.
    $ export CLASSPATH=/path/to/my/app/myapp.jar:$CLASSPATH

On MS Windows, that last line, setting the `CLASSPATH` environment variable, would look something like this:

    set CLASSPATH=C:\path\to\my\app\myapp.jar;%CLASSPATH%

Or, again on MS Windows, use the Control Panel and the System properties to set the CLASSPATH environment variable.

Run the application:

    $ java -jar myapp.jar mymainscript.py arg1 arg2

Or, if you have added your start-up script to the jar, use one of the following:

    $ java org.python.util.jython -jar myapp.jar arg1 arg2

    $ java -cp myapp.jar org.python.util.jython -jar myapp.jar arg1 arg2

    $ java -jar myapp.jar -jar myapp.jar arg1 arg2
:::
::::::::
:::::::::

::: 
### [6   Integrating, Embedding, and Extending \-- A Summary](#id69)

Here is what we have learned to do:

- Import and use Java classes in Jython.
- Extend a Java class in Jython.
- Implement Java classes that are more \"Jythonic\" and that expose Jython features such as doc-strings, inherit and extend Jython classes (for example, PyList, PyDict, etc.).
- Call Jython code from Java.
- Embed a Jython interpreter in a Java application.
- Package and deploy a Jython application as a jar file.
:::

:::::::::::::::: 
### [7   Jython+Java \-- Other Advanced Topics](#id70)

::: 
#### [7.1   Event handling](#id71)

Events are easy in Jython.

Here is an example taken from \"An Introduction to Jython\" ([http://www.javalobby.org/articles/jython/](http://www.javalobby.org/articles/jython/)):

    from javax.swing import *

    def hello(event):
        print "Hello. I'm an event."

    def test():
        frame = JFrame("Hello Jython")
        button = JButton("Hello", actionPerformed = hello)
        frame.add(button)
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        frame.setSize(300, 300)
        frame.show()

    test()
:::

::::::::::: 
#### [7.2   XML](#id72)

::: 
##### [7.2.1   jaxp](#id73)

Note: Tested with jython-2.2a.

Example:

    """

    To run this example, set your CLASSPATH with something like the following:

        export CLASSPATH=\
        ${path-to-xerces}/xerces-2_8_0/xercesImpl.jar:\
        ${path-to-xerces}/xerces-2_8_0/xml-apis.jar


    """


    import sys
    import java.lang.Boolean
    from javax.xml.parsers import DocumentBuilderFactory


    def test(infilename):
        """Parse XML document and show attributes and names.
        """
        dbf = DocumentBuilderFactory.newInstance()
        t = java.lang.Boolean(1)
        dbf.setNamespaceAware(t)
        db = dbf.newDocumentBuilder();
        doc = db.parse(infilename)
        # print dir(doc)
        node = doc.getDocumentElement()
        print 'Attributes:'
        show_attrs(node)
        print 'Names:'
        show_names(node)


    def show_attrs(node):
        """Show the attributes and their values.
        """
        node = node.getFirstChild()
        while node:
            if node.getNodeType() == node.ELEMENT_NODE:
                print ' %s:' % (node.getTagName(), )
                attrs = node.getAttributes()
                count = attrs.getLength()
                for idx in range(count):
                    attr = attrs.item(idx)
                    print ' %s: %s' % (
                        attr.getNodeName(), attr.getNodeValue(), )
            node = node.getNextSibling()


    def show_names(node):
        """Show the value of the name element for each person element.
        """
        node = node.getFirstChild()
        while node:
            if (node.getNodeType() == node.ELEMENT_NODE and
                node.getTagName() == 'person'):
                    show_person_name(node)
            node = node.getNextSibling()


    def show_person_name(node):
        node = node.getFirstChild()
        while node:
            if (node.getNodeType() == node.ELEMENT_NODE and
                node.getTagName() == 'name'):
                    show_text('name: ', node)
            node = node.getNextSibling()


    def show_text(msg, node):
        """Show a message and the value of a text node.
        """
        node = node.getFirstChild()
        while node:
            if node.getNodeType() == node.TEXT_NODE:
                print ' %s %s' % (msg, node.getNodeValue(), )
            node = node.getNextSibling()


    def usage():
        print 'Usage: jython test_jaxp.py <infilename>'
        sys.exit(-1)


    def main():
        args = sys.argv[1:]
        if len(args) != 1:
            usage()
        test(args[0])


    if __name__ == '__main__':
        main()

Resources:

- [jaxp: JAXP Reference Implementation](https://jaxp.dev.java.net/) ([https://jaxp.dev.java.net/](https://jaxp.dev.java.net/)).
- [Java API for XML Processing (JAXP)](http://java.sun.com/webservices/jaxp/index.jsp) ([http://java.sun.com/webservices/jaxp/index.jsp](http://java.sun.com/webservices/jaxp/index.jsp)).
:::

::: 
##### [7.2.2   Xerces](#id74)

Xerces is an implementation of XML parsers and a lot more. The JAXP API is also implemented in Xerces2.

Obtain Xerces here: [http://xerces.apache.org/xerces2-j/download.cgi](http://xerces.apache.org/xerces2-j/download.cgi).

Installation instructions are here: [Installation Instructions](http://xerces.apache.org/xerces2-j/install.html).

Set-up \-- Set your CLASSPATH. After unpacking the Xerces distribution, add the following jar files to your CLASSPATH:

- xercesImpl.jar
- xml-apis.jar

Here is an example that uses the Xerces DOM parser to parse an XML document, then print out information about the top level nodes in the document:

    from org.apache.xerces.parsers import DOMParser as dp

    def test():
        parser = dp()
        parser.parse('people.xml')
        doc = parser.getDocument()
        node = doc.getFirstChild()
        node = node.getFirstChild()
        while node:
            if node.getNodeType() == node.ELEMENT_NODE:
                print node.getTagName()
                attrs = node.getAttributes()
                count = attrs.getLength()
                for idx in range(count):
                    attr = attrs.item(idx)
                    print ' %s: %s' % (attr.getNodeName(), attr.getNodeValue(),)
            node = node.getNextSibling()

    if __name__ == '__main__':
        test()

Here is another example. This one also prints out the text values of the `name` elements:

    """

    To run this example, set your CLASSPATH with something like the following:

        export CLASSPATH=\
        ${path-to-jython2.2a}/jython.jar:\
        ${path-to-xerces}/xerces-2_8_0/xercesImpl.jar:\
        ${path-to-xerces}/xerces-2_8_0/xml-apis.jar


    """


    import sys
    from org.apache.xerces.parsers import DOMParser as dp


    def test(infilename):
        """Parse XML document and show attributes and names.
        """
        parser = dp()
        parser.parse(infilename)
        doc = parser.getDocument()
        node = doc.getFirstChild()
        print 'Attributes:'
        show_attrs(node)
        print 'Names:'
        show_names(node)


    def show_attrs(node):
        """Show the attributes and their values.
        """
        node = node.getFirstChild()
        while node:
            if node.getNodeType() == node.ELEMENT_NODE:
                print ' %s:' % (node.getTagName(), )
                attrs = node.getAttributes()
                count = attrs.getLength()
                for idx in range(count):
                    attr = attrs.item(idx)
                    print ' %s: %s' % (
                        attr.getNodeName(), attr.getNodeValue(), )
            node = node.getNextSibling()


    def show_names(node):
        """Show the value of the name element for each person element.
        """
        node = node.getFirstChild()
        while node:
            if (node.getNodeType() == node.ELEMENT_NODE and
                node.getTagName() == 'person'):
                    show_person_name(node)
            node = node.getNextSibling()


    def show_person_name(node):
        node = node.getFirstChild()
        while node:
            if (node.getNodeType() == node.ELEMENT_NODE and
                node.getTagName() == 'name'):
                    show_text('name: ', node)
            node = node.getNextSibling()


    def show_text(msg, node):
        """Show a message and the value of a text node.
        """
        node = node.getFirstChild()
        while node:
            if node.getNodeType() == node.TEXT_NODE:
                print ' %s %s' % (msg, node.getNodeValue(), )
            node = node.getNextSibling()


    def usage():
        print 'Usage: jython test_xerces.py <infilename>'
        sys.exit(-1)


    def main():
        args = sys.argv[1:]
        if len(args) != 1:
            usage()
        test(args[0])


    if __name__ == '__main__':
        main()

Notes:

- Except for the parser set-up (in function `test`), this example is almost the same as the JAXP example. For the most part, it uses the same API.

Resources:

- [Xerces Java Parser](http://xerces.apache.org/xerces2-j/)
- [Introduction to XML and XML With Java](http://totheriver.com/learn/xml/xmltutorial.html)
:::

::::: 
##### [7.2.3   dom4j](#id75)

::: 
###### [7.2.3.1   Installation and setup](#id76)

- Download `dom4j` from: [dom4j: the flexible XML framework for Java \-- http://www.dom4j.org/](http://www.dom4j.org/)
- Add the `dom4j` jar file to your `CLASSPATH`.
- In order to get some features to work, I also had to install the `jaxen` XPath engine. Add that to your `CLASSPATH`, too. See: [jaxen: universal Java XPath engine \-- http://jaxen.codehaus.org/](http://jaxen.codehaus.org/).
:::

::: 
###### [7.2.3.2   Examples etc](#id77)

There are examples at:

- [dom4j - Quick Start Guide \-- http://www.dom4j.org/guide.html](http://www.dom4j.org/guide.html)
- [dom4j cookbook \-- http://www.dom4j.org/cookbook.html](http://www.dom4j.org/cookbook.html)

Example 1a \-- This example parses an XML document (file), then walks the `dom4j` DOM element tree and prints out information on each node:

    import sys
    from org.dom4j.io import SAXReader

    def show_indent(level):
        return ' ' * level

    def show_node(node, level):
        """Display one node in the DOM tree.
        """
        if node.getNodeType() == node.ELEMENT_NODE:
            name = node.getName()
            print '%sElement node: %s' % (show_indent(level), name, )
            attrs = node.attributes()
            for attr in attrs:
                aName = attr.getQualifiedName()
                aValue = attr.getValue()
                print ' %sAttr -- %s: %s' % (show_indent(level), aName, aValue,)
            if node.text:
                print ' %sText: "%s"' % (show_indent(level), node.text,)

    def show_tree(node, level):
        show_node(node, level)
        level1 = level + 1
        if node.getNodeType() == node.ELEMENT_NODE:
            children = node.elements()
            for child in children:
                show_tree(child, level1)

    def test(infilename):
        print 'Version: %s' % (sys.version, )
        reader = SAXReader()
        doc = reader.read(infilename)
        root = doc.getRootElement()
        show_tree(root, 0)

    def main():
        args = sys.argv[1:]
        if len(args) != 1:
            print 'usage: test_dom4j_2.py in_xml_file'
            sys.exit(1)
        test(args[0])

    if __name__ == '__main__':
        #import pdb; pdb.set_trace()
        main()

Notes:

- We use `node.elements()` to get all children that are *elements*, but not, for example, text nodes.

Example 1b \-- This example also parses an XML document (file), then walks the `dom4j` DOM element tree and prints out information on each node. However, at each node it iterates over *all* the content nodes, including text nodes:

    import sys
    from org.dom4j.io import SAXReader

    def show_indent(level):
        return ' ' * level

    def show_node(node, level):
        """Display one node in the DOM tree.
        """
        if node.getNodeType() == node.ELEMENT_NODE:
            name = node.getName()
            print '%sElement node: %s' % (show_indent(level), name, )
            attrs = node.attributes()
            for attr in attrs:
                aName = attr.getQualifiedName()
                aValue = attr.getValue()
                print ' %sAttr -- %s: %s' % (show_indent(level), aName, aValue,)
        elif node.getNodeType() == node.TEXT_NODE:
            print '%sText node: "%s"' % (show_indent(level), node.text, )

    def show_tree(node, level):
        show_node(node, level)
        level1 = level + 1
        if node.getNodeType() == node.ELEMENT_NODE:
            children = node.content()
            for child in children:
                show_tree(child, level1)

    def test(infilename):
        print 'Version: %s' % (sys.version, )
        reader = SAXReader()
        doc = reader.read(infilename)
        root = doc.getRootElement()
        show_tree(root, 0)

    def main():
        args = sys.argv[1:]
        if len(args) != 1:
            print 'usage: test_dom4j_2.py in_xml_file'
            sys.exit(1)
        test(args[0])

    if __name__ == '__main__':
        #import pdb; pdb.set_trace()
        main()

Notes:

- We use `node.content()` to get *all* child nodes, *including* text nodes.

- Use tests such as the following to determine whether a node is an element node or a text node:

      if node.getNodeType() == node.ELEMENT_NODE:
          o
          o
          o
      elif node.getNodeType() == node.TEXT_NODE:
          o
          o
          o

Example 2 \-- This example creates an `dom4j` document object and adds element objects to it:

    import sys
    import org.dom4j.DocumentHelper
    import org.dom4j.io.OutputFormat
    from org.dom4j.io import XMLWriter
    from org.dom4j.io import OutputFormat

    def test():
        # 1.
        # Create a new document and add a few elements to it.
        doc = org.dom4j.DocumentHelper.createDocument()
        root = doc.addElement('specs')
        e1 = root.addElement('class1')
        e1.addAttribute('name', 'dave')
        e1.addAttribute('category', 'medium')
        e1.addText('some simple content')
        e1 = root.addElement('class2')
        e1.addAttribute('name', 'mona')
        e1.addAttribute('category', 'good')
        e1.addText('more content')
        # 2.
        # Print a text representation of the DOM tree.
        text = doc.asXML()
        print text
        print '\n', '-' * 40, '\n'
        # 3.
        # Print a formatted (pretty-print) representation.
        format = OutputFormat.createPrettyPrint()
        writer = XMLWriter(sys.stdout, format)
        writer.write(doc)
        print '\n', '-' * 40, '\n'
        print 'root:', root, '\n'
        # 4.
        # Iterate over the children of the root.
        # Print child and parent names, etc.
        itr = root.elementIterator()
        for idx, child in enumerate(itr):
            print idx, child
            parent = child.getParent()
            print 'parent:', parent.getName()
            print 'child:', child.getName()
            print 'text: "%s"' % child.getText()
            print

    test()

Notes \-- What this example does:

1.  Creates a new document and adds a few elements to it.
2.  Produces and prints a text representation of the DOM tree.
3.  Prints a formatted (pretty-print) representation.
4.  Iterates over the children of the root. Prints child and parent names, etc.

Resources:

- [http://www.dom4j.org/](http://www.dom4j.org/)
- [http://www.dom4j.org/dom4j-1.4/apidocs/index.html](http://www.dom4j.org/dom4j-1.4/apidocs/index.html)
:::
:::::

::::: 
##### [7.2.4   XMLBeans](#id78)

XMLBeans provides the ability to generate Java bindings for an XML document type from an XML Schema. Roughly speaking, XMLBeans generates a Java class for each element type defined in an XML Schema.

When used with Jython, those Java bindings become quite Jythonic.

You can read about XMLBeans here:

- [Welcome to XMLBeans \-- http://xmlbeans.apache.org/index.html](http://xmlbeans.apache.org/index.html).
- [XMLBeans at Wikipedia \-- http://en.wikipedia.org/wiki/XMLBeans](http://en.wikipedia.org/wiki/XMLBeans).

::: 
###### [7.2.4.1   Installation](#id79)

You can find XMLBeans at: [Welcome to XMLBeans \-- http://xmlbeans.apache.org/index.html](http://xmlbeans.apache.org/index.html).

To install XMLBeans, follow the instructions at: [Installing XMLBeans \-- http://xmlbeans.apache.org/documentation/conInstallGuide.html](http://xmlbeans.apache.org/documentation/conInstallGuide.html).

After unrolling the binary distribution, I added the following to my `CLASSPATH`:

- \$XMLBEANS_HOME/lib/xbean.jar
- \$XMLBEANS_HOME/lib/jsr173_1.0_api.jar

And, I added the following to my `PATH` environment variable:

- \$XMLBEANS_HOME/bin

where XMLBEANS_HOME is the directory in which XMLBeans is installed.
:::

::: 
###### [7.2.4.2   An example](#id80)

This example was copied from [XMLBeans at Wikipedia \-- http://en.wikipedia.org/wiki/XMLBeans](http://en.wikipedia.org/wiki/XMLBeans) and then adapted to Jython.

The XML Schema:

    <?xml version="1.0" encoding="UTF-8"?>
    <xs:schema targetNamespace="http://www.openuri.org/domain/country/v1"
               xmlns:tns="http://www.openuri.org/domain/country/v1"
               xmlns:xs="http://www.w3.org/2001/XMLSchema"
               elementFormDefault="qualified"
               attributeFormDefault="unqualified"
               version="1.0">
      <xs:element name="Country" type="tns:Country"/>
      <xs:complexType name="Country">
        <xs:sequence>
          <xs:element name="Name" type="xs:string"/>
          <xs:element name="Population" type="xs:int"/>
          <xs:element name="Iso" type="tns:Iso"/>
        </xs:sequence>
      </xs:complexType>
      <xs:complexType name="Iso">
        <xs:annotation><xs:documentation>ISO 3166</xs:documentation></xs:annotation>
        <xs:sequence>
          <xs:element name="Alpha2" type="tns:IsoAlpha2"/>
          <xs:element name="Alpha3" type="tns:IsoAlpha3"/>
          <xs:element name="CountryCode" type="tns:IsoCountryCode"/>
        </xs:sequence>
      </xs:complexType>
      <xs:simpleType name="IsoCountryCode">
        <xs:restriction base="xs:int">
          <xs:totalDigits value="3"/>
        </xs:restriction>
      </xs:simpleType>
      <xs:simpleType name="IsoAlpha2">
        <xs:restriction base="xs:string">
          <xs:pattern value="[A-Z]{2}"/>
          <xs:whiteSpace value="collapse"/>
        </xs:restriction>
      </xs:simpleType>
      <xs:simpleType name="IsoAlpha3">
        <xs:restriction base="xs:string">
          <xs:pattern value="[A-Z]{3}"/>
          <xs:whiteSpace value="collapse"/>
        </xs:restriction>
      </xs:simpleType>
    </xs:schema>

Supposing that you name the above schema `country.xsd`, you can compile this with XMLBeans using something like the following:

    $ scomp -out country.jar country.xsd

Here is a bit of Java code, copied from Wikipedia, that uses the generated Java classes:

    import org.openuri.domain.country.v1.Country;
    import org.openuri.domain.country.v1.Iso;
    public class CountrySample
    {
      public static void main(String[] args) {
        Country country = Country. Factory.newInstance();
        country.setName("Denmark");
        country.setPopulation(5450661); // from wikipedia :-)
        // print out country XMLBean as XML
        System.out.println(country.xmlText());
        // check if document is valid - will print "Document is invalid"
        // because required Iso child element in not in the object
        System.out.println ("Document is " + (country.validate() ? "valid" : "invalid"));
        // add child with complex type Iso to make the document valid
        Iso iso = country.addNewIso();
        iso.setAlpha2("DK");
        iso.setAlpha3("DNK");
        iso.setCountryCode(208);
        // print out country XMLBean as XML
        System.out.println(country.xmlText());
        // check if document is valid - will print "Document is valid"
        System.out.println ("Document is " + (country.validate() ? "valid" : "invalid"));
      }
    }

After translation to Jython, here is the equivalent code. Note that it uses the same generated Java classes as the above Java code:

    from org.openuri.domain.country.v1 import Country
    from org.openuri.domain.country.v1 import Iso
    from org.apache.xmlbeans import XmlOptions

    class CountrySample(object):

        def main(self, args):
            country = Country.Factory.newInstance()
            country.setName("Denmark")
            country.setPopulation(5450661); # from wikipedia :-)
            # Print out country XMLBean as XML.
            print country.xmlText()
            # Print out country XMLBean as XML with indentation.
            opts = XmlOptions()
            opts.setSavePrettyPrint()
            opts.setSavePrettyPrintIndent(4)
            print country.xmlText(opts)
            # Check if document is valid - will print "Document is invalid"
            # because required Iso child element in not in the object.
            if country.validate():
                condition = "valid"
            else:
                condition = "invalid"
            print "Document is", condition
            # Add child with complex type Iso to make the document valid.
            iso = country.addNewIso();
            iso.setAlpha2("DK")
            iso.setAlpha3("DNK")
            iso.setCountryCode(208)
            # Print out country XMLBean as XML.
            print country.xmlText(opts)
            # Check if document is valid - will print "Document is valid".
            if country.validate():
                condition = "valid"
            else:
                condition = "invalid"
            print "Document is", condition

    def test():
        country_sample = CountrySample()
        country_sample.main([])

    test()

Add the generated jar file to your CLASSPATH. In Linux, I can do that with the following:

    $ export CLASSPATH=$CLASSPATH:./country.jar

Now run it:

    $ jython test_xml.py

And, that prints out:

    <xml-fragment><v1:Name xmlns:v1="http://www.openuri.org/domain/country/v1">Denmark</v1:Name><v1:Population xmlns:v1="http://www.openuri.org/domain/country/v1">5450661</v1:Population></xml-fragment>
    <xml-fragment>
        <v1:Name xmlns:v1="http://www.openuri.org/domain/country/v1">Denmark</v1:Name>
        <v1:Population xmlns:v1="http://www.openuri.org/domain/country/v1">5450661</v1:Population>
    </xml-fragment>
    Document is invalid
    <xml-fragment>
        <v1:Name xmlns:v1="http://www.openuri.org/domain/country/v1">Denmark</v1:Name>
        <v1:Population xmlns:v1="http://www.openuri.org/domain/country/v1">5450661</v1:Population>
        <v1:Iso xmlns:v1="http://www.openuri.org/domain/country/v1">
            <v1:Alpha2>DK</v1:Alpha2>
            <v1:Alpha3>DNK</v1:Alpha3>
            <v1:CountryCode>208</v1:CountryCode>
        </v1:Iso>
    </xml-fragment>
    Document is valid
:::
:::::
:::::::::::

::::: 
#### [7.3   Database access](#id81)

::: 
##### [7.3.1   JDBC](#id82)

JDBC is Java classes. It is, therefore, usable from Jython.

You will need JDBC driver/adapters for your database.

But, JDBC is not very Pythonic.
:::

::: 
##### [7.3.2   zxJDBC](#id83)

zxJDBC *is* Pythonic. zxJDBC implements the Python DB API on top of JDBC. For more on the Python DB API, see [SIG on Tabular Databases in Python](http://python.org/sigs/db-sig/) and [Python Database API Specification v2.0](http://python.org/peps/pep-0249.html).

If zxJDBC is not already in your installed version of Jython, then you can:

1.  Downloading the source from [http://sourceforge.net/projects/zxjdbc](http://sourceforge.net/projects/zxjdbc).
2.  Creating a directory (e.g. `zxJDBC`), then un-rolling it.
3.  Add `zxJDBC/lib/zxJDBC.jar` to your `CLASSPATH`

You can get documentation on zxJDBC by:

1.  Downloading the source from [http://sourceforge.net/projects/zxjdbc](http://sourceforge.net/projects/zxjdbc).
2.  Creating a directory (e.g. `zxJDBC`), then un-rolling it.
3.  Pointing your browser at `zxJDBC/doc/index.html`.

Example \-- The following example opens a connection to a PostgreSQL database, then prints out the rows in a table in that database. In order to make this example work, I put the following jar files on my `CLASSPATH`:

- `zxJDBC.jar` \-- Not needed for Jython 2.2, and possibly not needed for the version of Jython 2.1 on your machine. JDBC support has been folded into Jython 2.1 and Jython 2.2a.
- `postgresql-8.1-407.jdbc3.jar` \-- You will need a suitable driver for your database and version.

Here is the example implementation:

    """

    For this test, add the JDBC driver to your CLASSPATH. For example,
    in my case I added:

        postgresql-8.2-506.jdbc4.jar

    """

    from com.ziclix.python.sql import zxJDBC

    def test():
        d, u, p, v = (
            "jdbc:postgresql://thrush:5432/test", # ... host, port, database
            "postgres", # user name
            "mypassword", # pass word
            "org.postgresql.Driver", # driver
            )
        db = zxJDBC.connect(d, u, p, v, CHARSET='iso_1')
        cur = db.cursor()
        cur.execute('select * from plant_db')
        rows = cur.fetchall()
        s1 = '%s %s %s' % (
            'Name'.ljust(12),
            'Description'.ljust(24),
            'Rating'.ljust(10),
            )
        print s1
        s1 = '%s %s %s' % (
            '===='.ljust(12),
            '==========='.ljust(24),
            '======'.ljust(10),
            )
        print s1
        for row in rows:
            rating = str(row[2])
            print '%s %s %s' % (
                row[0].ljust(12), row[1].ljust(24), rating.ljust(10), )
        cur.close()
        db.close()

    if __name__ == '__main__':
        test()

Which, when connected to my trivial, little database, prints out the following:

    Name Description Rating
    ==== =========== ======
    tomato red and tasty 8
    peach sweet and succulent 8
    tangerine sweet but tart 7

Resources:

- More information on zxJDBC: [http://jython.org/Project/userguide.html#database-connectivity-in-jython](http://jython.org/Project/userguide.html#database-connectivity-in-jython)
- The JDBC driver for PostgreSQL: [http://jdbc.postgresql.org/](http://jdbc.postgresql.org/)
- The JDBC driver for MySQL: [http://www.mysql.com/products/connector/j/](http://www.mysql.com/products/connector/j/)
- [Python Tabular Databases SIG: Status \-- http://www.python.org/community/sigs/current/db-sig/status/](http://www.python.org/community/sigs/current/db-sig/status/)
- The Python [Database Topic Guide \-- http://www.python.org/doc/topics/database/](http://www.python.org/doc/topics/database/)
:::
:::::
::::::::::::::::

::: 
### [8   Additional Exercises](#id84)

\[To be added.\]
:::

::: 
### [9   References and Sources](#id85)

Introductory articles:

- [An Introduction to Jython](http://www.javalobby.org/articles/jython/): An introductory article on Jython
- [alt.lang.jre: Get to know Jython](http://www-128.ibm.com/developerworks/library/j-alj07064/index.html): An introduction to Jython that includes a summary of Jython features.
- [Use Jython to Exercise Java APIs Without Compiling](http://www.devx.com/Java/Article/27571/1954?pf=true): Another introduction with an emphasis on the use of Java classes.
- [Charming Jython](http://www-128.ibm.com/developerworks/java/library/j-jython.html): Yet another introductory article.
- [Scripting Languages For Java](http://www.ociweb.com/jnb/archive/jnbMar2001.html): A comparison of scripting languages for Java.

Thanks to David Goodger for the following list or references. His \"Code Like a Pythonista: Idiomatic Python\" ([http://python.net/\~goodger/projects/pycon/2007/idiomatic/](http://python.net/~goodger/projects/pycon/2007/idiomatic/)) is worth a careful reading:

- \"Python Objects\", Fredrik Lundh, [http://www.effbot.org/zone/python-objects.htm](http://www.effbot.org/zone/python-objects.htm)
- \"How to think like a Pythonista\", Mark Hammond, [http://python.net/crew/mwh/hacks/objectthink.html](http://python.net/crew/mwh/hacks/objectthink.html)
- \"Python main() functions\", Guido van Rossum, [http://www.artima.com/weblogs/viewpost.jsp?thread=4829](http://www.artima.com/weblogs/viewpost.jsp?thread=4829)
- \"Python Idioms and Efficiency\", [http://jaynes.colorado.edu/PythonIdioms.html](http://jaynes.colorado.edu/PythonIdioms.html)
- \"Python track: python idioms\", [http://www.cs.caltech.edu/courses/cs11/material/python/misc/python_idioms.html](http://www.cs.caltech.edu/courses/cs11/material/python/misc/python_idioms.html)
- \"Be Pythonic\", Shalabh Chaturvedi, [http://shalabh.infogami.com/Be_Pythonic2](http://shalabh.infogami.com/Be_Pythonic2)
- \"Python Is Not Java\", Phillip J. Eby, [http://dirtsimple.org/2004/12/python-is-not-java.html](http://dirtsimple.org/2004/12/python-is-not-java.html)
- \"What is Pythonic?\", Martijn Faassen, [http://faassen.n\--tree.net/blog/view/weblog/2005/08/06/0](http://faassen.n--tree.net/blog/view/weblog/2005/08/06/0)
- \"Sorting Mini-HOWTO\", Andrew Dalke, [http://wiki.python.org/moin/HowTo/Sorting](http://wiki.python.org/moin/HowTo/Sorting)
- \"Python Idioms\", [http://www.gungfu.de/facts/wiki/Main/PythonIdioms](http://www.gungfu.de/facts/wiki/Main/PythonIdioms)
- \"Python FAQs\", [http://www.python.org/doc/faq/](http://www.python.org/doc/faq/)
:::
