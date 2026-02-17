# ThreadLocalVariables

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Thread Local Variables 

**NOTE**

1.  **THIS PAGE IS OUT OF DATE**: thread-locals are implemented in Jython 2.5.

2.  This page has been left in place for historical purposes relating to Jython 2.2.

Thread-local variables are a concept that was intoduced into cpython at version 2.4. I will not describe them here. Instead I refer you to the [cpython documentation for the threading module](http://www.python.org/doc/lib/module-threading.html).

Thread-locals have not yet been introduced to jython, since it is currently at version 2.2. However, until they are \"officially\" implemented, there is a simple workaround to get thread-local variables in jython 2.2.

## Cpython implementation 

Cpython comes with two different implementations of thread-local variables

1.  A fast C implementation which is used on platforms where native thread-locals are supported.
2.  A slower pure-python implementation which is used as a fallback when a native implementation is not available.

As you may have guessed, the solution for jython is to use the pure-python fallback implementation. This implementation lives in the cpython **Lib/\_threading_local.py** module.

## How to use the cpython implementation on jython 

To use the cpython implementation on jython, simply copy the **Lib/\_threading_local.py** module to your jython **Lib** directory.

Before going any further, there is a simple code change you must make. The reason for making this change is that the pure-python implementation stores information in the instance dictionary of the **localbase** class. The key under which it is stored is a tuple, which is not legal in jython, whose **`__dict__` keys must be strings**.

Make the following change to the definition of the **localbase** class, and it will work on jython.

    class _localbase(object):
        __slots__ = '_local__key', '_local__args', '_local__lock'

        def __new__(cls, *args, **kw):
            self = object.__new__(cls)
            # Comment out the following line
    #        key = '_local__key', 'thread.local.' + str(id(self))
            # Replace it with this line
            key = '_local__key' + 'thread.local.' + str(id(self))
            object.__setattr__(self, '_local__key', key)
            object.__setattr__(self, '_local__args', (args, kw))
            object.__setattr__(self, '_local__lock', RLock())

## Importing the definition of threading.local 

Normally on cpython, you would import thread-local support like this

    from threading import local

On jython, using the above workaround, you could import it like this (assuming you\'ve copied the **\_threading_local.py** module to your **Lib** directory.

    try:
        from threading import local
    except ImportError:
        from _threading_local import local

Or maybe like this

    import threading
    if not hasattr(threading, 'local'):
        import _threading_local
        threading.local = _threading_local.local

And that should be all you need to do.

## Performance considerations 

Since java **does** have support for thread-local variables (see [java.lang.ThreadLocal](http://java.sun.com/j2se/1.4.2/docs/api/java/lang/ThreadLocal.html)), it is likely that thread-local variables will be natively implemented on jython fairly soon.

However, until that is the case, the above solution will be fully functional, if slightly slower. When a native implementation becomes available, no code-changes will be necessary, unless perhaps to tidy up the imports.

[AlanKennedy](AlanKennedy)
