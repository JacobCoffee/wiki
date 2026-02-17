# CodingProjectIdeas/FileSystemVirtualization

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Note: this idea was originally written for SoC 2005. Since then [PEP 355](http://www.python.org/dev/peps/pep-0355/) was written, which describes an interface for a path object. This should serve as the basis for any implementation.

There are several object-oriented ways to access filesystems in Python, though none have reached a critical mass of popularity. Two instances are [py.local](http://codespeak.net/py/current/doc/) and [path](http://www.jorendorff.com/articles/python/path/).

Given that OO interface, you can create objects that look like filesystems but access other resources, like WebDAV servers, databases, etc. py.local contains an implementation that accesses a svn repository.

One of these could be extended, or a generic interface for filesystems could be developed alongside several functional implementations of that interface.

------------------------------------------------------------------------

- Take a look at Tcl\'s virtual file system for some inspiration. \-- Brett Cannon

- An existing work in Python is [itools.vfs](http://download.ikaaro.org/doc/itools/Chapter--VFS.html). Work on filesystem virtualisation should also take into account the existing urllib/urllib2 modules (and improvements - see [CleanupUrlLibProject](CleanupUrlLibProject)) along with other packages which provide file-like and os/os.path-like interfaces, notably [ftputil](http://ftputil.sschwarzer.net/). \-- [PaulBoddie](PaulBoddie)

- Check out [filelike](http://pypi.python.org/pypi/filelike/0.2.2)
