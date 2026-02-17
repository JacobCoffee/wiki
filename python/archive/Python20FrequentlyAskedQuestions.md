# Python20FrequentlyAskedQuestions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This is a copy of the historical Python 2.0 FAQ page. For a more recent version, see [PythonQuestions](PythonQuestions). \--[FredrikLundh](FredrikLundh)

# Python 2.0 FAQ 

Add your questions here and I\'ll do my best to answer them.

See also [CriticalPatches](./CriticalPatches.html) and [MiscPatches](./MiscPatches.html).

------------------------------------------------------------------------

## Win 95 Installation 

**Q** I run a Windows 95 200 mhz Compaq computer, when I tried to install Python 2.0, the installation program consistently crashes/freezes at 52% of the process. Can you give me any suggestions?

## C to Python API 

**Q** What are the differences between C to Python API from version 1.5.2 of Python

**A** One thing that changed (in a backwards compatible way!) is that Python sequence objects now have another slot, sq_contains. When the \"in\" operator is called and this slot is non-NULL, it is called instead of going through the object element by element and comparing.

------------------------------------------------------------------------

## Floating Point 

**Q.** Floating point is broken! For example:

    >>> 0.1+0.1
    0.20000000000000001
    >>>

This was correct in Python 1.5.2.

**A.** Binary floating point cannot represent decimal fractions exactly, so some rounding always occurs (even in Python 1.5.2). See [RepresentationError](RepresentationError).

What changed is that Python 2.0 shows more precision than before in certain circumstances (repr() and the interactive prompt).

You can use str() or print to get the old, rounded output:

    >>> print 0.1+0.1
    0.2
    >>> str (0.1+0.1)
    '0.2'

------------------------------------------------------------------------

## LONG_BIT Error 

**Q.** I get an error in pyport.h: `LONG_BIT definition appears wrong for platform (bad gcc config?).` When I remove the `#error` directive it builds fine.

**A.** You must be using Red Hat 7.0. It comes with a broken compiler. GCC 2.96 was never intended for distribution. You will need to update your glibc to version 2.2 (see [http://www.redhat.com/support/errata/RHBA-2000-079.html](http://www.redhat.com/support/errata/RHBA-2000-079.html) for more information).

I used the up2date command to install the new glibc.

------------------------------------------------------------------------

## pyexpat Module 

**Q.** I just downloaded version 2.0. When I try to run the test_sax.py module it complains that it can\'t find the driver pyexpat.py. I looked in the distribution and it doesn\'t seem to be there? I\'m running on Solaris 2.7. Thank You.

**A.** The pyexpat module is a compiled extension module. See the comments in the Modules/Setup file for instructions on getting and building the required C library. Once you\'ve built that, enable the module in the Modules/Setup file and type \"make\" in the top level of the Python source tree. \"make \--install\" will re-install Python for you, or you can copy Modules/pyexpat.so to \$exec_prefix/lib/python2.0/lib-dynload/ if you\'re building modules as shared objects.

**Q.** I tried to build pyexpat with Expat 1.2 or newer, but the test suite fails. What did I break?

**A.** Nothing. The pyexpat test shipped with Python 2.0 exposed details of some internal information from Expat that gets passed through the Python API. The format of that information changed between Expat 1.1 and Expat 1.2 (and could change again). The test has since been fixed to not expose that information. You should be able to use the pyexpat test in the CVS version of Python with Python 2.0 to make the test pass (without invalidating the test). The two files that need to be replaced are Lib/test/test_pyexpat.py and Lib/test/output/test_pyexpat.

------------------------------------------------------------------------

## Where\'s IDLE? 

**Q.** I just downloaded version 2.0 (BeOpen-Python-2.0-1.i386.rpm) and there is no trace of IDLE in there; an \"`rpm -qpl BeOpen-Python-2.0-1.i386.rpm | grep -i idle`\" comes up empty. [http://www.python.org/idle/](http://www.python.org/idle/) claims that IDLE 0.6 is distributed as part of Python 2.0. Checking further, I see that IDLE is included in [ftp://ftp.python.org/pub/python/src/python-2.0c1.tar.gz](ftp://ftp.python.org/pub/python/src/python-2.0c1.tar.gz) in the tools directory. Is this an oversight? Is there a way to install IDLE without unpacking the source tarball? ([bob@drzyzgula.org](mailto:bob@drzyzgula.org))

**A.** This is an oversight. None of the code in Tools is installed. I will fix this as soon as possible. ([jeremy@alum.mit.edu](mailto:jeremy@alum.mit.edu))

(Postscript: I don\'t think this was ever fixed.)

------------------------------------------------------------------------

## \"make test\" reports failures 

**Q.** I just downloaded and built version 2.0 under BSDI 4.0.1 with the \"\--with-threads=no\" option and the patch to Objects/Objects/fileobject.c for the TELL64 problem. Then I ran \"make test\" and got

    76 tests OK.
    3 tests failed: test_format test_largefile test_longexp

The question is, what do I do to resolve these failures or are they insignificant? ([gdinwiddie@min.net](mailto:gdinwiddie@min.net), Python newbie)

**A.** I think that you will find that Python generally works fine on your system. I\'m not familiar with BSDI but I have a suspicion that there\'s a problem with the support of 64-bit ints in C - not a huge loss typically unless you want to read and write files larger than 2 Gb. If you want to know more about what\'s going wrong, I suggest running the three failing tests manually; e.g. from the build directory you can do:

    ./python Lib/test/test_format.py

to see what went wrong with the test_format test.

Note that if you suspect a\'bug\' in Python (rather than a bug in your platform), the proper place to go to is the bug manager: [http://bugs.python.org/](http://bugs.python.org/) . ([guido@python.org](mailto:guido@python.org))

**Followup.** Thanks. FYI, I get these results

    ./python Lib/test/test_format.py | grep no
    '%#.117x' % (1,) =? '0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001' ... no
    u'%#.117x' % (1,) =? '0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001' ... no

    :./python Lib/test/test_largefile.py | grep no
    -1794967295L =?= 2500000001L ... no
    Traceback (most recent call last):
      File "Lib/test/test_largefile.py", line 61, in ?
        expect(os.fstat(f.fileno())[stat.ST_SIZE], size+1)
      File "Lib/test/test_largefile.py", line 45, in expect
        raise test_support.TestFailed, 'got %s, but expected %s' %\
    test_support.TestFailed: got -1794967295, but expected 2500000001

    ./python Lib/test/test_longexp.py | grep no
    Traceback (most recent call last):
      File "Lib/test/test_longexp.py", line 3, in ?
        l = eval("[" + "2," * REPS + "]")
    MemoryError

I hope this is of interest. ([gdinwiddie@min.net](mailto:gdinwiddie@min.net))

**A\*2.** There\'s definitely something broken. This warrants a bug report (if you haven\'t already submitted one to [SourceForge](SourceForge)). Useful data would be: what does \'%#.117x\' % (1,) yield? I\'m less interested in the largefile test outcome \-- it seems that the system doesn\'t actually support large files, even though it seems to support the interfaces. The longexp test looks like it might honestly run out of memory; how much memory does your system have? How much swap? See if this works if you change the file with a 10x smaller value of REPS.

------------------------------------------------------------------------

## Documentation in Windows Helpfile Format 

**Q.** Where do I get the documentation for Python 2.0 in the CHM (Compiled HTML) format?

**A.** Robin Dunn [announced](http://www.deja.com/=dnc/getdoc.xp?AN=683846117.1 "DejaNews") that he created a ZIP file with the BeOpen Python 2.0 docs, which you can download at \"[http://alldunn.com/python/py2docs.zip](http://alldunn.com/python/py2docs.zip)\". This also includes the tool (written in Python, of course) to generate the project files for the Microsoft Help Workshop.

**A.** See also \"[http://www.orgmf.com.ar/condor/pyshelf21.zip](http://www.orgmf.com.ar/condor/pyshelf21.zip)\" !

------------------------------------------------------------------------

## Where\'s the IDE for Python? 

**Q.** I just downloaded version 2.0. I\'m new to Python and would like to start in an integrated development environment. Can somebody please point to such a tool.

**A.** Commercial offerings: For Windows and Linux, there are several: PythonWorks ( [http://www.pythonworks.com](http://www.pythonworks.com) ); Wing IDE ( [http://www.wingide.com](http://www.wingide.com) ); BlackAdder ( [http://www.thekompany.com/products/blackadder/](http://www.thekompany.com/products/blackadder/) ).

In the free (what you get is not necessarily what you pay for) department: For Windows, there\'s also Pythonwin, which comes as part of ActivePython ([http://www.activestate.com](http://www.activestate.com)). For Mac OS (Classic and X), the standard [MacPython](MacPython) installation includes an IDE (\'Python IDE\'). For any platform with Tcl/Tk, there\'s also IDLE, which comes standard with Python ([http://www.python.org/idle/](http://www.python.org/idle/)).

In the future, expect more offerings, e.g. VisualPython (a Visual Studio plugin from ActiveState), Komodo (a Mozilla-based cross-platform offering from ActiveState), and Boa Constructor ([http://boa-constructor.sourceforge.net](http://boa-constructor.sourceforge.net)).

See also the FAQTS entry about this topic: [http://www.faqts.com/knowledge-base/view.phtml/aid/6433/fid/199/lang/en](http://www.faqts.com/knowledge-base/view.phtml/aid/6433/fid/199/lang/en)

Update: see [http://www-106.ibm.com/developerworks/linux/library/l-pide/](http://www-106.ibm.com/developerworks/linux/library/l-pide/) for a review of several IDEs mentioned above.

------------------------------------------------------------------------

## libreadline.so.3

**Q.** I just downloaded the version 2.0. rpm. I have an unsatisfied libreadline.so.3. What now?

**A.** The best solution in this case is to build from source. Go to the download page and download the source tarball. Unzip it, untar it, cd into the directory it creates, run ./configure, run make, run make install.

------------------------------------------------------------------------

## Windows 2K 

**Q.** I just tried installing version 2.0 on Win2K, it seemed to work ok, but none of the registry entries were made, but they did appear in the install file. Any suggestions?

**A.** Perhaps you don\'t have Administrator permissions?

------------------------------------------------------------------------

## RedHat 7.0 

**Q.** When I make Python 2.0 on [RedHat](RedHat) 7.0 (gcc-2.96-54, glibc-2.2-5), I get lots of compilation errors in Modules/bsddbmodule.c . What should I do?

**A.** You probably need to install a developer RPM (i.e. some lib & header files), in this case probably the \"GNU DB Module\".

**A.** There seems to be some sort of unfortunate interaction with RH7\'s db distribution. Even with the db1, db2 and db3 packages installed, the same compilation problems are seen. Adding \--without-libdb as a configure option avoids the compilation problem - at the expense of not having access to the Berkeley DB routines. Disappointingly, the gdbmmodule fails to compile, too.

**A.** I\'ve found that if you change the last #include \<db.h\> to #include \<db1/db.h\> in bsddbmodule.c that it will compile. Not sure about semantic issues afterwards yet.

------------------------------------------------------------------------

## Extensions using C++ compiled on Solaris with G++ 

**Q.** Linker errors when building extensions that use C++ on Solaris.

**A.** Martin von Loewis gave an explanation in python-dev: [http://mail.python.org/pipermail/python-dev/2001-March/013510.html](http://mail.python.org/pipermail/python-dev/2001-March/013510.html)

and more: [http://groups.google.com/groups?hl=en&lr=&ie=UTF-8&selm=avsmd9%24mcc%2401%241%40news.t-online.com](http://groups.google.com/groups?hl=en&lr=&ie=UTF-8&selm=avsmd9%24mcc%2401%241%40news.t-online.com)
