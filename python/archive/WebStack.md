# WebStack

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](../web/WebProgramming).

### Masthead 

URL

:   [https://pypi.python.org/pypi/WebStack](https://pypi.python.org/pypi/WebStack) (Google group: [webstack-discuss](http://groups.google.com/group/webstack-discuss))

version

:   1.2.7 (*2007-10-29*)

licence
:   LGPL

platforms
:   Where most of the supported frameworks can run

Python versions
:   Tested on 2.2.2, 2.3.3, 2.4.1 and 2.5.1 but should work on most releases

### Deployment Platforms 

Supports CGI for the most basic hosting environments, BaseHTTPServer and Twisted for standalone applications, Webware and mod_python for Apache environments, Java Servlet API for Java application servers, Zope 2 for integration with existing content management applications, and Django for those needing to work with fashionable full-stack frameworks.

### Suitability 

WebStack applications should have the luxury of being unaware of their deployment environment. Suitability should really only be an issue in selecting the underlying framework for such an environment.

### Development Interfaces 

The WebStack API is a servlet-like API reminiscent of the request objects from mod_python but has much in common with Webware\'s HTTPRequest and HTTPResponse objects, amongst other sources of influence. Users of the WebStack API could concentrate on building higher-level frameworks which expose different development paradigms (eg. presentation-driven development), although they could also develop applications directly for the API.

Unlike a number of frameworks, WebStack delegates the process of interpreting URLs to other components. Therefore, no \"object publishing\", \"context\" or \"deployment descriptor\" antics are involved, although WebStack does provide classes for handling URLs and dispatching to different resources.

### Environment Access 

Applications and frameworks built on WebStack will typically import Python modules and packages to access services, files and so on.

### Session, Identification and Authentication 

Uses the underlying framework support for users, cookies and sessions (if available). Where no such support is included in the underlying framework, simple functionality has been added.

### Persistence Support 

WebStack does not attempt to cover persistence functionality, although sessions are supported and a simple directory repository class is provided.

### Presentation Support 

WebStack leaves the issue of resource presentation to higher-level frameworks and applications (such as [XSLTools](http://www.python.org/pypi/XSLTools)).

### InTheirOwnWords 

Although there seems to be some demand for more coherency in Python Web development, many of the discussions around standard APIs seem to have ended with no apparent resolution. Rather than merely continue developing the [WebFrameworks](../web/WebFrameworks) overview and its predecessor documents, I thought it would be more effective to actually demonstrate that existing frameworks could be unified under a common API, thus showing that many frameworks do not offer compelling advantages in their APIs for typical Web applications (in that they differ only in stylistic or subjective ways).

Since many frameworks have traditionally been tied to particular hosting environments (one often needs to have a specific long-running process or Web server solution running to use a particular framework), I also wanted to show that various API design decisions are often not defensible by citing the \"unique\" nature of the framework\'s hosting or execution environment. WebStack demonstrates that applications can be written to run in many different hosting environments and can provide the end-user with much more flexibility in deploying such applications than they have with deploying applications written for a handful of traditional frameworks in mind. \-- [PaulBoddie](PaulBoddie)

### Comments 

This framework\'s principal author uses WebStack for his own Web projects, such as [WebOrganiser](http://www.python.org/pypi/WebOrganiser), and receives occasional feedback from other users (for which he is very grateful). WebStack doesn\'t reflect the apparent vigour of other projects in terms of number of commits per day or number of mailing list messages per month (or other fashionable metrics), but remains a central, stable and hopefully reliable component in other works.

### Hosting 

It should be possible to deploy a WebStack-compliant application, along with the WebStack package, in a hosting environment providing one of the frameworks or technologies supported by WebStack.
