# PyQt/SampleCode

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page contains links to some useful code snippets. Longer, more detailed code examples can be found via the [Overviews_and_Guides](./Overviews_and_Guides.html) page.

**Put any code snippet for PyKDE and PyQt that you find useful here. If the code is longer than one screen at normal point size, it might be better if you provide a rationale and a link, or just put it on a separate page.**

## PyQt 5 

- [QML callback function](QML%20callback%20function): How to pass and execute callback functions with QML.

- [Threading, Signals and Slots](../PyQt5/Threading,_Signals_and_Slots): How to perform work in one thread and use the result in another.

## PyQt 4 

- [Decoding Japanese Text](Decoding_Japanese_Text): The response to a posting on comp.lang.python, asking about decoding text for display in a GUI.

- [Screenshots](http://home.tampabay.rr.com/dataheli/) of various database and 3D graphics widgets, with code to follow soon. **\[dead link!\]**

- [Using GStreamer with PyQt](Using%20GStreamer%20with%20PyQt): How to use the GStreamer bindings for Python with PyQt (see [Multimedia Resources](Multimedia_Resources) for more multimedia links).

### Infrastructure 

- [Threading, Signals and Slots](Threading,_Signals_and_Slots): How to perform work in one thread and use the result in another. (Qt 4)

- [PyQt/AutoConnectingSlots](AutoConnectingSlots): How to have the signals of widgets automatically connected to Python defined slots.

- [Handling Qt\'s internal item MIME type](Handling%20Qt's%20internal%20item%20MIME%20type): How to implement a drop handler in a model to handle items dragged from standard models.

- [Handling an internal Qt MIME type](Handling%20an%20internal%20Qt%20MIME%20type): How to handle the internal MIME type used for drag and drop between item views.

- [Binding widget properties to Python variables](Binding%20widget%20properties%20to%20Python%20variables): Using Python\'s property system to access Qt properties and bind them to variables.

- [Making non-clickable widgets clickable](Making%20non-clickable%20widgets%20clickable): How to misuse event filters to add `clicked()`{.backtick} signals to widgets.

- [Undo and redo with line edits](Undo%20and%20redo%20with%20line%20edits): An incomplete example showing basic undo/redo handling.

- [Using a signal mapper](Using%20a%20signal%20mapper): How to associate values with signals from many widgets and use one slot to handle them all.

- [Sending Python values with signals and slots](Sending%20Python%20values%20with%20signals%20and%20slots): How to communicate Python values via Qt\'s signals and slots mechanism.

- [Using a translation of Qt](Using%20a%20translation%20of%20Qt): How to display standard dialogs and messages in your local language.

- [Getting the version numbers of Qt, SIP and PyQt](./PyQt(2f)Getting(20)the(20)version(20)numbers(20)of(20)Qt(2c20)SIP(20)and(20)PyQt.html): How to obtain the version information for the Qt-related modules you are using.

- [Writing a client for a zeromq service](Writing%20a%20client%20for%20a%20zeromq%20service): How to access a zeromq service while keeping the GUI responsive.

### Painting 

- [Drawing highlighted rows in a calendar widget](Drawing%20highlighted%20rows%20in%20a%20calendar%20widget): How to highlight the current week in a QCalendarWidget subclass.

- [Windows with gradient backgrounds](Windows%20with%20gradient%20backgrounds): How to change the background colour of a window to use a gradient instead of the standard colour in the palette.

- [Fading Between Widgets](Fading%20Between%20Widgets): How to create a stacked widget that fades between widgets on different pages.

- [Fading and unfading a widget with a delay](Fading%20and%20unfading%20a%20widget%20with%20a%20delay): How to produce a simple fade-unfade animation.

- [Paint on an image](Paint%20on%20an%20image): How to paint text and graphics on an image.

- [Painting and clipping demonstration](Painting%20and%20clipping%20demonstration): A demonstration showing how to clip what a painter draws on a widget.

- [Clipping SVG output](Clipping%20SVG%20output): How to clip Scalable Vector Graphics (SVG) output when drawing with QPainter.

- [GraphicsView\_-\_SimpleAnimation](GraphicsView_-_SimpleAnimation): How to construct a very simple animation using QGraphicsView, QGraphicsItem, QGraphicsItemAnimation and QTimeLine. (Qt4)

- [Python syntax highlighting](Python%20syntax%20highlighting): How to add syntax highlighting to a QPlainTextEdit widget. (Qt4)

- [Painting an overlay on an image](Painting%20an%20overlay%20on%20an%20image): How to paint one image onto another.

- [Movie splash screen](Movie%20splash%20screen): How to paint a movie on a splash screen instead of a static image.

- [Extend Two QPixmap](Extend%20Two%20QPixmap): How to paint merge two QPixmaps into one QPixmap.

### Widgets 

- [Widgets in a layout](Widgets%20in%20a%20layout): How to create widgets and put them in a layout.

- [Show an image using a label](Show%20an%20image%20using%20a%20label): How to display an image.

- [A full widget waiting indicator](A%20full%20widget%20waiting%20indicator): How to draw a busy/waiting indicator over an entire widget.

- [Handling context menus](Handling%20context%20menus): The different ways you can handle context menus.

- [Five minute steps in a QTimeEdit](Five%20minute%20steps%20in%20a%20QTimeEdit): Customise the behaviour of QTimeEdit by subclassing.

- [Customising tab bars](Customising%20tab%20bars): How to change the size allocated to tabs in tab bars and tab widgets.

- [Customising a tab to contain a menu](Customising%20a%20tab%20to%20contain%20a%20menu): How to put a menu button in a tab bar.

- [Adding auto-completion to a QLineEdit](Adding%20auto-completion%20to%20a%20QLineEdit): How to use a QStringListModel to provide data for auto-completion.

- [Adding tab-completion to a QLineEdit](Adding%20tab-completion%20to%20a%20QLineEdit): How to handle key events to enable tab-completion.

- [Adding custom signals to a simple painted widget](Adding%20custom%20signals%20to%20a%20simple%20painted%20widget): How to declare and use custom signals.

- [Creating a widget with a fixed aspect ratio](Creating%20a%20widget%20with%20a%20fixed%20aspect%20ratio): How to ensure that a widget keeps a certain aspect ratio when it is resized.

- [Compass widget](Compass%20widget): A simple custom widget, showing how to handle paint events.

- [Adding a background image to an MDI area](Adding%20a%20background%20image%20to%20an%20MDI%20area): How to display a non-tiled image in the background of an MDI area widget.

- [Selecting a region of a widget](Selecting%20a%20region%20of%20a%20widget): How to use a QRubberBand to select part of a widget.

- [Distinguishing between click and double click](Distinguishing%20between%20click%20and%20double%20click): How to handle a double click without acting on the first click.

### Item Views 

- [Using a different view with QComboBox](Using%20a%20different%20view%20with%20QComboBox): How to replace the standard view used for a combo box\'s pop-up menu.

- [Sorting numbers in columns](Sorting%20numbers%20in%20columns): How to sort a table by the numbers in a given column.

- [Animated items using delegates](Animated%20items%20using%20delegates): How to animate items in a list view, using a custom delegate, timer events and a signal.

- [Animated items using delegates and movies](Animated%20items%20using%20delegates%20and%20movies): How to animate items in a list view - an improved version of the previous example.

- [Adding items to a list widget](Adding%20items%20to%20a%20list%20widget): How to add items to a QListWidget instance.

- [A custom Python class-based 1D model](A%20custom%20Python%20class-based%201D%20model): A drag and drop-enabled model which holds Python objects.

- [Reading selections from a selection model](Reading%20selections%20from%20a%20selection%20model): How to read selections and update an underlying model.

- [Creating a context menu for a tree view](Creating%20a%20context%20menu%20for%20a%20tree%20view): How to determine the level of nesting in a tree view and create an appropriate menu.

- [Selecting items in unrelated views](Selecting%20items%20in%20unrelated%20views): How to use selection models to relate items in views with different models.

- [Showing a subset of a model in a view](Showing%20a%20subset%20of%20a%20model%20in%20a%20view): How to show a model in one view while showing a subset of the same model in another view.

### WebKit 

- [Using a Custom Protocol with QtWebKit](Using%20a%20Custom%20Protocol%20with%20QtWebKit): How to add support for a custom protocol to an embedded Web browser.

- [Embedding Widgets in Web Pages](Embedding%20Widgets%20in%20Web%20Pages): How to embed widgets written in Python into Web pages shown with QWebView.

- [Exposing Qt Classes to QtWebKit](Exposing%20Qt%20Classes%20to%20QtWebKit): How to wrap Qt classes and expose them to an embedded Web browser.

- [Augmented Web Browser](Augmented%20Web%20Browser): A Web browser with a side panel that shows a table of contents for the document being displayed.

### Multimedia 

- [Playing a sound with QtMultimedia](Playing%20a%20sound%20with%20QtMultimedia): How to use QAudioOutput to play a sound.

### Drag and Drop 

- [Exporting a file to other applications](Exporting%20a%20file%20to%20other%20applications): How to drag data as a file for other applications to load.

### Databases 

- [Removing a database](Removing%20a%20database): How to remove a database and optionally reload it again without getting warnings from Qt.

### Qt Designer and uic 

- [Previewing a form](Previewing%20a%20form): How to load and display a form created in Qt Designer.

## PyQt 3 

*Note: [PyQt]() 3 examples were not transferred from the old PyQt Wiki.*

- [CustomListViewItems](./CustomListViewItems.html): How to customize the painting of list view items. (Qt 3)

- [ListBoxAndListViewIterators](./ListBoxAndListViewIterators.html): How to loop over all items in list boxes and list views. (Qt 3)

- [DragAndDropWithPyQt](./DragAndDropWithPyQt.html): How to make use of drag and drop without subclassing. (Qt 3)

- [CreatingMdiApplications](./CreatingMdiApplications.html): Some links and pointers for MDI development. (Qt 3)

- [Wrapper_For_QWidgetFactory](./Wrapper_For_QWidgetFactory.html): How to set up the slot connections automatically in [PyQt](). (Qt 3)

- [LoadingUIFilesAtRuntime](./LoadingUIFilesAtRuntime.html): How to load classes (as opposed to instances) directly from UI files, at runtime. (Qt 3)

- [SimpleQScintillaExample](./SimpleQScintillaExample.html): a simple demonstration of QScintilla use with [PyQt](). (Qt 3)

- [SignalDecorator](./SignalDecorator.html): a decorator that provides the signal signature for a method. (Qt 3)

- [ScrollableGroupBox](./ScrollableGroupBox.html): A simple way to get a scrollable groupbox. (Qt 3)

- [Capturing_Output_from_a_Process](./Capturing_Output_from_a_Process.html): How to capture output from a process and show it in a text editor/browser. (Qt 3)

- [Printing_a_Worksheet](./Printing_a_Worksheet.html): How to print the contents of a worksheet onto a single page of A4 paper. (Qt 3)
