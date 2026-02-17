# MacPython/AppleScript

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# What is AppleScript? 

AppleScript is a scripting language developed by Apple, included as standard in Mac OS (System 7 Pro and later) and Mac OS X. It has two important technical features:

- It can communicate with local and remote processes via [../AppleEvents](./MacPython(2f)AppleEvents.html); commonly known as \"application scripting\".

- It is an [../OSA](./MacPython(2f)OSA.html) language component, allowing client applications to load and run scripts via the language agnostic OSA API. Client applications can use the OSA API to implement features such as Folder Actions (System Events), Mail rules, iCal alarm scripts, OSA script editing (Script Editor, Script Debugger), etc.

# Equivalent Python Features 

Python provides extensive third-party application scripting support and limited OSA language component support. It also supports AppleEvent handling and can load and use other OSA language components.

## Application scripting 

Python has long supported sending AppleEvents via the high-level `aetools` and `gensuitemodule` modules in its standard library. However, these modules have always had a number of shortcomings and have grown increasingly troublesome in recent Mac OS X releases; in particular, they are completely broken on Intel-based Macs. As a result, these and other AE/OSA-related modules will be removed in a future Python release and their use should be avoided.

There is also a low-level extension, `Carbon.AE`, that can be used to construct and send AppleEvents. Using this API requires detailed knowledge of the Apple Event Manager, however, and is rarely used directly.

A modern replacement to `aetools` and `gensuitemodule`, the [../AppscriptModule](./MacPython(2f)AppscriptModule.html), has been available since late 2003. (A second project, aeve, has since been discontinued.)

## Python OSA language components 

There have been several attempts to develop a Python OSA language component, though to date none of them provide a complete replacement for AppleScript.

- OSAPython implements much of the OSA interface, but is unfinished and is no longer being developed.

- MacPythonOSA is another attempt to implement the full OSA interface, but is also unfinished and currently inactive.

- PythonOSA provides a working implementation of the core OSA interface, allowing OSA scripts written in Python to be loaded, stored, compiled and executed. More advanced OSA features, such as the ability to send and receive AppleEvents to and from the host process are not currently available.

## Apple event handling 

The Python standard library has long provided a basic AppleEvent handing framework, MiniAEFrame, but as with `aetools` and `gensuitemodule` this module is unsupported on Intel Macs and will be removed in future, and its use should be avoided.

The low-level `Carbon.AE` extension can be used to install Apple event handlers, though lacks the ability to install coercion handlers and requires detailed knowledge of the [../AppleEventManager](./MacPython(2f)AppleEventManager.html) to use, so is rarely used directly.

There are two modern, high-level options for implementing AppleEvent handling in Python-based applications:

- aemreceive (bundled with the AppscriptModule) can be used to install AppleEvent handlers although it provides no assistance for resolving object references so is best suited for use in applications that don\'t implement an [../AppleEventObjectModel](./MacPython(2f)AppleEventObjectModel.html).

- PyObjC-based applications can leverage the [/AppKit](./MacPython(2f)AppleScript(2f)AppKit.html) framework\'s built-in Cocoa Scripting support to implement a full AppleEventObjectModel.

## OSA API access 

There are currently two ways to access the OSA API in Python:

- The `CarbonX.OSA` extension (bundled with the AppscriptModule) provides a low-level wrapper around the OSA API. (There is also a `Carbon.OSA` extension included in Python 2.4 and later, but it provides only a partial implementation and contains several bugs so is best avoided.) A high-level wrapper for `CarbonX.OSA` is under development.

- PyObjC includes a wrapper for the (currently undocumented) `OSAKit` API on OS 10.4 and later.

# See also 

- [../aeve](./MacPython(2f)aeve.html)

- [../AppscriptModule](./MacPython(2f)AppscriptModule.html)

- [../AppleEvents](./MacPython(2f)AppleEvents.html)

- [../AppleScriptNotes](./MacPython(2f)AppleScriptNotes.html)

- [../FourCharacterCode](./MacPython(2f)FourCharacterCode.html)

- [../OSA](./MacPython(2f)OSA.html)

- [http://wilbur.acm.uiuc.edu/afs/sig/macwarriors/www/applescript/](http://wilbur.acm.uiuc.edu/afs/sig/macwarriors/www/applescript/)

- [http://www.cs.utexas.edu/users/wcook/papers/AppleScript/AppleScript95.pdf](http://www.cs.utexas.edu/users/wcook/papers/AppleScript/AppleScript95.pdf)

- [http://developer.apple.com/technotes/tn2002/tn2106.html](http://developer.apple.com/technotes/tn2002/tn2106.html)

- [http://www.oreilly.com/pub/a/mac/2007/05/08/using-python-and-applescript-to-get-the-most-out-of-your-mac.html](http://www.oreilly.com/pub/a/mac/2007/05/08/using-python-and-applescript-to-get-the-most-out-of-your-mac.html)
