# AppsWithPythonScripting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Applications can be written almost completely in Python, but people are slow to change, so a considerable number of desktop applications are still written using C/C++ on Linux and Windows and a combination of C++ and Objective-C on Mac OS X. There has been a sustained trend of the use of Python to provide user automation or scripting, sometimes called macros, for C/C++ applications. This makes a lot of sense:

- Developers don\'t have to waste time and money inventing their own scripting language.

- Users don\'t have to learn a new automation language for every application they use, and can use Python books, exampling, and learning resources.

- Python is a [Free Software](FreeSoftware) ([Open Source](OpenSource)) solution and can be embedded and distributed without charge, so there are no royalty payments or licensing hassles

- Python is simple to learn, yet Python and its standard libraries are much more powerful than a proprietary language like VBScript

- Python is cross-platform

- [tools](AppsWithPythonScripting#head-3) like [Cython](http://www.cython.org/) and [BoostPython](BoostPython) make it easy to expose part or all of the application programming interface (API)

- Python scripting can be added to legacy projects just as well as new ones so developers don\'t have to abandon their old C/C++ code libraries

- On the Windows platform, Python has an excellent interface to COM (also known as ActiveX) and can be used to interface to almost any COM program (such as the MS-Office suite). Again, Python scripting can be added to enhance a project without change to the existing COM components. (See [Win32All](Win32All))

- [PyObjC](http://pyobjc.sourceforge.net) can be used to add scripting to any Cocoa app on Mac OS X

- Many Mac OS applications provide Apple event-based scripting interfaces, allowing them to be controlled from languages such as [AppleScript](http://www.apple.com/applescript/), [JavaScript OSA](http://www.latenightsw.com/freeware/JavaScriptOSA/), Perl (via [Mac::Glue](http://search.cpan.org/~cnandor/Mac-Glue/)), Python (via [appscript](http://freespace.virgin.net/hamish.sanderson/appscript.html)), Tcl and [UserTalk](./UserTalk.html). (See [MacPython](MacPython))

For many of the same reasons, Python is often used as the \"glue\" language for a project. In the Java world, people are using [Jython](Jython) as the glue and scripting language.

![(!)](/wiki/europython/img/idea.png "(!)") **This page is not for listing those applications primarily built with Python. Try [Applications](Applications) for those types of apps, tools, and frameworks.**

![(!)](/wiki/europython/img/idea.png "(!)") **Please keep wiki links as wiki links, use external links only if there is no existing page for the program.**

### Applications and Toolkits 

::: {}
  -------------------------------------------------------------------------------------------------------------- -------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                                                                                       **Platform**               **Notes**
  [Abaqus](http://www.abaqus.com/)                                                                        multi-platform             Finite element analysis, modeling, and visualization. Python is embedded for command scripting and GUI extensibility.
  [ArcGis](http://www.esri.com/software/arcgis/)                                                                                     
  [BioNumerics](http://www.applied-maths.com/bionumerics/bionumerics.htm)                                 Windows                    A suite of bioinformatics software applications, [uses Python](http://www.applied-maths.com/support/workshop_python.htm) to automate series of actions that are executed repeatedly, to create custom reports, import and export non-standard formats, perform custom calculations, etc.
  [ClearSilver](ClearSilver)                                                                              multi-platform             Web application framework
  [CodeSubWars](http://www.codesubwars.org/)                                                              Windows                    Free programming game. Uses Python as scripting language for submarine robots.
  Emacs, using [Pymacs](http://pymacs.progiciels-bpi.ca/)                                                 multi-platform             Text editor.
  [FontLab](http://www.fontlab.com/)                                                                      Windows, Mac OS            Commercial font editing software, uses Python as a macro language.
  [GXSM](http://gxsm.sourceforge.net/)                                                                    Linux, Mac OS X            Gnome X Scanning Microscopy - multi-channel 2D/3D data acquisition and visualization
  [Golly](http://golly.sourceforge.net/)                                                                                             Open source, cross-platform Conway\'s Game of Life simulator.
  [Helix DNA](https://helixcommunity.org/)                                                               multi-platform             The Helix community is a collaborative effort among real, independent developers, and leading companies to extend the Helix DNA™ platform, the first open multi-format platform for digital media creation, delivery and playback.
  [Kahakai Window Manager](http://kahakai.sourceforge.net/)                                               POSIX and X11              Python is used for event and key binding configuration.
  [Kaydara Motionbuilder](http://www.kaydara.com/products/motionbuilder/)                                 Mac OS X, Windows          Helpful for integrating into production pipelines and allows users to automate repetitive processes.
  [Mahogany](http://mahogany.sourceforge.net/)                                                            Linux, Mac OS X, Windows   [OpenSource](OpenSource) cross-platform mail and news client.
  [MindLathe](http://www.mindlathe.com/)                                                                  ?                          AI middleware
  [GarageCube Modul8](http://www.garagecube.com/modul8/)                                                  Mac OS X                   Video mixing and compositing for VJs and live performers; uses Python for internal scripting.
  [MUSHclient](http://www.mushclient.com/)                                                                Windows & WINE             MUD client
  [NSIS2](http://nsis.sourceforge.net/)                                                                   Windows                    There is an [NSIS Python Plugin](http://homepage.hispeed.ch/py430/python/) for this [OpenSource](OpenSource) installer for Windows. \-- Note: *makensis*, the installer compiler, now compiles and runs on POSIX systems too.
  [OGRE](http://www.ogre3d.org/)                                                                          multi-platform             Object-Oriented Rendering Engine
  [OpenOffice](http://www.openoffice.org/)                                                                multi-platform             [Python-UNO bridge](http://udk.openoffice.org/python/python-bridge.html) for scripting [OpenOffice](./OpenOffice.html) with Python
  Office and Outlook                                                                                             Windows                    While Microsoft Office apps including Microsoft Outlook were not originally designed to be scripted with Python, [PyWin32](http://wiki.python.org/moin/PyWin32) (formerly [Win32All](Win32All)) makes it possible to script Microsoft Office apps and build plug-ins. Of special note is the [SpamBayes](http://spambayes.sourceforge.net/windows.html) plug-in for Outlook which enables any Outlook user to use [SpamBayes](http://spambayes.sourceforge.net/windows.html) without even knowing anything about Python.
  [Orange](https://orange.biolab.si)                                                                     multi-platform             Orange is a component-based data mining software. It includes a range of preprocessing, modelling and data exploration techniques. It is based on C++ components, that are accessed either directly (not very common), through Python scripts (easier and better), or through GUI objects called Orange Widgets.
  [Orca](http://www.gnome.org/projects/orca/)                                                             GNOME                      Accessibility toolkit for applications using GTk+/AT-SPI that provides speech synthesis, braille, and magnification.
  [Paint Shop Pro 8](http://www.jasc.com/products/paintshoppro/)                                          Windows                    Photo and graphics editor. [PSP scripting resources](http://www.jasc.com/support/customercare/articles/psp8components.asp)
  [Panda3D](http://www.etc.cmu.edu/panda3d/)                                                              multi-platform             Open Source game and simulation engine. Disney is one of the notable users. Check out the [PyCon paper on Panda3d](http://www.python.org/pycon/dc2004/papers/29/Panda3D.htm).
  [ProScena](./ProScena.html) Studio                                                                                          A high-level content-authoring system and runtime for creating real-time interactive 3D simulations for training, education and gaming applications. [press release](http://www.prnewswire.com/cgi-bin/stories.pl?ACCT=SVBIZINK8.story&STORY=/www/story/03-25-2004/0002134657)
  [Ciranova\'s PyCell Studio](http://www.ciranova.com/products/)                                                                     A tool from an Electronic Design Automation company
  [Quantum GIS](http://www.qgis.org/)                                                                     multi-platform             User friendly open source Geographic Information System (GIS)
  [Resolver One](http://www.resolversystems.com/products/resolver-one.php)                                .NET/CLR                   Programmable spreadsheet built around [IronPython](IronPython).
  [Scorpion Vision Software](http://www.scorpionvision.com/)                                              Windows                    Machine-vision software for industrial use with Python scripting
  [Scribus](http://www.scribus.net/)                                                                                                 
  [SilverRun ModelSphere](http://www.silverrun.com/)                                                      Windows/Linux/Solaris      A relational data modeling tool with Jython scripting.
  [SPSS](http://www.spss.com/devcentral/)                                                                                            Statistical and data management package for analysts and researchers.
  [Squish](http://www.froglogic.com/squish)                                                               multi-platform             An automated GUI testing framework for Qt applications that supports Python scripting
  [Subversion](http://subversion.tigris.org/)                                                             multi-platform             A compelling replacement for CVS. See the [Project Links](http://subversion.tigris.org/project_links.html), [Bindings](http://subversion.tigris.org/bindings.html) or do a [Google site search](http://www.google.com/search?&q=site:subversion.tigris.org+python).
  [SuperKaramba](http://netdragon.sourceforge.net)                                                        Linux, KDE                 [SuperKaramba](./SuperKaramba.html) allows you to create cool dekstop widgets with little to no programming experience. It\'s similar to \"Konfabulator\" for the Mac.
  [truSpace](http://www.caligari.com/)                                                                    Windows                    3D modelling/animation package
  [Vim](http://www.vim.org/)                                                                              multi-platform             Text editor.
  [WinCvs](http://www.wincvs.org/)                                                                        Windows                    GUI front-end for CVS
  [XChat](http://www.xchat.org/) , [SilvereX\'s free Windows version](http://www.silverex.info/)   multi-platform             IRC Client
  -------------------------------------------------------------------------------------------------------------- -------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

### Games 

::: {}
  ---------------------------------------------------------------------------------------------- --------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                                                                       **Platform**                                        **Notes**
  [Backyard Hockey](http://www.funkidsgames.com/games/byhockey_pc/)                       Windows                                             [1](http://onlamp.com/pub/a/python/2002/07/11/pythonnews.html), [2](http://www.cygnus-software.com/papers/gamescriptinginpython.html), [3](http://mail.python.org/pipermail/tutor/2003-June/023690.html)
  [Battlefield 2](http://www.eagames.com/official/battlefield/battlefield2/us/home.jsp)   Windows?                                            Scriptable in Python
  [BigWorld](http://www.bigworldtech.com/)                                                Windows                                             Complete MMOG tool set. The [FAQ](http://www.bigworldtech.com/faq.php), [Client Engine](http://www.bigworldtech.com/client/client_object_scripting.htm) and [Server Engine](http://www.bigworldtech.com/server/server_custom_worlds.htm) pages highlight how Python is integrated.
  [Blade of Darkness](http://www.codemasters.com/blade/)                                  Windows                                             
  [Butterfly.net](http://butterfly.net/)                                                  multi-platform                                      \"The scalable, reliable and high performance online game platform.\" Uses Python for advanced interactions between players and non-player characters
  Cars with Guns                                                                                 Windows                                             
  [Civilization IV](http://civilization4.net/files/modding/PythonAPI/)                                                                        
  [Earth & Beyond](http://www.earthandbeyond.ea.com/)                                     Windows                                             
  [Eve-Online](http://www.eve-online.com/)                                                Windows                                             Uses [StacklessPython](StacklessPython) for client and server. Description from the web site - EVE: The Second Genesis, is a massively multiplayer, online, persistent world game. perhaps even too real to be called a game, but definitely more fun than reality. Played on the Net, it takes place in a world that is alive and kicking every day, every hour. Players are spaceship captains cruising around the universe, trading, fighting and communicating with other players.
  [Freedom Force](http://www.irrationalgames.com/ff/)                                     Windows                                             [http://www.google.com/search?q=Freedom+Force+Python](http://www.google.com/search?q=Freedom+Force+Python)
  [Frequency](http://www.gamerankings.com/htmlpages2/516506.asp)                          PS2                                                 
  [SpongeBob](./SpongeBob.html) Squarepants                                        PS2 and [GameCube](./GameCube.html)   See Jason\'s [paper](http://www.asbahr.com/papers.html) on the Python-based scripting system.
  [Star Trek Bridge Commander](http://www.bridgecommander.com/)                           Windows                                             
  [Temple of Elemental Evil](http://www.atari.com/toee/)                                                                                      
  [Toontown Online](http://play.toontown.com/)                                            Windows                                             MMORPG. [Postmortem: Disney Online\'s Toontown](http://www.gamasutra.com/features/20040128/goslin_01.shtml) on Gamasutra. Also see info on Panda3D above.
  [Uru: Ages Beyond Myst](http://uru.ubi.com/us/)                                         Windows                                             
  [Vega Strike](http://vegastrike.sourceforge.net/)                                       Linux, Mac, Windows                                 3D OpenGL Action Space Sim
  [Wesnoth](http://www.wesnoth.org)                                                       Linux, Mac, Windows                                 Open-source turn-based-strategy game, uses optional Python AI scripting since version 1.2.0
  ---------------------------------------------------------------------------------------------- --------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

### Graphics 

::: {}
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Acorn](http://flyingmeat.com/acorn/)                                                                                                                                          MacOS X                Image editor.
  [Blender](http://www.blender.org/)                                                                                                                                             multi-platform         [OpenSource](OpenSource) software for 3D modeling, animation, rendering, post-production, interactive creation and playback. [Blender Python API reference](http://www.blender.org/documentation/245PythonDoc/API_intro-module.html) and [tutorials](http://www.blender.org/tutorials-help/python/).
  [Crystal Space](http://crystal.sourceforge.net/)                                                                                                                               multi-platform         [OpenSource](OpenSource) 3D SDK
  [GIMP](http://www.gimp.org/)                                                                                                                                                   multi-platform, GTK    GNU Image Manipulation Program. [PyGimp](http://www.daa.com.au/~james/software/pygimp/) is a package that allows people to write plug-ins for Gimp on Python rather than Script-Fu (Scheme), Perl, Tcl or C.
  [SideFX Houdini](http://www.sidefx.com)                                                                                                                                                               Professional 3D animation and visual effects software
  [Inkscape](http://wiki.inkscape.org/wiki/index.php/PythonEffectTutorial)                                                                                                       multi-platform         Scalable Vector Graphics editor
  [irrlicht](http://irrlicht.sourceforge.net/)                                                                                                                                   multi-platform         The Irrlicht Engine is an open source high performance realtime 3D engine written and usable in C++ and also available for .NET languages. It is completely cross-platform, using D3D, OpenGL and its own software renderer, and has all of the state-of-the-art features which can be found in commercial 3d engines.
  [Autodesk Maya](http://www.autodesk.com/us/maya/docs/Maya85/wwhelp/wwhimpl/common/html/wwhelp.htm?context=DeveloperResources&file=Introduction_to_Maya_Python_API.html)                               3D modeling, animation, effects, and rendering program.
  [Open Inventor](http://oss.sgi.com/projects/inventor/)                                                                                                                         multi-platform         Object-oriented 3D toolkit. [Pivy](http://pivy.tammura.at/) is the Python binding for Open Inventor. Check out the [Pycon paper on Pivy](http://www.python.org/pycon/dc2004/papers/47/pycon-pivy-paper.html).
  [Poser](http://www.curiouslabs.com/)                                                                                                                                           Windows and Mac OS X   3D character animation tool
  [Vue Infinite](http://www.e-onsoftware.com/Products/vue5infinite/)                                                                                                             Multi-platform         Vue is e-on software\'s award-winning, complete 3D studio to create, render and animate ultra-realistic 3D natural environments.
  [Zeno](http://www.cgw.com/ME2/dirmod.asp?sid=&nm=&type=Publishing&mod=Publications::Article&mid=8F3A7027421841978F18BE895F87F791&tier=4&id=25375C2E874C44A29BFB7FDF86F4FD75)                          Internal graphics pipeline used by Industrial Light & Magic.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

### Tools For Integrating Python 

- [Pyrex](Pyrex) \-- now superceded by [Cython](http://www.cython.org/)

- [SWIG](http://www.swig.org/) ([SimplifiedWrapperAndInterfaceGenerator](http://c2.com/cgi/wiki?SimplifiedWrapperAndInterfaceGenerator "Wiki"))

- [BoostPython](BoostPython) and [Boost.Python](http://www.boost.org/libs/python/doc/index.html) (official page)

- [PyObjC](http://pyobjc.sourceforge.net) (Mac OS X)

- [SIP](http://www.riverbankcomputing.co.uk/sip/index.php)

### Articles 

- [Devs Using Python to Boost Integration](http://www.idevnews.com/TipsTricks.asp?ID=107) - In this two-part interview, Martelli offers Win32, Java and .NET devs some useful perspectives on Python, and how Python scripting can extend the integration capabilities of their Win32, ASP.Net, Java and C/C++ applications.

- Embedding Python in Multi-Threaded C/C++ Applications in [LinuxJournal](http://www.linuxjournal.com/article.php?sid=3641)

- [Building Hybrid Systems with Boost.Python](https://www.boost.org/doc/libs/1_66_0/libs/python/doc/html)

- [Integrating Python, C and C++](http://www.suttoncourtenay.org.uk/duncan/accu/integratingpython.html), presented at the ACCU conference by Duncan Booth, and his [conference slides](http://www.suttoncourtenay.org.uk/duncan/accu/accuconf2003.zip)

### Other Resources (many apps from pages below need to be copied to this page) 

- [PythonEditors](PythonEditors)

- [Organizations and Apps using Python](http://www.python.org/community/users.html)

- [http://www.thinkware.se/cgi-bin/thinki.cgi/PythonUsers](http://www.thinkware.se/cgi-bin/thinki.cgi/PythonUsers)

- [Game Scripting in Python](http://www.cygnus-software.com/papers/gamescriptinginpython.html)

- [Humongous Games](http://www.onlamp.com/pub/a/python/2002/07/11/pythonnews.html)

- [IntegratingPythonWithOtherLanguages](IntegratingPythonWithOtherLanguages)

### Additional Notes 

After adding Panda3D and Open Inventor I\'ve started to wonder whether those really qualify as apps the way I originally envisioned this list? Perhaps we should have a separate page for C/C++ libraries, frameworks, etc. that have Python bindings? That would include frameworks like GTK, QT, and [WxWidgets](WxWidgets) which have popular Python bindings. Regardless, all the Python bindings available for popular C/C++ tools and frameworks shows the agility of Python. There are great benefits to adding Python bindings to existing C/C++ (and Java) code bases so that you can leverage the power and flexibility of Python without abandoning an existing code base or giving up the speed of C/C++ code. In these cases, Python is a complement rather than a complete replacement for another programming language. \-- [KevinAltis](KevinAltis)
