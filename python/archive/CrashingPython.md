# CrashingPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

While a lot of effort has gone into making it difficult or impossible to crash the Python interpreter in normal usage, there are lots fairly easy ways to crash the interpreter. The BDFL [pronounced](http://mail.python.org/pipermail/python-dev/2006-January/059621.html) recently on the python-dev mailing list:

        I'm not saying it's uncrashable. I'm saying that if you crash it, it's a
        bug unless proven harebrained.

I thought it might be worthwhile to document some ways the interpreter can be crashed \-- although most of these are very unlikely to crop up in real code.

There is also [a directory in SVN repository](http://svn.python.org/view/python/trunk/Lib/test/crashers/) that demonstrates known ways to crash Python.

## 1. ctypes

    def crash():
            '''\
            crash the Python interpreter...
            '''
            i = ctypes.c_char('a')
            j = ctypes.pointer(i)
            c = 0
            while True:
                    j[c] = 'a'
                    c += 1
            j

from [pyl](https://www.pooryorick.com/secure/wiki/Pub/Pyl)

## 2. Bogus Input 

Through Python 2.4 you could crash the interpreter by redirecting stdin from a directory:

        % python2.4 -c 'import sys ; print sys.version'
        2.4.1 (#3, Jul 28 2005, 22:08:40) 
        [GCC 3.3 20030304 (Apple Computer, Inc. build 1671)]
        % python2.4 < .
        Bus error

Starting with 2.5 the interpreter notices and aborts:

        % python2.5 -c 'import sys ; print sys.version'
        2.5a0 (41847M, Dec 29 2005, 22:21:03) 
        [GCC 3.3 20030304 (Apple Computer, Inc. build 1671)]
        % python2.5 < .
        Fatal Python error: <stdin> is a directory
        Abort trap

Some modules also do not perform rigorous checking of data they operate on. The marshal module can cause it to crash the interpreter when given certain strings:

        $ python
        Python 2.4.2 (#2, Sep 30 2005, 21:19:01) 
        [GCC 4.0.2 20050808 (prerelease) (Ubuntu 4.0.1-4ubuntu8)] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import os, marshal
        >>> while True:
        ...     try:
        ...         marshal.loads(os.urandom(16))
        ...     except:
        ...         pass
        ... 
        Segmentation fault

Executing random code, since the interpreter does not verify the well-formed-ness of the code object (invalids opcodes, wrong stack size, etc.). The following code is known to crashing python 2.4.3 on Windows XP as well as on Linux.

        from types import CodeType as code
        exec code(0, 5, 8, 0, "hello moshe", (), (), (), "", "", 0, "") 

## 3. Exhausting Resources 

There are a number of areas where resource exhaustion can crash the interpreter. Here\'s one fairly easy to demonstrate way to do it though:

        % python
        Python 2.5a0 (41847M, Dec 29 2005, 22:21:03) 
        [GCC 3.3 20030304 (Apple Computer, Inc. build 1671)] on darwin
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import sys
        >>> sys.setrecursionlimit(1<<30)
        >>> f = lambda f:f(f)
        >>> f(f)
        Segmentation fault

A slightly subtler example involves getting the interpreter to exhaust some resource internally while performing a single operation:

        $ python
        Python 2.4.2 (#2, Sep 30 2005, 21:19:01) 
        [GCC 4.0.2 20050808 (prerelease) (Ubuntu 4.0.1-4ubuntu8)] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        >>> f = lambda: None
        >>> for i in xrange(1000000):
        ...     f = f.__call__
        ... 
        >>> del f
        Segmentation fault

## 4. GC/weakref interaction 

Interaction between these two systems has historically been a sticky point for CPython. There is still at least one problem in Python 2.4.2:

        $ python
        Python 2.4.2 (#2, Sep 30 2005, 21:19:01) 
        [GCC 4.0.2 20050808 (prerelease) (Ubuntu 4.0.1-4ubuntu8)] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import weakref
        >>> ref = None
        >>> class Target:
        ...   def __del__(self):
        ...       global ref
        ...       ref = weakref.ref(self)
        ... 
        >>> def g():
        ...   w = Target()
        ...   w = None
        ...   print ref()
        ... 
        >>> g()
        Segmentation fault

## 5. Dangerous Modules 

Some modules are designed to allow programmers access to the guts of things. Naturally, they also give programmers the opportunity to shoot themselves in the foot. Here are a few.

- The `new` module allows you to construct various types of objects that normally can\'t be explicitly created from the interpreter. You can, for example, create `code` objects and give them arbitrary strings as their \"bytecode\". There\'s no telling how successfully the interpreter will handle such abuses.

- The `dl` module is available on many Unix systems. It provides an interpreter-level interface to the `dlopen()` function, giving you dynamic access to the functions in arbitrary shared libraries. No checks are performed on the arguments to the functions you call. Hilarity can thus ensue. (The `ctypes` module, under consideration for inclusion in Python 2.5, provides similar functionality.)

- The `buffer` builtin can also be dangerous, since it notionally claims a reference to a range of memory, but does so without going through a Python object or using the standard Python refcount system. This is visible when, for example, constructing a buffer from an `array.array`, then resizing the `array` such that it internally `realloc()`s its storage, moving the memory in the process. The `buffer` will now refer to an invalid pointer.

- The `gc` module can be manipulated to give access to partially constructed object, accessing fields of which can cause crashes.

## 6. Multithreading 

Some modules (or rather objects in them) can cause a crash, if they are used imporperly **in multiple threads**;

\* Refering to the same MySQLdb connection, can cause Segmentation fault.

## 7. Other 

I\`ve got another way:

I have written a Tkinter GUI editor \[called \"GWiz\"\] to help me create and maintain Tk GUIs for my own projects. \[The editor itself is a GWiz project, too.\] On several occasions, I have forgotten to close the GWiz-created GUI before exiting I.D.L.E., and Python \[always?\] crashes on exit with an \"application requested an abnormal termination\" error requester. When I remember to close my app before closing I.D.L.E., everything goes away cleanly. I should add code to GWiz to do sys.atexit() clean-up, but I do not know how to UNregister atexit callbacks; it would be easy enough to fix, but it would require that the atexit module\`s call-back registration return the item added to the call-back list, and the addition of another function to remove items from the call-back list. I can post modifications to the library module, if someone will tell me where to post them.

\-- [lwickjr](../archive/lwickjr), 2006-Apr-21

`python2.5 -c 'lambda((x)): x'`

Also causes segmentation fault on some systems (Archlinux, MacOSX, Windows)

\-- glen_quagmire
