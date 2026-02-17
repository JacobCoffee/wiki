# PyQt/Exposing Qt Classes to QtWebKit

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Exposing Qt Classes to QtWebKit 

On the [PyQt mailing list](TheMailingList), Christophe [asked for examples](http://www.riverbankcomputing.com/pipermail/pyqt/2010-June/026803.html) that show Qt objects being added to QtWebKit for use with JavaScript.

A simple example of this can be found on Mario Boikov\'s blog: [Calling Python from JavaScript in PyQt\'s QWebkit](http://pysnippet.blogspot.com/2010/01/calling-python-from-javascript-in-pyqts.html).

The following code is an extreme example of this which uses a wrapper class to expose the QFile class and its open() and readAll() methods to JavaScript.

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import *
   3 from PyQt4.QtGui import *
   4 from PyQt4.QtWebKit import *
   5 
   6 
   7 js = \
   8 """
   9 QFile = function(path)
  10 {
  11     var name = _QFile_factory.createQFile(path);
  12     document.getElementById("name").innerText = name;
  13     return _wrapper;
  14 }
  15 """
  16 
  17 html = \
  18 """<html>
  19 <head>
  20   <title>JavaScript Qt Wrapper Test</title>
  21   <script type="text/javascript">
  22     function readFile()
  23     {
  24         var file1 = QFile("/home/user/temp.txt");       # <- put a path to a text file here
  25         var file2 = QFile("qtwrappertest.py");          # <- refer to this script or some other text file here
  26         var area1 = document.getElementById("contents1");
  27         var area2 = document.getElementById("contents2");
  28         file1.open(1);
  29         file2.open(1);
  30         area1.innerText = file1.readAll;
  31         area2.innerText = file2.readAll;
  32         file1.close();
  33         file2.close();
  34     }
  35   </script>
  36 </head>
  37 <body>
  38   <h1>JavaScript Qt Wrapper Test</h1>
  39   <p id="name"></p>
  40   <pre id="contents1">
  41      [Click the button to show the contents of a file.]
  42   </pre>
  43   <pre id="contents2">
  44      [Click the button to show the contents of a file.]
  45   </pre>
  46   <input type="button" onclick="readFile()" value="Click me">
  47 </body>
  48 </html>
  49 """
  50 
  51 class FileWrapper(QObject):
  52 
  53     def __init__(self, path):
  54     
  55         QObject.__init__(self)
  56         self.file = QFile(path)
  57     
  58     @pyqtSignature("open(int)")
  59     def open(self, flags):
  60     
  61         return self.file.open(QIODevice.OpenModeFlag(flags))
  62     
  63     def readAll(self):
  64     
  65         return str(self.file.readAll())
  66     
  67     readAll = pyqtProperty("QString", readAll)
  68     
  69     @pyqtSignature("close()")
  70     def close(self):
  71     
  72         self.file.close()
  73 
  74 class Browser(QWebView):
  75 
  76     def __init__(self, parent = None):
  77     
  78         QWebView.__init__(self, parent)
  79         self.connect(self, SIGNAL("loadFinished(bool)"), self.prepareJavaScript)
  80     
  81     def prepareJavaScript(self, ready):
  82     
  83         if not ready:
  84             return
  85         
  86         self.page().mainFrame().addToJavaScriptWindowObject("_QFile_factory", self)
  87         self.page().mainFrame().evaluateJavaScript(js)
  88     
  89     @pyqtSignature("createQFile(QString)")
  90     def createQFile(self, path):
  91     
  92         self.page().mainFrame().addToJavaScriptWindowObject("_wrapper", FileWrapper(path))
  93         return "_wrapper"
  94 
  95 
  96 if __name__ == "__main__":
  97 
  98     app = QApplication(sys.argv)
  99     browser = Browser()
 100     browser.setHtml(html)
 101     browser.show()
 102     sys.exit(app.exec_())
```
:::
::::
