# PyQt/MathTran_Equation_Editor

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# MathTran Equation Editor 

## Introduction 

[MathTran](http://www.mathtran.org/) is a Web service that can be used to obtain images of equations written using the [TeX](http://www.tug.org/whatis.html) typesetting language. Equations can be embedded into Web pages using a clever JavaScript library that you embed into your pages - this converts the TeX markup written in the `src`{.backtick} attributes of image elements into requests to the MathTran service.

You can also write requests to the service directly in the `src`{.backtick} to obtain images in a static Web page, or use the same approach to obtain images in a desktop application. This is exactly what we do in this example.

![mathtran-equation-viewer.png](attachments/PyQt(2f)MathTran_Equation_Editor/mathtran-equation-viewer.png "mathtran-equation-viewer.png")

**Note:** You should read the [Terms of Use](http://www.mathtran.org/wiki/index.php/Terms_of_Use) of the MathTran service before using this example.

## Modules 

We use the `QtCore`{.backtick} and `QtGui`{.backtick} modules to provide the basic infrastructure and user interface for our utility.

    import sys
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtNetwork import *

Although the Python standard library has facilities for fetching data from Web services, we use the `QtNetwork`{.backtick} module to communicate with the MathTran server.

## The Window Class 

The `Window`{.backtick} class provides both the user interface for the utility and handles all communication with the server using a `QHttp`{.backtick} instance whose `done()`{.backtick} signal is connected to the `updateForm()`{.backtick} method.

    class Window(QWidget):

        def __init__(self, parent = None):
        
            QWidget.__init__(self, parent)
            
            self.http = QHttp()
            self.connect(self.http, SIGNAL("done(bool)"), self.updateForm)
            
            self.outputLabel = QLabel()
            self.outputLabel.setFrameShape(QFrame.StyledPanel)
            self.equationEditor = QTextEdit()
            
            buttonBox = QDialogButtonBox()
            self.clearButton = buttonBox.addButton(self.tr("&Clear"),
                QDialogButtonBox.ResetRole)
            self.updateButton = buttonBox.addButton(self.tr("&Update"),
                QDialogButtonBox.ApplyRole)
            
            self.connect(self.clearButton, SIGNAL("clicked()"), self.clearForm)
            self.connect(self.updateButton, SIGNAL("clicked()"), self.fetchImage)

The user interface itself is simple. We use a placeholder `QLabel`{.backtick} that will be used to display the images obtained from the server, the user enters text into a `QTextEdit`{.backtick} widget, and a `QDialogButtonBox`{.backtick} contains two buttons with custom titles. The **Clear** button is connected to the `clearForm()`{.backtick} method of the class, allowing the user to clear the current text and image. The **Update** button is connected to the `fetchImage()`{.backtick} method, and this is used to request a new image from the server.

            layout = QVBoxLayout()
            layout.addWidget(self.outputLabel, 1)
            layout.addWidget(self.equationEditor)
            layout.addWidget(buttonBox)
            self.setLayout(layout)
            
            self.setWindowTitle(self.tr("MathTran Equation Editor"))

The widgets are arranged vertically, with the label at the top, the text editor in the middle, and the buttons at the bottom. The window title is customized to show the name of the utility.

The `clearForm()`{.backtick} method simply gives the label an empty (null) pixmap to display; this has the effect of removing the previously displayed image.

        def clearForm(self):
        
            self.outputLabel.setPixmap(QPixmap())
            self.equationEditor.clear()

We clear the equation editor at the same time, allowing the user to enter a new equation.

The `fetchImage()`{.backtick} method sets up and transmits a new request to the server. This method does not receive the data returned by the server; the `updateForm()`{.backtick} method will handle the server\'s response.

Before we do anything else, we first ensure that the user is not able to interact with the parts of the user interface that cause actions to be triggered. We disable the buttons and make the text editor read only:

        def fetchImage(self):
        
            self.clearButton.setEnabled(False)
            self.updateButton.setEnabled(False)
            self.equationEditor.setReadOnly(True)

This ensures that the user cannot send another request while another one is pending.

We need to construct a request to the server in the appropriate format:

        http://mathtran.org/cgi-bin/mathtran?D=<size>;tex=<encoded TeX markup>

The following code constructs a URL using a `size`{.backtick} of 3 and ensures that the text entered by the user is correctly encoded for use:

            url = QUrl()
            url.setPath("/cgi-bin/mathtran")
            url.setQueryDelimiters("=", ";")
            url.addQueryItem("D", "3")
            url.addQueryItem("tex", str(QUrl.toPercentEncoding(
                             self.equationEditor.toPlainText())))

We use the `QHttp`{.backtick} object previously created to fetch the data at the URL we specified:

            self.http.setHost("mathtran.org")
            self.http.get(url.toString())

Note that the request is not synchronous - we do not receive the data immediately. When the data is available the `QHttp`{.backtick} object will emit the `done(bool)`{.backtick} signal. In the `__init__()`{.backtick} method, we connected this signal to the `updateForm()`{.backtick} method for the purpose of handling data returned from any requests we make.

The `updateForm()`{.backtick} method is called with an argument that indicates whether an error occurred during the transaction with the server.

        def updateForm(self, error):
        
            self.clearButton.setEnabled(True)
            self.updateButton.setEnabled(True)
            self.equationEditor.setReadOnly(False)

            if error:
                return

We re-enable the buttons and make the text editor writable again in any case, and return if an error occurred.

At this point, the server should have returned some data into the `QHttp`{.backtick} object, which holds it internally. We now extract this data using its `readAll()`{.backtick} method and attempt to load it into a `QImage`{.backtick} object, taking advantage of its ability to determine the image format from the data it is given.

            image = QImage()
            if not image.loadFromData(self.http.readAll()):
                return
            
            pixmap = QPixmap.fromImage(image)
            self.outputLabel.setPixmap(pixmap)

If the image data was valid, we convert the image to a pixmap and pass it to the label to display.

## Running the Application 

We add the standard `if`{.backtick} statement and suite to create a `QApplication`{.backtick} object and an instance of our `Window`{.backtick} class.

    if __name__ == "__main__":

        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec_())

Finally, we show the window and start the event loop.

## Further Developments 

A more flexible version of this example was written for the [Creating_GUI_Applications_with_PyQt_and_Qt_Designer](./Creating_GUI_Applications_with_PyQt_and_Qt_Designer.html) talk at PyCon UK 2007.
