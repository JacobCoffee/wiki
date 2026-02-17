# StreamWriter

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

As of Python2.5, `StreamWriter` wraps (contains) a stream. It defines `write` and other respective methods to \"encode\" the data and pass the result to the stream. It exposes all other methods of the stream instance.

Pseudocode of the `codecs.StreamWriter` definition:

:::: 
::: 
``` 
   1 class StreamWriter(Codec):
   2     def __init__(self, stream):
   3         ....
   4 
   5     def write(self, data):
   6         return stream.write(self.encode(data))
```
:::
::::

The `encode` method normally converts values of type `unicode` to `str`s.

Codec modules will attach the `encode` method to the class definition derived from `StreamWriter` during the initialization. An excerpt from `encodings.utf_8.StreamWriter`:

:::: 
::: 
``` 
   1 class StreamWriter(codecs.StreamWriter):
   2     encode = codecs.utf_8_encode
```
:::
::::

------------------------------------------------------------------------

See also: [StreamReader](StreamReader), [StreamReaderWriter](StreamReaderWriter), [StreamRecoder](StreamRecoder).

------------------------------------------------------------------------

[CategoryUnicode](CategoryUnicode)
