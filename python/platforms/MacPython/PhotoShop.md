# MacPython/PhotoShop

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[/AppscriptModule](./MacPython(2f)PhotoShop(2f)AppscriptModule.html) scripting for [/PhotoShop](./MacPython(2f)PhotoShop(2f)PhotoShop.html)

To apply unsharp mask to the first layer of the first document:

:::: 
::: 
``` 
   1 ps = app("Adobe Photoshop CS")
   2 ps.filter_(ps.documents[1].art_layers[1], using=k.unsharp_mask, with_options={k.threshold:2, k.amount: 200.0, k.radius: 1.0})
```
:::
::::

You need the latest version of [/AppscriptModule](./MacPython(2f)PhotoShop(2f)AppscriptModule.html) for the ` filter_() ` command to work correctly.
