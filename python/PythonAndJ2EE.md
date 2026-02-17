# PythonAndJ2EE

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This document (originally derived from [PaulBoddie](PaulBoddie)\'s [Python Frameworks and J2EE Standards](http://www.boddie.org.uk/python/web_modules_enterprise.html) document) provides an analysis of Python Web modules and frameworks, along with a comparison of these frameworks to Java 2 Enterprise Edition (J2EE) standard technologies. Whilst many different Python Web modules and frameworks exist (see the [WebProgramming](WebProgramming) topic guide for details), this document only attempts to review those frameworks which provide environments comparable to the more complete J2EE implementations.

# Technology Overview 

Here follows a number of sections, each describing a J2EE technology, and each accompanied with a list of comparable technologies in the Python Web frameworks.

## Servlets 

Servlets are components which receive Web requests, typically over HTTP, and which respond to such requests by providing output suitable for display by a Web browser. Originally, servlets were the Java equivalent of CGI programs or scripts, albeit without the dependencies on specially named environment variables and other \"legacy\" aspects of CGI.

The implementation of a basic servlet typically includes a number of methods which respond to the different kinds of requests possible in the protocol used to access the application concerned. Since HTTP-related protocols are the most common for Web applications, implementations of methods handling the \"GET\" and \"POST\" request types are typically provided, and each of these methods will access a response object provided by the Web server (or \"servlet container\") in order to produce the application\'s output for the resource represented by the servlet.

### Comparable Technologies 

Python has long been an obvious choice for \"dynamic\", server-side Web applications, from simple CGI scripts to more complicated applications. Whilst most frameworks provide something equivalent to servlets, some frameworks provide mechanisms which are closer to the servlet concept than others.

::: {}
  ----------------------------- --------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------
  **Framework**                 **Equivalent**                                                                                                        **Notes**
  mod_python                    [Request handlers](http://www.modpython.org/live/current/doc-html/pyapi-handler.html)                          
  Webware                       [WebKit Servlets](http://webware.sourceforge.net/Webware-0.8.1/WebKit/Docs/Source/Summaries/Servlet.py.html)   Higher-level classes are also available
  [SkunkWeb](SkunkWeb)   No direct equivalent                                                                                                  Does not appear to promote the servlet model, preferring to promote \"hooks\" from STML
  Zope                          Products and [PythonMethods/PythonScripts](./PythonMethods(2f)PythonScripts.html)                       
  Snakelets                     [Snakelets](http://snakelets.sourceforge.net/) use snakelets as \"servlets\"                                   
  ----------------------------- --------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------
:::

## JavaServer Pages 

[JavaServer](./JavaServer.html) Pages (JSP) is a program-code-inside-HTML template technology, similar to Active Server Pages and other \*SP technologies, but with Java as the programming language of choice.

A JSP resource is composed principally of textual mark-up, usually HTML, which provides a representation of a page to be displayed to users of an application. Mixed in with the HTML are special JSP elements which provide dynamic aspects of the final page, such as substitution of text, inclusion of page components, and repetition of page components. The inputs to the JSP resource which determine the behaviour of such dynamic aspects are typically the properties of an incoming request from the user, combined with additional attributes of the request which are set by the application.

### Beans 

Java Beans are effectively objects with standardised method names which make it easier to refer to \"properties\" of an object. JSP resources can declare their usage of beans and pass information into beans for processing, and then extract information from beans for presentation.

### Scriptlets 

Scriptlets are program fragments which perform more complicated presentation-oriented logic than that permitted through the interaction with beans. With scriptlets, it is possible to construct a loop which wraps up a fragment of HTML; this fragment could then be repeated according to the amount or nature of the data available. Scriptlets appear inside special comment-like tags.

### Tag Libraries 

Tag libraries provide a means of extending the \"vocabulary\" available in the form of special JSP tags. Each such tag can be defined to perform application-level work and to produce output which is then incorporated into the final page. Use of tag libraries should reduce the amount of presentation-oriented logic within JSP resources in the form of scriptlets, whilst concentrating such logic in one place - the tag library\'s implementation for a given tag.

### Comparable Technologies 

Many \*SP systems have been invented for Python. Indeed, there can be a certain amount of confusion about the number of distinct frameworks available and their relation to each other. For a comparable technology, however, one would look for support for clean interaction with application components (beans), support for the extension of the \"vocabulary\" provided through tag libraries, and the ability to embed presentation-oriented logic within resources in a similar fashion to that provided by scriptlets.

::: {}
+:-------------:+:---------------------------:+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| **Framework**                               | **Equivalent**                                                                                     | **Notes**                                                                                  |
+---------------+-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| JSP           | mod_python                  | [Python Server Pages](http://www.modpython.org/live/current/doc-html/pyapi-psp.html)        |                                                                                            |
|               +-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
|               | Webware                     | [Python Server Pages](http://webware.sourceforge.net/Webware-0.8.1/PSP/Docs/index.html)     |                                                                                            |
|               +-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
|               | [SkunkWeb](SkunkWeb) | [STML](http://skunkweb.sourceforge.net/stmlrefer/)                                          |                                                                                            |
|               +-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
|               | Zope                        | DTML                                                                                               | Zope Page Templates (ZPT) is an alternative presentation technology                        |
+---------------+-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| Beans         | mod_python                  | No apparent equivalent                                                                             |                                                                                            |
|               +-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
|               | Webware                     | No apparent equivalent                                                                             |                                                                                            |
|               +-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
|               | [SkunkWeb](SkunkWeb) | [:component:](http://skunkweb.sourceforge.net/stmlrefer/node25.html)                        |                                                                                            |
|               +-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
|               | Zope                        | DTML Methods?                                                                                      | ZPT uses a DOM-based model to access data, rather than a simple object-oriented approach   |
+---------------+-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| Tag Libraries | mod_python                  | No apparent equivalent                                                                             |                                                                                            |
|               +-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
|               | Webware                     | No apparent equivalent                                                                             |                                                                                            |
|               +-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
|               | [SkunkWeb](SkunkWeb) | No apparent equivalent                                                                             |                                                                                            |
|               +-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
|               | Zope                        | Tags are implemented using Products                                                                | ZPT is not entirely compatible with the notion of tag libraries                            |
|               +-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
|               | Spyce                       | [Spyce taglibs](http://spyce.sourceforge.net/doc-tag_new.html)                              |                                                                                            |
+---------------+-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| Scriptlets    | mod_python                  | Part of the core PSP functionality                                                                 |                                                                                            |
|               +-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
|               | Webware                     | Part of the core PSP functionality                                                                 |                                                                                            |
|               +-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
|               | [SkunkWeb](SkunkWeb) | Tags support control-flow concepts                                                                 |                                                                                            |
|               +-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
|               | Zope                        | Iteration is supported using DTML tags, and arbitrary presentation can be coded in the tag classes | ZPT provides DTML-style iteration and other elementary control-flow concepts are supported |
+---------------+-----------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
:::

## Session Beans 

The J2EE framework attempts to provide more than just an HTML template system. Session beans are application-level objects through which interactions between the application and its users take place, and the state of those interactions is held in instances of session beans.

Two kinds of session beans are mentioned in the J2EE framework: stateless and stateful session beans. The difference between the two kinds is that stateless beans remember nothing about previous activities from one invocation to the next, whereas stateful beans do remember things and can be used to hold details of a particular user\'s activities, for example.

In short, stateless beans are effectively \"passive\" interfaces to application functionality, whereas stateful beans are likely to provide many instances of the same interface, each potentially specialised for different users. For Web applications, it is arguably more likely that stateless beans will be in widespread use, although stateful beans could be used in conjunction with sessions provided by the servlet container.

Session beans are created using a \"factory\"-style mechanism known as a \"home\", with different \"home\" instances identified through a reference defined in the application and fetched using the Java Naming and Directory Interface (JNDI) API.

### Comparable Technologies 

Most Python Web frameworks can trivially support access to application components through the use of \"import\" statements either in servlet or scriptlet code (or both). The provision of an abstract interface for acquiring objects by application-specific identifier is apparently not so widespread. Moreover, the interface to application-level components is not likely to be as tightly legislated as is found in the J2EE framework, although one might argue that the benefits of strict method naming stop short of being able to automatically share components between different applications.

## Entity Beans 

Whereas session beans provide a means of supporting interactions between an application and its users, entity beans attempt to support interactions between application components and the data available to the application. Each entity bean represents a bundle of data in the form of an object (or bean instance).

Like session beans, entity beans are obtained through an abstract interface providing \"home\" objects, which in turn provide entity beans upon request. Using a particular \"find\" method, one or several object references can be obtained, each representing data to be accessed in the application.

### Container Managed Persistence 

A container is an abstraction over a particular storage system, and container managed persistence is the mechanism by which data is retrieved from such a storage system, encapsulated by different kinds of objects and, if appropriate, converted back from such objects into representations used by the storage system concerned, all without the objects involved being aware of how the mechanism is implemented. What makes container managed persistence special is that it typically attempts to provide a generic object-oriented abstraction over the retrieval and storage of data.

### Bean Managed Persistence 

Where persistence is managed by the beans themselves, such beans must be aware of how they are represented in a storage system. However, there are certain situations where this is necessary:

- Where a generic abstraction is unsuitable - there may be existing representations of data in a database system, and container managed persistence may not respect such representations (the way data is organised in a database).
- It may be more efficient for the beans to retrieve information, since such objects may know much more about how their data is to be accessed or manipulated.

### Comparable Technologies 

Access to databases is frequently the next step for Web application developers after creating simple dynamic sites. Moreover, it is an attractive notion that data stored in database systems should be accessible using object-like abstractions, as opposed to issuing SQL queries and retrieving result sets. As a result, a number of Python frameworks attempt to support object-relational or object-oriented data stores.

## Transactions 

A pervasive concept in Enterprise [JavaBeans](./JavaBeans.html) is that of a transaction, and there are several ways that transactions can be created and used within an appropriate \"container\". In a fashion similar to that of many relational database management systems, EJB transactions provide the possibility for developers to support changes to data within an isolated context, where such changes can subsequently be \"undone\" if they prove to be inappropriate.

The EJB specification mandates two different kinds of transaction management. One is \"bean managed transaction management\" where the beans (the business objects which access and manipulate data) control the creation and completion or destruction of transactions; in this style of management, code appears in the bean objects to create transactions and to \"commit\" or \"rollback\" such changes explicitly. The other kind of transaction management is \"container managed transaction management\" where the container (in practice, the application server) controls the transactions according to guidelines provided by the developer; in this style of management, the transaction handling is mostly omitted from the code, although in practice, the developer still needs to indicate conditions where transactions would be rolled back (in other words, abandoned, with the changes made being discarded).

### Comparable Technologies 

The EJB transaction support is ambitious in its scope, but potentially provides support for activities which would otherwise need to be written over and over again by the developer for each application. Relatively few frameworks for Python seem to support anything other than access to databases in a transactional fashion, but one might question the need to provide support for transactional data manipulation \"above\" the database, especially if database access is tuned and performs well.
