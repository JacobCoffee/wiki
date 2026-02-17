# WebProgrammingTemplateHelp

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### Masthead 

URL

:   

version
:   The current stable version and its date, the development version can be added as well

licence
:   GPL, LGPL, Python licence etc.

platforms
:   restrict entries to those platforms known to work, perhaps distinguishing those platforms which are supported if commercial support is available

Python versions
:   see platforms

### Deployment Platforms 

It is usual for Web application frameworks to make use of existing technological infrastructure to provide an environment for application development. In other words, such frameworks do not always implement all of the services required to deploy and run a Web-based application. Therefore, developers who wish to use a particular framework need to be aware of how that framework integrates with other software components - these other components are the software platforms which the framework itself is deployed on.

Many Python frameworks for Web applications integrate with (or are deployed on) \"traditional\" Web server software, such as Apache Server, using a number of mechanisms including Common Gateway Interface (CGI) and Web server plug-ins. Some frameworks attempt to provide the functionality of a Web server, with consequences for maintenance, deployment issues, and so on.

The deployment platforms (and issues) can exclude certain frameworks from certain environments; for example, restrictive application hosting environments forbid the execution of \"long-running processes\". Coverage of the suitability of a framework will therefore be included in the description of each framework.

### Suitability 

### Development Interfaces 

Whilst Python frameworks are likely to encourage the use of Python source code to implement functionality, the nature of this code can take a number of different forms. An example of a recognisable development style is that of a CGI-based program which uses the Python library\'s cgi module (or an equivalent replacement) to provide access to the details of incoming Web requests. Some frameworks may encourage the \"CGI style\" whilst others encourage a \"servlet style\", inspired by Java servlets, which promotes object-based \"request handlers\", as opposed to Python programs or modules.

This document describes the nature of the code required to implement an application by associating each coding style with a number of recognisable style types, at least where this is appropriate.

### Environment Access 

In order for \"handler\" components to integrate with other application functionality, such as common \"business logic\" which may be shared between applications or different application portions, certain mechanisms may be provided to locate such functionality, as well as shared or external resources and the general environment of the underlying platform. Some frameworks may principally use the standard Python import mechanism to find packages, whereas some frameworks may provide other means to access different environments - Zope\'s object database offers an environment which combines resource and component access, for example.

### Session, Identification and Authentication 

The use of the term \"session\" on its own can be confusing, especially in the context of the terminology of particular Web frameworks. Therefore, this document uses the following terms:

Session:: Something which identifies a participant in a Web transaction as a distinct visitor, agent or user. Session implementations must exclude the possibility of confusing two different visitors (believing that they are identical) or refusing to acknowledge the identity of a previous visitor as the same visitor upon subsequent visits.

Identity and Identification:: The identification of a visitor permits the continued recognition of such a visitor as a distinct and known participant in Web transactions. However, identification alone does not assign any meaning to the assigned identity.

Authentication:: The assignment of additional meaning to a visitor\'s identity, relevant to the application, making that visitor a genuine user of the application. Such additional information can be used by an application to determine which actions are available to the user.

### Persistence Support 

In the context of Web applications, the term persistence is frequently used to mean \"the recording of visitor-related information which can be reused upon subsequent visits by the same visitor\". Thus, persistence is often used to record session information, although certain kinds of Web applications may involve the interaction of users with shared or underlying resources, and persistence can also be taken to mean \"convenient access to application resources\".

### Presentation Support 

Although other documents and resources exist which catalogue template and presentation system implementations, it is still worth documenting the presentation mechanisms which are supported as \"first class\" in the different frameworks. Such integration between frameworks and presentation systems can be seen in certain systems such as PHP and ASP, while JSP remains a \"preferred\" presentation technology for many J2EE-based applications.

### InTheirOwnWords 

A short abstract by the developers:

**What is it that makes your framework different from or better than the other frameworks?** This could be seen as advocacy, but by providing information like this, developers can decide whether the focus of your framework is compatible with their perspectives or needs.

**What is (or initially was) your motivation to develop the framework?** Something which is often said about open source development is that people are usually motivated to start a project because everything else does not quite fit their needs. This question attempts to assess whether this was the case with your framework, and whether it still is.

**In which ways do you see the framework developing?** Is the framework going to remain \"small, simple and focused on doing one thing well\" or are there higher ambitions? This is quite important for developers because the answer to this question will dictate whether they will need to integrate your framework with other frameworks and systems, or whether they will need to extend your framework.

**What kinds of applications are most suited to the framework?** If your framework was designed to support a particular kind of application well, then developers of such applications will surely want to know!

The current entries are mostly taken from the home page of the projects.

### Comments 

These are from users of the framework, those that tried and failed and those that tried multiple frameworks and then decided on one. Framework authors may reply to comments, but should use the [InTheirOwnWords](InTheirOwnWords) tag.

### Hosting 

This should be a list of websites where applications using this framework can be hosted. This could also be a comment along the lines *any CGI with Python \>= 2.1 will do*
