# PyQt/Adding the Gopher Protocol to QtWebKit

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Adding the Gopher Protocol to QtWebKit 

    import os, sys

    from PyQt4.QtCore import QObject, QTimer, QUrl, QVariant, SIGNAL
    from PyQt4.QtGui import *
    from PyQt4.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply, QTcpSocket
    from PyQt4.QtWebKit import QWebView

    class Downloader(QObject):

        def __init__(self, parent = None):
        
            QObject.__init__(self, parent)
            self.path = u""
        
        def saveFile(self, reply):
        
            fileName = unicode(reply.url().path()).split(u"/")[-1]
            if self.path:
                fileName = os.path.join(self.path, fileName)
            
            path = unicode(QFileDialog.getSaveFileName(self.parent(),
                self.tr("Save File"), fileName))
            
            if path:
                try:
                    open(unicode(path), "w").write(str(reply.readAll()))
                    self.path = os.path.split(path)[0]
                except IOError:
                    QMessageBox.warning(self.parent(), self.tr("Download Failed"),
                        self.tr("Failed to save the file."))


    class GopherReply(QNetworkReply):

        def __init__(self, url):
        
            QNetworkReply.__init__(self)
            self.gopher = QTcpSocket()
            self.gopher.bytesWritten.connect(self.writeGopherData)
            self.gopher.readyRead.connect(self.readGopherData)
            self.gopher.connected.connect(self.getResource)
            self.gopher.disconnected.connect(self.setContent)
            
            self.input = ""
            self.output = ""
            
            self.content = ""
            self.offset = 0
            
            self.setUrl(url)
            self.gopher.connectToHost(url.host(), 70)
        
        def getResource(self):
        
            path = self.url().path()
            if path.isEmpty() or path == u"/":
                self.output = "\r\n"
            else:
                self.output = str(path) + "\r\n"
            
            self.writeGopherData()
        
        def readGopherData(self):
        
            self.input += str(self.gopher.readAll())
        
        def writeGopherData(self, written = 0):
        
            self.output = self.output[written:]
            if self.output:
                self.gopher.write(self.output)
        
        def html(self, text):
        
            return unicode(text).replace(u"&", u"&amp;").replace(u"<", u"&lt;").replace(u">", u"&gt;")
        
        def setContent(self):
        
            if self.url().hasQueryItem(u"type"):
                self.setContentData()
            else:
                self.setContentList()
        
        def setContentData(self):
        
            self.open(self.ReadOnly | self.Unbuffered)
            if self.url().queryItemValue(u"type") == u"text":
                self.setHeader(QNetworkRequest.ContentTypeHeader,
                               QVariant("text/plain"))
            
            self.content = self.input
            self.setHeader(QNetworkRequest.ContentLengthHeader,
                           QVariant(len(self.content)))
            self.readyRead.emit()
            self.finished.emit()
        
        def setContentList(self):
        
            url = QUrl(self.url())
            if not url.path().endsWith(u"/"):
                url.setPath(url.path() + u"/")
            
            base_url = self.url().toString()
            base_path = unicode(url.path())
            
            self.open(self.ReadOnly | self.Unbuffered)
            content = (
                u"<html>\n"
                u"<head>\n"
                u"  <title>" + self.html(base_url) + u"</title>\n"
                u'  <style type="text/css">\n'
                u"  th { background-color: #aaaaaa;\n"
                u"       color: black }\n"
                u"  table { border: solid 1px #aaaaaa }\n"
                u"  tr.odd { background-color: #dddddd;\n"
                u"           color: black\n }\n"
                u"  tr.even { background-color: white;\n"
                u"           color: black\n }\n"
                u"  </style>\n"
                u"</head>\n\n"
                u"<body>\n"
                u"<h1>Listing for " + base_path + u"</h1>\n\n"
                )
            
            lines = self.input.splitlines()
            
            for line in lines:
            
                pieces = line.split("\t")
                if pieces == ["."]:
                    break
                try:
                    type, path, host, port = pieces[:4]
                except ValueError:
                    # This isn't a listing. Let's try returning data instead.
                    self.setContentData()
                    return
                
                if type[0] == "i":
                    content += u"<p>" + self.html(type[1:]) + u"</p>"
                elif type[0] == "h" and path.startswith(u"URL:"):
                    content += u"<p><a href=\""+path[4:]+u"\">"+self.html(type[1:])+u"</a></p>"
                elif type[0] == "0":
                    content += u"<p><a href=\"gopher://"+host+u":"+port+path+u"?type=text\">"+self.html(type[1:])+u"</a></p>"
                elif type[0] == "1":
                    content += u"<p><a href=\"gopher://"+host+u":"+port+path+u"\">"+self.html(type[1:])+u"</a></p>"
                elif type[0] == "4":
                    content += u"<p><a href=\"gopher://"+host+u":"+port+path+u"?type=binhex\">"+self.html(type[1:])+u"</a></p>"
                elif type[0] == "5":
                    content += u"<p><a href=\"gopher://"+host+u":"+port+path+u"?type=dos\">"+self.html(type[1:])+u"</a></p>"
                elif type[0] == "6":
                    content += u"<p><a href=\"gopher://"+host+u":"+port+path+u"?type=uuencoded\">"+self.html(type[1:])+u"</a></p>"
                elif type[0] == "9":
                    content += u"<p><a href=\"gopher://"+host+u":"+port+path+u"?type=binary\">"+self.html(type[1:])+u"</a></p>"
                elif type[0] == "g":
                    content += u"<img src=\"gopher://"+host+u":"+port+path+u"?type=binary\">"+self.html(type[1:])+u"</img>"
                elif type[0] == "I":
                    content += u"<img src=\"gopher://"+host+u":"+port+path+u"?type=binary\">"+self.html(type[1:])+u"</img>"
            
            content += (
                u"</body>\n"
                u"</html>\n"
                )
            
            self.content = content.encode("utf-8")
            
            self.setHeader(QNetworkRequest.ContentTypeHeader, QVariant("text/html; charset=UTF-8"))
            self.setHeader(QNetworkRequest.ContentLengthHeader, QVariant(len(self.content)))
            self.readyRead.emit()
            self.finished.emit()
        
        # QIODevice methods
        
        def abort(self):
            pass
        
        def bytesAvailable(self):
            return len(self.content) - self.offset
        
        def isSequential(self):
            return True
        
        def readData(self, maxSize):
        
            if self.offset < len(self.content):
                end = min(self.offset + maxSize, len(self.content))
                data = self.content[self.offset:end]
                self.offset = end
                return data


    class NetworkAccessManager(QNetworkAccessManager):

        def __init__(self, old_manager):
        
            QNetworkAccessManager.__init__(self)
            self.setCache(old_manager.cache())
            self.setCookieJar(old_manager.cookieJar())
            self.setProxy(old_manager.proxy())
            self.setProxyFactory(old_manager.proxyFactory())
        
        def createRequest(self, operation, request, device):
        
            if request.url().scheme() != "gopher":
                return QNetworkAccessManager.createRequest(self, operation, request, device)
            
            if operation == self.GetOperation:
                # Handle gopher:// URLs separately by creating custom QNetworkReply
                # objects.
                reply = GopherReply(request.url())
                return reply
            else:
                return QNetworkAccessManager.createRequest(self, operation, request, device)


    class Window(QWidget):

        def __init__(self, parent = None):
        
            QWidget.__init__(self, parent)
            
            self.addressEdit = QLineEdit()
            # gopher://mirror.lug.udel.edu:70
            self.addressEdit.setText("gopher://hal3000.cx:70")
            self.view = QWebView()
            
            old_manager = self.view.page().networkAccessManager()
            self.new_manager = NetworkAccessManager(old_manager)
            self.view.page().setNetworkAccessManager(self.new_manager)
            
            self.view.page().setForwardUnsupportedContent(True)
            self.downloader = Downloader(self)
            self.view.page().unsupportedContent.connect(self.downloader.saveFile)
            
            self.view.setUrl(QUrl(self.addressEdit.text()))
            
            self.addressEdit.returnPressed.connect(self.setUrl)
            self.view.urlChanged.connect(self.updateAddress)
            
            layout = QVBoxLayout(self)
            layout.addWidget(self.addressEdit)
            layout.addWidget(self.view)
        
        def setUrl(self):
            self.view.setUrl(QUrl(self.addressEdit.text()))
        
        def updateAddress(self, url):
            self.addressEdit.setText(url.toString())


    if __name__ == "__main__":

        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec_())
