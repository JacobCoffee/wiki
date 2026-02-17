# PyQt/QML callback function

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PyQt5 callback function 

This example code is available for download on [GitHub](https://github.com/ben-github/PyQt5-QML-CallbackFunction). This demo shows a QML calling a python function and passing a (QML) callback function as an argument. The python backend can then run the QML callback function. This can be useful for passing data from the python backend to the GUI and having the GUI be responsible for updating the graphical elements (via the callback function). Also, this can be used for non-blocking asynchronous updates of the GUI: By running the QML GUI in a separate thread as the python backend, The QML can request an update on data but not be blocking while that data is being obtained. While the QML GUI is running, python gets updated data over a slow link (REST query, serial port, etc) and once the data is ready, the callback function can be executed.

The code consists of three files. The shortest is the QML file which basically just loads the javascript to be run for the QML:

## main.qml

    import QtQuick 2.0
    import "application.js" as App

    Rectangle {
        id: appWindow
        width: 825
        height: 600
        color: '#000000'
        Component.onCompleted: App.onLoad()

The javascript to be loaded in contained in application.js:

## application.js

    function queueMe(response)
    {
        console.log('!!!!Defined Function Called: ' + response + "\n");
    }

    function onLoad()
    {
        console.log("onLoad start==================")

        ice.enqueue('#version 1', queueMe);
        ice.enqueue('#test', function test() { console.log('!!!! RAN ME TO ANONYMOUSE');});
        ice.enqueue('#asdft', function newtest(reply) { console.log('!!!! PASS DATA:    ' + reply + "\n");});
        console.log("     =========================")
        ice.processResponses();
        console.log("onLoad done==================")
    }

The ice prefixed functions are python functions. The onLoad() function runs ice.enqueue function which takes two arguments: string text and a callback function. As shown, you can pass either a function (1st enqueue) or an anonymous function (2nd enqueue). Additionally, the callback function can take an argument that python will provide (3rd enqueue).

The last file is the main python function main.py.

## main.py

    Skip to content
     This repository
    Explore
    Gist
    Blog
    Help
    ben-github ben-github
     
    1  Unwatch 
      Star 0
     Fork 0ben-github/PyQt5-QML-CallbackFunction
     branch: master  PyQt5-QML-CallbackFunction / main.py
    ben-githubben-github 11 days ago Merge commit '22b30d5'
    1 contributor
    52 lines (41 sloc)  1.475 kb RawBlameHistory  

    import sys
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtQuick import QQuickView
    from PyQt5.QtQml import QJSValue

    class iceController(QObject):
        def __init__(self):
            QObject.__init__(self)
            self.callback = []
            

        def dump(self):
            print('Dump was called')
            #print('Callback is %s' % self.callback)
            #print(dir(self.callback))
            #print('Callback is callable %s' % self.callback.isCallable)
            #print('Callback is callable %s' % self.callback.isCallable())
            for c in self.callback:
                c.call([QJSValue('asdf')])
            self.callback=[]
        @pyqtSlot(str, 'QJSValue')
        def enqueue(self, command, callback):
            print('Enqueuing function of %s' % command)
            #print('Test callback is %s' % callback)
            #print('Callback is callable?:  %s' % callback.isCallable())
            self.callback.append(QJSValue(callback))
            #self.callback = callback
            #self.dump()


        @pyqtSlot()
        def processResponses(self):
            print('processing responses')
            self.dump()

        @pyqtSlot(str)
        def log(self, s):
            print(s)

    print('Starting ICE Control GUI...')        
    app = QApplication(sys.argv)
    view = QQuickView()
    context = view.rootContext()

    ice = iceController()
    context.setContextProperty('PyConsole', ice)
    context.setContextProperty('ice', ice)

    view.setSource(QUrl("main.qml"))

Most of that code is just setting up a QML application. The enqueue function is what does most of the work. It needs the

    @pyqtSlot(str, 'QJSValue')

ahead of the function definition to tell it that the second argument to the function is an object of type QJSValue (which contains our QML callback function). The function just puts the callback function in a list, self.callback.

The other two functions to look at are processResponses and dump. processResponses is called by the application.js file and runs the dump. dump iterates over all elements in the self.callback list and calls them using the QJSValue method call. The functions are called with an argument of QJSValue(\'asdf\') which is just a string, but anything passed back to the QML must be of the type QJSValue.
