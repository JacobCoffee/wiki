# MacPython/FileMakerPro/Annoyances

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**About the Table class:**

- in some case, specifying the table class as `class_=k.table` doesn\'t work, use `class_='cTBL'` instead:

::: {}
  ----------------------------------------- ----------------------------------------
  **Instead of:**                           **do:**
  `fm.databases[1].count(class_=k.table)`   `fm.databases[1].count(class_='cTBL')`
  ----------------------------------------- ----------------------------------------
:::
