# Asking for Help/Why is my global not assigned?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: Why is my global not assigned? 

The following puzzles me: Both a and b are globals. Both are assigned an initial value in fun(). But b is considered unassigned in fun1().

:::: 
::: 
``` 
   1 def fun():
   2     global a,b
   3     a = [0]*1
   4     b = 0
   5     fun1()
   6 
   7 def fun1():
   8     a[0] += 1
   9     print('a[0]: ', a[0])
  10     b += 1
  11     print('b: ', b)
  12 
  13 
  14 fun()
  15 
  16  b += 1
  17 UnboundLocalError: local variable 'b' referenced before assignment
```
:::
::::

The purpose of `global`{.backtick} is to indicate which names are global in that specific part of a program. So, although you have indicated that `b`{.backtick} is global in `fun`{.backtick}, you still need to indicate that `b`{.backtick} is global in `fun1`{.backtick}. Otherwise, Python doesn\'t know where to get `b`{.backtick} from. It\'s actually slightly more complicated than this; for more, see below.

Now, you do manage to get away with not declaring `a`{.backtick} as global in both functions. The reason for this is that you aren\'t changing what `a`{.backtick} refers to, but are instead modifying an item (or element) in what `a`{.backtick} refers to (a list). So, Python deduces that `a`{.backtick} is a global and doesn\'t change its mind about it: `a`{.backtick} isn\'t itself made to refer to something else in `fun1`{.backtick}, so any reference to `a`{.backtick} is always to a global object.

So, back to the problem with `b`{.backtick}. When Python compiles `fun1`{.backtick}, it has to consider that `b`{.backtick} itself is being assigned to and that there\'s no `global`{.backtick} declaration for `b`{.backtick} in `fun1`{.backtick}. So, Python then believes `b`{.backtick} to be a local. But then, in the assignment itself, it has to get the value of `b`{.backtick} (think of it as `b + 1; b = <result>`{.backtick}), and at that point there is no such local, so you get the error.

In short, Python has to decide whether a name is local or global and stick with that decision for every mention of that name in a function: it can\'t switch between the two since it has to generate code that builds on the assumption that a name is always local or always global in that function. So you should always declare names as global in any function where you are assigning to them as globals. \-- [PaulBoddie](PaulBoddie) 2012-04-24 20:57:57

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
