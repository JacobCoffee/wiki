# Asking for Help/How can I import a module from a sibling directory?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: How can I import a module from a sibling directory? 

I am new to Python from Java background, I have following structure

    /root
            /folder1
                    Class1.py
                    Class2.py
            /folder2
                    Class3.py

I am in the folder2 and want to run class3.py but it need to import a module from Class1.py Could someone please help me?

Answer: I believe you just need to add folder1 to your path variable. Should be something along the lines of\...

:::: 
::: 
``` 
   1 import sys
   2 sys.path.append('/root/folder1')
   3 import Class1
```
:::
::::

If that doesn\'t work, look through the documentation for info on how the sys.path variable works \-- I may just have the syntax slightly off

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
