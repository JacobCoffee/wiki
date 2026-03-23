# lwickjr/Modules

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

My more-interesting modules include \"[Alias](./lwickjr(2f)Modules(2f)Modules(2f)Alias.html)\", \"[Edit](./lwickjr(2f)Modules(2f)Modules(2f)Edit.html)\", and \"[UT](./lwickjr(2f)Modules(2f)Modules(2f)UT.html)\". I\'ll add others to this page as I have opportunity.

## General Outlines 

- [Alias.py](attachments/lwickjr(2f)Modules/Alias.py) is a convenience module for I.D.L.E. [PyShell](./PyShell.html) usage, intended to save typing.

  - Provides a mechanism whereby arbitrary callables are \*effectively\* converted to commands in interactive Python, but not in modules. To do this, Alias splits off the first word of the command line, attempts to evaluate it, and iff it is callable, the tail of the command is also evaluated and passed to the callable as an argument tuple. This allows the manual use of \"dir\", \"reload\", et al, as statements without requiring that parentheses be typed. Parentheses are still required in module source, however, and in any function calls in the tail of the command line.
  - Provides a mechanism whereby arbitrary one-word names may be assigned to callable objects for use with the preceding mechanism. This allows one to dispense with the requirement to type fully-qualified long.nested.module.names for selected callables, and is where the module gets its name.
  - Provides a mechanism for allowing modules to be imported through a bare reference to the module name.
  - Provides a mechanism whereby modules imported by the preceding mechanism may auto-register aliases of their own choosing. Entering the name of a module that has already been imported does not re-import the module; rather it re-updates whatever auto-alias associations might exist in that module at the time the name is re-entered.
  - Provides its own list of aliases, available via the preceding mechanism, for managing the alias dictionary.
  - Does not function under IDLE without disabling the default sub-process. Probably does not function correctly, or even at all, without IDLE.

------------------------------------------------------------------------

- [Edit.py](attachments/lwickjr(2f)Modules/Edit.py)

  - Provides an Alias that attempts to open for editing the source for the module where the argument was defined, positioned, if possible, on the line where the definition starts.
  - Provides a mechanism for recording the current size and position of the active IDLE window such that subsequent attempts to open the window open it with the remembered geometry.
  - Provides an IDLE menu item to trigger the preceding mechanism.
  - Functions only under IDLE. Does not function correctly without disabling the default sub-process.

It seems to me that Edit is something that makes it so that you can jump straight to where a variable is defined, in IDLE. (Not really sure.) If so, that\'s awesome! I\'ve often times wished IDLE were more powerful; This is the kind of thing I\'d like to see more of. ![:)](/wiki/europython/img/smile.png%20":)")

\-- [LionKimbro](../../people/LionKimbro) 2005-04-01 21:16:29

[lwickjr](): You have the right idea, but variables are too simple for Edit to deal with. When you type \"edit thing\", \"thing\" \*MUST\* evaluate to an object for which one of the standard modules, \"inspect\", I believe, is capable of locating the information required to open the source module. For the module to open for editing at the line where the object is defined, it is required for perfect positioning that inspect be capable of determining the line number. In the absence of reliable information, Edit makes an educated guess, and positions the editor there. When the educated guess fails, the editor is positioned wherever I.D.L.E. would have positioned it had you opened the file for editing via another method. Basically, Edit is given a class, instance, module, etc., and attempts to display the Python source for the definition. Edit will work, however, for anything that Inspect can retrieve the required information from. Edit also provides a hook for invoking custom editors in place of I.D.L.E.\`s built-in editor. This would be useful, for example, for having edit invoke a G.U.I. editor instead when invoked on objects created by the G.U.I. editor.

------------------------------------------------------------------------

- [UT.py]( "Upload new attachment "UT.py"") - last uploaded 2005-11-26 - is a convenience module for miscellaneous support functions that I\`ve found useful.

  - Provides several \"utility\" functions that I\'ve found useful:

  - A \"smart\" reload substitute that can automatically re-load other modules in dependancy-order, if the module being reloaded registers its dependancies, with convenience functions for declaring those dependancies.

  - A convenience wrapper for cPickle that allows \[un-\]pickling single objects from/to a specified file with a single function call.

  - [ThisLine](./ThisLine.html), a function that returns the name and source line-number of the caller an arbitrary number of callers up the call-stack.

  - Some old stuff, commented out.

------------------------------------------------------------------------

- [GWiz.py](attachments/lwickjr(2f)Modules/GWiz.py), a \"\"functional\"\" but incomplete GUI editor. More details later.

------------------------------------------------------------------------

- [WinReg.py]( "Upload new attachment "WinReg.py""), a higher-level abstraction around \_winreg. Fully functional and complete.

------------------------------------------------------------------------

I hereby offer any modules that \"\"I\"\" attach to this page for inclusion in the official Python module library.

## Comments 

I have a hard time understanding what the modules are for; There\'s a lot of focus on *how* these things work, but I have difficulty figuring out what they are for.

\-- [LionKimbro](../../people/LionKimbro) 2005-04-01 21:16:29
