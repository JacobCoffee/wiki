# TestHarnessDesign

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Over the next couple of hours a wrote a crude shell (in Python) for sending commands and key sequences to the phone, and reading back raw serial responses and screens back. While crude this shell does offer command editing and history (via [readline](http://docs.python.org/lib/module-readline.html)) with automatically persistent history, it saves logs of all output to the phone (seperate logs for raw serial commands and for the key sequences which are embedded therein) and all input read back from the phone (again in separate streams, for raw characters read from the device and for each screenshot I take), and it allows me to insert comments into the history and log files (so I can take notes in the shell that I can correlate to specific entries in the logs).

Also my crude interactive shell uses the [optparse](http://docs.python.org/lib/module-optparse.html) module to initialize my serial connection (different phones have different speeds and are connected to different ports \-\-- I have an 8-port Moxa board installed on the Linux desktop workstation). I also played a littled with [ConfigParser](http://docs.python.org/lib/module-ConfigParser.html) so I could store most of the connection details and log file names in an .ini file and just call my script with a label representing which phone/port I want to play with.

So that was about four hours of scripting. My boss was impressed, but really it\'s only about 150 lines of code. [PySerial](PySerial), readline, and [ConfigParser](ConfigParser) are really doing all of the work. I\'m not so easily impressed with myself. That was just some throwaway scripting to help me understand the tools. There\'s no design, and I didn\'t see an easy way to use this shell\'s artifacts (log files) to automate any sort of playback. Also a lack of loop and condition handling makes it unsuitable for doing things like adding 99 entries to the phone\'s built-in address book, validate that they\'re all there, ensure that it gives this particular error when you try to add another, etc. (I wrote that up as another, stand alone, script, which is still semi-blind and offers almost no code reuse).

My point in posting all this is to solicit advice on a robust design for a real test harness. I\'m reasonably good at scripting but not experienced in design and have almost no formal CS training.

I\'ve been looking at packages like [PExpect](http://pexpect.sourceforge.net/) (*Expect* for Python), and at the [doctest](http://docs.python.org/lib/module-doctest.html) and [unittest](http://docs.python.org/lib/module-unittest.html) standard libraries, as well as some of the discussions around [c2.com:TestingFrameWork](http://c2.com/cgi/wiki?TestingFramework) for inspiration.

One thing I\'ve started doing is writing some psuedo-Python-code. These show what I might like my tests to look to a colleague who was charged with writing more of them. At first I thought of something that wasn\'t code at all but something like:

    >> 1234 Menu Down Down Enter 12*Down Enter Enter Esc
    << "Add a Phone Entry\nName:"
    >> "John" Enter
    << "Address:"
    >> SIP:169.254.1.1
    << "Speed Dial Entry:"
    >> Enter

(Simple \"send this,\" and \"expect that\" sequences). However, I realized that this would be far too limiting. I need to be able to do loops, handle conditions, and create higher level methods that build on these primitives. Also I\'m sure that there are many undiscovered requirements that will need to be implemented. So I scrapped that idea before coding any of it (though my throwaway shell does output files similar to this).

Then I thought about creating a class and using it something like:

:::: 
::: 
``` 
   1 # ...
   2 tst = PhoneTest(port='/dev/ttyM0', speed=9600, ...)
   3 tst.send("# a raw text command")
   4 if not tst.expect("# some raw response"):
   5    tst.fail("some failure message")
   6 tst.key("#keys parsed by name")
   7 if not tst.screen("# some screen substring or regex"):
   8    tst.fail("some other failure message")
   9 # ...
```
:::
::::

This is a bit better. I can also implement methods like **`setFactoryDefaults()`{.backtick}** and **`selectMenu()`{.backtick}** and I can have the [PhoneTest](./PhoneTest.html) class instantiate and contain a Phone object which abstracts some things (like the fact that accessing the menus on some models takes two keys rather than one key, and that the \"Enter\" key symbol is called \"OK\" on it, etc). (My function to send key sequences parses abstract common key notation into a dictionary of dictionaries keyed by each phone model and returning the real key symbols and sequences, it has to do things like press 2 three times for a letter \"c\" and detect if the next letter/digit is on the same button to pause for a full second to make the phone \"take\" that letter).

Obviously this exposes our responses and screen captures to Python\'s own conditional handling.

In this model, doing loops (adding 99 phone entries) is pretty easy:

:::: 
::: 
``` 
   1 # ....
   2 for i in range(99):
   3   tst.menuSelect("Add Phonebook Entry")
   4   if tst.screen() != "Name: ":
   5      tst.fail(tst.screen())
   6 # ...
```
:::
::::

\... *etc.*

However, it\'s still not very good. Obviously I have to report all my results (text output for now, later posting to a MySQL database). I\'ll also need options for debugging and logging (shades of [AspectOrientedProgramming](./AspectOrientedProgramming.html)?). I suppose the [PhoneTest](./PhoneTest.html) object can also contain a reporting object to handle that abstractly.

My main objection to this interface is that **all** the conditional logic is exposed. It seems silly to repeatedly type: `tst.key(...); if tst.screen(...) ...`{.backtick} and it clutters the flow of the test case. It\'s not data driven at all. Of course I can hide `tst.fail()`{.backtick}, and `tst.expect()`{.backtick} inside `tst.screen()`{.backtick}

Then I\'m back to something more linear like:

:::: 
::: 
``` 
   1 # ...
   2 tst = PhoneTest(port='/dev/ttyM0', speed=9600, ...)
   3 tst.send("# a raw text command")
   4 tst.expect("# some raw response") # fails if response not found
   5 tst.key("#keys parsed by name")
   6 tst.screen("# some screen substring or regex"):
   7 for i in range(99):
   8   tst.menuSelect("Add Phonebook Entry")
   9   tst.screen() != "Name: "
  10 # ...
```
:::
::::

\... where all the failures are implicit.

For some reason this just looks **wrong** to me. (It would violate the principle of least surprise to a Python coder, hiding all of the reporting logic inside the objects and having success determined implicitly by fall through)!

Another problem is that some of these screens will have variable data embeded in them (time of day, connection results, *etc.* and I need more flexible ways of determining if a given screen (or raw text response) is actually a success or failure. Also I have to be account for differences in screen size among the models of phone.

Meanwhile this format looks almost like the first one, with *\<\<* and *\>\>* replaced by *tst.key()* and *tst.screen()* respectively. In other words for the simple case it\'s just more cluttered.

A thought I had to address one of those issues involves building and maintaining a dictionary of screens for each phone model. Then in the the `tst.screen('XXX')`{.backtick} calls \'XXX\' becomes a key into the dictionary (or I just extend the `.screen`{.backtick} method to accept a string, a regex, **or** a key=\'keyName\' keyword argument).

If I use keyword arguments and since I usually need sequences of \"send this\" **and** \"expect that\" I might change things more by implementing a `.__call__()`{.backtick} methode which looks something like:

:::: 
::: 
``` 
   1 # ...
   2 tst = PhoneTest(port='/dev/ttyM0', speed=9600, ...)
   3 tst( send=" a raw text command"         expect="some response")
   4 tst( key="key sequence",                screen='screenName')
   5 for i in range(99):
   6   tst.menuSelect("Add Phonebook Entry" screen=re.compile('some regexp'))  # dynamically use string or regex object
   7   
   8 # ...
```
:::
::::

It\'s more terse but it doesn\'t actually look less cluttered. I also still don\'t like hiding the failure/reporting so deeply inside the class methods.

One of my objectives is to write a test harness that others will be using \-\-- that they\'ll be coding up their own test cases into long after I\'ve moved on. Another is to creating something that\'s reasonably similar to what we\'ll be using to test other interfaces (these phonse have web interfaces as well as the serial ones I\'ve described) and to test functionality beyond just what the screen displays in response to various button events and other commands. For example I know that later test cases will require me to initiate calls from one device to another and interact with the receiving device to see that the call was actually receieved. I\'ll also probably need to correlate some of my regressions to specific network capture behaviors. So I might need to use [PyCap](http://pycap.sourceforge.net/) (libpcap interface), for example.

(There\'s all sorts of work that\'s been done on HTTP automation in Python from the basic [socket](http://docs.python.org/lib/module-socket.html), and [httplib](http://docs.python.org/lib/module-httplib.html) standard libraries through the [ClientForm](http://wwwsearch.sourceforge.net/) and ClientCookie modules and [Puffin](http://www.puffinhome.org/docs.htm) up through Frank Cohen\'s [TestMaker](http://www.pushtotest.com/) (in [Jython](http://www.jython.org)).

The other thing I don\'t like about this last speculative psuedo-code is that it\'s still too cluttered for the most common case. I don\'t see a way for tests to be more data driven and less entwined in the code.

Another idea I\'ve been toying with is creating a mess of classes and subclasses. There\'s be a `TestCase`{.backtick} class with various descendents for different classes of tests; a `Phone`{.backtick} class with descendents for each model of phone, a `TestBaseException`{.backtick} and many descendents for each type of test failure. Each descendent of the `TestCase`{.backtick} would implement a `.run()`{.backtick} method and would `raise`{.backtick} exceptions from the `TestBaseException`{.backtick} family. I suppose that model would appeal to the OO purist in some way. However I\'m not seeing how I\'d actually instantiate and call the `.run()`{.backtick} methods of each of these subclasses.

:::: 
::: 
``` 
   1 tst = Add99Entries(model='xx' port='/dev/ttyM0')
   2 tst.run()
   3 tst2 + RegressBug999()  # settings pulled from INI file or database?
   4 # ...
```
:::
::::

I don\'t see it. This isn\'t data driven at all. Where do I maintain the list of available tests and the sequencing?

I\'ve also thought of something like:

:::: 
::: 
``` 
   1 # ...
   2 try:
   3    tst.idle()
   4    tst.keys('some key squence')
   5    tst.screen('screenName')
   6    # ...
   7 except TestCaseError, e:
   8    tst.fail(e.args)
   9 # ...
```
:::
::::

\... which looks reasonable. It doesn\'t completely hide the failures. At least it makes it obvious to a Python coder that these `tst`{.backtick} methods are expected to `raise`{.backtick} errors; and it lets me catch different subclasses of errors and handle them differently (with multiple `except`{.backtick} clauses ordered from most specific towards more general). That will be import, for example, since I will have pre-condition and setup methods and exceptions that should be raised and reported to the operator but should **not** be recorded as bugs to the developers; they are errors in the test harness or hardware set-up rather than bugs in the target of our testing.

So, that\'s an overview of my thoughts. These are possible approaches. Of course I\'ve only just started. Meanwhile I will re-write my interactive shell script (probably using the [Cmd](http://docs.python.org/lib/module-cmd.html) class or something out of [IPython](http://ipython.scipy.org/)). I will create my core `TestCase`{.backtick} and `Phone`{.backtick} classes (along with `Feedback`{.backtick} and `Reporter`{.backtick} classes), and start creating tables of keys, menus and screens for each phone; and methods to load, access, compare, and manage them.

Unfortunately none of what I\'m coding here can be released to open source (grump) but I hope that the discussion will still be entertaining and maybe even a little enlighteing for all.

I\'m hoping others will chew on these notions and spit on them mercilessly. Of course I\'m also hoping for some pointers to similar code; tools, or just a really good guide to test case/harness/framework design.

*I see you\'ve looked at the [unittest](http://docs.python.org/lib/module-unittest.html) module that comes with the standard Python distribution. In what ways is that lacking? Have you looked at Holger Krekel\'s [py.test](http://codespeak.net/py/current/doc/test.html) library?*

In any event, unless there\'s an outcry against my verbosity, I\'ll update this page as I work on the problem (and as I incorporate any good suggestioins).
