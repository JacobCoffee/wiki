# PythonImportEngine

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python Import Engine - Possible GSoC Project 

This concept has been put forward as a project for students to consider undertaking as part of [SummerOfCode/2011](../soc/SummerOfCode/2011)

The Python import process involves a great deal of process global state. At the very least, this includes:

- sys.modules
- sys.path
- sys.path_hooks
- sys.meta_path
- sys.path_importer_cache
- the import lock (imp.lock_held()/acquire_lock()/release_lock())

This project involves taking the in-development version of Python 3.3, including the \"importlib\" package, and attempting to implement an [ImportEngine](./ImportEngine.html) class, which encapsulates all of the mechanisms of Python\'s import system into a single object.

An ideal outcome is to successfully implement this within the limitations of the existing PEP 302 interface. A more likely outcome is to identify the minimal set of changes or additions to the PEP 302 interfaces needed in order to support this mode of operation (e.g. passing the import engine instance as an optional argument to loader and importer methods), and to fork importlib to support those interface changes.

If the task proves easier than expected, then there are multiple follow-on tasks that can be pursued:

- module blacklisting, preventing imports of certain modules via the engine
- engine subclassing to add additional features (e.g. module import notifications)
- engine subclassing to use the import engine API to interact with the existing process global state

If successful, this project may result in the [ImportEngine](./ImportEngine.html) API being made available in a future version of importlib, or else being used as a basis to propose a new revision of the PEP 302 interfaces. However, neither outcome can be guaranteed.

The full details of Python\'s import system are not cleanly documented. A good starting point is the [Python 3.3 \"importlib\" documentation](http://docs.python.org/dev/library/importlib) (especially the \"See also\" list), as well as the importlib source code. A more readable introduction may be found in [this draft ODT manuscript](http://svn.python.org/view/sandbox/trunk/userref/ODF/Chapter07_ModulesAndApplications.odt?view=log) in the svn.python.org sandbox. While the latter is slightly dated in some areas (it was written for Python 2.5), it still provides a solid overview of the essential operation of Python\'s import machinery.

If you are interested in this activity as a possible GSoC project (under the auspices of the PSF), contact [Alyssa Coghlan](mailto:ncoghlan@gmail.com) with any technical questions. Refer to [SummerOfCode/2011](../soc/SummerOfCode/2011) for details on the GSoC process itself.
