# PyQt/PyKDE_and_xattr

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Disclaimer: This tutorial is unfinished.

This tutorial will help you write a simple, but quite useful script. The resulting script can be used either on the command line, or as a servicemenu extension to konqueror.

We will start with some import statements. The first line signifies that this file can be executed (#!), and which program executes it (/usr/bin/python). You will also need to chmod +x on the resulting file to actually execute it. The sys module is needed to parse arguments on the command line. The os module is used for os.path functions.

    import os, sys

In order to make use of this script you must have user_xattr support on your filesystem. General info about extended attributes available here. [http://acl.bestbits.at/](http://acl.bestbits.at/) A good article explaining how to enable user_xattr support on your filesystem, as well as some examples on how to use them is here. [http://enterprise.linux.com/article.pl?sid=05/06/13/1352241](http://enterprise.linux.com/article.pl?sid=05/06/13/1352241)

The xattr extension is needed for this example can be found here [http://cheeseshop.python.org/pypi/xattr](http://cheeseshop.python.org/pypi/xattr) or here [http://undefined.org/python/#xattr](http://undefined.org/python/#xattr).

If you are using debian, you can apt-get install python-xattr .

    from xattr import xattr

The KTextBrowser class has limited HTML support which is real handy, because you can make some pretty displays. In order to ease the creation of HTML source for the textbrowser, I recommend using forgetHTML, which can be found here. [http://forgethtml.sourceforge.net/](http://forgethtml.sourceforge.net/)

If you are using debian, you can apt-get install python-forgethtml .

    from forgetHTML import SimpleDocument
    from forgetHTML import Anchor, Table
    from forgetHTML import TableRow, TableCell
    from forgetHTML import TableHeader, Header

KDE is built on top of Qt. Many of the more simple widgets are not subclasses in KDE, or PyKDE, as they do not require the features that set the KDE widgets apart from the Qt widgets. These are the widgets that will be needed from Qt.

    from qt import SIGNAL, SLOT
    from qt import QSplitter
    from qt import QGridLayout
    from qt import QLabel
    from qt import QFrame

Next, we will import classes from the PyKDE modules. You may notice that I don\'t use \"from kdeui import \*\" here. This is because it can be a little confusing later on in the code to know which module the imported object comes from. I also try to follow pep8(python coding style), at least where I think it makes sense. I also break it in other places where I think it makes more sense to break it (like import os, sys).

    from kdecore import KAboutData
    from kdecore import KCmdLineArgs
    from kdecore import KApplication
    from kdecore import KEntryKey, KEntry

    from kdeui import KAboutDialog
    from kdeui import KMainWindow
    from kdeui import KListView, KListViewItem
    from kdeui import KTextBrowser
    from kdeui import KMessageBox
    from kdeui import KLineEdit
    from kdeui import KDialogBase
    from kdeui import KStdAction
    from kdeui import KPopupMenu

Next we make a couple of handy functions to create and parse url\'s that we will make in the KTextBrowser. These url\'s don\'t have to be valid url\'s in the usual sense. They only have to be unique to the application that handles them. The way we will make urls in this script will be according to this method - action\|\|key\|\|filename, where \"action\" is the action to be performed (new, edit or delete), \"key\" is the name of the extended attribute, and filename is the name of the file. The double pipe is used to separate the parts of the url. You should use some sort of delimeter which won\'t be present in any other part of the url. You can use any string as a delimeter, but you should choose a \"rare\" multicharacter string that won\'t appear in the parts that you are joining.

    url_delimeter = '||'

    # handy function to split urls created in the text browser
    def split_url(url):
        return str(url).split(url_delimeter)

    def make_url(*args):
        return url_delimeter.join(args)

Next, we make a couple of forgetHTML subclasses to display the data. The colors are taken from the /etc/X11/rgb.txt file in X. Feel free to change them to suit your taste. I don\'t want to spend too much time explaining forgetHTML, but since there is no documentation for it, I will spend a short space explaining the basic concept.

ForgetHTML is DOM (Document Object Model) approach to generating HTML. This means that all of the markup elements are python objects. It is somewhat similar to the xml.dom.minidom in python, except it is not as complete, but uses a more pythonic style. Here is a short example of how to make an HTML fragment. This is not part of the script, but just an example of forgetHTML.

    >>> from forgetHTML import Anchor
    >>> from forgetHTML import TableCell
    >>> a = Anchor('hello', href='there')
    >>> print a
    <a href="there">
      hello
    </a>

    >>> c = TableCell(a)
    >>> c['bgcolor'] = 'blue'
    >>> print c
    <td bgcolor="blue">
      <a href="there">
        hello
      </a>
    </td>

    >>> from forgetHTML import TableRow
    >>> r = TableRow()
    >>> r.set(c)
    >>> r.append(c)
    >>> print r
    <tr>
      <td bgcolor="blue">
        <a href="there">
          hello
        </a>
      </td>
      <td bgcolor="blue">
        <a href="there">
          hello
        </a>
      </td>
    </tr>

Now that you have a glimpse of forgetHTML, hopefully the next part of the script won\'t appear too cryptic. We will start by making a table class to display the extended attributes of a file.

    # table to display and edit xattr's
    class XattrTable(Table):
        def __init__(self, **args):
            Table.__init__(self)

        def set_header(self, filename, fullpath):
            row = TableRow(bgcolor='LightSeaGreen')
            tbl_header = TableHeader(filename, colspan=3, align='center')
            row.append(tbl_header)
            self.set(row)
            href = make_url('new', 'attribute', fullpath)
            a = Anchor('new attribute', href=href)
            row = TableRow(TableCell(a), bgcolor='LightSeaGreen')
            self.append(row)

Next, we make a document class to hold the table we just defined.

    class BaseDocument(SimpleDocument):
        def __init__(self, title='BaseDocument', **args):
            SimpleDocument.__init__(self, title=title)
            self.maintable = XattrTable(class_='XattrTable')
            self.body.set(self.maintable)

Continuing with the [BaseDocument](./BaseDocument.html) class, we define a method for setting the filename. We use xattr to read the extended attributes for that file, and display them in a table.

        def set_filename(self, filename):
            fullpath = os.path.join(self.dirname, filename)
            self.maintable.set_header(filename, fullpath)
            xf = xattr(fullpath)
            for key, value in xf.items():
                ekey = key.encode()
                href = make_url('edit', ekey, xf.obj)
                a = Anchor(ekey, href=href)
                tk = TableCell(a)
                tv = TableCell(value)
                href = make_url('delete', ekey, xf.obj) 
                delanchor = Anchor('(del)', href=href)
                row = TableRow()
                row.append(tk)
                row.append(tv)
                row.append(delanchor)
                self.maintable.append(row)

Now, we get into the PyKDE part of the script. We will start with the KTextBrowser. The textbrowser is one of the more important objects in the script. The limited HTML support allows for easy, clean display of the data. It also allows for active interaction with the data by using HTML anchors. Using the textbrowser wisely can really speed up the development time, especially if you are new to using PyKDE. This is mainly because, for any action that you want to perform, you can use anchors, and parse the urls quicker than instantiating KDE objects and connecting the signals. This doesn\'t mean you should skip making button and menu items entirely, forcing the KDE application to look just like a web application. Web applications generally suffer by having little to no gui, or having the gui locked in the web browser. You should consider where the action would be more appropriately called from, in order to design the application. It is also helpful sometimes to duplicate something that is already on the toolbar or in the menu as an anchor in the textbrowser also.

Here we start by subclassing the KTextBrowser. Like most KDE widgets, we pass its parent to it, so it knows where it is in the widget hierarchy. The dirname attribute is made in the parent, which is the os.path.dirname of the files that are being handled by the script. The doc attribute is the document class listed above. When we perform self.setNotifyClick(True), this tells the textbrowser that we wish to be notified when the user clicks on an anchor. This is handled a a setSource method in the class.

    # text browser for xattr
    # much of the actual handling of the xattr's is done here
    class XattrBrowser(KTextBrowser):
        def __init__(self, parent):
            KTextBrowser.__init__(self, parent)
            self.resize(350, 450)
            self.dirname = parent.dirname
            # here we setNotifyClick to True so we can handle
            # url clicks
            self.setNotifyClick(True)
            self.doc = BaseDocument('Xattr Document')
            # pass dirname to doc
            self.doc.dirname = self.dirname

Continuing with the textbrowser, we define a method of setting the filename. This method will be called when a file is selected in the KListView in the parent item.

        def setFileName(self, filename):
            self.doc.set_filename(filename)
            self.setText(self.doc.output())

Now, we get to the \"magic\" part of the textbrowser, the setSource method. As I said above, this method is called when an anchor is clicked. The href of that anchor is passed as an argument to this method. Please note that the KTextBrowser differs from the QTextBrowser with regard to this method. In the QTextBrowser, this method is used to set the name of the displayed document. In the KTextBrowser, this method is \"Reimplemented to NOT set the source but to do the special handling.\" (quoting from KDE apidocs). The KDE apidocs also say not to call this method. We don\'t need to call it explicitly, we only need to define it so that it gets called internally when an anchor is clicked. In this method, we pull up a special dialog to further handle the action requested.

        # this is selected when a url is clicked
        # I'm not sure if this should really be used
        # the method has been changed from the qt function
        # but the kde apidocs are somewhat unclear on it.
        def setSource(self, url):
            action, key, filename = split_url(url)
            if action == 'new':
                dlg = XattrDialog(self, filename)
                dlg.connect(dlg, SIGNAL('okClicked()'), dlg.update_xattr)
                dlg.show()
            elif action == 'edit':
                value = xattr(filename).get(key)
                dlg = XattrDialog(self, filename, key, value)
                dlg.connect(dlg, SIGNAL('okClicked()'), dlg.update_xattr)
                dlg.show()
            elif action == 'delete':
                dlg = XattrDialog(self, filename, key, action='delete')
                dlg.connect(dlg, SIGNAL('okClicked()'), dlg.delete_xattr)
                dlg.show()

Now we define a couple of methods to actually perform the actions on the extended attributes. At the end of each of these methods, we update the textbrowser to display the new information.

        def update_xattr(self, filename, key, value):
            xf = xattr(filename)
            xf.set(key, value)
            self.setFileName(os.path.basename(filename))

        def delete_xattr(self, filename, key):
            xf = xattr(filename)
            xf.remove(key)
            self.setFileName(os.path.basename(filename))

I decided to go ahead and define the KMainWindow class here. In the attached script, it is defined at the bottom, but for the tutorial, I feel it is probably better to start explaining it here.

    # main window class
    class MainWindow(KMainWindow):
        def __init__(self, parent, filelist):
            KMainWindow.__init__(self, parent, 'PyKDE xattr editor')
            self.resize(500, 450)
            self.filelist = []
            self.dirname = os.path.dirname(filelist[0])
            # setup actions
            self.initActions()
            # setup the menus
            self.initMenus()

            
            # get basename's for the files to make the listview prettier
            for afile in filelist:
                if os.path.dirname(afile) != self.dirname:
                    KMessageBox.error(self, 'all files need to be in the same directory (for now)')
                    sys.exit(1)
                else:
                    self.filelist.append(os.path.basename(afile))

Here in the [init] method, we setup the main attributes for the class. The dirname attribute is not strictly necessary, nor is the requirement for all files in the filelist to be in the same directory. This has basically been done to keep the interface from being confusing and the tutorial shorter. It would probably make a good second tutorial to expand this script to use files in different directories, or even a small filesystem browser. Since we want to keep things simple and bug free (hopefully), we will endure this small limitation. Note that if files from different directories are passed as arguments, and error is raised and the script is exited. There is no real python error raised, but a KMessageBox.error, followed by a non-zero sys.exit.

Also note that we call the initActions and initMenus methods here. These methods don\'t have to have these particular names, but the method to initialize the actions must be called before the method to initialize the menus. I will detail why, when we get to those methods.

            # place a splitter in the window
            self.splitView = QSplitter(self, 'splitView')
            # pass dirname to splitter
            self.splitView.dirname = self.dirname
            if len(self.filelist) > 1:
                # place a listview in the splitter (on the left)
                self.listView = KListView(self.splitView, 'filelist_view')
                # fill listview
                self.initlistView()
                # setup signals
                self.connect(self.listView,
                             SIGNAL('selectionChanged()'), self.selectionChanged)
            

            # place text browser in splitter
            self.textView = XattrBrowser(self.splitView)

Continuing in the [init] method, we add a QSplitter (called splitView) to the window. We plan to have the filelist displayed on the left side of the splitter and the textbrowser on the right side. The order the listview and textbrowser classes are initialized in determine where they go. They are placed in a left to right fashion, top to bottom for a horizontal splitter. After we initialize the listview, we connect its \"selectionChanged\" signal to the selectionChanged method to handle that event. The method doesn\'t have to be named \"selectionChanged\", but the actual signal does. Notice that the listview is only created if there is more than one file in the filelist.

Now that we have defined all of the widgets, it\'s time to set the main widget. In the KMainWindow class, this method is called \"setCentralWidget\". We set this to be the QSplitter defined above. After that, we do a quick hack to handle the possibility of only having one file to manipulate. There is no real need for a listview with only one item, so we skipped creating it above. Since we already know which file is \"selected\" because there is only one, we go ahead and set the textbrowser to that file.

            self.setCentralWidget(self.splitView)
            # if there is only one file, go ahead and select it
            # and skip making the listView
            if len(self.filelist) == 1:
                self.textView.setFileName(self.filelist[0])

Now we are ready for the initActions and initMenus methods that were called above. Strictly speaking, I could have just put these in the [init] method. It would have probably made a better tutorial, but in practice it is better to have these types of initializations outside of [init], as it makes the code easier to read and maintain.

The self.actionCollection call returns a KActionCollection object. This is a set of all of the actions for the main window. At this time it is empty, so we will start filling it with actions. An action (or KAction object) is a structure that holds a name, icon, tooltip, keyboard shortcut, and short help text for a gui function. For instance, if you want a menu item that opens a file, you make a KAction object that contains the menu text \"Open a file\", an icon (probably called \"fileopen\"), a shorcut (probably Ctrl-O). Now that you made this action, you can put it in the menu. You can also put it in a toolbar, or a right-click popup menu. Doing this for many actions saves time in writing separate code for the menus and toolbar. It is also helpful that KDE comes with several common actions predefined. These are all held in the KStdAction enumerator. The above example for \"Open a file\" would be called KStdAction.open . So instead of calling KAction(text, icon, shortcut, parent, slot, actionCollection), you only have to call KStdAction.open(parent, slot, actionCollection), the text and icon are already predefined. In this script, we are only using the \"quit\" action.

        def initActions(self):
            collection = self.actionCollection()
            # here we add actions to the actionCollection
            # we are only using "quit" which is a standard action
            # other actions can be defined using KAction
            self.quitAction = KStdAction.quit(self.close, collection)

Now that we filled the actionCollection with our actions (only one in this example), we can put them in the menus.

        def initMenus(self):
            # here we make a popup menu that will be placed in the
            # main menubar
            mainmenu = KPopupMenu(self)
            # use the plug method of an action to plug it into something
            # like a menu or toolbar, here we plug it into mainmenu
            self.quitAction.plug(mainmenu)
            # this is the menubar of the window
            menubar = self.menuBar()
            # we insert the mainmenu under the "Main" section
            # of the menubar, the section is not there, but is created
            # when we do this.  The ampersand makes a keyboard accel
            menubar.insertItem('&Main', mainmenu)
            # we do the same for the help menu (which is already in the object,
            # but not on the menubar
            menubar.insertItem('&Help', self.helpMenu(''))
            

        def initlistView(self):
            self.listView.addColumn('file', -1)
            for afile in self.filelist:
                item = KListViewItem(self.listView, afile)
                # creating an another attribute for the item
                # isn't really necessary in this example
                # but this method is useful if you want
                # "full name of something" on the list,
                # but want to attach a uid to the item
                item.filename = afile

        def selectionChanged(self):
            item = self.listView.currentItem()
            # in this example str(item.text()) would work just
            # as well.
            # since we are using the attribute we attached to
            # the item, we don't have to coerce a QString from
            # item.text()
            self.textView.setFileName(item.filename)   
            

            
    class XattrFrame(QFrame):
        def __init__(self, parent, key, value, name='XattrFrame'):
            QFrame.__init__(self, parent, name)
            # 3 rows, 1 column, 0 margin, and -1 space (negative to use margin instead)
            # the middle row will work as a spacer
            self.grid = QGridLayout(self, 3, 1, 0, -1)
            if not key:
                self.keyfield = KLineEdit('user.', self)
            else:
                self.keyfield = QLabel(key, self)
            # add keyfield to row 0, column 0
            self.grid.addWidget(self.keyfield, 0, 0)
            # for row 1 to have a minimum size of 3 pixels
            self.grid.setRowSpacing(1, 3)
            self.valuefield = KLineEdit(value, self)
            # add valuefield to row 2, column 0
            self.grid.addWidget(self.valuefield, 2, 0)
            

    # main dialog class for handling xattr's
    class XattrDialog(KDialogBase):
        def __init__(self, parent, filename, key='', value='', action=None, name='XattrDialog'):
            KDialogBase.__init__(self, parent, name)
            self.filename = filename
            self.key = key
            self.value = value
            if action is None:
                self.frame = XattrFrame(self, key, value)
                self.setMainWidget(self.frame)
            else:
                msg = 'Really delete attribute %s from %s ?' % (key, os.path.basename(filename))
                lbl = QLabel(msg, self)
                self.setMainWidget(lbl)
                
        def update_xattr(self, *args):
            parent = self.parent()
            # we need to coerce the key and value from QStrings
            # to python strings
            key = str(self.frame.keyfield.text())
            value = str(self.frame.valuefield.text())
            if value != self.value:
                parent.update_xattr(self.filename, key, value)
            else:
                KMessageBox.information(parent,
                                        '%s is unchanged, doing nothing.' % self.key)

        def delete_xattr(self, *args):
            parent = self.parent()
            parent.delete_xattr(self.filename, self.key)
            
    # about this program
    class AboutData(KAboutData):
        def __init__(self):
            KAboutData.__init__(self,
                                'pykde-edit-xattrs',
                                'pykde-edit-xattrs',
                                '0.1',
                                "Edit xattr's from konqueror")
            self.addAuthor('Joseph Rawson', 'author',
                           'umeboshi@gregscomputerservice.com')
            self.setCopyrightStatement('public domain')

    # dialog class for the application
    # this will popup when help->about is selected from the help menu
    class AboutDialog(KAboutDialog):
        def __init__(self):
            KAboutDialog.__init__(self, parent, *args)
            self.setTitle('PyKDE xattr editor')
            self.setAuthor('Joseph Rawson')
            
    # main application class
    class MainApplication(KApplication):
        def __init__(self):
            KApplication.__init__(self)
            # in case something needs done before quitting
            self.connect(self, SIGNAL('aboutToQuit()'), self.quit)
            
        def quit(self):
            # do something special to quit here
            print "quitting PyKDE edit xattr's application"
            KApplication.quit(self)


    if __name__ == '__main__':
        aboutData = AboutData()
        # I don't know what these three lines are actually doing
        # but the end result 'args' is a KCmdLineArgs instance
        KCmdLineArgs.init(sys.argv, aboutData)
        KCmdLineArgs.addCmdLineOptions([('+files', 'files to edit')])
        args = KCmdLineArgs.parsedArgs()
        # it should be like this:
        ## for a in args:
        ##     print a
        # but it works like this:
        ## for a in range(args.count()):
        ##     print args.arg(a)
        filelist_args = [args.arg(a) for a in range(args.count())]
        # setup application
        app = MainApplication()

        # setup dcop and register the application
        dcop = app.dcopClient()
        appid = dcop.registerAs('pykde-edit-xattrs')

        filelist_args = [f for f in filelist_args if os.path.isfile(f)]
        if not len(filelist_args):
            KMessageBox.error(None, 'There were no applicable arguments')
            sys.exit(1)

        # the first argument to MainWindow is the parent
        # which is None (not the application object)
        win = MainWindow(None, filelist_args)
        win.show()
        
        # set main window in application
        app.setMainWidget(win)

        # run the application
        app.exec_loop()


    # this is the desktop file you will need to use this
    # example in konqueror.  The Exec line assumes
    # that the script is located in ~/bin
    #
    # desktop_file_contents:
    # ======================================
    # [Desktop Action edit-xattrs]
    # Exec=$HOME/bin/pykde-edit-xattrs %F
    # Name=Edit extended attributes
    #
    # [Desktop Entry]
    # Actions=edit-xattrs
    # ServiceTypes=all/allfiles
    # =======================================
    # cut and paste between the lines, remove the comments
    # and put the contents in a file name pykde-edit-xattrs.desktop
    # the desktop file should be placed in ~/.kde/share/apps/konqueror/servicemenus
