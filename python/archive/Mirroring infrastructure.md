# Mirroring infrastructure

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Mirroring infrastructure in PyPI 

- PEP: xx
- Title: Mirroring infrastructure in PyPI
- Author: Tarek Ziadé
- Discussions-To: Catalog SIG
- Status: Draft
- Python-Version: 2.6

## Abstract 

This PEP describes a mirroring infrastructure for PyPI.

## Motivations 

PyPI is hosting over 4000 projects and is used on a daily basis by people to build applications. Especially systems like easy_install and zc.buildout make intensive usage of PyPI.

For people making intensive use of PyPI, it can act as a single point of failure. People have started to set up some mirrors, both private and public. Those mirrors are active mirrors, which means that they are browsing PyPI to get synced.

In order to make the system more reliable, this PEP describes:

\- the mirror listing and registering at PyPI

\- the pages a public mirror should maintain.

- these pages will be used by PyPI, in order to get hit counts and the last modified date.

\- how a mirror should synchronize with PyPI

\- how a client can implement a fail-over mechanism

\- a contact form for Package maintainers

## Mirror listing and registering 

A new text page will be added at [http://pypi.python.org/mirrors](http://pypi.python.org/mirrors) that can be browsed like the simple index. This page gives a list of the mirrors through a list of links.

These links are the URL of the simple index of each mirror. The page will look like this:

    # PyPI mirrors
    #    
    # If you want to register a new mirror, send an email
    # to the catalog-SIG@python.org with:
    #
    # - The urls of your mirror:
    #   - the root of the server
    #   - the index page 
    #   - the last modified page
    #   - the local stats page
    #   - the global stats page
    #   - the mirrors page
    #
    # - The name and email of the maintainer.
    #   
    #   The registering is done manually and to become a
    #   mirror, you need to strictly follow the mirror protocol
    #   described here:
    #
    #    http://wiki.python.org/PEP_374
    #    
    # root,index,last-modified,local-stats,stats,mirrors
    http://example.com/pypi,index,last-modified,local-stats,stats,mirrors
    http://example2.com/pypi,index,last-modified,local-stats,stats,mirrors

When a mirror is proposed on the mailing list, it is manually added in the mirror list in the PyPI application after it has been checked to be compliant with the mirroring rules.

The mirror list page is a simple text page that can be browsed by any tool that wants to get a list of registered mirrors. Other package indexes that are not mirrors of PyPI are not added in the mirror list in PyPI. Although they can provide themselve the same mirroring list mechanism for their own mirrors.

## Special pages a mirror needs to provide 

A mirror needs to provide four pages, beside the index one:

- last-modified
- local-stats
- stats
- mirrors

### Last modified date 

CPAN uses a freshness date system where the mirror last synchronisation date is made available.

For PyPI, each mirror needs to maintain an url with a simple text content that represents the last synchronisation date the mirror maintains.

The date is provided in GMT time, using the iso 8601 format ([http://en.wikipedia.org/wiki/ISO_8601](http://en.wikipedia.org/wiki/ISO_8601))

Each mirror will be responsible to maintain its last modified date.

Conventionaly, this page should be reachable at: \"/last-modified\".

### Local statistics 

Each mirror is responsible to count all the downloads that where done on it. This is used by PyPI to sum up all downloads, to be able to display the grand total.

This page is a csv-like page, with a header at the first line. It needs to obey PEP 305 [http://www.python.org/dev/peps/pep-0305/#id19](http://www.python.org/dev/peps/pep-0305/#id19). Basically, it should be readable by Python csv module.

The fields in this file are:

- package: the distutils id of the package.
- filename: the filename that has been downloaded.
- useragent: the User-Agent of the client that has downloaded the package.
- count: the number of downloads.

The page will look like this:

    # package,filename,useragent,count
    zc.buildout,zc.buildout-1.6.0.tgz,MyAgent,142
    ...

The counting starts the day the mirror is launched.

Conventionaly, this page should be reachable at: \"/local-stats\", but any url relative to the mirror root can be given.

### Statistics page 

PyPI and each mirror are responsible to provide the grand total page at \"/stats\". This page is calculated daily by PyPI, by reading all mirrors local stats and suming them.

Therefore the mirrors should not try to rebuild this stat page but simply get PyPI\'s one during each synchronization.

It has the same structure than the local-stats page.

Conventionaly, this page should be reachable at: \"/stats\".

### Mirrors listing page 

Like /stats, each mirror should get and provide the /mirrors page.

Conventionaly, this page should be reachable at: \"/mirrors\".

## How a mirror should synchronize with PyPI 

A mirroring protocol calls Simple Index was described and implemented by Martin v. Loewis and Jim Fulton, based on how easy_install works. This section synthesizes it and give a few relevant links, plus a small part about User-Agent.

### The mirroring protocol 

XXX changelog, pje link + to be defined

### User-agent request header 

In order to be able to differentiate actions taken by clients over PyPI, a specific user agent name should be provided by all mirroring softwares.

This is also true for all clients like:

- zc.buildout
- setuptools
- pyinstaller
- etc.

XXX user agent registering mechanism at PyPI ?

## How a client can use PyPI and its mirrors 

XXX

## Fail-over mechanism 

Clients that are browsing PyPI should be able to use a fail-over mechanism when PyPI is not responding.

This can be done by parsing the /mirrors page of PyPI or the one located on any PyPI mirror.

It is up to the client to decide wich mirror should be used, depending on its geographical location and its responsivness.

This PEP does not describe how this fail-over mechanism should work, but it is strongly encouraged that the clients try to use the nearest mirror.

The clients so far that could use this mechanism:

- setuptools
- zc.buildout (through setuptools)
- pyinstaller

## Extra package indexes 

It is obvious that some package will not be uploaded to PyPI. Wether because they are private or wether because the project maintainer runs his own server where people get the project package. Although, it is strongly encouraged that a public package index follows PyPI and distutils protocols. In other words, the \"register\" and \"upload\" command should be compatible with any package index server out there.

Softwares that are compatible with PyPI and distutils:

- [PloneSoftwareCenter](./PloneSoftwareCenter.html)

- [EggBasket](./EggBasket.html)

## Merging several indexes 

When a client needs to get some packages from several distinct indexes, it should be able to use each one of them as a potential source of packages. Different indexes should be defined as a sorted list for the client to look for a package.

Each independant index can of course provide a list of its mirrors, if the /mirrors page is available.

That permits all combinations at client level, for a reliable packaging system with all levels of privacy.

## Other PyPI enhancements 

XXX

### Contact form for Package maintainers 

A form reachable from the package page will be added, where a registered user can submit a message to the package owner. This is to be used when someone wants to take over the distutils id name, or when someone (like a packager for example) would like to reach the package owner for some questions.

XXX isn\'t the mail in the metadata enough ? XXX the original whish here was to enforce the package owner to upload sdist.
