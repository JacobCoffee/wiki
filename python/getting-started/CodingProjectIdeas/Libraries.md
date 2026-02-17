# CodingProjectIdeas/Libraries

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Python library ideas 

Suggestions that involve working on various third-party libraries that aren\'t part of the Python source tree.

- Create a Pythonic auto-upgrade framework to allow scripts to update themselves to newer versions.

- Add EPS import to [ReportLab](./ReportLab.html) PDF library

  - [http://article.gmane.org/gmane.comp.python.reportlab.user/4052](http://article.gmane.org/gmane.comp.python.reportlab.user/4052)

- make [Spread](http://www.spread.org/) Python Binding compile with Python 2.4 on win32 (and possibly other major platforms)

- Revive the code or idea from [PyGUI](http://www.cosc.canterbury.ac.nz/~greg/python_gui/) or [Anygui](http://anygui.sourceforge.net/)

  - These are Python-level cross-toolkit compatibility libraries for GUI work. Currently there is a \"live\" project called [Cimarron](http://developer.berlios.de/projects/cimarron/) along these lines. (PyGUI is not a dead project, however Anygui is)

- [NotebookInterfaceForIpython](NotebookInterfaceForIpython)

- [../PygameOnCtypes](PygameOnCtypes)

- Develop the Visual Designer and help update the documentation of [Dabo](http://dabodev.com/).

  - Dabo is a framework for creating 3-tier desktop applications. The UI tier is a wrapper around [wxPython](http://www.wxpython.org/) that greatly streamlines and simplifies the wxPython API, and the Designer is a RAD tool for visually developing UI interfaces.

- Psyco for MacOSX. PPC, and universal binary versions. (Note: unlikely to find a mentor)

- Create a bunch of modules like what Squeak has for 3D modeling, events etc. (the exact list may be somewhat different, I haven\'t researched this in any depth). This is inspired by a recommendation from Alan Kay made at the Shuttleworth workshop. (Would the (GPL) soya3D projects be relevant here?)

- Design and implement an interface for manipulating both [Calc](http://www.openoffice.org/product/calc.html) and [Gnumeric](http://www.gnome.org/projects/gnumeric/) spreadsheets (in the same way that DB-API allows programs to interact with a variety of databases).

- Write an IPC or RPC package to allow for concurrent Python execution. Compare with [http://rpyc.sourceforge.net](http://rpyc.sourceforge.net)

- Implement ctypes support for GCC ARM platforms. The underlying issue is lack of closure API support for ARM in libffi. A patch available at [http://handhelds.org/\~pb/arm-libffi.dpatch](http://handhelds.org/~pb/arm-libffi.dpatch), that should be hopefully a good starting point. ctypes CVS has a libffi_arm_wince directory, which also seems to support closure API.

- Create a Python web app server, synthesized from the many options already available, with an eye towards the total developer experience.

- Integrate a Javascript interpreter with Python. [WebCleaner](http://webcleaner.sourceforge.net/) has some initial work; so extracting, documenting, and refining that code would be in order. The whole spec is probably too much, but you could focus on langauge support, or on \"what typical web pages actually need\".

- Implement [IEEE Std 802.1X](http://www.ieee802.org/1/pages/802.1x.html) Authenticator for wired networks,with one of the low-level python networking libraries: [scapy](http://www.secdev.org/projects/scapy/),[http://twistedmatrix.comTwisted.Pair](http://twistedmatrix.comTwisted.Pair),[pycap](http://pycap.sourceforge.net/) or maybe something else.Probably some python firewall bindings will be needed too.

- [PyGame](PyGame) Projects

  - Implement [CodingProjectIdeas/PygameOnCtypes](PygameOnCtypes)

  - Make a pygame plugin for IE, netscape. [CodingProjectIdeas/PythonWebPlugin](PythonWebPlugin)

  - [../PygameGui](./CodingProjectIdeas(2f)PygameGui.html)

  - .[/SimpleNetworkingForPygame](./CodingProjectIdeas(2f)Libraries(2f)SimpleNetworkingForPygame.html)

- Data mining in Python (e.g., adding a new data mining algorithm or tool to the Orange data mining suite, develop a new widget for text mining or 3-D data visualization, develop Orange interface to R or alike, port Orange to Mac OS X, [http://www.ailab.si/orange](http://www.ailab.si/orange))

- Add a wxPython/wax based object browser to the ipipe module which will be part of the next release of [IPython](http://ipython.scipy.org/) (more info on the [IPython wiki](http://projects.scipy.org/ipython/ipython/wiki/GoogleSommerOfCode2006)).

- Implement a pure python library that handles unicode [CLDR](http://www.unicode.org/cldr/). (like ICU?)

- Take an existing set of sources for [M2Crypto](M2Crypto) and build a robust distribution from it. This should include comprehensive API documentation, a full test suite, and providing a better Python interface, not just a light wrapper around openssl, for many of the functions like X.509 certificates that are not currently exposed.

- Work on [SAGE](http://sage.scipy.org/sage/), which is a Python-based free open source computer algebra system. SAGE is the algebraic analogue of [scipy](http://www.scipy.org)\-\--it incorporates and \"glues together\" a wide range of existing open-source mathematics packages such as Maxima, Matplotlib, and GAP. Here\'s a [list of projects](http://sage.scipy.org/sage/projects) and an [email contact](mailto:wstein@gmail.com).

- Conduct a review of one chunk of functionality in [scipy](http://www.scipy.org) similar to the one currently in progress about [the statistics package](http://projects.scipy.org/scipy/scipy/wiki/StatisticsReview). Alternatively, add a chunk of functionality to scipy. Recently discussed requests have been bindings to [SUNDIALS](http://www.llnl.gov/casc/sundials/), sparse matrices in [LAPACK packed storage formats](http://www.netlib.org/lapack/lug/node121.html), 3-D Delaunay tetrahedralization and natural neighbour interpolation, and porting the [Netlab](http://www.ncrg.aston.ac.uk/netlab/index.php) neural network code to scipy.

- Add more plot types to the recently refactored [Chaco](http://code.enthought.com/chaco/) plotting library ([contact](mailto:robert.kern@enthought.com)).

- Make [Traits UI](http://code.enthought.com/traits/) available to Qt, Tk, or GTK applications ([contact](mailto:robert.kern@enthought.com)).

- Help make [IPython\'s](http://ipython.scipy.org/) capabilities available inside a wxPython application.

- Use [Cassowary](http://www.cs.washington.edu/research/constraints/cassowary/) or some other constraint solving library to implement automatic, \"nice\" GUI layout.

- Write general [Pango](http://pango.org/) bindings that can be used by Python libraries to do general text layout outside of PyGTK and pycairo.

- Help merge the codebases of [matplotlib](http://matplotlib.sourceforge.net) and [Chaco](http://code.enthought.com/chaco/) ([contact](mailto:jdhunter@nitace.bsd.uchicago.edu), [contact](mailto:robert.kern@enthought.com)).

- Implement mathematical formula typesetting using TeX algorithms and TeX fonts but without needing a TeX installation.

- [Soya3d](http://www.soya3d.org/wiki/Soya) Projects

  - add multi-texture support (bump/normals mapping, etc)
  - verse support for shapes and materials
  - improved exporters/importers (blender, etc)
  - cal3d per-bone and morph animations
  - improved ode integration
  - api reference and improved examples/tutorials

- Improve [YAML](http://yaml.org/) [support in Python](http://pyyaml.org/), e.g.,

  - make [Python support in Syck](http://pyyaml.org/wiki/PySyck) (C extension) as complete as Ruby\'s

  - make [Syck](http://whytheluckystiff.net/syck/) support Unicode

  - contribute to [PyYAML](http://pyyaml.org/wiki/PyYAML) (pure Python version)

- Review and consolidate libraries/ modules for, e.g., file metadata reading and writing (MS Word doc, PDF, GIF, MP3/ ID3)

- Choose some common modules and [eggsify](http://peak.telecommunity.com/DevCenter/PythonEggs) them; write about it to promote more eggsification

- Extend the [CodeCoverage](CodeCoverage) module to extend into os.fork() and os.exec(\'python\') calls. Fix Nose to facilitate this.

- Write a [scipy](http://www.scipy.org) module that implements black-box, [automatic random number generation](http://statistik.wu-wien.ac.at/projects/arvag/index.html) algorithms for the numerous probability distributions defined in [scipy.stats](http://www.scipy.org/doc/api_docs/scipy.stats.distributions.html) ([contact](mailto:robert.kern@enthought.com)).

- A more complete CD interface. [libcdio](http://www.gnu.org/software/libcdio) is a library for Platform-dependent control and reading of a CD device. There is also some support for reading CD images (BIN/CUE CDRDAO, ISO) as though they were real devices. [Some work](http://freshmeat.net/projects/libcdio/?branch_id=62870) has been done to extend the API to Python, via SWIG. However this OO wrapping is not complete. In particular handling MMC (Multi-media) commands is missing and a CD-Paranoia interface (OO or not) is missing. All of the OO API\'s are fairly new, so if you feel you want to improve on the API, that\'s okay too.

- A python interface to [rabbitmq](http://www.rabbitmq.com/). They have a java interface right now (the engine itself is written in erlang) so you could use it for \"inspiration\".

- Convince/help Trevor Perrin to make a full ssl interface (i.e., make [tlslite](http://sourceforge.net/projects/tlslite) feature complete).

- Implement [Xml Encryption](http://www.w3.org/TR/xmlenc-core/) and [Xml Signature](http://www.w3.org/TR/xmldsig-core/) **using lxml**

  - First iterate on a \"pure\" python prototype (using tlslite or whatever) to create a clean API, and after that use pyrex to bind directly against Aleskey\'s xmlsec package for better performance (maybe both implementations could live together, a la ElementTree/cElementTree and StringIO/cStringIO). Another option is to use something from the [xmlsig project](http://xmlsig.sourceforge.net/).

  - Another try on the quest for a clean API: Use [jsr105](http://jcp.org/en/jsr/detail?id=105) and [jsr106](http://jcp.org/en/jsr/detail?id=106) for a reference (obviously using python idioms instead of the java ones).

------------------------------------------------------------------------

Less fleshed-out ideas:

- An educational programming environment similar to [Boxer](http://dewey.soe.berkeley.edu/boxer.html/index.html) for Python

  - Kind of a visual programming environment, where blocks are translated into \"boxes\" (along with a few other select ideas). One of the more conservative visual programming environments, and it seems very translatable to Python. Or maybe work on a decent programming environment for [PyLogo](http://pylogo.org). *Boxer isn\'t a programming environment. I think this idea isn\'t fleshed out enough.*

    - Having something similar to Simulink would be VERY useful in regards to the visual programming environment.

- A more complete version of Modelica in Python would also be useful [http://www.ercim.org/publication/Ercim_News/enw36/ernst.html](http://www.ercim.org/publication/Ercim_News/enw36/ernst.html) or [http://moncs.cs.mcgill.ca/people/ffan/report.dtml](http://moncs.cs.mcgill.ca/people/ffan/report.dtml)
