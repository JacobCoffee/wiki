# DogriLanguage

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Describe Dogri डोगरी Language and include links to Python information in डोगरी Language here.

ISO 639-2 Code: doi

[1SEP09 Ideally, all the language pages should be like the Polish or Turkish pages - all native language, only the necessary English. ]

There are some groundrules, some laid down by the site admins, some my suggestions:

1\) Pages must be named in ASCII and English ([PolishLanguage](PolishLanguage))

2\) Pages must have an explanation in English at the top (Links to Python information in \<language X\>)

3\) (my suggestion) We probably want to limit invites to edit the pages to people we know well, or Pythonistas with a track record. Hopefully this is inclusive enough without opening the site up to a spam flood and vandalismfest.

Where these pages really need help:

1\) check links, remove broken ones.

2\) add new links that are quality Python information and active.

3\) some care for languages that have next to nothing, but do have people in the Python community - even a link to the Wikipedia page for Python, in that language, is a start (Some are pretty complete and of high quality - the Russian language Wikipedia page for Python, for instance, packs a lot in).

**डोगरी**

Words for code snippet from [Wikipedia](http://en.wikipedia.org/wiki/Dogri_language)

Right to left script for Dogri not rendering in idle - need to update.

:::: 
::: 
``` 
   1 # -*- coding: utf-8 -*-
   2 # python 3.0 or python 3.1
   3 
   4 # trouble getting alternate right to left
   5 # script to render in idle
   6 डोगरी = {'Yes':'ऑह',
   7         'With':'कन्ने',
   8          'Shoes':'नुक्के',
   9          'Door':'पित्त',
  10          'What':'के',
  11          'Why':'की',
  12          'Watermelon':'अद्वाना',
  13          'World':'दुनिया'}
  14 
  15 for english in डोगरी:
  16     print(chr(34) + english + chr(34) + ' in English is ' +
  17           डोगरी[english] + ' in Dogri.')
```
:::
::::

------------------------------------------------------------------------

[CategoryLanguage](CategoryLanguage) [CategoryUnicode](CategoryUnicode) [CategoryPythonIndia](CategoryPythonIndia)
