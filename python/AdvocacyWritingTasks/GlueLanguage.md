# AdvocacyWritingTasks/GlueLanguage

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python as a Glue Language

::: 
### Introduction

The Python® language interpreter can be used as a glue language to connect software components. Components can then be manipulated by Python scripts and combined in new ways.

What can you do with scripting access to an existing system?

- Providing adaptability
- Scripting small tasks
- Testing
- Education and initial learning
- Use external libraries for performance or features
:::

::: 
### C/C++ Systems

The most widely used Python interpreter is the C implementation available from [http://www.python.org/](http://www.python.org/) and included in Mac OS X® and many Linux distributions. A Microsoft Windows® version is available from [http://www.python.org/](http://www.python.org/). There are a variety of tools to interface between Python and C code.
:::

::: 
### ctypes

The ctypes package is a foreign-function interface included with Python 2.5 and later versions that can load shared libraries (.dylib files on MacOS X, .so files on Linux, DLLs on Windows) and call arbitrary library functions.

The following example from the pyglet multimedia library uses ctypes to wrap some XLib functions:

    import ctypes
    from ctypes import *
    from ctypes.util import find_library as _find_library

    _libpath = _find_library('X11')
    if not _libpath:
        raise ImportError('Could not locate X11 library')
    _lib = cdll.LoadLibrary(_libpath)

    XLoadQueryFont = _lib.XLoadQueryFont
    XLoadQueryFont.restype = POINTER(XFontStruct)
    XLoadQueryFont.argtypes = [POINTER(Display), c_char_p]

    XSetAfterFunction = _lib.XSetAfterFunction
    XSetAfterFunction.restype = POINTER(CFUNCTYPE(c_int, POINTER(Display)))
    XSetAfterFunction.argtypes = [POINTER(Display), CFUNCTYPE(c_int, POINTER(Display))]

For more information about ctypes, refer to the ctypes section in the Python documentation ([2.5 version](http://docs.python.org/lib/module-ctypes.html)).
:::

::: 
### Pyrex

Pyrex ([http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/](http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/)) is a compiler that translates a Python-like language into C code for an extension module.

The following example is taken from the Pyrex wrapper for libxel ([https://gna.org/projects/libxel](https://gna.org/projects/libxel)), an event logging library:

    cdef extern from "xel/xel.h":
      int   xelInit(char *)
      void  xelShutdown(int)
      char *xelBegin(char *, int, int)
      int   xelEnd()
      void  xelEnable(int)
      int   xelEventF(int, char *, int, char *, char *, char *)
      int   xelExportXML(char *, char *, char *)
      int   xelExportCSV(char *, char *)
      int   xelCheckError()
      char *xelGetError()
      char *xelGetVersion()

    class XEL:

      def __init__(self, filename=''):
        self.sid = None
        if xelInit(filename) == self.ERROR:
          raise XELError(self.geterror())

      def __del__(self):
        self.end()
        xelShutdown(self.VACUUM)

      def begin(self, name, level=LEVEL_ALL, syschk=SYSCHK_ALL):
        self.sid = xelBegin(name,level,syschk)
        if not self.sid:
          raise XELError(self.geterror())

      def end(self):
        if self.sid:
          xelEnd()
:::

::: 
### SWIG for C/C++ libraries across languages

SWIG, the Simple Wrapper Interface Generator ([http://www.swig.org/](http://www.swig.org/)), parses C/C++ header files and custom interface descriptions, generating C code for an extension wrapping the C functions and data types. SWIG can use the same input to generate wrappers for several different language environments; supported languages other than Python include Perl, Tcl, Ruby, PHP, Java, and Common Lisp.

The following partial examples were taken from the SWIG bindings for the Subversion version control system ([http://subversion.tigris.org/](http://subversion.tigris.org/)):

    %include svn_global.swg

    %{
    #include <apr.h>
    #include <apr_general.h>

    #include "svn_md5.h"
    #include "svn_diff.h"
    %}

    #ifdef SWIGPYTHON
    %typemap(in) FILE * {
        $1 = PyFile_AsFile($input);
        if ($1 == NULL) {
            PyErr_SetString(PyExc_ValueError, "Must pass in a valid file object");
            SWIG_fail;
        }
    }
    #endif

    /* -----------------------------------------------------------------------
       wrap some specific APR functionality
    */

    apr_status_t apr_initialize(void);
    void apr_terminate(void);

    apr_status_t apr_time_ansi_put(apr_time_t *result, time_t input);

    void apr_pool_destroy(apr_pool_t *p);
    void apr_pool_clear(apr_pool_t *p);
:::

::: 
### Boost.Python for C++ libraries

Boost.Python ([http://www.boost.org/libs/python/doc/](http://www.boost.org/libs/python/doc/)) is a framework for wrapping C++ classes and functions as Python extensions without requiring any modifications to the original C++ code or headers.

The following example, taken from the pyactivemq project ([http://code.google.com/p/pyactivemq/](http://code.google.com/p/pyactivemq/)), wraps the `Message` class from the ActiveMQ-CPP library:

    #include <boost/python.hpp>
    #include <cms/Message.h>

    using namespace boost::python;
    using cms::Message;

    void export_Message()
    {
        class_<Message, boost::noncopyable>("Message", no_init)
            .def("acknowledge", &Message::acknowledge)
            .def("clearBody", &Message::clearBody)
            .def("clearProperties", &Message::clearProperties)
            .add_property("propertyNames", &Message::getPropertyNames)
            .def("propertyExists", &Message::propertyExists)
            .def("getBooleanProperty", &Message::getBooleanProperty)
            .def("getByteProperty", &Message::getByteProperty)
            .def("getDoubleProperty", &Message::getDoubleProperty)
            .add_property("correlationID", &Message::getCMSCorrelationID,
                          &Message::setCMSCorrelationID)
            .add_property("deliveryMode", &Message::getCMSDeliveryMode,
                          &Message::setCMSDeliveryMode)
            .add_property("destination",
                          make_function(&Message::getCMSDestination,
                                        return_internal_reference<>()),
                          make_function(&Message::setCMSDestination,
                                        with_custodian_and_ward<1,2>()))
            .add_property("messageID", &Message::getCMSMessageID,
                          &Message::setCMSMessageID)
            .add_property("type", &Message::getCMSType, &Message::setCMSType)
            ;
    }

This wrapper can be compiled using the Boost tools to produce a shared library that Python can import and use as a module.
:::

::: 
### SIP for C++ libraries

SIP ([http://www.riverbankcomputing.co.uk/sip/](http://www.riverbankcomputing.co.uk/sip/)) parses interface specifications to create Python bindings for C and C++ libraries. Originally written for wrapping the Qt® libraries from Trolltech®, SIP is now used for other projects as well.

The following SIP example wraps a C++ class called `Word`, making the class constructor and the `reverse()` method available as a Python module called `word`.

    // Define the SIP wrapper to the word library.

    %Module word 0

    class Word {

    %TypeHeaderCode
    #include <word.h>
    %End

    public:
        Word(const char *w);

        char *reverse() const;
    };
:::

::: 
### Python\'s C API

The Python interpreter has a documented C API for writing extension modules. Writing simple wrappers atop a C library is a straightforward task

The following example from Python\'s source code wraps the `is_term_resized()` function provided by the `curses` screen-handling library:

    static PyObject *
    PyCurses_Is_Term_Resized(PyObject *self, PyObject *args)
    {
      int lines;
      int columns;
      int result;

      if (!PyArg_ParseTuple(args,"ii:is_term_resized", &lines, &columns))
        return NULL;
      result = is_term_resized(lines, columns);
      if (result == TRUE) {
        Py_INCREF(Py_True);
        return Py_True;
      } else {
        Py_INCREF(Py_False);
        return Py_False;
      }
    }
:::

::: 
### Embedding Python

The most common approach for integrating Python into a system is to write extension modules that can then be used by Python scripts. In this approach, the Python interpreter is the top-level component, the one that controls the overall logic of the application.

It\'s also possible to embed Python within an application, leaving the application as the top level and calling Python functions or executing strings containing code as required by the application. For example, Vim uses Python as a scripting language.

The following example is taken from the \"Extending and Embedding the Python Interpreter\", part of Python\'s documentation set ([http://docs.python.org/ext/](http://docs.python.org/ext/)). The example takes the filename of a Python file, a function name, and optional string arguments, and calls the function passing the provided arguments.

    #include <Python.h>

    int
    main(int argc, char *argv[])
    {
        PyObject *pName, *pModule, *pDict, *pFunc;
        PyObject *pArgs, *pValue;
        int i;

        if (argc < 3) {
            fprintf(stderr,"Usage: call pythonfile funcname [args]\n");
            return 1;
        }

        /* Initialize interpreter */
        Py_Initialize();

        /* Error checking of pName left out */
        pName = PyString_FromString(argv[1]);
        pModule = PyImport_Import(pName);
        Py_DECREF(pName);

        if (pModule != NULL) {
            pFunc = PyObject_GetAttrString(pModule, argv[2]);
            /* pFunc is a new reference */

            if (pFunc && PyCallable_Check(pFunc)) {
                pArgs = PyTuple_New(argc - 3);
                for (i = 0; i < argc - 3; ++i) {
                    pValue = PyInt_FromLong(atoi(argv[i + 3]));
                    if (!pValue) {
                        Py_DECREF(pArgs);
                        Py_DECREF(pModule);
                        fprintf(stderr, "Cannot convert argument\n");
                        return 1;
                    }
                    /* pValue reference stolen here: */
                    PyTuple_SetItem(pArgs, i, pValue);
                }
                pValue = PyObject_CallObject(pFunc, pArgs);
                Py_DECREF(pArgs);
                if (pValue != NULL) {
                    printf("Result of call: %ld\n", PyInt_AsLong(pValue));
                    Py_DECREF(pValue);
                }
                else {
                    Py_DECREF(pFunc);
                    Py_DECREF(pModule);
                    PyErr_Print();
                    fprintf(stderr,"Call failed\n");
                    return 1;
                }
            }
            else {
                if (PyErr_Occurred())
                    PyErr_Print();
                fprintf(stderr, "Cannot find function \"%s\"\n", argv[2]);
            }
            Py_XDECREF(pFunc);
            Py_DECREF(pModule);
        }
        else {
            PyErr_Print();
            fprintf(stderr, "Failed to load \"%s\"\n", argv[1]);
            return 1;
        }
        Py_Finalize();
        return 0;
    }
:::

::: 
### Jython for Java Components

For systems written in Java蒂, Jython ([http://www.jython.org/](http://www.jython.org/)) is an implementation of Python written in pure Java that provides automatic access to Java classes from both scripts and an interactive prompt.

The following small script demonstrates using Swing from Jython, and is taken from the first chapter of \"Jython Essentials\" by Samuele Pedroni and Noel Rappin, published by O\'Reilly & Associates ([http://www.oreilly.com/catalog/jythoness/](http://www.oreilly.com/catalog/jythoness/)):

    import java.lang as lang
    import javax.swing as swing
    import java.awt as awt

    names = ["Groucho", "Chico", "Harpo"]
    quotes = {"Groucho": "Say the secret word",
            "Chico": "Viaduct?", "Harpo": "HONK!"}

    def buttonPressed(event):
         field.text = quotes[event.source.text]

    def exit(event):
        lang.System.exit(0)

    def createButton(name):
        return swing.JButton(name, preferredSize=(100,20),
                actionPerformed=buttonPressed)

    win = swing.JFrame("Welcome to Jython", size=(200, 200),windowClosing=exit)
    win.contentPane.layout = awt.FlowLayout(  )

    field = swing.JTextField(preferredSize=(200,20))
    win.contentPane.add(field)

    buttons = [createButton(each) for each in names]
    for eachButton in buttons:
        win.contentPane.add(eachButton)
    win.pack()
    win.show()
:::

::: 
### IronPython for CLR Components

IronPython, an implementation of Python written in C#, provides automatic access to CLR/.NET assemblies. IronPython runs on both Microsoft® .NET and on Novell® Mono. The IronPython web site is at [http://www.codeplex.com/Wiki/View.aspx?ProjectName=IronPython](http://www.codeplex.com/Wiki/View.aspx?ProjectName=IronPython).

The following small script demonstrates using the Windows Forms API from IronPython, and is taken from Michael Foord\'s IronPython/Windows Forms tutorial at \<[http://www.voidspace.org.uk/ironpython/winforms/index.shtml](http://www.voidspace.org.uk/ironpython/winforms/index.shtml)\>:

    import sys
    sys.path.append(r'C:\Python24\Lib')

    import clr
    clr.AddReference("System.Drawing")
    clr.AddReference("System.Windows.Forms")

    from System.Drawing import Point
    from System.Windows.Forms import Application, Button, Form, Label

    class HelloWorldForm(Form):
        def __init__(self):
            self.Text = 'Hello World'

            self.label = Label()
            self.label.Text = "Please Click Me"
            self.label.Location = Point(50, 50)
            self.label.Height = 30
            self.label.Width = 200

            self.count = 0

            button = Button()
            button.Text = "Click Me"
            button.Location = Point(50, 100)

            button.Click += self.buttonPressed

            self.Controls.Add(self.label)
            self.Controls.Add(button)

        def buttonPressed(self, sender, args):
            print 'The label *used to say* : %s' % self.label.Text
            self.count += 1
            self.label.Text = "You have clicked me %s times." % self.count

    form = HelloWorldForm()
    Application.Run(form)
:::

::: 
### Legal

Python is a registered trademark of the Python Software Foundation.

Java is a registered trademark of Sun Microsystems, Inc. in the United States and other countries.

Mac OS is a trademark of Apple Inc., registered in the U.S. and other countries.

Mono is a trademark of Novell, Inc. in the United States and other countries.

.NET

Qt is a trademark of Trolltech in Norway, the United States and other countries.

Tcl

Windows is a registered trademark of Microsoft Corporation in the United States and other countries.
:::
