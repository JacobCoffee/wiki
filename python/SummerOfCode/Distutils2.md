# SummerOfCode/Distutils2

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page describes tasks for the 2010 Summer of Code. Students and mentors are listed on the [Distutils2 teams](http://bitbucket.org/tarek/distutils2/wiki/GSoC_2010_teams) page.

**Contact: Tarek Ziadé \<[tarek@ziade.org](mailto:tarek@ziade.org)\>**

## GSOC Tasks 

### PEP 376 support 

- Implement pkgutil APIs described in PEP 376 : [http://bugs.python.org/issue8250](http://bugs.python.org/issue8250) \-- work started by people in the community already. (focus on speed with benches)

- Implement a dependency-graph builder

- Add basic PEP 376 support in Distribute \[and Pip is possible\]

Assigned to Josip.

### Installer / Uninstaller, PyPI 

- Implement Distutils2 APIs described in PEP 376.
- Add the uninstall command.
- think about a basic installer / uninstaller script. (with deps) \-- similar to pip/easy_install
- in a pypi subpackage;
  - Integrate a module similar to setuptools\' package_index

  - PyPI XML-RPC client for Distutils2: [http://bugs.python.org/issue8190](http://bugs.python.org/issue8190)

Assigned to Alexis.

### Distutils new commands 

- Add a post/pre-commit hook for install and uninstall commands: [http://bugs.python.org/issue8312](http://bugs.python.org/issue8312) see if it can be generic.

- enhance the check command (sanity tests)

- Move the upload_doc command from distribute

- add an optional call to upload_doc into upload

- Add a test command: [http://bugs.python.org/issue8324](http://bugs.python.org/issue8324)

Assigned to Konrad.

### Distutils build tool 

- Study 4Suite\' configure command

- Write a configure command: [http://bugs.python.org/issue8254](http://bugs.python.org/issue8254)

- Make install and build optionally use the configure file

- Make it possible to use setup.cfg to describe all the metadata: [http://bugs.python.org/issue8252](http://bugs.python.org/issue8252)

- Describe the resources files and the Python files using a \[resources\] or \[packages\] \[py_modules\]

  section in setup.cfg: [http://bugs.python.org/issue8253](http://bugs.python.org/issue8253)

- make setup.py optional (commands would be called through a -m call)

Assigned to Éric.

### Py3 support 

- Move the use_2to3 command from distribute
- Make sure distutils2 works under Py3 using 2to3

Assigned to Zubin.

### Tasks for all 

- Write a small tutorial in docs/ for each feature you add

### Misc 

- complete tutorial : [http://bugs.python.org/issue8255](http://bugs.python.org/issue8255)

- Promote and evangelize Distutils2--This will consist of helping python project to switch to/adopt Distutils2. We will define a list of targets at the beginning and the student will be in charge of helping them switching to Distutils2 if they want.
