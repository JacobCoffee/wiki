# PyConBrianWarner

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

I will be giving two talks at [PyCon](PyCon) this year.

# BuildBot: build/test automation 

## Abstract 

The BuildBot is a system to automate the compile/test cycle required by most software projects to validate code changes. By automatically rebuilding and testing the tree each time something has changed, build problems are pinpointed quickly, before other developers are inconvenienced by the failure. The guilty developer can be identified and harassed without human intervention. By running the builds on a variety of platforms, developers who do not have the facilities to test their changes everywhere before checkin will at least know shortly afterwards whether they have broken the build or not. Warning counts, lint checks, image size, compile time, and other build parameters can be tracked over time, are more visible, and are therefore easier to improve.

The overall goal is to reduce tree breakage and provide a platform to run tests or code-quality checks that are too annoying or pedantic for any human to waste their time with. Developers get immediate (and potentially public) feedback about their changes, encouraging them to be more careful about testing before checkin.

Features:

- run builds on a variety of slave platforms
- arbitrary build process: handles projects using C, Python, whatever
- minimal host requirements: python and Twisted
- slaves can be behind a firewall if they can still do checkout
- status delivery through web page, email, IRC, other protocols
- track builds in progress, provide estimated completion time
- flexible configuration by subclassing generic build process classes
- debug tools to force a new build, submit fake Changes, query slave status
- released under the GPL

## Presentation Notes 

I will be walking through the basic features of the BuildBot, demonstrating a sample installation which runs the Twisted unit test suite on all checkins. By that time, the code should be available on Sourceforge along with more documentation.

This presentation is currently [scheduled](http://www.python.org/pycon/pycon-schedule.html) for 10am on friday March 28th.

The full paper is available at [http://www.lothar.com/tech/papers/PyCon-2003/buildbot-pycon/buildbot.html](http://www.lothar.com/tech/papers/PyCon-2003/buildbot-pycon/buildbot.html) .

# Perspective Broker: RPC in Twisted 

## Abstract 

One of the core services provided by the [Twisted](http://www.twistedmatrix.com) networking framework is \"Perspective Broker\", which provides a clean, secure, easy-to-use Remote Procedure Call (RPC) mechanism. This paper explains the novel features of PB, describes the security model and its implementation, and provides brief examples of usage.

PB is used as a foundation for many other services in Twisted, as well as projects built upon the Twisted framework. twisted.web servers can delegate responsibility for different portions of URL-space by distributing PB messages to the object that owns that subspace. twisted.im is an instant-messaging protocol that runs over PB. Applications like CVSToys use PB to distribute notices every time a CVS commit has occurred. Using PB allows these projects to focus on the interesting parts.

## Presentation Notes 

I\'ll be walking through the main features of PB, running short sample programs to demonstrate how it all works. The presentation is currently scheduled for 3:15pm on wednesday March 26th.

I\'d recommend attending the \"Deferred Execution in Twisted\" talk scheduled for wednesday morning: PB relies heavily on Deferreds and understanding them will make PB easier to pick up.

I\'d also suggest the Twisted Tutorial which should happen just before this talk.

The full paper is available at [http://www.lothar.com/tech/papers/PyCon-2003/pb-pycon/pb.html](http://www.lothar.com/tech/papers/PyCon-2003/pb-pycon/pb.html) .

# Questions? Suggestions? 

Please add any questions, suggestions, or things you\'d like me to cover in the presentation here.

- Does the BuildBot have a home page yet?

- A: (22Mar2003): Yes. [http://buildbot.sourceforge.net/](http://buildbot.sourceforge.net/) is the URL. It is still pretty sparse, but there is a copy of the paper and some installation hints. Join the mailing list to be notified when a release is ready.
