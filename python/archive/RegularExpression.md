# RegularExpression

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

![](http://wiki.python.org/moin/RegularExpression?action=AttachFile&do=get&target=regex_characters.png "http://wiki.python.org/moin/RegularExpression?action=AttachFile&do=get&target=regex_characters.png")

flags when compiling:

![](http://taoriver.net/img/for_pi/regex_flags.png "http://taoriver.net/img/for_pi/regex_flags.png")

(All images PD, released by author, [LionKimbro](LionKimbro).)

## Searching & Matching 

You can *search* or *match.*

- *search* \-- find something *anywhere* in the string, and return it

- *match* \-- find something *from the beginning* of the string, and return it

You can also *split* on a pattern.

For example:

:::: 
::: 
``` 
   1 import re
   2 split_up = re.split(r"(\(\([^)]+\)\))",
   3                     "This is a ((test)) of the ((emergency broadcasting station.))")
```
:::
::::

\...which produces:

    ["This is a ", "((test))", " of the ", "((emergency broadcasting station.))" ]

## Compiling 

If you use a regex a lot, *compile it* first.

Consider:

:::: 
::: 
``` 
   1 import re
   2 match_obj=re.match("<(.*?)>(.*?)</(.*?)>", "<h1>robot</h1>")
   3 print mo.groups()
```
:::
::::

\...which outputs: `('h1', 'robot', 'h1')`

If you were going to do that match a lot, you could compile it, like so:

:::: 
::: 
``` 
   1 import re
   2 match_re=re.compile("<(.*?)>(.*?)</(.*?)>")
   3 match_obj=match_re.match("<h1>robot</h1>")
   4 print match_obj.groups()
```
:::
::::

\...which yields the same result.

The relative speed of compiled versus non-compiled patterns can be shown using the timeit module:

    python -m timeit -s 'import re' \
       'match_obj = re.match("<(.*?)>(.*?)</(.*?)>", "<h1>robot</h1>")'
    1000000 loops, best of 3: 1.35 usec per loop

    python -m timeit -s 'import re ; match_re = re.compile("<(.*?)>(.*?)</(.*?)>")' \
       'match_obj = match_re.match("<h1>robot</h1>")'
    1000000 loops, best of 3: 0.572 usec per loop

The above numbers were produced on an Intel Core i7 3770k running Python 2.7.6 (circa 2014). You should run the above commands on your Python version and specific hardware, and use patterns that represent your problem domain, for more representative results.

## See Also 

- [Regular expression operations](https://docs.python.org/3/library/re.html) \-- [PythonLibraryReference](PythonLibraryReference)

- [Regular Expression Syntax](https://docs.python.org/3/library/re.html#regular-expression-syntax) \-- [PythonLibraryReference](PythonLibraryReference)

- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html) - excellent Python-based regular expression tutorial, by [A.M. Kuchling.](http://www.amk.ca/)

- [Regex in a Nutshell](https://web.archive.org/web/20190322024325/https://bitcetera.com/en/techblog/2008/04/01/regex-in-a-nutshell/) cheat sheet

- [RegexBuddy](http://www.regexbuddy.com/python.html) - Handy tool to create and test Python regular expressions

- [Summary of Regular Expression Patterns](http://gnosis.cx/TPiP/regex_patterns.gif) \-- by [DavidMertz](DavidMertz)

- [redemo tool](http://pythoncard.sourceforge.net/samples/redemo.html) \-- ships with Python (C:\\\\Python24\\Tools\\Scripts\\redemo.py), indispensible when trying out regular expressions; ships with [PythonCard](./PythonCard.html) as well

- [periodic table of PERL operators](http://www.ozonehouse.com/mark/blog/code/PeriodicTable.pdf) \-- for those who like visualization

- [Regular Expression Starter](http://thepythonguru.com/python-regular-expression/) \-- A simple guide for beginners

- SVG source: [1,](http://taoriver.net/img/for_pi/regex_characters.svg) [2.](http://taoriver.net/img/for_pi/regex_flags.svg)

## Discussion 

### Requests 

- documentation on using re with [Unicode](../archive/Unicode) ..?

### Problem? 

The following feature does not seems to work in python:

For example, the ICU regular expression provides the following patterns:

- \\N{UNICODE CHARACTER NAME} Correspond au caractère nommé
- \\p{UNICODE PROPERTY NAME} Correspond au carctère doté de la propriété Unicode spécifiée.
- \\P{UNICODE PROPERTY NAME} Correspond au carctère non doté de la propriété Unicode spécifiée.
- \\s Correspond à un caractère séparateur. un séparateur est définit comme \[\\t\\n\\f\\r\\p{Z}\].
- \\uhhhh Correspond à un caractère dont la valeur hexa est hhhh.
- \\Uhhhhhhhh Correspond à un caractère dont la valeur hexa est hhhhhhhh. Exactement huit chiffres héxa doivent être fournis, même si le code point unicode le plus grand est \\U0010ffff.

\-- anonymous

I don\'t understand the problem. \-- [LionKimbro](LionKimbro) 2006-03-25 16:31:35

### Visualization 

- *I like the Venn diagram in this image. However, one part of the image is confusing. Where it refers to python strings, and \"regex strings\" (which are actually Python \"raw\" strings) and something called \"match strings\" \... what are these \"match strings. \-- JimD 2004-12-30 20:03:54*

The image isn\'t meant to be explanatory, it is meant to be reference and refreshing material.

That said: The \"match string\" is the final product of either of the two above expressions. It is what the above two expressions will literally match. If you have a better phrase, or would like to correct \"raw\" to \"regex,\" feel free to download the SVG, edit the text, place an image on the web, and link it from here. (The damn [LongImageIncorporationProcess](http://visual.wiki.taoriver.net/moin.cgi/LongImageIncorporationProcess) strikes again.) I may eventually get around to it myself one day, but it seems there are higher priorities, and the diagram is \"good enough.\"

That said, I appreciate the correction. \-- [LionKimbro](LionKimbro) 2005-01-01 00:22:14

### Image Hosting 

At the top of this page were two images/scehmes about re. Is it possible to redraw them here somehow? That server is not working, maybe someone has them dowloaded locally. Thanks a lot. \-- [PavelKosina](./PavelKosina.html)

I\'ve uploaded one as an attachment, still need to upload the other\... And, the source\...

(Anyone can do this, though, when the computers are online.)

\-- [LionKimbro](LionKimbro) 2006-03-25 16:31:35

------------------------------------------------------------------------

[CategoryDocumentation](CategoryDocumentation)
