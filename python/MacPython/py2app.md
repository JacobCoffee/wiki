# MacPython/py2app

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

py2app is a Python setuptools command which will allow you to make standalone application bundles and plugins from Python scripts. py2app is similar in purpose and design to py2exe for Windows.

Latest Version 0.5.3

## Installation 

(py2app version 0.5 2010-07-28 Ronald Oussuroren)

\"easy_install-X.Y -U py2app\" should install the software, where X.Y is your favorite version of Python.

There is one new feature in this release: experimental support for python 3. This basicly means that I managed to build a single application as a standalone application bundle, without much testing. Alias builds and plugin bundles almost certainly don\'t work (the first because alias builds use the Carbon module which isn\'t available in python 3, the latter because I had to rewrite the C code in the application bundles and probably have to do the same for plugin bundles).

## Notes 

Execute a bundled app from the commandline to see error messages:

- myapp.app/Contents/MacOS/myapp

## Link Collection 

Current repository:

- py2app: [http://bitbucket.org/ronaldoussoren/py2app](http://bitbucket.org/ronaldoussoren/py2app)

- macholib: [http://bitbucket.org/ronaldoussoren/macholib](http://bitbucket.org/ronaldoussoren/macholib)

- modulegraph: [http://bitbucket.org/ronaldoussoren/modulegraph](http://bitbucket.org/ronaldoussoren/modulegraph)

- altgraph: [http://bitbucket.org/ronaldoussoren/altgraph](http://bitbucket.org/ronaldoussoren/altgraph)

Old subversion:

- source [http://svn.pythonmac.org/py2app/py2app/trunk/](http://svn.pythonmac.org/py2app/py2app/trunk/)

- documentation [http://svn.pythonmac.org/py2app/py2app/trunk/doc/index.html](http://svn.pythonmac.org/py2app/py2app/trunk/doc/index.html)

<!-- -->

- [http://svn.pythonmac.org/py2app/py2app/trunk](http://svn.pythonmac.org/py2app/py2app/trunk)

- [http://svn.pythonmac.org/macholib/macholib/trunk](http://svn.pythonmac.org/macholib/macholib/trunk)

- [http://svn.pythonmac.org/altgraph/altgraph/trunk](http://svn.pythonmac.org/altgraph/altgraph/trunk)

- [http://svn.pythonmac.org/modulegraph/modulegraph/trunk](http://svn.pythonmac.org/modulegraph/modulegraph/trunk) checkout and install. install with \"python setup.py install\" or let easy_install do it for you.

  **ATTENTION** some things are in /Library/Python and some things in /Library/Frameworks/Python.framework/ and there is /usr/lib/python too.

Original version:

- source [http://undefined.org/python](http://undefined.org/python) (points to repository)

- documentation [http://undefined.org/python/py2app.html](http://undefined.org/python/py2app.html) (might be old)

### Problems before 0.5 

- for 64-bit systems, the pypi package (0.4.2) failed.
  - even with macholib, altgraph and modulegraph gathered from all around.

- here

  is some workaround [http://hg.hardcoded.net/py2app](http://hg.hardcoded.net/py2app),

  - that i have not tested, as macholib is missing

### current state 0.5.2 

### questions

is it really necessary to run \'python setup.py py2app\' with sudo ?

it writes into /Library ?

and there still is an error that ::

- \'/Library/Python/2.6/site-packages/py2app-0.5-py2.6.egg/py2app/apptemplate/prebuilt/main-i386\'

is missing. There is only ::

- main-fat3 main-intel main-universal

linking main-fat3 to main-i386 ::

- \'cd /Library/Python/2.6/site-packages/py2app-0.5-py2.6.egg/py2app/apptemplate/prebuilt\' \'ln -s main-fat3 main-i386\'

makes the build succeed, when using sudo ::

- sudo python setup-mac.py py2app

but the app crashes ::

- mine.app/Contents/MacOS/mine Traceback (most recent call last):

  File \"MySQLdb/[init].pyc\", line 19, in \<module\> File \"\_mysql.pyc\", line 18, in \<module\> File \"\_mysql.pyc\", line 15, in [load [ImportError](./ImportError.html): \'/usr/lib/python2.6/lib-dynload/\_mysql.so\' not found ]

\_so is in the app, but not in the system (i like to keep things local)

copying \_mysql.so into /usr/lib/python2.6/lib-dynload, cured this.

Then it works.

## Development 

### Python Versions 

modulegraph/util.py requires python\>=2.6 for immutable bytes by \'b\"something\"\'.

### Testing 

py.test is used for testing. modulegraph/util.py contains tests in util.py. maybe revert to unittest.
