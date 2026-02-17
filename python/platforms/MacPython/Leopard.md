# MacPython/Leopard

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Python releases have progressed far enough that it may be worth installing the current [MacPython](MacPython) distribution, however there may be conflicts between [MacPython](MacPython) installations and Mac OS X development tools, such as problems building PyObjC applications in Xcode. Mac OS X 10.5.x (Leopard) comes with the 2.5.1 Python distribution pre-installed, with an integrated Python Launcher.app. At the time of Leopard\'s launch, the official release version of Python was also 2.5.1. So some users may wish to avoid installing the pythonmac.org distribution and use the built-in python. However, the built-in python does not include IDLE.app and the standard pythonmac.org distribution will not allow its installation without the installation of at least a complete, redundant Python.framework.

Some people have legitimate reasons for wanting to install IDLE on Leopard. E.g., even though Leopard\'s Xcode 3.0 (and later) supports Python development, it does so in a heavyweight, support-all-of-Cocoa fashion. And educators teaching Python who wish to do so in a platform-agnostic way may also be best served by IDLE.

As mentioned at [http://www.givegoodweb.com/post/39/idle-on-leopard](http://www.givegoodweb.com/post/39/idle-on-leopard), IDLE, as a module rather than an application, is actually built into the default Python installed with Leopard. You can invoke IDLE from within the Python shell by typing the following:

- import idlelib.idle

Or from the unix command line in Terminal you can invoke IDLE by typing:

- python -m idlelib.idle

You can even create a shell script called, for example, IDLE, containing nothing but the previous line, make it executable (chmod +x IDLE), and it can be used to launch IDLE from the Finder or the Dock. All of these approaches require an open Terminal window (or will open one automatically, in the case of the shell script), the shell script can only be placed in the Dock as a document, rather than an application, and IDLE does not come to the foreground when it is launched by any of these methods, however the technique works fine. Still, if you want a standard Mac application version of IDLE, that can be placed in the Dock as an app, that comes to the foreground when it is launched, and that doesn\'t require Terminal, you can extract and use the [MacPython](MacPython) version of IDLE.app using the instructions below.

The following steps will allow the installation of IDLE.app (and other [MacPython](MacPython) 2.5 extras, such as Build Applet.app) on a Leopard machine without any redundant elements and without any conflicts with the pre-installed Python environment:

1\. Download and mount:

- [http://pythonmac.org/packages/py25-fat/dmg/python-2.5-macosx.dmg](http://pythonmac.org/packages/py25-fat/dmg/python-2.5-macosx.dmg)

2\. In Finder, do a Show Package Contents on \"[MacPython](MacPython).mpkg\" and navigate to Contents \> Packages \> [PythonApplications](PythonApplications)-2.5.pkg.

\[Note: The installer modifies \~/.bash_profile, so you may wish to make a backup copy before proceeding with the next step.\]

3\. Double click [PythonApplications](PythonApplications)-2.5.pkg and install it. This only installs items (including IDLE.app) in \"/Applications/MacPython 2.5\", so it won\'t interfere with your system install of Python. Also, the installer will let you chose a custom folder to install it into.

4\. In Terminal, create a symbolic link for the system\'s Python.framework in the location expected by the pythonmac.org tools, like so:

- cd /Library/Frameworks\
  sudo ln -s /System/Library/Frameworks/Python.framework/ Python.framework

You\'re done! IDLE.app works as intended. And since the pythonmac.org distro is the same 2.5.1 release as comes pre-installed with Leopard, there shouldn\'t be any module/interpreter compatibility issues.

**UPDATED WARNING:** This is a potentially dangerous change to your system! If you leave this symbolic link in place and then later attempt to install another version of Python, using a python.org installer or anything else that installs into \"/Library/Frameworks/Python.framework\", you risk overwriting the Apple-supplied Python files in \"/System/Library/Frameworks\". If you go ahead with the above suggestion, remember to remove the symbolic link before installing new versions of Python!

It is recommended that you delete the newly installed Python Launcher.app, because it is already present inside the system Python.framework. If you have installed Apple\'s developer tools (Xcode et al), it is recommended that you delete the newly installed Build Applet.app, because it is already present in /Developer/Applications/Utilities/MacPython 2.5.
