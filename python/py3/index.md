# Python 3 Migration

This section is largely a historical archive. Python 2 reached end-of-life on January 1, 2020, and the migration is long over for most projects. But these pages document the community's multi-year effort to move from Python 2 to Python 3 -- the tools that were built, the problems that came up, the porting guides that were written, and the debates that shaped the transition. If you are still maintaining a Python 2 codebase (it happens), the porting guides here are still technically accurate.

## Overview and FAQ

- [Python 2 or Python 3?](Python2orPython3) -- the classic "which version should I use?" page
- [Python 3 FAQ](Python3FAQ) -- frequently asked questions about Python 3
- [5 Years of Python 3](5YearsOfPython3) -- community feedback collected five years into the Python 3 era

## Porting Guides

- [Porting to Py3k](PortingToPy3k/index) -- the main porting guide with strategies and common issues
- [Porting to Py3k](PortingToPy3k) -- single-page porting overview (Python 2 EOL notice included)
- [Porting Python Code to Py3k](PortingPythonToPy3k) -- step-by-step instructions for converting pure Python code
- [Porting Extension Modules to Py3k](PortingExtensionModulesToPy3k) -- porting C extension modules to Python 3
- [Porting Django to 3k](PortingDjangoTo3k) -- notes from an early attempt to port Django at PyCon 2008
- [One Codebase for Python 2 and 3](2and3%20One%20codebase%20for%20dual%20version%20support) -- tips for maintaining a single codebase that runs on both versions

## Conversion Tools

- [2to3](2to3) -- the automatic translation tool for converting Python 2 code to Python 3
- [3to2](3to2) -- the reverse tool for backporting Python 3 code to Python 2
- [Py3k Conversion Tools](Py3kConversionTools) -- roundup of available tools for the 2-to-3 transition

## Python 3 Design and Planning

- [Python 3.0](Python3.0) -- Guido's original goals for Python 3.0, later consolidated into PEP 3000
- [Python 3.0 Suggestions](Python3.0Suggestions) -- community suggestions for what Python 3.0 should include
- [Python 3000](Python3000) -- the early planning page (largely of historical interest since 2008)
- [Martin von Loewis](MartinvonLoewis/index) -- pages from Martin von Loewis related to the Python 3 transition

## Python 3 Technical Details

- [Py3k Deprecated](Py3kDeprecated) -- features deprecated or removed in the Python 3 transition
- [Py3k Extension Modules](Py3kExtensionModules) -- status of extension module compatibility with Python 3
- [Py3k Regressions](Py3kRegressions) -- known regressions in early Python 3 releases
- [Py3k String Formatting](Py3kStringFormatting) -- the new string formatting methods based on PEP 3101
- [Py3k Str/Unicode Tests](Py3kStrUniTests) -- test cases for the string/unicode changes in Python 3
- [Py3k Todo](Py3kToDo) -- the old to-do list for the Python 3 transition
- [Python 3k String Repr](Python3kStringRepr) -- changes to string representation in Python 3
- [Python 3 UnicodeDecodeError](Python3UnicodeDecodeError) -- dealing with UnicodeDecodeError in Python 3

## Ecosystem Status

- [Python 3 Linux Distro Porting Status](Python3LinuxDistroPortingStatus) -- tracking Linux distribution support for Python 3
- [Python 3 Porting Status](Python3PortingStatus) -- tracking which third-party packages support Python 3

```{toctree}
:hidden:
:maxdepth: 1

MartinvonLoewis/index
PortingToPy3k/index
2and3 One codebase for dual version support
2to3
3to2
5YearsOfPython3
PortingDjangoTo3k
PortingExtensionModulesToPy3k
PortingPythonToPy3k
PortingToPy3k
Py3kConversionTools
Py3kDeprecated
Py3kExtensionModules
Py3kRegressions
Py3kStrUniTests
Py3kStringFormatting
Py3kToDo
Python2orPython3
Python3.0
Python3.0Suggestions
Python3000
Python3FAQ
Python3LinuxDistroPortingStatus
Python3PortingStatus
Python3UnicodeDecodeError
Python3kStringRepr
```
