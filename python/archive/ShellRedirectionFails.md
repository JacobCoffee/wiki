# ShellRedirectionFails

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

If you try to redirect printing of non-ASCII unicode strings into a file, Python doesn\'t know how to encode non-ascii characters because there are many text encodings in use across the world. You need to wrap standard output with an encoder that will convert unicode characters into encoding of your choice. For example, to convert characters into utf-8 encoding use:

:::: 
::: 
``` 
   1 import codecs
   2 sys.stdout = codecs.getwriter("utf-8")(sys.__stdout__)
```
:::
::::

Of course, this code is not portable since most users in the world don\'t use UTF-8 encoding for files. The `locale`{.backtick} module provides the function `getpreferredencoding()`{.backtick} that will try to guess what is the preferred encoding for text files. There are also other ways to ask user for encoding of text files: command line options of your script, parameters stored in a configuration file, and GUI dialogs are common examples.

### References 

- [locale module documentation](http://docs.python.org/lib/module-locale.html)
