# Unicode

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Resources to help you learn how to handle Unicode in your Python programs:

## General Unicode Resources 

- [The Absolute Minimum Every Software Developer Must Know about Unicode](http://www.joelonsoftware.com/articles/Unicode.html) - short intro to Unicode

- [Unicode](http://www.wikipedia.com/wiki/Unicode "WikiPedia") \-- Wikipedia unicode entry

## Python-Specific Resources 

### Standard Reference 

Search the Python reference for:

- unichr builtin

- string handling - example: `u'Hello\u0020World !'`{.backtick}

- [unicodedata](http://docs.python.org/lib/module-unicodedata.html) module

- regular expressions - see the `(?u)`{.backtick} flag, and the `re.UNICODE`{.backtick} constant

- exceptions - `UnicodeEncodeError`{.backtick}

### Tutorials 

- [End to End Unicode Web Applications in Python](http://dalchemy.com/opensource/unicodedoc/)

- [Dive Into Python: Unicode](http://diveintopython.org/xml_processing/unicode.html)

- [Python and Unicode](http://www.egenix.com/files/python/Unicode-EPC2002-Talk.pdf) (pdf talk) He also has a [brief tutorial](http://www.reportlab.com/i18n/python_unicode_tutorial.html).

- [Unicode for Programmers](http://www.jorendorff.com/articles/unicode/index.html) - Java and Python info

- [Python Unicode Objects](http://effbot.org/zone/unicode-objects.htm) - brief notes

### Sample Code 

- [HTMLifying and UnHTMLifying](http://www.intertwingly.net/blog/1581.html) - see atomef.py

### Pitfalls 

- [StrIsNotAString](StrIsNotAString)

- [PrintFails](PrintFails)

- [ShellRedirectionFails](ShellRedirectionFails)

- [UnicodeEncodeError](UnicodeEncodeError)

- [UnicodeDecodeError](UnicodeDecodeError)

- [DefaultEncoding](DefaultEncoding)

- [The standard encodings list](http://docs.python.org/lib/standard-encodings.html) is for the current version of python. [GB2312](http://en.wikipedia.org/wiki/GB2312) (PRC Chinese,) for example, is in Python2.4, but [not in Python2.2, nor Python2.3.](http://www.xahlee.org/perl-python/charset_encoding.html)

### Supported Encodings 

There is a [list of standard encodings in the Python documentation.](http://docs.python.org/lib/standard-encodings.html)

Encodings can be registered at runtime, as well, with the codecs module.

Python2.4 supports many codecs that 2.2 and 2.3 do not, including Chinese bg2312.

Encodings are specified in files found in a directory called \"encodings\"; one way to find the encodings with your Python distribution is to check the contents of this directory:

    >>> import encodings, os
    >>> [n for n in os.listdir(os.path.dirname(encodings.__file__))
    ...     if n[0] != '_' and n.endswith('.py')]
    ['aliases.py', 'ascii.py', 'base64_codec.py', 'charmap.py', 'cp037.py', ...]

Another is to list aliases from the encodings module.

    >>> import encodings
    >>> from encodings import aliases
    >>> aliases.aliases
    {'base64': 'base64_codec', 'us_ascii': 'ascii', ...}

Contributors: [LionKimbro](LionKimbro), [FredDrake](FredDrake), [JürgenHermann](./J(c3bc)rgenHermann.html).

### \"The Truth about Unicode in Python\" 

[The Truth about Unicode in Python](http://www.cmlenz.net/archives/2008/07/the-truth-about-unicode-in-python)

## Discussion 

Here\'s a conversation that I had on [CommunityWiki;](http://communitywiki.org/) I\'d like to bring the main ideas into here.

### Conversation between Lion and Bayle 

That looks like 32-bits per character, so I\'d say it\'s some form of little-endian utf-32.

And for some strange reason, Python only comes with \"utf-8\" and \"utf-16\" as valid \"decode\" values.

You can:

:::: 
::: 
``` 
   1 >>> bytes = "H\x00i\x00\n\x00"
   2 >>> unistring = bytes.decode('utf-16')
   3 >>> print unistring
   4 u'Hi\n'
```
:::
::::

You can do that for either \"utf-8\" or \"utf-16.\" But for some reason, I can\'t say \"utf-32\" or \"utf-32LE\" (LE=little endian). I have no idea why. I also don\'t know how it is that my Python programs are producing UTF-32 for you..!

I\'ve been wanting to diagram how Python unicode works, like how I diagrammed it\'s time use, and regex use.

Basically, \"encode\" is meant to be called *from* unicode data, and \"decode\" is meant to be called *from* bytes data. Continuing from above:

:::: 
::: 
``` 
   1 >>> bytes
   2 'H\x00i\x00\n\x00'
   3 >>> unistring = bytes.decode('utf-16')
   4 >>> unistring
   5 u'Hi\n'
   6 >>> unistring.encode('utf-8')
   7 'Hi\n'
   8 >>> unistring.encode('utf-16')
   9 '\xff\xfeH\x00i\x00\n\x00'
  10 >>> unistring.encode('utf-32')
  11 Traceback (most recent call last):
  12   File "<stdin>", line 1, in ?
  13 LookupError: unknown encoding: utf-32
```
:::
::::

I\'m guessing that the \"\\xff\" at the beginning of the utf-16 encoding is a byte-order marker, saying \"this is little endian.\"

I learned about unicode stuff about 2-3 weeks ago. I kept notes about what I thought were the largest mental misconceptions, and what were the most revealing ways of thinking about it. Sadly, I\'ve forgotten about all that. (Should\'a documented it in the wiki!)

In Python, the data in a unicode or byte string is exactly the same. The difference is only in how Python treats and presents the data. I found it super-helpful to *not* think about what the console said, or work with the console, because *the console lies.* That is, the characters go through conversions even being printed to the screen: Your console has an understanding of encoding, and your fonts have an understanding of encoding, and I had a lot of difficulty seperating it out.

I had a lot easier time thinking about the concepts, instead of the concrete representations. (Which is opposite my usual course of thinking.)

\"Decoded,\" to Python\'s mind, is data being treated as unicode data. \"Encoded,\" to Python\'s mind, is data being treated as bytes. The data isn\'t actually changing form, at all. It\'s just the *treatment* of the same data that is being changed. But there is *no actual conversion taking place.*

So, you only ever run \"decode\" on a byte string. (Another thing: Don\'t think of native Python strings as \"strings.\" Think of them as \"bytes.\" And indeed: In the new Python 3.0, they\'re calling it just that: strings are called \"bytes\" in Python3, and unicode strings are called just \"strings\" in Python3.)

So you can *decode* bytes, and *encode* unicode strings.

Don\'t think about decoding unicode strings, and don\'t think about encoding bytes. The bytes are already coded. Only unicode strings live in pure, abstract, heavenly, platonic form. There is no code there, only perfect clarity. (At least, that\'s how Python makes it seem for you.)

Again, sadly, I have no idea how to get from UTF-32 to Python unicode. I don\'t see the path. I saw something somewhere about being able to compile something in to your Python.

That said, if I\'m actually serving UTF-32 to you somehow,\... \...then there\'s probably a way I just don\'t know.

### (Discussion continued) 

On side-notes, I think the diagrams I\'ve posted for [WorkingWithTime](WorkingWithTime) and [RegularExpressions](./RegularExpressions.html) were eaten up in the transition to [MoinMoin](MoinMoin) 1.3; I\'ll repost them soon, after I get [my own wiki](http://wiki.taoriver.net/) upgraded to 1.3.

\-- [LionKimbro](LionKimbro) 2005-02-06 02:56:28

------------------------------------------------------------------------

[CategoryUnicode](CategoryUnicode)
