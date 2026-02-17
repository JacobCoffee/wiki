# JustAnotherPythoneer

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Discussion 

Perl coders are proud that Perl\'s motto is \"There\'s more than one way to do it.\"\
In comparison, Python is sometimes stereotyped as \"There\'s only one way to do it\", but this is of course not true. The Zen of Python, accessed via

    import this

includes the maxims:\
*Beautiful is better than ugly.*\
*Explicit is better than implicit.*\
*Simple is better than complex.*\
*Complex is better than complicated.*\
*Flat is better than nested.*\
*Sparse is better than dense.*\
*Readability counts.*\
*If the implementation is hard to explain, it\'s a bad idea.*\
*There should be one\-- and preferably only one \--obvious way to do it.*\

The net effect is that there is a limited set of good solutions for a given problem, and users are strongly encouraged to use them.

While Python attempts to discourage bad practices, and its indentation-based block structure and limited anonymous blocks (lambdas) make certain techniques difficult, it is possible to produce many more bad solutions than good for a given problem.

Please Feel Free to add/reorder/reallocate examples.

## The Problem 

Your signature block (up to four lines of 78 characters each) needs code that prints \"Just another Pythoneer\".

## The Limited Set of Good Solutions 

:::: 
::: 
``` 
   1 print "Just another Pythoneer"
```
:::
::::

(Though someone may point out that as a Python user following correct Pythonic practice, you are more correctly a *Pythonista*\... and give you a brief 6000 word essay on the historical debate over the naming of Python Users and the etymology of the root *Python* and the stem *-ista*\... and advise you against using the combination in an impromptu Spanish examination)

## The Larger Set of Not-So-Good Solutions 

### Normal Printing/Concatination 

:::: 
::: 
``` 
   1 print "Just", "another", "Pythoneer"
```
:::
::::

:::: 
::: 
``` 
   1 print "Just "\
   2       "another "\
   3       "Pythoneer"
```
:::
::::

:::: 
::: 
``` 
   1 j = "Just "
   2 a = "another "
   3 p = "Pythoneer"
   4 print j+a+p
```
:::
::::

:::: 
::: 
``` 
   1 import sys; sys.stdout.write("Just another Pythoneer\n")
```
:::
::::

### Substitution 

:::: 
::: 
``` 
   1 print '''%s %s %s''' % ("Just", "another", "Pythoneer")
```
:::
::::

:::: 
::: 
``` 
   1 print '%(j)s %(a)s %(py)s' % { "j": "Just", "a": "another", \
   2   "pl": "Perl Hacker", "py": "Pythoneer", "c": "C Coder", \
   3   "f": "Fortran Freak", "turtle" : "Logo Lover" }
```
:::
::::

:::: 
::: 
``` 
   1 class JAPy(int):
   2     def __str__(self):
   3         return "%s"*5%("Just",chr(self),"another", chr(self), "Pythoneer")
   4 print JAPy(32)
```
:::
::::

:::: 
::: 
``` 
   1 class JAPy(int): pass
   2 def s(s): s+=1; return "Just" + chr(s) + "another" + chr(s) + "Pythoneer"
   3 n, JAPy.__str__ = JAPy(31), s
   4 print n
```
:::
::::

:::: 
::: 
``` 
   1 print "Just another Perl Hacker".replace("Perl Hacker", "Pythoneer")
```
:::
::::

### Reversal 

:::: 
::: 
``` 
   1 x = ['r','e','e','n','o','h','t','y','P',' ','r','e','h','t','o','n','a',' ',
   2      't','s','u','J']
   3 x.reverse()
   4 print "".join(x)
```
:::
::::

:::: 
::: 
``` 
   1 print "".join(['r','e','e','n','o','h','t','y','P',' ','r','e','h','t','o','n',
   2                'a',' ','t','s','u','J'][::-1])
```
:::
::::

:::: 
::: 
``` 
   1 print "reenohtyP rehtona tsuJ"[::-1]
```
:::
::::

:::: 
::: 
``` 
   1 print "".join([x for x in list('reenohtyP rehtona tsuJ')[::-1]])
```
:::
::::

:::: 
::: 
``` 
   1 print "".join([x for x in list('reenohtyP rehtona tsuJ')][::-1])
```
:::
::::

### Iteration 

:::: 
::: 
``` 
   1 import sys
   2 for c in "Just another Pythoneer\n":
   3     sys.stdout.write(c)
```
:::
::::

:::: 
::: 
``` 
   1 import sys; [sys.stdout.write(c) for c in "Just another Pythoneer\n"]
```
:::
::::

:::: 
::: 
``` 
   1 x = ["Just", "another", "Pythoneer"]
   2 while x: print x[0], ; x = x[1:]
   3 print
```
:::
::::

:::: 
::: 
``` 
   1 x = ["Pythoneer", "another", "Just",]
   2 while x: print x[-1], ; x.pop()
   3 print
```
:::
::::

:::: 
::: 
``` 
   1 import random, sys; x = "Just another Pythoneer\n"
   2 while x:
   3   y = random.choice(x);
   4   if y == x[0]: sys.stdout.write(y); x = x[1:]
```
:::
::::

### Slicing and Indexing 

:::: 
::: 
``` 
   1 print "Just another Pythoneer and not a Perl Hacker".split(" and")[0]
```
:::
::::

:::: 
::: 
``` 
   1 print "I'm just another Pythoneer".split(" ",1)[1].capitalize()
```
:::
::::

:::: 
::: 
``` 
   1 import re
   2 a = ["Pythoneer", "extra", "Just", "words", "another", "Hello!"]
   3 m = re.match("(?P<three>\d+).(?P<one>\d+).(?P<two>\d+)", "1A5l2")
   4 print a[m.start("one")], a[m.start("two")], a[m.start("three")]
```
:::
::::

:::: 
::: 
``` 
   1 #Sometimes_code_does_not_really_need_to_have_syntacally_significant_whitespace
   2 g,u,n=range(3),"Why don't I use Java or Perl?",lambda(x),y:reduce(x.__add__,y)
   3 print"".join([u[P:H+P]for(H,P)in(zip(n(list,n(tuple,[([d],n(list,[[1+c%2]*(c+1
   4 )for(c)in(g)]))for(d)in(g)])[1:]),[16,12,8,19,6,5,8,1,25,23,2,8,1,5,14,25]))])
```
:::
::::

:::: 
::: 
``` 
   1 import platform as p; d=[list(x)for x in open(p.__file__[:-1])]; a=d[28]+d[12]
   2 for f,t in zip([0,5,7,8,10,12,19,20,21,22],[15,6,9,14,19,41,25,24,23,99]):
   3     del a[f:t]; a[8]=a[8].lower()
   4 print "".join(a)
```
:::
::::

### Recursion 

:::: 
::: 
``` 
   1 japy = lambda x: isinstance(x,dict) and x.keys()[0] + japy(x.values()[0]) or x
   2 print japy({"Just ": {"another ": "Pythoneer"}})
```
:::
::::

:::: 
::: 
``` 
   1 def k(x):
   2     if type(x) == type({}): return x.keys()[0] + k(x.values()[0])
   3     return x
   4 print k({"Just ": {"another ": "Pythoneer"}})
```
:::
::::

### Decoding 

:::: 
::: 
``` 
   1 import uu, StringIO
   2 s = StringIO.StringIO(); uu.decode(StringIO.StringIO('begin 666 '+\
   3   '-\01262G5S="!A;F]T:&5R(%!Y=&AO;F5E<@  \012 \012end\012'), s)
   4 print s.getvalue()
```
:::
::::

:::: 
::: 
``` 
   1 d,o=0x3B55094199ACFB742DB37F3F97B11175C0C8EL,[]
   2 while d:
   3     d,m=divmod(d,100);o.append(chr(m+32))
   4 print "".join(o)
```
:::
::::

:::: 
::: 
``` 
   1 def japy(d=0x3B55094199ACFB742DB37F3F97B11175C0C8EL):
   2     while d:
   3         d,m=divmod(d,100);yield m+32
   4 print "".join([chr(x) for x in japy()])
```
:::
::::

:::: 
::: 
``` 
   1 import pickle; print pickle.loads("S'Just another Pythoneer'\012p0\012.")
```
:::
::::

:::: 
::: 
``` 
   1 print u"Whfg nabgure Clgubarre".encode('rot13')
```
:::
::::

:::: 
::: 
``` 
   1 d,n=dict(zip("0123456789ABx"," aehnosturyPJ")), 10157833755785421529629225
   2 print "".join([d[c] for c in str(hex(n))[:-1]]).strip()
```
:::
::::

### Exception Handling 

:::: 
::: 
``` 
   1 try:
   2   vars()["Just another Pythoneer"]
   3 except KeyError, e:
   4   print eval(str(e))
```
:::
::::

:::: 
::: 
``` 
   1 try:
   2   raise "Just another Pythoneer"
   3 except:
   4   print sys.exc_info()[0]
```
:::
::::

:::: 
::: 
``` 
   1 try: __import__("Just another Pythoneer")
   2 except ImportError, m: print str(m)[-22:]
```
:::
::::

### Introspection 

:::: 
::: 
``` 
   1 """Just another Pythoneer"""
   2 print __doc__
```
:::
::::

:::: 
::: 
``` 
   1 class Print:
   2     def __call__(self): print
   3     def __getattr__(self, name): print name, ; return self
   4 Print().Just.another.Pythoneer()
```
:::
::::

:::: 
::: 
``` 
   1 class JAPy: pass
   2 def i(self,x="Just another Pythoneer"): pass
   3 def s(self): return self.__init__.func_defaults[0]
   4 print JAPy.__dict__.update({"__init__":i,"__str__":s}) or JAPy()
```
:::
::::

:::: 
::: 
``` 
   1 class func_defaults:
   2     func_defaults = "Just another Pythoneer";func_defaults=lambda \
   3     func_defaults = func_defaults:func_defaults.func_defaults.func_defaults[0]
   4 print func_defaults.func_defaults(func_defaults())
```
:::
::::

    class func_defaults:
        func_defaults = "Just another Pythoneer"
        def func_defaults(func_defaults=func_defaults):pass
    func_defaults,=func_defaults().func_defaults.func_defaults;print func_defaults

:::: 
::: 
``` 
   1 class Just_another_Pythoneer(object):
   2     def __init__(self):
   3         print " ".join(self.__class__.__name__.split("_"))
   4 Just_another_Pythoneer()
```
:::
::::

:::: 
::: 
``` 
   1 def Just_another_Pythoneer(fn):
   2     print fn.func_name.replace("_"," ")
   3 Just_another_Pythoneer(Just_another_Pythoneer)
```
:::
::::

:::: 
::: 
``` 
   1 def _(Just, another, Pythoneer):_
   2 print " ".join(_.func_code.co_varnames)
```
:::
::::

:::: 
::: 
``` 
   1 def f(z):
   2   '''Just another Pythoneer (and remember to document your code!)'''
   3   pass
   4 print f.__doc__[:22]
```
:::
::::

### Runtime Code 

:::: 
::: 
``` 
   1 exec "print 'Just another Pythoneer'"
```
:::
::::

:::: 
::: 
``` 
   1 x = compile("print 'Just another Pythoneer'\n", "japy", "single")
   2 eval(x)
```
:::
::::

## Credits 

[AndrewDalke](./AndrewDalke.html)\
[HansNowak](./HansNowak.html)\
\"Snippet 181\"\
[TaroOgawa](./TaroOgawa.html)\
[KazuoMoriwaka](./KazuoMoriwaka.html)\
\"just another Pythoneer\"
