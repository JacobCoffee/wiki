# Asking for Help/I'm taking an unhandled threading exception that I've been unable to locate

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: I\'m taking an unhandled threading exception that I\'ve been unable to locate 

I keep getting this unhandled exception, but I believe I have placed try except statements in all my threads. Any thoughts?

    Unhandled exception in thread started by <bound method Thread.__bootstrap of <Thread(Thread-169204, stopped 1004)>>
    Traceback (most recent call last):
      File "C:\Python27\lib\threading.py", line 503, in __bootstrap
        self.__bootstrap_inner()
      File "C:\Python27\lib\threading.py", line 518, in __bootstrap_inner
        del _limbo[self]
    KeyError: <Thread(Thread-169204, stopped 1004)>

A philosophical discussion appears to be appropriate here. How in fact does one get one\'s self out of \_limbo? The answer my friend is blowing in the wind. The answer is \...

Posted this question about a week ago and noone has answered. Not sure if anyone is paying attention to the Asking for Help portion of the wiki. Just to make sure that I know exactly how long its been on the wiki today\'s date is 3/22/2011. The wiki indicated that my question was sent to [MatsWichmann](MatsWichmann), [SkipMontanaro](SkipMontanaro), [FredDrake](FredDrake). Do these guys really exist?

::: note
Yes, I really exist. So do Fred and Mats. (I have even met Fred before.) I subscribe to all pages of the wiki mostly to revert spam introduced into it, not to answer questions. Personally, of all the uses one could think of for a wiki, asking and answering long-form help questions seems to me like just about the worst use possible. I ignore essentially all questions posted here unless it looks like someone is spamming this subtree of the wiki. \-- [SkipMontanaro](SkipMontanaro)
:::

Those guys get mails about updates to this page, yes. I did have a look at the `threading`{.backtick} module, but I have to admit that I am not really familiar with its architecture. There\'s a comment in the `__bootstrap`{.backtick} method which claims that exceptions thrown by \"daemon threads\" are meant to be ignored, but it looks like you\'re experiencing a problem with the actual administration of threads done by the module itself - that is, you aren\'t supposed to be concerned by the `_limbo`{.backtick} dictionary - and maybe there\'s a bug involved. I can only find [7264](http://bugs.python.org/issue7264 "Issue") which mentions `_limbo`{.backtick}, however. \-- [PaulBoddie](PaulBoddie) 2011-03-22 22:55:34

Skip and Paul,

Thanks for responding. Is there a better place to post my question? Where might that be?

Check out the links at the top of the [Asking for Help](./Asking(20)for(20)Help.html) page. I think it\'s helpful to have some kind of archive of questions and answers here, although I didn\'t start this activity, but unfortunately there aren\'t many people reading the questions, I\'m afraid. I would try the regular Python mailing list, maybe filing a bug if this is in some program where you\'re doing the right thing. You may have to share a bit of your code to have people help you, however. People really like to have the essence of a problem demonstrated in as short a program as possible. Feel free to use this page to communicate your problem if it\'s convenient, though, if you need to post some code somewhere and you don\'t think your e-mail program or newsreader is keeping it readable, for example. \-- [PaulBoddie](PaulBoddie) 2011-03-24 22:17:33

This patch seems to work for me. I will also post to the bugs list.

    --- threading27.py      Mon Apr 05 20:23:34 2010
    +++ threadingmod27.py   Tue Mar 29 10:16:59 2011
    @@ -439,6 +439,7 @@
             self.__stopped = False
             self.__block = Condition(Lock())
             self.__initialized = True
    +        self.isSelfInLimbo = True
             # sys.stderr is not stored in the class like
             # sys.exc_info since it can be changed between instances
             self.__stderr = _sys.stderr
    @@ -484,7 +485,9 @@
             finally:
                 # Avoid a refcycle if the thread is running a function with
                 # an argument that has a member that points to the thread.
    -            del self.__target, self.__args, self.__kwargs
    +            if not self.isSelfInLimbo:
    +                self.isSelfInLimbo = True
    +                del self.__target, self.__args, self.__kwargs
     
         def __bootstrap(self):
             # Wrapper around the real bootstrap code that ignores
    @@ -515,7 +518,10 @@
                 self.__started.set()
                 with _active_limbo_lock:
                     _active[self.__ident] = self
    -                del _limbo[self]
    +                if self in _limbo:
    +                    del _limbo[self]
    +                else:
    +                    self.isSelfInLimbo = False
                 if __debug__:
                     self._note("%s.__bootstrap(): thread started", self)

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
