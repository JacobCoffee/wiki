# PythonCdToDo

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

For improving the [PythonCd](PythonCd), we need some experienced helpers and testers, so if you are interested, please join in here! If you know how to make debian packages (or where to find them), provide some hints where to get the stuff not yet installed.

Current package list: [PythonCdRawPackageList](PythonCdRawPackageList)

# Software 

- [PyGeo](PyGeo)

- VPython

# Graphics and Fun stuff 

- images and logos
  - pythonic background image, see [http://www.ibiblio.org/obp/pyBiblio/images/](http://www.ibiblio.org/obp/pyBiblio/images/) - snake.png - thanks to Paul Carduner

    - needs to get 1024x768, so that snake is aligned top right (bsetbg command cant align top right)

  - lilo boot image - maybe derived from [http://www.ibiblio.org/obp/py4fun/](http://www.ibiblio.org/obp/py4fun/) ?

  - logo for top left of local moinmoin wiki

- that \"introducing python\" mpeg (250MB) is much too big to fit on the [PythonCd](PythonCd) (on a DVD, it would fit, of course ![;)](/wiki/europython/img/smile4.png ";)") - does anybody have a smaller version with acceptable quality? target should be 25..100MB.

  - [KevinAltis](KevinAltis) made a smaller version of the movie, but it is Quicktime, so that wouldn\'t work.

    - [http://www.python.org/other/python.mov](http://www.python.org/other/python.mov) - tried it, but using xine or vlc, I only get video, but no audio 8( vlc seemed to have less problems, xine sometimes didnt work.

# Hosting / Mirrors for ISO image distribution 

We need some server to distribute this, anybody sponsoring space and bandwidth? Possibilities:

- ![(./)](/wiki/europython/img/checkmark.png "(./)") Uni Erlangen - Currently this is the primary site, see [PythonCdDownload](PythonCdDownload).

- starship.python.net (acceptable use?)

- python.org (\"when it is ready\").

- Also, we could create a bittorrent file for the ISO image to ease server bandwidth. And find some CD pressing service that lets people purchase a copy of the CD by mail for only a few bucks.
  - for bittorrent we need a tracker AFAIK, starship.python.net maybe?
  - then, the people taking part in development could keep just their torrent client running

- [ToDo](./ToDo.html): maybe somebody else could contact some University in the US/Canada? Just check if it is possible to mirror the ISO there.

# Unsorted / Todo from EducationalCd 

- [Zope](Zope) and [ZODB](http://zope.org/Wikis/ZODB/FrontPage/)

  - requires a zope geek or it rather won\'t be done

- [Applications](Applications) (written in Python)

  - [GuidovanRobot](GuidovanRobot) (GvRobot)

  - [WorkforceConnections](./WorkforceConnections.html) (courseware through a web interface.)

  - Chandler

  - Shtoom

  - [QuantLib](./QuantLib.html) ([http://quantlib.sourceforge.net/](http://quantlib.sourceforge.net/)) - does this make sense on a bootable CD?

  - PyAC \# album creator

- [PyGE](PyGE) (maybe rather wait until it is easier to handle)

There are some ready to go apps like

- library automation
- Plone based school setup

that may show something good out of the box. \-- [MikeRovner](MikeRovner) 2004-04-09 18:59:28

TODO: move to [PythonCdPackages](PythonCdPackages) after installing on CD master (see comment at bottom of that page)

- wxGlade [http://mentors.debian.net/debian/pool/main/w/wxglade/](http://mentors.debian.net/debian/pool/main/w/wxglade/)

  - Mail tinuviel at sparcs.kaist.ac.kr if you have any questions.

- deutsche Uebersetzung des Python Tutorials [http://starship.python.net/crew/gherman/publications/tut-de/](http://starship.python.net/crew/gherman/publications/tut-de/)
