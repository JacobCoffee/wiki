# SubclassingDictionaries

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Subclassing Dictionaries 

The process differs by Python version.

## Python-2.2 

Derive from `dict`.

ex:

:::: 
::: 
``` 
   1 class Msg(dict):
   2 
   3     __slots__ = [] # no attributes
   4 
   5     def __init__(self, msg_type, kv_dict = {}):
   6         dict.__init__(self)
   7         self["msg-type"] = msg_type
   8         self.update(kv_dict)
   9 
  10     def Type(self):
  11         return self["msg-type"]
  12 
  13     def __getitem__(self, k):
  14         return self.get(k, None)
  15 
  16     def __delitem__(self, k):
  17         if self.has_key(k):
  18             dict.__delitem__(self, k)
  19 
  20     def __str__(self):
  21         pp = pprint.pformat(dict(self))
  22         return "%s:  %s" % (self.Type(), pp)
```
:::
::::

The `__slots__` line indicates that Msg has no attributes of its own, preserving memory; see [UsingSlots](UsingSlots).

## See Also 

[Python-2.2](../archive/Python-2.2), [SubclassingBuiltInTypes](SubclassingBuiltInTypes), [UsingSlots](UsingSlots)

## Questions 

- Is this bad Python-2.2 code? Make improvements..! I *do* think it\'s worth showing how to use slots in the context of subclassing dict; In many cases, I think, people would want to do it. I *do* wonder if slots should be specified before or after the initializer- something to put on the [UsingSlots](UsingSlots) page. \-- [LionKimbro](LionKimbro) 2003-09-07 17:07:24 [lwickjr](lwickjr): Before, I think, collected with the other declaritives.
