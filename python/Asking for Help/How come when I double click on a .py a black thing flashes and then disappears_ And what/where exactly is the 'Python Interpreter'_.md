# Asking for Help/How come when I double click on a .py a black thing flashes and then disappears? And what/where exactly is the 'Python Interpreter'?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: How come when I double click on a .py a black thing flashes and then disappears? And what/where exactly is the \'Python Interpreter\'? 

It seems like you\'re using Windows from the question. The \"black thing\" is called a \"console\", \"command line prompt\" or \"terminal\" depending on which person you ask, and it\'s the \"advanced\" way of accessing the programs and files on your computer. Usually you don\'t see it unless you go into the \"Start\" menu and find it, but Python programs ending in `.py`{.backtick} cause it to open while they are running because the program might write out some text, and the console is the standard way of showing such text - this dates back to the time of MS-DOS, but other systems also use the same kind of thing.

The console appears and disappears because the program finishes, possibly very quickly, and you don\'t get to see the messages produced by the program. It may be the case that the program needed to be run in a particular way and complained before exiting straight away and leaving you without any lasting indication of why it exited. Some programs should actually be started in the console so that you can see such messages and possibly interact with them using the keyboard in a basic text-only fashion.

Many programs are designed to work normally when double-clicking on a `.py`{.backtick} file and may produce a graphical interface with windows and icons, just like \"normal\" Windows applications. In such cases, opening the console is a distraction and unnecessary. On Windows, such programs usually have the `.pyw`{.backtick} ending on their filenames, indicating that the console is not supposed to be opened when the program is run. You could rename `.py`{.backtick} programs to end with `.pyw`{.backtick}, but it might be worth finding the instructions for such programs and seeing how they are supposed to be used first.

As for the Python interpreter, it is the software which understands Python code (in the `.py`{.backtick} and `.pyw`{.backtick} files) and makes it work. On Windows, the interpreter software is typically found somewhere in the Program Files folder.

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
