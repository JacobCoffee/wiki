# Pypi package downloads statistics RSS

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Download statistics for package registered on Pypi can be obtained, in RSS format, by subscribing your favorite RSS reader (e.g. [GoogleReader](./GoogleReader.html)) with the following:

     http://www.jldupont.com/services/pypirss/rss/$package_name

**Example**

\[[http://www.jldupont.com/services/pypirss/rss/pypp](http://www.jldupont.com/services/pypirss/rss/pypp)\]

------------------------------------------------------------------------

Q: I tried [http://www.jldupont.com/services/pypirss/rss/lockfile](http://www.jldupont.com/services/pypirss/rss/lockfile) but got an error. Does something need to be set up for each package?

A: There is no downloads available for this package, hence no statistics on downloads.

- ERROR: Error accessing \"downloads\" attribute from package\[lockfile\]

Q: You mean no downloads since you implemented this feature, or no downloads at all?

A: Sorry for the confusion: the XMLRPC interface to Pypi returns that an error code to the effect that no \'package_data\' is available. If I look at the page on Pypi \[[http://pypi.python.org/pypi/lockfile](http://pypi.python.org/pypi/lockfile)\], I don\'t see one either i.e. a download URL is made available BUT there are no \"uploaded files\" to Pypi.

Q. Interesting. People tell me they use lockfile, and it actually has a score listed when you search PyPI for \"lockfile\". Collecting download stats must be a relatively recent phenomenon.

------------------------------------------------------------------------

\[[http://wiki.python.org/moin/PyPiXmlRpc](http://wiki.python.org/moin/PyPiXmlRpc) Pypi XMLRPC\]. I must say that the XMLRPC interface could be augmented to make it easier to derive per-package-version statistics.

Thanks. Got it now:

    >>> server.release_urls('lockfile', '0.7')
    []
    >>> server.release_urls('lockfile', '0.6')
    []
    >>> server.release_urls('lockfile', '0.5')
    []
    >>> server.release_urls('lockfile', '0.4')
    []
    >>> server.release_urls('lockfile', '0.3')
    []
    >>> server.release_urls('lockfile', '0.2')
    [{'has_sig': False, 'upload_time': <DateTime '20071209T14:31:52' at 81de40c>, 'comment_text': '', 'python_version': 'source', 'url': 'http://pypi.python.org/packages/source/l/lockfile/lockfile-0.2.tar.gz', 'md5_digest': 'd5fb6d5c39a791c6fd218917707651eb', 'downloads': 163, 'filename': 'lockfile-0.2.tar.gz', 'packagetype': 'sdist', 'size': 9538}]
    >>> server.release_urls('lockfile', '0.1')
    []

Kind of a weird download distribution, but it explains things (I think). Delete all this stuff when you tire of seeing it\... \-- Skip

I forget to mention that the service only fetches the stat for the latest package release on record. \-- jld.
