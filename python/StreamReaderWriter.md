# StreamReaderWriter

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The Python2.5\'s `codecs.StreamReaderWriter` combines [StreamReader](StreamReader) and [StreamWriter](StreamWriter). The wrapper will read narrow `str` strings from the underlying stream and decode them to `unicode` strings. On writing `unicode` data to the wrapper, it will encode them to narrow `str` strings.

The user of the wrapper should specify character sets by supplying class definitions for the respective stream reader and writer.

Pseudocode:

:::: 
::: 
``` 
   1 class StreamReaderWriter:
   2     def __init__(self, stream, class_sr, class_sw):
   3         self.r = class_sr(stream)
   4         self.w = class_sw(stream)
   5 
   6     def read(self):
   7         return self.r.read()
   8 
   9     def write(self, data):
  10         return self.w.write(data)
```
:::
::::

The `codecs` module defines a function `codecs.open(name, encoding)` that returns an instance of `StreamReaderWriter` configured with the supplied encoding.

------------------------------------------------------------------------

See also: [StreamReader](StreamReader), [StreamWriter](StreamWriter), [StreamRecoder](StreamRecoder).

------------------------------------------------------------------------

[CategoryUnicode](CategoryUnicode)
