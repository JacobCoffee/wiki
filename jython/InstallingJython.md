# InstallingJython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Installing Jython 

Jython 2.5.0 is distributed as an executable jar file installer. After downloading it, either double click the jython_installer-2.5.0.jar or run java with the -jar option

`java -jar jython_installer-2.5.0.jar`

This will start the regular GUI installer on most systems, or a consoler installer on headless systems. To force the installer to work in headless mode invoke the installer with a console switch

`java -jar jython_installer-2.5.0.jar --console`

The installer will then walk through a similar set of steps in graphical or console mode: showing the license, selecting an install directory and JVM and actually copying Jython to the filesystem. After this completes, Jython is installed in the directory you selected. There\'s a script in the install directory, jython on Unix like systems or jython.bat on Windows, that will start up the Jython console which can be used to dynamically explore Jython and the Java runtime.

## Installation options 

You can get a list of the installer options by running:

`$ java -jar jython_installer-2.5.0.jar --help`

### Standalone mode 

The standalone option does no caching and so avoids the startup overhead (most likely at the cost of some speed in calling Java classes, but I have not profiled it)

And when you come to the \"Installation type\" page, select \"Standalone\".

When the installation is done, you will have a jython.jar with the /Lib files included that can be run like this:

`$ java -jar jython.jar`

You will get a jython prompt with no caching. Of course you can run scripts just by calling them as you might expect:

`$ java -jar jython.jar script.py`

And you can add this jar to the classpath of your app, which will allow standard imports.
