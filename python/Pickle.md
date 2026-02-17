# Pickle

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# What is Pickle? 

[http://docs.python.org/library/pickle.html](http://docs.python.org/library/pickle.html)

# Should I use Pickle? 

Of course not.

- It is insecure. Untrusted pickles can do arbitrary things. For example, this pickle executes arbitrary Python expressions: `pickle.loads("c__builtin__\neval\n(c__builtin__\nraw_input\n(S'py> '\ntRtR.")`{.backtick}

- It is Python-only: pickles cannot be loaded in any other programming language / environment.

- It is schemaless and opaque. See: [http://bpaste.net/show/d0UZUSsAHtekA0pDiQzu/](http://bpaste.net/show/d0UZUSsAHtekA0pDiQzu/)

# Alternatives 

- The json module ([http://docs.python.org/library/json.html](http://docs.python.org/library/json.html)) can handle dicts, lists, ints, floats, strings, booleans, and None. It cannot handle reference cycles, however. (pickle can.)

- PyYAML ([http://pyyaml.org/](http://pyyaml.org/)) can handle everything json can, as well as having comments inside source data, and reference cycles. However, it defaults to an unsafe pickle-like loader.
