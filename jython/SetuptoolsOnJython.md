# SetuptoolsOnJython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### setuptools includes Jython trunk support as of version 0.6c8! 

Setuptools trunk and its 0.6 branch have had [a couple of changes](http://svn.python.org/view?rev=60062&view=rev) (discussed [here on distutils-sig](http://mail.python.org/pipermail/distutils-sig/2008-January/008617.html)) made to fix incompatibilities with Jython.

Even as of these changes, there are a couple improvements that can be made to running setuptools on Jython:

- Most importantly, the lack of os.chmod. chmod can be implemented with JNA. setuptools simply avoids chmod if it does not exist as of ***[r60062](http://svn.python.org/view?rev=60062&view=rev))***

- setuptools\' use of marshal: setuptools uses marshal.load in two places \-- to get a code object from a .pyc file, so it can scan the code object\'s co_names and co_consts (basically to read a module\'s variables without importing it). This isn\'t portable: Jython\'s compiled .pys (actually Java .class files) can\'t be read via marshal, nor do Jython\'s code objects support co_names and co_consts
  - the two places this is used:

  - when a package doesn\'t mark itself as zip_safe, setuptools will scan it for special variable names (like \'[file]\') to determine zip_safetyness. ***(setuptools defaults to zip_safe=False for archives that don\'t set it as of [r60062](http://svn.python.org/view?rev=60062&view=rev))*** We could get around the lack of marshal compatibility here by using the tokenize module to read the source code. This wouldn\'t work in the rare case of a byte-code only egg.

  - setuptools.depend.get_module_constant: a generic way to grab the value of a module variable. currently only used by Require.get_version ***setuptools.depend is experimental, unsupported functionality that we don\'t need to worry about***

- We should consider making the -E command line argument disable the registry

The Jython changes made for setuptools:

- PEP 302 style zipimport module ***Added in r3463***

- number of misc. Jython bug fixes ***most already committed***

- file descriptor support for tempfile.mkstemp, os.open and tarfile ***Added in r3711***

- tempfile.mkstemp ***Added in r3712***

- os.chdir (also needed for distutils) ***Added in r3844***

- tarfile module ***Added in r3850***

- a valid sys.executable. required by setuptools and distutils for spawning subprocesses. ***Added in r3867, enabled via -Dpython.executable (see [http://article.gmane.org/gmane.comp.lang.jython.devel/4068](http://article.gmane.org/gmane.comp.lang.jython.devel/4068) )***

- a site-packages dir (jython needs to include it on sys.path by default). required by setuptools and distutils ***Added in r3886***

- distutils: requires [a number of small patches](http://hg.underboss.org/jython-pjenvey/rev/1026fe32c01c):

  - a valid sys.executable ***Added in r3867***

  - getpass module ***Added in r3876***

  - distutils metadata for the os.name == \'java\' (like path names, default bdist type, etc)

  - a jython spawn-like function: \"error: don\'t know how to spawn programs on platform \'java\'\". os.system works as a replacement

  - compile .py files to \$py.class instead of .pyc ***distutils and these last 3 modifications were added in r3888***

- imp.acquire/release_lock (and the accompanying lock_held which we don\'t actually need). Exposes the import machinery\'s lock via the imp module ***Added in r3894***

- setuptools runs a test to ensure .pth files work by running \"sys.executable -E -c pass\". -E is ignore environment on CPython, but is different on Jython (takes an argument):
  - -E codec : Use a different codec the reading from the console. ***-E codec renamed to -C codec in r4013. -E is now a noop (but valid) command line arg***

- os.lstat. setuptools cut and pasted shutil\'s rmtree from CPython 2.4, which uses lstat to check for a directory vs a symlink to a directory. We now support an os.stat that fills in st_mode\'s directory bit, but can we support lstat? (We definitely can with JNA)? Can setuptools avoid lstat completely (requiring a patch)? I don\'t think Java can safely determine a sym link yet. Java 1.7\'s JSR 203 (nio part 2) should address this as well as chmod, but we obviously need a solution for Java 1.5 ***Turned out we can implement a simple lstat in pure Java, added in r4014***

- for Jython on Windows: distutils.filelist.translate_pattern required ntpath to work correctly, and setuptools required chdir to not canonicalize the pathname via java.io.File ***both issues fixed with usage of ntpath, in r4171***
