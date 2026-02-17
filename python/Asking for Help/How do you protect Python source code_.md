# Asking for Help/How do you protect Python source code?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Concealing (\"Protecting\") Source Code 

In response to the following question:

\"How can I truly \"protect\" the python source code we create for a commercial product?\"

First of all, it is important to distinguish between **commercial** and **proprietary**. The restriction is in the licence you use, not on whether the code is visible or not. There are numerous commercial products whose source code is Free (and open source) Software: various distributions of GNU/Linux fit this profile. In contrast, various free (as in cost, ie. \"gratis\") programs are made available only as binary executables where the source code is not available; they are therefore proprietary products which are not commercial: official Microsoft add-ons and upgrades such as Internet Explorer fit this profile, along with other binary-only \"freeware\".

(Note that \"freeware\" should **not** be confused with Free Software - see the [Free Software Foundation site](http://www.fsf.org/) for more information on what Free Software is.)

It is, however, assumed that the questioner would like to hide their code from the user. This article now discusses technical solutions to achieve this objective.

## Use Compiled Bytecode 

Python produces `.pyc`{.backtick} files when programs are run for imported modules. This bytecode is not trivially understandable by most developers, and supplying only the bytecode might be sufficient in deterring modification of the code, but there are ways to \"decompile\" the bytecode and recover a human-readable program. The [decompyle](http://sourceforge.net/projects/decompyle/) program is probably the best known tool for this task.

Note that `.pyc`{.backtick} files are not portable between different versions of Python.

## Executable Creators (or Installers) 

Tools exist which embed modules and a Python interpreter together into an executable, like [PyInstaller](PyInstaller) and py2exe (see [DistributionUtilities](DistributionUtilities)). These tools offer an additional layer of obfuscation over merely supplying bytecode files, since any decompilation of the bytecode may only take place once the bytecode has been located in the executable. However, unless additional processes are introduced to obscure the bytecode, it is likely that the task of locating the bytecode would be trivial for even the least determined inquisitive individual.

## Software as a Service 

Perhaps the most reliable way of concealing source code is not to distribute your programs at all. Companies such as Google apparently use Python and yet have no difficulty in concealing their source code from outsiders.

## Python Source Code Obfuscators 

Diligently using search engines reveals that at least three obfuscators exist which accept Python source code as input, and produce transformed code which is harder to understand. Transformations provided by most Python code obfuscators include:

- Rename your code\'s internally used identifiers (variable names, function names,
  - class names, etc.) to gibberish.
- Remove or alter comments and docstrings.

Even if you compile your code to .pyc files before distributing it, these transformations should increase the labor required to reverse-engineer your code.

There are some other ways to obfuscate code object in runtime, like [Pyarmor](Pyarmor):

- Encrypt code object by DES to protect constants and literal strings.
- Obfuscate byte code of each code object when code object completed execution.
- Clear f_locals of frame as soon as code object completed execution.

## Editorial Notes and Opinions 

This topic touches on several others frequently discussed. A common thread in comp.lang.python, for example, bounces between someone who sincerely claims to need some sort of [obfuscation](./obfuscation.html) to prevent others from taking or modifying his ideas, and a gang of the old guard who ask precisely what the ideas are, who might take them, what would be the harm in that, and so on. One proposition often repeated is that the only safe code is that hosted on a remote machine.

Commercial developers should perhaps consider the necessity of concealing their source code. In certain kinds of businesses, a good relationship between the customer and the vendor is able to provide plenty of additional value to both parties: extensible, freely modifiable code is arguably more likely to be improved and adapted over time, quite probably as a service provided by the vendor; in contrast, merely shipping proprietary products and attempting to persuade customers to upgrade, perhaps with the customer running the continuous risk of versions they already use becoming obsolete (and with no means at their disposal to, for example, recompile the code for new platforms or systems) may aggravate the relationship between the parties over time.

. . .

\[Futility of protection schemes\--but equally for Java, C, \...\]

Also see \"[deployment](deployment)\".

------------------------------------------------------------------------

[CategoryPythonInBusiness](CategoryPythonInBusiness) [CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
