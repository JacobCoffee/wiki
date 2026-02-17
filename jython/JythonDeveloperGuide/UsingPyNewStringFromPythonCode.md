# JythonDeveloperGuide/UsingPyNewStringFromPythonCode

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Using Py.NewString from Python Code

On some really rare cases, you may need to convert a Java String (equivalent to a Python unicode object) to a Python String, without going through the encoding process. Suppose you have the following code (useful for the purposes of this document, but not wise, since you have better ways to do this using the Python standard library):

    from java.io import File

    def absolute_path(file_name):
      return File(file_name).getAbsolutePath()

Since Jython automatically converts Java Strings to Python unicode objects, the function will return unicode. But for tricky stuff like dealing with the file system, it may be the case that bytestrings could be a better way to represent file names than unicode objects (actually, they are better on Unix, but worse on Windows). So you decide to return bytestrings if the argument passed is a bytestring:

    from java.io import File

    def absolute_path(file_name):
      if isinstance(file_name, unicode):
          File(file_name).getAbsolutePath()
      return str(File(file_name).getAbsolutePath())

It seems to work, but consider that the `str()` builtin will perform encoding when converting an unicode value. Thus, if you call this function using:

    >>> absolute_path('\xfe')

It will raise an encoding error:

    File "<stdin>", line 4, in absolute_path
    UnicodeEncodeError: 'ascii' codec can't encode character u'\xfe' in position 23: ordinal not in range(128)

Which is not what you would expect. Again, this is tricky stuff, so the alternative isn\'t perfect, and introduces the `Py.newString` hack:

    from java.io import File
    from org.python.core import Py

    def absolute_path(file_name):
      if isinstance(file_name, unicode):
          File(file_name).getAbsolutePath()
      return Py.newString(File(file_name).getAbsolutePath())

`Py.newString` will directly wrap the passed Java String as a Python bytestring, without doing any encoding. How can that work if Java strings are arrays-of-2-bytes and Python bytestrings are arrays-of-1-byte. Simple: the higher order byte is discarded. It\'s far from perfect, but works in more cases than `str()`.
