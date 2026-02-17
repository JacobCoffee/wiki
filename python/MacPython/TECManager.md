# MacPython/TECManager

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# TECManager 

Pythonic wrapper for the Text to Unicode functionality of Apple\'s [Text Encoding Conversion Manager](http://developer.apple.com/documentation/Carbon/Conceptual/ProgWithTECM/).

# status

TECManager is at it\'s second release, version 0.2. It now supports Python text encodings (replaces the built-in mac specific codecs and adds new ones), and its usage is pretty much transparent after the module has been imported.

# examples

:::: 
::: 
``` 
   1 >> import TECManager as TM
   2 >> # convert a macRoman bullet to a unicode bullet
   3 >> '\xa5'.decode('mac_roman')
   4 u'\u2022'
   5 >> # convert a smHebrew HEBREW POINT QAMATS, alternate form "qamats qatan"
   6 >> '\xde'.decode('mac_hebrew')
   7 u'\u05b8\uf87f'
   8 >> # create a new 'mac_turkish' encoding, which is a modified smRoman script.
   9 >> TM.tec_codecs.createModule('encodings.mac_turkish', TM.getTextEncoding(script=TM.smRoman, language=TM.langTurkish, region=TM.verTurkey))
  10 >> '\xa5'.decode('mac_turkish')
  11 u'\u2022'
```
:::
::::

# links

[http://undefined.org/python/#TECManager](http://undefined.org/python/#TECManager)
