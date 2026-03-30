#!/usr/bin/env python

import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui import *

app = QApplication([])
tableWidget = QTableWidget()
tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)

def openMenu(position):

    menu = QMenu()
    quitAction = menu.addAction("Quit")
    action = menu.exec_(tableWidget.mapToGlobal(position))
    if action == quitAction:
        qApp.quit()

tableWidget.customContextMenuRequested.connect(openMenu)
tableWidget.show()

sys.exit(app.exec_())
