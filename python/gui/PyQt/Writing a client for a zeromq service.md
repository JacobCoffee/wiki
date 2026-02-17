# PyQt/Writing a client for a zeromq service

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Writing a client for a zeromq service 

On the `#pyqt`{.backtick} channel on [Freenode](http://freenode.net), `Nils^`{.backtick} asked for a way to write a GUI client for a [zeromq](http://www.zeromq.org) service, using the [Python bindings](http://www.zeromq.org/bindings:python).

We decided to try using a worker thread to monitor the socket that connects the client to the server, emitting a signal whenever new data is received.

:::: 
::: 
``` 
   1 ##############################################################################
   2 ##                                                                          ## 
   3 ##  adapted from http://zguide.zeromq.org/py:wuserver                       ##
   4 ##                                                                          ## 
   5 ##############################################################################
   6 
   7 
   8 import sys
   9 import zmq
  10 
  11 from PyQt4 import QtCore, QtGui        
  12                 
  13 class ZeroMQ_Listener(QtCore.QObject):
  14 
  15     message = QtCore.pyqtSignal(str)
  16     
  17     def __init__(self):
  18        
  19         QtCore.QObject.__init__(self)
  20         
  21         # Socket to talk to server
  22         context = zmq.Context()
  23         self.socket = context.socket(zmq.SUB)
  24 
  25         print "Collecting updates from weather server"
  26         self.socket.connect ("tcp://localhost:5556")
  27 
  28         # Subscribe to zipcode, default is NYC, 10001
  29         filter = str(app.arguments()[1]) if len(app.arguments()) > 1 else "10001"
  30         self.socket.setsockopt(zmq.SUBSCRIBE, filter)
  31         
  32         self.running = True
  33     
  34     def loop(self):
  35         while self.running:
  36             string = self.socket.recv()
  37             self.message.emit(string)
  38             
  39 class ZeroMQ_Window(QtGui.QMainWindow):
  40     def __init__(self, parent=None):
  41         QtGui.QMainWindow.__init__(self, parent)
  42 
  43         
  44         frame = QtGui.QFrame()
  45         label = QtGui.QLabel("listening")
  46         self.text_edit = QtGui.QTextEdit()
  47         
  48         layout = QtGui.QVBoxLayout(frame)
  49         layout.addWidget(label)
  50         layout.addWidget(self.text_edit)
  51         
  52         self.setCentralWidget(frame)
  53 
  54         self.thread = QtCore.QThread()
  55         self.zeromq_listener = ZeroMQ_Listener()
  56         self.zeromq_listener.moveToThread(self.thread)
  57         
  58         self.thread.started.connect(self.zeromq_listener.loop)
  59         self.zeromq_listener.message.connect(self.signal_received)
  60         
  61         QtCore.QTimer.singleShot(0, self.thread.start)
  62     
  63     def signal_received(self, message):
  64         self.text_edit.append("%s\n"% message)
  65 
  66     def closeEvent(self, event):
  67         self.zeromq_listener.running = False
  68         self.thread.quit()
  69         self.thread.wait()
  70 
  71 if __name__ == "__main__":
  72     app = QtGui.QApplication(sys.argv)
  73     
  74     mw = ZeroMQ_Window()
  75     mw.show()
  76     
  77     sys.exit(app.exec_())
```
:::
::::
