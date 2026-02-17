# SubclassingBuiltInTypes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## See Also 

- [SubclassingDictionaries](SubclassingDictionaries)

# Discussion 

I wonder a lot, \"How do I subclass built-in types?\"

There\'s a related question: \"How do I figure out if something is *sort of* like a particular type?\"

My goal is to take something, and say, \"Does this act pretty much like an integer?\" Or \"does this act pretty much like a float?\" Or \"does this act pretty much like a dictionary?\"

You could: count up all the behaviors you rely on. Then test if they all exist. If they all exist, consider that item a fit.

But, that seems really hard, if you\'ve got a whole class with a ton of methods, all of which use the item. \"Counting up\" seems pretty hard in that case, and it seems like it would require a lot of discipline.

Is there, then, a set of tests that we can run over an item, to see if it acts \"pretty much like\" an int, a float, a dict, a string, blah blah blah\...? (Or, at least supports the interface for all those things?)

What do people do about this?

Because I read all these things saying, \"Don\'t use `type`!\" \"Don\'t use `isInstance`!\" But I don\'t see much in the way of what *to* use.

\-- [LionKimbro](LionKimbro) 2004-09-12 17:10:47

------------------------------------------------------------------------

\[lwickjr\]: I like to use `issubclass`. I suppose one could define a module in the Standard Library consisting entirely of empty classes with appropriate names, and inherit from them:

Module interfaces:

    ...
    class dictLike: pass
    ...

User module:

    import interfaces
    ...
    class Shelf(interfaces.dictLike,...):
    ...

Then other users could write `isinstance(Thing, interfaces.dictLike)`, and be assured that anything that passes the test /promises/ to be \"like a dictionary\".

Comments?

------------------------------------------------------------------------

For instance, on the `int` class, there are some gazillion methods:

#!python \>\>\> dir( 42 ) \[\'[abs]\', \'[add]\', \'[and]\', \'[class]\', \'[cmp]\', \'[coerce]\', \'[delattr]\', \'[div]\', \'[divmod]\', \'[doc]\', \'[float]\', \'[floordiv]\', \'[getattribute]\', \'[getnewargs]\', \'[hash]\', \'[hex]\', \'[init]\', \'[int]\', \'[invert]\', \'[long]\',

- \'[lshift]\', \'[mod]\', \'[mul]\', \'[neg]\', \'[new]\', \'[nonzero]\', \'[oct]\',

\'[or]\', \'[pos]\', \'[pow]\', \'[radd]\', \'[rand]\', \'[rdiv]\', \'[rdivmod]\', \'[reduce]\', \'[reduce_ex]\', \'[repr]\', \'[rfloordiv]\', \'[rlshift]\', \'[rmod]\', \'[rmul]\', \'[ror]\', \'[rpow]\', \'[rrshift]\', \'[rshift]\', \'[rsub]\', \'[rtruediv]\', \'[rxor]\', \'[setattr]\', \'[str]\', \'[sub]\', \'[truediv]\', \'[xor]\'\] \>\>\> }}}

If you want to make something that\'s functionally *like* an int, can you get around having to implement all these methods?

Maybe I have the wrong page title; Maybe this shouldn\'t be called \"SubclassingBuiltInTypes,\" but rather \"[SimulatingBuiltInTypes](./SimulatingBuiltInTypes.html).\"

\-- [LionKimbro](LionKimbro) 2004-09-13 00:00:50
