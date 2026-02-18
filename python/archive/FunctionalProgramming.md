# FunctionalProgramming

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page demonstrates functional programming in Python.

## Challenge: Italicizing Text 

The challenge is to italicize some text that is specially marked in a [WikiLikeSyntax](../archive/WikiLikeSyntax).

For example, it should translate:

`"This includes ''italic'' text."`

into:

`"This includes <i>italic</i> text."`

Or even: `"This ''has'' several ''italic'' parts."` into `"This <i>has</i> several <i>italic</i> parts."`

## The Approach 

Our strategy is as follows:

1.  Divide the text into parts.
2.  Italicize every other part.
3.  Join the parts back together again.

## The Functional Solution 

:::: 
::: 
``` 
   1 italicize = lambda s: "".join(evens_and_odds(ident, italicize_one, s.split("''")))
```
:::
::::

*Wow!* One line! Put *that* in your pipe, and smoke it!

The advantages of functional programming are clear!

Well, yes and no; We have to provide the supporting functions, as well:

:::: 
::: 
``` 
   1 ident = lambda s: s
   2 italicize_one = lambda s: "<i>%s</i>" % s
   3 evens_and_odds = lambda evenf, oddf, L: [f(x) for (x, f) in zip(L, [evenf, oddf]*((len(L)+1)/2))]
```
:::
::::

Only four lines, total solution!

Let\'s look at how we might, more traditionally, perform this operation.

## The Traditional Way 

Here\'s a solution I had written, before I took an interest in functional programming:

:::: 
::: 
``` 
   1 def join_by_pairs(lst, start, end):
   2     """
   3     if   lst = [1,2,3,4,5,6,7,8],
   4     and  start = "a" and end = "b",
   5     
   6     result = [1,"a",2,"b",3,"a",4,"b",5,"a",6,"b",7,8]
   7 
   8     Notice that nothing is started that isn't ended.
   9     """
  10     num_links = len(lst)-1
  11     stops_lst = [start,end]*(num_links/2)
  12     result = []
  13     while len(stops_lst)>0:
  14         # add an item from  lst
  15         result.append(lst[0])
  16         lst = lst[1:]
  17         # add an item from  stops_lst
  18         result.append(stops_lst[0])
  19         stops_lst = stops_lst[1:]
  20     # copy over whatever is left
  21     result.extend(lst)
  22     return "".join(result)
  23 
  24 def bold_and_italics(text):
  25     """Perform '''bold''' and ''italics'' replacements.
  26 
  27     Note that, this assumes you've already called html_escape.
  28     """
  29     L = text.split("&apos;&apos;&apos;")
  30     text = join_by_pairs(L, "<b>", "</b>")
  31     L = text.split("&apos;&apos;")
  32     text = join_by_pairs(L, "<i>", "</i>")
  33     return text
```
:::
::::

I count 17 lines of actual code.

Granted, it\'s *slightly* different, and it also handles bolding.

We can add \"bolding\" to our code, as well:

:::: 
::: 
``` 
   1 bold_one = lambda s: "<b>%s</b>" % s
   2 boldize = lambda s: "".join(evens_and_odds(ident, bold_one, s.split("'''")))
   3 italicize_and_boldize = compose(boldize, italicize)
```
:::
::::

Oh, right, \"compose.\"

:::: 
::: 
``` 
   1 compose = lambda f, g: lambda x: g(f(x))
```
:::
::::

So, we\'ve added 4 lines. So we have a total of 8 lines.

## 47%, or 35%? 

8 against 17, still, is pretty good; 47%.

Some excuses, though: \"ident\" is standard issue. And if \"evens_and_odds\" *isn\'t* standard issue, there should at least be *something like it* that is. So I\'m going to claim that I\'ve got a *6 line* solution, which means I get credit for putting the function at *35%* it\'s original size.

Perhaps we\'re not scoring this the right way, though; Perhaps we should be talking about testing, debugging, documentation, or whatever. Perhaps it\'s worth something that there is no \"control flow\" here- no \"if\'s\" or \"while\'s\" at work; simply the gluing together of static pieces.

Regardless, there are clear advantages to programming this functionally, rather than in the more traditional way, even just comparing size alone.

## Where to Go from Here? 

If you found this intriguing, may I make a recommendation?

Study *the first section* of *the first chapter* of [TextProcessingInPython](../archive/TextProcessingInPython), by [DavidMertz](DavidMertz).

And then answer all the questions- in particular, question #3. If you can completely answer that question, (and it will require asking yourself a lot of sub-questions, and identifying commonalities in a lot of situations where ident is used,) you\'re probably in good shape.

You\'re also going to learn about \"currying.\" You might find yourself wanting a general \"curry anywhere\" function. Or the ability to reposition arguments to functions, and the like.

Have a look at [Python \"partial\" function proposals.](http://docs.python.org/dev/whatsnew/pep-309.html) Somewhere on the Internet, there\'s a complete \"partial\" implementation; I just forget where it is. I have it copied onto my other computer, I can\'t seem to locate it at the moment, though. It\'s an extremely useful function, though.

## Where You Can Go 

I\'ve written code that, in 5 short lines, performs a complete hierarchical parse of [OutlineMode](http://www.emacswiki.org/cgi-bin/wiki.pl?OutlineMode "EmacsWiki") data. And then adapted it slightly, to perform a complete hierarchical parse of still different code. It\'s based on a function that \"unflattens\" \-- you pass tests (generally regexes) that when applied to items in a list, figures out whether to \"go deep\" or to stay where it is.

If anybody requests it, I\'ll happily upload it here, along with my mess of functional support algorithms. I\'ve had bad experience getting response on this wiki; I often wonder if anybody\'s reading what goes on here. Perhaps everybody would just rather that this wiki were replaced with usenet forums, I don\'t know. (I actually prefer the ability to rework text, and to hyperlink between nodes.)

Regardless: You can do *amazing* things with functional programming. It seems to have something to do with abstracting out the \"for\" and \"while\" loops, and the ability to plug parts into other parts very easily.

## Function + Object Oriented Programming = Frankenstein 

I keep asking myself: \"What\'s going on here, with Functional Programming, and Object Oriented Programming?\"

[DesignPatterns](./DesignPatterns.html) and [ObjectOrientedProgramming](./ObjectOrientedProgramming.html) go a long way towards the \"plugging parts into other parts\" piece of the puzzle, but do they do it as tersely? The answer is clearly no. It takes two lines, minimum, just to get your \"class\" line out there, and your \"[init]\" line out there.

\"Higher Order Classes\" that combine other classes? Yikes; No-where near as elegant as the functions we see that combine and return other functions. This is not to suggest that there couldn\'t be a notation for classes that is as elegant; Only to say, I haven\'t seen it yet.

And do classes abstract out complex control structures? Well, complex control structures, \"yes,\" \-- \"managers\" and other class systems all have these complex control structures \-- but not the *simple* ones, like \"evens_and_odds.\" What do we call those kinds of things, like map, like reduce, like evens_and_odds, and so on? I don\'t know. But I don\'t see them, when I do object oriented programming, for some reason.

I perceive a tension between OO programming and Functional Programming. Functional Programming \"wants,\" (if you\'ll excuse my anthropomorphic spiritualist modeling,) to turn everything into a list, or an operation on a list. Object Oriented Programming, in turn, wants to turn everything into an object, a miniature fortress, an agent, an actor.

I find myself asking myself: \"Should this data be contained in an object, a fortress, a contained entity, with pre-conditions and post-conditions and methods and so on,\" or \"Should this data be held openly in lists, an interactive malleable nested table of data, mutable, copied, re-envisioned, transformed, by batallions of functional manipulators?\"

There\'s no clear and easy answer, but the two [metaphysical systems](http://communitywiki.org/MetaPhysics) seem at odds with one another.

I don\'t know the \"answer;\" But when my thoughts look for one, I find myself asking:

- Can Object Oriented Programming borrow Functional Programmings terse language mechanisms?

- Will Object Oriented culture develop easier ways of plugging objects in to one another, and creating adapters between their different interfaces?

- Is it crucial for OO programming, for Generic Programming (templates in C++, for instance) to take stronger hold in our minds? (That would make it easier to reuse objects, for instance, with different types.)

- Is the fundamental tension around issues of *security* and *integrity?* (Functional cares not for security; OO obsesses over it.)
