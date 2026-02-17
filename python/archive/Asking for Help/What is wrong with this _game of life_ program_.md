# Asking for Help/What is wrong with this "game of life" program?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: What is wrong with this \"game of life\" program? 

I have a problem with a program for Conway\'s Game of Life. Here\'s the source code:

:::: 
::: 
``` 
   1 #! /usr/bin/env python
   2 # Conway's game of life on a finite rectangular universe
   3 # The boundary is considered to be perpetually dead.
   4 
   5 def disp(state):
   6     h, v, zz = len(state[0])-2, len(state)-2, "+"
   7     for t in range(h):
   8         zz += "--"
   9     print zz + "+"
  10     for t in range(v):
  11         z = "|"
  12         for u in range(h):
  13             z += ["  ", "88"][state[t+1][u+1]]
  14         print z + "|"
  15     print zz + "+"
  16     for t in range(3):
  17         print
  18 
  19 def iterate(state):
  20     h, v, new = len(state[0])-2, len(state)-2, state
  21     r = [[0,0,0,1,0,0,0,0,0],[0,0,1,1,0,0,0,0,0]]
  22     for t in range(v):
  23         for u in range(h):
  24             aa = state[t][u]
  25             ab = state[t][u+1]
  26             ac = state[t][u+2]
  27             ba = state[t+1][u]
  28             bb = state[t+1][u+1]
  29             bc = state[t+1][u+2]
  30             ca = state[t+2][u]
  31             cb = state[t+2][u+1]
  32             cc = state[t+2][u+2]
  33             s = aa+ab+ac+ba+bc+ca+cb+cc
  34             new[t+1][u+1] = r[bb][s]
  35     return new
  36 
  37 state, s, iters = [], [], 0
  38 for t in range(20):
  39     state.append([])
  40     for u in range(20):
  41         state[t].append(0)
  42 
  43 state[3][3] = 1
  44 state[4][4] = 1
  45 state[5][4] = 1
  46 state[5][3] = 1
  47 state[5][2] = 1
  48 
  49 while True:
  50     print iters
  51     disp(state)
  52     for t in range(1000000):
  53         pass
  54     state = iterate(state)
  55     iters += 1
```
:::
::::

The program doesn\'t quite do what it should, but I can\'t find anything wrong with the source.

::: note
When *answering* questions, add the [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered) category when saving the page. This will move the link to this page from the questions section to the answers section on the [Asking for Help]() page.
:::

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp)
