# Asking for Help/How can I convert a hex representation to an integer?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Converting a Hex representation to an Integer 

I\'m running into some trouble when trying to convert a series of hex representations into an integer\... I\'m sure there is a builtin to do this (wouldn\'t make sense not to have one) but I can\'t find it for the life of me.

This is a dump of my interpreter session:

:::: 
::: 
``` 
   1 >>> file=open("C:/test.m4a")
   2 >>> contents=file.read()
   3 >>> contents.find('user')
   4 592
   5 >>> contents[592:600]
   6 'user\x00\xcc\x15\xa4'
```
:::
::::

and I need to convert the values following user (\'\\x00\\xcc\\x15\\xa4\') into an integer value\... what am I doing wrong here?

\[\'anon\'\]: try

:::: 
::: 
``` 
   1 >>> 0x00cc15a4
   2 13374884
```
:::
::::

[lwickjr](lwickjr): you use

:::: 
::: 
``` 
   1 >>> print int('0a', 16)
   2 10
   3 >>>
```
:::
::::

\...but these aren\`t hex values. Try ord() on each character, and see if that gives you the results you need.

[YerMat](./YerMat.html):

See module [struct](http://docs.python.org/lib/module-struct.html) !

:::: 
::: 
``` 
   1 >>> import struct
   2 >>> struct.unpack('I', '\x00\xcc\x15\xa4')
   3 (2752891904L,)
   4 >>> struct.unpack('i', '\x00\xcc\x15\xa4')
   5 (-1542075392,)
   6 >>>
```
:::
::::

## See Also 

- [BitManipulation](BitManipulation) has a bunch on working with hex

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
