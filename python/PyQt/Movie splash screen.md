# PyQt/Movie splash screen

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Movie splash screen 

On the `#pyqt`{.backtick} channel on freenode, iTayb asked if it was possible to show a movie instead of a static image in a splash screen.

The following code shows one way to do this, but it is implemented slightly differently to the way you might expect. Ideally, the drawContents() method of the QSplashScreen class would be reimplemented. However, this does not seem to get called, so we reimplement the paintEvent() method instead. This means that we can\'t use the showMessage() method to update the information in the splash screen.

:::: 
::: 
``` 
   1 import sys, time
   2 from PyQt4.QtCore import Qt, QTimer
   3 from PyQt4.QtGui import *
   4 
   5 class MovieSplashScreen(QSplashScreen):
   6 
   7     def __init__(self, movie, parent = None):
   8     
   9         movie.jumpToFrame(0)
  10         pixmap = QPixmap(movie.frameRect().size())
  11         
  12         QSplashScreen.__init__(self, pixmap)
  13         self.movie = movie
  14         self.movie.frameChanged.connect(self.repaint)
  15     
  16     def showEvent(self, event):
  17         self.movie.start()
  18     
  19     def hideEvent(self, event):
  20         self.movie.stop()
  21     
  22     def paintEvent(self, event):
  23     
  24         painter = QPainter(self)
  25         pixmap = self.movie.currentPixmap()
  26         self.setMask(pixmap.mask())
  27         painter.drawPixmap(0, 0, pixmap)
  28     
  29     def sizeHint(self):
  30     
  31         return self.movie.scaledSize()
  32 
  33 
  34 if __name__ == "__main__":
  35 
  36     app = QApplication(sys.argv)
  37     movie = QMovie("animation.gif")
  38     splash = MovieSplashScreen(movie)
  39     splash.show()
  40     
  41     start = time.time()
  42     
  43     while movie.state() == QMovie.Running and time.time() < start + 10:
  44         app.processEvents()
  45     
  46     window = QWidget()
  47     window.show()
  48     splash.finish(window)
  49     
  50     sys.exit(app.exec_())
```
:::
::::
