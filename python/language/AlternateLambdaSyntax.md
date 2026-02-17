# AlternateLambdaSyntax

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

As it stands, Guido van Rossum has suggested that lambda forms will disappear in [Python3.0](./Python3(2e)0.html). This started a number of threads on comp.lang.python suggesting alternate syntaxes for lambda in the hopes that one of them might be more amenable to GvR\'s tastes. This pages summarizes these suggestions.

- Update: GvR has changed his tune; lambda will remain unchanged.

  (Reference: [http://mail.python.org/pipermail/python-dev/2006-February/060415.html](http://mail.python.org/pipermail/python-dev/2006-February/060415.html)). This page is kept as a historic record only \-- none of the proposals below satisfied GvR\'s taste.

The main hope of this page is to find a way to retain the functionality of existing Python lambdas - a way to create simple deferred expressions within another expression. For many uses (e.g. lazy argument evaluation, or simple callbacks) separating the deferred expression out into a named function can actually reduce clarity, as it overemphasises the deferred expression at the expense of the expression that the deferred expression is only one part of.

## Goals for Alternate Form 

### Definitely Desirable Features 

- Acceptable to BDFL
  - If Guido doesn\'t like it, it ain\'t gonna happen!
- At least as capable as current lambda expressions
  - If a new syntax is to replace the status quo, it needs to be at least equivalent in expressiveness
- More Pythonic / Less ugly
  - The current lambda syntax simply doesn\'t blend well with the rest of Python\'s syntax. A syntax which mixes in with other expressions as cleanly as list comprehensions and generator expressions do should have a much better chance of gaining BDFL approval.
- More friendly to inexperienced users
  - Compared to other Python keywords, \'lambda\' is rather esoteric. In the challenge for \"farthest outside day-to-day English usage\", its closest competitor would probably be \'assert\', as even \'def\' and \'elif\' are just abbreviations for \'define\' and \'else if\'. Use of simpler keywords may make deferred expressions appear less intimidating than they seem with the current unusual keyword.
- Less external baggage
  - One of the problems with lambda is that developers familiar with lambda calculus expect more of it than it provides. They expect full anonymous functions, whereas Python\'s lambda expressions allow deferred evaluation of only a single expression. An alternate syntax described as providing deferred evaluation of expressions rather than anonymous functions may be less prone to trigger complaints about the single expression limitation (consider: how often are complaints heard regarding the restriction of the expression section of list comprehensions or generator expressions to single expressions?).

### Arguably Desirable Features 

- Support anonymous suites
  - No discussion of lambda is complete without it being suggested that it should be possible to embed entire suites inside expressions. Accordingly, some suggestions along these lines are included below under the heading Real Closures.

## Current Syntax 

:::: 
::: 
``` 
   1 lambda a, b, c:f(a) + o(b) - o(c)
   2 lambda x: x * x
   3 lambda : x
   4 lambda *a, **k: x.bar(*a, **k)
   5 ((lambda x=x, a=a, k=k: x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

## New Syntaxes 

### Args Before Expression 

Alyssa Coghlan: def-to syntax [1](./(5b).html#a)\]

:::: 
::: 
``` 
   1 (def (a, b, c) to f(a) + o(b) - o(c))
   2 (def (x) to x * x)
   3 (def () to x)
   4 (def (*a, **k) to x.bar(*a, **k))
   5 ((def (x=x, a=a, k=k) to x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Alyssa Coghlan: def-arrow syntax [1](./(5b).html#a)\]

:::: 
::: 
``` 
   1 (def (a, b, c) -> f(a) + o(b) - o(c))
   2 (def (x) -> x * x)
   3 (def () -> x)
   4 (def (*a, **k) -> x.bar(*a, **k))
   5 ((def (x=x, a=a, k=k) -> x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Alex Martelli: def-as syntax [2](./(5b).html#b)\]

:::: 
::: 
``` 
   1 (def (a, b, c) as f(a) + o(b) - o(c))
   2 (def (x) as x * x)
   3 (def () as x)
   4 (def (*a, **k) as x.bar(*a, **k))
   5 ((def (x=x, a=a, k=k) as x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Dave Benjamin: fun syntax [7](./(5b).html#g)\]

:::: 
::: 
``` 
   1 (fun(a, b, c): f(a) + o(b) - o(c))
   2 (fun(x): x * x)
   3 (fun(): x)
   4 (fun(*a, **k): x.bar(*a, **k))
   5 ((fun(x=x, a=a, k=k): x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Roman Suzi: quote-colon syntax [9](./(5b).html#i)\]

:::: 
::: 
``` 
   1 ` a, b, c:f(a) + o(b) - o(c)
   2 ` x: x * x
   3 ` : x
   4 ` *a, **k: x.bar(*a, **k)
   5 ((` x=x, a=a, k=k: x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Ka-Ping Yee: arrow syntax

:::: 
::: 
``` 
   1 a, b, c -> f(a) + o(b) - o(c)
   2 x -> x * x
   3 -> x
   4 *a, **k -> x.bar(*a, **k)
   5 ((x=x, a=a, k=k) -> x(*a, **k) for x, a, k in funcs_and_args_list)
```
:::
::::

to-syntax

:::: 
::: 
``` 
   1 a, b, c to f(a) + o(b) - o(c)
   2 x to x * x
   3 to x
   4 *a, **k to x.bar(*a, **k)
   5 ((x=x, a=a, k=k) to x(*a, **k) for x, a, k in funcs_and_args_list)
```
:::
::::

Tom Anderson: anonymous def syntax, normal form [12](./(5b).html#j)\]

:::: 
::: 
``` 
   1 def (a, b, c): return f(a) + o(b) - o(c)
   2 def (x): return x * x
   3 def (): return x
   4 def (*a, **k): return x.bar(*a, **k)
   5 ((def (x=x, a=a, k=k): return x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Tom Anderson: anonymous def syntax, shorthand form [12](./(5b).html#j)\]

:::: 
::: 
``` 
   1 def (a, b, c) = f(a) + o(b) - o(c)
   2 def (x) = x * x
   3 def () = x
   4 def (*a, **k) = x.bar(*a, **k)
   5 ((def (x=x, a=a, k=k) = x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Anders Munch: bare def syntax

:::: 
::: 
``` 
   1 (def (a, b, c) f(a) + o(b) - o(c))
   2 (def (x) x*x)
   3 (def () x)
   4 (def (*a, **k) x.bar(*a, **k))
   5 ((def (x=x, a=a, k=k) x(*a, **k)) for x, a, k in funcs_and_args_list)
```
:::
::::

### Expression Before Args 

Alyssa Coghlan: post-def syntax This is based on the \"normally nested expression before statement keyword\" idiom used with generator expressions, list comprehensions and PEP 308 conditional expressions.

:::: 
::: 
``` 
   1 (f(a) + o(b) - o(c) def (a, b, c))
   2 (x * x def (x))
   3 (x def ()) # Making the empty param list optional would be good for lazy arguments: (x def)
   4 (x.bar(*a, **k) def (*a, **k))
   5 ((x(*a, **k) def (x=x, a=a, k=k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Alyssa Coghlan: for syntax [6](./(5b).html#f)\]

:::: 
::: 
``` 
   1 (f(a) + o(b) - o(c) for (a, b, c))
   2 (x * x for (x))
   3 (x for ())
   4 (x.bar(*a, **k) for (*a, **k))
   5 ((x(*a, **k) for (x=x, a=a, k=k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Robert Brewer: for (no-parens) syntax [3](./(5b).html#c)\]

:::: 
::: 
``` 
   1 (f(a) + o(b) - o(c) for a, b, c)
   2 (x * x for x)
   3 (x for ())
   4 (x.bar(*a, **k) for *a, **k)
   5 ((x(*a, **k) for (x=x, a=a, k=k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Alyssa Coghlan: def-from syntax [4](./(5b).html#d)\]

:::: 
::: 
``` 
   1 (def f(a) + o(b) - o(c) from (a, b, c))
   2 (def x * x from (x))
   3 (def x from ())
   4 (def x.bar(*a, **k) from (*a, **k))
   5 ((def x(*a, **k) from (x=x, a=a, k=k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Alyssa Coghlan: from syntax (posted to clp, no reference handy)

:::: 
::: 
``` 
   1 (f(a) + o(b) - o(c) from (a, b, c))
   2 (x * x from (x))
   3 (x from ())
   4 (x.bar(*a, **k) from (*a, **k))
   5 ((x(*a, **k) from (x=x, a=a, k=k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Michael Spencer: from-args syntax [5](./(5b).html#e)\]

:::: 
::: 
``` 
   1 (f(a) + o(b) - o(c) from args(a, b, c))
   2 (x * x from args(x))
   3 (x from args())
   4 (x.bar(*a, **k) from args(*a, **k))
   5 ((x(*a, **k) from args(x=x, a=a, k=k)) for x, a, k in funcs_and_args_list)
```
:::
::::

Michael Spencer: for-args syntax [5](./(5b).html#e)\]

:::: 
::: 
``` 
   1 (f(a) + o(b) - o(c) for args(a, b, c))
   2 (x * x for args(x))
   3 (x for args())
   4 (x.bar(*a, **k) for args(*a, **k))
   5 ((x(*a, **k) for args()) for x, a, k in funcs_and_args_list)
```
:::
::::

Bengt Richter: colon-function-application syntax [8](./(5b).html#h)\]

:::: 
::: 
``` 
   1 (:f(a) + o(b) - o(c))(a, b, c)
   2 (:x*x)(X)
   3 (:x)()
   4 (:x.bar(*a, **k))(*a, **k)
   5 ((:x(*a, **k))(x=x, a=a, k=k) for x, a, k in funcs_and_args_list)
```
:::
::::

Talin: \'given\' keyword (Same as the \'for no parens\' except uses a different keyword.)

:::: 
::: 
``` 
   1 (f(a) + o(b) - o(c) given a, b, c)
   2 (x * x given x)
   3 (x given ())
   4 (x.bar(*a, **k) given *a, **k)
   5 ((x(*a, **k) given (x=x, a=a, k=k)) for x, a, k in funcs_and_args_list)
```
:::
::::

### functional syntax 

[lwickjr](lwickjr): How about converting the `lambda` functionality into a function? For example, in pure can-do-now Python:

:::: 
::: 
``` 
   1 from types import FunctionType as function
   2 def anonymous(
   3         name=None,
   4         filename=None,
   5         mode="eval",
   6         func_globals=None,
   7         func_closure=None,
   8         func_argdefs=(),
   9         flags=0,
  10         dont_inherit=False,
  11         source=None,
  12         code=None,
  13         ):
  14         """Create a possibly anonymous function inline"""
  15         ## Compute suitable default values from stack frame, omitted for brevity.
  16         if source: code = compile(soource, filename, mode, flags, dont_inherit=True)
  17         return function(code, func_globals, name, func_argdefs, func_closure)
```
:::
::::

If you don\'t like `anynomous` for the name, suggest something else! ![;)](/wiki/europython/img/smile4.png ";)")

### Real Closures 

Real closures subsume the functionality of lambda plus allow for multi-line statements.

------------------------------------------------------------------------

Curly braces for single-line and anonymous def for multi-line (from [10](./(5b).html#h)\], boo [11](./(5b).html#h)\], and this is also very similar to how Ruby does it):

:::: 
::: 
``` 
   1 #single-line (similar to ruby syntax)
   2 {a,b,c | return f(a) + o(b) - o(c)}
   3 {x | return x*x}
   4 {return x}
   5 {*a, **k | return x.bar(*a, **k)}
   6 
   7 #multi-line
   8 x = def (a,b,c):
   9     return f(a) + o(b) - o(c)
```
:::
::::

------------------------------------------------------------------------

Perhaps anonymous def for single line, anonymous def for single-line?

    foo.addCallback(def (result): result + 1)
    foo.addCallback(def (result, myExtra, args):
                         print 'hi!'
                         result += 1
                         return result
                    , extra, args=here)

Tom Anderson\'s syntax (which is subtly different - it still wants a return in single-line anonymous defs) could also be used for multi-line closures in this way.

## References 

- \[1\] [http://mail.python.org/pipermail/python-list/2004-December/256859.html](http://mail.python.org/pipermail/python-list/2004-December/256859.html)

- \[2\] [http://mail.python.org/pipermail/python-list/2004-December/256881.html](http://mail.python.org/pipermail/python-list/2004-December/256881.html)

- \[3\] [http://mail.python.org/pipermail/python-list/2004-December/257023.html](http://mail.python.org/pipermail/python-list/2004-December/257023.html)

- \[4\] [http://boredomandlaziness.skystorm.net/2004/12/anonymous-functions-in-python.html](http://boredomandlaziness.skystorm.net/2004/12/anonymous-functions-in-python.html)

- \[5\] [http://mail.python.org/pipermail/python-list/2004-December/257893.html](http://mail.python.org/pipermail/python-list/2004-December/257893.html)

- \[6\] [http://mail.python.org/pipermail/python-list/2004-December/257977.html](http://mail.python.org/pipermail/python-list/2004-December/257977.html)

- \[7\] [http://mail.python.org/pipermail/python-list/2005-January/258441.html](http://mail.python.org/pipermail/python-list/2005-January/258441.html)

- \[8\] [http://mail.python.org/pipermail/python-list/2005-January/258578.html](http://mail.python.org/pipermail/python-list/2005-January/258578.html)

- \[9\] [http://mail.python.org/pipermail/python-list/2005-January/258581.html](http://mail.python.org/pipermail/python-list/2005-January/258581.html)

- \[10\] [http://mail.python.org/pipermail/python-list/2005-January/258113.html](http://mail.python.org/pipermail/python-list/2005-January/258113.html)

- \[11\] [http://boo.codehaus.org/Closures](http://boo.codehaus.org/Closures)

- \[12\] [http://mail.python.org/pipermail/python-list/2005-June/287966.html](http://mail.python.org/pipermail/python-list/2005-June/287966.html)
