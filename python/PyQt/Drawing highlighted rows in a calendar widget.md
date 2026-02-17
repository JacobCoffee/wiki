# PyQt/Drawing highlighted rows in a calendar widget

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Drawing highlighted rows in a calendar widget 

On the Freenode #pyqt channel, rowinggolfer asked if it was possible to highlight the current week in a calendar widget.

:::: 
::: 
``` 
   1 from PyQt4.QtCore import *
   2 from PyQt4.QtGui import *
   3 
   4 class WeekCalendar(QCalendarWidget):
   5 
   6     def __init__(self, *args):
   7     
   8         QCalendarWidget.__init__(self, *args)
   9         self.color = QColor(self.palette().color(QPalette.Highlight))
  10         self.color.setAlpha(64)
  11         self.selectionChanged.connect(self.updateCells)
  12     
  13     def paintCell(self, painter, rect, date):
  14     
  15         QCalendarWidget.paintCell(self, painter, rect, date)
  16         
  17         first_day = self.firstDayOfWeek()
  18         last_day = first_day + 6
  19         current_date = self.selectedDate()
  20         current_day = current_date.dayOfWeek()
  21         
  22         if first_day <= current_day:
  23             first_date = current_date.addDays(first_day - current_day)
  24         else:
  25             first_date = current_date.addDays(first_day - 7 - current_day)
  26         last_date = first_date.addDays(6)
  27         
  28         if first_date <= date <= last_date:
  29             painter.fillRect(rect, self.color)
```
:::
::::
