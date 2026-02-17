# MacPython/FileMakerPro/DeliciousLibrary

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Transfer data from a [DeliciousLibrary](./DeliciousLibrary.html) XML database to a [FileMakerPro](./FileMakerPro.html) database**

:::: 
::: 
``` 
   1 #!/usr/bin/pythonw
   2  
   3 from pprint import pprint
   4 from elementtree import /ElementTree # [1]
   5 from appscript import *
   6 from Carbon.File import FSSpec # [2]
   7  
   8 # /FileMaker prefs
   9 FM_ID = 'com.filemaker.pro7'
  10 FM_DB_PATH = '/Users/SOMEUSER/Desktop/Library.fp7' # [3][4]
  11 FM_DB = 'Library'
  12 FM_TABLE = 'Library'
  13  
  14 # Delicious Library prefs
  15 DL_DB_PATH = '/Users/SOMEUSER/Library/Application Support/Delicious Library/Library Media Data.xml' # [4][5]
  16  
  17 # connect to the /FileMaker database
  18 try:
  19  fm = app(id=FM_ID)
  20 except ApplicationNotFoundError:
  21  print "FileMaker Pro 7 application has not been found."
  22  sys.exit(0)
  23  
  24 if not fm.databases[FM_DB].exists():
  25  try:
  26   fm.open(FSSpec(FM_DB_PATH))
  27  except:
  28   print "Can't open source database '%s'." % FM_DB_PATH
  29   sys.exit(0)
  30  
  31 if not fm.databases[FM_DB].tables[FM_TABLE].exists():
  32  print "Table '%s' doesn't exists in source database '%s'." % (FM_TABLE, FM_DB)
  33  sys.exit(0)
  34  
  35 t1 = fm.databases[FM_DB].tables[FM_TABLE]
  36  
  37 # open Delicious Library XML file
  38  
  39 tree = ElementTree.parse(DL_DB_PATH)
  40  
  41 ## and transfer book records
  42  
  43 fields = t1.fields.name.get()
  44  
  45 for el in tree.findall('//items/book'):
  46  data = [ (el.get(f) or '') for f in fields ]
  47  rec = fm.create(new=k.record, with_data=data, at=t1)
```
:::
::::

**Footnotes:**

1.  [ElementTree](http://effbot.org/zone/element-index.htm)

2.  \...Carbon.File.FSSpec not a good idea\... will correct asap\...

3.  \...will post Library.fp7 sample database asap\...

4.  you have to adapt the path\...

5.  [DeliciousLibrary](http://www.delicious-monster.com/)

![/!\\](/wiki/europython/img/alert.png "/!\") **Warning:** you could use [/ElementTree](./MacPython(2f)FileMakerPro(2f)DeliciousLibrary(2f)ElementTree.html) to edit the [/DeliciousLibrary](./MacPython(2f)FileMakerPro(2f)DeliciousLibrary(2f)DeliciousLibrary.html) XML file, but don\'t forget it\'s not a database: you could corrupt your [/DeliciousLibrary](./MacPython(2f)FileMakerPro(2f)DeliciousLibrary(2f)DeliciousLibrary.html) database in case of concurrent access. And no, [/DeliciousLibrary](./MacPython(2f)FileMakerPro(2f)DeliciousLibrary(2f)DeliciousLibrary.html) is not (yet) scriptable :-/
