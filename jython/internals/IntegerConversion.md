# IntegerConversion

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------
  **CPython function**                                                                                                                                                                                            **Jython method**
  long intobject::[PyInt](./PyInt.html)\_[AsLong](./AsLong.html)(register [PyObject](./PyObject.html) \*op)                                                             int [PyObject](./PyObject.html).asInt()
  [PyObject](./PyObject.html)\* intobject::[PyInt](./PyInt.html)\_[FromString](./FromString.html)(char \*s, char \*\*pend, int base)                                    [PyObject](./PyObject.html) [PyObject](./PyObject.html).`__int__`()
  Py_ssize_t intobject::[PyInt](./PyInt.html)\_[AsSsize](./AsSsize.html)\_t(register [PyObject](./PyObject.html) \*op)                                                  int [PyObject](./PyObject.html).`__int__`().asInt()
  Py_ssize_t abstract::[PyNumber](./PyNumber.html)\_[AsSsize](./AsSsize.html)\_t([PyObject](./PyObject.html) \*item, [PyObject](./PyObject.html) \*err)   int [PyObject](./PyObject.html).asIndex(err)
  int abstract.h::[PyIndex](./PyIndex.html)\_Check([PyObject](./PyObject.html) \*ob)                                                                                                  boolean [PyObject](./PyObject.html).isIndex()
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------
:::

When using asInt, consider whether you want to ensure the original object is an instanceof [PyInteger/PyLong](./PyInteger(2f)PyLong.html) prior to calling asInt on it. It\'s common to do this check before calling asInt, but is not required \-- otherwise asInt will attempt to implicitly convert non int/longs via user defined `__int__` methods.
