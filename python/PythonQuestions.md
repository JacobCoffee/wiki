# PythonQuestions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Add your questions here and we\'ll do our best to answer them.

![/!\\](/wiki/europython/img/alert.png "/!\") If you subscribe to this page you will be notified when it changes. That way you can easily tell if/when your question has been answered.

But see also:

- The [Python FAQ Wizard](http://www.python.org/cgi-bin/faqw.py).

- The FAQTs [knowledge base](http://www.faqts.com/knowledge_base/index.phtml/fid/199).

- [PythonFaq](http://purl.net/wiki/python/PythonFaq "EfnetPythonWiki") on #Python wiki.

- The [Infrequently Asked Questions](http://norvig.com/python-iaq.html) list maintained by [Peter Norvig](http://norvig.com).

- [Python20FrequentlyAskedQuestions](Python20FrequentlyAskedQuestions) (archive)

------------------------------------------------------------------------

## Win 95 Installation 

**Q.** I run a Windows 95 200 MHz Compaq computer, when I tried to install Python 2.0, the installation program consistently crashes/freezes at 52% of the process. Can you give me any suggestions?

**A.** Make sure you have enough disk space. Accept the default choices the installer suggests. Make sure all other programs are killed first, especially virus scanners (use Ctrl+Alt+Del repeatedly to kill off everything except Explorer and Systray). Try a more recent version of Python (like 2.2.1), which uses better installer technology. Try an [ActiveState](ActiveState) installer, which uses completely different installer technology. Try the minimalist [PythonWare](./PythonWare.html) installer, which seems to amount to an automated unzip. Accept that Microsoft no longer supports Win95 and plan to get another OS.

## pyexpat Module 

**Q.** I just downloaded version 2.0. When I try to run the test_sax.py module it complains that it can\'t find the driver pyexpat.py. I looked in the distribution and it doesn\'t seem to be there? I\'m running on Solaris 2.7. Thank You.

**A.** The pyexpat module is a compiled extension module. See the comments in the Modules/Setup file for instructions on getting and building the required C library. Once you\'ve built that, enable the module in the Modules/Setup file and type \"make\" in the top level of the Python source tree. \"make \--install\" will re-install Python for you, or you can copy Modules/pyexpat.so to \$exec_prefix/lib/python2.0/lib-dynload/ if you\'re building modules as shared objects.

## Documentation in Windows Helpfile Format 

**Q.** Where do I get the documentation for Python in the CHM (Compiled HTML) format?

**A.** See [http://www.orgmf.com.ar/condor/pytstuff.html](http://www.orgmf.com.ar/condor/pytstuff.html).

**A.** Since version 2.3 included in Windows distribution.

## Windows XP look-and-feel 

**Q.** How can I make [WxPython](WxPython) on Windows XP assume XP look-and-feel?

**A.** Put two files **python.exe.manifest** and **pythonw.exe.manifest**, both with the following contents:

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
    <assemblyIdentity version="1.0.0.0" processorArchitecture="X86" name="*.*.*" type="win32" />
    <description>*</description>
    <dependency>
    <dependentAssembly>
    <assemblyIdentity type="win32" name="Microsoft.Windows.Common-Controls"
     version="6.0.0.0" processorArchitecture="X86" publicKeyToken="6595b64144ccf1df" language="*" />
    </dependentAssembly>
    </dependency>
    </assembly>

in your Python installation directory (where respective **.exe** files reside). Next time you run your wxPython applications, they\'ll look like \"normal\" XP applications.

This may also affect other Python modules that use Windows display API.

- Follow-up (a *very* late one): With Python 2.2.2 it caused all windowed applications ([TkInter](TkInter) too) to crash on window close on my machine. Applications are not required (just allowed) to support the new DLL\'s for the XP fancy look. If you run into this problem and deleting manifests doesn\'t help, try un- and reinstalling Python.

## Missing Readline Module 

I have problem when i first install Python 2.4. It seems that the distribution lack readline.py

- Python 2.4.2 (#1, Feb 16 2006, 20:42:14)
       [GCC 4.0.2 20050901 (prerelease) (SUSE Linux)] on linux2
       Type "help", "copyright", "credits" or "license" for more information.
       Traceback (most recent call last):
         File "/etc/pythonstart", line 7, in ?
           import readline
       ImportError: No module named readline
       >>>

It\'s possible that the readline module is a separate package in your SUSE Linux distribution.

-Do not type if you do not know. I compiled Python 2.4.4 from source ./configure \--enable-readline make make install and I get this error.

## How to Access Tomcat from Python 

Looking for examples of accessing Tomcat applications from Python.

I will be looking myself, and will post what I learn here, but so far Tomcat applications that require authentication are giving my python applications a 401 no matter what I try.

**The Following Does Not Work**

    import urllib2

    myUrl = 'http://localhost:8080/manager/html'
    username = 'root'
    password = 'r00t4me'

    req = urllib2.Request(myUrl)

    base64string = ('%s:%s' % (username, password)).encode('base64')[:-1]
    authheader =  "Basic %s" % base64string
    req.add_header("Authorization", authheader)

    try:
        f = urllib2.urlopen( myUrl )
    except urllib2.HTTPError, e:
        if e.code == 401:
            print 'not authorized'
        elif e.code == 404:
            print 'not found'
        elif e.code == 503:
            print 'service unavailable'
        else:
            print 'unknown error: '
    else:
        print 'success'
        for line in f:
            print line,

This yields a 401 \'not authorized\' when it should not, i.e. the username and password are correct. This is to connect to the page for the Tomcat manager application as a test, not to do any real work.

## Python Object ID 

You can get a unique ID number for any object:

:::: 
::: 
``` 
   1 >>> x="hello"
   2 >>> id( x )
   3 10855264
   4 >>> 
```
:::
::::

\...but how do you get from the object ID, back to the object itself?

What can I do to take 10855264, in this case, and see if I can get back \"hello\"?

Or is that not possible, without making a dictionary to hold it?

:::: 
::: 
``` 
   1 >>> x="hello"
   2 >>> d={}
   3 >>> d[id(x)]=x
   4 >>> d
   5 {10855264: 'hello'}
   6 >>>
```
:::
::::

------------------------------------------------------------------------

Contributors: [SteveHolden](SteveHolden), [FredrikLundh](FredrikLundh), [JohannesGijsbers](JohannesGijsbers), [SkipMontanaro](SkipMontanaro)

------------------------------------------------------------------------

[CategoryFaq](CategoryFaq)
