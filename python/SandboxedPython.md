# SandboxedPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Sandboxed Python 

See also: [How can I run an untrusted Python script safely (i.e. Sandbox)](./Asking(20)for(20)Help(2f)How(20)can(20)I(20)run(20)an(20)untrusted(20)Python(20)script(20)safely(2028)i(2e)e(2e20)Sandbox(29).html) (from the [Asking for Help](./Asking(20)for(20)Help.html) page), [Security](Security).

Is there such a thing as \"Sandboxed Python\"? Something where you can run a Python that is limited in what it can do.

You could do all *sorts* of cool things with a sandboxed Python:

- You could turn a wiki into an RAD development platform. You just draw up your interface with [WikiSyntax](http://c2.com/cgi/wiki?WikiSyntax "Wiki"), write up a little bit of Python code, and bam- instant application. ![:)](/wiki/europython/img/smile.png ":)")

  - This is somewhat similar to [TiddlyWiki](http://www.tiddlywiki.com/) - a [JavaScript](./JavaScript.html)-based Wiki which behaves like a Web-based sandboxed application - although that approach utilises the [JavaScript](./JavaScript.html) sandbox functionality in the Web browser, rather than accessing a sandboxed server-side application.

- You could make a distributed code system, where not just resources, but functionality as well, can distribute safely over multiple computers.

## Technical Mechanisms 

A \"Sandboxed Python\" would let you permit or forbid modules, limit execution slices, permit or deny network traffic, constrain filesystem access to a particular directory (floated as \"/\"), and so on. It is also referred to as [RestrictedExecution](http://docs.python.org/lib/restricted.html), a topic brought up by Mitch Kapor at [PyCon](PyCon) and noted on his [blog](http://blogs.osafoundation.org/mitch/000559.html#000559).

Related topics include capabilities as mentioned in [PythonThreeDotOh](PythonThreeDotOh), specifically [this message on \"capability-mediated modules\"](http://mail.python.org/pipermail/python-dev/2003-March/034149.html). Some work has been done to support capabilities in languages with similar heritage to Python, notably [CaPerl](http://caperl.links.org/).

## Implementation/Realisation Strategies 

Some of these strategies were suggested in the discussion below.

### Use Another Runtime 

[PyPy](PyPy) has support for creating a sandboxed Python interpreter. The Java and CLR/.NET runtimes support restricted execution, and these can be utilised through the Jython and [IronPython](IronPython) variants of Python (as well as by other languages, obviously).

### Use Operating System Support 

Some operating systems support various levels of sandboxing, with the most extreme form being that of virtualisation or emulation. Yet UNIX-oriented operating systems also provide more lightweight mechanisms for restricting process behaviour such as chroot \"jails\", mandatory access controls, resource limits, and so on.

### Modify the CPython Runtime 

Whilst suggestions about removing functionality from CPython have been generally rejected either as being too simplistic and naive with regard to the possibilities to subvert Python\'s introspection mechanisms, or too restrictive with regard to support for commonly used modules or language features, it is at least reasonable to entertain the notion that a version of CPython linked to special system libraries and built without the more \"powerful\" or \"unsafe\" extensions (see [Plash\'s sandboxing and libc call modifications](http://plash.beasts.org/environment.html#table-glibc-calls) for one approach) would not have the ability to perform arbitrary operations on the filesystem or network. Indeed, this is the basis on which operating systems are hosted within each other using various virtualisation technologies.

### Use a Sandbox as an Accessory 

In some cases, the functionality of untrusted code may be strictly defined. For example, mobile agent systems may, for the agents themselves, permit only a highly restricted style of program, or may only permit a very limited style of interaction with other components. One solution which can be considered within this particular domain is Zope\'s [RestrictedPython](http://svn.zope.org/RestrictedPython/) - restricted subset of Python - although that solution focuses on reducing the level of expression in the language subset employed.

## History 

Prior to Python 2.3, there were two modules, rexec and Bastion which were attempted to provide a sandboxed environment. Unfortunately there were known bugs and work-arounds in these modules, and the introduction of new-style classes in Python 2.3 simply made matters worse. Rather than provide a false sense of security, the modules were removed in Python 2.3.

There are a number of people who are interested in creating a new sandboxing system for Python. Apart from the Zope [RestrictedPython](http://svn.zope.org/RestrictedPython/) implementation, some [work by Brett Cannon](http://svn.python.org/view/python/branches/bcannon-objcap/securing_python.txt) is ongoing, and related works such as [mxProxy](http://www.egenix.com/files/python/mxProxy.html) are also available (although the objectives of the latter and similar projects may be less ambitious than providing a full restricted execution environment).

------------------------------------------------------------------------

## Reactions 

For my part, I think this is something that the PSF should fund development on so that it happens sooner rather than later. There are enough interested parties, that lends itself to getting government or other grant funding. \-- [KevinAltis](KevinAltis)

Having used the rexec stuff years ago (1995-6), I seem to recall that the principles of that module involved restricting the modules available, possibly along with the attributes available from each module, class and object. Is there a concise summary of how such mechanisms could have been subverted/exploited and a description of why they are particularly hard to fix? Or is that what this page is about? \-- [PaulBoddie](PaulBoddie)

I think it should be what the page is about. The basic problem is that Python\'s introspection allows several ways to \"escape\". For instance, code which is passed a file object, f, are given access to that single file, but it ALSO can use \"type(f)\", or \"f.class\" to get access to \"file\" itself, and then use it to open any file. Security experts will tell you that \"plugging holes\" is generally a poor approach to security because there usually turn out to be additional \"holes\" you hadn\'t considered \-- true security requires an overall design with security considerations included. Doing this for Python is not impossible, but may prove difficult. On the other hand, I would agree that it is worthwhile. \-- [MichaelChermside](MichaelChermside)

I also have another idea\... I have long thought that much of the issues could be handled by creating a module which would make it easy to run bits of Python code in a *separate* interpreter, running as a separate process, and sandboxed using OS features. The difficulty would be that such a module would require OS-specific code\... but it would have the potential to provide sandboxing that was as reliable as the OS would allow. \-- [MichaelChermside](MichaelChermside)

Sounds like Parrot, ([PythonAndParrot](PythonAndParrot),) to me. \-- [LionKimbro](LionKimbro)

How so? \-- [MichaelChermside](MichaelChermside)

Oh, sorry. No, Parrot doesn\'t refer to running bits of Python code in a seperate interpreter.

Parrot seems like a good target for running the sandboxed code in. I mean: \".NET\" and all. Make it so you can secure the Parrot interpreter, and you\'re good. If a module requires custom C code links, or whatever, make it so you can close the gates to individual parts of C code, or something. And then make it so you can put various [RestrictedExecution](RestrictedExecution) thingies on the Python code. \-- [LionKimbro](LionKimbro)

Perhaps a better solution with the same approach would be [Jython](Jython). Java provides excellent sandboxing capabilities, and [Jython](Jython) has the distinct advantage that it *already exists and works*. \-- [MichaelChermside](MichaelChermside)

- As does [boo](http://boo.codehaus.org/), which runs on the .NET and Mono runtimes, which also have excellent sandboxing capabilities (I do not claim that they are any better than java, however). See [this thread](http://www.gamedev.net/community/forums/topic.asp?topic_id=264462) (you would have to convert the C# example posted by [VizOne](./VizOne.html) to boo. There is a C# to boo converter in the boo add-in for the free [SharpDevelop](./SharpDevelop.html) IDE).

Whereas Parrot; I think Parrot will function just fine. It\'ll just take a little time. \-- [LionKimbro](LionKimbro) 2004-05-07 16:54:04

We created a project [Pynbox](https://github.com/dsagal/pynbox) to run Python in a NativeClient OS-level sandbox. It makes it easy to install (root not required), works cross-platform, supports native modules, and allows configuring read/write access to specific filesystem directories. We use it at Grist Labs, but would love to know if there is wider interest and to get feedback. \-- [DmitryS](DmitryS) 2017-06-06
