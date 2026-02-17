# PyQt/Five minute steps in a QTimeEdit

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Five minute steps in a QTimeEdit 

On the `#pyqt`{.backtick} channel on Freenode, `rowinggolfer`{.backtick} asked if it was possible to make QTimeEdit step in five minute intervals.

The following subclass reimplements the `stepBy()`{.backtick} method and calls the base class implementation with an adjusted number of steps.

:::: 
::: 
``` 
   1 class FiveMinuteTimeEdit(QTimeEdit):
   2   def stepBy(self, steps):
   3     if self.currentSection() == self.MinuteSection:
   4       QTimeEdit.stepBy(self, steps * 5)
   5     else:
   6       QTimeEdit.stepBy(self, steps)
```
:::
::::
