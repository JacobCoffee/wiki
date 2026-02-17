# WithStatement

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page is dedicated to the public discussion of [PEP 343](http://www.python.org/peps/pep-0343.html): Anonymous Block Redux and Generator Enhancements.

I think this is a good one; I hope people agree. Its acceptance will obsolete about 4 other PEPs! (A sign that it fulfills a need and that the proposed solution is powerful.)

Please read the PEP; then add your comments here. Please sign your comments with your name. [GvR](GvR) (Guido van Rossum)

------------------------------------------------------------------------

Can someone please speak to the implementation schedule for WithStatement? I am dying to use it, but I don\'t appear able to import it even from the [future] yet! \-- Barnard Masonry

------------------------------------------------------------------------

I feel like PEP 343 and PEP 342 work together in some important way, but it\'s not clear what that is. Does one depend on the other? What kind of things are possible if both are accepted (vs. just one of them)? I think this is important to understanding where PEP 343 is leading; some discussion of this would be appreciated. \-- [IanBicking](IanBicking)

- No, they are quite independent. PEP 342 is for making generators into real coroutines. Maybe throw() can help a tiny bit there but I think it\'s not essential. PEP 342 adds argument-less yield to PEP 343 which is a very minor improvement (no \"yield None\"). [GvR](GvR)

------------------------------------------------------------------------

To assist in avoiding the mistake pointed out in the optional extension, the documentation of the standard library should include a description on how to use (or: how not to use) objects that support the `__enter__`/`__exit__` protocol. E.g.

- Do not use objects of this class as a parameter to `with`.

or

- Objects of this class may be used as a parameter to `with`. However, they will become invalid after the `with` block.

\-- *Eric Nieuwland*

- I\'d be very surprised if an object supporting `__enter__` and `__exit__` would say \"do not use this in a with-statement.\" ![:-)](/wiki/europython/img/smile.png ":-)") What makes sense, however, is to distinguish between objects that can be used at most once in a with-statement (like files) and objects that can be used over and over (like locks). [GvR](GvR)

The solution to this problem recommended in PEP 346 is to throw an explicit exception in `__enter__` when a non-reusable template is reused. PEP 343 uses this approach for the [generator-based templates](http://3d2f.com/tags/generator/based/templates/download/), and I would expect an `__enter__` method on file objects to do the same thing. \-- *Alyssa Coghlan*

------------------------------------------------------------------------

next_throw() is easier to grep with next(). *Niki Spahiev*

- Given that 99% of uses of both are implicit, I don\'t see how that matters. [GvR](GvR)

I don\'t want to teach beginners why python uses \'raise\' sometimes and \'throw\' other times. I predict: they\'re going to be coming from other languages, they\'re going to accidentally use \'throw\' as the statement, and they\'re going to get mad at \"all of python\'s weird quirks, like how it has both raise and throw\". *Drew Perttula*

- I\'m not so worried. Your tolerance for language quirks seems rather low. ![:-)](/wiki/europython/img/smile.png ":-)") [GvR](GvR)

  Raymond Hettinger added on python-dev (copied here by [GvR](GvR)):

  - \"This was intended. There was much discussion about this for PEP 288 and this was more or less a concensus choice. The term is already associated with exceptions in other languages and it captures the concept of the raise occurring somewhere else (what is thrown at or into). It is simple, clear, and tends to suggest all the right things. I have no doubt that someone can point out differing semantics in other languages but I don\'t care. The verbal cue is what we are after.\"

------------------------------------------------------------------------

I\'ve tuned out the recent conversation on these PEPs quite religiously, because I never thought they would result in anything even vaguely useful. Fortunately, I was dead wrong. PEP-343 is simple, elegant, and feels very Pythonic to me. I need to catch up now and think through the implications and corner-cases, but I can give a provisional +1 to the concept. Thanks to all those that didn\'t tune out and worked to get us to this point. \-- *Kevin Jacobs*

------------------------------------------------------------------------

A few immediate comments:

1.  Is g.throw(\...) supposed to let you raise exceptions in other threads (by having g catch the exception you throw it, then raise its own exception for its caller)? The PEP should be clear about this. It would be great if the answer is yes and if that\'s the case, objects like queues and sockets should be turned into generators to permit cross-thread signalling using generator exceptions. But I had the impression that this would be difficult in CPython.
    - This is not the intention at all. The PEP specifically speaks of \"where the generator g is currently suspended\". By definition this implies that it is not running in another thread. You must have had threads on your mind too much

      recently to even think of this. ![:-)](/wiki/europython/img/smile.png ":-)") [GvR](GvR)

      - I will read it again, but I don\'t remember seeing anything that made me think the generator couldn\'t be suspended in another thread. phr
        - Generators aren\'t tied to a thread, but they can only be executing in one thread at a time. When a generator yields in one thread, another thread can resume it with next() or throw() \-- but then the resumed generator executes in the thread that called next() or throw(). There\'s nothing new to this \-- it\'s been like this

          since generators were invented. [GvR](GvR)

          - Well, throw() didn\'t exist when generators were invented, so throw hasn\'t always been like anything ;-). If throw is supposed to resume execution in the throwing thread rather than the thread where the generator was last suspended, the PEP should clearly specify that. \--phr
            - It already says that throw() is just like next(). [GvR](GvR)
2.  I thought some of the original motivation of PEP 310 was to lessen the pain of giving up the idiom of expecting files to be closed when their last reference goes away. So if 343 no longer guarantees that the exit method will be run when the \"with\" statement finishes, it\'s lost some of its main motivating functionality. I wonder if having a more serious treatment of block scope, so that destructors are guaranteed to be called when a scope exits (by falling through or via an exception), would also take care of this issue.
    - Where did you read that the `__exit__` method isn\'t guaranteed to be called upon exit from the with statement? The translation explicitly calls it! Read again. You may be confused with g.close(). That\'s only relevant when you use a for-loop without an explicit with-statement. [GvR](GvR)

There was some good discussion on clpy a while ago that I\'ll try to locate, and add some more comments during the weekend. \--Paul Rubin (phr)

------------------------------------------------------------------------

Overall I think this is a great proposal. It will allow a lot of things to be made a great deal more natural - probably many things that have not yet been considered.

I can see a lot of areas in the standard libs where improvements could be made using this construct. It will seem slightly inconsistent in areas where this is not done.

The only negative to the proposal is the extra complexity. The idea is a little magical, and may not be easy for new users to pick up. New users will not be forced to use it of course. However ironically the very usefulness of the idiom will probably lead to it being widely used in libraries, which will of course require new users to learn it sooner or later!

\-- [MichaelSmith](MichaelSmith)

------------------------------------------------------------------------

I like the idea and the \"with .. as ..\" syntax, where readable keywords are used instead of obscure characters, like decorators use. It looks like Python to me. What I don\'t like is the use of decoratorated generators to create the templates. Generators don\'t seem to fit the problem here. First you have to add generator enhancements. Then you use a decorator, because the enhancements still don\'t make generators fit the problem. It is almost like generators and decorators are the latest and coolest additions to the language, so we\'re going to use them for everything we possibly can. I find example 4, using a simple class, to be much more readable than example 1. To me, example 4 shows the relative DISadvantage of using a generator template. I would dump the generator changes and just keep the with statement.

Patrick Ellis

- Well, you have a choice not to use generators. ![:-)](/wiki/europython/img/smile.png ":-)") To many who participated in the discussion on python-dev, using generators to write templates is an essential part. The more state you carry over from `__enter__` to `__exit__` the more you will appreciate the generator. [GvR](GvR)

------------------------------------------------------------------------

What happened to Fredrik Lundh\'s proposal (14/5/2005) to use the existing \'try\' keyword instead of \'with\', eg:

    try opening(file) as f: ...
    try locking(mutex): ...
    try atomic_transaction(connection): ...

Try already has the idea of doing cleanup at block exit. I saw only reply in support of the idea on the list, but no other comments.

Thomas Leonard

- When this were combined with an except or finally clause, it would be confusing to the reader which applies to which \-- does the except clause

  catch exceptions in the `__exit__` method, or does the `__exit__` method see exceptions raised in the except clause? [GvR](GvR)

  - Python already has this problem when combining except and finally. If we take the same solution (make them mutually exclusive) then there\'s no problem. You still get a more readable syntax and one less keyword. Thomas Leonard
    - Doesn\'t help.

      When combining except & finally, the answer is explicit: control moves only forward. (At the very least you can use this to remember the rule.) But when combining with & except (or finally), the handler for with is implicit, so there is no parallel heuristic to decide which one handles which. [GvR](GvR)

      - I meant, don\'t allow combining with & except or with & finally. Ie, the try: has neither an except nor a finally clause if it has an expression. After all, the proposed with: syntax doesn\'t allow these either. I\'m not sure what you mean about control moving forwards. The versions of Python here (2.3 and 2.4) don\'t allow except and finally at the same time.

------------------------------------------------------------------------

I can\'t tell from the PEP whether or not it is recommended that objects themselves expose `__enter__` and `__exit__` (like locks and files). It mentions the possability, but all the examples do otherwise. Greg Ewing was the only person I remember disliking the idea, but then changed his mind (to a tepid +0.6).

I do understand the reluctance to pick the one-and-only way an object can be used in a `with` statement, but I suspect that most classes are factored well enough that the default `with` behavior is obvious (and more obvious than using a helper function like `opening` or `locking`). And any object that may have more than one `with` behavior can have 0 or 1 inherent behaviors and 1 or more helpers, but I seriously doubt there would be any cases like that in the standard library.

\-- [BenjiYork](BenjiYork)

- Time will tell. The with-statement doesn\'t force you either way. The PEP doesn\'t strongly recommend either way because we don\'t have the experience with this yet to know which pattern is better. Personally I\'d like to be cautious \-- use explicit wrapper methods

  like opening() and locking() first, and add `__enter__` and `__exit__` methods to some objects later. [GvR](GvR)

------------------------------------------------------------------------

Personally I find the half-hearted approach to adding features rather frustrating. I liked new style classes a lot, and I like classmethod and company. But it was frustrating that decorator syntax didn\'t come along until a couple releases after we needed them (putting aside how absurdly difficult a decision that turned out to be). I think it led to a very gradual and vague adoption of new class functionality. And maybe that\'s not bad, but as someone who likes the features it was frustrating. At the time, I felt like I was being punished for using new features because the syntax wasn\'t keeping up with other parts of the language. And the punishment continues, because I don\'t feel like I can use decorators for another year because I still have to support Python 2.3.

It also means much more tracking of versions. Now will I have to know that, in Python 2.4 I use `try:finally:`, in Python 2.5 `with opening()`, in Python 2.6 `with open()`, etc.? Can\'t we have a little faith in our imaginations and add a few `__enter__` and `__exit__` methods that seem so obviously useful, like to files and threading.Lock objects?

Adding features is always a problem, but adding them gradually just makes it that much worse. I think the reception of this feature is positive enough (+1 from me, BTW) that it shows people understand why it matters and understand where we should start using it right away. \-- [IanBicking](IanBicking)

- Trust me, it is frustrating for me too. But given the large number of users we *have* to go slowly. Compare it to upgrading a freeway or an airport. It\'s much more complicated than building a new one, because you have to accommodate existing traffic while the work is going on. But the alternative is Perl 6\...

  In this particular case, I actually believe that adding `__enter__` and `__exit__` to file objects is *wrong*, but for lock objects it is *right*. Does that help?

  [GvR](GvR)

  - So you don\'t think we should detect `with open(X)` as a special language construct?!? Sorry, just trying to think about how Perl would approach this\... ![;)](/wiki/europython/img/smile4.png ";)") I\'m certainly not set on any particular example, I haven\'t

I would prefer that `__enter__` and `__exit__` be added to `Lock` and `RLock` objects, since it\'s really, REALLY obvious what `with lock:` does. Hey, and nice work on unifying the synchronize keyword, database transactions, etc into the (consistent and intuitive) PEP 343. I see why [IanBicking](IanBicking) thinks PEP 342 and 343 are related: they both do black magic with generators, look weird at first, but end up making a lot of sense and looking Pythonic. I didn\'t think coroutines could be expressed so cleanly in Python, either. It\'s impressive, really. \-- [ConnellyBarnes](./ConnellyBarnes.html)

## Using \".something\" syntax 

I think many Python programmers hate endless ` self.XXX ` in, for example, ` __init__(self) `. Maybe it could be replaced with ` .XXX `:

    class A(object):
        def __init__(self):
            .state = "OK"
            .value = 1

I think it may be useful because WITH statement would be often used like ` with self: `

- I think the . in this case is much to easy to overlook. If you really dislike writing self. so much, you could use an editor macro to translate your version to real python

## Flow Control macros 

I was very impressed with this and associated PEPs (340, 346, etc), but sorely disappointed when it was decided to remove the looping capabilities from the `with`{.backtick} statement. Having read Raymond Chen\'s linked rant about flow control macros, I felt I had to point out some of the differences between the flow control macros he was (quite rightly) complaining about, and those proposed here.

A block statement (`def, class, for, if, etc`) in Python (or most other languages) means \"start at the top of this block, run through it X times, let control flow off the end\". For if statements, X is 0 or 1, for defs and classes it\'s 0 (but the code is given a name for later) and for loops it\'s anything. Constructs that can \"jump\", such as break, continue, and return, break this reasoning, so it\'s important that you can see them clearly, and that they\'re not hidden behind macros (this is the gist of Raymond Chen\'s piece).

The proposed with statement does not break this reasoning, as it defines a new \"block type\". It doesn\'t cause control to jump around semi-randomly like hidden breaks, continues, and returns do. It is comparable to `#define until(x) while(!(x))`, in that it defines a sensible control structure that doesn\'t break structured programming, unlike the macros Raymond Chen dislikes (MUST_SUCCEED and its ilk).

And I really like `auto_retry`.

Am I too late?

Stephen Dolan

- By several months. However, you can still write something like `auto_retry` as a generator which returns an appropriate sequence of context managers:

<!-- -->

        for mgr in auto_retry(Exception, 3):
            with mgr:
                retry_if_this_fails()

- \-- *Alyssa Coghlan*
