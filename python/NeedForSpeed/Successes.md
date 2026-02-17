# NeedForSpeed/Successes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Things we think the Python community will like.

- Frame optimizations: once a function is called it retains the allocated frame for use in future calls, avoiding allocation and initialization overhead. Frame size has also been slightly reduced ([RichardJones](RichardJones)).

  This gave a 10% [PyStone](./PyStone.html) improvement on [RichardJones](RichardJones)\' test machine, compared to Python 2.4 (from 20242 to 22935).

- Applied Py_LOCAL and PY_LOCAL_AGGRESSIVE compiler tuning from SRE to ceval.c (currently for Windows only). This results in a 3-10% [PyStone](./PyStone.html) speedup on our Intel boxes ([FredrikLundh](FredrikLundh)).

- Made Gzip readline 30-40% faster ([BobIppolito](BobIppolito))

- Speed up string and Unicode operations ([AndrewDalke](./AndrewDalke.html), [FredrikLundh](FredrikLundh)). Most notably, repeat is much faster, and most search operations (find, index, count, in) are a LOT faster (25x for the related stringbench tests). Parts of the code has also been moved into a \"stringlib\" directory, which contain code that\'s used by both string types, and lots of new tests has been added to the test suite. Here are the current \"stringbench\" results:

<!-- -->

            str(ms) uni(ms) %       comment
            -----------------------------------------------------
            1699.32 2321.11 73.2    TOTAL 2.4.3
            1208.67 2322.07 52.1    TOTAL 2.5a2
             303.15  384.46  78.9    TOTAL trunk (revision 46448)

- Patch 1335972 was a combination bugfix+speedup for string-\>int conversion. These are the speedups measured on my Windows box for decimal strings of various lengths. Note that the difference between 9 and 10 is the difference between short and long Python ints on a 32-bit box. ([TimPeters](TimPeters)) The patch doesn\'t actually do anything to speed conversion to long directly; the speedup in those cases is solely due to detecting \"unsigned long\" overflow more quickly:

<!-- -->

            length speedup
            ------ -------
             1       12.4%
             2       15.7%
             3       20.6%
             4       28.1%
             5       33.2%
             6       37.5%
             7       41.9%
             8       46.3%
             9       51.2%
            10       19.5%
            11       19.9%
            12       23.9%
            13       23.7%
            14       23.3%
            15       24.9%
            16       25.3%
            17       28.3%
            18       27.9%
            19       35.7%

- The struct module has been rewritten to pre-compile struct descriptors (similar to the RE module). This gives a 20% speedup, on average, for the test suite ([BobIppolito](BobIppolito)). Taking advantage of new ability to \"compile\" a struct pattern (similar to compiling regexps) can be much faster still.

- A pack_to() method has been added to the struct module to support packing directly into a writable buffer. Also, recv_buf() and recvfrom_buf() methods were added to the socket module to read directly into a writable buffer ([MartinBlais](MartinBlais)). Right now, the only way to create a writable buffer from Python is via the array module, but I\'m adding a new class that supports this (see below).

- Worked on using profile guided optimizations in Visual Studio 8 ([KristjanJonsson](./KristjanJonsson.html), RichardMTew). This appears to give on the order of 15% speed improvement in the pybench test suite. A new PCBuild8 directory will be added with automated mechanisms for doing this.

- Patch 1442927 aimed at speeding `long(str, base)`{.backtick} operations. It required major fiddling for portability, endcase correctness, and avoiding significant slowdowns on shorter input strings. Now it\'s up to 6x faster, although it takes a lot of digits to get that, and it\'s still slower for 1-digit inputs. ([TimPeters](TimPeters))

Speedups at various lengths for decimal inputs, comparing 2.4.3 with current trunk:

      len  speedup
     ----  -------
       1     -4.5%
       2      4.6%
       3      8.3%
       4     12.7%
       5     16.9%
       6     28.6%
       7     35.5%
       8     44.3%
       9     46.6%
      10     55.3%
      11     65.7%
      12     77.7%
      13     73.4%
      14     75.3%
      15     85.2%
      16    103.0%
      17     95.1%
      18    112.8%
      19    117.9%
      20    128.3%
      30    174.5%
      40    209.3%
      50    236.3%
      60    254.3%
      70    262.9%
      80    295.8%
      90    297.3%
     100    324.5%
     200    374.6%
     300    403.1%
     400    391.1%
     500    388.7%
     600    440.6%
     700    468.7%
     800    498.0%
     900    507.2%
    1000    501.2%
    2000    450.2%
    3000    463.2%
    4000    452.5%
    5000    440.6%
    6000    439.6%
    7000    424.8%
    8000    418.1%
    9000    417.7%

- Replaced some Python C-API calls by newer, speedier versions. Most notably, using [PyObject](./PyObject.html)\_[CallFunctionObjArgs](./CallFunctionObjArgs.html) instead of [PyObject](./PyObject.html)\_[CallFunction](./CallFunction.html) when all arguments are [PyObject](./PyObject.html) pointers (the O format code) can shave some 30% off the actual function call ([GeorgBrandl](./GeorgBrandl.html)).

- Reworked, debugged and applied a patch to speed up interpreter startup by reducing the number of open() calls ([GeorgBrandl](./GeorgBrandl.html)).

  - Even for repeated invocation of the interpreter where all files remain in the cache, you get the following figures:

<!-- -->

       Time for 1000 interpreter startups
       Python 2.4 trunk  16.470 secs
       Python 2.5.2a2    17.328 secs
       Python 2.5 trunk  15.873 secs

- Made all built-in exceptions real C new-style types. In 2.5 alpha, they were just objects faking to be classes, which slowed them down by 20% compared to 2.4. After this change, exception handling is around 30% faster than in 2.4 ([RichardJones](RichardJones), [GeorgBrandl](./GeorgBrandl.html)).

- Added support for min(), max(), sum(), and pow() to Psyco. This produces significant speedups when used in combination with virtualized objects. ([JohnBenediktsson](./JohnBenediktsson.html))

<!-- -->

        Operation             CPython 2.4.3    Psyco 1.5.1   Psyco-NFS
        ------------------    -------------    -----------   -----------
        sum(range(100))       9.856            8.709         0.016
        min(1, max(2, 3))     1.131            0.504         0.017
        pow(3, 2, 2)          0.602            0.140         0.016

- Added support for int(), float(), and round() to Psyco. These become quite efficient within a set of other psyco operations. ([JohnBenediktsson](./JohnBenediktsson.html))

<!-- -->

        Operation             CPython 2.4.3    Psyco 1.5.1   Psyco-NFS
        ------------------    -------------    -----------   -----------
        int(round(5.375))     0.975            0.461         0.015

- ![/!\\](/wiki/europython/img/alert.png "/!\") NB. These operations now all take 0.016 seconds because they are constant-folded! You need examples with non-constant arguments in the branchmarks. Also, you need to compile Psyco in debugging mode for testing - some of these examples generate fatal assertion errors in the Psyco-NFS branch. ([ArminRigo](./ArminRigo.html))

<!-- -->

- [GeorgBrandl](./GeorgBrandl.html) and [JackDiederich](./JackDiederich.html) worked on a rewrite of the Decimal module in C. This will kick-start a Google [SummerOfCode](SummerOfCode) project, which will therefore achieve more than originally planned.

- regexp searching speedup by 1%-2% on linux just by using [PyObject](./PyObject.html)\_(MALLOC\|FREE) for small allocations instead of system malloc. Unfinished is a free lists implementation for the small frequently allocated objects. \_sre.c uses very few objects at the same time - even caching a single SRE_REPEAT object gives a speedup of almost 1%! I \[[JackDiederich](./JackDiederich.html)\] will try and finish the patch before 2.5beta.

- \[unfinished\] \_sre.c matching can be sped up by 3-5% by using free lists for the small frequently allocated objects. It uses very few at the same time - even caching a single SRE_REPEAT object gives a speedup of almost 1%. I \[[JackDiederich](./JackDiederich.html)\] will try and finish the patch before 2.5beta.

- \[unfinished\] Implemented a new "hot buffer" class, which consists in a moving string that sits on top of a fixed allocated memory buffer. The buffer has a window which defines the visible portion (you can change this window during parsing). Given a hot buffer, you should be able to read data into it from the network or from a file without having to create temporary strings, and to extract bytes and other basic types from it similarly. (Martin Blais). We still need to implement direct I/O from/to a file (we have network only now) and to implement the common use patterns described in the test in C, e.g. for parsing netstrings, parsing line-delimited input. See the README.txt file in the module for more stuff to do. (I will complete this later).
