# CharlieGroves/DescrFailures

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Fixed 

- mro can\'t be modified by subtypes
  - altmro

- [http://jython.org/bugs/1603315](http://jython.org/bugs/1603315) - jython doesn\'t line up with CPython\'s expected kwargs

  - kwdargs

- [http://jython.org/bugs/1603312](http://jython.org/bugs/1603312) - an overflow error isn\'t raised by int subclasses for large values

  - ints

# Filed 

- [http://jython.org/bugs/1603314](http://jython.org/bugs/1603314) - [PyModule](./PyModule.html) is old style class

  - pymods
  - test_dir
  - modules

- [http://jython.org/bugs/1603315](http://jython.org/bugs/1603315) - jython doesn\'t line up with CPython\'s expected kwargs

  - keywords

- [http://jython.org/bugs/1506749](http://jython.org/bugs/1506749) - instance dicts can\'t be set or deleted

  - setdict

- [http://jython.org/bugs/1604250](http://jython.org/bugs/1604250)

  - descrdoc

- [http://jython.org/bugs/1604252](http://jython.org/bugs/1604252)

  - setclass

- copy doesn\'t work on instances of new style classes - [http://jython.org/bugs/1604258](http://jython.org/bugs/1604258)

  - copies
  - copy_setstate

- [http://jython.org/bugs/1604264](http://jython.org/bugs/1604264)

  - str_of_str_subclass

- [PyStringMap](./PyStringMap.html) is missing iter methods - [http://jython.org/bugs/1604265](http://jython.org/bugs/1604265)

  - dictproxyiterkeys
  - dictproxyitervalues
  - dictproxyiteritems

- [http://jython.org/bugs/1605006](http://jython.org/bugs/1605006)

  - str_of_str_subclass

- [http://jython.org/bugs/1605009](http://jython.org/bugs/1605009)

  - string_exceptions

- [http://jython.org/bugs/1605011](http://jython.org/bugs/1605011) - assigning [bases] doesn\'t change lookup in classes

  - test_mutable_bases
  - test_mutable_bases_catch_mro_conflict

- [http://jython.org/bugs/1605019](http://jython.org/bugs/1605019) - binding instance method to class calls class instead of instance

  - methods

- [http://jython.org/1605023](http://jython.org/1605023) - new on metaclass not called

  - metaclass

# To File 

- mutable_names - setting [name] on a class does nothing

- slotspecials - slots need [weakref]

# Don\'t Understand Failure 

- supers - subclassing super causes binding to break

- overloading - a\[0:10\] = \"foo\" doesn\'t call [setslice] on a

- comparison method on inherited class not called, superclass is used instead
  - inherits
  - binopoverride
  - str_subclass_as_dict_key
  - rich_comparisons

# Cpython Specific Tests 

- checks that things aren\'t allowed to inherit CFunction. I doubt we care.
  - errors

- expects immediate gc
  - slots
  - subtype_resurrection
  - weakref

- expects attributes to be descriptors
  - classic

- expects id == hash on object
  - specials
  - subclasspropagation

- expects classes to have [basicsize]

  - slotmultipleinheritance

# To Investigate 

- pickles
- delhook
- pickleslots
- subclass_right_op
- meth_class_get
- isinst_isclass
- proxysuper
- carloverre
