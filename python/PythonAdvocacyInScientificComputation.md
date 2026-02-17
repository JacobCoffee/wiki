# PythonAdvocacyInScientificComputation

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page originated as an essay [MichaelTobis](MichaelTobis) posted [http://groups.google.com/group/comp.lang.python/msg/06d6b58b963fa10e](http://groups.google.com/group/comp.lang.python/msg/06d6b58b963fa10e) on Usenet.

------------------------------------------------------------------------

Is there a role for Python in high-performance computing?

The established use of Fortran in continuum models such as climate models has some benefits, including very high performance and flexibility in dealing with regular arrays, backward compatibility with the existing code base, and the familiarity with the language among the modeling community. Fortran 90 and later versions have taken many of the lessons of object oriented programming and adapted them so that logical separation of modules is supported, allowing for more effective development of large systems. However, there are many purposes to which Fortran is ill-suited which are increasingly part of the modeling environment.

These include: source and version control and audit trails for runs, build system management, test specification, deployment testing (across multiple platforms), post-processing analysis, run-time and asynchronous visualization, distributed control and ensemble management. To achieve these goals, a combination of shell scripts, specialized build tools, specialized applications written in several object-oriented languages, and various web and network deployment strategies have been deployed in an ad hoc manner. Not only has much duplication of effort occurred, a great deal of struggling up the learning curves of various technologies has been required as one need or another has been addressed in various ad hoc ways.

A new need arises as the ambitions of physical modeling increase; this is the rapid prototyping and testing of new model components. As the number of possible configurations of a model increases, the expense and difficulty of both unit testing and integration testing becomes more demanding.

Fortunately, there is Python. Python is a very flexible language that has captured the enthusiasm of commercial and scientific programmers alike. The perception of Python programmers coming from almost any other language is that they are suddenly dramatically several times more productive than previously, in terms of functionality delivered per unit of programmer time.

One slogan of the Python community is that the language \"fits your brain\". Why this might be the case is an interesting question. There are no startling computer science breakthroughs original to the language, Rather, Python afficionados will claim that the language combines the best features of such various languages as Lisp, Perl, Java, and Matlab. Eschewing allegiance to a specific theory of how to program, Python\'s design instead offers the best practices from many other software cultures.

The synergies among these programming modes is in some ways harder to explain than to experience. The Python novice may nevertheless observe that a single language can take the place of shell scripts, makefiles, desktop computation environments, compiled languages to build GUIs, and scripting languages to build web interfaces. In addition, Python is useful as a wrapper for Fortran modules, facilitating the implementation of true test-driven design processes in Fortran models.

Another Python advocacy slogan is \"batteries included\". The point here is that (in part because Python is dramatically easier to write than other languages) there is a very broad range of very powerful standard libraries that make many tasks which are difficult in other languages astonishingly easy in Python. For instance, drawing upon the standard libraries (no additional download required) a portable webserver (runnable on both Microsoft and Unix-based platforms) can be implemented in seven lines of code. (See [http://effbot.org/librarybook/simplehttpserver.htm](http://effbot.org/librarybook/simplehttpserver.htm) ) Installation of pure python packages is also very easy, and installation of mixed language products with a Python component is generally not significantly harder than a comparable product with no Python component.

Among the Python components and Python bindings of special interest to scientists are the elegant and powerful matplotlib plotting package, which began by emulating and now surpasses the plotting features of Matlab, SWIG, which allows for runtime interoperability with various languages, f2py which specifically interoperates with Fortran, NetCDF libraries (which cope with NetCDF files with dramatically less fuss than the standard C or Fortran bindings), statistics packages including bindings to the R language, linear algebra packages, various platform-specific and portable GUI libraries, genetic algorithms, optimization libraries, and bindings for high performance differential equation solvers (notably, using the Argonne National Laboratory package PetSC). An especially interesting Python trick for runtime visualization in models that were not designed to support it, pioneered by David Beazley\'s SWILL, embeds a web server in your model code.

See especially [http://starship.python.net/\~hinsen/ScientificPython/](http://starship.python.net/~hinsen/ScientificPython/) and [http://scipy.org](http://scipy.org) as good starting points to learn about scientific uses of Python.

------------------------------------------------------------------------

[JuhoSchultz](./JuhoSchultz.html) followed up, \"A slight broadening of the perspective could show another advantage: Python is also used for data processing, at least in astronomy. Modeling and processing the data in the same environment is very practical. Spend more time on modeling and processing the critical data sections - critical data section may depend on model parameters and sampling (which is often incomplete and uneven). You also avoid wasting CPU cycles to model things not in the data.

A theorist may be perfectly happy with Fortran, and an observer could do his stuff with simple scripts. But if they need to work together, Python is a very good option.\"

[PeterTillotson](./PeterTillotson.html) added, \"\... an area that doesn\'t come out strongly enough for me is Python\'s ability to drop down to and integrate with low level algorithms. This allows me to to optimise the key bits of design in python very quickly and then if I still need more poke i can drop down to low level programming languages. Optimise design, not code unless I really need to.

To be fair the same is at least partly true for Java ( though supporting JNI code scares me ) but my prototyping productivity isn\'t as high.

The distributed / HPC packages may also be worth noting - PyMPI and [PyGlobus](./PyGlobus.html).\"

[CameronLaird](CameronLaird) focused on a few details in a follow-up [http://groups.google.com/group/comp.lang.python/msg/39906e2430f72925](http://groups.google.com/group/comp.lang.python/msg/39906e2430f72925)

comp.lang.fortran responded to the essay in a long and contentious thread [http://groups.google.com/group/comp.lang.fortran/browse_thread/thread/e772dd0847d445c/](http://groups.google.com/group/comp.lang.fortran/browse_thread/thread/e772dd0847d445c/) that brought out needs for specific explanations of Python\'s advantages in testing, as well as differential affection for Ruby (!).

\'Python Scripting for Computational Science\' by Hans Petter Langtangen is a good introduction to Python for scientific computing. Its early chapters also have good explanatory material for scientists considering expanding their toolkit to include a dynamic scripting language like Python. [http://folk.uio.no/hpl/scripting/](http://folk.uio.no/hpl/scripting/)

I (the original author of the article) added an introductory sentence at the top, to clarify the intended original audience for the article. Many of the points here also apply to the individual researcher doing one-off coding, but a few do not. Perhaps that should be in a separate article, or perhaps in a rewrite.
