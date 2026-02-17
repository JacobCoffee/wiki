# MacPython/XcodeIntegration

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Running scripts from Xcode 

It\'s not terribly difficult to tell Xcode to launch a Python process and start your script. Create a custom executable, point it at Python, and set the arguments and environment variables appropriately. Detailed instructions are here:

[http://ulaluma.com/pyx/archives/2004/02/running_python.html](http://ulaluma.com/pyx/archives/2004/02/running_python.html)

# User Scripts 

- [StartupScript](attachments/MacPython(2f)XcodeIntegration/StartupScript) - A Python replacement for the Apple-provided example written in Perl. Install at `~/Library/Application Support/Apple/Developer Tools/`

- [un_commentLines.py](attachments/MacPython(2f)XcodeIntegration/un_commentLines.py) - A Python version of the Apple-provided \"Un-Comment\" script to be Python-aware. (You\'ll need to remove the shortcut in the first comment script.) Install at `~/Library/Application Support/Apple/Developer Tools/Scripts/10-User Scripts/30-Comments`. \[1/1/5\] Fixed error with perl scripts, and added support for commenting applescripts.

# Xcode Plug-Ins 

- [XOgre-0.0.tgz](http://undefined.org/python/XOgre-0.0.tgz) - A quick hack to replace Xcode\'s Find menu with [OgreKit](http://www-gauge.scphys.kyoto-u.ac.jp/~sonobe/OgreKit/)\'s (regular expression engine). Put the pbplugin at `~/Library/Application Support/Apple/Developer Tools/Plug-Ins`.

- [XPython-0.0.tgz](http://undefined.org/python/XPython-0.0.tgz) ([XPython-bin-0.0.tgz](http://undefined.org/python/XPython-bin-0.0.tgz) for built Plug-In and two examples) - I put Python in Xcode! Unpack the built version at `~/Library/Application Support/Apple/Developer Tools/`. Check this out:\

![](http://undefined.org/python/XPython_0.png "http://undefined.org/python/XPython_0.png")\
\
And even scarier.. here\'s the [MacPython/PyObjC](PyObjC) class browser demo INSIDE Xcode. Just look at all those proprietary Apple classes:\
![](http://undefined.org/python/XPython_1.png "http://undefined.org/python/XPython_1.png")

# Notes 

- The User Scripts feature is totally \"borrowed\" from [TextExtras](http://www.lorax.com/FreeStuff/TextExtras.html)! Look at `/System/Library/PrivateFrameworks/DevToolsInterface.framework/Versions/A/Resources/UtilityScripts` \-- it\'s \*the same\*.
