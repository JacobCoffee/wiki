# PyFileBenchmarks

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Some [PyFile](./PyFile.html) benchmarks, mostly to show off the [PyFile](./PyFile.html) nio

Tests done on OS X 10.4.10 Java 1.5.0_07 in server mode

Preparations: 10

Test iterations (average taken of): 5

Notes:

\* This page is made for a larger browser window so that the small and big graphs lie on the same row

\* jython\'s file iter is roughly the same code as its readline, whereas CPython\'s readline is not as optimized as its iter. So the fact that our readline speed is very close to CPython\'s isn\'t totally fair, CPython\'s iter still beats us

\* The few anomalies in the smaller benchmarks are due to JIT kicking in. Ideally we would run more preparations and iterations

\* i don\'t have text mode benchmarks because they\'re only applicable to windows. their read times would be a little faster than \'U\' mode. write times would be slower than \'rb\' but still faster than old [PyFile](./PyFile.html)

\* The write times show both writing to a ram disk and writing to a hard disk. Writing to a hard disk shows how much slower Jython\'s old [PyFile](./PyFile.html) really is in a normal workload, compared to CPython and [PyFile](./PyFile.html) nio, whose write times are limited to the speed of the hard disk. Writing to a ram disk shows how potentially fast CPython and [PyFile](./PyFile.html) nio can write

Reading:

:::: 
::: 
``` 
   1     def test_read(self, fp):
   2         fp.read()
```
:::
::::

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_read.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_read.jpg") ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_read.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_read.jpg")

:::: 
::: 
``` 
   1     def test_iter(self, fp):
   2         for line in fp:
   3             pass
```
:::
::::

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_iter.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_iter.jpg") ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_iter.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_iter.jpg")

:::: 
::: 
``` 
   1     def test_readline(self, fp):
   2         while fp.readline():
   3             pass
```
:::
::::

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_readline.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_readline.jpg") ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_readline.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_readline.jpg")

:::: 
::: 
``` 
   1     def test_readline_with_tell(self, fp):
   2         while fp.readline():
   3             fp.tell()
```
:::
::::

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_readline_with_tell.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_readline_with_tell.jpg") ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_readline_with_tell.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_readline_with_tell.jpg")

:::: 
::: 
``` 
   1     def test_readlines(self, fp):
   2         fp.readlines()
```
:::
::::

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_readlines.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_readlines.jpg") ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_readlines.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_readlines.jpg")

Writing:

:::: 
::: 
``` 
   1 MSG = ('abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz123456789'
   2        '0abcdefgh\r\n')
```
:::
::::

:::: 
::: 
``` 
   1     def test_write(self, fp, lines):
   2         write = fp.write
   3         for i in range(lines):
   4             write(MSG)
```
:::
::::

To a ramdisk:

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_write.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_write.jpg") ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_write.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_write.jpg")

To disk:

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/small/test_write.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/small/test_write.jpg") ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/big/test_write.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/big/test_write.jpg")

:::: 
::: 
``` 
   1     def test_writelines(self, fp, lines):
   2         lines = [MSG for i in range(lines)]
   3         fp.writelines(lines)
```
:::
::::

To a ramdisk:

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_writelines.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/small/test_writelines.jpg") ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_writelines.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-ramdisk/big/test_writelines.jpg")

To disk:

![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/small/test_writelines.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/small/test_writelines.jpg") ![](http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/big/test_writelines.jpg "http://underboss.org/~pjenvey/jython/pyfile-nio/osx-disk/big/test_writelines.jpg")
