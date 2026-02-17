# ConsoleChoices

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Contents**

# The Console 

Left to itself, a Java program simply reads and writes characters at the console through JVM-provided streams. This plain behaviour may be augmented by the command window on your system with some line-editing capability (such as using the cursor keys to revisit a typo back up the line), or the ability to recall previously entered lines. On Unix-like systems it is common for a shell or console application to use a library that provides sophisticated editing and line recall, while the console itself provides little more than a line buffer with delete. On Windows, the command window provides basic editing and recall, from which applications benefit without further effort.

In order to privide a common behaviour across platforms, the Jython interpreter (the one that gives you the Python `>>> `{.backtick} prompt) will access the console through a library called JLine, when it detects that the console is interactive. You may choose otherwise.

The choice of console affects interactions with the user through `sys,stdin`{.backtick}, `sys.stdout`{.backtick} and `raw_input()`{.backtick}. `raw_input()`{.backtick} always uses the other two streams to issue its prompt and read your response. The Python prompt `>>> `{.backtick} is issued through `raw_input()`{.backtick}.

## Choosing a Console (jython command) 

The console is chosen by naming a class in the Jython setting `python.console`{.backtick} (see [Settings](Settings)). The sources of this setting, in descending order of precedence are:

1.  Java System properties (including a command-line `-Dpython.console=`{.backtick} option).

2.  The Jython registry.

3.  The default value `org.python.util.JLineConsole`{.backtick} set by the jython program.

The default Jython registry makes no setting of `python.console`{.backtick} so if you do not set `python.console`{.backtick} on the command line you will get a JLineConsole. If you specify a class that cannot be found, or some other error occurs while loading and initialising the alleged console, you will get a non-fatal error and a PlainConsole.

## Choosing a Console (embedded interpreter) 

The console is chosen by naming a class in the Jython setting `python.console`{.backtick} (see [Settings](Settings)). The sources of this setting, in descending order of precedence are:

1.  The Jython registry.

2.  Java System properties (including a command-line `-Dpython.console=`{.backtick} option).

If `python.console`{.backtick} remains undefined the console class is `org.python.core.PlainConsole`{.backtick}.

The default Jython registry makes no setting of `python.console`{.backtick} so if you do not set `python.console`{.backtick} on the command line you will get a PlainConsole. If you specify a class that cannot be found, or some other error occurs while loading and initialising the alleged console, you will get a non-fatal error and a PlainConsole.

When using the embedded interpreter, PlainConsole is the recommended choice as installing the line-editing consoles will have a permanent and perhaps confusing effect on the application\'s use of the standard streams. If you use a line-diting console, do so by setting `python.console`{.backtick} and getting the interpreter before taking any references to `System.in`{.backtick} or `System.out`{.backtick}. When using the JSR-223 script engine, the engine directs the interpreter to use its own streams, with which it wraps `System.in`{.backtick} and `System.out`{.backtick} before initialising Jython. The [ScriptEngine](./ScriptEngine.html) does not then benefit from the installed console.

## Properties of the Available Consoles 

### JLineConsole 

**JLineConsole** (`-Dpython.console=org.python.util.JLineConsole`) provides line-editing cross-platform. The behaviour of the system terminal is radically altered, and `System.in`{.backtick} and `System.out`{.backtick} are both replaced by specialised objects. `sys.stdin`{.backtick} and `sys.stdout`{.backtick} wrap these objects instead of the original JVM ones. In the event of an uncontrolled exit of the JVM you may need to type blindly `stty sane` (Unix) to get a console that echoes correctly.

In version 2.7 of Jython, the JLine console has been tested to work with:

- Windows codepages 1252 and 1253 (therefore probably works with other single-byte encodings). It does not work with the UTF-8 codepage 65001.
- Linux (Mint 14) Gnome terminal with locales en_GB.UTF-8, en_GB.iso88591, el_GR.iso88597 (therefore probably works with other single-byte encodings).

### ReadlineConsole 

**ReadlineConsole**: (`-Dpython.console=org.python.util.ReadlineConsole`) is an alternative (Unix) line-editing console that uses the library `libjavareadline`{.backtick}. The behaviour of the system terminal is altered, and `System.in`{.backtick} and `System.out`{.backtick} are both replaced by specialised objects. `sys.stdin`{.backtick} and `sys.stdout`{.backtick} wrap these objects instead of the original JVM ones. The readline console takes an extra setting `python.console.readlinelib`{.backtick} with values of `GnuReadline`{.backtick} or `Editline`{.backtick}.

In version 2.7 of Jython, the Readline console has been tested using `-Dpython.console.readlinelib=GnuReadline`{.backtick} to work with:

- Linux (Mint 14) Gnome terminal with locales en_GB.UTF-8, en_GB.iso88591, el_GR.iso88597 (therefore probably works with other single-byte encodings).

The Readline console has been tested using `-Dpython.console.readlinelib=Editline`{.backtick} to work with

- Linux (Mint 14) Gnome terminal with locales en_GB.iso88591, el_GR.iso88597 (therefore probably works with other single-byte encodings). It does not recognise characters beyond US-ASCII when the locale is UTF-8.

### PlainConsole 

**PlainConsole**: (`-Dpython.console=org.python.core.PlainConsole` or simply `-Dpython.console= `) provides no (additional) line-editing. `System.in`{.backtick}and `System.out`{.backtick} are unmolested.

`PlainConsole`{.backtick} is inconvenient on Linux because there is no line recall or and not facility to correct typing mistakes other than to delete backwards to the error. It is acceptable on Windows since the system itself provides some line recall and editing.

## Notes on using the Consoles 

Encoding is a tricky subject.

### Linux 

This is based on Linux Mint 14 (a Ubuntu derivative), the `bash`{.backtick} shell and Gnome Terminal. By default, the environment uses UTF-8 and you can expect the `JLineConsole`{.backtick} and `ReadlineConsole`{.backtick} (with `python.console.readlinelib=GnuReadline`{.backtick}) to work. The `ReadlineConsole`{.backtick} with `python.console.readlinelib=Editline`{.backtick} appears only to accept US-ASCII.

These notes do not cover how to type characters outside the US-ASCII set. You can install a range of keyboard mappings, and locales that support the encodings you need. This author uses the UK Extended WinKeys keyboard layout to access a range of accented characters and for these tests also installed a Greek keyboard layout and locale.

To obtain an environment with ISO-8859-1 encoding, launch as

    $ export LC_ALL=en_GB.iso88591
    $ jython

or `en_US.iso88591` if that\'s appropriate. You must set the encoding in the terminal window menu as well as through the shell environment.

The JVM should then pick up the encoding in use and configure the console object, and `sys.stdin`{.backtick} and `sys.stdout`{.backtick} to use it. To check this, use:

    >>> import sys
    >>> sys.stdin.encoding
    'ISO-8859-1'

### Windows 

This is based on Windows 7 command shell. When using the command window with non-ascii characters, in order to get characters represented correctly on screen, you must set a \"TrueType\" font (from the properties menu of the window). You can expect the `JLineConsole`{.backtick} to work with any single-byte encoding, but it does not work with codepage 65001, the close approximation to UTF-8. The root of this problem is that Windows uses a different \"wide character\" API for this, while JLine only calls the byte-oriented one.

These notes do not cover how to install support for alternate languages and keyboard mappings. This author uses the UK Extended keyboard layout to access a range of accented characters and for these tests also installed a Greek keyboard layout.

To obtain an environment with ISO-8859-1 encoding, launch as

    > chcp 1252
    > jython

(You may find cp1252 is your default.) The JVM should then pick up the encoding in use and configure the console object, and `sys.stdin`{.backtick} and `sys.stdout`{.backtick} to use it. To check this, use:

    >>> import sys
    >>> sys.stdin.encoding
    'Cp1252'
