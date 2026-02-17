# PyQt/simple5

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## \"Simple\" Stage 5 

### updateStatus 

In Stage 4 the listing was long enough to fill one wiki page, so we did not spend much time discussing it. Now we can discuss several items in the list.

The **updateStatus** method from **Simple \"Finished\"** is shown in the inset below:

:::: 
::: 
``` 
   1     def updateStatus(self, message):
   2         '''Keep status current.'''
   3         if self.fileName is not None:
   4             flbase = os.path.basename(self.fileName)
   5             self.setWindowTitle(unicode("Simple Editor - " + flbase + "[*]") )
   6             self.statusBar().showMessage(message, 5000)
   7             self.setWindowModified(self.dirty)
```
:::
::::

It is called whenever it seems desirable to update the status, including the displayed name of the file being edited. There is a strange addition of a string **\"\[\*\]\"**, which is shown only if the text in the editor has changed, except that it must not happen whilst the file name is still **\"None\"**. When the program is instantiated, the **[init]** procedure sets sensibly the **fileName** to **None**.

Actually we never see the string **\"\[\*\]\"** - PyQt is smart enough to show **\"fileName\*\"** when the text is altered. If you examine the code, you will see that there is a signal

            self.textEdit.textChanged.connect(self.setDirty)

that is activated when the text has changed and it calls the method to set flag \"dirty\" to True, which in turn causes the **updateStatus** to be called. All the programming steps to achieve these fairly smart status indication changes can be figured out, but where do we get the basic information - what and how: **title display changes, text in editor window changes etc.?**

### Qt Assistant 

Just like the **Qt Designer** is an indispensable tool, so is **Qt Assistant**. Let me quote what a few better informed people on the PyQt mailing list

    pyqt@riverbankcomputing.com

have told me about the need to use the **Qt Assistant** when I asked:

    Is it possible to access lines of text in a textEdit?  If so how can I find information about it?

The answers from two **gurus** were:

    If you enter findBlockByLineNumber in Qt Assistant you will see that this method  belongs to a QTextDocument object and returns a QTextBlock object QTextEdit has a method called "document()" which returns a QTextDocument.  Henning SchrÃ¶der

**and**

    Searching for some functionality of QTextEdit, e.g. how to get at a specific line via line number: 
     * Look up QTextEdit in assistant
       We read: The QTextEdit class provides a widget that is used to edit and
       display both plain and rich text. 
     * Click on more...
       We read: QTextEdit works on paragraphs and characters. A paragraph is a
       formatted string which is word-wrapped to fit into the width of the
       widget. By default when reading plain text, one newline signifies a paragraph.
       Sounds like we're looking for paragraphs in plain text mode
     * Check class methods, that do what we want: 
       Nothing obvious stands out
     * Check base classes:
       QTextEdit inherits from QAbstractScrollArea only, that won't help us
       much here
     * Check methods again: 
       Nothing obvious with paragraphs, but QTextDocument * document() might be
       interesting
     * Click on document() method:
       We read: Returns a pointer to the underlying document.
     * Check it out: click on QTextDocument
       We read: The QTextDocument class holds formatted text that can be viewed and edited 
       using a QTextEdit We're getting nearer, but still no ball: check out class methods
     * It has a method: QTextBlock findBlockByLineNumber ( int lineNumber ) 
       Sounds like the best fit: click on method
     * We read: Returns the text block that contains the specified lineNumber.
       What the hell is a QTextBlock? Click:
       It encapsulates text fragments, and provides access to them
     * Check methods: QString text() sounds, like what we are looking for
       We read: Returns the block's contents as plain text.
    Target reached. Pete (Hans-Peter Jansen)

What I sought and got was not **\"a fish for one meal\"**, but a line, hook and instructions to **\"feed me continually\"**. It\'s now up to me to make good use of it. I feel morally obliged to **share** it with you!

### Selecting and Compiling Resources 

Concentrating our mind to code development, leads to unintended consequence of ignoring some other important aspects of programming, which, once learned, easily drift from our attention. Resources is one such aspect. Where do all the icon images come from?

First are the artistic images. There are several collections freely available in public domain. We used a \"tango\" collection. It is fairly extensive and freely available on the web. To save space in our tar balls, we selected images to a small collection that we call **select_tango**. To associate images to the icons, we edit a XML file **simple.qrc**:

    <!DOCTYPE RCC><RCC version="1.0">
    <qresource>
    <file alias="filenew.png">select_tango/32x32/actions/document-new.png</file>
    <file alias="fileopen.png">select_tango/32x32/actions/document-open.png</file>
    <file alias="filesave.png">select_tango/32x32/actions/document-save.png</file>
    <file alias="filesaveas.png">select_tango/32x32/actions/document-save-as.png</file>
    <file alias="fileprint.png">select_tango/32x32/actions/document-print.png</file>
    <file alias="filequit.png">select_tango/32x32/actions/system-log-out.png</file>
    <file alias="about.png">select_tango/32x32/apps/preferences-system-session.png</file>
    <file alias="help.png">select_tango/32x32/apps/help-browser.png</file>
    <file>help/analysis.html</file>
    <file>help/filemenu.html</file>
    <file>help/index.html</file>
    </qresource>
    </RCC>

Let us look at the third line in more detail:

    <file alias="filenew.png">select_tango/32x32/actions/document-new.png</file>

**filenw.png** is the program name for the image of the **icon** for the corresponding **action**; *select_tango* is the directory of our icon images selected from the *tango* collection. This line is almost self-explanatory for a human eye, but not for the computer. It can be converted to the computer readable format in several ways - one way is shown below:

    pyrcc4 simple.qrc > qrc_simple.py

This command needs to be executed in the directory with subdirectories **select_tango, help** and, of course, file simple.qrc. For the record, I am using Python 2.6.6, Qt 4.7.0, [PyQt](PyQt) 4.7.4 binaries from ubuntu 10.10 repositories. As the development proceeds in an astounding pace, all these may change and occasional incompatibility with earlier versions can not be completely ruled out.

What this last command achieves has a humorous shading: a human readable **simple.qrc** is converted to a computer readable **qrc_simple.py**. Obviously, what is computer readable, is not human readable and vice versa\...

You will no doubt recall that **qrc_simple** and **ui_simple** are *imported* to the program and thus made available to augment the \"Simple\" **text editor.**

[Return Home](./PyQt(2f)simple.html)
