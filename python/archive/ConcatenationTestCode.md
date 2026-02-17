# ConcatenationTestCode

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Counter to the [PythonSpeed/PerformanceTips](./PythonSpeed(2f)PerformanceTips.html), on python 2.4 the following string concatenation is almost twice as fast:

:::: 
::: 
``` 
   1 from time import time
   2 t = time()
   3 
   4 s = 'lksdajflakjdsflku09uweoir'
   5 for x in range(40):
   6     s += s[len(s)/2:]
   7 
   8 print 'duration:', time()-t
```
:::
::::

as:

:::: 
::: 
``` 
   1 from time import time
   2 t = time()
   3 
   4 s = 'lksdajflakjdsflku09uweoir'
   5 for x in range(40):
   6     s = "".join((s, s[len(s)/2:]))
   7 
   8 print 'duration:', time()-t
```
:::
::::

------------------------------------------------------------------------

On the win32 Python 2.4 I\'m seeing the join sample above complete in less than half the time of the concatenating sample.

- -db

Usually the join() is located *outside* the loop, that code makes this extremely hard though (becuase of the self-referencing of the generated string). But that situation is not the norm. \-- [JürgenHermann](./J(c3bc)rgenHermann.html) 2005-08-01 06:07:51

Are you guys kidding? The whole page is contrieved. Correct implementation of \"join\" is:

    from time import time
    t = time()

    s = 'lksdajflakjdsflku09uweoir'
    r = [s]
    for x in range(40):
        r.append(s[len(s)/2:])
    s = "".join(r)

    print 'duration:', time()-t

which gives on [PythonWin](PythonWin) 2.4 (#60, Nov 30 2004, 09:34:21) \[MSC v.1310 32 bit (Intel)\] on win32 execution times:

    1st  duration: 54.4060001373
    Last duration: 0.0160000324249

\-- \-- [MikeRovner](MikeRovner) 2005-08-02 10:19:06

- Mike, that code generates a very different (and much shorter) s. Note how the original code takes the half of the *preconcatenated* s, making the size grow exponentially (which generates megabytes of data). \-- [JürgenHermann](./J(c3bc)rgenHermann.html) 2005-08-30 18:44:05

\-- \-- [DavidFord](./DavidFord.html) 2005-10-18 10:19:06 A few notes (your mileage may vary - this is a 4Mb file being stripped of unprintable characters)

- Regex replacement rather than creating a list and joining it is 2.5x faster than the tooling above

- This is far slower than the equivalent Java code (around 4x slower) using String.charAt() and [StringBuffers](./StringBuffers.html)

------------------------------------------------------------------------

I tend to create a stream of strings in a loop that should be concatenated. I generated the script to test the join vs += performance for some randomly generated data and found that for 100,000 strings of length up to ten characters, join is maybe 20% faster than using +=. It certainly was not an order of magnitude faster. The results tended to vary each time through the outer loop, even though I attempted to control the garbage collection and ensured my Windows XP machine was 95% idle apart from running the script.

:::: 
::: 
``` 
   1 from time import time
   2 import random, gc
   3 
   4 '''
   5 Check speed of string concatenation vs joining in different versions of Python
   6 
   7 
   8 
   9 Python 2.6.1 (r261:67517, Dec  4 2008, 16:51:00) [MSC v.1500 32 bit (Intel)] on win32
  10 Type "copyright", "credits" or "license()" for more information.
  11 
  12     ****************************************************************
  13     Personal firewall software may warn about the connection IDLE
  14     makes to its subprocess using this computer's internal loopback
  15     interface.  This connection is not visible on any external
  16     interface and no data is sent to or received from the Internet.
  17     ****************************************************************
  18 
  19 IDLE 2.6.1
  20 >>> ================================ RESTART ================================
  21 >>>
  22  jointime =      0.063  concattime =  0.0780001  join/concat =  80.77%
  23  jointime =      0.062  concattime =  0.0780001  join/concat =  79.49%
  24  jointime =      0.063  concattime =  0.0780001  join/concat =  80.77%
  25  jointime =      0.062  concattime =  0.0780001  join/concat =  79.49%
  26  jointime =      0.062  concattime =  0.0780001  join/concat =  79.49%
  27  jointime =      0.063  concattime =  0.0780001  join/concat =  80.77%
  28  jointime =      0.062  concattime =  0.0779998  join/concat =  79.49%
  29  jointime =      0.062  concattime =  0.0780001  join/concat =  79.49%
  30  jointime =      0.062  concattime =  0.0940001  join/concat =  65.96%
  31  jointime =  0.0469999  concattime =  0.0780001  join/concat =  60.26%
  32 
  33 
  34 
  35 Python 2.5.3 (r253:67855, Dec 19 2008, 16:58:30) [MSC v.1310 32 bit (Intel)] on win32
  36 Type "copyright", "credits" or "license()" for more information.
  37 
  38     ****************************************************************
  39     Personal firewall software may warn about the connection IDLE
  40     makes to its subprocess using this computer's internal loopback
  41     interface.  This connection is not visible on any external
  42     interface and no data is sent to or received from the Internet.
  43     ****************************************************************
  44 
  45 IDLE 1.2.3
  46 >>> ================================ RESTART ================================
  47 >>>
  48  jointime =  0.0779998  concattime =      0.063  join/concat = 123.81%
  49  jointime =  0.0780001  concattime =  0.0780001  join/concat = 100.00%
  50  jointime =      0.109  concattime =  0.0939999  join/concat = 115.96%
  51  jointime =  0.0780001  concattime =      0.062  join/concat = 125.81%
  52  jointime =      0.063  concattime =  0.0780001  join/concat =  80.77%
  53  jointime =  0.0780001  concattime =  0.0779998  join/concat = 100.00%
  54  jointime =      0.063  concattime =  0.0780001  join/concat =  80.77%
  55  jointime =      0.062  concattime =      0.172  join/concat =  36.05%
  56  jointime =      0.079  concattime =  0.0779998  join/concat = 101.28%
  57  jointime =      0.063  concattime =  0.0780001  join/concat =  80.77%
  58 >>>
  59 
  60 
  61 PythonWin 2.4.3 - Enthought Edition 1.0.0 (#69, Aug  2 2006, 12:09:59) [MSC v.1310 32 bit (Intel)] on win32.
  62 Portions Copyright 1994-2004 Mark Hammond (mhammond@skippinet.com.au) - see 'Help/About PythonWin' for further copyright information.
  63 >>>  jointime =      0.062  concattime =  0.0940001  join/concat =  65.96%
  64  jointime =  0.0929999  concattime =  0.0780001  join/concat = 119.23%
  65  jointime =      0.063  concattime =  0.0780001  join/concat =  80.77%
  66  jointime =      0.062  concattime =  0.0780001  join/concat =  79.49%
  67  jointime =      0.062  concattime =      0.062  join/concat = 100.00%
  68  jointime =      0.063  concattime =  0.0780001  join/concat =  80.77%
  69  jointime =  0.0780001  concattime =  0.0780001  join/concat = 100.00%
  70  jointime =  0.0940001  concattime =  0.0940001  join/concat = 100.00%
  71  jointime =      0.063  concattime =  0.0780001  join/concat =  80.77%
  72  jointime =  0.0780001  concattime =  0.0780001  join/concat = 100.00%
  73 
  74 
  75 '''
  76 
  77 def stringstotest(n=100000, rmin=0, rmax=10):
  78     ' Returns a list of random strings of between rmin to rmax characters in length'
  79     allchars = 'qwertyuiopasdfghjklzxcvbnm'
  80     allchars += allchars.upper()
  81 
  82     return [ "".join( random.choice(allchars)
  83                       for i in xrange(random.randint(rmin, rmax)) )
  84              for j in xrange(n) ]
  85 
  86 strings = stringstotest()
  87 
  88 for i in xrange(10):
  89     gc.collect()
  90     gc.disable()
  91     # JOIN
  92     t0 = time()
  93     l = []  # list to "".join()
  94     for string in strings:
  95         l.append(string)
  96     joined = "".join(l)
  97     jointime = time() - t0
  98 
  99     gc.enable()
 100     del l, joined
 101     gc.collect()
 102     gc.disable()
 103 
 104     # CONCATENATION
 105     t0 = time()
 106     s = ''  # string to +=, concatenate
 107     for string in strings:
 108         s += string
 109     concattime = time() - t0
 110 
 111     del s
 112 
 113     print " jointime = %10g  concattime = %10g  join/concat = %6.2f%%" % (
 114         jointime, concattime, jointime/float(concattime)*100 )
 115 
 116 gc.enable()
```
:::
::::

\-- Paddy3118 2009-01-01 09:48:00

Thanks for this. I\'ve run a modified version of above examples on Windows for Python 2.7.1 and Python 3.2. And strangely **Python 3.2 is 2x slower**.

    Z:\Code\Python>"c:\Program Files\Python3.2\python.exe" string_concatenation.py
    Loops 100
    concatenate1 duration: 0.0s
    Size: 173285
    concatenate2 duration: 0.015000104904174805s
    Size: 173285
    concatenate3 duration: 0.0s
    Size: 173285

    Loops 1000
    concatenate1 duration: 10.375s
    Size: 17482535
    concatenate2 duration: 10.17199993133545s
    Size: 17482535
    concatenate3 duration: 0.06200003623962402s
    Size: 17482535

    Z:\Code\Python>"c:\Program Files\Python2.7.1\python.exe" string_concatenation.py
    Loops 100
    concatenate1 duration: 0.0160000324249s
    Size: 173285
    concatenate2 duration: 0.0s
    Size: 173285
    concatenate3 duration: 0.0s
    Size: 173285

    Loops 1000
    concatenate1 duration: 5.17199993134s
    Size: 17482535
    concatenate2 duration: 5.07800006866s
    Size: 17482535
    concatenate3 duration: 0.0320000648499s
    Size: 17482535

:::: 
::: 
``` 
   1 from time import time
   2 s = 'qwertyuiopasdfghjklzxcvbnm123456789'
   3 LOOPS = 10
   4 
   5 def timeit(f, *args):
   6     def new_f(*args):
   7         t = time()
   8         result = f(*args)
   9         print('{0} duration: {1}s'.format(f.__name__,time()-t))
  10         print('Size: {result}'.format(result=result))
  11     return new_f
  12 
  13 @timeit
  14 def concatenate1(s, loops):
  15     """slow and memory consuming"""
  16     r = s
  17     for x in range(loops):
  18         r += x*s
  19     return len(r)
  20 
  21 @timeit
  22 def concatenate2(s, loops):
  23     """faster using join in loop"""
  24     r = s
  25     for x in range(loops):
  26         r = "".join((r, x*s))
  27     return len(r)
  28 
  29 @timeit
  30 def concatenate3(s, loops):
  31     """much faster using list"""
  32     r = [s]
  33     for x in range(loops):
  34         r.append(x*s)
  35     r = "".join(r)
  36     return len(r)
  37 
  38 if __name__ == '__main__':
  39     for loops in (100, 1000):
  40         print("\nLoops {}".format(loops))
  41         concatenate1(s, loops)
  42         concatenate2(s, loops)
  43         concatenate3(s, loops)
```
:::
::::

\-- llakomy 2011-03-10 12:03:00

Not surprising at all. Every character in the original string and all generated strings is 2-4x the size in Python 3 compared to Python 2 (depending on whether you compiled Python 3 for UTF-16 or UTF-32). Most of the work is copying characters around, so your results would be expected. You might try running the same test with your \'s\' variable and the \"\" used with join defined as bytes literals (b\'qwertyuiopasdfghjklzxcvbnm123456789\' and b\"\".join(\...) respectively).

\-- Josh 2011-04-20 16:07:00

As Josh hints at above, the format of the string matters a lot for this. With byte-code strings, concatenating with += is as fast as a .join outside of the for loop, and several times faster than a .join inside the for loop. With Unicode, the concatenation is roughly 300x slower than a .join outside the for loop (with Unicode, the for inside the loop is faster than concatenation, but not by much). Used llakomy\'s code to test on 2.7.3.

\-- Different Josh
