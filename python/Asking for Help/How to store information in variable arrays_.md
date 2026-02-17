# Asking for Help/How to store information in variable arrays?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# How to store information in variable arrays? 

How would I store information in variables that I can go back later and compare? Such as

:::: 
::: 
``` 
   1 x = 1
   2 text = []
   3 while x <= 10:
   4      text.append(int(raw_input("Enter a number: ")))
   5      x = x + 1
   6 
   7 for x in range(10): 
   8     print text[x]
```
:::
::::

I just need to do this to compare a history to make sure a number hasn\'t already been entered earlier. But this is just a small example. I get nasty errors.

Thanks!

edit: that should work now We initialize a list first with `text = []`{.backtick}. Then we just append each element to that list.

------------------------------------------------------------------------

You can use the `in`{.backtick} operator:

:::: 
::: 
``` 
   1 if number in text:
   2     print "Number already entered!"
```
:::
::::

If you choose to use a set instead of a list\...

:::: 
::: 
``` 
   1 text = set()
```
:::
::::

\...then the above test still works, but you\'ll use the `add`{.backtick} method on the set when adding numbers, not an `append`{.backtick} method.

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
