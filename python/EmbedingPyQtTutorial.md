# EmbedingPyQtTutorial

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Oleksandr Yakovlyev\'s Embeding PyQt Tutorial 

This is a short tutorial to embed your Qt application in [PyQt](PyQt) . It assumes knowledge of bash, Python, Qt+[PyQt](PyQt) and sip.

## Hybrid Application? 

One day I discovered that it can be really great to use [PyQt](PyQt) scripts in a Qt application. It assumes that such Hybrid application can have two \"branches\" - c++ code and python code working together, exchange signals between two these branches, of course possibility to create new objects with python/pyqt and connect signal/slots beetween two parts of the application (Qt and [PyQt](PyQt)), well between Qt objects and [PyQt](PyQt) objects. Well, even more, with Python you can create new classes in runtime, and \... this is almost magic, these new clases/objects will work together with C++(Qt) part of application.

First challenge is event loop. Python and Qt application have their own event loop, and I have not found way to use only Qt event loop yet. So we need to use Python ([PyQt](PyQt)) event loop. It means next change in application:

- Removed main.cpp
- Created main.py with same functionality

Usually Qt application does not have any critical code in main.cpp so it can not be complicated to make same code with Python. Also the modification does not reflect performance because all code is C++ still.

The application code compiles into shared library. Let\'s try it with Qt example (examples/application)

### application.h

- #ifndef APPLICATION_H 
      #define APPLICATION_H 

      #include <qmainwindow.h> 

      class QTextEdit;

      class ApplicationWindow: public QMainWindow
      {
          Q_OBJECT

      public:
          ApplicationWindow();
          ~ApplicationWindow();

      protected:
          void closeEvent( QCloseEvent * );

      public slots:
          void newDoc();
          void choose();
          void load(QString fileName);
          void save();
          void saveAs();
          void print();
          void script();

          void about();
          void aboutQt();

      signals:
          void runScript(const QString&);

      private:
          QPrinter *printer;
          QTextEdit *e;
          QString filename;
      };

       
      #endif 

Here I have added signal void runScript(const QString&)

### application.cpp

- #include "application.h"

      ...

      ApplicationWindow::ApplicationWindow()
          : QMainWindow( 0, "example application main window", WDestructiveClose | WGroupLeader )
      {

          ...

          QToolButton * runButton = new QToolButton(QPixmap(), "Run Script", QString::null, this, SLOT(script()), fileTools);
          runButton->setUsesTextLabel(true);

          ...

          e = new QTextEdit( this, "editor" );
          e->setText("MainWindow.statusBar().hide()");
          e->setFocus();
          setCentralWidget( e );
      }

      void ApplicationWindow::script()
      {
          emit runScript(e->text());
      }

      ...

I added a toolbutton \"Run Script\". Text of script is content of QTextEdit (editor of application example)

Now we can create pro file. Remember that our qt application is shared library now.

### application.pro

- TEMPLATE        = lib
      CONFIG          += qt warn_on release
      HEADERS         = application.h
      SOURCES         = application.cpp
      TARGET          = coreapp

      unix:UI_DIR             = .ui
      unix:MOC_DIR            = .moc
      unix:OBJECTS_DIR        = .obj

      win32:UI_DIR            = .tmp
      win32:MOC_DIR           = .tmp
      win32:OBJECTS_DIR       = .tmp

So, we have compiliable small qt application with editor and button \"Run Script\". Let us to make wrapping for the application. We create dir \"coreappwrap\" where we put wrapping generated with sip. Now we create sip file for our wrappings:

### coreapp.sip

- %Module coreappwrap 0

      %Import qt/qtmod.sip

      class ApplicationWindow : QMainWindow
      {
      %TypeHeaderCode
      #include "../application.h"
      %End

      public:
          ApplicationWindow();
          ~ApplicationWindow();

      public slots:
          void newDoc();
          void choose();
          void load(const QString &);
          void save();
          void saveAs();
          void print();

          void about();
          void aboutQt();

      signals:
          void runScript(const QString&);

      };

Note, that we use #include \"../application.h\" because sip generates files to coreappwrap/. It is important to wrap our signal runScript, because it will be used in python part.

Now we create configure.py according to [Phil Thompson manual](http://www.river-bank.demon.co.uk/docs/sip/sipref.html#a-simple-c-example)

### configure.py

- import os
      import sipconfig
      import pyqtconfig

      # The name of the SIP build file generated by SIP and used by the build
      # system.
      build_file = "pyqtscripting.sbf"

      # Get the PyQt configuration information.
      config = pyqtconfig.Configuration()

      # Get the extra SIP flags needed by the imported qt module.  Note that
      # this normally only includes those flags (-x and -t) that relate to SIP's
      # versioning system.
      qt_sip_flags = config.pyqt_qt_sip_flags

      # Run SIP to generate the code.  Note that we tell SIP where to find the qt
      # module's specification files using the -I flag.
      os.system(" ".join([ \
          config.sip_bin, \
          "-c", "coreappwrap", \
          "-b", "coreappwrap/"+build_file, \
          "-I", config.pyqt_sip_dir, \
          qt_sip_flags, \
          "coreapp.sip" \
      ]))

      # Create the Makefile.  The QtModuleMakefile class provided by the
      # pyqtconfig module takes care of all the extra preprocessor, compiler and
      # linker flags needed by the Qt library.
      makefile = pyqtconfig.QtModuleMakefile(
          dir="coreappwrap",
          configuration=config,
          build_file=build_file
      )

      # Add the library we are wrapping.  The name doesn't include any platform
      # specific prefixes or extensions (e.g. the "lib" prefix on UNIX, or the
      # ".dll" extension on Windows).
      makefile.extra_libs = ["coreapp"]
      makefile.LFLAGS.append("-L..")
      makefile.LFLAGS.append("-Wl,-rpath,.")
      makefile.LFLAGS.append("-Wl,-rpath,..")

      # Generate the Makefile itself.
      makefile.generate()

We used -Wl,-rpath,. and -Wl,-rpath,.. because generated python module located in coreappwrap directory. makefile.extra_libs = [coreapp](./coreapp.html) is our Qt application that we have created with application.pro. It is libcoreapp.so.XXX files

Now it is time to compile that all. First build our Qt application:

- $ qmake application.pro
      $ make

It creates libcoreapp.so.XXX in \".\" directory

Let\'s prepare wrappings:

- $ python configure.py

It creates wrappings files in coreappwrap

And compile them

- $ cd coreappwrap
      $ make
      $ cd ..

It creates coreappwrap/coreappwrap.so. It is python module.

At the end we need to write main.py to run it all

### main.py

- import sys

      sys.path.append("coreappwrap")

      from qt import *
      from coreappwrap import *

      class RunScript(QObject):
          def __init__(self, mW):
              QObject.__init__(self)
              self.mainWindow = mW
              
          def runScript(self, script):
              MainWindow = self.mainWindow
              exec(str(script))

      a = QApplication(sys.argv)
      w = ApplicationWindow()
      r = RunScript(w)
      w.setCaption("Embeding example")
      w.show()
      a.connect(w, SIGNAL('runScript(const QString&)'), r.runScript)
      a.connect(a, SIGNAL('lastWindowClosed()'), a, SLOT('quit()') )
      a.exec_loop()

Note that \"exec\" see [MainWindow](./MainWindow.html) variable and user have access to it with scripts. You can use other variables you want to be acceessed by scripts, etc

The example (tarball ) is located at [http://yshurik.kiev.ua/PyQtScripting.tar.gz](http://yshurik.kiev.ua/PyQtScripting.tar.gz), 4k (link error) [http://yshurik.kiev.ua/PyQtScripting.zip](http://yshurik.kiev.ua/PyQtScripting.zip), 4k

You may also make corrections to this page. If you have questions or comments, send them to me at [yshurik@me.com](mailto:yshurik@me.com).
