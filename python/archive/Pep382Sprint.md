# Pep382Sprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PEP 382 Sprint 

- Silver Spring, Maryland USA 21-Jun-2011 2000UTC

Attendees:

- Erik Bray
- Jason Coombs
- Michael Droettboom
- Eric Smith
- Barry Warsaw
- Steve Waterbury

Bitbucket clone: [https://bitbucket.org/embray/pep-382-sprint](https://bitbucket.org/embray/pep-382-sprint)

# Tasks 

- review Martin\'s branch `hg clone http://hg.python.org/features/pep-382`

  - look for reference counting issues

  - other initialization issues (`*foo = NULL`)

- do we have sufficient test coverage?
  - top-level non-trivial [init].py

  - various reload scenarios

  - both `__init__.py` and `.pth` file exists

  - multiple .pth files in the same namespace package directory

  - `.pth` files that contain path names: do they set `__path__` correctly?

  - is `package.__path__` set correctly? must contain one `*`, at the beginning

  - test that `load_module_with_path()` (pep 302 loader) gets called correctly

  - test [AttributeError](./AttributeError.html) when that\'s missing

- is `importlib` is covered?

- pull down 3rd party pep 302 loader and see if/how it\'s broken

- refactor import.c to yank out anything that can be written as a 302 loader?
  - \--e.g. zip import\-- Already done, but zipimport needs to support PEP-382
  - load-from-file could just be a PEP 302 loader
  - could land independently (but need to go through python-dev)
  - does this really make our lives easier?

- attempt a merge of mvl\'s branch to trunk

- figure out build problems on windows (jaraco)

- test_imp gives one failure on fedora (make sure imp module has been updated) - **fixed**

- stylistic cleansing of import.c
  - tests against 0 vs. NULL

  - mispellings

  - should LBYL on [AttributeError](./AttributeError.html) in `find_path`

# PEP Questions 

- Clarify what happens when a directory contains both an `__init__.py` and a `.pth` file

- PEP should clarify what the impact of the PEP is on existing namespace packages (i.e. those with magic `__init__.py` files

- Do `import` statements in `.pth` files get ignored or does it raise an error?

- Impact of PEP on setuptools/packaging/distutils\*

- Use case for extending existing .pth file syntax (minus `import` support)? I.e why are non-\* lines in the .pth files added to [path]? And should these really be called `.pth` files? At least clarify the PEP!

# Action Items 

\"It\'s all so freaking big we can never make any progress on it\" - ES

Finish off PEP 302:

- Jason [created a bitbucket clone](https://bitbucket.org/jaraco/cpython-pep302) for import.c refactoring

- Eric to experiment zipping the stdlib and delete the Lib dir by sys.path hacking, does Python still work?

- Isolate a path loader to match zip importer perhaps refactored from importlib

- Add this loader to the front of path_hooks and see if stdlib can be imported

- Rip out the stuff out of import.c that\'s not associated with calling path_hooks

- Benchmarking, is the Python version good enough? If so, who needs C?

- If not, make a C version of the loader

In parallel:

- Complete the PEP 382 tests identified above
- Clarify open PEP 382 questions
- Rewrite zipimport in Python?
- create a sub-mailing list on python.org
