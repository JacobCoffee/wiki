# CodingProjectIdeas

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page is aimed to be the starting point of collection for ideas for projects which could benefit the Python community, either projects that help the Python core, develop the standard library, third party packages, or more.

Ideally, each project should be expanded into a more full-featured description, so that people can judge the value, the effort involved, the size of the project (takes a week, takes a month, etc.), who knows enough about the project to help out, etc.

(Formatting:

- Topics with a paragraph or so of thought, start new a page with a . in front of the wiki word, i.e. ` ./CleanupUrlLibProject` to scope the new pages a bit

- for topics not fleshed out beyond a sentence or two, indent the sentence six spaces on a newline below the topic title/summary; this is to make sure that the description does not overpower the title/summary

)

- [SimpleTodo](SimpleTodo): finite projects that improve (maybe just clean up) part of Python\'s implementation.

- .[/PythonCore](CodingProjectIdeas/PythonCore)

- .[/StandardLibrary](CodingProjectIdeas/StandardLibrary)

- [CodingProjectIdeas/Libraries](CodingProjectIdeas/Libraries)

- .[/PythonWebProgrammingIdeas](CodingProjectIdeas/PythonWebProgrammingIdeas)

- .[/ApplicationIdeas](CodingProjectIdeas/ApplicationIdeas)

- Port standard library modules implemented in C to Python
  - This is basically what the [PyPy](PyPy) project is doing. See their site for more details on what parts of the Python standard library have not yet been translated.

- .[/PythonDocInOpenEbook](CodingProjectIdeas/PythonDocInOpenEbook)

- fix some old, old bugs in sourceforge
  - This is not a high profile, totally new idea, but maybe even helps the community more than founding another web framework

- A better way to create (singlefile) executables by bringing the advantages of py2exe and [McMillans](./McMillans.html) compiler together.

  - Note that the next version of py2exe will allow this - it\'s 95% finished in CVS already \-- theller.

    Don\'t forget [cx_Freeze](http://starship.python.net/crew/atuining/cx_Freeze/) which has a lot of nice properties too. For Windows, Linux and Irix also look at [PyInstaller](http://pyinstaller.hpcf.upr.edu).

- Enhance the Python catalog of modules
  - [http://www.python.org/pypi](http://www.python.org/pypi) \-- contact [Catalog-SIG](http://www.python.org/sigs/catalog-sig/) for more.

  <!-- -->

  - ratings (both automatic and user)

  - admin interfaces

  - new pydotorg look and feel

  - fix and implement PEP 345

  - Auto-generate portions of a C extension module based off of a Python definition (e.g., create the function definitions, parsing of arguments, [PyTypeObject](./PyTypeObject.html) fields, init function for module, etc.). Would use AST off of existing Python code. Would need some way to update a generating C extension module when Python file changes without destroying extension module (as presumably body of functions have been filled in).

- [Helper tools for core Python development](CoreDevHelperTools)
