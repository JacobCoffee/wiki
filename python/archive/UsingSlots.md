# UsingSlots

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Introduction 

`__slots__`{.backtick} has a mixed reputation in the Python community. On the one hand, they are considered to be popular. Lots of people like using them. Others say that they are badly understood, tricky to get right, and don\'t have much of an effect unless there are many instances of objects that use them. This article will explain what they are, how, and why to use them, and when not to use them.

## What Is \`\_\_slots\_\_\` ? 

`__slots__`{.backtick} are discussed in the Python Language Reference under section 3.3.2, Customizing Attribute Access. The first thing we should understand is that `__slots__`{.backtick} is only used in the context of Python classes. `__slots__`{.backtick} is a class variable that is usually assigned a sequence of strings that are variable names used by instances. For example:

    class Example():
        __slots__ = ("slot_0", "slot_1")
        
        def __init__(self):
            self.slot_0 = "zero"
            self.slot_1 = "one"
            
    x1 = Example()
    print(x1.slot_0)
    print(x1.slot_1)

        zero
        one

The `__slots__`{.backtick} declaration allows us to explicitly declare data members, causes Python to reserve space for them in memory, and prevents the creation of `__dict__ `{.backtick} and `__weakref__`{.backtick} attributes. It also prevents the creation of any variables that aren\'t declared in `__slots__`{.backtick}.

## Why Use \`\_\_slots\_\_\`? 

The short answer is slots are more efficient in terms of memory space and speed of access, and a bit safer than the default Python method of data access. By default, when Python creates a new instance of a class, it creates a `__dict__`{.backtick} attribute for the class. The `__dict__`{.backtick} attribute is a dictionary whose keys are the variable names and whose values are the variable values. This allows for dynamic variable creation but can also lead to uncaught errors. For example, with the default `__dict__`{.backtick}, a misspelled variable name results in the creation of a new variable, but with `__slots__`{.backtick} it raises in an [AttributeError](./AttributeError.html).

    class Example2():
        
        def __init__(self):
            self.var_0 = "zero"
            
    x2 = Example2()
    x2.var0 = 0

    print(x2.__dict__.keys())
    print(x2.__dict__.values())
    ```

        dict_keys(['var_0', 'var0'])
        dict_values(['zero', 0])


    x1.slot1 = 1

        ---------------------------------------------------------------------------

        AttributeError                            Traceback (most recent call last)

        Input In [3], in <module>
        ----> 1 x1.slot1 = 1


        AttributeError: 'Example' object has no attribute 'slot1'

As mentioned earlier, a `__slots__`{.backtick} declaration uses less memory than a dictionary, and direct memory access is faster than dictionary lookups. `__slots__`{.backtick} variables use dot notation for assignment and referencing in exactly the same way as the default method. But it should be noted that attempting to access the `__slots__`{.backtick} tuple by subscription returns only the name of the variable.

    x1.__slots__[0]

        'slot_0'

## Using Other Types for \`\_\_slots\_\_\` 

The Python documentation states that any non-string iterable can be used for the `__slots__`{.backtick} declaration. For example, it is possible to use a list, and a user might want to take advantage of the fact that a list is mutable, whereas a tuple is not. It is possible to do so, but keep in mind two key points:

1.  `__slots__`{.backtick} is a class variable. If you have more than one instance of your class, any change made to `__slots__`{.backtick} will show up in every instance.

2.  You cannot access the memory allocated by the `__slots__`{.backtick} declaration by using subscription. You will get only what is currently stored in the list.

It is usually best to stick to the base case in order to avoid confusion and unexpected results. The following example shows how things can get confusing if you mutate a `__slots__`{.backtick} list.

    class Example3():
        __slots__ = ["slot_0"]
        
        def set_0(self, _value):
            self.__slots__[0] = _value
            
        def get_0(self):
            return self.__slots__[0]
        
    a = Example3()
    b = Example3()

    a.set_0("zero")
    b.set_0("not zero")
    a.slot_0 = 0

    print(a.get_0())
    print(a.slot_0)
       
    ```
        not zero
        0

## Default Values 

The following text appears in the Python Language Reference section 3.3.2.4.1:

- \"`__slots__ `{.backtick}are implemented at the class level by creating descriptors \... for each variable name. As a result, class attributes cannot be used to set default values for instance variables defined by `__slots__`{.backtick}; otherwise, the class attribute would overwrite the descriptor assignment.\"

Some readers might find this documentation confusing. It is not necessary for a user to implement descriptors in order to use `__slots__`{.backtick}. The point to remember is that default values for variables declared in `__slots__`{.backtick} cannot be set using class attributes. If default values are desired, they must be set in the `__init__(self)`{.backtick} definition. However, it is not necessary to assign all variables a value in the `__init__`{.backtick} function. As long as it has been declared in `__slots__`{.backtick}, a variable can be assigned a value using dot notation after the class has been instantiated.

## Why Not Use Slots? 

There may be cases when you might not want to use `__slots__`{.backtick}; for example, if you would like for your class to use dynamic attribute creation or weak references. In those cases, you can add `'__dict__'`{.backtick} or `'__weakref__'`{.backtick} as the last element in the `__slots__`{.backtick} declaration.

Certain Python objects may depend on the `__dict__`{.backtick} attribute. For example, descriptor classes depend on the `__dict__`{.backtick} attribute being present in the owner class. Programmers may want to avoid `__slots__`{.backtick} in any case where another Python object requires `__dict__`{.backtick} or `__weakref__`{.backtick} to be present. According to the Descriptor How To Guide for Python 3.9, the functools.cached_property() is another example that requires an instance dictionary to function correctly.

## Beyond The Basics 

There are a few things to be aware of when going beyond the basics. Slots variables declared in parents are available in child classes. However, child subclasses will have `__dict__`{.backtick} and `__weakref__`{.backtick} attributes unless they also define `__slots__`{.backtick}, which should only contain names of additional slots. Multiple inheritance with multiple slotted parent classes can be used, but only one parent is allowed to have attributes created by slots. The other bases must have empty slot layouts. For additional details, please see the Python Language Reference, section 3.3.2.4.1.

## Conclusion 

Using `__slots__`{.backtick} is straightforward. They are a simple, efficient, and safe alternative to Python\'s default method of data access. The only known exception is when another object requires access to the `__dict__`{.backtick} attribute.
