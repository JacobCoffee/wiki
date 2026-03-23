# Intermediate Conundrums

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Here are some short examples that have provided unexpected results for intermediate-level Python programmers.

Add new examples by copying and editing the following sample. *Edit your code so it is short and does nothing more than illustrate your problem.* Often programming problems are solved by making the effort to create simple examples that reproduce them. This page is meant for problems that appear in a few lines of code after the extraneous fluff has been removed. Things that may appear normal to experienced Python programmers but appear weird: at least when one first encounters them.

If you can answer your own question, do so. Otherwise leave the answer part for somebody else to edit.

### Sample (copy and edit me) 

**Bold**

    print("edit this")

**Usage**

    >>> edit this

**Question**

Edit this question.

**Answer**

Edit this answer.

### Metaclass Instantiation 

**Bold**

    class A(object):
        
        def __init__(self):
            self.__setattr__('x',1)
            
    a = A()

    class M(type):
        
        def __init__(cls,cls_name,bases,cls_dict):
            super(M,cls).__init__(cls_name,bases,cls_dict)
            cls.__setattr__('y',1)

    class B:
        __metaclass__ = M
        pass

**Usage**

    >>> import Play
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
      File "Play.py", line 14, in ?
        class B:
      File "Play.py", line 12, in __init__
        cls.__setattr__('y',1)
    TypeError: Error when calling the metaclass bases
         expected 2 arguments, got 1

**Question**

I thought creating the class B was analogous to creatig the object a. Clearly, my use of `__setattr__()` has stretched the analogy too far but \... I don\'t know what\'s going on.

**Answer**

While it is true that - conceptually - a class is an instance of its metaclass, there is still a big difference between class objects and instance objects (Yes, it\'s confusing).

A call to `instance.func(a, b)` gets translated into `instance.__class.__.func(instance, a, b)` \-- it\'s a bound method. A call to `cls.func(a, b)` does **not** get translated into `cls.__class__.func(cls, a, b)`, because it is an **unbound method**. It won\'t get translated into anything and that\'s why `__setattr__()` complains, it expects the object whose attribute should get set as its first argument. You could have written `M.__setattr__(cls, 'y', 1)` instead.

**Hex values passed to external code**

    ioctl(fd, 0xc0107307)

**Usage**

    >>> fd = open("/dev/null")
    >>> import fcntl
    >>> fcntl.ioctl(fd,0xc0107307)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    OverflowError: long int too large to convert to int

**Question**

How do I pass in a hex cmd to ioctl, or some other external function that is expecting an int, not a long?

**Answer**

There doesn\'t seem to be anyway to let python know that you are trying to build an unsigned value, so:

def convert32(number):

- return int(-(number \^ 0xffffffff)-1)

ioctl(fd, convert32(0xc0107307))
