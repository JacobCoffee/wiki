# Asking for Help/'break' outside loop

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

I ask for help about an error I recieved in the tutorial of Hunt the Wumpus in the Hello! Python guide book

# Asking for Help: \... 

Hello. my name is Jonmark, and I recieved the Hello! Python book as a gift in order to learn programming. I strated working, and right at the beginning, at the part where you create your first program, the basic version Hunt the Wumpus game. I copied the the written text, made the required modifications and right when I was about to finish the program (I know its to big of a word for that basic game), the command line told that at the last line (see the program code) the is an error. it said: \"SyntaxError: \'break\' outside loop\". I tried for some time to modifie the statement with the meager knowledge I possess of the Python language but at the time of the writing, I held no success. can anyone aid me in this dire of times? thank you in advance, Jonmark

------------------------------------------------------------------------

It sounds like the `break`{.backtick} statement isn\'t being associated with the statements inside the loop because it isn\'t at the right indentation level. Python uses \"whitespace\" - that is, spaces and tabs, which effectively leave blank space in a line of a program - to indicate groups of statements. For example:

:::: 
::: 
``` 
   1 total = 0
   2 for number in range(1, 10):
   3     total += number
   4     print total
```
:::
::::

Here, lines 3 and 4 are grouped together inside the `for`{.backtick} loop. What may have happened to you is something like this:

:::: 
::: 
``` 
   1 total = 0
   2 for number in range(1, 10):
   3     total += number
   4 print total
```
:::
::::

Here, I\'m using something other than `break`{.backtick} to illustrate a general point. If you really wanted the `print`{.backtick} statement to work each time you go round the loop, then the second piece of code isn\'t what you want because the `print`{.backtick} statement on line 4 is not at the same level as the rest of the body of the loop (which is line 3).

So you need to make sure that the whitespace is exactly correct in the program you\'ve copied from the book. You also need to be a bit careful about tabs and spaces. If you use the tab key to position the statements on each line, avoid using the space bar to do this job in the same program: sometimes the tab key produces special tab characters - not space characters - and Python treats these tab characters differently (as a certain number of spaces). You can check your program by running it with the `-t`{.backtick} option. For example:

    python -t program.py

I hope this helps a bit. \-- [PaulBoddie](PaulBoddie) 2012-01-06 16:36:25

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
