# PeopleFilter

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

It\'s a formalization of a distributed social network. I get my best music recommendations from one or two people who have interests very similar to mine. I also get my best programming info from a different set of people, I learn about the coolest new linux programs from another set, etc. So, I suggest a more formalized and automated PeopleFilter, something like usenet, something like a blog, but with even more added. Throw in a few ants, some reinforcing structures, parts of a trust web, and hey presto, you might have something cooler than slashdot. *i think the same trust framework can be used for other things too: the [PeopleCheat](http://purl.net/wiki/python/PeopleCheat "EfnetPythonWiki") problem comes to mind* \-- [AllenShort](http://purl.net/wiki/python/AllenShort "EfnetPythonWiki")

The current idea is to run a server on a [TwistedPython](http://purl.net/wiki/python/TwistedPython "EfnetPythonWiki") instance, and to define different sets of other equal servers to get raw input from\... think SQL queries running against usenet servers, where the first layer of filters was to get into the server of your friend that you\'re now connected to\....so for one set of friends, your SQL query might look like: `SELECT MUSIC WHERE ((VOTES.PercentageLiked > 50) AND (RemoteServer.owner) voted 'liked')` which in english (since my sql is so bad) means \"where over 50% of the people who voted on this music selection liked it, and where the remote server\'s owner liked it. (I would probably also have \"where votes \> 50\" as a local-server wide query rule, but then maybe you\'d miss something)

but for another set of friends, might switch the MUSIC part to NEWS_ARTICLES, and add \"WHERE ARTICLE.[TroveCategory](./TroveCategory.html) = \'computer\'\"

the spirit of this idea is that I get my best recommendations from people I know and respect, and many of them are on irc, so I miss large sections of their lives where we have common interests, and would very much enjoy exchanging information, so there are probably better ways to structure that \... someone dug up a \'common interest finder\' kind of server, but it doesn\'t handle content. Someone else pointed to usenet, but it doesn\'t let me form my own people-based network, another pointed to email, and that\'s close, but it\'s not something where I can tune a sql query so I don\'t get spam, and it\'s also not a pull system.

The differences between email and PeopleFilter are things like, email is directed to a person like a letter, but PeopleFilter is directed to a subject or a rating. Spam would not get very far in this system, and as soon as it started to, no one would get content from the originating site.

I think you\'d need pieces like PGP signing of articles, and PGP signing of votes of \'like, don\'t like\' \'interesting, boring\' so that several statistics could emerge:

- how many people have read the article eg. I think I would have a default rule that says \"SELECT \* WHERE (COUNT(VOTES) \> 500000)\" because otherwise I would probably never know that Bush became the president.

- how interesting it is to your friends, and the whole web surrounding them

- where your friends and interests intersect

\--[ShaeErisson](ShaeErisson)

(A system in this spirit is being worked on called Yenta; it doesn\'t share content, merely interests. [http://foner.www.media.mit.edu/people/foner/yenta-brief.html](http://foner.www.media.mit.edu/people/foner/yenta-brief.html) -dash)

*I believe that Reptile is a system with similar aims. [http://reptile.openprivacy.org](http://reptile.openprivacy.org)*

    <e@ircnet> what's a peoplefilter?
    <dash> e: like a weblog without the web

further notes \[*restored by jh, after vandalizing?*\]:

I\'m still hung up on the signing idea. I\'d like for people to be able to sign something as \'nifty\' or as \'sucks\' so that I\'ll have more information to select on\...

the problem with this is signature synchronization. If I write a document and put it on my server, and three of my friends get it, and sign that article as interesting, how do they get those new signatures?

the obvious solution is to have the signatures for an article kept on the server the article originated from\... but that\'s not peer to peer anymore.. that means servers need to be online all the time.

On the other hand, if you friend gets something that sucks, you\'ll never see it\... they\'ll delete it, right? or maybe they\'ll never select it in the first place? I\'m not sure.

okay, much thinking later, I think signatures should backwash upon article synchronization. I also think that signatures should qualify as articles, and be searchable, what else could be significant to the system and yet searchable?

*I think that signatures should stay attached to messages, and not \"backwash\"; all you have to do is merge the votes/signatures attached to disparate copies of the same article. that way, localised information isn\'t lost, but there\'s no need to complicate with chaining back upwards either\.... -[AllenShort](./AllenShort.html)*

I happen to own the domain peoplefilter.com for another project which is \"on the shelf\" so if you are interested in it, let me know. - Kevin Harrison

## Features 

- article synchronization upon request - sql like article searching
- signing of an article - author, and good/bad per reader
- struct style definition of a document
- struct definitions are documents as well (the old Smalltalk Metaclass story, or think Netscape saying \"would you like to download this plugin\")
- signatures are docs

## Properties 

- document expiration (for example, an open invitation to IPC12 will just expire at some point)

*You guys should look at the old Firefly and Ringo projects, which did more sophisticated correlation than is described here, and generally gave excellent recomendations. They used curve fitting to estimate how a user would rate a particular item based on the ratings of other users who rated other items similarly to the user. I.e., if User A rates John Coltrane an 8 and Miles Davis an 8 and Charlie Parker a 9, and User B rates John Coltrane a 7 and Miles Davis a 9, then Firefly or Ringo would figure that User B would also give Charlie Parker a high rating.\'. The Firefly system was purhcased by Microsoft and the technology has been sunk into Launchcast, which actually delivers music in a Internet Radio format.* \-- [RobertChurch](RobertChurch)

Also relevant: [CollaborativeFiltering](http://www.usemod.com/cgi-bin/mb.pl?CollaborativeFiltering "MeatBall"), [ContentFiltering](http://www.usemod.com/cgi-bin/mb.pl?ContentFiltering "MeatBall"), [VotingMustDie](http://www.usemod.com/cgi-bin/mb.pl?VotingMustDie "MeatBall"), [ViewPoint](http://www.usemod.com/cgi-bin/mb.pl?ViewPoint "MeatBall"), [TransactionBasedCommunity](http://www.usemod.com/cgi-bin/mb.pl?TransactionBasedCommunity "MeatBall")
