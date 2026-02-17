# boost.python/RelatedProjects

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Weave 

From [DavidAbrahams](./DavidAbrahams.html):

Boost.Python is designed with the idea in mind that users never touch a PyObject\*.

Boost.Python depends on quite a few of the other boost libraries (possibly a few others):

- type_traits
- bind
- function
- mpl
- smart_ptr

IIUC, [weave](weave) can be used for embedding nontrivial C++ code, if you\'re willing to stick it all inside one function body. Furthermore, tools like weave.blitz() can make an enormous difference by compiling an entire C++ expression template corresponding to an arbitrarily complicated Python expression. Surely that\'s nontrivial. It\'s definitely *cool*. I think weave offers enormous power to the person who\'s programming mostly in Python.
