# WebwareSprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Sprinters: 

Add your name to this list if you\'re considering sprinting on Webware. Put \"definitely\", \"probably\", or \"maybe\" in parens next to your name so we\'ll have a rough idea of how many bibs to get for the lobster dinner.

That\'s a joke. There\'s no lobster dinner. Unless we will it to be so.

- Tripp Lilley (definitely)
- Mike Orr (definitely)
- Ian Bicking (definitely)

## Sprint Topic Discussion: 

There\'s no consensus yet on what, precisely, we\'ll be working on, but I know I\'ve a personal bias towards [MiddleKit](MiddleKit) enhancements, DAVKit enhancements, and bringing [UserKit](UserKit) out of its alpha-ness.

Feel free to contact me (Tripp Lilley, [tripp+pycon-webware-sprint@perspex.com](mailto:tripp+pycon-webware-sprint@perspex.com)) directly about the sprint topics, or, better yet, post to webware-devel.

Note that, by design, sprints are \"not intended for newbies\". That doesn\'t mean newbies aren\'t welcome, it just means that our focus is going to be on enhancing the code, not teaching the code.

Now, with that said, I\'m rusty on the code ![:)](/wiki/europython/img/smile.png%20":)") I expect that I\'ll personally spend at least some portion of my sprint time fleshing out and diagramming Webware\'s architecture, bringing up to date some of the earlier work by Chuck, Ian, and others.

I expect this exercise would be helpful to those who haven\'t yet peered deeply inside Webware\'s source, but would like to. So, uh, newbies *are*, in fact, welcome to this particular sprint ![:)](/wiki/europython/img/smile.png%20":)")

\-- [TrippLilley](./TrippLilley.html)

------------------------------------------------------------------------

I\'m don\'t really use [MiddleKit](MiddleKit) (hence [SqlObject](SqlObject)), so that\'s not really of interest to me.

DAVKit would be interesting, but I feel like a lot of its development should focus around testing and maturing (and also handling error conditions). I\'m not sure if that\'s good sprint material.

[UserKit](UserKit) certainly is good sprint material. Well\... I personally would want to rethink the whole thing from the ground up \-- I find the design a little baroque, considering it has few features and yet is still hard to understand. It uses inheritance where mere composition is called for, among other architectural complexities. But there\'s a bunch of interesting and useful stuff to be done with user management.

There\'s also CMS-like issues. All websites have static content as well as dynamic \-- Webware deals well with the dynamic stuff, but it could stand to do better with the static stuff. This is Zope territory, obviously we\'d do it more simply. [UserKit](UserKit) would be a great way to start with this. The two could be worked on at the same time.

Another related item to [UserKit](UserKit) and CMS is a better security structure. Right now it\'s do-it-yourself just like user management.

Lastly, we could actually develop an application. I think it would be really nice to have a Webware application of general appeal, both as an example, and just maybe as a killer app (shoot high!) \-- writing an application can be very satisfying. And we could do a little infrastructure work where the application calls for it \-- I can imagine a True Webware App being a way to codify some of the idioms that are currently just idioms, but deserve to be more. Things like application layout, class layout, application distribution, as well as all of the aforementioned issues (user management, security, CMS).

\-- [IanBicking](IanBicking)

------------------------------------------------------------------------

It would be wonderful to have some work on [MiddleKit](MiddleKit) and [UserKit](UserKit) during the spring. Patrick Giagnocavo of [http://www.zill.net/](http://www.zill.net/) has been very supportive of webware hosting. His service is Postgres-based, so it would be great to have the various Postgres patches at source-forge rolled into the mainstream releases.

A second feature for Middlekit would be the ability to store [MiddleKit](MiddleKit) objects in session, and not have things run amok if the session is flushed to disk. Jason Hildebrand has some ideas on making [MiddleKit](MiddleKit) objects sessionable at [http://webware.colorstudy.net/twiki/bin/view/Webware/MiddleKitAndWebKit](http://webware.colorstudy.net/twiki/bin/view/Webware/MiddleKitAndWebKit).

I\'d also second Ian\'s ideas on [UserKit](UserKit).

There\'s only one source-code repository on [http://www.freshmeat.net](http://www.freshmeat.net) at this point (Scriptorium). An application that would facilitate code-reuse and code-harvesting might be a great sample application - not trivial, yet not overly complicated.

\-- [KevinDahlhausen](KevinDahlhausen)

------------------------------------------------------------------------

I\'d be most interested in outlining/documenting the code, or in designing a CMS spec, but I\'ll do anything. I haven\'t looked at the Webware code base closely, since I\'ve been using [WebwareExperimental](./WebwareExperimental.html) and my development time has been focused on Cheetah.

\-- [MikeOrr](./MikeOrr.html)

------------------------------------------------------------------------

[CategoryPyCon](CategoryPyCon)
