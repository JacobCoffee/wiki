# BengaliLanguage

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Links to Python information in Bengali Language [1SEP09 Ideally, all the pages should be like the Polish or Turkish pages - all native language, only the necessary English. ]

There are some groundrules, some laid down by the site admins, some my suggestions:

1\) Pages must be named in ASCII and English ([PolishLanguage](PolishLanguage))

2\) Pages must have an explanation in English at the top (Links to Python information in \<language X\>)

3\) (my suggestion) We probably want to limit invites to edit the pages to people we know well, or Pythonistas with a track record. Hopefully this is inclusive enough without opening the site up to a spam flood and vandalismfest.

Where these pages really need help:

1\) check links, remove broken ones.

2\) add new links that are quality Python information and active.

3\) some care for languages that have next to nothing, but do have people in the Python community - even a link to the Wikipedia page for Python, in that language, is a start (Some are pretty complete and of high quality - the Russian language Wikipedia page for Python, for instance, packs a lot in).

ISO 639-1 Code: bn

**বাংলা**

[Bangla-language Wikipedia page for Python] [পাইথন](http://bn.wikipedia.org/wiki/%E0%A6%AA%E0%A6%BE%E0%A6%87%E0%A6%A5%E0%A6%A8_%28%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A7%8B%E0%A6%97%E0%A7%8D%E0%A6%B0%E0%A6%BE%E0%A6%AE%E0%A6%BF%E0%A6%82_%E0%A6%AD%E0%A6%BE%E0%A6%B7%E0%A6%BE%29) - বাংলা উইকিপিডিয়ার নিবন্ধ

[A site for kids learning Python\*/ \[\[[http://hukush-pakush.appspot.com/\|হুকুশ](http://hukush-pakush.appspot.com/%7Cহুকুশ) পাকুশের প্রোগ্রামিং শিক্ষা আলফা\]\] - বাচ্চাদের জন্য পাইথন শেখার বাংলা সাইট ]

/\* GPL-licensed software written in Python (wxPython) enabling phonetic typing in Bangla with an English keyboard layout

[মুক্তলেখা](http://code.google.com/p/muktalekhaa/) - পাইথন ব্যবহার করে লেখা বাংলা লেখার মুক্ত সফটওয়ার

[pybangla](http://pybangla.appspot.com) - পাইথন বাংলাদেশ

[code snippet provided by Rami Chowdhury, who apologises for his awful spelling throughout this page] [Spellings corrected by Ratul R. Minhaz] পাইথন ৩ থেকে বাংলা শব্দ ব্যবহার করে প্রোগ্রাম লেখা যায়:

:::: 
::: 
``` 
   1 $ python3.1
   2 Python 3.1 (r31:73572, Aug 10 2009, 18:55:18)
   3 [GCC 4.3.2 20081105 (Red Hat 4.3.2-7)] on linux2
   4 Type "help", "copyright", "credits" or "license" for more information.
   5 >>> def সালাম_বল(নাম):
   6 ...     কথা = "সালাম {0}। কেমন অাছেন?".format(নাম)
   7 ...     print(কথা)
   8 ...
   9 >>> অামি = 'রুমি'
  10 >>> সালাম_বল(অামি)
  11 সালাম রামি। কেমন অাছেন?
  12 >>> তুমি = 'বাবু'
  13 >>> শালাম_বল(তুমি)
  14 শালাম বাবু। কেমন অাছেন?
```
:::
::::

ফাইলে বাংলা নিয়ে কাজ করতে \'utf-8\' ব্যবহার করুন:

:::: 
::: 
``` 
   1 # -*- coding: utf-8 -*-
   2 #!/usr/bin/python3.1
   3 
   4 def সালাম_বল(নাম):
   5    কথা = "সালাম {0}। কেমন অাছেন?".format(নাম)
   6    print(কথা)
   7 
   8 অামি = 'রুমি'
   9 তুমি = 'Carl'
  10 
  11 if __name__ == '__main__':
  12    সালাম_বল(অামি)
  13    সালাম_বল(তুমি)
```
:::
::::

### ব্লগ 

- [সামহোয়্যার ইন ব্লগ](http://www.google.com.bd/custom?domains=www.somewhereinblog.net&q=%E0%A6%AA%E0%A6%BE%E0%A6%87%E0%A6%A5%E0%A6%A8&sitesearch=www.somewhereinblog.net&client=pub-6383224968083856&forid=1&ie=UTF-8&oe=UTF-8&flav=0000&sig=GQYjOYEqLSfb_zjI&cof=GALT%3A%23008000%3BGL%3A1%3BDIV%3A%23FFFFFF%3BVLC%3A663399%3BAH%3Acenter%3BBGC%3AFFFFFF%3BLBGC%3AFFFFFF%3BALC%3A0000FF%3BLC%3A0000FF%3BT%3A000000%3BGFNT%3A0000FF%3BGIMP%3A0000FF%3BLH%3A80%3BLW%3A300%3BL%3Ahttp%3A%2F%2Fwww.somewhereinblog.net%2Flogo.jpg%3BS%3Ahttp%3A%2F%2Fwww.somewhereinblog.net%3BFORID%3A1&hl=en) - পাইথন সম্পর্কিত জিঞ্জাসা

[CategoryLanguage](CategoryLanguage) [CategoryUnicode](CategoryUnicode)
