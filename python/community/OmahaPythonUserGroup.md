# OmahaPythonUserGroup

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The Omaha Python User Group was restarted in early 2007. It is composed of local developers (both newbies and experienced) who enjoy learning more about their favorite language and meeting up with other Python programmers.

Our wiki page is here and the mailing list is here: [python.org-hosted mailing list](http://mail.python.org/mailman/listinfo/omaha).

------------------------------------------------------------------------

**Table of Contents:**

### Contact Information 

- Mail list: [http://mail.python.org/mailman/listinfo/omaha](http://mail.python.org/mailman/listinfo/omaha)

- Web Site: [www.OmahaPython.org](http://www.OmahaPython.org)

- Meeting Schedule via Google Calendar: [http://www.google.com/calendar/render?cid=epouplrdducr6atraggiflnfeg%40group.calendar.google.com](http://www.google.com/calendar/render?cid=epouplrdducr6atraggiflnfeg%40group.calendar.google.com)

### Next Meeting 

We meet the First Wednesday of the Month.

- November 7, 2007 - 7pm
  - Topics:
    - Lightning Talks
    - TBA
    - Group Q and A session

    Location:
    - Clancy\'s East\
      7128 Pacific Street (72nd & Pacific)\
      Omaha, NE

    Refreshments:
    - It\'s Clancy\'s \-- so food and drink will be available.

    Door Prize(s)?:
    - ??

### Topic ideas for future events 

**Topic suggestions:**\

- To Be Announced

**Topics you\'re willing to speak about (with speaker identified):**\

- pygame (Aaron Grothe)
- pythoncard (Aaron Grothe)

### Past Meetings 

**October 3, 2007**\
The gathering stayed strong again this month with 2 new people joining in the fray. A presentation on mod_python, publisher and psp was given while pizza was eaten. (Funny thing about having good pizza in an Irish pub\<g\>)

Talk then went on about using python in sysadmin tasks and then on to how best to setup some massive home storage. GlusterFS , ZFS and NFS.

- We all seem to have a need for terra type storage\<g\>

A copy of \"The Python Cookbook\" was handed out to the winner of the door prize (Thanks O\'Reilly)

After the meeting a social hour(s) ensued with wild eyed talk of google phones and grand central.

We look forward to seeing old friends and new faces at the next meeting. Details are on the website, www.[OmahaPython](./OmahaPython.html).org .

**September 5, 2007**\
Well we\'ve managed to maintain a new meeting attendance level. There were 6 of us again tonight at the meeting, 5 alumni and 1 new attendee. The meeting started out with some introductions and talk about Py3K alpha. We then turned to talk about the various python implementations C, Iron, Jython and [ActiveState](ActiveState)\'s.

Talk then turned to available windowing options and what exactly was built-in for python as opposed to 3rd party libraries. [PythonCard](./PythonCard.html), [http://pythoncard.sourceforge.net/](http://pythoncard.sourceforge.net/), is the project I was trying to recall. While not a windowing kit \-- it is based on wxPython, it offers a nice entry point in to building a client GUI for a python project for those new to python and GUI kits.

There were some random topics brought up and answered as we munched on some quite good pizza.

We then broke out some code for the pyorhythms, [https://bitbucket.org/dundeemt/pyorhythms](https://bitbucket.org/dundeemt/pyorhythms), group project. We talked about how the imports had been laid out, the over all structure of the program and a number of questions from those new to python were asked. What are those triple commented things (docstrings, [http://www.diveintopython.org/getting_to_know_python/documenting_functions.html](http://www.diveintopython.org/getting_to_know_python/documenting_functions.html)) how are they used, etc.

We then talked about the use of map statements and what was going to happen to them in Py3K. Someone asked what does reduce do, and I didn\'t have an answer then as I hadn\'t used it before, but have one now

\"reduce(function, sequence)\" returns a single value constructed by calling the binary function function on the first two items of the sequence, then on the result and the next item, and so on. For example, to compute the sum of the numbers 1 through 10:

\>\>\> def add(x,y): return x+y \... \>\>\> reduce(add, range(1, 11)) 55

- see [http://docs.python.org/tut/node7.html#SECTION007130000000000000000](http://docs.python.org/tut/node7.html#SECTION007130000000000000000)

I did a live demonstration of pyorhythms and there was some pleasant smiles and nods at seeing how well pylab, [http://matplotlib.sourceforge.net/](http://matplotlib.sourceforge.net/), graphed everything.

At the end of the meeting we handed out the door prize, \"Beautiful Code.\"

After the meeting some of stuck around and pondered the architecture of the google file system,[http://en.wikipedia.org/wiki/Google_File_System](http://en.wikipedia.org/wiki/Google_File_System), why doesn\'t google offer a google apps appliance? and the possible ramifications of Grand Central, [http://grandcentral.com/home](http://grandcentral.com/home), and the rumored google phone, [http://www.sltrib.com/business/ci_6803112](http://www.sltrib.com/business/ci_6803112).

For those of you who couldn\'t attend we hope to see you next month (Brad et al)

**July 12, 2007**\
The meeting opened up with lots of interesting rumors, speculation and general kibitzing about Google\'s plans for the new CB location. Who knows for sure \-- but lots of fun in the mean time.

Jeff gave a presentation on Crunchy ([http://crunchy.sourceforge.net/](http://crunchy.sourceforge.net/)) Talk about a gee whiz app. We poked at it with sticks and xkill ([http://www.xfree86.org/current/xkill.1.html](http://www.xfree86.org/current/xkill.1.html)) to figure out how/who had control of the tkinter/wx/gtk windows.

The graphics capabilities brought out some questions about graphing packages available to Python. Jeff recalled a recent blog entry by Fuzzyman a.k.a Michael Foord ([http://www.voidspace.org.uk/python/weblog/](http://www.voidspace.org.uk/python/weblog/)) about him looking for a graphing package to use with [IronPython](IronPython) ([http://www.voidspace.org.uk/python/weblog/arch_d7_2007_06_23.shtml#e753](http://www.voidspace.org.uk/python/weblog/arch_d7_2007_06_23.shtml#e753)). A bit of googling and gnuplot ([http://gnuplot.info/](http://gnuplot.info/)) was found.

Next was a question about xml parsers from someone new to Python and while no one was definitive, we suggested that they look at elementtree ([http://docs.python.org/lib/module-xml.etree.ElementTree.html](http://docs.python.org/lib/module-xml.etree.ElementTree.html)) and lxml ([http://lxml.de/](http://lxml.de/))

The conversation then drifted towards web development. We had a java programmer in the group who has been recently been using Django ([http://www.djangoproject.com/](http://www.djangoproject.com/)) and is becoming enamored with Python. We gabbed about storm ([https://storm.canonical.com/](https://storm.canonical.com/)) and news about how the [TurboGears](TurboGears) had started implementing TG2 ([http://www.blueskyonmars.com/2007/06/27/turbogears-2-a-reinvention-and-back-to-its-roots/](http://www.blueskyonmars.com/2007/06/27/turbogears-2-a-reinvention-and-back-to-its-roots/)) as an abstraction on top of Pylons ([http://pylonshq.com/](http://pylonshq.com/)). There was also talk of mod_wsgi ([http://www.modwsgi.org/](http://www.modwsgi.org/)) and how it is different than mod_python ([http://www.modpython.org/](http://www.modpython.org/)). Jeff shared a little bit about mod_wsgi\'s embedded and daemon modes he had picked up from Graham\'s recent blog entry ([http://blog.dscpl.com.au/2007/07/web-hosting-landscape-and-modwsgi.html](http://blog.dscpl.com.au/2007/07/web-hosting-landscape-and-modwsgi.html)).

The talk then veered in to lambda ([http://docs.python.org/ref/lambdas.html](http://docs.python.org/ref/lambdas.html)) and the java types whispered \"anonymous\" \<g\> This quickly veered in to discussion on how binding ([http://docs.python.org/ref/naming.html](http://docs.python.org/ref/naming.html)) operates, which lead to an impromptu demonstration of passing a function as an argument to a function and how you assign a function to a dictionary element.

    >>> def f(x):
    ...     return x*x
    ... 
    >>> print f(2)
    4

    >>> def g(fn,x):
    ...   return apply(fn,[x])
    ... 
    >>> g(f,2)
    4

    >>> d={}
    >>> d['foo']=f
    >>> print d['foo'](2)
    4

As the meeting came to a close, we decided to change the meeting time from the 2nd Thursday of the month to the 1st Wednesday of the month. In the case that a holiday coincides with or is immediately adjacent to that day, the meeting will be held 1 week later on the second Tuesday. There was also a motion to move the meeting location and two locations were put up for consideration:

- Scooter\'s Java Express @ 120th and Blondo
- Student Union @ UNO\'s campus, 60th and Dodge

We will investigate these two locations and report back to the list for a vote by early next week.

Brad S. won the Door Prize of \"Python in a Nutshell, 2nd Edition\". Tom never contacted us to pick it up so he lost out from last month. Sorry Tom.

Thanks and appreciation to Jay and Reboot The User for donating the meeting space and Dundee Media & Technology, Inc. for the pizza and pop.

**June 14, 2007**\
Another banner meeting occurred this evening. Although it was a bit warm there were some cool conversations going on at the meeting tonight. There were questions and talk about, targeting win32, :

- ctypes - [http://python.net/crew/theller/ctypes/](http://python.net/crew/theller/ctypes/)) win32all - [http://sourceforge.net/project/showfiles.php?group_id=78018](http://sourceforge.net/project/showfiles.php?group_id=78018)

database:

- db api - [http://www.python.org/dev/peps/pep-0249/](http://www.python.org/dev/peps/pep-0249/) sqlalchemy - [http://www.sqlalchemy.org/](http://www.sqlalchemy.org/)

packaging:

- py2exe - [http://www.py2exe.org/](http://www.py2exe.org/) cx_freeze - [http://python.net/crew/atuining/cx_Freeze/](http://python.net/crew/atuining/cx_Freeze/) distutils - [http://www.python.org/community/sigs/current/distutils-sig/](http://www.python.org/community/sigs/current/distutils-sig/) easy_install - [http://peak.telecommunity.com/DevCenter/EasyInstall](http://peak.telecommunity.com/DevCenter/EasyInstall)

UI:

- wxPython - [http://www.wxpython.org/](http://www.wxpython.org/) pythoncard - [http://pythoncard.sourceforge.net/](http://pythoncard.sourceforge.net/)

Web:

- django - [http://www.djangoproject.com/](http://www.djangoproject.com/) turbogears - [http://www.turbogears.org/](http://www.turbogears.org/) pylons - [http://pylonshq.com/](http://pylonshq.com/) mod_python - [http://www.modpython.org/](http://www.modpython.org/) cheetah - [http://www.cheetahtemplate.org/](http://www.cheetahtemplate.org/)

Jeff gave a short presentation on the subprocess module [http://docs.python.org/dev/lib/module-subprocess.html](http://docs.python.org/dev/lib/module-subprocess.html) The slides and example code are available on the website. [http://www.omahapython.org/](http://www.omahapython.org/) He also gave a little demo of his current internal project showing off subprocess, mod_python and pyRSS2Gen.

There was also a round of talk about using python as a tool to target multiple platforms at once, giving the user leverage to move between those platforms as they see fit. Also the ability of python to leverage existing code and services. A number of the attendees illustrated this topic by talking about how they are using python to build on existing resources and integrate systems on the application and OS level. It is interesting to see Python being used in banks and hospitals.

As with previous meetings, kudos to Jay and Reboot The User for graciously donating the space for the gathering. Pizza and Pop sponsored by DM&T.

The door prize winner tonight, Todd, will receive \"Python in a Nutshell, 2nd Edition\" courtesy of O\'Reilly. Unfortunately I left the house in such a rush tonight, that I didn\'t remember to bring it along. Todd, if you are going to be at the OLUG East luncheon Friday, I will have it with me and you can get it there. Otherwise, email me off list and we can make arrangements to get it to you pdq.

Mark your calendars early, July 12, and don\'t miss out on the fun. Here is gCal link so you can add it to your calendar. [http://www.google.com/calendar/render?cid=epouplrdducr6atraggiflnfeg%40group.calendar.google.com](http://www.google.com/calendar/render?cid=epouplrdducr6atraggiflnfeg%40group.calendar.google.com)

We\'ll be giving away something for a door prize. There will be food and drink and hopefully many more \"lightning\" talks about projects by local python developers.

**May 10, 2007**\
Well now, that was quite a meeting. We ended up not talking about any of the announced subjects so it was a very good meeting. Eli made an appearance tonight [http://eli.criffield.net/](http://eli.criffield.net/) and for a sysadmin who doesn\'t \"program\", Eli has produced some pretty interesting python projects. sipie [http://freshmeat.net/projects/sipie/](http://freshmeat.net/projects/sipie/), Pronounced SY PIE, like \"sirius python\", sipie is a command line player for Sirius online Internet streaming

We also talked about using private certs and CA\'s, the different python based packages and use them with the twisted framework[http://twistedmatrix.com/trac/](http://twistedmatrix.com/trac/). Eli hammered out the details and did something with twisted that not many knew was possible. Thanks for sharing \-- Very Cool.

As with previous meetings, kudos to Jay and Reboot The User for graciously donating the space for the gathering. The new executive conference room is nearing completion \-- we will be stylin\' then. Also, props to Todd for covering the pizza guy before I got there. Pizza and Pop sponsored by DM&T.

And finally, thanks to O\'Reilly (Marsee) for the great door prize. Eli won the door prize, \"Programming Python\" by Mark Lutz.

**April 12, 2007:**\
First Off, a big thank you to Jay and Reboot The User for allowing us to have our meeting at Reboot The User. It worked out very well - nice seeing your code on a 50\" display! Jay also supplied the Internet access too.

While the meeting was small, I consider it to be successful. We talked a little bit about [PyCon](PyCon) and then moved on to the email2rss project. There was discussion on the two major packages used, libgmail and PyRSS2Gen module. You can see the outcome of the email2rss.py project at [http://www.dundeemt.com/rss/omaha-rss.xml](http://www.dundeemt.com/rss/omaha-rss.xml) Which is a RSS feed of the User Group mail list.

Other elements of the project discussed were:

- slices
- pickle module
- option parsing
- pylint
- editors (Komodo Edit/IDE and SciTE)

There was an open discussion about python in the work place. The consensus seemed to be small skunk-work projects were ideal for introducing the language. Python\'s ability to sling data and ability to integrate with sysadmin type scripts make it ideal for this type of assault.

The wiki, mailing list and flyer were shown. Until the need presents itself, we will continue to use the resources provided by the PSF. In fact, there is an effort through the Python Advocacy group to enhance user group resources. Go Advocacy!

There was discussion of the rumored Google-Plex / Council Bluffs. It was agreed that this would be a good thing for the metro IT community if it is true. Council Bluffs, IA sits across the Missouri River from Omaha. A number of our members work in Council Bluffs.

Pizza and Pop were provided by Dundee Media & Technology. Be sure to mail the list with requests for toppings and flavors for the next meeting, as DM&T will sponsoring the food and beverages for the meeting.

### Meeting Flyers 

Meeting flyers are a great way to get the word out about the meetings. Please post them (with proper approval) in places that might be frequented by past, present or future Python users.

[OmahaPythonUserGroupFlyerWithTearAways.pdf](attachments/OmahaPythonUserGroup/OmahaPythonUserGroupFlyerWithTearAways.pdf)

### Meeting Presentations 

June 14, 2007 - subprocess module slides: [SubprocessSlides-20070614.tar.gz](attachments/OmahaPythonUserGroup/SubprocessSlides-20070614.tar.gz)

------------------------------------------------------------------------

[CategoryUsergroups](CategoryUsergroups)
