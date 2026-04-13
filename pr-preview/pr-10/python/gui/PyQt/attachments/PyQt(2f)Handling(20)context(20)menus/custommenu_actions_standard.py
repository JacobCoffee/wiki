#!/usr/bin/env python

import sys
from PyQt4.QtCore import Qt
from PyQt4.QtGui import *

app = QApplication([])
tableWidget = QTableWidget()
tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)

quitAction = QAction("Quit", None)
quitAction.triggered.connect(qApp.quit)
tableWidget.addAction(quitAction)

tableWidget.show()
sys.exit(app.exec_())
