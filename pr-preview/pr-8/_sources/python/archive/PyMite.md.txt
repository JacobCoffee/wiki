# PyMite

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### What is PyMite 

PyMite is a flyweight Python interpreter written from scratch to execute on 8-bit and larger microcontrollers with resources as limited as 64 KiB of program memory (flash) and 4 KiB of RAM. PyMite supports a subset of the Python 2.5 syntax and can execute a subset of the Python 2.5 bytecodes. PyMite can also be compiled, tested and executed on a desktop computer.

Considering PyMite is designed to run on embedded 8-bit architectures, one should not expect PyMite to do everything Python can do. However, its capability may surprise you. Since PyMite is written from scratch, it has a few features that set it apart: stackless from the start and fast, easy, native C function support.

### Availability 

The latest version of PyMite is available from [http://code.google.com/p/python-on-a-chip/](http://code.google.com/p/python-on-a-chip/)

------------------------------------------------------------------------

### Conversation Before PyCon 2003 

I would like to know how many people plan to attend this presentation. I would also like to target my presentation as best I can to those people attending. So please add questions/suggestions below; for example:

- I would attend if \...

- Will PyMite run on \...

- etc.

------------------------------------------------------------------------

*your question/comment here*

Very Cool! I have an AVR board that is just itching to have this installed. I will definitely be in attendance! I\'m especially interested in what kind of hardware interfaces you\'re providing (avr.porta.write(0x34)?) and what kind of simulation environment (if any) exists. -[PyConBrianWarner](../conferences/pycon/PyConBrianWarner)

------------------------------------------------------------------------

This is a fascinating project. I\'ve been looking for an embeddable system-on-a-chip that would run a reduced-size python. It would be a great help to attendees of your talk without previous microcontroller background to see on this wiki a list of typical devices you are targeting, so that we might familiarize ourselves with them beforehand.

I\'m specifically interested in the [AxisETRAX](http://www.axis.com/en/products/dev_etrax_100lx/) as an embedded system. It seems capable enough (runs linux) that it might run a standard python, given enough RAM and eliminating unecessary libraries. PyMite is exciting because it might run (and run fast) on the standard [standard chip](http://developer.axis.com/products/etrax100lx/) or [MCM](http://developer.axis.com/products/mcm/index.html) with no additional storage. -Jeff Kowalczyk

------------------------------------------------------------------------

Very impressive effort. I have written a multitasking OS for AVRs and working on a simple language compiler but I like the look of PyMite better! I am wondering at the performance you have observed with PyMite - all those overheads are not noticed on a desktop processor, but they must be a problem on small MCUs. I am looking forward to giving PyMite a spin and seeing what it can do.

Cheers, MikeS - mike at acslink stop net stop au

### Comments & Answers on feedback 

All, I have made release_01 available on Sourceforge under the Artistic License. This release is ugly in the sense that I have not made one ounce of effort to make the directory structure pretty. I simply zipped up the development tree as it exists in version 7 (I\'m using Subversion for source code management). I apologize for the ugliness please send feedback on how I can improve this. The URL is: [http://sourceforge.net/projects/thmonkeeproject](http://sourceforge.net/projects/thmonkeeproject)

Brian, thanks for the enthusiasm. I can say that reading/writing to Ports and peripherals is critically important and is supported. However, my approach is a bit more generic than your example. My first crack at solving this is to employ peek(addr) and poke(addr, val) operations which read and write values in memory. Since most MCUs have their peripheral control registers mapped into memory, these two operations allow abundant flexibility and a platform-neutral interface.

Jeff, one early bit of feedback I got was to avoid talking too much about hardware (when I felt I had barely mentioned hardware in my paper). So it is good to hear your comments which ask for more hardware details; this balances the scales. As I said above, the primary target is the Atmel [AtMega103](./AtMega103.html) (or 128) because this is the device I have driving my robot controller board. However, any device in the [AtMega](./AtMega.html) family which meets these requirements: 20KiB Flash and 4K RAM, will run today. But the 4K heap is rather small and limits the complexity of programs that can be run. I am also intending to port PyMite to the popular Motorola HC11-through-Star12 family. Porting to the HC11 would allow PyMite to run on MIT\'s popular Handyboard robot controller. These first two porting targets are simply my preference. This does not limit in any way someone taking the PyMite source and porting it to the processor of their choice. The only requirements so far are an ANSI C compiler, and a fair amount of porting effort.

Jeff, you mention the Axis controller. I find the \"standard chip\" to be more like a microprocessor and the MCM to be more like a microcontroller (memory and peripherals are on-board). If linux (uCLinux?) runs on this device, PyMite would offer less resource consumption than running the full Python interpreter. However, PyMite is still too early in development to make any claims that it would be \"better\" for this environment.

------------------------------------------------------------------------

[CategoryPyConSpeakerPage](CategoryPyConSpeakerPage) [CategoryPyCon2009](CategoryPyCon2009) [CategoryImplementations](CategoryImplementations)
