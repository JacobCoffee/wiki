# MacPython/FileMakerPro/AppscriptingOverview

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

![{i}](/wiki/europython/img/icon-info.png "{i}") *to use this script, you\'ll need the Library.fp7 and Library.tab sample files (I will post them asap) and to edit the `DBPATH` and `IMPORTFILE` variables accordingly.*

:::: 
::: 
``` 
   1 #!/usr/bin/pythonw
   2 
   3 from pprint import pprint
   4 from appscript import *
   5 from Carbon.File import FSSpec
   6 import codecs
   7 
   8 DBPATH = '/Users/SOMEUSER/Desktop/Library.fp7'
   9 DBNAME = 'Library'
  10 TBLNAME = 'Library'
  11 IMPORTFILE = '/Users/SOMEUSER/Desktop/library.tab'
  12 
  13 
  14 """ 
  15         Connecting to /FileMaker and opening database
  16 """
  17 
  18 fm = app(id='com.filemaker.pro7') # [1]
  19 
  20 if not fm.databases[DBNAME].exists():
  21         fm.open(FSSpec(DBPATH)) # [2]
  22 
  23 
  24 """
  25     Querying database schema
  26 """
  27 
  28 print "FileMaker has %d database(s) opened: " % fm.count(class_=k.database)
  29 print ", ".join(fm.databases.name.get()) # [3]
  30 
  31 db = fm.databases[DBNAME] # [3]
  32 
  33 print "\nDatabase '%s' has %d table(s): " % (DBNAME, db.count(class_='cTBL')) # [4]
  34 print ", ".join(db.tables.name.get())
  35 
  36 t1 = db.tables[TBLNAME]
  37 
  38 print "\nTable '%s' has %d field(s): " % (TBLNAME, t1.count(class_=k.field))
  39 print ", ".join(t1.fields.name.get())
  40 
  41 print "\nTable '%s' schema:\n(name, type, nulls OK, unique value, global value)" % TBLNAME
  42 pprint(zip(
  43         t1.fields.name.get(), 
  44         t1.fields.default_type.get(),
  45         t1.fields.nulls_OK.get(),
  46         t1.fields.unique_value.get(),
  47         t1.fields.globalValue.get()))
  48 
  49 
  50 """
  51         Creating new records
  52 """
  53 
  54 if t1.count(class_=k.record) > 0:
  55         t1.records.delete()
  56 
  57 f = codecs.open(IMPORTFILE, 'r', 'mac_roman')
  58 
  59 for line in f:
  60         data = line.split('\t')
  61         rec = fm.create(new=k.record, with_data=data, at=t1) # [5]
  62 
  63 f.close()
  64 
  65 
  66 """
  67         Looking at records
  68 """
  69 
  70 print "\nTable '%s' has %d record(s)" % (TBLNAME, t1.count(class_=k.record))
  71 
  72 qry1 = t1.records.filter(its.fields['title'].cellValue.contains(u'Calvin'))
  73 
  74 if qry1.exists():
  75         print "\nselect title from library where title contains \'Calvin\':"
  76         pprint(qry1.fields['title'].get())
  77 
  78 qry2 = t1.records.filter(its.fields['author'].cellValue.contains(u'McCaffrey'))
  79 
  80 if qry2.exists():
  81         print "\nselect title from library where author contains \'McCaffrey\':"
  82         pprint(qry2.fields['title'].get())
  83 
  84 qry3 = t1.records.filter(its.fields['genre'].cellValue.contains(u'Thrillers'))
  85 
  86 if qry3.exists():
  87         print "\nselect title, authors from library where genre contains \'Thrillers\':"
  88         pprint(zip(qry3.fields['title'].get(), qry3.fields['author'].get()))
  89 
  90 print "\nselect distinct author from library:"
  91 pprint(set(t1.fields['author'].get())) # [XXX]
  92 
  93 # show "List" layout with the records from qry3, sorted by authors
  94 
  95 qry3.show()
  96 fm.layouts['List'].show()
  97 fm.layouts['List'].sort(by=fm.fields['author']) # [XXX]
```
:::
::::

**Footnotes:**

1.  use `app(id='com.filemaker.pro7')` instead of `app('FileMaker Pro')` to be sure only [/FileMakerPro](./MacPython(2f)FileMakerPro(2f)AppscriptingOverview(2f)FileMakerPro.html) 7 is launched

2.  Carbon.File.FSSpec is not the best way to handle files. I have to investigate that point\...

3.  `fm.databases.name` returns the db name with the \'.fp7\' suffix, but it can be omitted when specifying `fm.databases[...]`

4.  specifying the table class as `class_=k.table` doesn\'t work, use `class_='cTBL'` instead

5.  according to [FileMakerPro](./FileMakerPro.html)\'s Apple Event Reference, the fastest way to insert data is to:

    - use `fm.create(new=k.record, with_data=data, at=table1)`, with data as a list of values in the same order as `table1.fields.name.get()`

    - insert data at the table level, outside the currently found set.
