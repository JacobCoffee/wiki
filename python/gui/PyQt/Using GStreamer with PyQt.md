# PyQt/Using GStreamer with PyQt

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Using GStreamer with PyQt 

This example code was posted to the [PyQt mailing list](http://www.riverbankcomputing.com/mailman/listinfo/pyqt) in [a message](http://www.riverbankcomputing.com/pipermail/pyqt/2009-September/024240.html) by Baz Walter.

:::: 
::: 
``` 
   1 import sys, os
   2 import gobject, pygst
   3 pygst.require('0.10')
   4 import gst
   5 from PyQt4.QtCore import SIGNAL, SLOT
   6 from PyQt4.QtGui import QApplication, QMainWindow, QPushButton, \
   7                          QFileDialog
   8 
   9 
  10 class MainWindow(QMainWindow):
  11      def __init__(self):
  12          QMainWindow.__init__(self)
  13          self.setWindowTitle('Audio-Player')
  14          self.resize(120, 50)
  15          self.move(500, 500)
  16          self.button = QPushButton(self)
  17          self.button.setText('Start')
  18          self.button.setMinimumSize(90, 0)
  19          self.setCentralWidget(self.button)
  20          self.connect(self.button, SIGNAL('clicked()'), self.start_stop)
  21          self.player = gst.element_factory_make('playbin', 'player')
  22          try:
  23              # alsasink pulsesink osssink autoaudiosink
  24              device = gst.parse_launch('alsasink')
  25          except gobject.GError:
  26              print 'Error: could not launch audio sink'
  27          else:
  28              self.player.set_property('audio-sink', device)
  29              self.bus = self.player.get_bus()
  30              self.bus.add_signal_watch()
  31              self.bus.connect('message', self.on_message)
  32 
  33      def start_stop(self):
  34          if self.button.text() == 'Start':
  35              filepath = QFileDialog.getOpenFileName(self, 'Choose File')
  36              if filepath:
  37                  self.button.setText('Stop')
  38                  self.player.set_property('uri', 'file://' + filepath)
  39                  self.player.set_state(gst.STATE_PLAYING)
  40          else:
  41              self.player.set_state(gst.STATE_NULL)
  42              self.button.setText('Start')
  43 
  44      def on_message(self, bus, message):
  45          t = message.type
  46          if t == gst.MESSAGE_EOS:
  47              self.player.set_state(gst.STATE_NULL)
  48              self.button.setText('Start')
  49          elif t == gst.MESSAGE_ERROR:
  50              self.player.set_state(gst.STATE_NULL)
  51              err, debug = message.parse_error()
  52              print 'Error: %s' % err, debug
  53              self.button.setText('Start')
  54 
  55 
  56 if __name__ == '__main__':
  57 
  58      gobject.threads_init()
  59      qApp = QApplication(sys.argv)
  60      qApp.connect(qApp, SIGNAL('lastWindowClosed()'),
  61                   qApp, SLOT('quit()'))
  62      mainwindow = MainWindow()
  63      mainwindow.show()
  64      sys.exit(qApp.exec_())
```
:::
::::
