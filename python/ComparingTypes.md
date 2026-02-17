# ComparingTypes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

- Shows common types/objects from other languages and suggests a suitable python type/object.

These two tables to show some *comparable* collection types when transfering from another language to python. It gives you a good place to look if nothing else.

This first table shows the python object you might use if you would have used the other object in a previous language.

::: {}
+-----------------------------------------------------------+
| **Other Languages to Python**                             |
+-----------------------------------------------------------+
:::

- ::: {}
    ------------ --------- --------- ------- ------
    python       php       Java      C/C++   perl
    list         array\*   array     array   ?
    dictionary   array     hashmap   map     ?
    ------------ --------- --------- ------- ------
  :::

\*php array is more like a dictionary, but it can have numeric keys.\
\
And conversly if you were to try and replace something in python you can use the following Objects to mimic the python one.

::: {}
+-----------------------------------------------------------+
| **Python to other languages**                             |
+-----------------------------------------------------------+
:::

- ::: {}
    ------------- --------- ----------------------------------------------------------------- ------- ------
    python        php       Java                                                              C/C++   perl
    list          array\*   java.util.[ArrayList](./ArrayList.html)\<Object\>   array   ?
    dictionary    array     [HashMap](./HashMap.html)\<Object,Object\>          Map     ?
    array.array   ?         array                                                             array   ?
    ------------- --------- ----------------------------------------------------------------- ------- ------
  :::
