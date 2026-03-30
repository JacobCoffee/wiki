#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def bind(objectName, propertyName, type):

    def getter(self):
        return type(self.findChild(QObject, objectName).property(propertyName).toPyObject())
    
    def setter(self, value):
        self.findChild(QObject, objectName).setProperty(propertyName, QVariant(value))
    
    return property(getter, setter)

class Window(QWidget):

    def __init__(self, parent = None):
    
        QWidget.__init__(self, parent)
        nameEdit = QLineEdit()
        nameEdit.setObjectName("nameEdit")
        addressEdit = QTextEdit()
        addressEdit.setObjectName("addressEdit")
        contactCheckBox = QCheckBox()
        contactCheckBox.setObjectName("contactCheckBox")
        
        layout = QFormLayout(self)
        layout.addRow(self.tr("Name:"), nameEdit)
        layout.addRow(self.tr("Address:"), addressEdit)
        layout.addRow(self.tr("Receive extra information:"), contactCheckBox)
    
    name = bind("nameEdit", "text", str)
    address = bind("addressEdit", "plainText", str)
    contact = bind("contactCheckBox", "checked", bool)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
