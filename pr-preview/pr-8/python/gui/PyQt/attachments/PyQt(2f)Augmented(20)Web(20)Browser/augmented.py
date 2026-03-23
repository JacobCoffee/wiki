#!/usr/bin/env python

"""
augmented.py - Demonstrates how to call WebKit's JavaScript objects from Python
               and call Python objects from JavaScript.

This file is part of the PyQt for Desktop and Embedded Devices package.

Copyright (C) 2009 David Boddie <david.boddie@nokia.com>
Copyright (c) 2009 Nokia Corporation and/or its subsidiary(-ies).
All rights reserved.

Contact: Nokia Corporation (qt-info@nokia.com)

You may use this file under the terms of the BSD license as follows:

"Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
 * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor the names
   of its contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
 FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
"""

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *


js = \
"""findAnchors = function()
{
    findAnchorsInNode(document, 0);
}

findAnchorsInNode = function(parent)
{
    var children = parent.childNodes;
    
    for (var i = 0; i < children.length; i++) {
        var child = children[i];
        if (child.nodeName == "A") {
            if (child.hasAttributes()) {
                var attributes = child.attributes;
                for (var j = 0; j < attributes.length; j++) {
                    if (attributes[j].nodeName == "name") {
                        var following = findFollowing(child);
                        anchorList.addHeading(following.nodeName, attributes[j].nodeValue, getAnchorText(following));
                    }
                }
            }
        } else if (child.hasChildNodes()) {
            findAnchorsInNode(child);
        }
    }
}

findFollowing = function(anchor)
{
    var next = anchor.nextSibling;
    while (next && next.nodeType != Node.ELEMENT_NODE)
        next = next.nextSibling;
    
    return next;
}

getAnchorText = function(parent)
{
    var children = parent.childNodes;
    var text = "";
    
    for (var i = 0; i < children.length; i++) {
        var child = children[i];
        if (child.nodeType == Node.TEXT_NODE)
            text = text + child.nodeValue;
        else if (child.hasChildNodes())
            text = text + findAnchorText(child);
    }
    
    return text;
}
"""

class Browser(QMainWindow):

    default_url = QUrl("http://doc.qt.nokia.com/4.5/qt4-5-intro.html")
    
    def __init__(self, parent = None):
    
        QMainWindow.__init__(self, parent)
        
        fileMenu = QMenu(self.tr("&File"), self)
        newAction = fileMenu.addAction(self.tr("&New Document"))
        newAction.setShortcut(QKeySequence(QKeySequence.New))
        self.connect(newAction, SIGNAL("triggered()"), self.newDocument)
        exitAction = fileMenu.addAction(self.tr("E&xit"))
        exitAction.setShortcut(QKeySequence(self.tr("Ctrl+Q")))
        self.connect(exitAction, SIGNAL("triggered()"), self.close)
        self.menuBar().addMenu(fileMenu)
        
        toolbar = QToolBar(self.tr("Document"), self)
        self.documentCombo = QComboBox()
        self.documentCombo.currentIndexChanged.connect(self.openDocument)
        self.addressEdit = QLineEdit()
        self.addressEdit.returnPressed.connect(self.openUrl)
        toolbar.addWidget(QLabel(self.tr("Document:")))
        toolbar.addWidget(self.documentCombo)
        toolbar.addWidget(QLabel(self.tr("Address:")))
        toolbar.addWidget(self.addressEdit)
        self.addToolBar(toolbar)
        
        headingsDockWindow = QDockWidget(self.tr("Headings"), self)
        headingsDockWindow.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.headingsList = QTreeView()
        self.headingsList.setHeaderHidden(True)
        self.headingsModel = QStandardItemModel()
        self.headingsList.setModel(self.headingsModel)
        headingsDockWindow.setWidget(self.headingsList)
        self.addDockWidget(Qt.LeftDockWidgetArea, headingsDockWindow)
        
        self.headingsList.clicked.connect(self.goToAnchor)
        
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)
        self.newDocument()
    
    def newDocument(self, url = default_url):
    
        self.documentCombo.addItem(url.toString())
        webview = QWebView()
        webview.setUrl(url)
        webview.titleChanged.connect(self.updateDocumentTitle)
        webview.loadFinished.connect(self.prepareJavaScript)
        
        index = self.stackedWidget.addWidget(webview)
        self.documentCombo.setCurrentIndex(index)
        self.updateAddress()
    
    def updateAddress(self):
    
        url = self.stackedWidget.currentWidget().url()
        self.addressEdit.setText(url.toString())
    
    def openDocument(self, index):
    
        self.stackedWidget.setCurrentIndex(index)
        widget = self.stackedWidget.currentWidget()
        if widget:
            self.updateAddress()
            self.listHeadings(widget)
    
    def openUrl(self):
    
        text = self.addressEdit.text()
        self.stackedWidget.currentWidget().setUrl(QUrl(text))
    
    def updateDocumentTitle(self, title):
    
        index = self.stackedWidget.indexOf(self.sender())
        self.documentCombo.setItemText(index, title)
        self.updateAddress()
    
    def prepareJavaScript(self, success):
    
        if not success:
            return
        
        if self.sender() != self.stackedWidget.currentWidget():
            return
        
        webview = self.sender()
        webview.page().mainFrame().addToJavaScriptWindowObject("anchorList", self)
        webview.page().mainFrame().evaluateJavaScript(js)
        self.listHeadings(webview)
    
    def listHeadings(self, webview):
    
        self.headingsModel.clear()
        webview.page().mainFrame().evaluateJavaScript("findAnchors();")
    
    @pyqtSignature("addHeading(QString, QString, QString)")
    def addHeading(self, nodeName, name, title):
    
        if str(nodeName) not in ("H1", "H2", "H3", "H4", "H5", "H6"):
            return
        
        webview = self.stackedWidget.currentWidget()
        url = webview.page().mainFrame().url()
        url.setFragment(name)
        
        level = int(str(nodeName)[1])
        newItem = QStandardItem(title)
        newItem.setData(QVariant(url), Qt.UserRole)
        newItem.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        
        parent = self.headingsModel
        i = 1
        while i < level:
            if parent.rowCount() == 0:
                item = QStandardItem("[%i]" % i)
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                parent.appendRow(item)
            elif parent == self.headingsModel:
                item = parent.item(parent.rowCount() - 1, 0)
            else:
                item = parent.child(parent.rowCount() - 1, 0)
            parent = item
            self.headingsList.setExpanded(parent.index(), True)
            i += 1
        
        parent.appendRow(newItem)
    
    def goToAnchor(self, index):
    
        url = index.data(Qt.UserRole).toUrl()
        if url.isValid():
            webview = self.stackedWidget.currentWidget()
            webview.load(url)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
