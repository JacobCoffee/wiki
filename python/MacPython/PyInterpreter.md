# MacPython/PyInterpreter

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[PyInterpreter](PyInterpreter) is an example of how you can do rather advanced editing in pure Python using [/PyObjC](./MacPython(2f)PyInterpreter(2f)PyObjC.html). It uses a [NSTextView](./NSTextView.html) delegate to provide stdin/stdout coloring, command history, a (incredibly scary implementation of a) faked stdin, text completion (only in OS X 10.3 and later). Note that completion in OS X is bound to the F5 key by default, but I\'ve also bound it to option-tab for convenience. It should be relatively easy to include in other [PyObjC](./PyObjC.html) projects, and I\'m hoping it will be distributed with a future version as an example.

[PyInterpreter](PyInterpreter) will only work in [MacPython](MacPython) 2.3 or later with [/PyObjC](./MacPython(2f)PyInterpreter(2f)PyObjC.html) 1.0 or later, and will not be ported or tested on anything older than that.

# Status 

[PyInterpreter](PyInterpreter) 0.3 ([download](http://undefined.org/python/PyInterpreter-0.3.tgz)) was released on 10/28/2003. The latest version is in [/PyObjC](./MacPython(2f)PyInterpreter(2f)PyObjC.html) svn.

# Screenshots 

![](http://undefined.org/python/PyInterpreter_0.png "http://undefined.org/python/PyInterpreter_0.png")

# Homepage 

Just here, for now

# Credits 

[BobIppolito](BobIppolito) - Developer\
[JustVanRossum](JustVanRossum) - Insight, ideas, testing

# Suggestions 

*From [JustVanRossum](JustVanRossum):*

\[This comment is about [/PyInterpreter](./MacPython(2f)PyInterpreter(2f)PyInterpreter.html) 0.2; stdin reading has been reworked for 0.3\]\
stdin.readline() dialog: I think this should ideally be a sheet, even though the rest of the app will still block (Hm, I suppose you could run a nested event loop until readline returns, ick\...). [/DrawBot](./MacPython(2f)PyInterpreter(2f)DrawBot.html) contains AskString.{py\|nib} which gives you a convenient way to use just such a sheet, but I\'m not sure it useful for [/PyInterpreter](./MacPython(2f)PyInterpreter(2f)PyInterpreter.html) since it *doesn\'t* block. Thinking out loud a bit more: once a nested event loop is in place, it obviously shouldn\'t be a dialog/sheet in the first place, and stdin.readlione() might as well behave like it does in a terminal. (And yes, co-routines would save our butts here\...)

(Eventually I\'d like to have much/all of EasyDialogs.py in Cocoa-savvy form. Project anyone?)

*Reply from [BobIppolito](BobIppolito):*

I implemented the nested event loop method. It works, but it\'s \*scary\*. Also, how much of EasyDialogs is actually useful in [/PyObjC](./MacPython(2f)PyInterpreter(2f)PyObjC.html), given how easy it is to do these things? If you make a list of useful targets I may start implementing some of them.

*From [JustVanRossum](JustVanRossum):*

[CocoaEasyDialogs](./CocoaEasyDialogs.html): it\'s a major pain to implement sheets, mostly due to that stupid callback signature. A simple Python callback is nicer (that\'s what my AskString.py does). EasyDialogs.Message() is nice and simple; would like to have as a sheet. AskPassword() has its uses. AskYesNoCancel is very convenient. ProgressBar is doubtful, since it\'s usually better to integrate it into the rest of the UI. But the killers are AskFileForOpen() and AskFileForSave: I find doing these in raw Cocoa pretty disgusting (again, that sheet callback, it\'s messy even with endSheetHelper). The question is, can we make thin wrappers that are still flexible enough for non-standard usage?

*From mwh:*

Two features that spring to mind (haven\'t got the iBook here so can\'t test): auto-indent and syntax coloring. Otherwise, cool!

*Reply from [BobIppolito](BobIppolito):*

Both are coming soon!

*From [DinuGherman](DinuGherman):*

You might want to mention explicitly that it needs Python 2.3, since it makes use of the yield statement\...

*Reply from [BobIppolito](BobIppolito):*

Changed above.

*From bbum:*

Should this work with the Panther build of Python and [/PyObjC](./MacPython(2f)PyInterpreter(2f)PyObjC.html) as built from the repository? It isn\'t for me \-- `TypeError: class /PyInterpreter does not correctly implement protocol NSTextViewDelegate: the signature for method textView:completions:forPartialWordRange:indexOfSelectedItem: is @@:@@{_NSRange=II}N^i instead of @@:@@{_NSRange=II}^i`

*Reply from [BobIppolito](BobIppolito):*

The signature in [/PyInterpreter](./MacPython(2f)PyInterpreter(2f)PyInterpreter.html) is correct. [/PyObjC](./MacPython(2f)PyInterpreter(2f)PyObjC.html)\'s signature is fixed in \[svn\].

*From mwh:*

Oh, one more (still no iBook, though :-): is it even sensible to ask about palettizing this so you could set up a [/PyInterpreter](./MacPython(2f)PyInterpreter(2f)PyInterpreter.html) in IB?

*Reply from [BobIppolito](BobIppolito):*

Maybe? I\'ve never tried making pallettes.

*mwh:*

I have, but failed miserably ![:-)](/wiki/europython/img/smile.png ":-)") Ronald managed to get it to work though, so perhaps I\'ll try some time.

*[MichaelHudson](MichaelHudson) again:*

Well, I\'ve now downloaded it and played around a bit. It\'s cool, but I hope I don\'t give offense by saying it\'s not as good as I hoped it might be. One thing I was disappointed about is the lack of support for multiline editing (have you used IDLE? that gets this right). I have the feeling that making a *really good* shell will involve some scary hacking with keybindings and the like. Well, these no substitute for effort, so hopefully I\'ll find some time to get stuck in soon!

*Reply from [BobIppolito](BobIppolito):*

Patches accepted. [/PyObjC](./MacPython(2f)PyInterpreter(2f)PyObjC.html) \[svn\] has the latest. And no, I haven\'t used IDLE (or any other Python IDE) for a meaningful length of time. I\'m more concerned with having a nice IDE than having the best interactive interpreter on the planet, but I don\'t really have enough interest/time for either right now.

*[MichaelHudson](MichaelHudson):*

Somehow I hadn\'t noticed it getting into [/PyObjC](./MacPython(2f)PyInterpreter(2f)PyObjC.html). I **am** concerned about having \"the best interactive interpreter on the planet\", and will try to come up with some good patches soon-ish.

*Reply from [BobIppolito](BobIppolito):*

It\'s not in a release version of [/PyObjC](./MacPython(2f)PyInterpreter(2f)PyObjC.html) \-- it\'s very new.. I wrote it not too long ago (not even two weeks at this point), haven\'t put a whole lot of time into it, as you can probably tell by the brevity of the source. The best interpreter on the planet would make everyone\'s day for sure, perhaps when you start putting together patches it\'ll inspire me, and probably others, like Just, to work on it some more!
