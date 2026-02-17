# PrintFails

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Issue 

If you try to print a unicode string to console and get a message like this one:

    >>> print u"\u03A9"
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
      File "C:\Python24\lib\encodings\cp866.py", line 18, in encode
        return codecs.charmap_encode(input,errors,encoding_map)
    UnicodeEncodeError: 'charmap' codec can't encode character u'\u1234' in position
     0: character maps to <undefined>

This means that the python console app can\'t write the given character to the console\'s encoding.

More specifically, the python console app created a \_io.TextIOWrapperd instance with an encoding that cannot represent the given character.

**sys.stdout** \--\> **\_io.TextIOWrapperd** \--\> (your console)

To understand it more clearly, look at:

- sys.stdout

- sys.stdout.encoding \-- ![/!\\](/wiki/europython/img/alert.png "/!\") This seems to work on one of my computers (Vista,) but not on another of my computers (XP.) I haven\'t looked into differences of situation in detail.

## Windows 

By default, the console in Microsoft Windows only displays 256 characters (cp437, of [\"Code page 437\"](http://en.wikipedia.org/wiki/Code_page_437), the original IBM-PC 1981 extended ASCII character set.)

If you try to print an unprintable character you will get `UnicodeEncodeError`.

Setting the PYTHONIOENCODING environment variable as described above can be used to suppress the error messages. Setting to \"utf-8\" is not recommended as this produces an inaccurate, garbled representation of the output to the console. For best results, use your console\'s correct default codepage and a suitable error handler other than \"strict\".

## Various UNIX consoles 

There is no standard way to query UNIX console for find out what characters it supports but fortunately there is a way to find out what characters are considered to be printable. Locale category LC_CTYPE defines what characters are printable. To find out its value type at python prompt:

:::: 
::: 
``` 
   1 >>> import locale
   2 >>> locale.getdefaultlocale()[1]
   3 'utf-8'
```
:::
::::

If you got any other value you won\'t be able to print all unicode characters. As soon as you try to print a unprintable character you will get `UnicodeEncodeError`. To fix this situation you need to set the environment variable LANG to one of supported by your system unicode locales. To get the full list of locales use command \"locale -a\", look for locales that end with string \".utf-8\". If you have set LANG variable but now instead of `UnicodeEncodeError` you see garbage on your screen you need to set up your terminal to use font unicode font. Consult terminal manual on how to do it.

## print, write and Unicode in pre-3.0 Python 

Because file operations are 8-bit clean, reading data from the original `stdin` will return `str`\'s containing data in the input character set. Writing these `str`\'s to `stdout` without any codecs will result in the output identical to the input.

      $ echo $LANG
      en_CA.utf8

      $ python -c 'import sys; line = sys.stdin.readline(); print type(line), len(line); print line;'
      [TYPING: абв ENTER]
      <type 'str'> 7
      абв

      $ echo "абв" | python -c 'import sys; line = sys.stdin.readline(); print type(line), len(line); print line;'
      <type 'str'> 7
      абв
      $ echo "абв" | python -c 'import sys; line = sys.stdin.readline(); print type(line), len(line); print line;' | cat
      <type 'str'> 7
      абв

Since programmers need to display `unicode` strings, the designers of the `print` statement built the required transformation into it.

- When Python finds its output attached to a terminal, it sets the `sys.stdout.encoding` attribute to the terminal\'s encoding. The `print` statement\'s handler will automatically encode `unicode` arguments into `str` output.

<!-- -->

        $ python -c 'import sys; print sys.stdout.encoding; print u"\u0411\n"'
        UTF-8
        Б

- When Python does not detect the desired character set of the output, it sets `sys.stdout.encoding` to None, and `print` will invoke the \"ascii\" codec.

<!-- -->

        $ python -c 'import sys; print sys.stdout.encoding; print u"\u0411\n"' 2>&1 | cat
        None
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
        UnicodeEncodeError: 'ascii' codec can't encode character u'\u0411' in position 0: ordinal not in range(128)

I (IL) understand the implementation of Python2.5\'s `print` statement as follows.

:::: 
::: 
``` 
   1     # At Python startup.
   2     sys.stdout.encoding = tty_enc
   3     if tty_enc is not None:
   4       class_tty_enc_sw = codecs.getstreamwriter(tty_enc)
   5     else
   6       class_tty_enc_sw = None
   7 
   8     def print(*args):
   9       if class_tty_enc_sw is not None:
  10         eout = class_tty_enc_sw(sys.stdout)
  11       else:
  12         eout = None
  13       for arg in args:
  14          sarg = stringify_to_str_or_unicode(arg)
  15          if type(sarg) == str or eout is None:
  16            # Avoid coercion to unicode in eout.write().
  17            sys.stdout.write(sarg)
  18          else:
  19            eout.write(sarg)
```
:::
::::

- At startup, Python will detect the encoding of the standard output and, probably, store the respective [StreamWriter](StreamWriter) class definition. The `print` statement stringifies all its arguments to narrow `str` and wide `unicode` strings based on the width of the original arguments. Then `print` passes narrow strings to `sys.stdout` directly and wide strings to the instance of [StreamWriter](StreamWriter) wrapped around `sys.stdout`.

- If the user does not replace `sys.stdout` as shown below and Python does not detect an output encoding, the `write` method will coerce `unicode` values to `str` by invoking the ASCII codec ([DefaultEncoding](DefaultEncoding)).

Python file\'s `write` and `read` methods do not invoke codecs internally. Python2.5\'s file `open` built-in sets the `.encoding` attribute of the resulting instance to `None`.

Wrapping `sys.stdout` into an instance of [StreamWriter](StreamWriter) will allow writing `unicode` data with `sys.stdout.write()` and `print`.

      $ python -c 'import sys, codecs, locale; print sys.stdout.encoding; \
        sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout); \
        line = u"\u0411\n"; print type(line), len(line); \
        sys.stdout.write(line); print line'
      UTF-8
      <type 'unicode'> 2
      Б
      Б

      $ python -c 'import sys, codecs, locale; print sys.stdout.encoding; \
        sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout); \
        line = u"\u0411\n"; print type(line), len(line); \
        sys.stdout.write(line); print line' | cat
      None
      <type 'unicode'> 2
      Б
      Б

The `write` call executes `StreamWriter.write` which in turn invokes codec-specific `encode` and passes the result to the underlying file. It appears that the `print` statement will not fail due to the argument type coercion when `sys.stdout` is wrapped. My (IL\'s) understanding of `print`\'s implementation above agrees with that.

## read and Unicode in pre-3.0 Python 

I (IL) believe reading from `stdin` does not involve coercion at all because the existing ways to read from `stdin` such as `"for line in sys.stdin"` do not convey the expected type of the returned value to the `stdin` handler. A function that would complement the `print` statement might look like this:

      line = typed_read(unicode)   # Generally, a list of input data types along with an optional parsing format line.

`print` statement encodes `unicode` strings to `str` strings. One can complement this with decoding of `str` input data into `unicode` strings in `sys.stdin.read/readline`. For this, we will wrap `sys.stdin` into a [StreamReader](StreamReader) instance:

      $ python -c 'import sys, codecs, locale; \
        print sys.stdin.encoding; \
        sys.stdin = codecs.getreader(locale.getpreferredencoding())(sys.stdin); \
        line = sys.stdin.readline(); print type(line), len(line)' 2>&1
      UTF-8
      [TYPING: абв ENTER]
      <type 'unicode'> 4
      $ echo "абв" | python -c 'import sys, codecs, locale; \
        print sys.stdin.encoding; \
        sys.stdin = codecs.getreader(locale.getpreferredencoding())(sys.stdin); \
        line = sys.stdin.readline(); print type(line), len(line)'
      None
      <type 'unicode'> 4

See also: [Unicode](Unicode)

------------------------------------------------------------------------

[CategoryUnicode](CategoryUnicode)
