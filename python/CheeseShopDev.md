# CheeseShopDev

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page is about development of the [Python Package Index](http://pypi.org) (formerly known as Cheeseshop):

- More Info: [CheeseShop](CheeseShop)

- PyPI APIs: [JSON](PyPIJSON), [XMLRPC](PyPIXmlRpc)

# Developing the Package Index 

## PyPI.nextgen: 

Currently, as of 2019-06-27, PyPI has undergone a complete rewrite from scratch, and as a result much of the information on this page is not up-to-date.

The development moved from Mercurial (Python) to Git (C, shell). License changed from BSD-3 to Apache 2.0. Project code named \'warehouse\' can be downloaded from:

- [https://github.com/pypa/warehouse](https://github.com/pypa/warehouse)

## Testing Your Stuff Against PyPI 

If you need to test stuff against PyPI (registration, uploading, API activities) then please [use the alternative server, test.pypi.org](https://packaging.python.org/guides/using-testpypi/).

## TO-DO list 

Meta-to-do: file the issues below that are still unresolved in [the GitHub issue tracker](https://github.com/pypa/warehouse/issues), then remove this section. \-- [SumanaHarihareswara](SumanaHarihareswara) 2019-08-23 10:57:10

- A dump of download counts.

- A big structured dump of all package meta-data.

- A link from package to RTFD.

- [PEP for metadata 1.2](http://www.python.org/peps/pep-0345.html) \-- not finished and needs more catalog-sig discussion)

- documented procedures for \"taking over\" entries should the original owner of the entry go away (and any required system support)

- change notification emails

- per-classifier \"wiki\" content to allow description and discussion around each classifier (perhaps what packages are available and how they relate to one another)

- screenshot images (with thumbnailing and a \"latest screenshot\" on the front page?) - or perhaps icons instead of thumbnails for some packages?

Something that\'s been requested, but needs much more thought and analysis to see whether it causes any problems: the ability to treat project names and versions as case-insensitive, while removing extraneous characters (as in pkg_resources.safe_name()) for purposes both of searching and determining name uniqueness when registering.

### Done 

- command-line tool to query pypi and fetch entries: [yolk](http://pypi.python.org/pypi/yolk)

## Not Going TO-DO 

- Edit [PEP 243](http://www.python.org/peps/pep-0243.html) to reflect reality. The interface is implemented in the distutils register and upload commands. This code is good enough for documentation, especially because it\'s the only implementation necessary.

- moderated user reviews and ratings (this would require quite a lot of support from volunteers though)

## Proposals 

- [EnhancedPyPI](http://wiki.python.org/moin/EnhancedPyPI) Enhance multiple package index servers support in Distutils.

## Previous PyPI version 

The legacy version of PyPI is the code that was running on [http://pypi.python.org](http://pypi.python.org) for many years, till mid-2018. [This LWN article goes into the history.](https://lwn.net/Articles/751458/) The information below should help you get around the code.

- The PyPI code was hosted under the Python Packaging Authority project: [https://bitbucket.org/pypa/pypi](https://bitbucket.org/pypa/pypi) and is now on GItHub: [https://github.com/pypa/pypi-legacy](https://github.com/pypa/pypi-legacy)

- Bug and patch tracker [https://github.com/pypa/pypi-legacy/issues](https://github.com/pypa/pypi-legacy/issues)

- [Mailing List](http://mail.python.org/mailman/listinfo/distutils-sig) ([Gmane](http://dir.gmane.org/gmane.comp.python.distutils) web interface)

- API that is used by easy_install [http://peak.telecommunity.com/DevCenter/EasyInstall#package-index-api](http://peak.telecommunity.com/DevCenter/EasyInstall#package-index-api)

- [PyPIOAuth](PyPIOAuth) - authentication library for Google and Launchpad logins

## Legacy PyPI architecture and endpoints 

PyPI is a WSGI application that can be executed standalone using `python pypi.wsgi`{.backtick} command if all requirements are met. `pypi.wsgi`{.backtick} contains usual WSGI wrapper code and delegates request processing to `WebUI.run()`{.backtick} method from `webui.py`{.backtick}. This method just opens DB and handles exceptions, actual request processing is done in `WebUI.inner_run()`{.backtick}. This method analyzes URL endpoint and executes appropriate handler. As of 2011-04, the rules to match endpoints to handlers are the following:

::: {}
  ------------------ -------------------- --------------------------------------------
  /simple            WebUI.run_simple()   dump all package names on single html page
  /simple/(.+)/      WebUI.run_simple()   dump all links for a package in html list
  /serversig/(.+)/   .run_simple_sign()   save as above, but signed by server
  /mirrors           .mirrors()           display static page with a list of mirrors
  /daytime           .daytime()           display current server time
  ------------------ -------------------- --------------------------------------------
:::

\...

XML-RPC requests are detected by CONTENT_TYPE=`text/xml`{.backtick} variable in CGI environment and processed by `rpc.RequestHandler().__call__()`{.backtick}. List of XML-RPC \"endpoints\" is available on [PyPIXmlRpc](PyPIXmlRpc) page.

## Legacy PyPI Development Environment Hints 

Removed (visible in [page history](https://wiki.python.org/moin/CheeseShopDev?action=recall&rev=81)) because developing and running legacy PyPI is deprecated. \-- [SumanaHarihareswara](SumanaHarihareswara) 2019-08-23 10:57:10
