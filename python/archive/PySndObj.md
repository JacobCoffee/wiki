# PySndObj

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Description: The Sound Object Library is an object-oriented audio processing library. It provides objects for synthesis and processing of sound that can be used to build applications for computer-generated music. See for more information the [sndObj homepage](http://sndobj.sourceforge.net/#python).

## Installation 

There is no installer included, but you can move/copy (for the Windows platform) the .pyd and .dll files to your %pythondir%\\DLL and the .pyc files to %pythondir%\\Libs .

## Documentation 

- [The (limited) python manual](http://downloads.sourceforge.net/sndobj/PySndObj.pdf?modtime=1169813301&big_mirror=0)

- [The official manual](http://downloads.sourceforge.net/sndobj/SndObj_Manual-2.6.4.pdf?modtime=1169813964&big_mirror=0)

For further assistance, please have a look at the [mailinglist](http://sourceforge.net/mailarchive/forum.php?forum_name=sndobj-devel)

## Code Examples 

Some examples not available in [the manual](http://downloads.sourceforge.net/sndobj/PySndObj.pdf?modtime=1169813301&big_mirror=0). More examples are included in the download itself.

### A simple synth 

A simple synth with band limited noise, oscilators, and alternating L-R output. In case of any issue, contact [renato.fabbri@gmail.com](mailto:renato.fabbri@gmail.com) AND/OR contact sndObj mailing list.

:::: 
::: 
``` 
   1 import sndobj
   2 import time
   3 
   4 tab = sndobj.HarmTable()
   5 osc = sndobj.Oscili(tab, 440, 10000)
   6 noise = sndobj.Randh(100000, 10000)
   7 
   8 x=1
   9 y=2
  10 
  11 outp = sndobj.SndRTIO(2)
  12 outp.SetOutput(x, osc)
  13 outp.SetOutput(y, noise)
  14 
  15 mod = sndobj.Oscili(tab, 2, 560)
  16 osc.SetFreq(440,mod)
  17 
  18 mod2=sndobj.Oscili(tab, 4, 50)
  19 mod.SetFreq(2, mod2)
  20 
  21 q=2
  22 mod3 = sndobj.Oscili(tab, q, 1000)
  23 noise.SetFreq(1000, mod3)
  24 
  25 thread = sndobj.SndThread()
  26 thread.AddObj(mod)
  27 thread.AddObj(mod2)
  28 thread.AddObj(mod3)
  29 thread.AddObj(osc)
  30 thread.AddObj(noise)
  31 thread.AddObj(outp, sndobj.SNDIO_OUT)
  32 
  33 thread.ProcOn()
  34 
  35 n=0
  36 while n < 8:
  37     if x==1:
  38         x=2
  39         y=1
  40     else:
  41         x=1
  42         y=2
  43     outp.SetOutput(x, osc)
  44     outp.SetOutput(y, noise)
  45     time.sleep(1)
  46     n +=1
  47 
  48 thread.ProcOff()
```
:::
::::
