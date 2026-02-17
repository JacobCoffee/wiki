# StreamRecoder

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The `codecs.StreamRecoder` class re-encodes data between 2 character sets. Its constructor expects the information on 2 character sets in different forms. The user should specify the internal character set as a pair of `encoder` and `decoder`. She should provide the external character set by supplying class definitions of a codec-specific `StreamReader` and `StreamWriter`.

Pseudocode of `codecs.StreamRecoder` of the Python2.5 version:

:::: 
::: 
``` 
   1 class StreamRecoder:
   2     def __init__(self, stream, e, d, class_sr, class_sw):
   3         # internal encoder, decoder^  ^external decoder, encoder
   4         self.r = class_sr(stream)
   5         self.w = class_sw(stream)
   6         ...
   7 
   8     def read(self):
   9         return self.e(self.r.read())
  10 
  11     def write(self, data):
  12         return self.w.write(self.d(data))
```
:::
::::

The `codecs` module defines a function `codecs.EncodedFile()` that will return an instance of `StreamRecoder` according to the supplied internal and external character sets.

------------------------------------------------------------------------

See also: [StreamReader](StreamReader), [StreamWriter](StreamWriter), [StreamReaderWriter](StreamReaderWriter).

------------------------------------------------------------------------

[CategoryUnicode](CategoryUnicode)
