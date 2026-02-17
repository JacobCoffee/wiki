# SummerOfCode/PythonImportEnginePlanning

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Page for design and implementation details for the Import Engine GSoC 2011 project.

[http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/gslodkowicz/1](http://www.google-melange.com/gsoc/proposal/review/google/gsoc2011/gslodkowicz/1)

PEP: XXX

Title: Python Import Engine

Version: \$Revision\$

Last-Modified: \$Date\$

Author: Alyssa Coghlan \<[ncoghlan@gmail.com](mailto:ncoghlan@gmail.com)\>, Greg Slodkowicz \<[jergosh@gmail.com](mailto:jergosh@gmail.com)\>

Status: Draft

Type: Standards Track

Content-Type: text/x-rst

Created: 4-Jul-2011

Post-History: XXX

::: 
### Abstract

This PEP proposes incorporating an \'import engine\' class which would encapsulate all state related to importing modules into a single object and provide an alternative to the built-in implementation of the import statement, which is syntactic sugar for the `__import__()` method. Currently the bulk of importing work is done by means of module finders and loaders, and their interfaces would require a simple change in order to work both the builtin import functionality and importing via import engine objects. In that sense, this PEP constitutes a revision of finder and loader interfaces described in PEP 302 [\[1\]](#id5).
:::

::: 
### Rationale

Historically, any modification to the import functionality required re-implementing `__import__()` entirely. PEP 302 provides a major improvement by introducing separation between imports of different types of modules. As a result, additional process-global state is stored in the sys module. This, along with earlier import-related global state, comprises:

- sys.modules
- sys.path
- sys.path_hooks
- sys.meta_path
- sys.path_importer_cache
- the import lock (imp.lock_held()/acquire_lock()/release_lock())

Isolating this state would allow multiple import states to be conveniently stored within a process. Placing the import functionality in a self-contained object would allow subclassing to add additional features (e.g. module import notifications or fine-grained control over which modules can be imported). The engine would also be subclassed to make it possible to use the import engine API to interact with the existing process-global state.
:::

::: 
### Proposal

We propose introducing an ImportEngine class to encapsulate import functionality. This includes the `__import__()` function which can be used to as an alternative to the built-in `__import__()` when desired and also `import_module()`, equivalent to `importlib.import_module()` [\[3\]](#id7).

Since the new style finders and loaders should also have the option to modify the global import state, we introduce a `GlobalImportState` class with an interface identical to `ImportEngine` but taking advantage of the global state. This can be easily implemented using class properties.
:::

::::::: 
### Design and Implementation

::: 
#### API

The proposed extension would consist of the following objects:

`engine.ImportEngine`

> `__import__(self, name, globals={}, locals={}, fromlist=[], level=0)` Reimplementation of the builtin `__import__()` function. The import of a module will proceed using the state stored in the ImportEngine instance rather than the global import state. For full documentation of `__import__` funtionality, see [\[2\]](#id6) . `__import__()` from `ImportEngine` and its subclasses can be used to customise the behaviour of the `import` statement by replacing `__builtin__.__import__` with `ImportEngine.__import__`.

`import_module(name, package=None)`
:   A reimplementation of `importlib.import_module()` which uses the import state stored in the ImportEngine instance. See [\[3\]](#id7) for a full reference.

`from_engine(self, other)`
:   Create a new import object from another ImportEngine instance. The new object is initialised with a copy of the state in `other`. When called on `engine.sysengine` as `other`, `from_engine()` can be used to create an ImportEngine object with a **copy** of the global import state.

`GlobalImportEngine(ImportEngine)`
:   Convenience class to provide engine-like access to the global state. Provides `__import__()`, `import_module()` and `from_engine()` methods like `ImportEngine` but writes through to the global state in `sys`.
:::

::: 
#### Global variables

`engine.sysengine`
:   Instance of GlobalImportEngine provided for convenience (e. g. for use by module finders and loaders).
:::

::: 
#### Necessary changes to finder/loader interfaces:

`find_module` (cls, fullname, path=None, **engine=None**)

`load module` (cls, fullname, path=None, **engine=None**)

The only difference between \'new style\' and PEP 302 compatible finders/loaders is the presence of an additional `engine` parameter. This is intended to specify an ImportEngine instance or subclass there of. This parameter is optional so that the \'new style\' finders and loaders can be made backwards compatible by falling back on engine.sysengine with the following simple pattern:

    find_module(cls, fullname, path=None, engine=None)
      if not engine:
        engine = engine.sysengine

      ...

An implementation based on Brett Cannon\'s importlib has been developed by Greg Slodkowicz as part of the 2011 Google Summer of Code. The code repository is located at [https://bitbucket.org/jergosh/gsoc_import_engine/](https://bitbucket.org/jergosh/gsoc_import_engine/).
:::

::: 
#### Open Issues

The existing importlib implementation depends on several functions from `imp`, Python\'s builtin implementation of `__import__` located in *Python/import.c*. These functions are unaware of ImportEngine and place the newly imported module in `sys.modules`. Naturally, this is a problem from the ImportEngine point of view. The offending methods are:

- imp.init_builtin()
- imp.load_dynamic()

However, since there can be only a single instance of each builtin/dynamic module per process, they are essentially process-global regardless of the way they are imported. Currently, the simplest solution for supporting them in ImportEngine seems to have new style loaders call the existing imp methods and then copy appropriate references from `sys.modules` into the state inside the import engine.

Similarly, `imp.NullImporter` implements a `load_module` method which is incompatible with \'new style\' loaders. Since the `NullImporter` class does next to nothing (i. e. always returns None), it has been reimplemented in Python. The only way this could cause problems would be explicitly checking if a module\'s importer is an imp.NullImporter (which occurs only in some unittests).
:::
:::::::

::: 
### References

  ---------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\[1\]](#id1)   PEP 302, New Import Hooks, J van Rossum, Moore ([http://www.python.org/dev/peps/pep-0302](http://www.python.org/dev/peps/pep-0302))
  ---------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------

  ---------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\[2\]](#id3)   \_\_import\_\_() builtin function, The Python Standard Library documentation ([http://docs.python.org/library/functions.html#\_\_import\_\_](http://docs.python.org/library/functions.html#__import__))
  ---------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  \[3\]   *([1](#id2), [2](#id4))* Importlib documentation, Cannon ([http://docs.python.org/dev/library/importlib](http://docs.python.org/dev/library/importlib))
  ------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: 
### Copyright

This document has been placed in the public domain.
:::
