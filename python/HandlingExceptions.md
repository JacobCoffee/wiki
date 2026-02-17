# HandlingExceptions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Handling Exceptions 

The simplest way to handle exceptions is with a \"try-except\" block:

:::: 
::: 
``` 
   1 (x,y) = (5,0)
   2 try:
   3   z = x/y
   4 except ZeroDivisionError:
   5   print "divide by zero"
```
:::
::::

If you wanted to examine the exception from code, you could have:

:::: 
::: 
``` 
   1 (x,y) = (5,0)
   2 try:
   3   z = x/y
   4 except ZeroDivisionError as e:
   5   z = e # representation: "<exceptions.ZeroDivisionError instance at 0x817426c>"
   6 print z # output: "integer division or modulo by zero"
```
:::
::::

## General Error Catching 

Sometimes, you want to catch *all* errors that could possibly be generated, but usually *you don\'t*. In most cases, you want to be as specific as possible. In the first example above, if you were using a catch-all exception clause and a user presses Ctrl-C, generating a [KeyboardInterrupt](https://docs.python.org/library/exceptions.html#KeyboardInterrupt), you don\'t want the program to print \"divide by zero\".

However, there are some situations where it\'s best to catch *all* errors.

For example, suppose you are writing an extension module to a web service. You want the error information to output the output web page, and the server to continue to run, if at all possible. But you have no idea what kind of errors you might have put in your code.

In situations like these, you may want to code something like this:

:::: 
::: 
``` 
   1 import sys
   2 
   3 try:
   4     untrusted.execute()
   5 except:  # catch *all* exceptions
   6     e = sys.exc_info()[0]
   7     write_to_page("<p>Error: %s</p>" % e)
```
:::
::::

[MoinMoin](https://moinmo.in) software is a good example of where general error catching is good. If you write MoinMoin extension macros, and trigger an error, MoinMoin will give you a detailed report of your error and the chain of events leading up to it. Python software needs to be able to catch *all* errors, and deliver them to the recipient of the web page.

Another case is when you want to do something when code fails:

:::: 
::: 
``` 
   1 try:
   2     do_some_stuff()
   3 except:
   4     rollback()
   5     raise
   6 else:
   7     commit()
```
:::
::::

By using `raise` with no arguments, you will re-raise the last exception. A common place to use this would be to roll back a transaction, or undo operations. If it\'s a matter of cleanup that should be run regardless of success or failure, then you would do:

:::: 
::: 
``` 
   1 try:
   2     do_some_stuff()
   3 finally:
   4     cleanup_stuff()
```
:::
::::

## Finding Specific Exception Names 

Standard exceptions that can be raised are detailed at:

- [https://docs.python.org/library/exceptions.html](https://docs.python.org/library/exceptions.html)

Look to class documentation to find out what exceptions a given class can raise.

# See Also: 

On this wiki: [WritingExceptionClasses](WritingExceptionClasses), [TracebackModule](./TracebackModule.html).

For general (non-Python specific) ideas about exceptions, consult [ExceptionPatterns](http://c2.com/cgi/wiki?ExceptionPatterns "Wiki").

# To Write About\... 

- Give example of IOError, and interpreting the IOError code.
- Give example of multiple excepts. Handling multiple excepts in one line.

# Questions 

## General Error Handling 

In the \"general error handling\" section above, it says to catch all exceptions, you use the following code:

:::: 
::: 
``` 
   1 import sys
   2 
   3 try:
   4     untrusted.execute()
   5 except:  # catch *all* exceptions
   6     e = sys.exc_info()[0]
   7     write_to_page("<p>Error: %s</p>" % e)
```
:::
::::

However, it originally was:

:::: 
::: 
``` 
   1 try:
   2     untrusted.execute()
   3 except Exception as e:
   4     write_to_page( "<p>Error: %s</p>" % str(e) )
```
:::
::::

Someone pointed out that \"except\" catches more than just `except Exception as e`

*Why is that the case? What is the difference?*\-- [LionKimbro](LionKimbro)

For now (version \<= 2.4) exception doesn\'t have to be inherited from Exception. Thus plain \'except:\' catches all exceptions, not only system. String exceptions are one example of an exception that doesn\'t inherit from Exception. \-- [MikeRovner](MikeRovner)

I believe that as of 2.7, exceptions still don\'t have to be inherited from Exception or even [BaseException](./BaseException.html). However, as of Python 3, exceptions *must* subclass `BaseException`. \-- [ElephantJim](./ElephantJim.html)

## Getting Useful Information from an Exception 

So, I\'ve got something like:

:::: 
::: 
``` 
   1 (a, b, c) = d
```
:::
::::

\...and Python spits back:

:::: 
::: 
``` 
   1 ValueError: unpack list of wrong size
```
:::
::::

\...and so, you naturally wonder, \"Well, what *was* in `d`?\"

You know- you can put a `print d` in there, and that works. But is there a better, more interesting way to get at that information that people know of?

You can do something like:

:::: 
::: 
``` 
   1 try:
   2     a, b, c = d
   3 except Exception as e:
   4     e.args += (d,)
   5     raise
```
:::
::::

The `.args` attribute of exceptions is a tuple of all the arguments that were passed in (typically the one and only argument is the error message). This way you can modify the arguments and re-raise, and the extra information will be displayed. You could also put a print statement or logging in the `except` block.

Note that not all exceptions subclass Exception (though almost all do), so this might not catch some exceptions; also, exceptions aren\'t required to have an `.args` attribute (though it will if the exception subclasses Exception and doesn\'t override `__init__` without calling its superclass), so the code as written might fail But in practice it almost never does (and if it does, you should fix the non-conformant exception!)

## Isn\'t it better to prevent then to remediate? 

\> [https://www.joelonsoftware.com/items/2003/10/13.html](https://www.joelonsoftware.com/items/2003/10/13.html)

Joel Spolsky might be a great C++ programmer, and his advice on user interface design is invaluable, but Python is not C++ or Java, and his arguments about exceptions do not hold in Python.

Joel argues:

\"They are invisible in the source code. Looking at a block of code, including functions which may or may not throw exceptions, there is no way to see which exceptions might be thrown and from where. This means that even careful code inspection doesn\'t reveal potential bugs.\"

(Note that this is also the argument behind Java\'s checked exceptions \-- now it is explicit that an exception can be thrown \-- except that [RuntimeException](./RuntimeException.html) can still be thrown anywhere. -jJ)

I don\'t quite get this argument. In a random piece of source code, there is no way to tell whether or not it will fail just by inspection. If you look at:

    x = 1
    result = myfunction(x)

you can\'t tell whether or not myfunction will fail at runtime just by inspection, so why should it matter whether it fails by crashing at runtime or fails by raising an exception?

(Crashing is bad. By explicitly declaring the exception, you warn people that they may want to handle it. Java does this awkwardly. C doesn\'t have a good way to do it at all, because the error returns are still in-band for regular returns. In python, passthrough exceptions aren\'t marked, but error conditions stand out where they are created, and they don\'t usually mimic valid returns. -jJ)

Joel\'s argument that raising exceptions is just a goto in disguise is partly correct. But so are for loops, while loops, functions and methods! Like those other constructs, exceptions are gotos tamed and put to work for you, instead of wild and dangerous. You can\'t jump \*anywhere\*, only highly constrained places.

Joel also writes:

\"They create too many possible exit points for a function. To write correct code, you really have to think about every possible code path through your function. Every time you call a function that can raise an exception and don\'t catch it on the spot, you create opportunities for surprise bugs caused by functions that terminated abruptly, leaving data in an inconsistent state, or other code paths that you didn\'t think about.\"

(Even now, a fairly high percentage of the bugs found in CPython\'s C code are memory leaks caused by premature exits \-- exactly what Joel warned about. It isn\'t such a problem with python code, because the language is supposed to take care of fixing accounting-type invariants for you. -jJ)

This is a better argument for \*careful\* use of exceptions, not an argument to avoid them. Or better still, it is an argument for writing code which doesn\'t has side-effects and implements data transactions. That\'s a good idea regardless of whether you use exceptions or not. (In python, \"transactions\" are small enough that it is usually difficult to interrupt an operation inside one without writing C code. You \*can\* do it, say, with recursive generators, but it is difficult.)

Joel\'s concern about multiple exit points is good advice, but it can be taken too far. Consider the following code snippet:

    def myfunc(x=None):
       result = ""
       if x is None:
           result = "No argument given"
       elif x == 0:
           result = "Zero"
       elif 0 < x <= 3:
           resutl = "x is between 0 and 3"
       else:
           result = "x is more than 3"
       return result

There is no benefit in deferring returning value as myfunc does, just for the sake of having a single exit point. \"Have a single exit point\" is a good heuristic for many functions, but it is pointless make-work for this one. (In fact, it increases, not decreases, the chances of a bug. If you look carefully, myfunc above has such a bug in the \"0 \< x \<= 3\" clause.)

Used correctly, exceptions in Python have more advantages than disadvantages. They aren\'t just for errors either: exceptions can be triggered for exceptional cases (hence the name) without needing to track (and debug) multiple special cases.

Lastly, let me argue against one of Joel\'s comments:

\"A better alternative is to have your functions return error values when things go wrong, and to deal with these explicitly, no matter how verbose it might be. It is true that what should be a simple 3 line program often blossoms to 48 lines when you put in good error checking, but that\'s life, and papering it over with exceptions does not make your program more robust.\"

Maybe that holds true for C++. I don\'t know the language, and wouldn\'t like to guess. But it doesn\'t hold true for Python.

(The difference is that Python reduces the chances of an error in the first place, and makes raising an exception the clean way to \"return an error value\". It is definately a cleaner way to pass through an error value that was generated by something you called.)

This is how Joel might write a function as a C programmer:

    def joels_function(args):
        error_result = 0
        good_result = None
        process(args)
        if error_condition():
            error_result = -1  # flag for an error
        elif different_error_conditon():
            error_result = -2
        else:
            more_processing()
            if another_error_conditon():
                error_result = -3
            do_more_work()
            good_result = "Success!"
        if error_result != 0:
            return (False, error_result)
        else:
            return (True, good_result)

and then call it with:

    status, msg = joels_function(args)
    if status == False:
        print(msg)
        # and fail...
    else:
        print(msg)
        # and now continue...

This is how I would write it in Python:

    def my_function(args):
        process(args)
        if error_condition():
            raise SomeError("An error occurred")
        elif different_error_conditon():
            raise SomeError("A different error occurred")
        more_processing()
        if another_error_conditon():
            raise SomeError("Another error occurred")
        do_more_work()
        return "Success!"

and call it with:

    try:
        print(my_function(args))
    except SomeError as msg:
        print(msg)
        # and fail...
    # and now continue safely here...

In the case of Python, calling a function that may raise an exception is no more difficult or unsafe than calling a function that returns a status flag and a result, but writing the function itself is much easier, with fewer places for the programmer to make a mistake. (The one difference is that if you don\'t handle the error, your program will stop and complain, instead of continuing and corrupting the data.)

In effect, exceptions allow the Python programmer to concentrate on his actual program, rather than be responsible for building error-handling infrastructure into every function. Python supplies that infrastructure for you, in the form of exceptions.

(I\'m sorry, but if you had actually done much programming in C++, you\'d know that there\'s not much difference between the two languages when it comes to exceptions, at least unless you program C++ in the old-fashioned C-like way with new\'s and delete\'s sprinkled everywhere. You\'re basically dismissing Joel\'s argument. This whole section is a bit weak, maybe it would be better to just state \"don\'t overuse exceptions as that can lead to hard-to-verify spaghetti code\" and be done with it ![:)](/wiki/europython/img/smile.png ":)") \--olau)

------------------------------------------------------------------------

See also: Italian translation at [ManutenereLeEccezioni](ManutenereLeEccezioni).
