# PylonsOnJythonOld

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: 
### Pylons (trunk, 0.9.7) on Jython

**Status**: Pylons is mostly working on Jython with a few different requirements:

> - The mako jython branch is required
> - The mako branch currently requires the explicit [inclusion of the antlr jar in your classpath](hhttp://www.nabble.com/_ast-td16622739.html)
> - Scripts created by setuptools (such as paster) currently aren\'t runnable for two reasons: 1) they aren\'t made executable (on POSIX) due to lack of os.chmod and 2) their shebang lines are invalid due to the fact that the Jython sys.executable is a shell script. This will require a patch to setuptools to fix POSIX (in a hacky way) and is going to require a lot more trouble on Windows. See [this thread](http://mail.python.org/pipermail/distutils-sig/2008-April/009357.html)
:::

:::::::::::::::::: 
### Pylons on Jython requirements that were made or are pending (not a complete list)

::: 
#### Installing Pylons and its dependencies

> - distutils and setuptools **(distutils is now supported and setuptools-0.6c8 supports jython-trunk, See** [SetuptoolsOnJython](SetuptoolsOnJython) \*\* for more details)\*\*
> - Ensure all dependencies\' tests pass. Pylons on jython buildbot: [http://pylonshq.com:8014/](http://pylonshq.com:8014/)
:::

::: 
#### nose

**nose trunk is now fully supported on Jython**

Pylons projects require nose, but most packages (including Pylons) use nose as their own test runners.

requires:

> - optparse module **(added in r4018)**
> - a fix for the cell variable (variables used in closures) bug here: [http://pylonshq.com/pasties/667](http://pylonshq.com/pasties/667) **(fixed in r4038)**
> - fix for new.instancemethod not allowing a PyType as its class argument **(fixed in r4051)**
> - fix for inspect.argspec not working (also needed for Pylons, among other things) **(fixed in r4053)**
> - imp.find_module returned entries in regard to bytecode files instead of .py files when they were available **(fixed in r4080)**
> - fix type names and class \_\_module\_\_ in doctests **(fixed in r4107, 4111)**
> - methods weren\'t always inheriting their inner functions\' \_\_name\_\_ and \_\_doc\_\_ **(fixed in r4109)**
> - compiler package (and compiler requires the parser module which Jython lacks). nose only needs the compiler module to use compiler.consts.CO_GENERATOR; until there\'s a parser jython will provide a broken compiler module that doesn\'t import parser **(added in r4114)**
> - Patches to nose for Jython compatibility: [http://code.google.com/p/python-nose/issues/detail?id=160](http://code.google.com/p/python-nose/issues/detail?id=160)
:::

::: 
#### Routes

**All tests pass, minus one doctest (that fails due to expecting CPython dict ordering)**
:::

::: 
#### Paste

requires:

**Paste is mostly working, with the exception of paste.cgiapp**

> - subprocess module: if it doesn\'t exist (Python 2.3) it uses a version copied over from CPython 2.4 (paste.util.subprocess24) **(added in r4150)**
> - paste.script.util.uuid requires the Python 2.3 int/long unification (PEP 237) phase B **(added in r4175)**
> - modulefinder module (imported in paste/\_\_init\_\_.py). Jython currently lacks it, and modulefinder relies on reading code objects via marshal.load **(modulefinder added in r4179)**
> - webbrowser module: paste.fixture imports it, Jython doesn\'t include it. It\'s pretty useless without the platform dependent CPython ic module on most environments. Without that, only console based browsers work and Jython\'s os.system can\'t redirect their stdin to actually make them usable **(Paste/WebTest trunk now only import webbrowser when it\'s needed)**
> - paste.util.quoting required a quirky fix to re.sub **(fixed in r4343)**
> - some tests rely on source code encodings (PEP 263) support
> - selectable files: cgiapp selects on files. we can emulate selectable files if the file is backed by a FileChannel, but cgiapp also selects on a subprocess\'s (with stdout=PIPE) stdout file, which is backed by a StreamIO. We\'ll probably never be able to fully support this module in Jython
:::

::: 
#### PasteDeploy

**All tests pass**
:::

::: 
#### PasteScript

**All tests pass**

> - PasteScript imports a number of CPython only modules (like pwd and fcntl) **(now conditionally)**
> - One failing test requires the Cheetah templating language (maybe we\'ll just skip it)
> - test_egg_finder doesn\'t seem to have its paths setup correctly **fixed, was a py.test to nosetest migration fixture problem**
:::

::: 
#### WebOb

**All the important tests are passing, the current failures are either due to testing \> 2.3 behavior, and one due to cStringIO\'s repr not matching CPython\'s**
:::

::: 
#### WebTest

**All tests pass**
:::

::: 
#### WebError

**All tests pass**
:::

::: 
#### Mako

**mako has a branches/jython, when combined with the experimental \_ast support in jython-trunk (see http://www.nabble.com/\_ast-td16622739.html) 95% of tests pass**

> - There are still issues with some tests relying on source code encodings (PEP 263) support
> - There\'s an issue with Unicode handling in some cases, because Jython\'s \_ast uses a \_ast.Unicode type (unlike CPython). Its \'s\' value returns a string instead of unicode (unlike CPython)
:::

::: 
#### Beaker

**All tests pass**

requires:

> - Paste (for paste.fixture) **can be installed/imported now**
> - base64.b64encode: might die on an attempting to import b64encode in beaker.crypto.PBKDF2 (at least it does when the tests are run) **fixed, b64encode is 2.4 specific, 2.3 backwards compat was added**
:::

::: 
#### WebHelpers

requires:

> - routes **(can be installed/imported now that Paste doesn\'t blow up)**
> - simplejson **(can be installed now)**
> - webhelpers.textile requires the unicodedata module **now imported only when needed**
> - the literal object requires a fix for our str/unicode \_\_add\_\_/\_\_radd\_\_ problems **fixed in r4350**
> - some tests rely on source code encodings (PEP 263) support
:::

::: 
#### FormEncode

requires:

> - gettext (which requires the locale module, which Jython lacks) **(both were added in r4077, 4084)**
> - required a couple fixes dealing with metaclasses **(fixes in r4336, r4339)**
> - some tests rely on source code encodings (PEP 263) support
> - attempts to import xml.parsers.expat.ExpatError
> - uses elementtree which isn\'t supported (not even the pure Python version works due to reliance on xml.parsers.expat). I\'ve contacted Fredrik Lundh about an experimental version of elementtree for Jython that\'s in his sandbox (mentioned here [http://42.blogs.warnock.me.uk/2004/09/](http://42.blogs.warnock.me.uk/2004/09/)[elementtree_is](/jython/elementtree_is).html ) but I haven\'t heard back from him =\[
:::

::: 
#### simplejson

**all simplejson tests were passing until a few revisions ago, when a test was added that utilizes the decimal module which we currently lack (though decimal is totally not required for simplejson)**

> - [SetuptoolsOnJython](SetuptoolsOnJython) (actually distutils) currently had trouble installing simplejson because it attempts to compile its optional C extensions (that help performance). It expected to catch a distutils.errors.CCompilerError **(fixed in r4157: A CCompilerError is now raised)**
:::

::: 
#### decorator

> - requires function.func_defaults to be writable and it currently isn\'t on Jython **(fixed in 4177)**
> - Note: decorators aren\'t currently supported in Jython, however the decorator module doesn\'t actually use decorators (works on CPython 2.3)
:::
::::::::::::::::::

::::: 
### Later down the road

::: 
#### SQLAlchemy

> - The [Dialect Refactor II](http://www.sqlalchemy.org/trac/ticket/672) ticket will need to be implemented to properly support using SQLAlchemy via Jython\'s DBAPI jdbc driver, [zxJDBC](http://jython.org/Project/userguide.html#database-connectivity-in-jython). Jason Kirtland has begun working on this.
> - Frank Wierzbicki has done some preliminary work on using SQLAlchemy with Jython, info [here](http://groups.google.com/group/sqlalchemy/browse_frm/thread/d60db24fe1683a41/09320033f406d78b?hl=en&lnk=gst), and gave a talk on his preliminary work at PyCon 2008: \"Database development with Jython, SQLAlchemy, and Hibernate\"
:::

::: 
#### Turbogears 2

> - Jim Baker started playing with Genshi on Jython. Genshi\'s Markdown class requires the same str/unicode \_\_add\_\_/\_\_radd\_\_ fix webhelpers needs.
> - Ariane Paola is slated to work on porting TurboGears 2 components for Jython for Google\'s Summer of Code
> - Georgy Berdyshev is slated to work on porting Zope components to Jython for Jython for Google\'s Summer of Code
:::
:::::
