# PyQt/Using_Python_Custom_Widgets_in_Qt_Designer

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Introduction 

Recent versions of [PyQt](PyQt) contain something special for developers who use [Qt Designer](http://doc.qt.digia.com/4.3/designer-manual.html) to design the user interfaces for their applications. In addition to the full range of standard Qt widgets, you can now install your own pure Python custom widgets and use them in your designs. All the signals, slots and properties defined in Python are accessible in Designer\'s user interface and behave just the same as for widgets written in C++.

## Background Information 

Qt Designer is a user interface design tool for Qt applications that makes it possible for non-programmers to create user interfaces for applications. In many respects, it separates the design of an application from its function, leaving designers in control of its look and feel and basic usability while developers write the underlying application logic.

Most of the standard Qt widgets are available to users of Qt Designer, and these can be used to create arbitrarily complex user interfaces. However, many applications are designed to use custom widgets and components, and these often need to be made available to designers. Fortunately, Qt Designer was written with this problem in mind, and there are two ways that custom widgets can be represented.

1.  Standard widgets can be *promoted* to act as placeholders for custom widgets. Since a custom widget\'s class is a subclass of a standard widget\'s class, that standard widget can be used as a placeholder.

2.  You can create custom widget plugins that Qt Designer loads at run time to allow custom widgets to be used directly in the user interface design process.

In C++, developers have to create an additional plugin class, based on QDesignerCustomWidgetInterface, that informs Qt Designer about the custom widget\'s name and which is used to create instances of it for use in forms created by the user. The custom widget and the plugin class are then compiled together to create a plugin that Qt Designer can load. The custom widget code is often compiled separately into applications that use forms which reference the custom widget.

In Python, an additional plugin class is also needed, but developers only need to put the modules containing the custom widget and plugin class on special paths so that Qt Designer can find them. Since the custom widget code does not need to be built or combined with the plugin code, very little extra work is required in order to make custom widgets work with Qt Designer.

## An Example Custom Widget 

The `PyAnalogClock`{.backtick} widget is a version of the [Analog Clock example](http://doc.trolltech.com/4.3/widgets-analogclock.html) supplied with Qt 4 and [PyQt4](PyQt4) which provides a property to allow the clock to show the time in different time zones, a slot to enable the time zone to be changed in response to signals from other components, and two signals of its own to report changes to the time and time zone.

![designer-analog-clock-shadow.png](attachments/PyQt(2f)Using_Python_Custom_Widgets_in_Qt_Designer/designer-analog-clock-shadow.png "designer-analog-clock-shadow.png")

Instead of quoting the example in full, we will only note the changes that need to be made to the Analog Clock example in order to integrate it with Qt Designer. Refer to the original example to see how the clock performs tasks such as painting and event handling.

### Adding Signals 

The first change we make to the original widget is to declare the signals the widget is able to emit. Normally, this isn\'t something that [PyQt](PyQt) widgets need to do --- arbitrary signals can be emitted at any time --- but Qt Designer needs to be know about the custom widget\'s signals so that it can connect them to slots in other widgets.

    class PyAnalogClock(QtGui.QWidget):

        __pyqtSignals__ = ("timeChanged(QTime)", "timeZoneChanged(int)")

We use the `__pyqtSignals__`{.backtick} class variable to define two signals that are used to inform other components of changes to the clock\'s time and time zone. The variable must refer to a sequence of strings - we could have used a list instead of a tuple, for example. Signals that are declared in this way are emitted in the same way as any other signal.

We change the class\'s `__init__()`{.backtick} method to define an attribute to hold the time zone and, as well as connecting the timer to the widget\'s `update()`{.backtick} slot, we also connect it to the newly added `updateTime()`{.backtick} method.

        def __init__(self, parent = None):

            QtGui.QWidget.__init__(self, parent)
            self.timeZoneOffset = 0

            timer = QtCore.QTimer(self)
            self.connect(timer, QtCore.SIGNAL("timeout()"), self, QtCore.SLOT("update()"))
            self.connect(timer, QtCore.SIGNAL("timeout()"), self.updateTime)
            timer.start(1000)

            # ...

        def updateTime(self):

            self.emit(QtCore.SIGNAL("timeChanged(QTime)"), QtCore.QTime.currentTime())

The `updateTime()`{.backtick} method simply emits the current time every second when a time out occurs.

The `timeZoneChanged()`{.backtick} signal is emitted whenever the user, or another component, changes the time zone property. This is shown in the following section.

### Adding a Property 

The `timeZone`{.backtick} property is implemented using the `getTimeZone()`{.backtick} getter method, the `setTimeZone()`{.backtick} setter method, and the `resetTimeZone()`{.backtick} method.

        def getTimeZone(self):

            return self.timeZoneOffset

The getter just returns the internal time zone value.

The `setTimeZone()`{.backtick} method is also defined to be a slot \-- we show this in the next section.

        def setTimeZone(self, value):

            if value != self.timeZoneOffset:
                self.timeZoneOffset = value
                self.emit(QtCore.SIGNAL("timeZoneChanged(int)"), value)
                self.update()

Note that we only change the internal `timeZoneOffset`{.backtick} attribute, emit the `timeZoneChanged()`{.backtick} signal and update the widget if the new value is different to the old one. It is especially important to avoid infinite loops with signal emissions --- for example, if we connected two clocks together to keep them in sync.

Qt\'s property system supports properties that can be reset to their original values. This method enables the `timeZone`{.backtick} property to be reset.

        def resetTimeZone(self):

            if self.timeZoneOffset != 0:
                self.timeZoneOffset = 0
                self.emit(QtCore.SIGNAL("timeZoneChanged(int)"), 0)
                self.update()

Again, we guard against unnecessary signal emission by ensuring that the time zone is not already zero before emitting the `timeZoneChanged()`{.backtick} signal and updating the widget.

Qt-style properties are defined differently to Python\'s properties. To declare a property, we call `pyqtProperty()`{.backtick} to specify the type and, in this case, getter, setter and resetter methods.

        timeZone = QtCore.pyqtProperty("int", getTimeZone, setTimeZone, resetTimeZone)

### Adding a Slot 

Since it may be useful to be able to update the clock\'s time zone from other input widgets, we want to make the `setTimeZone()`{.backtick} method a slot. Normally, we don\'t have to do anything special to use methods as slots with [PyQt](PyQt), but Qt Designer needs this information to allow users to select suitable slots when connecting components together.

We use the [standard decorator syntax](http://www.riverbankcomputing.com/Docs/PyQt4/pyqt4ref.html#the-qtcore-pyqtsignature-decorator) that is used to annotate methods for use with `pyuic4`{.backtick} and [PyQt4](PyQt4)\'s `uic`{.backtick} module. Here\'s the annotated `setTimeZone()`{.backtick} method:

        @QtCore.pyqtSignature("setTimeZone(int)")
        def setTimeZone(self, value):

            if value != self.timeZoneOffset:
                self.timeZoneOffset = value
                self.emit(QtCore.SIGNAL("timeZoneChanged(int)"), value)
                self.update()

The `@pyqtSignature`{.backtick} decorator is used to tell [PyQt](PyQt) which argument type the method expects, and is especially useful when you want to define slots with the same name that accept different argument types. This allows the method to be a Qt slot, which means that it can be found by Qt Designer (and other C++ components) via Qt\'s meta-object system.

## Defining the Widget\'s Plugin Interface 

Before the widget can be used in Qt Designer, we need to prepare another class that describes our custom widget and tells Qt Designer how to instantiate it. The approach used is the same as that used for C++ plugins; the only difference being that we derive our plugin class from a [PyQt](PyQt)-specific base class. Nonetheless, we must still implement the interface required of custom widget plugins, even if we use Python instead of C++ to do so.

The `__init__()`{.backtick} method is only used to set up the plugin and define its `initialized`{.backtick} attribute.

    from PyQt4 import QtGui, QtDesigner
    from analogclock import PyAnalogClock

    class PyAnalogClockPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

        def __init__(self, parent = None):

            QtDesigner.QPyDesignerCustomWidgetPlugin.__init__(self)

            self.initialized = False

The `initialize()`{.backtick} and `isInitialized()`{.backtick} methods allow the plugin to set up any required resources, ensuring that this can only happen once for each plugin.

        def initialize(self, core):

            if self.initialized:
                return

            self.initialized = True

        def isInitialized(self):

            return self.initialized

The `createWidget()`{.backtick} factory method creates new instances of our custom widget with the appropriate parent.

        def createWidget(self, parent):
            return PyAnalogClock(parent)

The `name()`{.backtick} method returns the name of the custom widget class that is provided by the plugin.

        def name(self):
            return "PyAnalogClock"

The `group()`{.backtick} method returns the name of the group in Qt Designer\'s widget box that the custom widget belongs to, and the `icon()`{.backtick} method returns the icon used to represent the custom widget in Qt Designer\'s widget box.

        def group(self):
            return "PyQt Examples"

        def icon(self):
            return QtGui.QIcon(_logo_pixmap)

The `_logo_pixmap`{.backtick} variable refers to a QPixmap object. This is created by including an ASCII XPM image in the source code as the `_logo_16x16_xpm`{.backtick} variable, and instantiating the QPixmap in the following way:

    _logo_pixmap = QtGui.QPixmap(_logo_16x16_xpm)

The `toolTip()`{.backtick} method returns a short description of the custom widget for use in a tool tip. The `whatsThis()`{.backtick} method returns a longer description of the custom widget for use in a \"What\'s This?\" help message.

        def toolTip(self):
            return ""

        def whatsThis(self):
            return ""

Qt Designer treats container widgets differently to other types of widget. If the custom widget is intended to be used as a container for other widgets, the `isContainer()`{.backtick} method should return `True`{.backtick}, and we would need to provide another plugin class in addition to this one if we wanted to add custom editing support for this widget.

        def isContainer(self):
            return False

Since our custom widget is not a specialized container widget, this method returns `False`{.backtick} instead.

The `domXml()`{.backtick} method returns an XML description of a custom widget instance that describes default values for its properties. Each custom widget created by this plugin will be configured using this description. The XML schema can be found at [http://doc.trolltech.com/designer-ui-file-format.html](http://doc.trolltech.com/designer-ui-file-format.html).

        def domXml(self):
            return (
                   '<widget class="PyAnalogClock" name=\"analogClock\">\n'
                   " <property name=\"toolTip\" >\n"
                   "  <string>The current time</string>\n"
                   " </property>\n"
                   " <property name=\"whatsThis\" >\n"
                   "  <string>The analog clock widget displays "
                   "the current time.</string>\n"
                   " </property>\n"
                   "</widget>\n"
                   )

Here, we provide tool tip and \"What\'s This?\" property values. These will be used for widgets placed on forms in Qt Designer.

The `includeFile()`{.backtick} method returns the module containing the custom widget class. It may include a module path in cases where the module is part of a Python package.

        def includeFile(self):
            return "analogclock"

## Extending a Qt widget while maintaining Designer features 

For example suppose you want to extend a `QStackedWidget`{.backtick} while maintaining useful designer features like the *Insert new page* menu. This is easily achieved by supplying a special XML structure (described [in the schema](http://doc.trolltech.com/designer-ui-file-format.html)) with the `domXML`{.backtick} method.

Key concept is the usage of `customWidgets`{.backtick} and `customWidget`{.backtick} elements and `extends`{.backtick} attribute of `customWidget`{.backtick}.

Here comes a full example: we are defining a new `CSlidingPanel`{.backtick} class which inherits `QStackedWidget`{.backtick}

        def domXml(self):
            return ("""
                <ui language="c++">
                    <widget class="CSlidingPanel" name="SlidingPanel">
                        <property name="toolTip">
                            <string>{0}</string>
                        </property>
                        <property name="whatsThis">
                            <string>{1}</string>
                        </property>
                        <property name="styleSheet">
                            <string>background-color: rgb(184, 184, 184);</string>
                        </property>
                    </widget>
                    <customwidgets>
                        <customwidget>
                            <class>CSlidingPanel</class>
                            <extends>QStackedWidget</extends>
                        </customwidget>
                   </customwidgets>
                </ui>""".format(self.toolTip(), self.whatsThis())
            )

## Using the Custom Widget in Qt Designer 

[PyQt4](PyQt4) includes a common plugin loader for Qt Designer that enables widgets written in Python, with corresponding plugin interfaces defined in the way shown above, to be automatically loaded by Qt Designer when it is run. However, in order for this to work, we need to place the modules containing the custom widget and its plugin class in the appropriate locations in the file system.

By default, modules containing plugin classes should be located in the `python`{.backtick} directory inside the directory containing the other Qt plugins for Qt Designer. For testing purposes, the `PYQTDESIGNERPATH`{.backtick} environment variable can be used to refer to the location of the modules containing the plugin classes.

The modules containing the custom widgets themselves only need to be located on one of the standard paths recognized by Python, and can therefore be installed in the user\'s `site-packages`{.backtick} directory, or the `PYTHONPATH`{.backtick} environment variable can be set to refer to their location.
