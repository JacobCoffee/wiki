# PyQt/Paint on an image

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Paint on an image 

On the `comp.lang.python`{.backtick} newsgroup (`python-list`{.backtick}), Laszlo Nagy asked for suggestions for a library to render antialiased images using [TrueType](./TrueType.html) font files.

Here is a hurriedly written program to do that ([source code](attachments/PyQt(2f)Paint(20)on(20)an(20)image/painttext.py "source code")).

![painttext.png](attachments/PyQt(2f)Paint(20)on(20)an(20)image/painttext.png "painttext.png")

:::: 
::: 
``` 
   1 import sys
   2 from PyQt4.QtCore import Qt
   3 from PyQt4.QtGui import *
   4 
   5 class Window(QWidget):
   6 
   7     def __init__(self, parent = None):
   8     
   9         QWidget.__init__(self, parent)
  10         
  11         self.label = QLabel()
  12         
  13         self.lineEdit = QLineEdit("ABCDE")
  14         self.fontComboBox = QFontComboBox()
  15         self.sizeSpinBox = QDoubleSpinBox()
  16         self.sizeSpinBox.setMinimum(1.0)
  17         self.sizeSpinBox.setValue(12.0)
  18         saveButton = QPushButton(self.tr("Save"))
  19         
  20         self.lineEdit.textChanged.connect(self.updateImage)
  21         self.fontComboBox.currentFontChanged.connect(self.updateImage)
  22         self.sizeSpinBox.valueChanged.connect(self.updateImage)
  23         saveButton.clicked.connect(self.saveImage)
  24         
  25         formLayout = QFormLayout()
  26         formLayout.addRow(self.tr("&Text:"), self.lineEdit)
  27         formLayout.addRow(self.tr("&Font:"), self.fontComboBox)
  28         formLayout.addRow(self.tr("Font &Size:"), self.sizeSpinBox)
  29         
  30         layout = QGridLayout()
  31         layout.addWidget(self.label, 0, 0, 1, 3, Qt.AlignCenter)
  32         layout.addLayout(formLayout, 1, 0, 1, 3)
  33         layout.addWidget(saveButton, 2, 1)
  34         self.setLayout(layout)
  35         
  36         self.updateImage()
  37         self.setWindowTitle(self.tr("Paint Text"))
  38     
  39     def updateImage(self):
  40     
  41         font = QFont(self.fontComboBox.currentFont())
  42         font.setPointSizeF(self.sizeSpinBox.value())
  43         metrics = QFontMetricsF(font)
  44         
  45         text = unicode(self.lineEdit.text())
  46         if not text:
  47             return
  48         
  49         rect = metrics.boundingRect(text)
  50         position = -rect.topLeft()
  51         
  52         pixmap = QPixmap(rect.width(), rect.height())
  53         pixmap.fill(Qt.white)
  54         
  55         painter = QPainter()
  56         painter.begin(pixmap)
  57         painter.setFont(font)
  58         painter.drawText(position, text)
  59         painter.end()
  60         
  61         self.label.setPixmap(pixmap)
  62     
  63     def saveImage(self):
  64     
  65         formats = QImageWriter.supportedImageFormats()
  66         formats = map(lambda suffix: u"*."+unicode(suffix), formats)
  67         path = unicode(QFileDialog.getSaveFileName(self, self.tr("Save Image"),
  68             "", self.tr("Image files (%1)").arg(u" ".join(formats))))
  69         
  70         if path:
  71             if not self.label.pixmap().save(path):
  72                 QMessageBox.warning(self, self.tr("Save Image"),
  73                     self.tr("Failed to save file at the specified location."))
  74 
  75 
  76 if __name__ == "__main__":
  77 
  78     app = QApplication(sys.argv)
  79     window = Window()
  80     window.show()
  81     sys.exit(app.exec_())
```
:::
::::
