# ctypes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

\"ctypes is an advanced [FFI](./FFI.html) \... package for Python \...\", according to its [home page](http://www.python.net/crew/theller/ctypes/).

[Python 2.5](./Python(20)2(2e)5.html) includes ctypes.

### CTypes FAQs 

**FAQ: How do I copy bytes to Python from a ctypes.Structure?**

    def send(self):
            return buffer(self)[:]

**FAQ: How do I copy bytes to a ctypes.Structure from Python?**

    def receiveSome(self, bytes):
            fit = min(len(bytes), ctypes.sizeof(self))
            ctypes.memmove(ctypes.addressof(self), bytes, fit)

**FAQ: Why should I fear using ctypes.memmove?**

ctypes.memmove emulates the memmove of C with complete faithfulness. If you tell memmove to copy more bytes than sizeof(self), you will overwrite memory that you do not own, with indeterminate consequences, arbitrarily delayed.

**FAQ: How do I start or stop reversing the bytes of each field?**

To decide the byte order of your fields, derive your class of `_fields_` from the `ctypes.LittleEndianStructure` class or from the `ctypes.BigEndianStructure` class rather than deriving your class from the local native `ctypes.Structure` class.

**FAQ: How do I change the byte length of a ctypes.Structure?**

Declare the max length and allocate that much memory, but then copy less than all of the memory allocated. You change the byte length that you use, not the byte length that ctypes.sizeof reports. For example:

    class MaxByteString(ctypes.Structure):
            _fields_ = [('bytes', 0xFF * ctypes.c_ubyte)]

**FAQ: How do I say memcpy?**

    ctypes.memmove

(Remember the difference in argument order between `memmove` and `memcpy`.)

**FAQ: How do I say offsetof?**

    def offsetof(self, field):
            return ctypes.addressof(field) - ctypes.addressof(self)

That example of an offsetof method works when self is an instance of the structure, the field is a member of self, and the field is an instance of an array class or structure class.

The offsetof macro of C works more often. The C macro works for any type of field and works when you have the class but no instance. Imitating the C macro with Python ctypes is possible but tedious: you begin by fetching the `_pack_` of the `self.__class__` and the `ctypes.sizeof` for each of the `_fields_`.

**FAQ: How do I say uchar?**

    ctypes.c_ubyte

**FAQ: How do I say ((void \*) -1)?**

    INVALID_HANDLE_VALUE = ctypes.c_void_p(-1).value

**FAQ: How do I contribute to this CTypes FAQ?**

FAQ: Why is the documentation for ctypes so utterly worthless and devoid of useful examples?

1\. Learn how to edit this Wiki page at:

[http://wiki.python.org/moin/WikiSandBox](http://wiki.python.org/moin/WikiSandBox)

2\. Post newbie CTypes questions into comp.lang.python, per the remarkable invitation of:

*from: [http://wiki.python.org/moin/MovingToPythonFromOtherLanguages](http://wiki.python.org/moin/MovingToPythonFromOtherLanguages)*

*Don\'t be surprised to have your questions answered by the original \... The best thing about comp.lang.python is how \"newbie-friendly\" the mail group is. You can ask any question and never get a \"RTFM\" thrown back at you.*

**FAQ: How do I learn Python CTypes, after learning C and Python?**

1\. Read a version of the CTypes tutorial:

The search [http://www.google.com/search?q=site%3Adocs.python.org+ctypes](http://www.google.com/search?q=site:docs.python.org+ctypes) once upon a time did find [http://docs.python.org/lib/module-ctypes.html](http://docs.python.org/lib/module-ctypes.html)

2\. Download and locally search a version of the CTypes tutorial.

The search [http://www.google.com/search?q=ctypes+tutorial](http://www.google.com/search?q=ctypes+tutorial) once upon a time did find [http://python.net/crew/theller/ctypes/tutorial.html](http://python.net/crew/theller/ctypes/tutorial.html)

3\. Read other CTypes wiki\'s:

The search [http://www.google.com/search?q=ctypes+python+wiki](http://www.google.com/search?q=ctypes+python+wiki) once upon a time did find [http://starship.python.net/crew/theller/wiki](http://starship.python.net/crew/theller/wiki)

**FAQ: How do I convert between c declarations (in .h files) to ctypes declarations?**

It would be nice if you could define a struct only once. Is there any module that can parse .h files structs? It seems like it should be here.

*The only such parse I know of is part of the python SWIG package ([http://www.swig.org/](http://www.swig.org/)). I imagine that it could become involved to write a far more lean and concise parser without ending up relying on a full fledge C compiler like this (unless you wanted to define only a subset of valid C headers for which to write your parser for).*

------------------------------------------------------------------------

- [CategoryFaq](CategoryFaq)
