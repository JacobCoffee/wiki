# Admin/PlanetSetup

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# planet.python.org setup 

![/!\\](/wiki/europython/img/alert.png "/!\") *Please note: The administration pages have all been migrated to the new [PSF Systems Wiki](https://psf.projecthut.com/trac/psfsystems/wiki). Please no longer add information to these pages. If you need access to the new wiki, please contact [psf@python.org](mailto:psf@python.org) for details.*

## Setup 

*Note: These instructions are probably outdated ! The current installation is run via a Github repository at [https://github.com/python/planet](https://github.com/python/planet)*

planet.python.org is currently hosted on dinsdale.python.org. It\'s running a 2005 version of the software

The set-up is in the /data/planet/ directory. Templates and the configuration files are in /data/planet/config/. Currently the configuration files are:

- config.ini : for planet.python.org
- jython.ini : for planet.jython.org

The Subversion URL for the repository is [file:///data/repos/www/trunk/planet/config](file:///data/repos/www/trunk/planet/config) on dinsdale, or `svn+ssh://pydotorg@svn.python.org/trunk/planet/` for remote access.

For example: `svn co svn+ssh://pydotorg@svn.python.org/trunk/planet/`

Currently the live Planet set-up is under the \'amk\' user ID on dinsdale; we should move it to some generic user ID and put it in some common group. There\'s no commit hook that automatically updates the live files after a checkin; instead I just log into dinsdale, edit config.ini or jython.ini as desired, commit it, and wait for the next scheduled update to run.

The sites are updated with the following cron jobs (again, under my user ID):

    37 1,4,7,10,13,16,19,21 * * * /data/planet/run.sh /data/planet/config/config.ini
    47 1,10,19 * * * /data/planet/run.sh /data/planet/config/jython.ini

(run.sh is a little wrapper script; it can be useful to execute \"run.sh -o \<config-file\>\" when experimenting with template changes.)

## Adding/removing feeds 

The mechanical task of adding and removing feeds is pretty easy: edit the appropriate config. changes.

The sort-ini.py script sorts the URLs in a .ini file in-place. Keeping the URLs in sorted order makes it easier to find accidental duplications and variants of feeds. To run it, just do \"./sort-ini.py config.ini\". The contents of the file will be read, sorted, and written out into the same filename. (The files are version-controlled, so the script is pretty sloppy about rewriting the file.)

Add/drop requests are currently sent to planet-at-python.org, which is aliased to the pydotorg mailing list.

Editorially speaking: the feed list started out as \'feeds from members of the Python community\', and there wasn\'t much concern about whether they were posting Python-related content or not. As the list of feeds grew longer, I started to want to reduce the number of posts, and began choosing to use Python-specific category feeds when they\'re available.

However, I don\'t get upset over non-Python related posts as long as the weblog in question still posts Python-related content fairly often. (I haven\'t defined a bright-line test for what \'fairly often\' means.) Occasionally I\'ll see weblog comments that ask the author \'why is this political/personal stuff showing up on Planet Python?\'; these sorts of comments make me sad, but I can\'t think of a good way to tell these commenters to just deal with it.

In the past I have dropped feeds of people who began writing exclusively about non-Python topics, sometimes after sending them an e-mail asking if this is a temporary or permanent change (sometimes it\'s obvious). Generally I\'ll drop feeds that haven\'t been updated at all in 9 months, but I haven\'t done a systematic liveness check in at least a year.

## Tasks 

- Possible task: move entire set-up to ximinez.python.org, which runs more of the dynamic content for \*.python.org.

- Update code to latest PlanetPlanet or Venus release.

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite)
