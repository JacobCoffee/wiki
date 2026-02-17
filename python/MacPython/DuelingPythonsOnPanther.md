# MacPython/DuelingPythonsOnPanther

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**How to install newer Python with the Apple installed Python.**

Panther comes with Python 2.3.0, installed using Framework install, at `/System/Library/Frameworks/Python.framework/Versions/2.3`. If you want to install a newer version, you might get the [Fatal Python error: Interpreter not initialized (version mismatch?) error](http://www.pythonmac.org/wiki/FAQ#head-097ea8835a1f3701e2a081691e163c18b115bbc0).

You can avoid this problem by installing Python like this:

1.  Configure, make and make install - using standard unix install:

        ./configure
        make
        sudo make install

    Python will be installed to \'/usr/local\'

2.  Create a link to python with a unique name:

        cd /usr/local/bin
        ln python python2.3.4

3.  In your scripts, use:

**Technical details**

This problem is caused by this [bug 932977](http://sourceforge.net/tracker/index.php?func=detail&aid=932977&group_id=5470&atid=105470). Because of bug in darwin, Python does not get `/usr/local/bin/python` as first argument, but only `python`. So it tries to look for python in the system path, and of course finds `/usr/bin/python`.

The results is that you run Python 2.3.4, and it loads modules from Python 2.3.0. When you try to load extenstion modules, like `cStringIO`, you get this `Interpreter not initialized` error.

This problem is fixed in Python 2.4a3, see [http://www.opendarwin.org/pipermail/cvs-darwinports-all/2004-February/023306.html](http://www.opendarwin.org/pipermail/cvs-darwinports-all/2004-February/023306.html) .
