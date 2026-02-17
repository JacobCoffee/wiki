# Iterator

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

An **iterable** object is an object that implements `__iter__`, which is expected to return an **iterator** object.

An **iterator** object implements `__next__`, which is expected to return the next element of the iterable object that returned it, and to raise a `StopIteration` exception when no more elements are available.

In the simplest case, the iterable will implement `__next__` itself and return `self` in `__iter__`. However, this has its limitations and may produce unexpected results in concurrent environments (e.g. with the multiprocessing API).

You can use iterables in for loops, to construct lists with list comprehensions, or as input arguments for the `list` function.

## Example Iterator 

Here is an iterator that returns a random number of 1\'s:

:::: 
::: 
``` 
   1 import random
   2 
   3 class RandomIterable:
   4     def __iter__(self):
   5         return self
   6     def __next__(self):
   7         if random.choice(["go", "go", "stop"]) == "stop":
   8             raise StopIteration  # signals "the end"
   9         return 1
```
:::
::::

**Q:** Why is `__iter__` there, if it just returns self?

**A:** This is a very simple case. More complex iterables may very well return separate iterator objects.

**Q:** When would I need an extra iterator?

**A:** Iterators will typically need to maintain some kind of position state information (e.g., the index of the last element returned). If the iterable maintained that state itself, it would become inherently non-reentrant (meaning you could use it only one loop at a time).

:::: 
::: 
``` 
   1 for eggs in RandomIterable():
   2     print(eggs)
```
:::
::::

You can also use it in list construction:

:::: 
::: 
``` 
   1 >>> list(RandomIterable())
   2 [1]
   3 >>> list(RandomIterable())
   4 []
   5 >>> list(RandomIterable())
   6 [1, 1, 1, 1, 1]
   7 >>> list(RandomIterable())
   8 [1]
```
:::
::::

\...both of these uses require `__iter__`.

An object isn\'t iterable unless it provides `__iter__`. And for an object to be a valid iterator, it must provide `__next__`.

## Manual usage 

Although you won\'t need this in most cases, you can manually get the iterator from an iterable object by using the `iter()` function. Similary, you can manually call `__next___` using the `next()` function.

## Links 

- [PEP-234: Iterators](http://www.python.org/peps/pep-0234.html)

- [Itertools: Functions creating iterators for efficient looping](https://docs.python.org/3/library/itertools.html)

- [Functional programming and iterators](https://docs.python.org/3/howto/functional.html?highlight=iterator#functional-howto-iterators)

- [Python iterator basics (how they work + examples)](https://python.land/deep-dives/python-iterator)

See also: [Generators](Generators)
