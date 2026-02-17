# MacPython/SummitMinutes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

These are the minutes of a meeting of some of the [MacPython](MacPython) developers (Jack Jansen, Bob Ippolito and Ronald Oussoren) at Mar 15 2004

#### Do we want to unify MacPython and PyObjC? 

- If not: where is the IDE/PackMan/etc going?
- If yes: how are we going to organise this?
  - Split [MacPython](MacPython) out from Python?

  - Merge [../PyObjC](./MacPython(2f)PyObjC.html) into Python?

We decided to keep the [../PyObjC](./MacPython(2f)PyObjC.html) and Python CVS repositories separate. Some things will move from the Python repository to the [../PyObjC](./MacPython(2f)PyObjC.html) repository, or, actually, their replacements will: the next version of the IDE, [../PackMan](./MacPython(2f)PackMan.html) and [../BuildApplet](./MacPython(2f)BuildApplet.html) will live in the PyObjC repository.

- [../PyObjC](./MacPython(2f)PyObjC.html) will move the the Python license, we have a message from the main

old contributors that they are okay with this.

#### What is our timeline? 

We would like to have a [MacPython](MacPython) distribution in summer. This distribution will consist of the new IDE, [PackMan](./PackMan.html), [BuildApplet](./BuildApplet.html), [../PyObjC](./MacPython(2f)PyObjC.html) and bug fixes for the Panther Addon distribution. For the Jaguar distribution it will also contain Python 2.3.X for whatever X is current then, for the Panther Addon distribution it will rely on Apple-installed [MacPython](MacPython).

#### Who is our audience? 

- Only 10.3?
- Only existing Python users, or new blood too?
  - OSA scripters?
  - anyone else?
- Try and keep the audience broad!

Both 10.2 and 10.3 are widely used, so we should try to cater for 10.2 too. 10.1 is too much work.

We need to make sure existing Python users migrating to the Mac feel comfortable with [MacPython](MacPython). They seem so at the moment, we need to keep it that way.

[AppleScripters](./AppleScripters.html) may be an interesting audience in the future, but we have to have more infrastructure finished before we actively target them.

Another interesting audience is education. For this we definitely need the new IDE.

#### What do we want in Python 2.4? 

- new IDE

- new packman

- [../BuildApplet](./MacPython(2f)BuildApplet.html) on steroids

- new icons

- new OSA support

- new/improved toolbox modules:
  - Quicktime

  - [../CoreFoundation](./MacPython(2f)CoreFoundation.html)

  - launch services

  - OSA

  - more?

- Python as OSA language?

- running gui scripts with python in stead of pythonw

- x11 integration

Because our first aim is the summer [MacPython](MacPython) distribution for 2.3.X we are concentrating on what is needed for that: IDE, packman, [../BuildApplet](./MacPython(2f)BuildApplet.html) and icon. The others are optional (or not doable before 2.4).

Bob is going to go after the icon artist again to try and get glasses on the snake, which will hopefully make it acceptable to people with snake-fobia.

Ronald has a [../PackMan](./MacPython(2f)PackMan.html) in [../PyObjC](./MacPython(2f)PyObjC.html). Jack is going to look at it. The old [../PackMan](./MacPython(2f)PackMan.html) will be dropped as soon as possible.

[BuildApplet](./BuildApplet.html) will be rewritten to be a front-end to bundlebuilder. Usability to the (relative) novice is going to be important. We envision that you drop a script on it, and then get a dialog with options (build standalone, use stdio console, include icns file, include plist file, include nib, etc). Defaults for these will be picked up similar to what old [../BuildApplet](./MacPython(2f)BuildApplet.html) did, i.e. if you drop `foo.py` on [../BuildApplet](./MacPython(2f)BuildApplet.html) it will look for `foo.icns` and if it is found fill it in, etc.

[BuildApplet](./BuildApplet.html) will not only be able to save the resulting applet, but optionally also the bundlebuilder call you would use to create it. [../BuildApplet](./MacPython(2f)BuildApplet.html) should be a GUI only, if it needs functionality this will be put into bundlebuilder.

Whether [../BuildApplet](./MacPython(2f)BuildApplet.html) will be a front-end to bundlebuilder or to Bobs next generation bundlebuilder remains to be seen, probably the latter. In that case it would also acquire functionality (but somewhat hidden so as not to daunt newcomers) to select which modules to include/exclude, etc.

We talked a little abou toolbox module naming, and the need to get rid of mactoolboxglue in the Python core library, but postponed most of that.

On the pythonw issue: for 2.4 we should add something like MacOS.NeedWM() (in addition to the existing WMAvailable()). This would test whether WM access is available, and if not print a decent human-readable error message and exit. We would then use this in [EasyDialogs](./EasyDialogs.html), probably Tkinter, etc etc etc. Not before 2.4, though.

We could make life for X11 lovers easier by creating a standard place to put X11-dependent modules, such as non-aqua \_tkinter. `/Library/Python/2.3/x11` comes to mind. The script `x11python` would then prepend this location to sys.path. By providing that script and an x11-version of \_tkinter we could make this the standard.

#### Who is going to work on the new IDE, and when\... 

- [PyOxide](./PyOxide.html)?

  - There\'s still the license\...

- what are our other options?

We talked a lot about this, but unfortunately I (Jack) didn\'t take notes.

Fortunately Ronald did take notes ![:-)](/wiki/europython/img/smile.png ":-)")

We\'ve discussed some of the alternatives:

- The [../PyOxide](./MacPython(2f)PyOxide.html) license might be a problem, it is also not written in Python

- Xcode is too project-based for newbies and/or use in a teaching environment, otherwise we could try to create some add-ons for Xcode to transform it into a Python IDE.

The long term view is to create an IDE that can do everything, but for the summer release we\'ll focus on a functional replacement for the current [MacPython](MacPython) IDE (perfect is the enemy of good enough). In the long run we\'d like to see:

- Must be able to print both scripts and script output. This is essential for use in a classroom environment.
- User scripts run in a seperate executable (like IDLE). This functionality is in idlelib, that might be usuable. There\'s also the HAP debugger, which can be used for debugging over TCP/IP (e.g. from another machine).

<!-- -->

- A generic inspection/browsing interface. This could then be used for inspecting:
  - python objects in the debugger
  - application state of apple-scriptable application (\"OSA debugger\")
  - C state of application (using GDB)
  - It should be possible to execute statements in specific stackframes from the debugger (bdb can do this, but most frontends to it can not) The inspector should offer an interface for customizing the inspection of specific classes and instances (the Xcode debugger has this, and that\'s very convenient)
- Integrating external editors would be nice (added when both Bob and Ronald noted that \'vi\' keybindings would be nice to have)
- It should be possible to work with projects, but standalone python files should also work.

There are various components that could be reused: [../PyObjC](./MacPython(2f)PyObjC.html) has examples containing a classbrowser and python interpreter widget. Drawbot has a python editor widget that includes syntax coloring.

The working name for the new IDE is PyDE, the code will be located in the PyDE module of the [../PyObjC](./MacPython(2f)PyObjC.html) repository. The module has been created, but is mostly empty.

In the \*very\* long run Jack would like to see a VB/hypercard tool that would allow you to paint a GUI, attach code to interface elements and would then create a normal Cocoa application (a NIB file and a \"normal\" MVC application). The application would be able to read back the generated code to allow modification. This requires a significant amount of work.

#### Serious bugs/omissions/problems to fix: 

- Does the installer problem (839865) still exist?
- bundlebuilder NG
- Interaction between Apple-Python and User-installed-Python
- linking of extensions
- where to put scripts, includes, etc (i.e. layout for
  - /Library/Python and \~/Library/Python)

We\'re going to investigate the installer problem, it could be that it is 10.2 only. Besides the referenced problem there is also the (null) problem if you build a [../RootDiskOnly](./MacPython(2f)RootDiskOnly.html) installer. The [../PyObjC](./MacPython(2f)PyObjC.html) and Python installer builder modules are going to be merged.

bundlebuilder2 is going to be a package, so it can include [PyMacApp](./PyMacApp.html). It\'s going to have a different name (appbundle and various others flew around, Bob will pick something). It\'s also going to have other new nifty things.

We think that we can switch to linking extensions with \"-undefined dynamic_lookup\" on Panther without any adverse effectrs on compatibility. This would solve the main problem between the two pythons. What remains to be seen is whether we can somehow coerce distutils to also use dynamic_lookup when building with Apple-installed Python (which wasn\'t built that way).

For 2.3.X we put scripts in `/Library/Python/2.3/bin` and includes in `/Library/Python/2.3/include` through some [../PackMan](./MacPython(2f)PackMan.html) magic. [../PackMan](./MacPython(2f)PackMan.html) will also try to pass the include directory to later builds.

For 2.4 configure and distutils need to be taught about the DEPLOYMENT_TARGET environment variable, so it will become possible to develop for 10.2 on 10.3, and so extensions built with 10.2-python on 10.3 are automatically 10.2 compatible.

(Ronald) We also discussed createing a `bdist_packman` command for distutils. This would create a tarfile like `bdist_dumb`, but using a symbolic name for the special directories (e.g. `SITE_PACKAGES/Foo/foo.py` instead of `/.../site-packages/Foo/Foo.py`). [../PackMan](./MacPython(2f)PackMan.html) will use these tarfiles instead of the `bdist_dumb` files it is currently using for binary installs.

Packman will install scripts and include files into /Library/Python instead of inside the framework (scripts is definitely for the summer release, not sure about the include files). Binaries/scripts will be installed into /Library/Python/2.3/bin. This is a bit messy for Python 2.3 (/Library/Python/2.3 is also the site-packages directory), but Python 2.4 will use the correct directory structure (site-packages will be a sibling of bin, just like in \~/Librrary/Python).

#### What do we need to integrate, and when? 

- [../PyMacApp](./MacPython(2f)PyMacApp.html)

  - needs different name (cf. [MacApp](./MacApp.html))

  - optional, or always use this?

  - Can we make the plist-file dependencies optional?

- [../AppScripting](./MacPython(2f)AppScripting.html)

  - needs a different name, preferrably short. OSA? Scripting?
  - or is aeve still an option?
  - how well do we know it?

- DSP\'s OSA stuff
  - if/when it gets done\...

[PyMacApp](./PyMacApp.html) is goint to be renamed, and there\'s no reason to make it optional (at least, not for Panther). The plist-file dependency is not going to be optional, because of the \"explicit is better than implicit\" dictum.

Bob is going to talk to Hamish on [AppScripting](./AppScripting.html).

We are going to bug DSP until he delivers OSA.

#### Internal things 

- Use new header files, not universal, for bgen
  - Or use a different tool? What?
- How about our flaky installer builder, switch to Apple tools?

Not for the summer release.

#### What do people still have up their sleeve? 

- Bob\'s [../PackMan](./MacPython(2f)PackMan.html) helper

- Jack\'s [../PackManPro](./MacPython(2f)PackManPro.html) (non-existent)?

later.

#### What do we need from the general Python community? 

- In other words: which PEPs do we need to write;-)

- distutils
  - installation database
  - python/vendor/admin/user installation
  - also for include, scripts, etc
  - more?

- packman

- bug fixes to vendor-supplied python?

- [PyArg](./PyArg.html)\_Parse

The various people mumbled promises to put some work into this, at some point.

#### Outreach 

- Should we come up with killer examples?
  - OSA scripting
  - CGI scripting
- Should we get someone to write a book?

The general feeling is that it is slightly too early to go for a book.
