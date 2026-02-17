# JythonFaq/InstallingJython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Installation and Setup 

[JythonFaq](JythonFaq)

## Command-line support in Jython? 

Jython 2.5 and 2.7 fully support command-line history using JLine, although there are circumstances in which JLine cannot be loaded. (This is currently the case on cygwin for Jython 2.7.0.)

Jython 2.7 also supports tab completion.

------------------------------------------------------------------------

## Why do I get the error, \"can\'t create package cache dir, \'/cachedir/packages\'\" 

An essential optimization in Jython is the caching of Java package information. The caching requires \'/cachedir/packages/\' in the python.home directory. It is often the case on \*nix that users lack sufficient priveledges to create or write to this directory.

Because the problem is merely permissions, something similar to \"mkdir cachedir; chmod a+rw cachedir\" within Jython\'s directory should eliminate this error message.

If you are using Windows, the solution is even easier. The value you have set for the \"-Dpython.home\" in your startup doesn\'t exist. Either correct the typo or create that directory.

------------------------------------------------------------------------

## Where\'s the registry file 

Jython\'s installation includes a file called \"registry\" that you will find in the root directory of the Jython installation (e.g. /usr/local/jython or c:\\jython).

At initialization, Jython searches for the \"registry\" file in the directory specified by the \"python.home\" property, or the \".jython\" file in the user\'s home directory.

The \"python.home\" property is often set in the startup with Java\'s -D switch. The shell script that starts Jython (jython.bat or jython) demonstrates the use of the -D switch to set the \"python.home\" property. When embedding Jython, it is often still best to use the -D switch because the -D properties appear in System.getProperties(), which is usually the \"preProperties\" (first arg) in the static [PythonInterpreter](./PythonInterpreter.html).initialize method. With python.home in the preProperties, the interpreter successfully loads preProperties, registry properties, and postProperties (the second arg to initialize) in the correct order.

If you wish to use your home directory, and do not know where your home directory is, don\'t worry- Jython knows:

` >>> print java.lang.System.getProperty("user.home") `

If you run into complaints about create \".jython\", don\'t worry- Jython can:

     >>> import java, os
     >>> filename = os.path.join(java.lang.System.getProperty("user.home"), ".jython")
     >>> open(filename, "w")

------------------------------------------------------------------------

## GUI-less installer? 

Run

` java -jar jython-installer.jar --help `

for full help, including text console and command line installation.

------------------------------------------------------------------------

## Jython cannot find your Java class, even though it exists in the CLASSPATH. 

Jython cannot find your Java class, even though it exists in the class path. This shows up as \"[ImportError](./ImportError.html): cannot import name xxx\" or \"[AttributeError](./AttributeError.html): java package xxx\' has no attribute \'yyy\'\"

This happens when Jython is run using java -jar jython.jar. Use the Jython launcher (bin/jython or bin\\jython.exe) to ensure that the Jython jar is on the CLASSPATH.
