# Johannes Gijsbers

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

See [JohannesGijsbers](http://c2.com/cgi/wiki?JohannesGijsbers "Wiki") for more on me, but I\'m subscribed to this page, so leave me messages here.

*On vacation for a while now.*

**Email:** jlgijsbers at planet dot nl

------------------------------------------------------------------------

So, if we had a nice pattern repository wiki, we could write about *decorate-sort-undecorate* there and link to it\... *{;D}=* \-- [LionKimbro](LionKimbro) 2003-11-21 22:18:39

[PortlandPatternRepository](http://c2.com/cgi/wiki?PortlandPatternRepository "Wiki")? ![;)](/wiki/europython/img/smile4.png ";)") \-- JohannesGijsbers

Two thoughts:

- I\'d like a *focused* design patterns community.

- I\'d like a *block* patterns community.

I think that there is a type of pattern that people use within a procedure.

For an example of a basic one, there is the [ForLoop](ForLoop).

But there are also others, like FirstTimeSeperate versus FirstTimeIntegrated.

That is, do you:

:::: 
::: 
``` 
   1 first_time_a()
   2 always_b()
   3 first_time_c()
   4 always_d()
   5 
   6 while condition:
   7   always_b()
   8   always_d()
```
:::
::::

\...or do you\...

:::: 
::: 
``` 
   1 first=1
   2 
   3 while condition:
   4     if first: first_time_a()
   5     always_b()
   6     if first: first_time_c()
   7     always_d()
   8     first=0
```
:::
::::

Surely, there are advantages to each one, no?

I taught beginning programmers for 2 years. I found that I didn\'t have words for a lot of things that I was trying to explain to them. Now I think I have the word for it: a \"block pattern.\"

I think a site of block patterns would be interesting, and very beneficial for study by beginners.

DecorateSortUndecorate may be a block pattern. But maybe not- maybe it\'s an algorithmic pattern. But are they that different?

Speaking of algorithms- we need multiple algorithms wiki. {:)}=

Good talking with you. Feel free to delete whenever you like.

\-- [LionKimbro](LionKimbro) 2003-11-22 04:45:20

What do you mean with a block pattern? It seems like another level of Scope (as in the [DesignPatternsBook](http://c2.com/cgi/wiki?DesignPatternsBook "Wiki")). \-- JohannesGijsbers

------------------------------------------------------------------------

As for DP: Yes, it is a matter of scope.

My design patterns book isn\'t about how you arrange your lines and variables within a function. It\'s about how you arrange your collection of classes, objects. I want \"block design patterns,\" to give my students who are just trying to figure out how to write a function.

Like: \"NestedLoops,\" to do things like cycling over lists of lists, and hitting all of them.

I\'ve been programming since I was 7 years old. When I took CS in college, I got to watch people smarter than I am struggle with how to calculate out a multiplication table, or follow two pointers in a row.

I don\'t think they\'re stupid. I think that I just figured out, through trial and error, in my first years of programming, how to make these basic structures.

It\'d be nice to have a systematic way to teach those basic \"block\" patterns. (I\'m just making up the term.)

\-- [LionKimbro](LionKimbro)

I see what you\'re getting at. How about \"[ProceduralPatterns](./ProceduralPatterns.html)\", with block patterns being one of the scopes involved. The other scope would probably be about splitting things up into functions. \-- JohannesGijsbers

Yes, yes, that\'s exactly it. Though I don\'t think it should pollute *this* wiki. ![:)](/wiki/europython/img/smile.png ":)") \-- [LionKimbro](LionKimbro)

------------------------------------------------------------------------

Johannes, Thanks for the message. I have read the spelling conventions. What bothered me was that you had used Wiki sometimes and wiki sometimes. I will go back to [FrontPage](FrontPage) and may the remaining cases consistent to the spelling conventions if that is ok. It looks like I made them consistent the wrong way,. ;o) \--[AndrewCates](AndrewCates)

------------------------------------------------------------------------

[CategoryHomepage](CategoryHomepage)
