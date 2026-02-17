# PyQt/Using a Custom Protocol with QtWebKit

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Using a Custom Protocol with QtWebKit 

This example was written in response to [a message on the Python-list mailing list](http://mail.python.org/pipermail/python-list/2009-June/714967.html). It shows how to implement support for a new URL scheme in [WebKit](WebKit), so that additional protocols can be used with embedded browsers.

See [Adding the Gopher Protocol to QtWebKit](./PyQt(2f)Adding(20)the(20)Gopher(20)Protocol(20)to(20)QtWebKit.html) for a more complex example.

We begin by importing the PyQt4 modules and defining a simple HTML page:

    import sys

    from PyQt4.QtCore import QTimer, QVariant, SIGNAL
    from PyQt4.QtGui import *
    from PyQt4.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
    from PyQt4.QtWebKit import QWebView

    html = """<html>
    <head>
    <title>Test page for the download:// scheme</title>
    </head>
    <body>
    <h1>Downloads</h1>

    <a href="download://myfile">Download a file</a>

    <hr />
    <a href="http://www.google.com">A normal link</a>
    </body>
    </html>
    """

Custom data obtained by the application needs to be returned to the Web browser in custom QNetworkReply objects. We subclass QNetworkReply to create DownloadReply, a class which simply returns data held in a string.

Some QIODevice methods need to be reimplemented to ensure that the reply will be accepted by the browser. In particular, the readData() method performs the work of returning data to the browser, so it is important to ensure that this behaves correctly.

In the initialisation method, we queue an emission of the readyRead() signal. This tells the browser that the reply\'s data can be read. We need to queue the signal rather than emit it directly because, when the reply is being created, the browser does not yet know about it. Similarly, we queue an emission of the finished() signal to tell the browser that all the data is available for unbuffered reading.

    class DownloadReply(QNetworkReply):

        def __init__(self, parent, url, operation):
        
            QNetworkReply.__init__(self, parent)
            self.content = "<html><head><title>Test</title></head><body>This is a test.</body></html>"
            self.offset = 0
            
            self.setHeader(QNetworkRequest.ContentTypeHeader, QVariant("text/html; charset=ASCII"))
            self.setHeader(QNetworkRequest.ContentLengthHeader, QVariant(len(self.content)))
            QTimer.singleShot(0, self, SIGNAL("readyRead()"))
            QTimer.singleShot(0, self, SIGNAL("finished()"))
            self.open(self.ReadOnly | self.Unbuffered)
            self.setUrl(url)
        
        def abort(self):
            pass
        
        def bytesAvailable(self):
            # NOTE:
            # This works for Win:
            #      return len(self.content) - self.offset
            # but it does not work under OS X. 
            # Solution which works for OS X and Win:
            #     return len(self.content) - self.offset + QNetworkReply.bytesAvailable(self)
            return len(self.content) - self.offset
        
        def isSequential(self):
            return True
        
        def readData(self, maxSize):
        
            if self.offset < len(self.content):
                end = min(self.offset + maxSize, len(self.content))
                data = self.content[self.offset:end]
                self.offset = end
                return data

We need to ensure that we provide the correct headers with the data. In particular, since we are returning HTML for display, we need to include character set information with the content type and encode the data correctly in a string. (In this example, we use plain ASCII text, but we could start with a Unicode string and encode it as UTF-8.)

We also need to provide a custom NetworkAccessManager class that can return DownloadReply objects as required. This will be instantiated once and used to replace the default network access manager in the Web browser component.

The instance uses the same settings as the old manager, but provides a new implementation of the createRequest() method, which only uses the custom reply object when dealing with GET operations that involve the \"download\" scheme (for download:// URLs).

    class NetworkAccessManager(QNetworkAccessManager):

        def __init__(self, old_manager):
        
            QNetworkAccessManager.__init__(self)
            self.old_manager = old_manager
            self.setCache(old_manager.cache())
            self.setCookieJar(old_manager.cookieJar())
            self.setProxy(old_manager.proxy())
            self.setProxyFactory(old_manager.proxyFactory())
        
        def createRequest(self, operation, request, data):
        
            if request.url().scheme() != "download":
                return QNetworkAccessManager.createRequest(self, operation, request, data)
            
            if operation == self.GetOperation:
                # Handle download:// URLs separately by creating custom
                # QNetworkReply objects.
                reply = DownloadReply(self, request.url(), self.GetOperation)
                return reply
            else:
                return QNetworkAccessManager.createRequest(self, operation, request, data)

In the part of the example where we set up the application, we replace the existing network access manager with our custom version, taking care to keep the old manager around so that we can use it to dispatch requests for URL schemes that we don\'t handle.

    if __name__ == "__main__":

        app = QApplication(sys.argv)
        view = QWebView()
        
        old_manager = view.page().networkAccessManager()
        new_manager = NetworkAccessManager(old_manager)
        view.page().setNetworkAccessManager(new_manager)
        
        view.setHtml(html)
        view.show()
        sys.exit(app.exec_())
