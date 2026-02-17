# TamilLanguage

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Links to Python related information in Tamil

ISO 639-1 Code: ta

[1SEP09 Ideally, all the language pages should be like the Polish or Turkish pages - all native language, only the necessary English. ]

There are some groundrules, some laid down by the site admins, some my suggestions:

1\) Pages must be named in ASCII and English ([PolishLanguage](PolishLanguage))

2\) Pages must have an explanation in English at the top (Links to Python information in \<language X\>)

3\) (my suggestion) We probably want to limit invites to edit the pages to people we know well, or Pythonistas with a track record. Hopefully this is inclusive enough without opening the site up to a spam flood and vandalismfest.

4\) No anonymous changes.

Where these pages really need help:

1\) check links, remove broken ones.

2\) add new links that are quality Python information and active.

3\) some care for languages that have next to nothing, but do have people in the Python community - even a link to the Wikipedia page for Python, in that language, is a start (Some are pretty complete and of high quality - the Russian language Wikipedia page for Python, for instance, packs a lot in).

**தமிழ்**

Words for code snippet from [masteranylanguage.com](http://www.masteranylanguage.com/cgi/f/rView.pl?pc=MALTamil&tc=Foods&vm=fc&sw=1&la=)

:::: 
::: 
``` 
   1 # -*- coding: utf-8 -*-
   2 # python 3.0 or 3.1
   3 
   4 # Tamil identifiers (variables)
   5 வாழைப்பழம = 'banana'
   6 பால் = 'milk'
   7 நீர் = 'water'
   8 சாதம = 'rice'
   9 காப்பி = 'coffee'
  10 மீன் = 'fish'
  11 இறைச்சி = 'meat'
  12 பழம = 'fruit'
  13 கோழி = 'chicken'
  14 தக்காளி = 'tomato'
  15 
  16 foods = {'வாழைப்பழம':வாழைப்பழம,
  17          'பால்':பால்,
  18          'நீர்':நீர்,
  19          'சாதம':சாதம,
  20          'காப்பி':காப்பி,
  21          'மீன்':மீன்,
  22          'இறைச்சி':இறைச்சி,
  23          'பழம':பழம,
  24          'கோழி':கோழி,
  25          'தக்காளி':தக்காளி}
  26 
  27 for food in foods:
  28     print('\nEnglish:  ' + foods[food])
  29     print('தமிழ்:  ' + food)
```
:::
::::

[http://ta.wikipedia.org/wiki/பைத்தான்](http://ta.wikipedia.org/wiki/பைத்தான்) Wikipedia

[http://www.tamilnation.org/digital/tic_03/16_rganesh.pdf](http://www.tamilnation.org/digital/tic_03/16_rganesh.pdf) Paper on Tamil version of Python (Pytham)

[download Python related scripts(?)](http://students.uta.edu/mx/mxa6471/download.html)

[Pycon India 2009 TDD](http://www.slideshare.net/Siddhi/test-driven-development-with-python) - has section on reversing Tamil string (Unicode behaves differently than ASCII)

[Ubuntu forum](http://locoteam.ubuntuforums.org/showthread.php?t=884394&page=3) - some code for detecting Tamil Unicode string.

[CategoryLanguage](CategoryLanguage) [CategoryUnicode](CategoryUnicode) [CategoryPyConIndia2009](CategoryPyConIndia2009)
