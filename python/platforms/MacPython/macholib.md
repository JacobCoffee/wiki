# MacPython/macholib

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

I followed a link labelled \"macholib trac\", and it took me to this page, so here we go. ![;-)](/wiki/europython/img/smile4.png%20";-)")

issue #1: TypeError when macholib is just being installed due to setup_requires reporter: [zooko@zooko.com](mailto:zooko@zooko.com)

As detected by a TahoeLAFS buildbot:

[http://allmydata.org/buildbot/builders/zooko%20ootles%20Mac-amd64%2010.4/builds/225/steps/mac_exe/logs/stdio](http://allmydata.org/buildbot/builders/zooko%20ootles%20Mac-amd64%2010.4/builds/225/steps/mac_exe/logs/stdio)

When macholib is not currently installed, but is marked as \"setup_requires\" in the setup.py file, then py2app yields the following traceback:

    Installed /Users/tahoebuildslave/trunk6/mac/macholib-1.2-py2.5.egg
    Traceback (most recent call last):
      File "./setup.py", line 56, in <module>
        setup(**setup_args)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/distutils/core.py", line 112, in setup
        _setup_distribution = dist = klass(attrs)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/site-packages/setuptools-0.6c9-py2.5.egg/setuptools/dist.py", line 223, in __init__
        _Distribution.__init__(self,attrs)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/distutils/dist.py", line 267, in __init__
        self.finalize_options()
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/site-packages/setuptools-0.6c9-py2.5.egg/setuptools/dist.py", line 256, in finalize_options
        ep.load()(self, ep.name, value)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/site-packages/setuptools-0.6c9-py2.5.egg/pkg_resources.py", line 1913, in load
        entry = __import__(self.module_name, globals(),globals(), ['__name__'])
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/site-packages/py2app-0.3.6-py2.5.egg/py2app/build_app.py", line 27, in <module>
        import macholib.MachOStandalone
      File "build/bdist.macosx-10.3-i386/egg/macholib/MachOStandalone.py", line 8, in <module>
      File "build/bdist.macosx-10.3-i386/egg/macholib/MachOGraph.py", line 17, in <module>
      File "build/bdist.macosx-10.3-i386/egg/macholib/MachO.py", line 15, in <module>
      File "build/bdist.macosx-10.3-i386/egg/macholib/util.py", line 56, in <module>
    TypeError: Error when calling the metaclass bases
        cannot create 'builtin_function_or_method' instances

If you try the same build again (so this time a macholib egg is already present in the PWD then the build succeeds.
