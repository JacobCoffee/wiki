# EclipsePythonIntegration

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Using Eclipse as a Python editor 

It is not known which version of Eclipse these comments refer to, please be careful and read the release notes for the plugin you choose.

A few plugins for [Eclipse](Eclipse) are in progress that will enable Eclipse to be used as a Python IDE.

::: {}
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------+------------------+-------------------------+---------------------------------------+--------------------------------------------------+
| Name                                                  | URL                                                                                                                 | Version      | Last Update      | Licensing               | Supports Jython                       | Remarks                                          |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------+------------------+-------------------------+---------------------------------------+--------------------------------------------------+
| Dynamic Languages Toolkit                             | [http://www.eclipse.org/dltk/](http://www.eclipse.org/dltk/)                                                 | 4.0.0        | June 25, 2012    | EPL\*                   | ?                                     |                                                  |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------+------------------+-------------------------+---------------------------------------+--------------------------------------------------+
| Pydev                                                 | [http://pydev.org](http://pydev.org/)/                                                                       | 3.3.3        | January 27, 2014 | EPL\*                   | Yes                                   | It also supports [IronPython](IronPython) |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------+------------------+-------------------------+---------------------------------------+--------------------------------------------------+
| [PythonMonkey](./PythonMonkey.html)     | [http://code.google.com/p/jrfonseca/wiki/PythonMonkey](http://code.google.com/p/jrfonseca/wiki/PythonMonkey) | 0.1.0        | October 21, 2007 |                         | Yes                                   |                                                  |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------+------------------+-------------------------+---------------------------------------+--------------------------------------------------+
| [TruStudio](./TruStudio.html)           | [http://www.xored.com/trustudio](http://www.xored.com/trustudio) (defunct)                                   | 1.0.1a / 1.1 | May 18, 2005     | no more available       | [Merged](http://www.eclipse.org/proposals/dltk/) into DLTK project                |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------+------------------+-------------------------+---------------------------------------+--------------------------------------------------+
| JyDT                                                  | [http://www.redrobinsoftware.net/jydt/](http://www.redrobinsoftware.net/jydt/)                               | 1.4.15       | June 23, 2006    | CPL                     | Jython only                           |                                                  |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------+------------------+-------------------------+---------------------------------------+--------------------------------------------------+
| [EclipseColorer](./EclipseColorer.html) | [http://colorer.sf.net/](http://colorer.sf.net/)                                                             | 0.9.9        | July 22, 2011    | Mozilla PL / GPL / LGPL | Yes?                                  | Syntax highlighting only                         |
+-------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------+------------------+-------------------------+---------------------------------------+--------------------------------------------------+
:::

\* Eclipse Public License

To point out the obvious, it would be nice if some of these teams would combine their efforts.

## Some Features 

*The next seven sections of documentation, up to and including \"Supplying parameters to your jython or python program\" are contributed by Andy Bulka [abulka@netspace.net.au](mailto:abulka@netspace.net.au) .*

------------------------------------------------------------------------

- These plugins provide *syntax highlighting* to allow for easy location of code segments with just a glance.

- Significantly, you can use Eclipse *bookmarking* and create *task* bookmarks inside the eclipse python editor. This is way cool.

- Lines with **def** are given little notches in the scroll bar, which you can click on and jump to that python function/method.

- You can run **jython** or python on the current file and get the output appear in the eclipse console window.

- You can use the Search/Grep feature of Eclipse to search through your python source code modules.

- You can define a \"working set\" which is a custom list of python files that you want to have listed in the left hand Navigator window.

- Instead of importing a folder into eclipse (which copies the files into c:\\eclipse\\workspace\\\...) you can instead create a linked folder which means that you can edit files on your regular file system. To do this, create a new folder, then when prompted, click \"Advanced\" and select the folder on your file system to link to. Sometimes you have to \'refresh\' the list by r.clicking on the folder and selecting \'refresh\'.

## Which plug-in is the best? 

Both [PyDev](PyDev) and [TruStudio](./TruStudio.html) are undergoing active development and both feature and extensive set of useful tools for developing in Eclipse. It\'s not hard to try either of them out, so you might as well just try them both out and see which you enjoy more.

Going by the popularity on Google, (using a very unscientific method of just searching for the two words *python eclipse*) it seems as though [PyDev](PyDev) is more popular.

### PyDev 

*added by [KirbyUrner](KirbyUrner) [urnerk@python.org](mailto:urnerk@python.org)*

I saw a demo of this at OSCON 2004, presented by Dana Moore. Alex Totek has done the majority of the work so far, with help from Fabio Zadrozny. pydev includes a debugger. Dana previewed auto-completion but as of this writing it\'s not in the most recent release (0.5.3). I also saw the Python shell integrated into Eclipse. The development language for the plugin itself is Java, not Jython.

# Configuring Eclipse for running Python and Jython 

## Jython 

To configure Eclipse to run jython on the current file you are editing:

Select from the menu: Run -\> External Tools -\> Configure -\> New

then fill in the following values:

- **Name**: jython

- **Tool Location**: E.g. C:\\jython-2.1\\jython.bat

- **Working Directory**: -\> Browse Variables -\> \${container_loc}

- **Tool Arguments**: -\> Browse Variables -\> \${resource_name}

#### Supplying parameters to your jython or python program 

If you need to run an app which requires arguments, you will need to make another tool configuration (just copy the jython one) and simply add the necessary arguments to the **Tool Arguments** field.

For example instead of just

- \${resource_name}

*you would instead put*

- \${resource_name} **c:\\\\**

Notice I have supplied the argument **c:\\\\**

# Embedding Jython into Eclipse 

Don Coleman has written a jython code completion shell which he says he would be happy to rewrite for Eclipse.

- [http://don.freeshell.org/jython/](http://don.freeshell.org/jython/)

This URL was given by Don Coleman in an ASPN jython users newsgroup,

- [http://aspn.activestate.com/ASPN/Mail/Message/Jython-users/1620125](http://aspn.activestate.com/ASPN/Mail/Message/Jython-users/1620125)

How to make Jython unit tests\... and see them inside Junit plugin : [here](http://www.devx.com/Java/Article/26602/1954?pf=true) and modification and completion [here](http://lauploix.blogspot.com/2005/03/test-driven-development-why-using.html)

# Running SCons from CDT Eclipse 

SCons is a powerful software construction tool in python, more flexible than ant and simpler than make. It is primarily intended to manage builts for C/C++ programs. To set up SCons as the builder from CDT, add it as a custom builder:

- Select the project and edit its properties.
- From the Builder menu on the left, select new.
- Enter the full path to \"scons.bat\" file that comes with your installation.
- Add command line targets as necessary in the box below.
- Make sure python is setup in the default environment.

Note: Eclipse cannot currently spawn arbitrary shell programs, so even if the .py extension is registered, calling scons.py will fail from Eclipse.

There is now an [Scons Builder Plugin](http://nic-nac-project.de/~lothar/eclipse/update/SConsBuilderPlugin.html) for the Eclipse CDT.

For more information about SCons, see [http://www.scons.org/](http://www.scons.org/)

# Some Eclipse features people want with Jython/Python 

- project/file management (module organization)
- package explorer
- file manipulation (history, compare, replace, etc)
- collapsible code outlining
- integrated step-through debugging
- UML
- refactoring tools (rename of classes and methods)
- indentation support (tab / backtab)
- outline with classes and methods
- search for references (who calls method X)
- execution of code snippets from a file being edited
- use the Eclipse update manager for plug-in and core jython updates
- incremental compilation of Jython
- syntax highlighting and auto-completion
- support for pyunit (unittest)
- a Jython console, where one could try short snippets of code, with access to the current project classpath

# Eclipse would gain 

- Python/Jython support in the editor
  - this is what the existing plug-ins address, but they are incomplete
- better scriptable customization
  - use Jython as the \"glue\" language for extending Eclipse
- runtime interactive shell for trying and testing Java classes
- simplifies mixing Jython/Java to broaden range of problems that can be solved
- large user base of Jython/Python programmers

# Other Links 

- [Jython](Jython)

- [Python](Python)

- [IntegratedDevelopmentEnvironments](IntegratedDevelopmentEnvironments) - Python IDEs not based on Eclipse

------------------------------------------------------------------------

[CategoryJython](CategoryJython)
