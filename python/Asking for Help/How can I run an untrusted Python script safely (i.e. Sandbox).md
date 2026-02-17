# Asking for Help/How can I run an untrusted Python script safely (i.e. Sandbox)

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## How can I run an untrusted Python script safely (i.e. Sandbox) 

See also: [Security](Security), [SandboxedPython](SandboxedPython).

I\'ve noticed that some people mention a Python style sandbox, but nothing concrete. Here\'s my problem:

I would like to be able to distribue a Python script to be run on computers that may not trust me (I.E. for use as a Folding@Home kind of distributed application.)

However, I would like my Python script to run in a secured sandbox that would not allow that script (by malice or accident) to damage that person\'s computer.

Also, I would like to be able to call compiled programs to do work (distribute a compiled C++ module to use hard hard hard calculations as a program, then pass the program parameters to do the work, then retrieve the values from standard out, etc); but again, the compiled programs would be \"untrustworthy\" and would need to be sandboxed somehow.

And thoughts that could help along with this would be great! Thanks.

## Some ideas about sandboxing Python 

Here are some ideas that you might consider; note that not all of them will be appropriate for some kinds of environments or systems:

- pypy-c provides sandboxing support, see [pypy sandboxing docs](http://codespeak.net/pypy/dist/pypy/doc/sandbox.html)

- Use [Jython](Jython) and try and use the Java platform to lock down the program\'s privileges. It should be possible to run Jython programs as applets, if implemented appropriately.

- Have some kind of mechanism that builds a chroot jail for your software, perhaps using [chrootbuilder](http://www.wiredyne.com/software/chrootbuilder.html) (a Python program which defines chroot jails and emits shell scripts which set them up), [makejail](http://www.floc.net/makejail/) (another Python program which makes chroot jails) or [Jailkit](http://olivier.sessink.nl/jailkit/) (a chroot jail utility collection which also uses Python). Note that chroot jails can still be insecure if not set up properly (as described [in this article](http://www.bpfh.net/simes/computing/chroot-break.html)) and it is best to investigate the potential security weaknesses along with the \"best practices\" used to minimise security risks (as described [in this article](http://www.unixwiz.net/techtips/chroot-practices.html)) and to consider general advice about writing secure programs (such as [this chapter on minimising privileges](http://www.dwheeler.com/secure-programs/Secure-Programs-HOWTO/minimize-privileges.html)). Something like [Plash](http://plash.beasts.org/) might be an improvement: a tool based on chroot which \"virtualizes the file namespace, and provides per-process/per-sandbox namespaces\".

- Consider using [fakechroot](http://fakechroot.alioth.debian.org/) and [fakeroot](http://fakeroot.alioth.debian.org/) with chroot in order to avoid needing root privileges.

- Operating system virtualisation solutions might prove to be too resource intensive for small-scale sandboxing, but a range of such solutions are available - see [Wikipedia\'s \"Comparison of virtual machines\"](http://en.wikipedia.org/wiki/Comparison_of_virtual_machines) for an overview.

Unfortunately, CPython\'s restricted execution capabilities (rexec, Bastion) were deprecated after it was discovered that improved introspection capabilities had rendered their mechanisms ineffective. By using an alternative runtime (ie. [Jython](Jython)) or operating system features (eg. chroot jails), you may actually be utilising a better solution, however. \-- [PaulBoddie](PaulBoddie)

- [http://pypi.python.org/pypi/RestrictedPython/](http://pypi.python.org/pypi/RestrictedPython/)

- [http://www.wesnoth.org/forum/viewtopic.php?t=15593](http://www.wesnoth.org/forum/viewtopic.php?t=15593) says galcon\'s pysafe is similar to zope restrictedpython but simpler, is included in a zip there - i did not find pysafe anywhere from the author, his announcement is [http://www.wesnoth.org/forum/viewtopic.php?t=15593](http://www.wesnoth.org/forum/viewtopic.php?t=15593)

In addition to the above, added anonymously, you might want to inspect [jailtools](http://www.python.org/pypi/jailtools) to see whether it provides some useful ideas for chroot jail construction. Note that I **do not** make any guarantees about security for jailtools. \-- [PaulBoddie](PaulBoddie)

I suggest using [Pynbox](https://github.com/dsagal/pynbox), Python in a NativeClient (NaCl) sandbox. NaCl is the best project I know of to run native code in a sandbox, which is what the question is asking for. We created Pynbox to make it easy to install and run Python under NaCl, including ability to use native modules. Building new native modules is more involved, but there are instructions and an example. \-- [DmitryS](DmitryS) 2017-06-06

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
