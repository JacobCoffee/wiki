# IronPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## IronPython 

[IronPython](https://ironpython.net) is an open source implementation of Python for the .NET CLR and Mono, originally created by [Jim Hugunin](http://hugunin.net/index.html).

You can get news and download the latest version fromt the projects website: [https://ironpython.net/](https://ironpython.net/)

IronPython uses the Dynamic Language Runtime, a framework for writing dynamic languages for .NET which originated in IronPython 1. It also runs on Silverlight, a .NET browser plugin that runs on Windows and the Mac (and a Mono port called Moonlight runs on Linux). This means that IronPython can be used for client-side scripting *in the browser*.

IronPython is a Python compiler. It compiles Python code to in memory bytecode before execution (which can be saved to disk, making binary only distributions possible).

Performance is comparable to CPython - much faster for some things (where it can take advantage of the JIT compiler in the underlying platform), but slower for other things (particularly the built in container types where a lot of work has been done on optimising the CPython types).

Reasons that CPython programmers might be interested in IronPython include:

- Corporate credibility (introducing new technologies can be very difficult in some companies, if .NET is already established then you may need no excuse to start using IronPython)

- No [GlobalInterpreterLock](GlobalInterpreterLock) - IronPython has *no GIL* and multi-threaded code can use multi core processors

- The .NET framework library is *very big*. Particularly the user interface library Windows Forms is very good.

- IronPython is easy to embed in .NET applications as a scripting language

- Easier to extend than CPython (C# is memory managed and C# types can be used directly in IronPython with no wrapping)

- Silverlight!

A book on IronPython for Python and .NET developers: [IronPython in Action](https://www.manning.com/books/ironpython-in-action).

A useful resource for IronPython code examples, is the [IronPython Cookbook (archive)](http://web.archive.org/web/20190823082138/http://www.ironpython.info:80/index.php?title=Main_Page).

A book that introduces core concepts of IronPython programming using a .NET--centric approach is [Pro IronPython](https://link.springer.com/book/10.1007/978-1-4302-1963-7).

[IronPython Winforms tutorial (archive)](https://web.archive.org/web/20191130090900/http://www.zetcode.com/tutorials/ironpythontutorial/) at [ZetCode](http://www.zetcode.com/).

Mozilla announced a project to port the DLR (well, the underlying Core CLR that it uses in fact) to run on their Tamarin JIT. This means that IronPython could also run in future versions of Firefox. (See [IronMonkey](http://wiki.mozilla.org/Tamarin:IronMonkey)). Unfortunately this project has not made any progress since its announcement.

## Other Python-Like Languages for .NET/Mono 

Some other Python-like languages for .NET and Mono include:

- [BooLanguage](BooLanguage) - Syntax is very similar to Python\'s, yet the language is statically compiled. It implements many features that have been suggested for [Python3.0](../py3/Python3.0). See [Gotchas for Python Users (archive)](https://web.archive.org/web/20150504021553/http://boo.codehaus.org/Gotchas+for+Python+Users) for specific comparisons between boo and CPython.

- [Cobra Language](http://cobra-language.com/)

## Accessing .NET from CPython 

[Python for .NET (archive)](https://web.archive.org/web/20050225022729/http://www.zope.org/Members/Brian/PythonNet/index_html) is the reverse of IronPython, it lets you access .NET assemblies from CPython.

------------------------------------------------------------------------

See also: [PythonAndParrot](PythonAndParrot), [LoGix](LoGix), IronPython IDE
