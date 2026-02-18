# PythonWebsiteContentMigration

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Note:** These are older notes on content migration from the old site. Since some of the old site is still in the old format and copied over automatically by the build process, this is being retained in case there is something useful in it.

## A quick guide to how a link should converted on the new website 

First an example.

Old Style: ../Mirrors.html

New Style: /doc/mirrors/

What would have been a single page in the old site is now a directory named after the old page (without \'.html\') containing index.html.

In the source repository, the page is made up of several files that contain template information, content and maybe some sub-menu stuff and this is all whacked together by Pyramid to produce the new site. But you should know that already if you are editing links in pages.. ![:-)](/wiki/europython/img/smile.png%20":-)")

A link on a page like \'\<a href=\"../Mirrors.html\"\>Blah\</a\>\' should be converted so that:

a\) The link is lowercase (because the directory that the page content is in will be

b\) The suffix should be removed if it is .html, not if it is .pdf or .rst

c\) Preferably the relative portion should be replaced with an abolute path. If the page is moved within the website, the links on the page will not require maintenance.

## Files/Directories that need to be copied over into the new python tree 

not checking the /\<N\> or /doc/\<N\> folders yet

### script needed 

/channews.rdf /channews.dat \^ rdf to be moved from /new/rdf/index.html and header replaced with xml directive .. what about .dat

/dev/summary/channews.rdf /dev/summary/channews.dat \^ needs generating? do the summaries still get generated still?

### files/directories to be copied into www 

NO /community already moved NO /consortium points to psf NO /cp4e omitting YES /css will be need for some legacy content YES /buildbot YES /ftp

YES /idle should this page have a warning that it may be removed or pointed elsewhere YES /emacs should this page have a warning that it may be removed or pointed elsewhere YES /editors should this page have a warning that it may be removed or pointed elsewhere

YES? /neal pictures of guido and python, should we move? (also has a patches subdir)

YES? /other spread & python movie\... should these be here.. can we move them into files?

??? /packages?

NO? /packman - short term copy (this is apparently no longer being maintained according to email from owner/ex-maintainer)

??? /patches

YES /pics - all of the old assets

??/ /psa

YES /pycon/dc2003 - copy to /community/pycon/dc2003 YES /pycon/dc2004 - ditto ??? /pycon/dc2005 ??? /pycon/2006

NO? /psf I\'m fairly sure everything was converted to the new site already during the sprint (?)

YES /pythonlabs

??? /scripts this shouldn\'t really be in the publicly available web tree?

YES /search/hypermail - important historical archives

YES /pyvault - note sure of status (no email reply from maintainer) but copy for now

### redirects needed 

above and beyond the checks for ./\<mixedcase\>.html which should redirect to ./\<lowercase\> the following will be needed

/\<n\> (python versions) -\> /download/releases/\<n\>

/consortium \> /psf /dev/devintro.html \> /dev/devintro

smb://192.168.0.2/python/www.python.org/download/download_linux.html smb://192.168.0.2/python/www.python.org/download/download_mac.html smb://192.168.0.2/python/www.python.org/download/download_os2.html smb://192.168.0.2/python/www.python.org/download/download_other.html smb://192.168.0.2/python/www.python.org/download/download_source.html smb://192.168.0.2/python/www.python.org/download/download_win31.html smb://192.168.0.2/python/www.python.org/download/download_windows.html \^ Do we need all of these? they should be copied over for legacy?

/pycon -\> /community/pycon

/security -\> /news/security

/sigs -\> /community/sigs (check for individual sig redirects?)

/why -\> /about/why

/sf/######## -\> source forge bug/patch lookup

/Jobs.html -\> /community/jobs /Help.html -\> /help /News.html -\> /news /security -\> /news/security

/topics(.\*) -\> /doc/topics(.\*) /psf(.\*) -\> /community/psf(.\*)

/audio -\> [http://wiki.python.org/moin/Audio](http://wiki.python.org/moin/Audio)

### action taken on directories 

/dev/buildbot \^ what is going to happen and where does this come from

/dev/doc/devel /dev/doc/maint /dev/doc/maint23 /dev/doc/maint24 /dev/doc/newstyle /dev/doc/python-docs-devel.tar.bz2 /dev/doc/python-docs-maint23.tar.bz2 /dev/doc/python-docs-maint24.tar.bz2 /dev/doc/python-docs-newstyle.tar.bz2

\^ all of above need addressing (probably just copying in?

/dev/src \^ looks like it just needs copying in?

/doc/essays \^ looks like it could be copied over??? it might need a new style index page though to make it fit in better?

/doc/\<n\> (python versions) \^ Copy over

/doc/api /doc/current /doc/dist /doc/ext /doc/inst /doc/lib /doc/mac /doc/ref /doc/tut \^ latex docs to be copied over

/doc/icons \^ graphics for the documentation

/doc/QuickRef.html \^ needs to be copied over or transformed to new style (or a bit of both)

/doc/pythonVSscheme.html /doc/progtype.html /doc/pypref.html /doc/PyCPP \^ copy or update?

/doc/lj21.html /doc/lj21cover.gif \^ copy across

- \-- converted and moved into /doc/intros where it belongs (Martin)

/doc/News.html \^ old news ? should it be copied (I think it should go somewhere)

/doc/Newbies.html \^ another \'introduction to python\'

/doc/newb.html \^ a book page.. would be better updated and put under booklist/bbokstore

/doc/LutzBlurb.html \^ another introduction to python

/doc/IPwP_errata.txt \^ internet programming with python errata?

/doc/Hints.html can\'t find many references to it.. it should really be converted and a good home found for it.

/download/contrib-categories /download/contrib-entries /download/contrib-master.py /download/contrib-master.txt \^ are these doing something clever?

/download/SendingBinaries.html \^ should this be in the main menu?

/editors/editors/Python.CLF \^ don\'t know what this is

/topics/writing \^ I can\'t see any inbound links to this page?

/windows \^ needs reviewing but copy across for now

/workshops \^ needs reviewing (some of this is in already) but copy across for now

### action taken on files 

/community - copied across the clpya-guidelines.txt (should this be in download too??)

/contact.html - added

/doc/Railroad.ps moved into /files/doc/Railroad.ps

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite)
