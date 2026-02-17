# AaronWatters/Build64bitPythonOnSolarisAMD64

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Describe AaronWatters/Build64bitPythonOnSolarisAMD64 here.

On Solaris using 64 bit Intel compatible processors you can build applications like Python in either 32 bit mode or 64 bit mode.

Apps built in 32 bit mode cannot link to components built in 64 bit mode \-- so it is often very useful to build Python in 64 bit mode. Even worse, if the 64 bit app tries to load a 64 bit component using a 32 bit loader you also fail.

The symptom of attempting an incompatible application/loader/component combination says something like

       BAD ELF TYPE

To use Python with 64 bit components you need to build python in 64 bit mode. I wasted a number of hours figuring out how to do this, so I thought I\'d share it here. The magic sequence was:

         export PATH=/usr/sfw/bin:$PATH
         export BASECFLAGS="-m64 -L/usr/lib/64 -L/usr/ccs/lib/amd64 -R/usr/sfw/lib/64"
         export CC="gcc $BASECFLAGS"
         export AR=gar
         cd Python-2.5.1/
         ./configure
         gmake

It\'s possible that some of the above is redundant, but it worked for me. This makes Python build in 64 bit mode, using 64 bit libraries and a 64 bit loader. The \"-R\" part was particularly problematic to track down \-- it gets the right loader (I think). I hope this helps someone (like me later when I lose this information).
