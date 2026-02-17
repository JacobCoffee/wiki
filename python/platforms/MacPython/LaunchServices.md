# MacPython/LaunchServices

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# /LaunchServices 

[LaunchServices](./LaunchServices.html) is a pythonic wrapper for just about everything Apple\'s [Launch Services API](http://developer.apple.com/technotes/tn/tn2017.html) has to offer. It was developed primarily to make [/aeve](./MacPython(2f)LaunchServices(2f)aeve.html) a hell of a lot easier to use.

# status

[LaunchServices](./LaunchServices.html) is at its first public release, 0.1

# examples

:::: 
::: 
``` 
   1 >> import LaunchServices as LS
   2 >> LS.GetDisplayNameForPath('/')
   3 u'Crack'
   4 >> LS.GetKindStringForPath('/')
   5 u'Volume'
   6 >> LS.GetApplicationPathForInfo(extension='mp3')
   7 u'/Applications/iTunes.app'
   8 >> LS.GetApplicationPathForInfo(creator='MACS')
   9 u'/System/Library/CoreServices/Finder.app'
  10 >> LS.FindApplicationPath(bundle='com.apple.iChat')
  11 u'/Applications/iChat.app'
```
:::
::::
