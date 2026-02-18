# EmbeddedPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Embedded Python 

Python can be used in embedded, small or minimal hardware devices, depending on how limiting the devices actually are.

### Devices capable of running CPython 

Some modern embedded devices have enough memory and a fast enough CPU to run a typical Linux-based environment, for example, and running CPython on such devices is mostly a matter of compilation (or cross-compilation) and tuning.

Devices which could be considered as \"embedded\" by modern standards and which can run tuned versions of CPython include the following:

- [Gumstix](http://www.gumstix.org/)

- [Raspberry Pi](http://www.raspberrypi.org/)

- [BeagleBone Black](http://beagleboard.org/Products/BeagleBone%20Black)

- FIC [Neo1973](http://wiki.openmoko.org/wiki/Neo1973) and [Neo FreeRunner](http://wiki.openmoko.org/wiki/Neo_FreeRunner) ([Python on Openmoko](http://wiki.openmoko.org/wiki/Python))

- [Telit GSM/GPRS modules](http://www.telit.com/en/products/python/why-python.php) (also available as [AarLogic family](http://www.roundsolutions.com/aarlogic/index.htm) GPRS/GPS QUAD Band Modules)

See also [PythonForArmLinux](../archive/PythonForArmLinux) and [OpenEmbedded](OpenEmbedded).

### Work to improve CPython for embedded applications 

Various efforts have been made to make CPython more usable for embedded applications:

- [Patches in the OpenEmbedded repository](http://cgit.openembedded.org/cgit.cgi/openembedded/tree/recipes/python)

- Cross-compilation issues: [1006238](http://bugs.python.org/issue1006238 "Issue"), [5404](http://bugs.python.org/issue5404 "Issue"), [3871](http://bugs.python.org/issue3871 "Issue")

- General interpreter startup costs: [SpeedUpInterpreterStartup](../performance/SpeedUpInterpreterStartup)

- File access overhead on startup: [Improving interpreter startup speed](http://mail.python.org/pipermail/python-list/2008-October/467718.html), [Tons of stats/opens to non-existing files increases Python\'s startup on loaded NFS servers](http://mail.python.org/pipermail/python-list/2005-May/339691.html), [Startup time](http://mail.python.org/pipermail/python-dev/2003-May/035359.html)

- Import-related costs: [\_\_file\_\_](http://mail.python.org/pipermail/python-dev/2010-March/098042.html)

- Using a launcher process where \"expensive\" modules are required: [Introducing python-launcher](http://blogs.gnome.org/johan/2007/01/18/introducing-python-launcher/)

### Reduced or reworked Python implementations 

Some devices may be more restrictive in that the typical memory footprint of CPython may exceed the amount of memory available on the device. In such cases, a re-engineered or adapted version of CPython, perhaps even to the point where it can be considered a new implementation of Python, might be appropriate.

Examples of such implementations include the following:

- [PyMite](PyMite)

- [Tiny Python](Tiny%20Python)

- [Zerynth](../archive/Zerynth) formerly Viper

On the other hand, one can start with a full build, and simply remove unneeded modules, *e.g.*, Tkinter, etc., to realize a reduced-size Python with little effort.

### Python-based tools for developing embedded applications 

Sometimes the embedded environment is just too restrictive to support a Python virtual machine. In such cases, various Python tools can be employed for prototyping, with the eventual application or system code being generated and deployed on the device.

Tools that support this kind of development include the following:

- [MyHDL](https://myhdl.org/)

- [WhatOS](https://sourceforge.net/projects/whatos/)
