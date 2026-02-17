# Admin/SiteBuild

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The automatic build process for the www.python.org site on dinsdale works like this.

## Post-commit hook 

An SVN post-commit hook adds a \"buildqueued\" file to the `/data/website-build/build/status`{.backtick} directory, containing the revision number; that\'s it. A file called \"pepqueued\" is added for PEP checkins, which are in a different repository.

This directory is accessible through the web at [http://www.python.org/status/](http://www.python.org/status/).

The post-commit hook runs `/data/repos/www/hooks/post-commit`{.backtick} -\> `update-web-wrapper`{.backtick} -\> `update-web.py`{.backtick} as user amk.

## Automatic build 

A cron job runs every 5 minutes (`build/scripts/post-commit-svnup-binary`{.backtick}, a set-uid binary), under the amk account. It runs `build/scripts/post-commit-svnup.py`{.backtick} which checks for \"buildqueued\" & \"pepqueued\" files. If found, it rebuilds the site, calling in turn `build/scripts/server-build.py`{.backtick}. (The name post-commit-svnup-\* is misleading; they\'re not called by post-commit hook any more, but once were.)

The script performs the following steps:

1.  \"svn up\" in the `build/`{.backtick} directory

2.  build the new `.html`{.backtick} files in build/out

3.  copy the new files to `/data/ftp.python.org/pub/www.python.org`{.backtick}

The site-updating cron job is run as user tparkin, and its output is appended to `build/status/postcommitlog.txt`{.backtick}. If that log file doesn\'t exist, a new one is created, but only writable by tparkin.
