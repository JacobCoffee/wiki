# MacPython/VoodooPad/AppscriptingOverview

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

![/!\\](/wiki/europython/img/alert.png "/!\") *using Carbon.File.FSSpec doesn\'t seem to be the best way to handle files. I\'ll correct these examples asap\...*

**1. Opening documents, creating pages and modifying content**

:::: 
::: 
``` 
   1 #!/usr/bin/pythonw
   2 
   3 from appscript import *
   4 from Carbon.File import FSSpec
   5 
   6 # connect to /VoodooPad
   7 vp = app(id='com.flyingmeat.VoodooPad')
   8 
   9 # open an existing test document
  10 vpdoc = vp.open(FSSpec('/Users/SOMEUSER/Test1.vdoc'))
  11 
  12 # create a scratchpad with some initial content
  13 scratchpad = u'AppScript Scratchpad'
  14 
  15 vpdoc.create_page(
  16         with_title = scratchpad, 
  17         with_contents = u'Hello, world !')
  18 
  19 # add some text to the scratchpad
  20 vp.prepend(
  21         text = u'some text before...\n', 
  22         to = vpdoc.pages[scratchpad])
  23         
  24 vp.append(
  25         text = u'\n...some text after\n\n', 
  26         to = vpdoc.pages[scratchpad])
  27 
  28 # add a link from the index page to the scratchpad page 
  29 vp.prepend(
  30         text = u'A link to the /AppScript Scratchpad Page...\n\n', 
  31         to = vpdoc.pages[u'index'])
  32 
  33 # create a bunch of pages
  34 for pnum in xrange(1,10):
  35         vpdoc.create_page(
  36                 with_title = u'Page %d' % pnum, 
  37                 with_contents = u'Hello, world !\n\nThis is page %d.' % pnum)   
  38 
  39 # create an index on the scratchpad
  40 vpdoc.open_page(with_title=scratchpad)
  41 
  42 comment = u'There are %d page(s) and %d paragraph(s) in document %s:\n\n' % (
  43         vpdoc.count(each=k.page),
  44         vpdoc.pages.text.count(each=k.paragraph),
  45         vpdoc.name.get())
  46 
  47 vp.append(
  48         text = comment, 
  49         to = vpdoc.pages[scratchpad])
  50 
  51 for pname in vpdoc.pages.name.get():
  52         vp.append(
  53                 text = u'\u2022 %s\n' % pname, 
  54                 to = vpdoc.pages[scratchpad])   
  55 
  56 # ?
  57 print vp.taunt()
```
:::
::::

**2. Deleting pages and content**

:::: 
::: 
``` 
   1 # do some cleanup
   2 vpdoc.delete_page(with_title=scratchpad)
   3 
   4 for i in xrange(1,10):
   5         vpdoc.delete_page(with_title='page %d' % i)
   6 
   7 # doesn't work:
   8 #vpdoc.pages['index'].text.paragraphs.first.delete()
```
:::
::::
