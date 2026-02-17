# PyQt/SampleCode

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page contains links to some useful code snippets. Longer, more detailed code examples can be found via the [Overviews_and_Guides](./Overviews_and_Guides.html) page.

**Put any code snippet for PyKDE and PyQt that you find useful here. If the code is longer than one screen at normal point size, it might be better if you provide a rationale and a link, or just put it on a separate page.**

## PyQt 5 

- [QML callback function](QML callback function): How to pass and execute callback functions with QML.

- [Threading, Signals and Slots](../PyQt5/Threading,_Signals_and_Slots): How to perform work in one thread and use the result in another.

## PyQt 4 

- [Decoding Japanese Text](Decoding_Japanese_Text): The response to a posting on comp.lang.python, asking about decoding text for display in a GUI.

- [Screenshots](http://home.tampabay.rr.com/dataheli/) of various database and 3D graphics widgets, with code to follow soon. **\[dead link!\]**

- [Using GStreamer with PyQt](Using GStreamer with PyQt): How to use the GStreamer bindings for Python with PyQt (see [Multimedia Resources](Multimedia_Resources) for more multimedia links).

### Infrastructure 

- [Threading, Signals and Slots](Threading,_Signals_and_Slots): How to perform work in one thread and use the result in another. (Qt 4)

- [PyQt/AutoConnectingSlots](AutoConnectingSlots): How to have the signals of widgets automatically connected to Python defined slots.

- [Handling Qt\'s internal item MIME type](Handling Qt's internal item MIME type): How to implement a drop handler in a model to handle items dragged from standard models.

- [Handling an internal Qt MIME type](Handling an internal Qt MIME type): How to handle the internal MIME type used for drag and drop between item views.

- [Binding widget properties to Python variables](Binding widget properties to Python variables): Using Python\'s property system to access Qt properties and bind them to variables.

- [Making non-clickable widgets clickable](Making non-clickable widgets clickable): How to misuse event filters to add `clicked()`{.backtick} signals to widgets.

- [Undo and redo with line edits](Undo and redo with line edits): An incomplete example showing basic undo/redo handling.

- [Using a signal mapper](Using a signal mapper): How to associate values with signals from many widgets and use one slot to handle them all.

- [Sending Python values with signals and slots](Sending Python values with signals and slots): How to communicate Python values via Qt\'s signals and slots mechanism.

- [Using a translation of Qt](Using a translation of Qt): How to display standard dialogs and messages in your local language.

- [Getting the version numbers of Qt, SIP and PyQt](./PyQt(2f)Getting(20)the(20)version(20)numbers(20)of(20)Qt(2c20)SIP(20)and(20)PyQt.html): How to obtain the version information for the Qt-related modules you are using.

- [Writing a client for a zeromq service](Writing a client for a zeromq service): How to access a zeromq service while keeping the GUI responsive.

### Painting 

- [Drawing highlighted rows in a calendar widget](Drawing highlighted rows in a calendar widget): How to highlight the current week in a QCalendarWidget subclass.

- [Windows with gradient backgrounds](Windows with gradient backgrounds): How to change the background colour of a window to use a gradient instead of the standard colour in the palette.

- [Fading Between Widgets](Fading Between Widgets): How to create a stacked widget that fades between widgets on different pages.

- [Fading and unfading a widget with a delay](Fading and unfading a widget with a delay): How to produce a simple fade-unfade animation.

- [Paint on an image](Paint on an image): How to paint text and graphics on an image.

- [Painting and clipping demonstration](Painting and clipping demonstration): A demonstration showing how to clip what a painter draws on a widget.

- [Clipping SVG output](Clipping SVG output): How to clip Scalable Vector Graphics (SVG) output when drawing with QPainter.

- [GraphicsView\_-\_SimpleAnimation](GraphicsView_-_SimpleAnimation): How to construct a very simple animation using QGraphicsView, QGraphicsItem, QGraphicsItemAnimation and QTimeLine. (Qt4)

- [Python syntax highlighting](Python syntax highlighting): How to add syntax highlighting to a QPlainTextEdit widget. (Qt4)

- [Painting an overlay on an image](Painting an overlay on an image): How to paint one image onto another.

- [Movie splash screen](Movie splash screen): How to paint a movie on a splash screen instead of a static image.

- [Extend Two QPixmap](Extend Two QPixmap): How to paint merge two QPixmaps into one QPixmap.

### Widgets 

- [Widgets in a layout](Widgets in a layout): How to create widgets and put them in a layout.

- [Show an image using a label](Show an image using a label): How to display an image.

- [A full widget waiting indicator](A full widget waiting indicator): How to draw a busy/waiting indicator over an entire widget.

- [Handling context menus](Handling context menus): The different ways you can handle context menus.

- [Five minute steps in a QTimeEdit](Five minute steps in a QTimeEdit): Customise the behaviour of QTimeEdit by subclassing.

- [Customising tab bars](Customising tab bars): How to change the size allocated to tabs in tab bars and tab widgets.

- [Customising a tab to contain a menu](Customising a tab to contain a menu): How to put a menu button in a tab bar.

- [Adding auto-completion to a QLineEdit](Adding auto-completion to a QLineEdit): How to use a QStringListModel to provide data for auto-completion.

- [Adding tab-completion to a QLineEdit](Adding tab-completion to a QLineEdit): How to handle key events to enable tab-completion.

- [Adding custom signals to a simple painted widget](Adding custom signals to a simple painted widget): How to declare and use custom signals.

- [Creating a widget with a fixed aspect ratio](Creating a widget with a fixed aspect ratio): How to ensure that a widget keeps a certain aspect ratio when it is resized.

- [Compass widget](Compass widget): A simple custom widget, showing how to handle paint events.

- [Adding a background image to an MDI area](Adding a background image to an MDI area): How to display a non-tiled image in the background of an MDI area widget.

- [Selecting a region of a widget](Selecting a region of a widget): How to use a QRubberBand to select part of a widget.

- [Distinguishing between click and double click](Distinguishing between click and double click): How to handle a double click without acting on the first click.

### Item Views 

- [Using a different view with QComboBox](Using a different view with QComboBox): How to replace the standard view used for a combo box\'s pop-up menu.

- [Sorting numbers in columns](Sorting numbers in columns): How to sort a table by the numbers in a given column.

- [Animated items using delegates](Animated items using delegates): How to animate items in a list view, using a custom delegate, timer events and a signal.

- [Animated items using delegates and movies](Animated items using delegates and movies): How to animate items in a list view - an improved version of the previous example.

- [Adding items to a list widget](Adding items to a list widget): How to add items to a QListWidget instance.

- [A custom Python class-based 1D model](A custom Python class-based 1D model): A drag and drop-enabled model which holds Python objects.

- [Reading selections from a selection model](Reading selections from a selection model): How to read selections and update an underlying model.

- [Creating a context menu for a tree view](Creating a context menu for a tree view): How to determine the level of nesting in a tree view and create an appropriate menu.

- [Selecting items in unrelated views](Selecting items in unrelated views): How to use selection models to relate items in views with different models.

- [Showing a subset of a model in a view](Showing a subset of a model in a view): How to show a model in one view while showing a subset of the same model in another view.

### WebKit 

- [Using a Custom Protocol with QtWebKit](Using a Custom Protocol with QtWebKit): How to add support for a custom protocol to an embedded Web browser.

- [Embedding Widgets in Web Pages](Embedding Widgets in Web Pages): How to embed widgets written in Python into Web pages shown with QWebView.

- [Exposing Qt Classes to QtWebKit](Exposing Qt Classes to QtWebKit): How to wrap Qt classes and expose them to an embedded Web browser.

- [Augmented Web Browser](Augmented Web Browser): A Web browser with a side panel that shows a table of contents for the document being displayed.

### Multimedia 

- [Playing a sound with QtMultimedia](Playing a sound with QtMultimedia): How to use QAudioOutput to play a sound.

### Drag and Drop 

- [Exporting a file to other applications](Exporting a file to other applications): How to drag data as a file for other applications to load.

### Databases 

- [Removing a database](Removing a database): How to remove a database and optionally reload it again without getting warnings from Qt.

### Qt Designer and uic 

- [Previewing a form](Previewing a form): How to load and display a form created in Qt Designer.

## PyQt 3 

*Note: [PyQt](PyQt) 3 examples were not transferred from the old PyQt Wiki.*

- [CustomListViewItems](./CustomListViewItems.html): How to customize the painting of list view items. (Qt 3)

- [ListBoxAndListViewIterators](./ListBoxAndListViewIterators.html): How to loop over all items in list boxes and list views. (Qt 3)

- [DragAndDropWithPyQt](./DragAndDropWithPyQt.html): How to make use of drag and drop without subclassing. (Qt 3)

- [CreatingMdiApplications](./CreatingMdiApplications.html): Some links and pointers for MDI development. (Qt 3)

- [Wrapper_For_QWidgetFactory](./Wrapper_For_QWidgetFactory.html): How to set up the slot connections automatically in [PyQt](PyQt). (Qt 3)

- [LoadingUIFilesAtRuntime](./LoadingUIFilesAtRuntime.html): How to load classes (as opposed to instances) directly from UI files, at runtime. (Qt 3)

- [SimpleQScintillaExample](./SimpleQScintillaExample.html): a simple demonstration of QScintilla use with [PyQt](PyQt). (Qt 3)

- [SignalDecorator](./SignalDecorator.html): a decorator that provides the signal signature for a method. (Qt 3)

- [ScrollableGroupBox](./ScrollableGroupBox.html): A simple way to get a scrollable groupbox. (Qt 3)

- [Capturing_Output_from_a_Process](./Capturing_Output_from_a_Process.html): How to capture output from a process and show it in a text editor/browser. (Qt 3)

- [Printing_a_Worksheet](./Printing_a_Worksheet.html): How to print the contents of a worksheet onto a single page of A4 paper. (Qt 3)
