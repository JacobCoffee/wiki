# PyConLeonardRichardson

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Synopsis 

Oftentimes, a very small or very new web application will keep all of its configuration settings inside the code itself (hopefully as variable settings in some obvious place). To change the configuration, a user must become a developer of the application. For example:

        #Whether or not to enable image uploads
        ENABLE_IMAGE_UPLOADS = 1

        #The maximum size of an uploaded image, in kilobytes
        MAXIMUM_IMAGE_SIZE = 100

A larger, more flexible, or more mature application may keep its configuration settings in a text file loaded by the application at runtime. When configuring such an application a user is changing data, rather than code, and acting as an administrator rather than a developer. Python\'s [ConfigParser](../../language/ConfigParser) module provides built-in support for this level of flexibility, for example:

        [Images]
        enable-image-upload=1 #Whether or not to enable image uploads
        maximum-image-size=100 #Maximum size of an uploaded image, in kb

The natural next step towards better usability is to provide an interface to the configuration file from within the application itself, using the same framework and UI standards found in the rest of the application. This allows a user to configure the application while remaining just that\--a user:

        Enable image uploads? [X]

        Maximum image size? 100___ kb

The easiest and best way to take this next step is to use a configuration framework.

The purpose of my talk is to get more of the world\'s configuration data out of configuration files and into configuration frameworks with Web interfaces. Configuration frameworks are easier to use, can enforce configuration semantics, and don\'t require shell access to the hosting machine. The framework I describe is also useful for doing a user preferences engine.

## Manifest 

My presentation comes with all sorts of goodies:

- [A scholarly paper](http://www.crummy.com/devel/PyCon2003/Beyond%20The%20Config%20File.htm), with footnotes and everything.

- [Presentation slides.](http://www.crummy.com/devel/PyCon2003/slides/)

- A full-featured configuration interface library called I Want Options (as used in [NewsBruiser](./NewsBruiser.html); you can [view it in CVS](http://newsbruiser.tigris.org/source/browse/newsbruiser/nb/lib/IWantOptions.py))

- Three implementations of a silly text generation program, illustrating the \"three ages of App\" mentioned above.
  - An implementation which uses inline variable settings for its configuration

  - An implementation which reads its configuration from a file

  - An implementation which reads its configuration from a file, and provides a web interface to that same file through I Want Options.

    You can [download these examples](http://www.crummy.com/devel/PyCon2003/examples.tar.gz) as a tarball.

- An implementation of a simple portal program, which uses I Want Options both to provide an interface to user preferences and an interface to site options. You can [download this example](http://www.crummy.com/devel/PyCon2003/examples.tar.gz) in the same tarball as the other examples.

## About Me 

Hello! I\'m Leonard. This was my first conference talk. If you\'re interested in me personally, you can visit [my homepage](http://www.crummy.com/).

The code in this talk is almost all code I wrote for [NewsBruiser](http://newsbruiser.tigris.org/), a weblogging application which you might be interested in independently of the subject of this talk.

## Work Log 

04/02: The slides are up. I think I\'m done with this page.

04/01: [PyCon](PyCon) is over, but the putting-things-on-the-web fun has just begun. I added links to my paper and the examples. The slides will be forthcoming once I get them off my laptop.

03/24: Packing up for [PyCon](PyCon). Hope to see you there!

03/18: Fixed up the final example, documented all the examples, tarred everything up and put it onto my site. Now it\'s just the slides I gotta do.

03/18: Just submitted my paper. I\'ll let you in on a little secret: I didn\'t know I was supposed to write a paper! I thought it was just an abstract and some slides, so I sort of panicked when I got mail from Steve Holden saying to send in my paper ASAP. On the plus side, now that I have a paper the slides will be much easier. I got a lot more good information and arguments from having to write a paper than I would have had otherwise. I\'d like to thank Jason Robbins, Kevin Maples, and Greg Stein for their comments on early drafts of the paper.

I have to get the links mentioned in my paper working tonight. Off to do that\...

03/11: First draft of the paper is done. It\'s about 20k in ReST format; I don\'t know if that\'s long enough; it\'s not a whole lot longer than my abstract. But I said pretty much everything I wanted to say in the abstract, except for the details of my implementation.

I actually gave a talk at work today about our configuration framework (a different one, written in Java). It went pretty well, so I\'m hopeful for the [PyCon](PyCon) talk. Man, I couldn\'t shut up about the configuration framework, I just kept talking and talking! ![:)](/wiki/europython/img/smile.png%20":)")

03/06: Wrote the user preferences app; it\'s a tiny portal application. Still needs some work.

02/27: Just wrote the same app three times. The last time was the most interesting, as I\'d never before implemented a context or a configuration CGI within the framework of I Want Options. When I originally wrote what is now IWO, it was a big blob of [NewsBruiser](./NewsBruiser.html)-specific code; the framework per se is less than a week old. I\'ve now got ideas about more things I can move into IWO (an example context implementation, and some more configuration CGI logic). The other two implementations also gave me some ideas; if I changed it so that the user pass the context into the [OptionConfig](./OptionConfig.html) constructor, instead of passing it in to all the methods (which seems reasonable), I could turn getOptionValue into a [getitem] implementation, which would be cool.

02/21: Got all the [NewsBruiser](./NewsBruiser.html)-specific code out of Options.py. To celebrate, moved it out of [NewsBruiser](./NewsBruiser.html) proper and into the lib/ directory. It\'s now a reusable library called [I Want Options](http://newsbruiser.tigris.org/source/browse/newsbruiser/nb/lib/IWantOptions.py).

To get all the code moved out I had to define a plugin class (it\'s currently called \'wrapper\', but that doesn\'t make much sense) which contains application-specific code and is passed into the [OptionGroup](./OptionGroup.html) and Option constructors. It basically simulates a superclass of all the Option classes, so that you can change the generic Option behavior without having to change all the Option classes to subclass a different class. There might be a design pattern that describes this which would make renaming it easy. Or it might just be an OO hack, in which case I\'ll probably call it \"Implementation\" or \"[ImplementationDetails](./ImplementationDetails.html)\".

02/19: Yesterday I worked on cleaning up Options.py: moving out [NewsBruiserisms](./NewsBruiserisms.html), adding comments and [PyDoc](../../people/PyDoc). I tell myself that this is useful work for the talk and not just a heavily disguised method of procrastination. Today: more of the same. Also set up this wiki page.

------------------------------------------------------------------------

[CategoryPyConSpeakerPage](CategoryPyConSpeakerPage)
