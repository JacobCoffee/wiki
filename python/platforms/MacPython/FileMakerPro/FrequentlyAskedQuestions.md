# MacPython/FileMakerPro/FrequentlyAskedQuestions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Q:** *I have [FileMakerPro](./FileMakerPro.html) 6 and 7 on the same machine. How can I be sure I open the right one ?*

**A:** With `fm = app('FileMaker Pro')` or `fm = app('FileMaker Pro.app')`, you\'ll never know. Use `fm6 = app(id='com.filemaker.filemakerpro')` for [FileMakerPro](./FileMakerPro.html) 6 and `fm7 = app(id='com.filemaker.pro7')` for [FileMakerPro](./FileMakerPro.html) 7.
