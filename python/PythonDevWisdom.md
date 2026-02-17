# PythonDevWisdom

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Useful, practical notes and code snippets from the python-dev mailing list 

### Managing refcounts for arg to PyArg_ParseTuple 

After an 8-hour bug hunt, Tim Peters [noted this bit of wisdom](http://mail.python.org/pipermail/python-dev/2003-April/034557.html)

- *Word to the wise: don\'t ever try to reuse a variable whose address is passed to `PyArg_ParseTuple`{.backtick} for anything other than holding what `PyArg_ParseTuple`{.backtick} does or doesn\'t store into it. You\'ll never get the decrefs straight (and even if you manage to at first, the next person to modify your code will break it).*

Qualification: this really refers just to `PyObject*`{.backtick} pointers.

Reason: if p is `PyObject*`{.backtick}, and &p is passed to `PyArg_ParseTuple`{.backtick}, p either retains its initial value (probably NULL), or gets a **borrowed** reference to an object. In the former case `Py_DECREF()`{.backtick} is wrong, and in the latter case a potential disaster (p will eventually get decrefed to 0, and the memory will get recycled then, earlier than it should \-- which may be gazillions of cycles after you screwed up in the function calling `PyArg_ParseTuple`{.backtick}). If on some other path thru the code, you decide to reuse the vrbl name to hold a new, temporary Python object, you almost certainly need to decref that one before returning (else its memory will leak). Then you\'ve got one name that must, or must not, be decrefed upon exit, \"depending\". The real bitch is that screwups here usually occur on error paths, so are rare.

### Don\'t be overly afraid of goto. 

Refcounts are much easier to keep straight if you use forward gotos for error exits. Initialize your `PyObject*`{.backtick} locals to NULL, and write a sequence of matching `Py_XDECREF`{.backtick} calls following the error label. This is essentially compiling a `try/except`{.backtick} block by hand.

## Other snippets 

### Python changes line endings for you 

If you open a file in text mode, and send out the newline character \'\\n\' then Python will substitute the contents of os.linesep. Similarly, if you are reading a file and Python encounters the os.linesep sequence it will substitute the newline character. (This will happen ONLY to files opened in text mode, files opened in binary mode will not perform any conversion.)

For example, if you have this code in Windows:

:::: 
::: 
``` 
   1     fOutputFile = open("output.txt", "w")
   2     fOutputFile.write("A\r\nB")
   3     fOutputFile.close
```
:::
::::

then output.txt will contain, in hex: `0x41 0x0d 0x0d 0x0a 0x42`. That\'s because os.linesep under Windows is `0x0d 0x0a`.

To ensure that you get the correct line endings for your operating system, the correct way to do this is to just put \\n in your string. However, if you require the line ending `0x0d 0x0a` no matter which operating system is being used, you have to open the file in binary mode:

:::: 
::: 
``` 
   1     fOutputFile = open("output.txt", "wb")
   2     fOutputFile.write("A\r\nB")
   3     fOutputFile.close
```
:::
::::
