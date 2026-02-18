# PyQt/EuroPython2006Talk

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Authors: Torsten Marek, *David Boddie*

## Introducing PyQt4 for GUI Application Development 

- *We decided to use this title [for the official submission](http://indico.cern.ch/contributionDisplay.py?contribId=33&sessionId=41&confId=44).*

- *[Abstract and Slides](http://indico.cern.ch/contributionDisplay.py?contribId=33&sessionId=41&confId=44)*

### Status 

*Submitted the talk, presented it, and uploaded slides.*

### Abstract 

[PyQt4](../../../gui/PyQt4) is a set of bindings for Qt 4, a cross-platform C++ framework used to make graphical user interface (GUI) applications. With the release of [PyQt4](../../../gui/PyQt4), Python developers are now able to develop powerful cross-platform applications and deploy them under the GNU General Public License (GPL) or the Qt Commercial License on all platforms that support Qt and Python.

We will first briefly discuss [PyQt](../../../gui/PyQt) (for Qt 3) and PyKDE (bindings for the K Desktop Environment), and take a look at what has changed in [PyQt4](../../../gui/PyQt4). The main part of the presentation will cover the new possibilities that [PyQt4](../../../gui/PyQt4) offers developers, including access to Qt\'s rich text handling features, sophisticated data handling controls, internationalization support, and integration with the Qt Designer GUI design tool.

Remarks:

- *Have I over-engineered the opening sentence? :-)*

- *Should we just submit something like this and fine-tune it later?*

- I don\'t know how many \"commercial\" people will be there, maybe we should stress that it\'s possible to deploy it under a commercial license as well.

- *Both licenses are mentioned now.*

### Thoughts 

I\'m not completely sure whom to target. Judging from the fact that this is a Python conference, we should probably put emphasis on the Python part and not on the compatibility between [PyQt](../../../gui/PyQt) and Qt/C++. I think there\'s no need to actually win somebody for Python.

- advantages of using Python\'s native data types and all extension modules with Qt (less programming sit-ups)
  - *Yes, this is part of what makes using [PyQt](../../../gui/PyQt) (rather than Qt on its own) interesting to many people, though we\'ve already said that this is a Qt for Python talk, not a Python for Qt talk. ;-)*
- wrapping own C++ widgets with sip?
  - *Maybe a bit specialized for a general talk.*
- are we going to use real-world programs or write the examples ourselves?
  - *A bit of both, I think. See the Demos and Examples section.*

*I think we\'re trying to answer the question, \"Why use [PyQt](../../../gui/PyQt) to create applications?\" rather than, \"Why use Python to write Qt applications?\" The latter question would form the basis of a talk I should give to my colleagues. ;-)*

- maybe make a small comparison with other GUI toolkits - better look on Win32 than Gtk, no non-native widgets on Linux as wx has

- *I want to try and avoid making this sort of comparison, or at least making it part of the talk. I suspect that there will be fans of these toolkits at [EuroPython](../EuroPython), and would rather not spend too much time arguing with them. :-)*

*One way to approach this is to ask, \"What advantages does [PyQt](../../../gui/PyQt) give Python developers? Which features are particularly special or interesting?\"*

### Introduction 

*General features of Qt and [PyQt](../../../gui/PyQt):*

- *Cross-platform - Not just Linux, Windows and Mac OS X, but Windows 9x to XP, various Unix variants, Linux, and Mac OS X. Also available as Qtopia Core on embedded Linux.*

- *Dual licensed*

### Topics 

*I think it would be good to split the talk into sections. Apart from the review part, which could just show things like examples of [PyQt](../../../gui/PyQt) applications and Python applications in KDE, the second part could also be split into interesting topics that are accompanied by examples.*

*Taking the [Qt 4 Whitepaper](http://www.trolltech.com/products/qt/learnmore/whitepapers) as inspiration, and trying not to turn this into some kind of marketing document, the key points are:*

- *Widgets, layouts and styles*

  - *The range of widgets available is worth mentioning, as is the native look and feel provided by the style system.*

  - *It would be good to mention event-handling, while recognizing that it isn\'t necessarily a central feature for certain kinds of users.*

  - *Although I\'m not sure how useful is is, I think we can say that [PyQt](../../../gui/PyQt) is not really much less \"Pythonic\" than other frameworks. Writing Qt applications in C++ is quite a Pythonic experience in itself these days.*

- *Standard GUI features + internationalization*

  - *Main window application paradigm is supported, but there are plenty of opportunities for applications to follow other paradigms.*

- *Signals and slots, meta-objects and properties*

  - *Not everyone knows about signals and slots. Some other frameworks still use callbacks.*

  - *Preview of Python to meta-object system integration.*

  - Stress that all the programming sit-ups required for Qt/C++ are not needed for [PyQt4](../../../gui/PyQt4), at little or no loss

- *Graphics features*

  - *Transparency, anti-aliasing, accelerated rendering and SVG support are all attractive features to a lot of people. Given that [PyQt](../../../gui/PyQt) makes these available to Python users on a wide variety of platforms, I think it\'s worth showing off these features.*

  - *Fortunately, there are lots of nice examples and demos available, though many could be even nicer. ![:-)](/wiki/europython/img/smile.png%20":-)") Some of these need to be ported to Python.*

- *Rich text and printing support*

  - *I really need to write some examples to really show off the new API for rich text editing.*

  - *Features like PDF printing support will be interesting to a lot of people.*

- *Database support and item views*

  - *These are only linked together because there are database models in Qt 4.*

  - *Going into any kind of detail for the model/view architecture isn\'t feasible. The database examples help people see the value of the model/view approach.*

  - Maybe we could write sth. like QSqlTableModel for a DBAPI-Module

  - *Perhaps, yes. Or find a non-SQL database to use as a backend.*

- *Tools - Designer, Linguist and Assistant*

  - *The people want to see Designer. ;-)* - Too bad that using Python widgets in Designer doesn\'t work yet, but we can demonstrate how to use them anyway

    - *They work for me, but I had to patch [PyQt](../../../gui/PyQt) to get that behaviour. I can send you the patch scripts if you want. I need to work on that again to make it less of a hack.*

  - *Linguist satisfies a need that many people don\'t realise they have. There are Python versions of the translation tools.*

  - *Assistant comes with Qt documentation, but you can use it to host your own documentation. The QAssistantClient class can also be used to provide online help.*

- *Input/output and networking*

  - *[PyQt](../../../gui/PyQt)\'s networking classes probably aren\'t compelling for many Python users. However, classes like QProcess and the XML classes are more useful than many people probably realise. The [QtDom](./QtDom.html)\* classes provide a DOM interface that\'s a lot faster than minidom, for example.* Wrt to XML, I stay clear from anything that has DOM in its name - for Python, [ElementTree](../../../people/ElementTree) is a far better API

  - *I guess that\'s true for many people. It would be interesting to compare the QDom classes with (c)[ElementTree](../../../people/ElementTree) in terms of performance, but probably not interesting for this kind of talk.*

- *Other features*

  - *The resource system will be interesting to some people.*

  - *Cross-platform support for threading is valuable, but Python already has a usable API for that.*

  - I find Qt4 (even compared to Qt3) to have a very consistent, so your intuitions are right if you know the principal guidelines of the framework

***The problem with this approach is that it doesn\'t really point out the fundamental features that make Qt different, or at least provide the basic architectural foundations, such as layouts, signals and slots, and support for internationalization. Unfortunately, I think the alternative approach would be fairly dry and technical, and would probably be more appropriate for training material.***

### Demos and Examples 

*I think we should carefully look at what\'s already available, especially for [PyQt4](../../../gui/PyQt4), before spending time creating new demos and examples. The [PyQt4Examples](./PyQt4Examples.html) page shows what\'s been ported from C++, though there are a few more examples that aren\'t quite finished, and the Qt snapshots contain more recent ones as well.*

*Visually appealing and/or interesting Qt/PyQt examples:*

- *puzzle (either drag and drop or item view)*

- *application (or one of the other main window examples)*

- *? (a networking example)*

- *? (an OpenGL example)*

- *painterpaths*

- *svgviewer*

- *orderform (or something more impressive) and syntaxhighlighter*

- *mandelbrot (maybe with improvements)* - needs speed-up (or my laptop is too slow)

  - *I think it needs to have the speed-critical parts rewritten in C++, and that kind of misses the point. Perhaps we could choose a better example. :-)*

- *plugandpaint (perhaps too strange for a Python example and may require infrastructure work)*

- *charactermap*

- *imageviewer*

- *screenshot (and/or another example for KDE)*

- *scribble*

- *dombookmarks*

### Things We Missed Out 

*I still need to finish writing sections about databases, OpenGL and internationalization. I think it\'s probably too optimistic to hope that we\'ll get everything mentioned here into the talk.*
