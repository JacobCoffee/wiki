# ImplementSequenceType

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Information that might be useful while implementing or maintaining a sequence type, based on things I discovered while trying to implement `bytearray`.

# Sequence Types 

Jython provides some apparatus to support the implementation of sequence types.

## Helper class SequenceIndexDelegate 

The range of things that can appear in Python as the \"index\" of a sequence type is a lot broader than in most languages. Consider

    >>> a=list(range(10))
    >>> a
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> del a[2:7:3]
    >>> a
    [0, 1, 3, 4, 6, 7, 8, 9]
    >>> b=list(range(20))
    >>> b[30:-15:-3]
    [19, 16, 13, 10, 7]
    >>> b[30:-15:-3] = "abcde"
    >>> b
    [0, 1, 2, 3, 4, 5, 6, 'e', 8, 9, 'd', 11, 12, 'c', 14, 15, 'b', 17, 18, 'a']

If you were the implementer of `list`, your implementation of `__delitem__(self,key)` would have to support not only a simple integer key, but a slice representing 2:7:3. Similarly, `__getitem__` must synthesise a return list picked according to the slice, and `__setitem__` must be able to assign these elements from a sequence. All this while observing the rules of extended slicing.

Jython provides a useful abstract class `org.python.core.SequenceIndexDelegate` that recognises whether the key was a simple integer or a slice, deals with illegal types and range checks, and in the case of a slice, converts it into indexes you can use safely in a `for` loop where you do the actual operation. To connect these goodies into your implementation, create a concrete inner class extending `SequenceIndexDelegate` by overriding the required 8 methods with call-back methods into your own implementation:

:::: 
::: 
``` 
   1     public abstract int len();
   2     public abstract PyObject getItem(int idx);
   3     public abstract void setItem(int idx, PyObject value);
   4     public abstract void delItem(int idx);
   5     public abstract PyObject getSlice(int start, int stop, int step);
   6     public abstract void setSlice(int start, int stop, int step, PyObject value);
   7     public abstract void delItems(int start, int stop);
   8     public abstract String getTypeName();
```
:::
::::

Your implementations of the standard API, such as `__setitem__`, can delegate almost immediately to corresponding methods of this inner class, with all their arguments uninspected. The inner class will then call the right methods from these 8 to handle the actual work. There\'s still plenty for your code to deal with, but you can do it knowing the arguments are of well-defined type and have safe values.

## Base class PySequence 

Jython provides further help in the form of `org.python.core.PySequence`, with the intention that an implementer of sequence types extend the class. This has been used as a base for Python types `list` and `array.array`, and soon `bytearray`.

`PySequence` uses the delegaion technique discussed in the previous section, however it cannot do all the work. Although it makes the delgate concrete, the implementations of most of the 8 callback methods themselves depend on abstract methods within `PySequence`. Here is an extract:

:::: 
::: 
``` 
   1     protected final SequenceIndexDelegate delegator = new SequenceIndexDelegate() {
   2 
   3 ...
   4         @Override
   5         public void setItem(int idx, PyObject value) {
   6             pyset(idx, value);
   7         }
   8 
   9         @Override
  10         public void setSlice(int start, int stop, int step, PyObject value) {
  11             setslice(start, stop, step, value);
  12         }
  13 ...
  14     };
```
:::
::::

The methods `pyset` and `setSlice` referenced here are amongst 7 methods that extensions implementing sequence types are expected to override:

:::: 
::: 
``` 
   1     // These methods must be defined for any sequence
   2     protected abstract PyObject pyget(int index);
   3     protected abstract PyObject getslice(int start, int stop, int step);
   4     protected abstract PyObject repeat(int count);
   5 
   6     // These methods only apply to mutable sequences
   7     protected void pyset(int index, PyObject value) {
   8         throw Py.TypeError("can't assign to immutable object");
   9     }
  10     protected void setslice(int start, int stop, int step, PyObject value) {
  11         throw Py.TypeError(String.format("'%s' object does not support item assignment",
  12                                          getType().fastGetName()));
  13     }
  14     protected void del(int i) {
  15         throw Py.TypeError(String.format("'%s' object does not support item deletion",
  16                                          getType().fastGetName()));
  17     }
  18     protected void delRange(int start, int stop) {
  19         throw Py.TypeError(String.format("'%s' object does not support item deletion",
  20                                          getType().fastGetName()));
  21     }
```
:::
::::

You can see that read-access methods are abstract, but methods that change content are provided with implementations that will throw an error if not overriden. These are ready for use by immutable sequence types.

`PySequence` also provides actual implementations for methods `__setitem__` in terms of the delegate:

:::: 
::: 
``` 
   1     // Java API
   2     @Override
   3     public void __setitem__(int index, PyObject value) {
   4         delegator.checkIdxAndSetItem(index, value);
   5     }
   6     @Override
   7     public void __setitem__(PyObject index, PyObject value) {
   8         seq___setitem__(index, value);
   9     }
  10     // Python API
  11     final void seq___setitem__(PyObject index, PyObject value) {
  12         delegator.checkIdxAndSetItem(index, value);
  13     }
```
:::
::::

Although this last method `PySequence.seq__setitem__(PyObject, PyObject)` is essentially the entrypoint we need from Python, it cannot be exposed directly as (say) `list.__setitem(self,key,value)`: it has the wrong name and is not directly in the implementing class. So in `PyList` we find:

:::: 
::: 
``` 
   1     @ExposedMethod(doc = BuiltinDocs.list___setitem___doc)
   2     final synchronized void list___setitem__(PyObject o, PyObject def) {
   3         seq___setitem__(o, def);
   4     }
```
:::
::::

There is no need, however, to wrap the Java API method `__setitem__(int, PyObject)` any further. The inherited version is just fine.

When Python encounters

    b=list(range(20))
    b[30:-15:-3] = "abcde"

it will invoke something like

    b.list___setitem__(new PySlice(30,-25,-3), new PyString("abcde"))

The sequence of method calls will then be like:

    b.list___setitem__(PySlice(30,-25,-3), PyString("abcde")) ->
    b.seq___setitem__(PySlice(30,-25,-3), PyString("abcde")) ->
    b.delegator.checkIdxAndSetItem(PySlice(30,-25,-3), PyString("abcde")) ->
    b.delegator.checkIdxAndSetSlice(PySlice(30,-25,-3), PyString("abcde")) ->
    b.delegator.setSlice(19, -1, -3, PyString("abcde")) ->
    b.setslice(19, -1, -3, PyString("abcde"))

Notice that the slice, ostensibly a bad fit for a length 20 sequence, was transformed into three integers that can validly index the sequence as:

:::: 
::: 
``` 
   1         for (int i=19; i>-1; i+=-3)
   2                 b.myList.get(i);
```
:::
::::

which is both the correct meaning for the slice and runs no risk of access out of bounds. In this example the `step` of the slice was negative, and so the loop counts down. The final value of the loop is not used for access.

The case `step==1` means a contiguous slice `[start:stop]`. Implementations usually deal with this as a special case either because it has different semantics (e.g. in `__setitem__` or `__delitem___`), or because contiguous elements can be processed with an efficient block operation. A helper function `PySequence.sliceLength(start, stop, step)` exists to make the processing loop easier to get right. A typical idiom is:

:::: 
::: 
``` 
   1     if (step == 1) {
   2         // Do something efficient with block start...stop-1
   3     } else {
   4         int n = sliceLength(start, stop, step);
   5         for (int i = start, j = 0; j < n; i += step, j++) {
   6             // Perform jth operation with element i
   7         }
   8     }
```
:::
::::
