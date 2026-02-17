# PyQt/Embedding Widgets in Web Pages

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Embedding Widgets in Web Pages 

This example was written in preparation for the [Plugging into the Web](http://doc.qt.digia.com/qq/qq26-webplugin.html) article for Qt Quarterly 26 and posted here in response to [a message on the Python-list mailing list](http://www.riverbankcomputing.com/pipermail/pyqt/2009-June/023306.html).

We begin by importing the [PyQt4](PyQt4) modules and defining a simple HTML page:

    import sys
    from PyQt4.QtCore import QSize, Qt
    from PyQt4.QtGui import *
    from PyQt4.QtWebKit import *

    html = \
    """<html>
    <head>
    <title>Python Web Plugin Test</title>
    </head>

    <body>
    <h1>Python Web Plugin Test</h1>
    <object type="x-pyqt/widget" width="200" height="200"></object>
    <p>This is a Web plugin written in Python.</p>
    </body>
    </html>
    """

Note the use of the `object`{.backtick} tag with a custom `type`{.backtick} attribute. This refers to a custom MIME type that we will register later on with QtWebKit.

The widget we want to embed in Web pages is a simple custom widget that implements a paint event and provides a size hint:

    class WebWidget(QWidget):

        def paintEvent(self, event):
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(Qt.white)
            painter.setPen(Qt.black)
            painter.drawRect(self.rect().adjusted(0, 0, -1, -1))
            painter.setBrush(Qt.red)
            painter.setPen(Qt.NoPen)
            painter.drawRect(self.width()/4, self.height()/4,
                             self.width()/2, self.height()/2)
            painter.end()
        
        def sizeHint(self):
            return QSize(100, 100)

To make the widget available for embedding, we need to register it with QtWebKit. There are two ways to do this:

- Create a subclass QWebPage and reimplement the createPlugin() method, then pass an instance of this class to a QWebView object.
- Create a subclass QWebPluginFactory and register an instance of it with an existing QWebPage object.

Here, we create a custom subclass of QWebPluginFactory and reimplement the create() method to return an instance of our custom widget when asked for the MIME type we wish to associate with it:

    class WebPluginFactory(QWebPluginFactory):

        def __init__(self, parent = None):
            QWebPluginFactory.__init__(self, parent)
        
        def create(self, mimeType, url, names, values):
            if mimeType == "x-pyqt/widget":
                return WebWidget()
        
        def plugins(self):
            plugin = QWebPluginFactory.Plugin()
            plugin.name = "PyQt Widget"
            plugin.description = "An example Web plugin written with PyQt."
            mimeType = QWebPluginFactory.MimeType()
            mimeType.name = "x-pyqt/widget"
            mimeType.description = "PyQt widget"
            mimeType.fileExtensions = []
            plugin.mimeTypes = [mimeType]
            print "plugins"
            return [plugin]

We also need to reimplement the plugins() method to inform QtWebKit about the MIME type we support with our custom widget. We can provide implementations for create() and plugins() that register and create many custom widgets.

In the main program, we enable plugins globally for the application, set our own factory on the default QWebPage instance provided by the QWebView widget, and we set the HTML for the widget to show.

    if __name__ == "__main__":

        app = QApplication(sys.argv)
        QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True)
        view = QWebView()
        factory = WebPluginFactory()
        view.page().setPluginFactory(factory)
        view.setHtml(html)
        view.show()
        sys.exit(app.exec_())

The result should be a page containing a title and a simple decorated widget.
