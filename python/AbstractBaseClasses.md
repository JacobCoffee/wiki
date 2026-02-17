# AbstractBaseClasses

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Possible Python 3K Class Tree? 

\[**News Update:** some ideas from this wiki page are being incorporated into [PEP 3119](http://python.org/dev/peps/pep-3119/).\]

This page contain an incomplete thinking-out-loud description of a re-factoring of the base and built-in Python types into a set of Abstract Base Classes (ABCs) and concrete types. This would probably be a good time to enumerate the exceptions various basic operations can raise, as well.

Some questions:

- How to handle optional and keyword parameters to methods, such as the *cmp* parameter to the \"sort\" method on `MutableSequence`? Are they different methods with and without the parameter? Are they just keyword methods, and don\'t affect the method differentiation? \[+1 to drop \'cmp\' completely and make \'key\' the first positional arg\]

- What is the real relationship between Sequence, Mapping, Set, and Dict? Isn\'t a Sequence also a mapping (of integer index values to Object sequence values)? Isn\'t a Dict also a Set (of key values)?

- Should the `MutableSequence` interface be further broken up \-- for instance, a `deque` may not be appropriate for sorting?

- Currently, `Boolean` is a subtype of `Integer`, which is odd. But we still want a way to test any `Object` for \"trueness\". Should `Boolean` be an abstract type that\'s mixed-in to `Object`, or a concrete type that inherits from `Object` (thus implying that non-Boolean `Object`s may exist)? I\'ve added a \"true()\" method to `Object`, which is simply a way of coercing it to a `Boolean` value (perhaps it should be called \"boolean()\"). \[+1 for mixin\]

- Should destructive operations on `MutableSequence` return the sequence? They don\'t currently, but this would be very useful. I\'ve made it so in this list\...

- Should `None` just be a very special instance of `Object`? Does the `Null` type need to exist?

- If a file is opened in binary mode, should its iterator be over bytes instead of lines? Should \"readline()\" even work on a binary file?

<!-- -->

    Comparable:
     equals (Comparable) => Boolean

    Object (Comparable):
     hash () => Integer
     # presumably for "is" we compare the ids of the two objects
     id () => Comparable
     true () => Boolean
     # we rename __str__ to "printable_rendition"
     printable () => String
     class () => Type
     implements (Type) => Boolean
     getattr (String name) => Object
     setattr (String name, Object value)
     delattr (String name) => Object

    TypeSequence (Sequence):
     # sequence of Type objects

    Type (Object):
     name () => String
     # supertypes yields list of immediate parent types (what's in __bases__)
     supertypes () => TypeSequence
     # interfaces yields flattened list of all interface types this implements
     interfaces () => TypeSequence

    Null (Object):
     # according to the language reference manual, the Null type contains only one value, "None"
     None

    Exception (Object):
     args () => Sequence

    ExceptionContext (Object):
     exception () => Exception
     traceback () => Traceback

    Boolean (Object):
     True
     False

    Orderable:
     # according to Jim Jewett, only < is currently used for ordering
     less_than (Object) => Boolean

    Numeric:
     add (Numeric) => Numeric
     subtract (Numeric) => Numeric
     product (Numeric) => Numeric
     quotient (Numeric) => Numeric
     floored_quotient (Numeric) => Numeric
     remainder (Numeric) => Numeric
     negate (Numeric) => Numeric
     absolute_value () => Numeric
     exponentiate (Numeric) => Numeric
     magnitude () => Numeric

    Integer (Object, Orderable, Numeric):
     or (Integer) => Integer
     xor (Integer) => Integer
     and (Integer) => Integer
     shift (Integer) => Integer
     invert (Integer) => Integer
     real () => Real

    Real (Object, Orderable, Numeric):
     floor () => Integer
     ceiling () => Integer

    Complex (Object, Orderable, Numeric):
     conjugate () => Complex

    Decimal (Object, Orderable, Numeric):
     TBD

    Iterable:
     # let's rename __iter__ to "iterator"
     iterator () => Iteration

    StringIterable:
     # yields an iteration of String values

    KeyValueIterable (Iterable):
     # yields an iteration of key-value pairs 

    Iteration (Object, Iterable):
     next () => Object

    # should Container be Iterable, or should that be reserved for real types, like Tuple?
    Container (Iterable):
     # we keep "len" as a mandatory method -- should we?  And why isn't it "size"?
     len () => Integer   
     contains (Object) => Boolean
     # we rename __getitem__ to "get"
     get (Object key) => Object

    MutableContainer (Container):
     # we rename __setitem__ to "add"
     # may quite easily raise KeyError when "key" is of the wrong type
     add (Object key, Object value)
     # we rename __delitem__ to "remove"
     remove (Object key)

    Set:
     is_subset (Set) => Boolean
     is_superset (Set) => Boolean
     union_with (Set) => Set
     intersection_with (Set) => Set
     difference (Set) => Set
     symmetric_difference (Set) => Set
     # should this be "multiply" to match Sequence?
     shallow_copy () => Set

    Sequence (Container):
     # this "contains" method looks for sub-sequences
     # how do we differentiate it from the Container method "contains()"?
     # should it be called "subsequence"?
     covers (Sequence) => Boolean
     # normal access via index
     # "end" defaults to start, "step" defaults to 1
     slice (Integer start, Integer end = None, Integer step = None) => Sequence
     # return self + other Sequence
     concatenate (Sequence) => Sequence
     # N shallow copies of self
     multiply (Integer) => Sequence

    SequenceOfOrderable (Sequence):
     # do "min" and "max" make sense over arbitrary sequences?  Should really only apply to sequences of "Orderable"
     min () => Orderable
     max () => Orderable

    MutableSequence (Sequence, MutableContainer):
     # append just calls "add(len(self), Object)"
     append (Object) => self
     # value at I is replaced with Object
     replace (Object, Integer position) => self
     # slice from I to J is replaced with values of Iterator
     replace (Iterable, Integer start, Integer end, Integer step = 1) => self
     extend (Object) => self
     count (Object) => Integer
     reverse ()
     index (Object, Integer start = 0, Integer end = len(self)) => Integer
     pop (Integer position = 0) => Object
     push (Object, Integer position = 0) => self
     delete (Integer start, Integer end = start, Integer step = 1) => self
     sort (Function comparison_fn = None, Function key_fn = None, Boolean reverse = False) => self

    ByteSequence (Object, Sequence):
     # should this be a MutableSequence?

    Buffer (Object, MutableSequence):
     # is this just mutable version of ByteSequence?

    String (Object, Sequence):
     TBD

    Tuple (Object, Sequence):

    List (Object, MutableSequence):

    Mapping:
     # extra version of "get" which takes a default value
     get (Object key, Object default = None) => Object
     # should delete return the deleted value?  Why not.  That removes the need for "pop".
     delete (Object key) => Object
     clear ()
     # shallow copy of mapping
     shallow_copy () => Mapping
     contains (Object key) => Boolean
     # items returns a value which is guaranteed to satisfy both the Set interface and the KeyValueIterable interface
     items () => (Set and KeyValueIterable)
     keys () => Set
     values () => Set
     # get_or_set is the current "setdefault"
     get_or_set (Object key, Object value) => Object
     update (Mapping) => self
     # alternate form of "update" takes Iterable of key-value pairs
     update (KeyValueIterable) => self
     # yet another form takes no positional parameters, and arbitrary keyword arguments
     # I need a notation for this kind of method
     update (KWDS) => self
     # do we really need fromkeys?
     fromkeys (Sequence keys, Object initial_value) => Mapping

    Dict (Object, Mapping, MutableContainer):
     # should some methods (e.g., "fromkeys") be here instead of in Mapping?

    ExecutionContext:
     enter () => ExecutionContext
     exit (ExceptionContext) => Boolean

    Stream:
     close ()

    RandomAccessStream:
     # do we really need to continue to mimic the low-level UNIX seek and tell?
     # why not use Python sequence-style indices for offset?  Positive int for relative
     # to start, negative int for relative to end, and just call tell() and add an offset
     # if  you want to seek relative to the current location, for heaven's sake.
     seek (Integer offset)
     tell () => Integer
     
    BinaryInputStream (Stream):
     # read tries to read the whole file, but may return just a part of it
     read () => ByteSequence
     read (Integer) => ByteSequence

    OutputStream (Stream):
     flush()

    BinaryOutputStream (OutputStream):
     write (ByteSequence) => Integer

    TextStream:
     encoding () => String

    TextOutputStream (OutputStream, TextStream):
     writeline (String) => Boolean
     writelines (StringIterable) => Boolean

    TextInputStream (Stream, TextStream)
     readline () => String
     readlines () => StringIterable

    DiskFile (RandomAccessStream):
     fileno () => Integer
     filename () => String
     isatty () => Boolean
     truncate (Integer size)
     mode () => String
     # It would be nice to have another method, "mimetype", which would try to guess
     # the MIME type for the file, and if it can it would return two strings, the MIME major
     # type and minor type for the file.  It would return None, None if it couldn't figure it out.
     # I'd suggest UNIX implementation just use "file", while Windows implementations
     # use registry and file extensions.
     # something like:  mimetype () => String, String
