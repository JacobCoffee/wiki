# Zope

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://www.zope.org/](http://www.zope.org/)

current Zope 2 stable release

:   2.10.0 (*2006-10-03*)

current Zope 2 release from the previous stable branch

:   2.9.5 (*2006-10-02*)

current Zope 3 stable release

:   3.3.0 (*2006-09-21*)

licence

:   [ZPL](http://www.zope.org/Resources/ZPL) - Zope is open source, as are many of the extensions and add-ons available for it.

platforms
:   Zope works on UNIX and Windows platforms.

Python versions
:   2.4.3

Download URL

:   [http://www.zope.org/Products](http://www.zope.org/Products)

### Deployment Platforms 

- As a standalone server - this is the default, which permits Zope to be run relatively easily \"out of the box\".
- Integrated with a Web server using CGI, PCGI or FastCGI.
- The Zope environment is provided by long-running processes.

### Protocols 

Out of the box
:   HTTP, WebDAV, FTP, XML-RPC, SOAP?

Through additional modules
:   ???

### Suitability 

The \"out of the box\" single server option makes Zope attractive for developers who either do not want to integrate many components or have little experience in doing so. The need to have Zope processes continuously running excludes Zope from certain hosting environments, but being available as a packaged product with explicit security features, Zope is also attractive to other, potentially more spec ialised hosting companies. Thus, Zope hosting can be had, even for free, with certain hosting providers.

### Development Interfaces 

- Presentation-oriented - DTML methods and templates provide a lightweight introduction to the processing of inputs and the production of Web pages in response.

- Object-oriented, servlet-like - external methods and Zope Products expose request and response objects to Python components.

- [BoaConstructor](BoaConstructor) is an IDE which integrates well with Zope, allowing editing of presentation and logic files from within the same environment.

- [WingIde](WingIde) provides support for developing and debugging Zope applications.

### Environment Access 

- Zope\'s object database (ZODB) is the principal means of associating resources with application components.
- Adapters which provide access to external resources, such as database systems, are available for use with Zope.

### Session, Identification and Authentication 

- Zope 2.5 (and earlier releases with [CoreSessionTracking](./CoreSessionTracking.html)) provides a mechanism for the identification of users.

- Zope has always supported authentication for \"site editors\", but such support may only be appropriate for \"content management\" applications.

- Zope has a significant security system with very granular settings.

### Persistence Support 

- Zope provides near-transparent object persistence in the object database, and it is possible to have multiple object database instances.
- Interaction with relational database systems is typically performed using SQL.
- Certain tools are available for querying object database instances, but the reliance on ZODB for the storage of application data (should this be chosen) may be a significant concern in certain environments.
- A noticeable tradeoff therefore exists between convenience of persistence (using ZODB) and openness of access (using SQL-based databases).

### Presentation Support 

- DTML - Zope\'s original [StructureAnnotation](StructureAnnotation) presentation technology which provides additional special tags for use in HTML or other textual resources.

- ZPT (Zope Page Templates) - a [StructureAnnotation](StructureAnnotation) presentation technology which specifies HTML/XML attributes for use with HTML/XML-based documents and allows Python expressions and references to be embedded.

Other presentation systems could presumably be supported in Zope, but from Zope 2.5, the above technologies appear to be \"first class\".

### Comments 

Zope provides so much support for some activities that certain kinds of applications can be created and configured in very short periods of time, given enough experience of Zope development. Where object persistence is required, for example, Zope applications require little effort to make such mechanisms work, whereas other frameworks (such as [EnterpriseJavaBeans](EnterpriseJavaBeans) container-managed persistence) require a certain amount of administrative overhead (the declaration of each object schema) and may be prone to obscure failure, given the complexity of the integration and configuration of many different systems. \-- [PaulBoddie](PaulBoddie)

Python version should probably mention 2.1.3 (which works well with Zope 2.4.x and 2.5.x), Python versions 2.1.1 and 2.1.2 do not. Python 2.2 is not officially supported for 2.5.x and before (not sure about later versions). \-- Terry Hancock

For Zope 2.7.0, Python 2.3.3 is the preferred release \-- [JeffreyShell](./JeffreyShell.html)

[MythDebunking](MythDebunking): *Zope is hard to learn.*

Zope *is* hard to learn. If it\'s the right tool to solve your problem, it\'s arguably worth the pain of learning it because it is extremely powerful. However, as with most web platforms, there is a \"Zope way\" to approach solving any problem with it. The principle of \"expect to throw your first attempt away\" applies strongly with Zope; learn it via smaller examples and projects before tackling anything very substantial. \-- [BenLast](./BenLast.html)

Zope performance is not stellar. Expect to use a caching reverse proxy or the like (commonly, this is Apache) to \"front-end\" a Zope site if you are serving high levels of traffic. Zope has extremely good support for various levels of internal and external (proxy) caching. \-- [BenLast](./BenLast.html)

### Hosting 

[http://www.zope.org/Resources/ZSP](http://www.zope.org/Resources/ZSP) contains a list. New entries should be added to that list instead of on this page.
