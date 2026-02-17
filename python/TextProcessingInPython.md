# TextProcessingInPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Text Processing in Python** is a book by [DavidMertz](DavidMertz).

The free text is available at:

[http://gnosis.cx/TPiP/](http://gnosis.cx/TPiP/)

Buy the dead-trees version at:

[http://tinyurl.com/jskh](http://tinyurl.com/jskh)

A review by Danny Yee at: [http://dannyreviews.com/h/Text_Python.html](http://dannyreviews.com/h/Text_Python.html)

# Notes 

I\'m uploading some notes I kept from section 1.1, on his combinatorial [HigherOrderFunction](./HigherOrderFunction.html)s, in the thought that someone might gain some use or insight out of it. \-- [LionKimbro](LionKimbro)

## Chapter 1, Section 1 

### Combinatorial.py 

![mertz_chof.png](attachments/TextProcessingInPython/mertz_chof.png "mertz_chof.png")

[mertz_chof.svg](attachments/TextProcessingInPython/mertz_chof.svg)

### Question 3 

I took a particular interest in question 3. Question 3 asks: \"Why is ident() important?\"

`ident()` is critical because it\'s a pass-through function.

You really have to look at what the whole \"higher order function\" (HOF) thing is all about, in order to really get it.

Outline of explanation:

- HOF\'s Contribute Functionality
- There is Space for Custom Functionality
- Ignoring Custom Functionality
- Ident is None, NULL, 0, Pass-Through

**HOF\'s Contribute Functionality**

A lot of times, we look at these higher-order-functions, and we think to ourselves, \"Why, that\'s easy. That\'s so basic. That\'s not really *doing* anything. It\'s just this little flim-flam wrapper.\"

So, let\'s look for a second at one of these flim-flam wrappers. Let\'s look at the function: \"and\_\".

`and_ = lambda f,g: lambda x, f=f, g=g: f(x) and g(x)`

Look at it! *Look at it!* It\'s rediculous! There\'s hardly anything there. It\'s arguably more wrapper, than functionality.

So, we think of this as being \"nothing.\"

But, look more carefully.

In Question 2, right before Question 3, David was starting to point this out to us- making us think about \"shortcutting.\" Let\'s look at this a liitle more deeply, shall we?

    if operator.truth(f(x)):
        if operator.truth(g(x)):
            return True
    return False

What I\'ve done here is expanded out the functionality of \"and\", in long form, to show a bit more of the structure.

Does it still appear flimsy? Well, let\'s talk about this. Let\'s look at the functionality, qualitatively.

Functionality and structure that we can find in here:

- We convert the output of f(x) to True or False, making use of the operator.truth method.
- We convert the output of g(x) to True or False, making use of the operator.truth method.
- The algorithm has an if-then structure, with one nesting.
- We return True or False.

So, we see, that there\'s actually some \"stuff\" that\'s going on in here; There\'s some stuff happening in that little \"and\" expression.

And, in fact, for the HOF\'s in general, there\'s \"stuff\" going on. It is often hidden; especially within these more simple atomic functions.

How was it hidden?

It was hidden in the *language.* It was hidden in the operators. We just *assume* when we see `and`, to think that it will do these various things. But we rarely think of it as having 4 attributes of functionality, or 3 attributes, or whatever. We just think \"oh, this is very simple and basic.\"

But, it is a mistake. And when we see these HOFs in `combinatorial.py`, and think that because they\'re all one-liners, that there\'s \"not much going on in there,\" we\'re making this mistake. We fail to see the structure, the operations being performed, and so on.

So we end up with this simplistic idea of what HOF\'s are all about. And then when we\'re asked: \"Why is `ident()` so important,\" we\'re struck dumb, because we can\'t see it.

- HOFs are introduced to readers through very simple expressions.
- But the simple expressions actually have deeper functionality and structure to them.
- So we end up thinking that HOFs are simplistic, when actually, they\'re more interesting than that.

**There is Space for Custom Functionality**

HOFs accept or return functionality.

Let\'s just consider those HOFs that accept functionality, right now. (Regardless of whether or not they return functionality.) We\'re talking about the ident() function. Arguably, it could be returned from \"`foo(0)`\", but that\'s just a distraction at this point; We\'re here to understand the value of ident(). (You can come back and think about this later, after you\'ve read the full article.)

So considering HOFs that accept functionality,\... What\'s happening here?

We\'ve got a HOF, a HOF that is itself a complex array of function calls and structure, and we\'re being given the opportunity to supply some function calls of our own, into this system.

The image to hold in your mind is of a gigantic clockwork. You\'ve got a HOF. By now, you should have ejected the image in your mind of a simple flimsy thing. Instead, I want you to see the HOF as a mighty machine, a gigantic clockwork.

And now you have this opportunity, to plug in your own clockwork, into the system.

It\'s got some sockets, you see, where you can say, \"Oh, I\'m going to plug in my own custom machine here.\"

This is what the whole \"Higher Order Function\" thing is about, you see: It\'s about working with machinery itself, and not just data.

So, in a HOF, (one that accepts functionality, at least,) you have all these opportunities for inserting your own, custom, functionality.

**Ignoring Custom Functionality**

But sometimes, you don\'t WANT to put in custom functionality!

Sometimes, you want to just say, \"I\'ll pass.\"

*Why would you do that?*

That\'s what our question is all about, isn\'t it?

Why would you do that?

Framed this way, the answer is clear:

You\'d do that, because you care about *the rest of the functionality.*

Remember: The HOF is a gigantic clockwork. It\'s a \"mighty machine.\"

You might not *care* about whatever little piece of machinery you can put in there; You might *only* want to make use of exactly whatever is in the gigantic clockwork.

So if you want what is in the gigantic clockwork, but you don\'t care about what\'s in your little contribution to the final machine, then you just pass \"ident()\".

**Ident is None, NULL, 0, Pass-Through**

`ident()` is \"None.\" `ident()` is \"NULL.\" `ident()` is 0 (zero).

`ident()`, in higher-order-function land, is \"pass-through,\" or \"pass.\"

\"No thank you.\"

So the answer to the question \"Why ident()?\", \... \...is: \"Because I wanted the functionality that was in the HOF, unaltered.\"

The reason we were confused, is because we thought that HOF\'s didn\'t \"do anything\" on their own. But they do, and it can be adventageous to us to take advantage of it.

Question 3 was nice, because it kindly pointed towards what this whole \"higher order function\" thing is all about.

Frankly, I don\'t know what the \"hint\" was about.

          Hint: Suppose you have a list of lines of text, where some
          of the lines may be empty strings.  What filter can you
          apply to find all the lines that start with a '#'?

Perhaps I just don\'t have a very good answer to question 3. Perhaps I\'ve missed some essential point.

But, here was my answer to the hint:

:::: 
::: 
``` 
   1 return filter(lambda x:x.startswith("#"), lines)
```
:::
::::

Frankly, I didn\'t see any insight there.

If anyone knows, please let me know. (Perhaps attach a comment here, or something.)

**Remainder of the Answer**

From here, I\'ll show a couple examples, of what we learned here. That is, I\'ll show places where you might want to use `ident()`, in order to take advantage of the unadulterated functionality embodied within the HOF.

- Validation \-- using and\_ (& and\'s *shortcutting*)

- Copy \-- get a copy of arguments in the output

**Validation**

The first example is validation.

We can perform validation on an argument, making sure that it is non-Null, before performing a test on the argument with another function, to see if it\'s true or not.

So, instead of writing:

    if x is not None:
        if operator.truth(f(x)):  # f(x) will break, if x is None
            do_foo(x)

\...over and over, we can construct a general function through HOF magic,\...

    general = and_(ident, f)

\...and then:

    if general(x):
      do_foo()

You\'ve got two benefits here:

- You\'ve got a general function.
- This is all shorter.

**Copy**

Just to see something a little different, we\'ll look at using `ident()` to generate a copy of input, in the output.

`apply_each(funcs, args)` is a function that applies the arguments to a series of functions, and gives you back the results in a list.

:::: 
::: 
``` 
   1 apply_each = lambda fns, args=[]: map(apply, fns, [args]*len(fns))
```
:::
::::

Or, in the preferred Python list-comprehension form:

:::: 
::: 
``` 
   1 apply_each = lambda fns, args=[]: [f(*args) for f in fns]
```
:::
::::

So, if you wanted to make a function that constructs: `[f(x), x]`

\...for whatever, reason, you can:

:::: 
::: 
``` 
   1 my_func = apply_each(f, ident)
```
:::
::::

**Conclusion**

So, just to remind you: Why is `ident()` useful?

It\'s useful because it makes it possible to take advantage of the raw functionality of combinatorial higher order functions.
