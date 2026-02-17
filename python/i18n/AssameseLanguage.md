# AssameseLanguage

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Links to Python information in the Assamese Language

ISO 639-1 Code: as

[1SEP09 Ideally, all the language pages should be like the Polish or Turkish pages - all native language, only the necessary English. ]

There are some groundrules, some laid down by the site admins, some my suggestions:

1\) Pages must be named in ASCII and English ([PolishLanguage](PolishLanguage))

2\) Pages must have an explanation in English at the top (Links to Python information in \<language X\>)

3\) (my suggestion) We probably want to limit invites to edit the pages to people we know well, or Pythonistas with a track record. Hopefully this is inclusive enough without opening the site up to a spam flood and vandalismfest.

Where these pages really need help:

1\) check links, remove broken ones.

2\) add new links that are quality Python information and active.

3\) some care for languages that have next to nothing, but do have people in the Python community - even a link to the Wikipedia page for Python, in that language, is a start (Some are pretty complete and of high quality - the Russian language Wikipedia page for Python, for instance, packs a lot in).

**অসমীয়া**

Texts for code snippets (national song) courtesy of [www.assam.org](http://www.assam.org/node/2330)

:::: 
::: 
``` 
   1 # -*- coding: utf-8 -*-
   2 # python 3.0 or python 3.1
   3 
   4 LATINLINE1 = "\n\na' mor Aponaar dex"
   5 LATINLINE2 = "a' mor cikuNI dex"
   6 LATINLINE3 = 'enekHan xuwalaa enekHan Xufalaa'
   7 LATINLINE4 = 'enekHan maramar dex\n\n'
   8 
   9 # not necessary (could use list), but illustrates dictionary
  10 LATIN = {1:LATINLINE1, 2:LATINLINE2, 3:LATINLINE3, 4:LATINLINE4}
  11 
  12 for num in range(4):
  13    print(LATIN[num + 1])
  14 
  15 অসমীয়া1 = "অ' েমাৰ আেপানাৰ েদশ"
  16 অসমীয়া2 = "অ' েমাৰ িচকুণী েদশ"
  17 অসমীয়া3 = 'এেনখন শুৢবলা এেনখন সুফলা'
  18 অসমীয়া4 = 'এেনখন মৰমৰ েদশ'
  19 
  20 অসমীয়া = {1:অসমীয়া1, 2:অসমীয়া2, 3:অসমীয়া3, 4:অসমীয়া4}
  21 
  22 for num in range(4):
  23     print(অসমীয়া[num + 1])
```
:::
::::

------------------------------------------------------------------------

[CategoryLanguage](CategoryLanguage) [CategoryUnicode](CategoryUnicode) [CategoryPythonIndia](CategoryPythonIndia)
