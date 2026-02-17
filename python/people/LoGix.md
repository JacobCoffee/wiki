# LoGix

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A front-end to Python that has powerful macro capabilities.

[http://livelogix.net/logix/](http://livelogix.net/logix/) For example, adding an \"isa\" operator:

    [base]: defop 50 expr "isa" expr func ob typ:
          :     return isinstance(ob, typ)

    [base]: 'a' isa str
    True

------------------------------------------------------------------------

See also: [BooLanguage](BooLanguage), [IronPython](IronPython)
