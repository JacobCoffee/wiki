# PyQt/Playing a sound with QtMultimedia

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Playing a sound with QtMultimedia 

This example shows how to use the QAudioOutput class, introduced in Qt 4.6, to play a simple sine wave.

**Warning:** By default, the volume is set to zero because it is not possible to determine how loud the sound will be when played. Experiment carefully when playing sounds, especially if you are wearing headphones, to avoid causing damage to your hearing.

:::: 
::: 
``` 
   1 from math import pi, sin
   2 import struct, sys
   3 
   4 from PyQt4.QtCore import QBuffer, QByteArray, QIODevice, Qt
   5 from PyQt4.QtGui import QApplication, QFormLayout, QLineEdit, QHBoxLayout, \
   6                         QPushButton, QSlider, QVBoxLayout, QWidget
   7 from PyQt4.QtMultimedia import QAudio, QAudioDeviceInfo, QAudioFormat, QAudioOutput
   8 
   9 class Window(QWidget):
  10 
  11     def __init__(self, parent = None):
  12     
  13         QWidget.__init__(self, parent)
  14         
  15         format = QAudioFormat()
  16         format.setChannels(1)
  17         format.setFrequency(22050)
  18         format.setSampleSize(16)
  19         format.setCodec("audio/pcm")
  20         format.setByteOrder(QAudioFormat.LittleEndian)
  21         format.setSampleType(QAudioFormat.SignedInt)
  22         self.output = QAudioOutput(format, self)
  23         
  24         self.frequency = 440
  25         self.volume = 0
  26         self.buffer = QBuffer()
  27         self.data = QByteArray()
  28         
  29         self.deviceLineEdit = QLineEdit()
  30         self.deviceLineEdit.setReadOnly(True)
  31         self.deviceLineEdit.setText(QAudioDeviceInfo.defaultOutputDevice().deviceName())
  32         
  33         self.pitchSlider = QSlider(Qt.Horizontal)
  34         self.pitchSlider.setMaximum(100)
  35         self.volumeSlider = QSlider(Qt.Horizontal)
  36         self.volumeSlider.setMaximum(32767)
  37         self.volumeSlider.setPageStep(1024)
  38         
  39         self.playButton = QPushButton(self.tr("&Play"))
  40         
  41         self.pitchSlider.valueChanged.connect(self.changeFrequency)
  42         self.volumeSlider.valueChanged.connect(self.changeVolume)
  43         self.playButton.clicked.connect(self.play)
  44         
  45         formLayout = QFormLayout()
  46         formLayout.addRow(self.tr("Device:"), self.deviceLineEdit)
  47         formLayout.addRow(self.tr("P&itch:"), self.pitchSlider)
  48         formLayout.addRow(self.tr("&Volume:"), self.volumeSlider)
  49         
  50         buttonLayout = QVBoxLayout()
  51         buttonLayout.addWidget(self.playButton)
  52         buttonLayout.addStretch()
  53         
  54         horizontalLayout = QHBoxLayout(self)
  55         horizontalLayout.addLayout(formLayout)
  56         horizontalLayout.addLayout(buttonLayout)
  57     
  58     def changeFrequency(self, value):
  59     
  60         self.frequency = 440 + (value * 2)
  61     
  62     def play(self):
  63     
  64         if self.output.state() == QAudio.ActiveState:
  65             self.output.stop()
  66         
  67         if self.buffer.isOpen():
  68             self.buffer.close()
  69         
  70         self.createData()
  71         
  72         self.buffer.setData(self.data)
  73         self.buffer.open(QIODevice.ReadOnly)
  74         self.buffer.seek(0)
  75         
  76         self.output.start(self.buffer)
  77     
  78     def changeVolume(self, value):
  79     
  80         self.volume = value
  81     
  82     def createData(self):
  83     
  84         # Create 2 seconds of data with 22050 samples per second, each sample
  85         # being 16 bits (2 bytes).
  86         
  87         self.data.clear()
  88         for i in xrange(2 * 22050):
  89             t = i / 22050.0
  90             value = int(self.volume * sin(2 * pi * self.frequency * t))
  91             self.data.append(struct.pack("<h", value))
  92 
  93 
  94 if __name__ == "__main__":
  95 
  96     app = QApplication(sys.argv)
  97     window = Window()
  98     window.show()
  99     sys.exit(app.exec_())
```
:::
::::
