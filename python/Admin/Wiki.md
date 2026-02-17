# Admin/Wiki

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

![/!\\](/wiki/europython/img/alert.png "/!\") *Please note: The administration pages have all been migrated to the new [PSF Systems Wiki](https://psf.projecthut.com/trac/psfsystems/wiki). Please no longer add information to these pages. If you need access to the new wiki, please contact [psf@python.org](mailto:psf@python.org) for details.*

The MoinMoin installation is on dinsdale, and is a stock Debian package.

There are 4 instances:

- main.py
- jython.py
- pycon.py
- psf.py

Their configuration files are in `/data/moin/instances/`{.backtick}; there\'s also a `farmconfig.py`{.backtick} containing global settings.

After changing any of the configuration files, you should restart Apache for the changes to take effect: `apache2ctl graceful`{.backtick}. This should not cause any visible downtime to endusers.

The configuration files are kept in a mercurial repository, so please commit your changes with `hg commit -u yourname`{.backtick} if you change anything.

MoinMoin uses WSGI, which is configured to restart after 1000 requests, so any such change will propagate eventually (typically after about 1h).

See also [PythonWikiChanges](PythonWikiChanges)

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite)
