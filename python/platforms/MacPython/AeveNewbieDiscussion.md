# MacPython/AeveNewbieDiscussion

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# How to use aeve for newbies 

This aeve module sounds great, exactly what I\'ve been looking for, but I must say that I have been having a ton of trouble getting things to work. Some more documentation would really help. To see what I can add to the effort, I\'ve added this page to jot down my findings. - [WinstonWolff](WinstonWolff) Nov 03

**Q: How do I Install this thing?**

A: In order to install aeve on Panther you need these modules: - ww nov 03

1.  pyrex - [http://www.cosc.canterbury.ac.nz/\~greg/python/Pyrex/](http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/)

2.  [../LaunchServices](LaunchServices) - available on this Mr. Ippolitti\'s website: [http://undefined.org/python/#LaunchServices](http://undefined.org/python/#LaunchServices)

3.  TECManager - also at undefined.org

4.  Finally, you can install aeve. I installed all of the above using \"python setup.py build\" and then \"sudo python setup.py install\"

**Q: How do I get started? I know Python, but I don\'t know a thing about [../AppleScript](AppleScript).**

A: To get a primer on how to \"read\" [../AppleScript](AppleScript) and understand it as a Python programmer, I found Apple\'s \"AppleScript Language Guide\" the most useful. - [WinstonWolff](WinstonWolff) Nov 03

**Q: I\'ve seen the iCal example of how to \"make\" an object, but I want to automate [../OmniGraffle](OmniGraffle). How do I create these properties to pass into make()? I\'ve tried the following, but the iter Objects For Name() doesn\'t work.**

:::: 
::: 
``` 
   1 import aeve
   2 app = aeve.talkto('/Applications/OmniGraffle.app')
   3 from aeve.Applications import OmniGraffle as og
   4 origin  = og.shape._aereg_.iterObjectsForName("origin", aekind="property", deep=True).next()
   5 size    = og.Standard_Suite._aereg_.iterObjectsForName("size", aekind="property", deep=True).next()
   6 name    = og.Standard_Suite._aereg_.iterObjectsForName("name", aekind="property", deep=True).next()
   7 
   8 shape = app.make(new=og.shape, with_properties={ origin:(100,100), size:(20,20), name:"Circle" } )
```
:::
::::

A: no answer yet.

**Q: I\'m just having a really hard time finding my way around, where should I look for info?**

A: no answer yet.
