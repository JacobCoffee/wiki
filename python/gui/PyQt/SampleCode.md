# PyQt/SampleCode

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page contains links to some useful code snippets. Longer, more detailed code examples can be found via the [Overviews_and_Guides](./Overviews_and_Guides.html) page.

**Put any code snippet for PyKDE and PyQt that you find useful here. If the code is longer than one screen at normal point size, it might be better if you provide a rationale and a link, or just put it on a separate page.**

## PyQt 5 

- [QML callback function](./PyQt(2f)QML(20)callback(20)function.html): How to pass and execute callback functions with QML.

- [Threading, Signals and Slots](./PyQt5(2f)Threading(2c)_Signals_and_Slots.html): How to perform work in one thread and use the result in another.

## PyQt 4 

- [Decoding Japanese Text](./PyQt(2f)Decoding_Japanese_Text.html): The response to a posting on comp.lang.python, asking about decoding text for display in a GUI.

- [Screenshots](http://home.tampabay.rr.com/dataheli/) of various database and 3D graphics widgets, with code to follow soon. **\[dead link!\]**

- [Using GStreamer with PyQt](./PyQt(2f)Using(20)GStreamer(20)with(20)PyQt.html): How to use the GStreamer bindings for Python with PyQt (see [Multimedia Resources](./PyQt(2f)Multimedia_Resources.html) for more multimedia links).

### Infrastructure 

- [Threading, Signals and Slots](./PyQt(2f)Threading(2c)_Signals_and_Slots.html): How to perform work in one thread and use the result in another. (Qt 4)

- [PyQt/AutoConnectingSlots](./PyQt(2f)AutoConnectingSlots.html): How to have the signals of widgets automatically connected to Python defined slots.

- [Handling Qt\'s internal item MIME type](./PyQt(2f)Handling(20)Qt(27)s(20)internal(20)item(20)MIME(20)type.html): How to implement a drop handler in a model to handle items dragged from standard models.

- [Handling an internal Qt MIME type](./PyQt(2f)Handling(20)an(20)internal(20)Qt(20)MIME(20)type.html): How to handle the internal MIME type used for drag and drop between item views.

- [Binding widget properties to Python variables](./PyQt(2f)Binding(20)widget(20)properties(20)to(20)Python(20)variables.html): Using Python\'s property system to access Qt properties and bind them to variables.

- [Making non-clickable widgets clickable](./PyQt(2f)Making(20)non(2d)clickable(20)widgets(20)clickable.html): How to misuse event filters to add `clicked()`{.backtick} signals to widgets.

- [Undo and redo with line edits](./PyQt(2f)Undo(20)and(20)redo(20)with(20)line(20)edits.html): An incomplete example showing basic undo/redo handling.

- [Using a signal mapper](./PyQt(2f)Using(20)a(20)signal(20)mapper.html): How to associate values with signals from many widgets and use one slot to handle them all.

- [Sending Python values with signals and slots](./PyQt(2f)Sending(20)Python(20)values(20)with(20)signals(20)and(20)slots.html): How to communicate Python values via Qt\'s signals and slots mechanism.

- [Using a translation of Qt](./PyQt(2f)Using(20)a(20)translation(20)of(20)Qt.html): How to display standard dialogs and messages in your local language.

- [Getting the version numbers of Qt, SIP and PyQt](./PyQt(2f)Getting(20)the(20)version(20)numbers(20)of(20)Qt(2c20)SIP(20)and(20)PyQt.html): How to obtain the version information for the Qt-related modules you are using.

- [Writing a client for a zeromq service](./PyQt(2f)Writing(20)a(20)client(20)for(20)a(20)zeromq(20)service.html): How to access a zeromq service while keeping the GUI responsive.

### Painting 

- [Drawing highlighted rows in a calendar widget](./PyQt(2f)Drawing(20)highlighted(20)rows(20)in(20)a(20)calendar(20)widget.html): How to highlight the current week in a QCalendarWidget subclass.

- [Windows with gradient backgrounds](./PyQt(2f)Windows(20)with(20)gradient(20)backgrounds.html): How to change the background colour of a window to use a gradient instead of the standard colour in the palette.

- [Fading Between Widgets](./PyQt(2f)Fading(20)Between(20)Widgets.html): How to create a stacked widget that fades between widgets on different pages.

- [Fading and unfading a widget with a delay](./PyQt(2f)Fading(20)and(20)unfading(20)a(20)widget(20)with(20)a(20)delay.html): How to produce a simple fade-unfade animation.

- [Paint on an image](./PyQt(2f)Paint(20)on(20)an(20)image.html): How to paint text and graphics on an image.

- [Painting and clipping demonstration](./PyQt(2f)Painting(20)and(20)clipping(20)demonstration.html): A demonstration showing how to clip what a painter draws on a widget.

- [Clipping SVG output](./PyQt(2f)Clipping(20)SVG(20)output.html): How to clip Scalable Vector Graphics (SVG) output when drawing with QPainter.

- [GraphicsView\_-\_SimpleAnimation](./PyQt(2f)GraphicsView_(2d)_SimpleAnimation.html): How to construct a very simple animation using QGraphicsView, QGraphicsItem, QGraphicsItemAnimation and QTimeLine. (Qt4)

- [Python syntax highlighting](./PyQt(2f)Python(20)syntax(20)highlighting.html): How to add syntax highlighting to a QPlainTextEdit widget. (Qt4)

- [Painting an overlay on an image](./PyQt(2f)Painting(20)an(20)overlay(20)on(20)an(20)image.html): How to paint one image onto another.

- [Movie splash screen](./PyQt(2f)Movie(20)splash(20)screen.html): How to paint a movie on a splash screen instead of a static image.

- [Extend Two QPixmap](./PyQt(2f)Extend(20)Two(20)QPixmap.html): How to paint merge two QPixmaps into one QPixmap.

### Widgets 

- [Widgets in a layout](./PyQt(2f)Widgets(20)in(20)a(20)layout.html): How to create widgets and put them in a layout.

- [Show an image using a label](./PyQt(2f)Show(20)an(20)image(20)using(20)a(20)label.html): How to display an image.

- [A full widget waiting indicator](./PyQt(2f)A(20)full(20)widget(20)waiting(20)indicator.html): How to draw a busy/waiting indicator over an entire widget.

- [Handling context menus](./PyQt(2f)Handling(20)context(20)menus.html): The different ways you can handle context menus.

- [Five minute steps in a QTimeEdit](./PyQt(2f)Five(20)minute(20)steps(20)in(20)a(20)QTimeEdit.html): Customise the behaviour of QTimeEdit by subclassing.

- [Customising tab bars](./PyQt(2f)Customising(20)tab(20)bars.html): How to change the size allocated to tabs in tab bars and tab widgets.

- [Customising a tab to contain a menu](./PyQt(2f)Customising(20)a(20)tab(20)to(20)contain(20)a(20)menu.html): How to put a menu button in a tab bar.

- [Adding auto-completion to a QLineEdit](./PyQt(2f)Adding(20)auto(2d)completion(20)to(20)a(20)QLineEdit.html): How to use a QStringListModel to provide data for auto-completion.

- [Adding tab-completion to a QLineEdit](./PyQt(2f)Adding(20)tab(2d)completion(20)to(20)a(20)QLineEdit.html): How to handle key events to enable tab-completion.

- [Adding custom signals to a simple painted widget](./PyQt(2f)Adding(20)custom(20)signals(20)to(20)a(20)simple(20)painted(20)widget.html): How to declare and use custom signals.

- [Creating a widget with a fixed aspect ratio](./PyQt(2f)Creating(20)a(20)widget(20)with(20)a(20)fixed(20)aspect(20)ratio.html): How to ensure that a widget keeps a certain aspect ratio when it is resized.

- [Compass widget](./PyQt(2f)Compass(20)widget.html): A simple custom widget, showing how to handle paint events.

- [Adding a background image to an MDI area](./PyQt(2f)Adding(20)a(20)background(20)image(20)to(20)an(20)MDI(20)area.html): How to display a non-tiled image in the background of an MDI area widget.

- [Selecting a region of a widget](./PyQt(2f)Selecting(20)a(20)region(20)of(20)a(20)widget.html): How to use a QRubberBand to select part of a widget.

- [Distinguishing between click and double click](./PyQt(2f)Distinguishing(20)between(20)click(20)and(20)double(20)click.html): How to handle a double click without acting on the first click.

### Item Views 

- [Using a different view with QComboBox](./PyQt(2f)Using(20)a(20)different(20)view(20)with(20)QComboBox.html): How to replace the standard view used for a combo box\'s pop-up menu.

- [Sorting numbers in columns](./PyQt(2f)Sorting(20)numbers(20)in(20)columns.html): How to sort a table by the numbers in a given column.

- [Animated items using delegates](./PyQt(2f)Animated(20)items(20)using(20)delegates.html): How to animate items in a list view, using a custom delegate, timer events and a signal.

- [Animated items using delegates and movies](./PyQt(2f)Animated(20)items(20)using(20)delegates(20)and(20)movies.html): How to animate items in a list view - an improved version of the previous example.

- [Adding items to a list widget](./PyQt(2f)Adding(20)items(20)to(20)a(20)list(20)widget.html): How to add items to a QListWidget instance.

- [A custom Python class-based 1D model](./PyQt(2f)A(20)custom(20)Python(20)class(2d)based(20)1D(20)model.html): A drag and drop-enabled model which holds Python objects.

- [Reading selections from a selection model](./PyQt(2f)Reading(20)selections(20)from(20)a(20)selection(20)model.html): How to read selections and update an underlying model.

- [Creating a context menu for a tree view](./PyQt(2f)Creating(20)a(20)context(20)menu(20)for(20)a(20)tree(20)view.html): How to determine the level of nesting in a tree view and create an appropriate menu.

- [Selecting items in unrelated views](./PyQt(2f)Selecting(20)items(20)in(20)unrelated(20)views.html): How to use selection models to relate items in views with different models.

- [Showing a subset of a model in a view](./PyQt(2f)Showing(20)a(20)subset(20)of(20)a(20)model(20)in(20)a(20)view.html): How to show a model in one view while showing a subset of the same model in another view.

### WebKit 

- [Using a Custom Protocol with QtWebKit](./PyQt(2f)Using(20)a(20)Custom(20)Protocol(20)with(20)QtWebKit.html): How to add support for a custom protocol to an embedded Web browser.

- [Embedding Widgets in Web Pages](./PyQt(2f)Embedding(20)Widgets(20)in(20)Web(20)Pages.html): How to embed widgets written in Python into Web pages shown with QWebView.

- [Exposing Qt Classes to QtWebKit](./PyQt(2f)Exposing(20)Qt(20)Classes(20)to(20)QtWebKit.html): How to wrap Qt classes and expose them to an embedded Web browser.

- [Augmented Web Browser](./PyQt(2f)Augmented(20)Web(20)Browser.html): A Web browser with a side panel that shows a table of contents for the document being displayed.

### Multimedia 

- [Playing a sound with QtMultimedia](./PyQt(2f)Playing(20)a(20)sound(20)with(20)QtMultimedia.html): How to use QAudioOutput to play a sound.

### Drag and Drop 

- [Exporting a file to other applications](./PyQt(2f)Exporting(20)a(20)file(20)to(20)other(20)applications.html): How to drag data as a file for other applications to load.

### Databases 

- [Removing a database](./PyQt(2f)Removing(20)a(20)database.html): How to remove a database and optionally reload it again without getting warnings from Qt.

### Qt Designer and uic 

- [Previewing a form](./PyQt(2f)Previewing(20)a(20)form.html): How to load and display a form created in Qt Designer.

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
