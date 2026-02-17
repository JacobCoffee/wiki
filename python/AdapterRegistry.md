# AdapterRegistry

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

An **adapter registry** is a piece of software that knows how to adapt one interface to another interface.

(In this explanation, \"**interface**\" is some promise about what an object has and what it can do. Without getting into particulars, we probably mean what attributes and methods the object supports.)

## Why Do We Care? 

Let\'s say you have the following classes:

- `Directory`

- `RssFeed`

- `MoinMoinWiki`

- `MoinMoinWikiPage`

- `TextFile`

Now, you want to say things like:

`Directory("~/foo/").receive(MoinMoinWiki("http://...").page("AdapterRegistry"))`

We\'d like to teach the `Directory` how to receive a `TextFile`, and then how to adapt a `MoinMoinWikiPage` into a `TextFile`.

Or, we can create a class called `TextFilesCollection`, and the `Directory ` could receive them. Then the `MoinMoinWiki` can say, \"I can be interpreted by way of the `TextFilesCollection` interface.\"

Then you can write:

`Directory("~/foo/").receive(MoinMoinWiki("http://..."))`

\...and you get a backup of the entire wiki.

## More Examples 

If you have a Eggs, and you need to plug it into some Spam, then you can have them automatically figure each other out. Or a third party mechanism can help the two figure each other out.

The example is given in [Using the Adapter Registry](http://webforce.at/Interface/human.txt/view) of having a file object (that supports IFile) that indirectly supports ISize.

That is:

- Suppose that there were IFile.
- And suppose further, for some reason, IFile does not have a \"size()\" function, telling the size in bytes.
- But suppose then someone made an interface \"ISize,\" that means \"things that give their size in bytes.\"
- If you had all this, then somebody can write an adapter that calculates out the size in bytes for anything meeting IFile.
- (That is, there\'s some way to infer size information by performing calculations over an IFile implementation.)
- Then, anywhere that an ISize can be used, you can also use an IFile.

Whenever I\'m programming, and I find a situation where this would be useful, I\'ll put a note here as a use case. I feel like it comes up a lot.

## Culture of Interfaces 

(I\'m about to say a bunch of things. I can\'t substantiate them with links right at this moment, though. If you know the links, though, please provide them, so it doesn\'t look like I\'m just making this stuff up. Of course, I may just well be flat wrong, or have seriously misunderstood. Caveat Emptor.)

People have talked about how in the Java camp, people build on standards. There has been talk also that perhaps this is because of interface support in Java. With well-defined interfaces, the thinking goes, people focus on the ability to provide multiple implementations specialized for different circumstances, different uses. And also, it\'s easy to know if you meet an interface or you do not. And there seems to be something attractive about having a well defined specification. (As opposed to, say, [SubclassingBuiltInTypes](SubclassingBuiltInTypes) .)

People disagree about whether it\'s a good or not. But the point is, it\'s plausible to believe that if we have interface support and an AdapterRegistry built into Python, that we may experience a change in Python culture. There is a tension here.

You may find something interesting in the bottom of the page: \"[PythonThreeDotOh](PythonThreeDotOh).\" You should perhaps also read: \"[PythonFederalEnterpriseArchitecture](PythonFederalEnterpriseArchitecture).\"

## Zope Adapter Registry 

Zope includes the concepts of interfaces and adapters. Zope is referenced a lot in talk about an adapter registry; Conversation about adapter registries in Python seems inseperable from the Zope adapter registry.

(There\'s also something called [PyProtocols](./PyProtocols.html) that I don\'t know anything about, and there are also interfaces and adapters (I believe) in [PEAK](./PEAK.html), which is very complicated.)

- [Using the Adapter Registry](http://webforce.at/Interface/human.txt/view)

If you study the Zope adapter registry, \[[http://www.emacswiki.org/cw/WikiAsYouLearn](http://www.emacswiki.org/cw/WikiAsYouLearn) you may want to keep public notes, in which case, you should know about the Zope Interfaces wiki:

- [Zope Interfaces wiki](http://www.zope.org/Wikis/Interfaces/FrontPage)

# Discussion 

I don\'t mean to be inflammatory; This is just something that interests me, and that I\'m trying to understand. I don\'t really have anyone to talk with about these things in [my local community.](http://www.seapig.org/)

If I\'ve seriously missed the mark, please correct me; And, if you know something, and can help us understand these things, please explain, preferably in some form of plain language.

re: use cases, it strikes me that it\'s perhaps not just the uses in code, but also in the how-programmers-work-together space. Something that is useful in code, say, makes something take up fewer lines, fewer characters. But something that acknowledges how programmers work together, has something to do with our habits and psychology and subjective experiences. Use cases may be speculative, because they might say things like, \"Well, if you have interfaces, then people will use them, because they like to have a clean spec that they can know clearly whether they are meeting it or not. And if you have interfaces, then you\'ll have lots of little components that you can just string together. And if you have adapters, that stringing along is easier still- you don\'t have to write custom functions for adaption for every thing, every project.\"

We may not be able to find striking use cases, (\"look at how fewer lines this takes!\"), because the utility might come from the pragmatics of our use of our language.

\-- [LionKimbro](LionKimbro) 2005-04-01 20:54:27
