# NotebookInterfaceForIpython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This project aims to develop a file format and interactive support for documents which can combine Python code with rich text and embedded graphics. The initial requirements only aim at being able to edit such documents with a normal programming editor, with final rendering to PDF or HTML being done by calling an external program (to be written by the students).

- Can somebody provide more detail? From the brief description provided this looks like a combination of mail merge and PHP.

- This seems to be very much like what Mathematica does, using \"notebooks\" for code, graphics and formatted text. This would be much like an interactive interpreter, but the cells with code could called in any order, and the return value would be shown in the editor as text, except if it\'s type is Graphics (or something), in which case the graphic would be shown as an image in the editor just below the code who generated it. This would be very nice! \-- [NiltonVolpato](./NiltonVolpato.html)

- The [crunchy](http://code.google.com/p/crunchy) project seems to have the above functionality as part of its feature set, although its stated goal may be different. Oh, and its for Python rather than IPython.

- I\'m working on something called [Notebook](http://notebook.hortont.com) which aims to do something like this for arbitrary languages, but it\'s in its infancy at the moment (contributors are welcome!)
