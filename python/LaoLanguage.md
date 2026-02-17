# LaoLanguage

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Links to Python information in Lao

ISO 639-1 Code: lo

[1SEP09 Ideally, all the language pages should be like the Polish or Turkish pages - all native language, only the necessary English. ]

There are some groundrules, some laid down by the site admins, some my suggestions:

1\) Pages must be named in ASCII and English ([PolishLanguage](PolishLanguage))

2\) Pages must have an explanation in English at the top (Links to Python information in \<language X\>)

3\) (my suggestion) We probably want to limit invites to edit the pages to people we know well, or Pythonistas with a track record. Hopefully this is inclusive enough without opening the site up to a spam flood and vandalismfest.

4\) No anonymous edits.

Where these pages really need help:

1\) check links, remove broken ones.

2\) add new links that are quality Python information and active.

3\) some care for languages that have next to nothing, but do have people in the Python community - even a link to the Wikipedia page for Python, in that language, is a start (Some are pretty complete and of high quality - the Russian language Wikipedia page for Python, for instance, packs a lot in).

**ພາສາລາວ**

Phrases taken from [laoconnection](http://laoconnection.com/language2a.htm)

Getting Lao words for identifiers (variables) and text:

:::: 
::: 
``` 
   1 >>> # -*- coding: utf-8 -*-
   2 >>> # python 3.0/3.1
   3 >>> # having some problems with combination characters rendering correctly
   4 >>> # Courier 10 point font at size 14 in idle seems to work best
   5 >>>
   6 >>> # get 'my name is' phrase from Unicode
   7 >>> '\u0E8A\u0EB7\u0EC8\u0E82\u0EAD\u0EC9\u0EA2\u0EC1\u0EA1\u0EC8\u0E99'
   8 'ຊື່ຂອ້ຢແມ່ນ'
   9 >>> # get 'I am from' phrase from Unicode
  10 >>> '\u0E82\u0EC9\u0EAD\u0EA2\u0EA1\u0EB2\u0E88\u0EB2\u0E81'
  11 'ຂ້ອຢມາຈາກ'
  12 >>> # get 'Laos' from Unicode
  13 >>> '\u0EA5\u0EB2\u0EA7'
  14 'ລາວ'
  15 >>> # get 'Canada' from Unicode
  16 >>> '\u0E84\u0EB2\u0E99\u0EB2\u0E94\u0EB2'
  17 'ຄານາດາ'
  18 >>> # get 'America' from Unicode
  19 >>> '\u0EAD\u0EB2\u0EC0\u0EA1\u0EA3\u0EB4\u0E81\u0EB2'
  20 'ອາເມຣິກາ'
  21 >>> # get 'France' from Unicode
  22 >>> '\u0E9D\u0EA3\u0EC9\u0EC8\u0E87'
  23 'ຝຣ້່ງ'
```
:::
::::

Using UTF-8 encoded identifiers:

:::: 
::: 
``` 
   1 # -*- coding: utf-8 -*-
   2 # python 3.0/3.1
   3 
   4 # using Lao name Dao (ດາວ) from Wikipedia = star
   5 # using ຊ່ືອ (name) from Wikipedia as my variable
   6 ຊ່ືອ = ['ດາວ', 'Bob', 'Mary', 'Monique']
   7 
   8 countries = ['ລາວ', 'ຄານາດາ', 'ອາເມຣິກາ', 'ຝຣ້່ງ']
   9 
  10 for ຊ່ືອx, countryx in zip(ຊ່ືອ, countries):
  11     print('\nຊື່ຂອ້ຢແມ່ນ ' + ຊ່ືອx)
  12     print('ຂ້ອຢມາຈາກ ' + countryx + '\n')
```
:::
::::

[CategoryLanguage](CategoryLanguage) [CategoryUnicode](CategoryUnicode)
