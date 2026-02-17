# ComparisonJavaJython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Describe ComparisonJavaJython here.

::: {}
  ------------------ ---------------------------------------------------------------------------------------- ------------------------------------------------------------------------
  **Description**    **In Java**                                                                              **In Jython**
  array of doubles   xCoord = Double\[25\]                                                                    xCoord = jarray.zeros(25, \"d\")
  Size of array      mx = data.length;                                                                        mx = len(data)
  array assignment   double re = reFun.evaluate(new double\[\] {data\[i\]\[j\]\[0\], data\[i\]\[j\]\[1\]});   re = self.reFun.evaluate(\[data\[i\]\[j\]\[0\], data\[i\]\[j\]\[1\]\])
  ------------------ ---------------------------------------------------------------------------------------- ------------------------------------------------------------------------
:::
