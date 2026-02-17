# CollectionsIntegration

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### Background 

This page considers the integration of java.util collections interfaces into core jython objects in going from Jython 2.1 to 2.2:

Jython 2.1 support for Java Collections integration is a one-way street. It\'s possible to make Collections object act as a PyObject but it\'s not possible to make a PyObject act as a Collection.

The integration of Collections into Jython happens through the CollectionProxy and CollectionProxy2 classes. They wrap the Collection instance with the appropriate proxy and delegate Jython calls to the Collection instance.

Going the other way fails. Take for example:

      >>> from java.util import ArrayList
      >>> a = ArrayList([1,2,3])
      Traceback (innermost last):
        File "<console>", line 1, in ?
      TypeError: java.util.ArrayList(): 1st arg can't be coerced to java.util.Collection or int

In this example the ArrayList constructor is expecting a java.util.Collection instance but since the PyList does not implement this interface the TypeError is thrown. Since the Collection framework is fundamental to Java since 1.2 the [JythonDevelopmentTeam](./JythonDevelopmentTeam.html) will address this issue. The implementation is currently being written by [ClarkUpdike](ClarkUpdike).

### Design 

There are two different approaches:

1.  Subclass the Abstract classes available in java.util for the Collection framework.

2.  Continuing subclassing PyObject with the additional work of implementing the appropriate interface.

Approach 2 offers the best integration options. Jython is primarily an implementation of Python so implementing the data structures as they are in Python takes priority over the Java implementations. In addition, the keyword and index arguments for method calls are already done. The implementation of the interfaces will need only delegate to the appropriate PyObject instance\'s method for the same functionality.

::: {}
  ------------------ ------------- -------------------
  **Jython Class**   **Extends**   **Implements**
  PySequence         PyObject      List (Collection)
  PyArray            PySequence    
  PyList             PySequence    
  PyString           PySequence    
  PyTuple            PySequence    
  PyXRange           PySequence    
  PySet              PyObject      Set
  PyDictionary       PyObject      Map
  ------------------ ------------- -------------------
:::

### Discussion 

------------------------------------------------------------------------

[ClarkUpdike](ClarkUpdike) Mar 2 2005 PM\
Reflecting further on PyArray, we may want to consider not having it implement `List`{.backtick}. When I read the docs on the jarray and array modules at the respective jython and python websites, I find the following:

- jython\'s jarray moduleis primarily for interaction with java
  - as the jython object type to hold java arrays returned by java methods

  - for java methods that require java arrays as parameters

  - ref: [http://www.jython.org/docs/jarray.html](http://www.jython.org/docs/jarray.html)
- python\'s array module is primarly for performance/efficiency
  - ref: [http://docs.python.org/lib/module-array.html](http://docs.python.org/lib/module-array.html)

Performance might not have been a concern at all for jarray. But I know I have used jarray on occasion for that very reason. In any event, I\'ll presume the two reasons for their existence are, in descending priority:

- java array integration
- performance

I\'ve been assuming that since PyArray is a sequence, it should also implement `List`{.backtick}. But the reasons not do this are:

- The use case for treating arrays as `List`{.backtick}s seems weak. Java uses the `Array.asList(Object[] a)`{.backtick} method to get a `List`{.backtick} from an array, and that is all I think is really required from a collection interoperability standpoint. Python offers the `tolist()`{.backtick} method, and PyArray should offer the same thing. Remember, `list`{.backtick} *will* implement `List`{.backtick}, so your only 9 keystrokes away ![:)](/wiki/modernized/img/smile.png ":)")

- Python arrays are list-like: append, extend, slice, etc. I think we can make PyArray do the same tricks.

- You can\'t make PyArray implement `List`{.backtick} and still retain the performance benefits, especially for primitives. You would have to choose from one of the following:

  - Element data stays as-is in PyArray (including primitive arrays, but all access through collection methods converts to and from the wrapper classes on-the-fly. This would retain the performance in jython, but would be lousy in java. If you iterated over the same list 10 times you\'d create 10x the wrapper objects (they are not stored, only the primitive values). In some cases, it would really thrash the jvm. Any kind of caching scheme would greatly increase the memory needed.

  - Element data is a java array, but primitive types are stored in object arrays (`Integer[]`{.backtick}, not `int[]`{.backtick}). This would allow the simplest integration with `List`{.backtick}, but performance would suffer.

  - Element data is a `List`{.backtick}. Wouldn\'t make any sense (but I\'m listing it for completeness), PyArray would just exist to provide a java array when needed.

Anyway, that\'s why I think PyArray should not implement list, but should just grow the python 2.2 array behavior, and provide an easy bridge to a `List`{.backtick}, via `tolist()`{.backtick}. As always, maybe I\'m missing something obvious\...

Here\'s what this design would look like:

    PySequence <--+-- PSequenceList <---- (PyList, PyTuple)
                  |
                  +-- (PyArray, PyString, PyXRange)

------------------------------------------------------------------------

[ClarkUpdike](ClarkUpdike) Mar 2 2005 AM\
This is in response to \<waiting for post to show up on sourceforge\>. It is a work in progress\--but feel free to comment. I\'ve concentrated on the impact of implementing the `List`{.backtick} interface:

\`List\`

:   `java.util.List`{.backtick}

\`list\`

:   python `list`{.backtick} type (nice to be able to say \'type\', eh?)

I\'ve been thinking on how to accomplish the \"Approach 2\" design, which is basically a delegation model, in the sense that the subject classes will continue to subclass PyObject. PySequence does not have an \"element data\" field\--which leaves the concrete classes to handle that. Here are some observations on the current 2.1 design:

::: {}
  ------------------ ------------- --------------------------------------------------- ---------------------------------------------------------------------------------------
  **Jython Class**   **Extends**   **current element data field**                      **Notes**
  PySequence         PyObject      N/A                                                 
  PyArray            PySequence    `Object data;`{.backtick}                           `data`{.backtick} is set to primitive array or array of arbitrary class
  PyList             PySequence    `protected PyObject[] list;`{.backtick}             
  PyString           PySequence    `private String string;`{.backtick}                 jython depends heavily on interning of String
  PyTuple            PySequence    \*`public PyObject[] list;`{.backtick}              `list`{.backtick} field is referenced directly by 8 classes in 14 methods
  PyXRange           PySequence    N/A                                                 int attributes start, stop, step, (useless without `PySequence.__iter__()`{.backtick}
  PySet              PyObject      `protected Hash`{.backtick}`Set _set;`{.backtick}   based on [BrianZimmer](BrianZimmer)\'s [SetsModule](SetsModule)
  PyDictionary       PyObject      `protected Hashtable table;`{.backtick}             
  ------------------ ------------- --------------------------------------------------- ---------------------------------------------------------------------------------------
:::

My current thinking is that we should add a new branch to PySequence\--let\'s call it PySequenceList. PySequence would remain as is, and PySequenceList would subclass PySequence and implement the java.util.List interface. PyString and PyXRange would subclass PySequence and PyArray, PyList, PyTuple would subclass PySequenceList. This seems appropriate because, although PyXRange and PyString technically fall under the description of `List`{.backtick}, the practicality of them as a `List`{.backtick} is nil. Am I missing something obvious here? Would anyone ever use PyXRange in java? And PyString is auto-converted to a `java.lang.String`{.backtick}.

    PySequence <--+-- PySequenceList <---- (PyArray, PyList, PyTuple)
                  |
                  +-- (PyString, PyXRange)

Not sure about PyList and PyTuple sharing an additional base class with a predefined element data field. Could do it that way, or could use delegation on a specialized element data class, or could leave it as-is (with copied code for certain methods\--although the amount of copied code will increase.

One key decision is about the element data field in PyList and PyArray. Currently, it\'s PyObject\[\]. This is efficient because it eliminates casting, but keeping it makes `List`{.backtick} implementation difficult (take a look at the source for `java.util.AbstractList`{.backtick}), and all the `System.arraycopy`{.backtick} makes `append`{.backtick} slow. If we were to switch it to an [ArrayList](./ArrayList.html), it would buy us easier collection integration, but will cost performance (who knows how much). There\'s also a \"middle-of-the-road\" approach, which is to use a specialized class to wrap a PyObject array and provide `List`{.backtick} like behavior (I have some experience with doing this). This approach might also be used with PyArray.

PyArray requires some important decisions also. The collections methods are all `Object`{.backtick} based. So anything coming or going throught these interfaces will require wrapping/boxing. If PyArray were to use an `Array`{.backtick}`List`{.backtick} and fully box everything from both java and jython, their performance (their main reason for existing?) would take a major hit. My thinking is this is not a viable option. This means there could be some difficult code to write to implement `List`{.backtick}, unless we use the specialized class mentioned above (but typed to the particular primitive array types).

Other general improvements:

- eliminate deprecated methods?

- Replace signatures to collection implementations (Vector, HashSet, HashTable) with intefaces (List, Set, Map)

- Clean up of PyXRange copies field and deprecate `repeat()`{.backtick}, `getSlice()`{.backtick}

------------------------------------------------------------------------

- [ClarkUpdike](ClarkUpdike) Feb 12 2005

  - [java.util.Collections](http://java.sun.com/j2se/1.3/docs/api/java/util/Collections.html): Is there a need to provide a jython version of this class (especially the synchronized and unmodifiable wrapper methods)? If it is not implemented and the java.util.Collections wrappers are used on new collection objects, the returned objects will only proxy for the java.util interface and will be broken in jython. There is also a PyImmutableSet in [BrianZimmer](BrianZimmer)\'s [SetsModule](SetsModule), but I don\'t think there is an immutable dictionary equivalent.

  [BrianZimmer](BrianZimmer) Feb 13 2005

  - I\'m inclinded to say *no*. Consider this code:

            List a = new ArrayList();
            a.add(1);
            a.add(2);
            List b = Collection.unmodifiableList(a);
            try {
              b.add(3);
            } catch (UnsupportedOperationException e) {
              e.printStackTrace();
            }
            a.add(3);

    Without making a copy of the collection it is always possible to mutate the delegate. The Collections methods only wrap and delegate; they do not instruct the source to be immutable. In Python, this is handled through the use of two different classes: list and tuple. Consider this code:

            a = [1,2,3,4]
            b = tuple(a)
            a.append(5)
            print a, b

    Since the tuple makes a copy of the list and does not delegate, the immutability is preserved. If an immutable Collection is really desired, copy it and make it immutable (this is really the true way in Java as well). This relieves Jython collections from concerning themselves with immutability because they will gladly offer up their contents through the standard Collection interface for the creation of a new, all Java Collection which can be used as the source.

    In the case of PyImmutableSet, it\'s part of the Python module, so it must be implemented. The relationship for mutable and immutable collections in Jython:

    ::: {}
      ------------- ----------------
      **Mutable**   **Immutable**
      PyList        PyTuple
      PySet         PyImmutableSet
      PyDict        none
      ------------- ----------------
    :::

    Synchronization should follow the same approach.
