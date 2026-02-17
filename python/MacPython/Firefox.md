# MacPython/Firefox

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Firefox doesn\'t really play in the Applescripting world. See [this bug filed against it](https://bugzilla.mozilla.org/show_bug.cgi?id=125419), and vote for that bug if you\'d like to make it Applescriptable.

However, there are some workarounds for Firefox 2. Adium uses this:

    if ((application processes whose (name is equal to "firefox-bin")) count) is greater than 0 then
         tell application "Firefox"
             if (count of every window) is greater than 0 then
                   set the end of candidateURLs to «class curl» of window 1
              end if
          end tell
    end if

Hengist says this might be written in appscript like this:

    from appscript import *
    ff = app('Firefox')
    appscriptref = ff.windows[1]
    aemref = appscriptref.AS_aemreference
    aemref = aemref.property('curl')
    appscriptref = ff.AS_newreference(aemref)
    print appscriptref.get()

Unfortunately, [Firefox 3 broke this workaround](https://bugzilla.mozilla.org/show_bug.cgi?id=427448).
