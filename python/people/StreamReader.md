# StreamReader

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

As of Python2.5, `StreamReader` wraps (contains) a stream. It defines `read` and other respective methods to read the data from the stream and \"decode\" them. The class exposes all other methods of the stream instance.

Pseudocode of the `codecs.StreamReader` definition:

:::: 
::: 
``` 
   1 class StreamReader(Codec):
   2     def __init__(self, stream):
   3         ....
   4 
   5     def read(self):
   6         return self.decode(stream.read())
```
:::
::::

The `decode` method normally converts values of type `str` to `unicode`.

Codec modules will attach the `decode` method to the class definition derived from `StreamReader` during the initialization. An excerpt from `encodings.utf_8.StreamReader`:

:::: 
::: 
``` 
   1 class StreamReader(codecs.StreamReader):
   2     decode = codecs.utf_8_decode
```
:::
::::

------------------------------------------------------------------------

See also: [StreamWriter](StreamWriter), [StreamReaderWriter](StreamReaderWriter), [StreamRecoder](StreamRecoder).

------------------------------------------------------------------------

[CategoryUnicode](CategoryUnicode)
