# PyPI/DownloadMetaDataProposal

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PyPI Download Meta Data Proposal 

This page collects comments and ideas for a proposal to migrate away from having PyPI-based installers such as easy_install and pip crawl arbitrary links on the [PyPI /simple/ index](https://pypi.python.org/simple/).

Here\'s the original posting to the catalog-sig:

- [\[Catalog-sig\] Migrating away from scanning home pages (was: Deprecate External Links)](http://mail.python.org/pipermail/catalog-sig/2013-February/005436.html)

## Sketch of the proposal 

Version: 0.1 (older versions can be found in the page history)

Here\'s an approach that would work to start the transition away from crawling websites while not breaking old tools:

### Limiting scans to download_url 

Installers and similar tools preferably no longer scan the all links on the /simple/ index, but instead only look at the download links (which can be defined in the package meta data) for packages that don\'t host files on PyPI.

### Going only one level deep 

If the download links point to a meta-file named \"**\<packagename\>-\<version\>-downloads.html#sha256=\<sha256-hashvalue\>**\" (the *downloads.html* file for the purpose of this proposal), the installers download that file, check whether the hash value matches and if it does, scan the file in the same way they would parse the `/simple/` index page of the package - think of the downloads.html file as a symlink to extend the search to an external location, but in a predefined and safe way.

### Notes 

- The creation of the downloads.html file is left to the package owner (we could have a tool to easily create it).

- Since the file would use the same format as the PyPI /simple/ index directory listing, installers would be able to verify the embedded hash values (and later GPG signatures) just as they do for files hosted directly on PyPI.

- The URL of the downloads.html file, together with the hash fragment, would be placed into the setup.py download_url variable. This is supported by all recent and not so recent Python versions.

- No changes to older Python versions of distutils are necessary to make this work, since the download_url field is a free form field.

- No changes to existing distutils meta data formats are necessary, since the download_url field has always been meant for download URLs.

- Installers would not need to learn about a new meta data format, because they already know how to parse PyPI style index listings.

- Installers would prefer the above approach for downloads, and warn users if they have to revert back to the old method of scanning all links.

- Installers could impose extra security requirements, such as only following HTTPS links and verifying all certificates.

- In a later phase of the transition we could have PyPI cache the referenced distribution files locally to improve reliability. This would turn the push strategy for uploading files to PyPI into a pull strategy for those packages and make things a lot easier to handle for package maintainers.

  Since there are legal implications when redistributing files obtained from other servers, either the PyPI terms would have to be adapted, or the download.html file would need to be extended to include a marker, which the PyPI server could then use to enable/disable caching of the distribution files (the commonly used [rel=\"no-follow\" attribute](http://en.wikipedia.org/wiki/Nofollow) could be used for this).

### Comments 

The above is a sketch, not a fully worked out proposal, so feedback is welcome. Please add your comments here:

\...
