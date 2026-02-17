# PyPISimple

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[PyPI](CheeseShopDev) APIs: **Simple**, [JSON](PyPIJSON), [XMLRPC](PyPIXmlRpc).

For up to date documentation, see [https://warehouse.readthedocs.io/api-reference/legacy/](https://warehouse.readthedocs.io/api-reference/legacy/)

You can get a list of all the distributions available on PyPI from the URL

        https://pypi.org/simple/

This returns a HTML page containing a list of links to the individual distribution pages.

If you wish to retrieve information about the download files available for specific distribution you may use

        https://pypi.org/simple/<distribution_name>/

This returns a HTML page containing a list of links to the actual downloadable files, and to other URLs registered by the project. The distribution name should be in canonical form (all lowercase, with dashes replaced by underscores) but there is a redirect from the name as specified by the project to the canonical name (and from the names without a trailing backslash to the version with a trailing backslash). To minimise network round trips, the canonical name should be used.

The following code can be used to extract the URLs from the simple API pages:

    from xml.etree import ElementTree
    from urllib.request import urlopen

    def get_distributions(simple_index='https://pypi.org/simple/'):
        with urlopen(simple_index) as f:
            tree = ElementTree.parse(f)
        return [a.text for a in tree.iter('a')]

    def scrape_links(dist, simple_index='https://pypi.org/simple/'):
        with urlopen(simple_index + dist + '/') as f:
            tree = ElementTree.parse(f)
        return [a.attrib['href'] for a in tree.iter('a')]

**TODO**: Add further details about links, `rel=`{.backtick}, `#md5=`{.backtick}, `#egg=`{.backtick}, links scraped from long_description and how/when to follow download links externally.
