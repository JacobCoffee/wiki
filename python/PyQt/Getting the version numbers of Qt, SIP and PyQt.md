# PyQt/Getting the version numbers of Qt, SIP and PyQt

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Getting the version numbers of Qt, SIP and PyQt 

When you report a bug in PyQt you need to supply information about the configuration you are using, including the versions of the Qt library, SIP and [PyQt](PyQt) modules. The following code should help.

:::: 
::: 
``` 
   1 from PyQt4.QtCore import QT_VERSION_STR
   2 from PyQt4.pyqtconfig import Configuration
   3 
   4 print("Qt version:", QT_VERSION_STR)
   5 cfg = Configuration()
   6 print("SIP version:", cfg.sip_version_str)
   7 print("PyQt version:", cfg.pyqt_version_str)
```
:::
::::

Note that the pyqtconfig module is deprecated in [PyQt](PyQt) 4.10. See [http://pyqt.sourceforge.net/Docs/PyQt4/build_system.html](http://pyqt.sourceforge.net/Docs/PyQt4/build_system.html) for more details. If you are unable to import pyqtconfig (for example when using Riverbank\'s packaged binaries) you can use the following:

:::: 
::: 
``` 
   1 from PyQt4.QtCore import QT_VERSION_STR
   2 from PyQt4.Qt import PYQT_VERSION_STR
   3 from sip import SIP_VERSION_STR
   4 
   5 print("Qt version:", QT_VERSION_STR)
   6 print("SIP version:", SIP_VERSION_STR)
   7 print("PyQt version:", PYQT_VERSION_STR)
```
:::
::::

For [PyQt5](./PyQt5.html) getting the version is the same as in the last example above, just exchange [PyQt4](PyQt4) for [PyQt5](./PyQt5.html)
