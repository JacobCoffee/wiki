# PydotorgRedesign

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Why? 

**Note:** Much of this has been done. See [PythonWebsite](../infrastructure/PythonWebsite) for ongoing work on content and tools for the python.org website.

During [PyCon](../conferences/pycon/PyCon) 2003 the need to make changes to python.org was clearly identified. See [PythonOrgWebsiteRedesignOpenSpace](../archive/PythonOrgWebsiteRedesignOpenSpace).

The overhaul is taking place in (at least) two phases, as detailed below. The phases are not set in stone, items can and should be moved around as necessary.

## Phase 1 

Primary goal is to quickly improve the site\'s basic usability:

- Reduce some of the duplication (Summary vs. Intros, Events.html vs /conferences/) (Done, pretty much)
- Improve usability from the standpoint of very inexperienced people who get directed to python.org. (The site is probably OK for experienced users.)
- Improve usability of the exceedingly busy top page. If a new graphic design is necessary to get that done, so be it. (Some simplification has been made, but it\'s still awfully crowded.)
- Fix the egregiously bad/outdated parts (the FAQ) (done)
- Simplified search on front page (done)

## Phase 2 

Currently, it is largely unknown what will happen during this phase but here are some possibilities:

- Complete redesign of the site including graphic design, structure and navigation. The focus should be on making the site more obvious to use (particularly for beginners), make it look more \"professional\".
- Content management to reduce the load on the webmasters. (Site mirroring needs to be seriously considered.)
- User comments for documentation.

# Home Page Mockups 

- Mockups from Pollenation [A web design & development company from Yorkshire, the spiritual home of \'Monty Python\', allegedly](http://pollenation.net)

  - [supports text resizing](http://www.pollenation.net/assets/public/index_rounded.html) ([screenshot](http://www.pollenation.net/assets/public/design2.gif))

  - [Collapsible using javascript/DOM](http://www.pollenation.net/assets/public/index_collapsible.html)

  - [Collapsible via multiple pages](http://www.pollenation.net/assets/public/index_about.html)

  - [HTML 6.1KB for page (22.9KB total)](http://www.pollenation.net/assets/public/index.html)([screenshot](http://www.pollenation.net/assets/public/design1.gif))

  - [Revised](http://www.pollenation.net/assets/public/python_pollen_2.gif)

  - [Original](http://www.pollenation.net/assets/public/python_pollen.gif)

  - [Tim\'s notes on the redesign](http://www.pollenation.net/assets/public/redesign-notes.txt)

  - [early design idea](http://pollenation.net/assets/public/python3.html)

  - [another early idea](http://pollenation.net/assets/public/p4.png)

  - [early \'monty\' idea](http://pollenation.net/assets/public/treatment/pythonweb.png)

  - [PNG image of home page idea](http://pollenation.net/assets/public/python-main-oct05c.png)

  - [Home Page idea built & tested in css layout from oct 2003](http://pollenation.net/assets/public/draft-oct19.html)

  - [Internal Page idea built & tested in css layout from oct 2003](http://pollenation.net/assets/public/draft-oct23.html)

  - [new logo idea from nov 2003](http://pollenation.net/assets/public/new-logo.png)

  - [page design idea to go with previous logo](http://pollenation.net/assets/public/new-altdesign.png)

  - [variation on above](http://pollenation.net/assets/public/newpython.png)

  - [developer bookmark page idea](http://pollenation.net/assets/public/python-dev.png)

- [http://www.insigniodesign.com/holdenweb/scaled/](http://www.insigniodesign.com/holdenweb/scaled/)

- [http://www.python.org/index-gray.html](http://www.python.org/index-gray.html)

- Mockups from Walter
  - [Walter\'s mockup](http://styx.livinglogic.de/~walter/www.python.org.gif)

  - [Walters Html](http://styx.livinglogic.de/~walter/www.python.org/)

  - [Walters converted from source](http://styx.livinglogic.de/~walter/www.python.org-converted/)

# Home Page must haves 

Feel free to expand this, I just want to get down my priorities. Based on the stats, feedback at OSCON, and my own usage of python.org. The home page has a few very clear usage scenarios.

- Someone knows nothing about Python, so the home page has to make it clear without a lot of extra navigation
- A new or existing user needs to download Python (most typically the current version)
- Documentation, documentation, documentation !
- Related to documentation is the need to search the current documentation and/or site
- Then there are a whole host of other things to do

# Other home pages for consideration 

- [http://www.perl.org/](http://www.perl.org/)

- [http://www.php.net/](http://www.php.net/)

- [http://www.openswf.org/](http://www.openswf.org/)

- [http://www.microsoft.com/net/](http://www.microsoft.com/net/)

- [http://www.apache.org/](http://www.apache.org/)

# Mailing List 

- [http://mail.python.org/mailman/listinfo/pydotorg-redesign](http://mail.python.org/mailman/listinfo/pydotorg-redesign)

# IRC session 

An IRC session took place between 18:00 and 17:30. Logs available here :[html formatted](http://www.pollenation.net/assets/public/pydotorg-redesign/irclog210703.html) [raw](http://www.pollenation.net/assets/public/pydotorg-redesign/irclog210703.txt) In attendence were Kevin Altis, Tim Parkin, Matt Goodall, and Fred Drake.

Latest IRC Session jun 2004 [psfprc](http://www.pollenation.net/assets/public/pydotorg-redesign/FreeNode-psfprc.log)

# Python logo images 

- [All images](http://pythoncard.sourceforge.net/images/just_python.png)

# Other tasks 

- Getting rid of PSA stuff and moving still-valid info to other parts of the site.
  - (Done \-- see [http://www.python.org/community/](http://www.python.org/community/) . Must now update links.\]

- Reorganizing [UserGroups](http://www.python.org/UserGroups.html) and [NonEnglish](http://www.python.org/doc/NonEnglish.html) \-- there\'s currently a lot of overlap, and what I\'d really like to do is move it to a database with multiple views

- Figuring out how to manage the commercial exits and other kinds of links to external resources

- Fixing up the pycon directory (I made a boo-boo when setting it up, and we\'ll need to move the old stuff before starting in on DC2004) (Done).

- Reorganizing Intros and Newbies \-- also a lot of overlap. (Done \-- see [http://www.python.org/topics/learn/](http://www.python.org/topics/learn/) . Must now update links.\]

- Implement a well-formedness checker for [HT2HTML](http://ht2html.sourceforge.net/), to help support well-formed XHTML on the site (Fred Drake volunteers). A simple version of this now exists and can be accessed via **make wfcheck** in a pydotorg checkout, but the output isn\'t as helpful as it could be. Most pages don\'t pass the check.

# Comments 

How about simply upgrading the python.org wiki and making more use of it?

Using a wiki makes it much easier to update content (as you see right here), add links and fix stuff. It puts the burden of maintaining the site on the shoulders of the community, not a few webmasters. The current [MoinMoin](MoinMoin) version (not the old version you are using now) is themeable and has access control lists for critical pages, like the FrontPage.

At the [moinmoin homepage](http://moinmoin.wikiwikiweb.de/), we are doing *everything* in the wiki. It works ![;)](/wiki/europython/img/smile4.png ";)")

\-- [ThomasWaldmann](ThomasWaldmann) 2004-07-11 11:19:12

Rewriting more of our content from HTML into ReST will help with well-formedness, and that\'s probably easier than fixing the HTML page-by-page.

\-- [AndrewKuchling](AndrewKuchling)

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite)
