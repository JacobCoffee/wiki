# JythonReleaseNotes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Jython 2.7.0 Release Notes 

# Installing Jython 

Use the Jython installation jar to install Jython. Three installation modes are provided:

- GUI
- Text console
- Command line, for automated installation

From java -jar jython-installer-2.7.0.jar \--help, we can some examples of how to install Jython:

    example of a GUI installation:
            java -jar jython-installer.jar

    example of a console installation:
            java -jar jython-installer.jar -c

    example of a silent installation:
            java -jar jython-installer.jar -s -d targetDirectory

    examples of a silent installation with more options:
            java -jar jython-installer.jar -s -d targetDirectory -t minimum -i src
            java -jar jython-installer.jar -s -d targetDirectory -t standard -e demo doc -i src

A standalone Jython jar is also provided for users who intend to embded Jython.

# Running Jython 

Jython has a new launcher that is written in Python and executed by CPython 2.7. For Windows, CPython is bundled into the launcher (bin\\jython.exe) by the [PyInstaller](./PyInstaller.html) program. For other systems, the installer determines if CPython 2.7 is available, and if so, uses CPython 2.7 to launch Jython.

You can always see the command the launcher will use via the \--print option:

    $ bin/jython --print
    java -Xmx512m -Xss1024k -classpath /Users/jbaker/jython2.7.0/jython.jar:. -Dpython.home=/Users/jbaker/jython2.7.0 -Dpython.executable=/Users/jbaker/jython2.7.0/bin/jython -Dpython.launcher.uname=darwin -Dpython.launcher.tty=true -Dfile.encoding=UTF-8 org.python.util.jython

Often it may make more sense to directly execute Jython in this fashion.

The following environment variables do not usually have to be set, but if they are, they must be set correctly (see [http://bugs.jython.org/issue2346](http://bugs.jython.org/issue2346)):

- JAVA_ENCODING - Character set encoding, such as UTF-8

- JAVA_MEM - Java memory (sets via -Xmx)

- JAVA_OPTS - options to pass directly to Java

- JAVA_STACK - Java stack size (sets via -Xss)

- JAVA_HOME - Java installation directory, if set the java command is assumed to be at \$JAVA_HOME/bin/java

- JYTHON_HOME - Jython installation directory

- JYTHON_OPTS - default command line arguments

Empty settings are currently assumed to be significant, so use unset to remove if on a Unix-like system; on Windows, you can unset an environment variable via set ENVVAR=.

# Backwards-breaking changes 

FIXME

# New features 

FIXME

# NEWS 

More details can be found in the NEWS file, which is incorporated here:

    For more details, please see https://hg.python.org/jython

    Jython 2.7rc3
      Bugs fixed
       - [ 2311, 2319 ] Many compatibility fixes for launcher (bin/jython, bin/jython.exe)
       - [ 2332 ] jython -m test.regrtest -e now finds the tests it should
       - [ 1572 ] sys-package-mgr console messages silenced by default. Thanks to Emmanuel Jannetti.
       - [ 2327 ] Tests in org/python/tests/imp run only with  proper path
       - [ 2105 ] Fix inconsistent conversion of PyObject to String in StdoutWrapper
       - [ 1795 ] Support both subclassing from Java in a Python class and a Python implementation of __tojava__
       - [ 1861 ] Fix threading.Lock to support non-reentrant semantics
       - [ 2323 ] Fixes pickling issues in object.__reduce__ and cPickle.{load, loads}
       - [ 1540 ] Fix stack overflow due to how proxies for Java classes resolve super method in Java
       - [ 2325 ] Enable piping input into Jython without getting extraneous prompt output
       - [ 2324 ] Fix index computation for StringBuilder after seek back in cStringIO
       - [ 2171 ] Fixed direct calls to __pow__() on int, long and float with a modulo of None
       - [ 2326 ] Java's weakly consistent iteration of ConcurrentMap is compatible with mutation
       - [ 2322 ] Refreshed several networking modules from CPython 2.7.9 due to CVE-2013-1752
       - [ 1670 ] Added automatic type coercion of decimal.Decimal to java.lang.{Double, Float}
       - Pull in hand coded AST work into code gen in asdl_antlr
       - [ 2307 ] Fixed normalization of paths on Windows
       - Module tempfile now returns temporary directory in proper case (See also CPython issue 14255)
       - Faster extended slice deletion in bytearray.
       - [ 2304 ] Fixed __module__ missing from functions in the time and operator modules

    Jython 2.7rc2
      Bugs fixed
       - [ 2301 ] time.strftime now always returns a bytestring (fixes pip on Japanese locales)
       - [ 2297 ] Updates Jython installer to use jython.exe
       - [ 2298 ] Fix setuptools wheel bundled by ensurepip so it checks for Windows on Jython
       - [ 2300 ] Fix bin/jython.py to not consume subcommand args
      New features
       - Installer installs pip, setuptools by default, but custom builds can de-select.
         Does not change standalone usage. (Runs jython -m ensurepip as last install step.)
       - Makes jython.py be the default launcher (as bin/jython) if CPython 2.7 is available.
      Removed support
       - Installer no longer supports using an alternative JRE when generating Jython launchers.
         Instead just use JAVA_HOME environment variable to select the desired JRE.
         (Removed because of the new native launcher, jython.exe, that is now used on Windows.)

    Jython 2.7rc1
      Bugs fixed
       - [ 1793 ] Fix relative seek in read/write mode via a non-buffered readinto() method 
       - [ 2282 ] Speed up startup with compiled $py.class files included for standalone, full jars
       - [ 1371, 2283, 2296 ] More robustness wrt security managers, python.home, import of non-ascii names
       - [ 2068 ] Use position(long) setter to manually update file channel's position post-write.
       - [ 2288 ] Posix link and symlink support now uses NIO2
       - [ 2120 ] Use Java instead of JNR for os.chmod, os.mkdir when running on Windows
       - [ 2226 ] Matches CPython's re support of what counts as a Unicode whitespace codepoint
       - [ 1725 ] Speed up re matching by not executing SRE_STATE#TRACE in the sre regex engine
       - Exceptions with non-ascii args should not cause an exception when displayed on console
       - [ 2274 ] Remove Jython-specific pythonpath, test_pythonpath; update pwd to support unicode
       - [ 2289 ] Ensure core types are Serializable, specifically PyUnicode
       - [ 2272 ] Generalize adding special slots (__dict__, __weakref__); adds support for Werkzeug
       - [ 2280 ] Avoid deadlock at shutdown with synchronization of PySystemStateCloser, FinalizeTrigger
       - [ 2275 ] Upgrade JLine to support keyboard layouts using AltGr (such as Finnish) on Windows
       - Improve robustness of socket and SSL support, especially error handling
       - time.sleep(0) should always attempt to yield CPU
       - [ 2271 ] Restore __tojava__ to datetime.{date, datetime, time} classes
       - [ 2084, 1729 ] Robust handling of sun.misc.Signal exceptions across various JVM implementations
       - [ 2189 ] Add java_user scheme to support user directory installs
       - Fix Popen._internal_poll so that it does not race with java.lang.Process finalization
       - Fix reflection-based garbage collection traversal for CPython compatible gc semantics
       - [ 1491 ] Windows launcher now uses jython.exe (built with PyInstaller) instead of jython.bat
         This means that pip, nosetests, yolk, and other installed tool scripts finally work on Windows

      New features
       - Can add a __dict__ slot descriptor to a subclass of Java classes, such as java.util.HashMap
       - Directly execute zip files or dirs with top level __main__.py to support wrapper scripts
         generated by distlib, part of pip
       - Reflection-based traversal is now activated by default as a fallback for ordinary traversal.
         This impacts third-party extenders of PyObject. A warning is emitted that suggests next steps
         on how to avoid this cost.
       - Uses classpath wildcard in jython.py/jython.exe to minimize the launcher command line,
         (main benefit is Jython developers on Windows using dev builds)
       - Adds new Jython launcher written in Python, bin/jython.py, to be run by CPython 2.7

    Jython 2.7b4
      Bugs Fixed
        - [ 2032 ] Fixed typo in compiler/pycodegen.py
        - [ 2190 ] Raise ValueError when unichr() is called with isolated surrogate codepoint
        - [ 1057 ] Finalizer support (__del__) for new style classes
        - [ 2192 ] Server requests were hanging using jython, django and django-jython
        - [ 2204 ] Minimum (core) install will now suport Jython console
        - [ 2184 ] inspect.callargs, including anonymous tuples in function params
        - [ 2100 ] Fix deficiencies in PyUnicode beyond the BMP
        - Fix bug in supporting meta path importers for six
        - [ 2183 ] Rework function attributes support
        - [ 2115 ] Allow bound methods as arg for single method interface param
        - [ 2163 ] Refactor Py, PySystemState to init constants early
        - [ 2217 ] Update serial release to 3 for sys.version_info
        - [ 2090, 1494 ] Behaviour of long in the JSR-223 engine
        - [ 2196 ] Do not emit duplicate entries in building standalone jar
        - [ 1708 ] Ensure regrtest runs in a C locale to avoid failures
        - [ 2037 ] Prevent non-byte values appearing in str()
        - [ 2205 ] Guard via module import lock all entry points from Java into import
        - [ 1631 ] Fully proxy java.util.Map objects as Python dicts
        - [ 2215 ] Fully proxy java.util.List objects as Python lists
        - [ 2242 ] select.select and related socket.connect_ex fixes
        - [ 2241 ] Fully proxy java.util.Set objects as Python sets
        - [ 2239, 1825 ] os.getenv, os.listdir may return unicode instead of bytes
        - [ 2110 ] Update Java Native Runtime jars
        - [ 2236 ] Interactive parser does not accept try ... except E as e: syntax
        - [ 2232 ] Visit class decorators when visiting class def in scopes compilation
        - [ 2247 ] dict.pop should not add additional quoting in KeyError
        - [ 2238 ] os.system now uses a simpler wrapping of ProcessBuilder
        - [ 1561 ] Raises NotImplementedError if abstract method from Java is not implemented
        - [ 2221 ] Implement Popen.pid 
        - [ 2150 ] Fix regrtest to support -x to exclude tests
        - [ 1152612 ] All dict methods for __dict__ except views
        - [ 1762054 ] Add webbrowser module
        - [ 2252 ] Args in sys.argv are now unicode if characters > 127
        - [ 2092 ] Upgrade to JLine2 and add tab completion support
        - [ 2236 ] Interactive parser does not accept try ... except E as e: syntax
        - [ 2237 ] Fully conformant math and cmath support
        - [ 2244 ] More robust testing of math and cmath modules
        - [ 2224 ] id(...) now persists object resurrection and a pattern is provided to solve similar issues
                   (i.e. attributes bound to a PyObject via a WeakHashMap) in an analogue way (See JyAttribute.java).

      New features
        - Full support of Python buffer protocol, along with Java ByteBuffer support
        - Add index to PyUnicode facilitating O(1) access to strings beyond the BMP.
        - java.util.{Map, List, Set} are now treated as subclasses of the
          corresponding Python abstract base classes
        - jythonlib module to simplify usage of Java internals from Python;
          weakref collections now directly use corresponding collections from
          Google Guava and java.util
        - CPython's _json.c was ported to Java to speed up JSON encoding/decoding
        - Upgraded third party libraries
        - Initial support for ensurepip module
        - Callbacks can be registered/unregistered to be notified when
          bytecode is loaded, using jythonlib.bytecodetools
        - Jython now features an optional, but recommended-to-implement traverseproc-mechanism
          like CPython. This enables some new gc-features to optionally emulate CPython-specific
          gc-behavior. See doc in gc.java and Traverseproc.java.

      Potentially backwards breaking changes, removing silent errors:

        - remove method on proxied List objects now follows Python
          sematics: a ValueError is raised if the item is not found in the
          java.util.List. In the past, Java semantics were used, with a
          boolean returned indicating if the item was removed or
          not. Given how this interacted with Jython, such remove
          invocations were in the past silent, and perhaps were actually a
          bug.

        - d[key_not_present], if d implement java.util.Map, no longer
          returns None, but raises KeyError, which means this behavior now
          matches standard dict semantics.

        - Abstract methods of an inherited class or interface from Java now raise
          NotImplementedError, instead of returning None (in Java, null) or some
          "zero", if they are not implemented in the extending Python class.

        - os.getenv, os.listdir, sys.argv now return unicode instead of
          str values if a given value is not ascii, thus allowing such
          values to be passed through to Java, eg
          java.io.File(sys.argv[1]). Earlier such behavior was potentially
          silently failing in Python functions, but passing through to
          Java because of bug 2037. This behavior conforms with Python
          3.x, which uses Unicode.

    Jython 2.7b3
      Bugs Fixed
        - [ 2225 ] Jython+django-jython - no module named site
        - [ 1497 ] ast classes do not have appropiate base classes
        - [ 1980 ] ast.Eq, ast.Gt, ast.GtE, ast.In, ast.Is, ast.IsNot, ast.Lt, ast.LtE, ast.NotEq and ast.NotIn should be subclasses of ast.cmpop
        - [ 1981 ] ast.And and ast.Or should be subclasses of ast.boolop
        - [ 2130 ] Fix max such that any raised ValueError uses the correct error message text
        - [ 2180 ] default encoding is not UTF-8
        - [ 2094, 2147, 2174 ] Fix bugs in select.poll, threadpool group closing, and SSL handshaking
        - [ 2178 ] Update Apache Commons Compression to 1.8.1 for jar-complete builds
        - [ 2176 ] Fix bz2.BZ2File.read so it reads the number of requested bytes
        - [ 2028 ] Implement unicode._formatter_parser and unicode._formatter_parser
        - [ 1747 ] Synchonize runClosers upon shutdown
        - [ 1898 ] Support subprocess termination vs terminate/kill methods
        - [ 2096 ] Fix subprocess construction such that handles are inherited if not set
        - [ 2123 ] Preserve original name of console encoding
        - [ 1728 ] Make PyDictionary#equals() more robust, similar to PyTuple and PyList
        - [ 2040 ] Ensure that bz2 decompression has enough data to decode
        - [ 2146 ] Fix xrange compliance
        - [ 1591 ] Interactive interpreter stuck on '...' loop
        - [ 1982 ] Modify enumerate such that it can it work with arbitrarily long integers
        - [ 2155 ] Enable IP address objects to be used as tuples
        - [ 1991 ] Subclassed itertools classes can now chain, and be iterated by Java code
        - [ 2062 ] os.write accepts objects having the buffer API
        - [ 1949 ] Update collections.deque to 2.7 compliance, and is now threadsafe
        - [ 1066 ] Add CJK codecs, as well as other codecs available in Java but not in Jython directly
        - [ 2112 ] time.strptime now uses _strptime.py
        - [ 2123 ] Use Java codec throughout parser (not sometimes a Python one)
        - [ 2078 ] Fix tuple creation for inet6 addresses, and support for bound inet4 socket local address
        - [ 2088 ] Fix defaultdict so that derived classes __missing__ methods are not ignored
        - [ 2108 ] Cannot set attribute to instances of AST/PythonTree (blocks pyflakes)
        - [ 1982 ] builtin function enumerate() should support an optional 'start' argument
        - [ 1896215 ] findResource(s) for SyspathJavaLoader
        - [ 2140 ] Raise ValueError on args of invalid domain for math.sqrt, math.log
        - [ 2119 ] Updated *Derived.java classes as generated by src/templates/gderived.py.
        - [ 2087 ] Updated defaultdict to use LoadingCache idiom instead of deprecated ComputingMap
        - [ 2133 ] Fix memory leak by doing computed loads only with __getitem__ in defaultdict
        - Full bz2 support
        - Fix the struct module so that struct.Struct class can be derived from.
     
      Work on resource cleanup

        - RefReaperThread is now a Runnable to avoid ClassLoader resource leaks
        - ShutdownCloser is now a Runnable to avoid subclass audit issues under a SecurityManager
        - Remove shadowing of mutable statics in PySystemState, instead make them instance variables
        - Fix PySystemState such that it supports AutoCloseable, Closeable

      Potentially backwards breaking changes

        - Fix ThreadState so that Jython runtime can be unloaded, using Object[1] indirection
        - Use weakkey/weakvalue when caching ThreadState for a given thread, instead of using ThreadLocal
        - recursion_count is now more approximate, because not all entry/exit pairs are tracked
        - By default, site module is imported when using PythonInterpreter
          Use -Dpython.import.site=false (as of RC1) to not import site at all

      New Features

        - Added socket reboot work, using Netty 4 to fully support socket, select, and ssl API

    Jython 2.7b2
      Bugs Fixed
        - [ 1753 ] zlib doesn't call end() on compress and decompress
        - [ 1860 ] test failures in test_array.py
        - [ 1862 ] cStringIO does not support arrays as arguments
        - [ 1876 ] PYTHONIOENCODING unsupported, used (among others) by PyDev
        - [ 1926 ] Adjust MutableSet.pop test so we do not need to skip it
        - [ 1964 ] time.strptime() does not support %f in format
        - [ 2005 ] threading.Event object's wait([timeout]) function returns null instead of True/False.
        - [ 2013 ] %x hex formatting takes O(N^2) time.
        - [ 2020 ] str.translate should delete characters in the second arg when table is None
        - [ 2027 ] Discrepancy in bin(-num) output
        - [ 2033 ] test_strptime fails: test_mar1_comes_after_feb29_even_when_omitting_the_year
        - [ 2046 ] sys.stdin.readline() hangs when used interactively (JLine, Windows)
        - [ 2060 ] Thread ident missing
        - [ 2071 ] datetime strftime %f does not work
        - [ 2075 ] Incorrect padding for hex format strings
        - [ 2082 ] Unexpected (Pdb) prompt during regression tests
        - [ 2083 ] os.unlink() can delete directories
        - [ 2089 ] sys.stdout not flushed after sys.exit
      New Features
        - Command line option -E (ignore environment variables)
        - Environment variable PYTHONIOENCODING, and corresponding registry items
      Removed support
        - No longer supports Java 6; the minimum version is now Java 7

    Jython 2.7b1
      Bugs Fixed
        - [ 1716 ] xrange slicing raises NPE.
        - [ 1968 ] Fixes for test_csv.py.
        - [ 1989 ] condition.notify_all() is missing.
        - [ 1994 ] threading.Event doesn't have is_set method fixed.
        - [ 1327 ] ThreadState needs API cleanup work
        - [ 1309 ] Server sockets do not support client options and propagate them to 'accept'ed client sockets.
        - [ 1951 ] Bytecode Interpreter stack optimization for larger arguments
        - [ 1894 ] bytearray does not support '+' or .join()
        - [ 1921 ] compiler module broken in Jython 2.7 
        - [ 1920 ] Backport CO_FUTURE_PRINT_FUNCTION to Lib/compiler/pycodegen.py
        - [ 1914 ] Float formatting broken in many non-English locales in Jython 2.7
        - [ 1909 ] attrgetter does not parse dotted attributes
        - [ 1924 ] Implement operator.methodcaller
        - [ 1934 ] Break itertools.compress into a separate class 
        - [ 1933 ] Break itertools.cycle into a separate class
        - [ 1932 ] Make check for iterability in chain() arguments lazy
        - [ 1931 ] Check that there are exactly 2 filter args
        - [ 1913 ] Support short -W options
        - [ 1897 ] 2.7.0ax only has partial ssl support
        - array_class in jarray module returns the "Array of a type" class
      New Features
        - bytearray complete
        - a buffer API
        - memoryview
        - bz2 module

    Jython 2.7a2
        - [ 1892 ] site-packages is not in sys.path

    Jython 2.7a1
      Bugs Fixed
        - [ 1880 ] Sha 224 library not present in Jython
