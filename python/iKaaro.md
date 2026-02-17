# iKaaro

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://www.hforge.org/ikaaro/](http://www.hforge.org/ikaaro/)

version

:   0.60.5 (*2009-10-29*)

licence
:   GPLv3

platforms
:   Unix

Python versions
:   2.6

### Deployment Platforms 

iKaaro includes its own web server, in production environment deploy behind an Apache (or nginx, etc.)

### Suitability 

iKaaro is a content management framework based on a simple yet efficient model. It is designed with ease of use and strict separation of concerns in mind. Developers have very few concepts to learn in order to be productive.

### Development Interfaces 

### Environment Access 

Using the Zope object database (ZODB) as a transactional filesystem. iKaaro only stores folders or files (persistent resources). Any logic is separated in non-persistent classes (handlers).

You can use all of the Python libraries to access external resources (relational databases, web or host filesystem resources, etc.).

You can use built-in Zope FTP support to import and export from ikaaro; though you would miss the metadata suport when just importing files. An ikaaro site can be exported to the filesystem in 5 lines of code, and you can import it back without more difficulty.

### Session, Identification and Authentication 

Shipped with session support, cookie-based authentication for the client side. You can use any of the Python adapter for connecting with your information system (SQL, LDAP\...), or just store your users and their information inside ikaaro.

Objects to be published throught the web are protected by default. You can then allow their publishing through Access Control Lists (ACL). ACLs can be as simple as the boolean True, or as complex as accessing a database and checking a workflow state. You decide.

### Persistence Support 

Using the Zope Object Database (ZODB), but transparently for the developer (filesystem abstraction).

As already stated, you can access a relational database or the host filesystem.

### Presentation Support 

iKaaro comes with the Simple Template Language (STL, provided by [itools](./itools.html)). It takes only 5 keywords so it is very easy to learn. STL comes in the form of an XML namespace, placing your data inside an XML or XHTML template. No logic is possible, so it is clean and safe. You first compute the data you need in your publishing method, then you can STL to transform your template with the namespace (in the sense of Python variables) you provide (usually a dictionary).

### InTheirOwnWords 

iKaaro brings the fun back to Zope. Strict separation of concerns was something really missing in my Zope developments. When you are constantly extending and refactoring, you\'re happy with logic separated from your object data.

Nothing is hidden in object attributes but serialised in a file. Metadata for example is separated from the content object as it should be. You can extend it with your business metadata using your own XML namespace, and ikaaro with deserialise it back (load into objects).

One powerful feature of itools/ikaaro are the skeletons. You build your application, folder or file resource in memory, then apply it to the ZODB. Imagine deploying a new instance of your site already with a hierarchy, user accounts, groups, several front-end sites, an indexing catalog, and all of your business rules applied.

### Comments 

iKaaro is an open community. We use a decentralised revision management (Arch, aka tla, aka bazaar), so anyone is welcome to develop without requiring CVS login.

Most of the concepts you need you learn with iKaaro is provided by the [itools](./itools.html) library, which is covered by a 85 pages documentation. For learning iKaaro itself, you are driven by an introductory documenation, and a 5 step tutorial, which brings one concept at a time.

Each new version of ikaaro is provided with an upgrade script, when necessary. You are never stuck with a site you cannot migrate.

### Hosting 

So far, you need a dedicated hosting in order to install ikaaro. We are working towards a solution for M16.
