# PortingPythonToPy3k

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: 
Caution!

**Python 2.x will no longer be supported after 1 Jan 2020.**

Python 2 reaches end of life in January 2020, and will no longer receive security updates. This page has resources to help with porting applications still running Python 2 to Python 3.
:::

:::::::::::::::::: 
### Porting Python Code to 3.x

There are three ways to support Python 3:

1.  make code run unmodified in both Python 2 and Python 3
2.  maintain a Python 2 base and use [2to3](2to3) to generate Python 3 code
3.  maintain a Python 3 base and use [3to2](3to2) to generate Python 2 code

Each approach has its strengths and weaknesses. Beyond this document, the approaches are also discussed in the official [HOWTO on porting Python 2 code to Python 3](http://docs.python.org/py3k/howto/pyporting.html).

::::::::: 
#### Approach 1: Make code run unmodified in both Python 2 and Python 3

Supporting code that runs in both Python 2.6 and Python 3 is now not much more difficult than porting to Python 3 and leaving behind Python 2.6.

Python 2.6 and 2.7 provide forward-compatibility for some of the new syntax in Python 3 through `__future__` import statements:

    from __future__ import (absolute_import, division,
                            print_function, unicode_literals)

Beyond `__future__` imports, two 3rd-party packages that greatly ease the task of supporting both Python 2 and Python 3 in a single codebase are:

- [future](http://python-future.org). future makes it possible to support both Python versions from one clean, hack-free codebase.
- [six](http://pythonhosted.org/six/). six is a thinner layer that also supports older versions\--like 2.3, 2.4, and 2.5\--which is very awkward without six.

For more information about the many forward-compatibility features that were added in Python 2.6 and Python 2.7, see these pages: [What\'s New in Python 2.6](http://docs.python.org/whatsnew/2.6.html) and [What\'s New in Python 2.7](http://docs.python.org/whatsnew/2.7.html).

::: 
##### Strings and Unicode

As of Python 2.6 the 2.x line includes a \"bytes = str\" alias in the builtins. Along with the bytes literal syntax, this allows binary data stored in a `str` instance to be clearly flagged so that it will use the correct type when the code is run in 3.x (either directly or via the [2to3](2to3) conversion tool). The reason it is done this way rather than backporting the 3.x `bytes` type is that most 2.x APIs that expect immutable binary data expect it as an 8-bit `str` instance.

[future](http://python-future.org) solves this problem by providing [backports](http://python-future.org/what_else.html#bytes) of the `bytes` and `str` objects from Python 3 that inherit from Python 2\'s `str` and `unicode` objects, respectively.

To support versions earlier than 2.6, it is possible to define the alias at the top of the module:

    try:
      bytes # Forward compatibility with Py3k
    except NameError:
      bytes = str

When using \"from \_\_future\_\_ import unicode_literals\" in a module, it may also be useful to insert \"str = unicode\" near the top of the module. This will ensure that \"isinstance(\'\', str)\" remains true in that module:

    try:
      str = unicode
    except NameError:
      pass # Forward compatibility with Py3k
:::

::::: 
##### Supporting older Python versions

::: 
###### Print Statement/Function

Since `print` is a statement in Python 2 and a function in Python 3, the `print` statement cannot be used in code that runs in both Python 2.5 and Python 3.

The solution for supporting both Python 2.6/2.7 and Python 3 is to use `print` as a function together with the `__future__` import:

    from __future__ import print_function
    print('hello world')

To support Python versions older than 2.6, you can instead use the print\_ function provided by six, or you can use the `sys.stdout.write` method as follows, replacing this:

    print 'hello world'

with this:

    import sys
    sys.stdout.write('hello world\n')
:::

::: 
###### Exceptions

Python 2.6 introduced the `as` keyword for exceptions which is used in Python 3:

    try:
        1 / 0
    except ZeroDivisionError as e:
        pass

Python versions \<2.6, which do not support the `as` keyword, have incompatible syntax with Python 3 for accessing the value of an exception. To support older Python versions, you can use the following idiom to save the value of an exception:

    import sys
    try:
        open('/path/to/some/file')
    except IOError:
        _, e, _ = sys.exc_info()
:::
:::::

::: 
##### Relative Imports

Python 3 makes a distinction between relative and absolute imports, dropping support for implicit relative imports. In Python 2.5+, use `from __future__ import absolute_import` to get the same behavior as Python 3. To support older versions as well, only use absolute imports. Replace a relative import:

    from xyz import abc

with an absolute import:

    from mypackage.xyz import abc
:::

::: 
##### Integer Division

Make sure to use from \_\_future\_\_ import division (introduced in Python 2.2) to get the non-truncating behavior, which is default in Python 3.
:::
:::::::::

::: 
#### Additional resources

- [http://stromberg.dnsalias.org/\~dstromberg/Intro-to-Python/](http://stromberg.dnsalias.org/~dstromberg/Intro-to-Python/)
:::

:::: 
#### Approach 2: Maintain a Python 2 base and use 2to3 to generate Python 3 code

Make sure the code runs in Python 2.6 and use [2to3](2to3)

This approach does *not* require that support for versions before 2.6 needs to be dropped. Even the need to test with 2.6 is not strict - one could just as well use this approach on code that has never been tested with 2.6, and is only known to work on 2.5.

[2to3](2to3) is a Python program that reads Python 2.x source code and applies a series of fixers to transform it into valid Python 3.x code. The standard library contains a rich set of fixers that will handle almost all code. [2to3](2to3) supporting library *lib2to3* is, however, a flexible and generic library, so it is possible to write your own fixers for [2to3](2to3). *lib2to3* could also be adapted to custom applications in which Python code needs to be edited automatically. For more information about [2to3](2to3), see: [http://doc.python.org/library/2to3.html](http://doc.python.org/library/2to3.html)

Usage of [2to3](2to3) can be integrated into the installation process: [2to3](2to3) can be run as a build step in distutils. With distutils, the following fragments are needed in a setup.py:

    try:
        from distutils.command.build_py import build_py_2to3 as build_py
        from distutils.command.build_scripts import build_scripts_2to3 as build_scripts
    except ImportError:
        # 2.x
        from distutils.command.build_py import build_py
        from distutils.command.build_scripts import build_scripts
    ...
    setup(...
      cmdclass = {'build_py': build_py,
                  'build_scripts': build_scripts
                 }
    )

This will leave intact all source files, and convert them to Python 3 in the build area, if setup.py is run on Python 3. \'setup.py install\' will then copy the 3.x version of the code into the target directory. If run on 2.x, nothing will change at all (as 2.x doesn\'t provide the build_py_2to3 class).

For distribute, this approach can be expressed as:

    setup(...
      use_2to3=True
    )

Manual changes (not done by [2to3](2to3)):

- os.path.walk =\> os.walk: see [issue4601](http://bugs.python.org/issue4601).
- rfc822 =\> email

::: 
##### Strings and Bytes

Design decisions needs to be taken what exactly must be represented as bytes, and what as strings (Unicode data). In many cases, this is easy. However, data sent or received over pipes or sockets are usually in binary mode, so explicit conversions may be necessary. For example, the Postgres API requires SQL queries to be transmitted in the connection encoding. It is probably easiest to convert the queries to the connection encoding as early as possible.

The standard IO streams (sys.stdin, sys.stdout, sys.stderr), are in text mode by default in Python 3. Calling sys.stdout.write(some_binary_data) will fail. To write binary data to standard out, you must do the following:

    sys.stdout.flush()
    sys.stdout.buffer.write(some_binary_data)

The flush() clears out any text (unicode) data that is stored in the TextIOWrapper, and the buffer attribute provides access to the lower-level binary stream. If you are only writing binary data, you can remove the text layer with sys.stdout = sys.stdout.detach() in Python 3.1; in Python 3.0, do sys.stdout = sys.stdout.buffer.
:::
::::

::: 
#### Approach 3: Maintain a Python 3 base and use 3to2 or futurize to generate Python 2 code

3to2 is a tool to help with automatically converting Python 3-only code into Python 2-only code. See [3to2](3to2).

An alternative is to use the `futurize` script from the [future](http://python-future.org) package with the [\--from3](http://python-future.org/automatic_conversion.html#backwards-3-to-both) option. This extends 3to2 by adding imports from the future package to provide Python 2 compatibility from the same codebase.
:::

:::::: 
#### Additional resources

- [http://python-future.org](http://python-future.org)
- [http://diveintopython3.org/porting-code-to-python-3-with-2to3.html](http://diveintopython3.org/porting-code-to-python-3-with-2to3.html)
- [http://packages.python.org/distribute/python3.html](http://packages.python.org/distribute/python3.html)
- [http://lucumr.pocoo.org/2010/2/11/porting-to-python-3-a-guide](http://lucumr.pocoo.org/2010/2/11/porting-to-python-3-a-guide)
- [http://lucumr.pocoo.org/2011/1/22/forwards-compatible-python/](http://lucumr.pocoo.org/2011/1/22/forwards-compatible-python/)
- [http://techspot.zzzeek.org/2011/01/24/zzzeek-s-guide-to-python-3-porting](http://techspot.zzzeek.org/2011/01/24/zzzeek-s-guide-to-python-3-porting)
- [https://pythonconverter.com](https://pythonconverter.com)
- Consultants available to hire for Python 2 support and migration: [https://wiki.python.org/moin/PythonConsulting/Python%202%20support%20and%20migration](https://wiki.python.org/moin/PythonConsulting/Python%202%20support%20and%20migration)
- Projects that need to continue using 2.7 can use a fork that promises to preserve backwards compatibility like [Tauthon](https://github.com/naftaliharris/tauthon)
- [Porting Py65 (and my Superboard) to Python 3](http://dabeaz.blogspot.com/2011/01/porting-py65-and-my-superboard-to.html) - 19 Jan 2011
- [Supporting Python 3: An in-depth guide - Migrating Strategies](http://python3porting.com/strategies.html)
- [\"Moving to Python 3\"](http://lwn.net/Articles/426906/) - LWN.net, 9 Feb 2011.

::: 
##### Martin\'s notes from psycopg2

- the buffer object is gone; I use memoryview in 3.x.
- various tests where in the code of the form if version_major == and version_minor \> 4 (say, or 5) This will break for 3.x; you have to write if (version_major == 2 and version_minor \> 4) or version_major \> 2
- Python code 2: setup.py needs to run in both versions. I had to replace popen2 with subprocess if available. Also, map() now returns an iterator, which I explicitly convert into list, and so on.
- Python code 3: the test suite doesn\'t get installed, and hence not auto-converted with [2to3](2to3) support. I explicitly added a [2to3](2to3) conversion into the test runner, which copies the py3 version of the test into a separate directory.
:::

::: 
##### Differences in specific libraries

These are porting notes on differences in third party libraries when run on Python 2 and Python 3.

- [PyQt4](./PortingPythonToPy3k(2f)PyQt4.html)
:::

::: 
##### More links

- a bunch of very useful reference code: [http://code.google.com/p/python-incompatibility/](http://code.google.com/p/python-incompatibility/)
- [PortingDjangoTo3k](PortingDjangoTo3k)
- [Porting Durus / QP / Qpy / Dulcinea, using approach targeting Python 2 and Python 3 off same code base](http://mail.mems-exchange.org/durusmail/qp/441/) - packages released but not in pypi yet.
- [Early2to3Migrations](Early2to3Migrations)
- [Stephan Deibel\'s blog post on code usable from Python 2.0 through 3.0](http://pythonology.blogspot.com/2009/02/making-code-run-on-python-20-through-30.html)
- [Python code that demonstrates differences between 2.5 and 3.0, and ways of making the same code run on 2.6 and 3.x](http://python-incompatibility.googlecode.com/)
- Georg Brandl\'s blog post collecting some information: [http://pythonic.pocoo.org/2008/12/14/python-3-porting-resources](http://pythonic.pocoo.org/2008/12/14/python-3-porting-resources)
- A blog post about porting experience: [psycopg2 porting to Python 3: a report](http://initd.org/psycopg/articles/2011/01/24/psycopg2-porting-python-3-report/)
- Reference Card: Moving from Python 2 to Python 3: [http://ptgmedia.pearsoncmg.com/imprint_downloads/informit/promotions/python/python2python3.pdf](http://ptgmedia.pearsoncmg.com/imprint_downloads/informit/promotions/python/python2python3.pdf)
- [Lennart Regebro\'s overview of Porting strategies](http://python3porting.com/strategies.html)
- [Dropbox\' migration to Python 3](https://blogs.dropbox.com/tech/2018/09/how-we-rolled-out-one-of-the-largest-python-3-migrations-ever/)
- [Instagram\'s migration to Python 3](https://thenewstack.io/instagram-makes-smooth-move-python-3/)
:::
::::::
::::::::::::::::::
