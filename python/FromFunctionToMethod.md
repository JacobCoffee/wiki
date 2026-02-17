# FromFunctionToMethod

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# From Function to Method 

Bruno Desthuilliers / John Posner

Python newcomers often have hard time understanding the \"magic\" behind Python\'s methods. And the truth is that Python\'s object model can be a bit peculiar when compared to most mainstream (or not-so-mainstream) object-oriented programming languages. (There are quite a few threads on c.l.py with either direct or indirect questions about what makes a Python method.)

Here\'s a brief \-- but hopefully helpful \-- overview of what exactly *is* a Python method, showing how Python magically inserts `self`{.backtick} or `cls`{.backtick} into the argument list of a method call.

## From Function \... 

The **def** statement *always* yields a function object. Always. If you don\'t believe it, try the following snippet:

    class Foo(object):
        def bar(self):
            return "baaz"

    print type(Foo.bar)               # <type 'instancemethod'>
    print type(Foo.__dict__['bar'])   # <type 'function'>

So, why is it that `type(Foo.bar)`{.backtick} is not the same as `type(Foo.__dict__['bar'])`{.backtick}? The answer is: attribute lookup rules and the descriptor protocol.

## \... To Method, via the Descriptor Protocol 

The descriptor protocol specifies that during an attribute lookup, if a name resolves to a class attribute *and* this attribute has a `__get__`{.backtick} method, then this `__get__`{.backtick} method is called. The argument list to this call includes either:

- the instance and the class itself, or

- **None** and the class itself

The return value of this call becomes the result of the attribute lookup. This mechanism is what provides support for computed attributes.

The **function** type implements this descriptor protocol. So when a function is an attribute of a class object and you access it as an attribute of the class itself, its `__get__`{.backtick} method is called with **None** and the class as arguments. When you access it as an attribute of an instance of the class, its `__get__`{.backtick} method is called with the instance and the class as arguments.

With the instance object (if any) and class object available, it\'s easy to create a method object that wraps the function object. This is itself a callable object; calling it mostly injects the instance as the first item in the argument list and returns the result of calling the wrapped function object.

A (naive) implementation of the whole thing might look like this:

    class method(object):
        def __init__(self, func, instance, cls):
             self.im_func = func
             self.im_self = instance
             self.im_class = cls

        def __call__(self, *args, **kw):
             # XXX : all sanity checks removed for readability
             if self.im_self:
                 args = (self.im_self,) + args
             return self.im_func(*args, **kw)

    class function(object):
         def __get__(self, instance, cls):
             return method(self, instance, cls)

So, what turns a function into a method is not that the function is defined in a class statement\'s body (well, not directly at least). Rather, it\'s that the function is an attribute of the class. For what it\'s worth, the following code is perfectly legal:

    class Foo(object):
        pass

    def func(obj):
        print "obj is %s " % obj

    Foo.method = func

    f = Foo()

    f.method()    # all three of these
    Foo.method(f) # invocations produce
    func(f)       # the same result

## References 

In the official Python documentation, the basics are at:

- [Implementing Descriptors](http://docs.python.org/reference/datamodel.html#implementing-descriptors)

- [Invoking Descriptors](http://docs.python.org/reference/datamodel.html#invoking-descriptors)

For an in-depth treatment, including a discussion of static methods and class methods, see:

- [Descriptor HowTo Guide](http://docs.python.org/2/howto/descriptor.html) (Python 2) - [Descriptor HowTo Guide](http://docs.python.org/3/howto/descriptor.html) (Python 3).
