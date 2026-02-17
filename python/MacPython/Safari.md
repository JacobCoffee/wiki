# MacPython/Safari

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

You can get the current URL of the current window from Safari with the following appscript:

    import appscript
    print appscript.app("Safari").windows.first.current_tab.URL()
