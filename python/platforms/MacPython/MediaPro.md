# MacPython/MediaPro

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

iView MediaPro\'s scripting support contains a couple of design flaws that together cause by-index references to fail when scripting it from Python+appscript. (This bug doesn\'t affect [AppleScript](./AppleScript.html) users, as [AppleScript](./AppleScript.html)\'s own shortcomings mask the problem there.) MediaPro 3.1.1 and earlier versions are affected (a bug report has been submitted, so future versions may rectify this).

Example:

    print app('iView MediaPro').windows[1].get()
    # -> app('iView MediaPro').windows[1L] # (IMP returns the window index as an unsigned integer)

    print app('iView MediaPro').windows[1L].get()
    # -> CommandError -1703: Some data was the wrong type. # (IMP only accepts a signed integer for the window index)

The following module provides a workaround for this bug on appscript 0.16.0 and later by rebuilding any by-index references before they are packed and sent to [MediaPro](./MediaPro.html).

    """impdaddy.py -- Workaround for iView MediaPro's buggy by-index reference forms."""

    __all__ = ['iViewMediaPro']

    from appscript import *

    class _IMPDaddy:
        """This class reconstructs an existing aem reference, making sure any 
            by-index specifiers always use typeSInt32 index numbers.
            
            iView MediaPro generates by-index specifiers with typeUInt32
            by-index specifiers, but only accepts typeSInt32 values.
        """
        
        def __init__(self):
            self.ref = None
        
        def __getattr__(self, name):
            if name in ['app', 'con', 'its']:
                import aem
                self.ref = getattr(aem, name)
            else:
                self.ref = getattr(self.ref, name)
            return self
        
        def __call__(self, *args, **kargs):
            self.ref = self.ref(*args, **kargs)
            return self
        
        def byindex(self, i):
            """Fixes by-index specifiers."""
            self.ref = self.ref.byindex(int(i))
            return self


    def iViewMediaPro():
        """Returns an app object for iView MediaPro, inserting a workaround for an IMP bug 
            that causes it to choke on its own by-index references. For appscript 0.16.0+
        """
        iview = app('iView MediaPro')
        realpack = iview.AS_appdata.pack
        def custompack(data):
            # intercept any appscript/aem references and fix them up before packing
            if hasattr(data, 'AS_aemreference'):
                data = data.AS_aemreference
            if hasattr(data, 'AEM_resolve'):
                rebuilder = _IMPDaddy()
                data.AEM_resolve(rebuilder)
                data = rebuilder.ref
            return realpack(data)
        iview.AS_appdata.pack = custompack
        return iview

Example usage:

    from impdaddy import iViewMediaPro

    imp = iViewMediaPro()

    print imp.windows[1L].get() # this now works
    #-> app(u'/Applications/iView MediaPro 3/iView MediaPro.app').windows[1L]

(For the curious, the above module also provides an interesting demonstration of aem\'s `AEM_resolve` method, which \'replays\' the full sequence of method calls used to construct an existing aem reference. Appscript uses this method itself when converting generic references to real references, and when generating string representations of appscript references for on-screen display.)
