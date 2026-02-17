# PyQt/AutoConnectingSlots

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Automatically Connecting Slots by Name 

The code in attachment to replace connectSlotsByName() has been working great for me. I\'m replacing more and more QObject.connect() -like code with it (I could not use the connectSlotsByName() from Qt because it binds callbacks twice (and yes, even if I did decorate my callbacks) and most importantly because my callbacks are not on the same object. \--[MartinBlais](MartinBlais)

:::: 
::: 
``` 
   1 def connectSlotsByName(container, callobj):
   2     """
   3     A version of connectSlotsByName() that uses a potentially different object
   4     to search for widget instances and to search for callbacks.  This is more
   5     flexible than the version that is provided with Qt because it allows you to
   6     bind to callbacks on any object, not just on the widget container class
   7     itself.  You can also call this with a number of combinations of container
   8     and callback objects.
   9 
  10     * 'container': an instance whose attributes will be inspected to find
  11       Qt widgets.
  12 
  13     * 'callobj': an object which will be inspect for appropriately named methods
  14       to be used as callbacks for widgets on 'container'.
  15 
  16     See QtCore.QMetaObject.connectSlotsByName() for some background info.
  17     """
  18     logging.debug('connectSlotsByName  container=%s  callobj=%s' % (container, callobj))
  19 
  20     for name in dir(callobj):
  21         cb = getattr(callobj, name)
  22         if not callable(cb):
  23             continue
  24 
  25         mo = re.match('on_(.+)_([^_]+)$', name)
  26         if not mo:
  27             continue
  28 
  29         nwidget, nsignal = mo.groups()
  30         try:
  31             widget = getattr(container, nwidget)
  32         except AttributeError:
  33             logging.debug("  Widget '%s' not found; method '%s' will not be bound." %
  34                           (nwidget, name))
  35             continue
  36 
  37         # Support the QtCore.pyqtSignature decorator.
  38         signature = '%s(%s)' % (nsignal, getattr(cb, '_signature', ''))
  39 
  40         logging.debug('  Connecting: %s to %s: %s' % (widget, signature, cb))
  41         QObject.connect(widget, SIGNAL(signature), cb)
```
:::
::::
