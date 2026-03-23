# lwickjr

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[lwickjr](lwickjr) 2011-09-15 18:23:10: I\`ve just reviewed the site.py bug mentioned below, and it still exists in Python 3.1.2. Will someone please fix it?

[lwickjr](lwickjr) 2011-09-15 18:20:53: Trivial edit to get the comment into the log. ![:)](/wiki/europython/img/smile.png%20":)")

Quote: \"Editor: [PaulBoddie](../people/PaulBoddie) Comment: Suspicious edit resembling spam. Apologies if casino stuff is now actually lwickjr\'s focus.\" Nope; you\`re right. Thanks!

[lwickjr](lwickjr) 2010-09-06 19:25:09: Gah! I\`ve lost my edits TWICE now, once to not being logged in \[I haven\'t been around so long that I forgot I had never logged in from this particular machine; it\'s newish\], and once to failing to answer the question that I presume protects the site from unauthorized editing.

Trying a \*third\* time\... Ok, that worked; re-entering the actual information\...

Hmm, I note that the [DateTime](./DateTime.html) tags below failed to stamp the time when I last edited this page YEARS ago. Odd. I guess I didn\'t know how to use them then. ::shrug::

Having recently installed Python 2.7.0, I was browsing through the installation, specifically the `site`{.backtick} module \[there wasn\'t a `usercustomize`{.backtick} module last time I checked, and the new mechinism was interesting; I had been keeping my personal code in the `site-packages`{.backtick} directory on my personal Windoze machine\] when I noticed an error in the definition of the `addpackage`{.backtick} function.

To whit, if `addpackage`{.backtick} is ever called with `None`{.backtick} as the value of `known_paths`{.backtick} \[which it never is\], `addpackage`{.backtick} makes a totaly useless call to `_init_pathinfo`{.backtick} without saving the results, which I infer should be stored into `known_paths`{.backtick} \[as is done in `addsitedir`{.backtick}\], as `addpackage`{.backtick} will then go on to throw a `KeyError`{.backtick} exception by attempting to use the `None`{.backtick} value still in `known_paths`{.backtick} as a dictionary-type container. The indicated fix is to copy the `known_paths = _init_pathinfo()`{.backtick} line in `addsitedir`{.backtick} over the `_init_pathinfo()`{.backtick} line in `addpackage`{.backtick}. I also recommend that the `known_paths`{.backtick} argument be made to default to `None`{.backtick} as it does in `addsitedir`{.backtick}, and appears \[from the body of the fuction\] to have been intended.

As this bug was discovered through visual inspection and I am not registered at any of the usual Python development sites, would someone please verify this bug and bring it to the attention of the appropriate individuals and/or groups? Thanks!

Whew! Third time\`s the charm, I hope! Also, each time brought forth a somewhat-improved version of the above text \[\'least I think so ![;)](/wiki/europython/img/smile4.png%20";)") \].

------------------------------------------------------------------------

Attention, please: I am interested in the possibility of de-linting some of the documentation. How do I go about signing up?

[FredDrake](../people/FredDrake) sez: See the [Documentation Development](http://www.python.org/dev/doc/) page.

[lwickjr](lwickjr) 2026-02-14 16:15:21: Done, which I noted on your page some time ago. ![:)](/wiki/europython/img/smile.png%20":)") \[I find myself wondering if anyone found the delinted pages.\]

[lwickjr](lwickjr) 2026-02-14 16:15:21: [LionKimbro](../people/LionKimbro): \"Parnassus\". ![;)](/wiki/europython/img/smile4.png%20";)")

------------------------------------------------------------------------

Welcome to my page.

------------------------------------------------------------------------

After reading [RealNamesPlease](http://c2.com/cgi/wiki?RealNamesPlease "Wiki"), [RealNamesPleaseDiscussion](http://c2.com/cgi/wiki?RealNamesPleaseDiscussion "Wiki"), and [OneNamePlease](http://c2.com/cgi/wiki?OneNamePlease "Wiki"),

I respectfully decline to change my login ID.

This is the ID I use exclusively online, it is derived from my \"RL\" name, and it is the ID under which I receive my e-mail.

In accordance with [OneNamePlease](http://c2.com/cgi/wiki?OneNamePlease "Wiki") and [RealNamesPleaseDiscussion](http://c2.com/cgi/wiki?RealNamesPleaseDiscussion "Wiki"), I conclude that while \"lwickjr\" is not \"exactly\" in accordance with [RealNamesPlease](http://c2.com/cgi/wiki?RealNamesPlease "Wiki"), it IS \"close enough\".

Please, no flames; no offense intended.

------------------------------------------------------------------------

If anyone with GOOD American-English spelling skills would care to proofread this page and correct any spelling errors that I can\'t find, feel free. I\'ve been adding known-correctly-spelled words to the online spelling checker, but I\'m a tad unsure of a few of my spellings.

------------------------------------------------------------------------

I have a few questions that I\'ve been unable to find answer for.

All the documentation I\'ve seen seems to assume that someone wanting to publish Python modules has \-- and knows how to use \-- a 24/7 file server available to use.

This is not always the case.

Further, I have found the documentation on distributing Python modules to be strong on the mechanics of how to PACKAGE modules \[somewhat over-kill, I think, for simple drop-in single-file modules\], and nearly nonexistent on how to PUBLISH them.

Could someone [please] write a page on [PublishingPythonModules](PublishingPythonModules) that is understandable by someone with significant \*computer\* experience but minimal \*Internet\* experience?

## Links 

[PublishingPythonModules](PublishingPythonModules) [SkipMontanaro](../people/SkipMontanaro) [Some of my more publishable modules](lwickjr/Modules) [Vaults of Parnassus](http://py.vaults.ca/apyllo.py)

------------------------------------------------------------------------

Hi lwick, before I answer some of your questions, I\'d like you to consider [RealNamesPlease](http://c2.com/cgi/wiki?RealNamesPlease "Wiki"). It is one of our [WikiGuidelines](../people/WikiGuidelines), and it has worked well for us so far.

I\'m not completely sure what you mean by publishing Python modules. If you need a space to upload your Python modules, you might want to consider [StarshipPython](../people/StarshipPython). It used to be free for PSA members, but the PSA has ceased to exist, so I guess a small donation to the [PythonSoftwareFoundation](../psf/PythonSoftwareFoundation) will do now. Would that solve your problem?

\-- [JohannesGijsbers](../people/JohannesGijsbers)

[lwickjr](lwickjr): Possibly. I\'ve written a few useful-to-me modules that I think others might also find useful. I\'d like to share them, but I am NOT on-line 24/7, and would like someone to host them for downloading. As for [WikiName](WikiName)s, would LWickJr do? If so, how do I change it?

With a real name I meant the one in your passport, not capitalizing your nick into a [WikiName](WikiName). Changing it is easy: just create the new page and cut all content from this page into it. Then delete this page and log in using your new name. \-- [JohannesGijsbers](../people/JohannesGijsbers)

[lwickjr](lwickjr): Don\'t have a passport. As for my \"nick\", the L is my first initial, the Wick is my family name, and the Jr is because I\'ve got the same name as my father. Isn\'t this \"real\" enough?

- /\-\-- later the same day \-\--
  - Having read [RealNamesPlease](http://c2.com/cgi/wiki?RealNamesPlease "Wiki"), [RealNamesPleaseDiscussion](http://c2.com/cgi/wiki?RealNamesPleaseDiscussion "Wiki"), and [OneNamePlease](http://c2.com/cgi/wiki?OneNamePlease "Wiki"), I choose to continue using [lwickjr](lwickjr) as my login name. It is a persistent on-line identity. It is directly related to my given name. It is the \*only\* ID I use online. I doubt that anyone here would like to call me \"the Hungry Hacker\", with which I sign all my e-mail. Having stated my position, I simply shall ignore the issue and contribute as best I can. After all, isn\'t that why we\'re here? No offense taken; none intended.

  \\\-\--

------------------------------------------------------------------------

BTW, what do you think of the modules I describe [here](lwickjr/Modules)?

As for publishing modules, it seems to me that we in the Python community are not yet [as organized as the Ruby community.](http://rubyforge.org/softwaremap/trove_list.php)

For the most part, people set up their own website, maybe something on [SourceForge](../people/SourceForge), get a listing on [PyPi](./PyPi.html) or the vaults (of what-I-cant-spell,) and mention it on the python-announce usenet forum.

It would be a good subject for a new wiki page. I think there\'s already one that\'s started somewhere, that it would be worthwhile to revisit.

\-- [LionKimbro](../people/LionKimbro) 2005-04-01 21:16:29

[lwickjr](lwickjr): Um, sorry about that. The descriptions are heavy on \*what\* the modules do, but totally void of either of how they work or why one would want to use them.

As for that WIKIPage you mention, [How to publish Python modules](PublishingPythonModules), I created it in hopes that someone would populate it with useful information. I\'m thinking of doing just that. Ok, people, just how big is \"small enough\"?

Sombody else (Who?): You\`re right, it \*is\* worth revisiting, in case someone \_has\_ done just that. Someone suggested that small modules can be posted here.

[lwickjr](lwickjr): Yes; I\'ve seen that.

[lwickjr](lwickjr): Please note: \"[How to publish Python modules](PublishingPythonModules)\" has been superceeded by [PublishingPythonModules](PublishingPythonModules).

I\'m uploading some of my more publishable modules as attachments to [this page](lwickjr/Modules). \"Alias\" is in [lwickjr/Modules:Alias.py](attachments/lwickjr(2f)Modules/Alias.py "lwickjr/Modules:Alias.py"), \"Edit\" is in [lwickjr/Modules:Edit.py](attachments/lwickjr(2f)Modules/Edit.py "lwickjr/Modules:Edit.py"), and \"UT\" is in [lwickjr/Modules:UT.py]( "Upload new attachment "UT.py"") - I \*hope\* they\'re not to big.

Does Edit interest you? Don\'t forget: it \*does\* require that the default subprocess be turned off, as it REQUIRES interaction between the user dataspace and the I.D.L.E. dataspace, and I don\`t \[currently\] know how to use the IPC \[Inter-Process Communication\] that I.D.L.E. uses for the purpose. Alias has the same requirement, and for the same reason.

------------------------------------------------------------------------

[CategoryHomepage](CategoryHomepage)
