# AlternativeDescriptionOfProperty

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Alternative Description of Property 

John Posner

Following is a revision of the official documentation for **property**, which can be found at [http://docs.python.org/library/functions.html#property](http://docs.python.org/library/functions.html#property). For an introduction to Python\'s property feature, see [ComputedAttributesUsingPropertyObjects](ComputedAttributesUsingPropertyObjects).

## property(\[getfn\[, setfn\[, delfn\[, docstr\]\]\]\]) 

**property** is a built-in data type, used to implement managed (computed) attributes. You assign the property object created by the call `property(optional-args)`{.backtick} to a class attribute of a new-style class (a class that inherits from **object**). When the attribute is accessed through an instance of the class, it dispatches functions that implement the managed-attribute operations.

The *getfn* argument is a function or method that will be dispatched to get the attribute value; likewise, *setfn* is a function for setting the value, and *delfn* is a function for deleting the attribute. *docstr* is a string that becomes the managed attribute\'s doc string; if you omit this argument, *getfn* \'s doc string, if any, is used instead.

This example creates a managed attribute named `x`{.backtick} in class `Cls`{.backtick}:

    class Cls(object):
        def __init__(self):
            self._x_storage = 100

        def get_val(self):
            return self._x_storage
        def set_val(self, value):
            self._x_storage = value
        def del_attr(self):
            del self._x_storage

        x = property(get_val, set_val, del_attr, "I'm the 'x' property.")

    # using the managed attribute
    obj = Cls()
    print obj.x + 5   # executes get_val(obj)
    obj.x = 55        # executes set_val(obj, 55)

A minimal usable property has a \"get the value\" function only, specified as the sole argument to `property()`{.backtick}. This makes it easy to create a read-only property using the decorator `@property`{.backtick}:

    class Cls(object):
        def __init__(self):
            self._x_storage = 100

        @property
        def x(self):
            return self._x_storage

        # decorator invocation above is equivalent to placing
        # the statement "x = property(x)" here

The decorator effectively converts the \"get the value\" method `x`{.backtick} into a read-only managed attribute with the same name.

Although you typically don\'t need to use them, a property object has its own attributes, `fget`{.backtick}, `fset`{.backtick}, and `fdel`{.backtick}, which provide direct access to the functions that it dispatches. You can use these attributes only if you access the property object through the class itself (not through an instance):

    >>> Cls().x
    100
    >>> Cls.x
    <property object at 0x00E905A0>
    >>> Cls.x.fget
    <function get_val at 0x00E6F7F0>

These attributes are read-only, but a property object also has `getter`{.backtick}, `setter`{.backtick}, and `deleter`{.backtick} methods, designed to be used as decorators, that populate or modify its `fget`{.backtick}, `fset`{.backtick}, and `fdel`{.backtick} attributes. For example, an existing property object\'s `setter`{.backtick} method accepts a single function/method argument and returns a *new* property object that is a copy of the existing one, but with its `fset`{.backtick} attribute set to the specified function/method. Thus, class `Cls`{.backtick} in the example above could be reimplemented like this::

    class Cls(object):
        def __init__(self):
            self._x = 100

        x = property()

        @x.getter
        def x(self):
            """I'm the 'x' property."""
            return self._x

        @x.setter
        def x(self, value):
            self._x = value

        @x.deleter
        def x(self):
            del self._x

Using the same name `x`{.backtick} for all the methods causes this name to be repeatedly rebound, to a series of property objects created by the decorators. The process starts with an \"empty\" property, and gradually builds up to a property that is \"full\" of dispatch functions.
