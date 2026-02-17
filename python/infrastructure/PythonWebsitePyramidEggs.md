# PythonWebsitePyramidEggs

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Egg Install Guide 

I\'ve found that the simplest way is by using Philip Eby\'s easy_install

1\) download [http://peak.telecommunity.com/dist/ez_install-0.3a3-py2.4-unix.sh](http://peak.telecommunity.com/dist/ez_install-0.3a3-py2.4-unix.sh)

2\) rename it easy_install and place it on your path

3\) easy_install [http://peak.telecommunity.com/dist/setuptools-0.3a3-py2.4.egg](http://peak.telecommunity.com/dist/setuptools-0.3a3-py2.4.egg)

That gets your setuptools and easy_install going

4\) easy_install [http://pyramid.pollenation.net/download/pysyck-0.45_pyx-py2.4-linux-i686.egg](http://pyramid.pollenation.net/download/pysyck-0.45_pyx-py2.4-linux-i686.egg)

and you should be done\...

# Further Eggs\'perimentation 

If you want to try installing everything from eggs, you\'ll have a few problems - I hope these can get sorted as they could make installing and dependencies etc,. a painless process I\'m looking forward to when I can do \'easy_install pyramid\' and all dependencies follow ![:-)](/wiki/europython/img/smile.png ":-)") .. I think docutils should work but I\'ve not built a roman egg for it yet. Twisted 2 and Zope Interfaces definitely don\'t work so you\'ll have to build those from source. Pyramid also doesn\'t work as it requires a script (which eggs will support soon I believe).

easy_install [http://pyramid.pollenation.net/download/docutils-0.3.10-py2.4.egg](http://pyramid.pollenation.net/download/docutils-0.3.10-py2.4.egg) (this needs the roman module which I haven\'t built an egg for or tested yet)

easy_install [http://pyramid.pollenation.net/download/nevow-0.4.1-py2.4.egg](http://pyramid.pollenation.net/download/nevow-0.4.1-py2.4.egg)

Pyramid installs but doesn\'t copy the scripts out\... this could be fixed soon but for now install from source

easy_install [http://pyramid.pollenation.net/download/pyramid-0.1-py2.4.egg](http://pyramid.pollenation.net/download/pyramid-0.1-py2.4.egg)

not sure about twisted yet from what I\'ve seen twisted doesn\'t currently work (has a zope dependency and zope can\'t be built as an egg yet, twisted needs scripts also.)

[http://peak.telecommunity.com/DevCenter/EasyInstall](http://peak.telecommunity.com/DevCenter/EasyInstall)
