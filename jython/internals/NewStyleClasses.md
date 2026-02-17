# NewStyleClasses

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Description of type/class unification: [Unifying types and classes in Python](http://www.python.org/2.2.2/descrintro.html)

There are two primary objectives:

1.  expose the necessary methods for making an existing class \'new-style\'
2.  generating a wrapper class for subclasses in python to implement

To do this there are two scripts:

- gexpose.py (for exposing)
- gderived.py (for deriving or subclassing)

They each have a simple input language for determing exactly what to implement. Note that these .expose files are hand generated.

For example, looking at a partial listing of list.expose:

    type_name: list
    type_class: PyList
    # exposed methods
    expose_meth: :- append o
    expose_meth: :i count o
    expose_meth: pop i?
    expose_meth: :b __nonzero__

So the type_name is \'list\'.

:::: 
::: 
``` 
>>> type([])
<type 'list'>
```
:::
::::

It is intended to expose methods for PyList.

- It exposes the method \'`append`\' which takes a PyObject and returns void.

- It exposes the method \'`count`\' which takes a PyObject and returns an int.

- It exposes the method \'`pop`\' which takes an optional int and returns a PyObject.

- It exposes the method \'`__nonzero__`\' which takes no arguments and returns a boolean.

Running gexpose.py produces some Java code.

    $ python gexpose.py list.expose > list.txt

Opening the file list.txt in your favorite editor you\'ll see the Java code. This code should then be pasted into the class PyList at the top of the file. This will result in a slew of compiler problems.

The problem is PyList doesn\'t have any of the methods. The generated code expected \'list_append\' but PyList has only \'append\' so the compiler complains. This is intended. Now for the boring part. For each method exposed, we need to create a new method. For example:

:::: 
::: 
``` 
public void append(PyObject o) {
    list_append(o);
}

final void list_append(PyObject o) {
    resize(length+1);
    list[length-1] = o;
}
```
:::
::::

Notice the new method is final and package protected. So follow the pattern for each method that needs to be exposed.

The special method `__init__` should delegate to \'list_init\' which needs to handle the constructor arguments of a list. If there is no argument, create a new list. If an argument, copy it\'s contents to a new list.

Make sure the class has a constructor which takes a PyType.

Finally, make sure the type is registered with `__builtin__`.

- It should also be noted an existing \'list\' was registered which provided the construction of a new list under the old scheme. I moved this code to PyList and deleted it from `__builtin__`. This is much better since all list construction now happens in one spot.

Run some quick tests:

:::: 
::: 
``` 
>>> list()
[]
>>> list([1,2,3])
[1, 2, 3]
>>> type([])
<type 'list'>
>>> list
<type 'list'>
>>> 
```
:::
::::

After that was done, run the regrtest and the bugtests. The bugtests caught a bug in my original effort. I had forgotten to make the constructor with PyType argument so any list(arg) call failed quickly as the PyType instance was the argument to the PyList(PyObject) constuctor and since PyType is not iterable, the call failed. The tests were great in tracking this down.

Next steps:

- automate this process a bit more if possible

- tuple, string, float, file -\> new-style

- `[].index.__self__` does not work correctly

- mutable `__bases__` and `__class__`

- support for `__del__`

- support for `__slots__`
