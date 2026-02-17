# PyOhio2008/Talks

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

= PyOhio 2008 Scheduled Talks =

+-------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
|       | Auditorium                                                                                                     | Loft                                                                                                                                          |
+=======+================================================================================================================+===============================================================================================================================================+
| 9:00  | Library opens; Registration                                                                                                                                                                                                                                    |
+-------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| 9:30  | Talking to The Web with Python                                                                                 |                                                                                                                                               |
+-------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| 10:30 | TurboGears 2                                                                                                   |                                                                                                                                               |
+-------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| 11:30 | Lunch                                                                                                          |                                                                                                                                               |
|       |                                                                                                                |                                                                                                                                               |
|       | Lightning Talks                                                                                                |                                                                                                                                               |
+-------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| 12:30 | [PostgreSQL and Python](attachments/PyOhio2008(2f)Talks/postgres_python.ppt) |                                                                                                                                               |
+-------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| 1:30  | Iteration in Python                                                                                            | [Cross Platform Desktop Apps w/ Python & GWT](attachments/PyOhio2008(2f)Talks/CrossPlatformDesktopApps.pdf) |
+-------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| 2:30  | Paver: easily manage Python code                                                                               |                                                                                                                                               |
+-------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| 3:30  | [Decorators are fun](http://scratch.tplus1.com/decoratortalk)                      | BEA WebLogic Scripting with Python                                                                                                            |
+-------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| 4:30  | Google App Engine                                                                                              |                                                                                                                                               |
+-------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| 5:30  | Poster session                                                                                                 |                                                                                                                                               |
|       |                                                                                                                |                                                                                                                                               |
|       | Prize giveaway                                                                                                 |                                                                                                                                               |
+-------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| 6:00  | Library closes                                                                                                                                                                                                                                                 |
+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

:::::: 
### Talk Materials

::: 
#### Cross Platform Desktop Apps w/ Python & GWT

[YADAF Slides](attachments/PyOhio2008(2f)Talks/CrossPlatformDesktopApps.pdf)

[YADAF Code](http://code.google.com/p/yadaf/)
:::

::: 
#### [Decorators are fun](http://scratch.tplus1.com/decoratortalk)
:::

::: 
#### [PostgreSQL and Python](attachments/PyOhio2008(2f)Talks/postgres_python.ppt)
:::
::::::

:::::: 
### Talking to The Web with Python (Auditorium, 9:30)

::: 
#### Presenter

Gary Bernhardt
:::

::: 
#### Summary

Web frameworks like Django and TurboGears have drawn attention to Python\'s presence on the server side of the web, but there are also powerful client-side tools available. This talk will be an overview of two such tools:

> 1\. Beautiful Soup, an XML/HTML parser that\'s extremely robust in the presence of invalid markup. It allows the programmer to gloss over the fine structure of a document, focusing only on the parts that matter for the application.
>
> 2\. Universal Feed Parser, an RSS/Atom parser designed to be tolerant of invalid documents. It goes farther than Beautiful Soup by normalizing feeds\' structure and hiding the differences between RSS and Atom.

These libraries make it easy to deal with the inconsistent and often invalid data that are so common on the web. They have a wide range of applications, from data mining to mashups to thick client applications. For this talk, fine details of the APIs will be avoided; instead, practical use cases will be highlighted, especially those where the libraries can be combined for greater effect.
:::

::: 
#### Experience level

Intermediate level. A basic familiarity with HTTP, HTML, and RSS/Atom concepts will be assumed.
:::
::::::

:::::: 
### TurboGears 2, the next-gen next-gen framework (Auditorium, 10:30)

::: 
#### Presenter

Mark Ramm
:::

::: 
#### Summary

TurboGears 2 is the next generation of the TurboGears framework. This talk explain how TurboGears, Rails, Django, and other \"next-generation\" fell short, and why a new generation of full-stack web-framework was needed. Obviously, TurboGears, Rails, and Django meet lots of people\'s needs, and have made web application development better. But there\'s still more to be done, and TurboGears 2 is an attempt move \"next-generation, full-stack, rapid application development\" forward, so that it can solve a whole new set of problems.
:::

::: 
#### Experience level

Assumes some knowledge of Python, and web development but does not assume any prior familiarity with TurboGears, Django, or Rails.
:::
::::::

:::::: 
### PostgreSQL and Python (Auditorium, 12:30)

::: 
#### Presenter

Brent Friedman
:::

::: 
#### Summary

1.Brief overview of database connectivity, to gauge audience familiarity level 2.Brief history of postgresql 3.Overview of pg/python 4.Overview of psycopg2 (multi-threading, connection pool, etc.) 5.Live demo with pg/python 6.Common gotchas (errors, troubleshooting, etc.) 7.Questions
:::

::: 
#### Experience level

Beginner
:::
::::::

:::::: 
### Iteration in Python: Iterators, Generators, Itertools, and Special Methods (Auditorium, 1:30)

::: 
#### Presenter

Brandon Mintern
:::

::: 
#### Summary

A key paradigm in Python is iteration over collections of data. Python has several powerful facilities that make using and defining that iteration quite straightforward. In my talk, I will compare and contrast iterators and generators, discuss how to define iteration in a custom class, and show how the generator-based itertools module can make complex iteration patterns simple and efficient.
:::

::: 
#### Experience level

The talk should benefit all but the most advanced Python programmers. The target audience will have some Python experience, but no specific former knowledge will be necessary.
:::
::::::

:::::: 
### Cross Platform Desktop Applications with Python and GWT (Loft, 1:30)

[YADAF Slides](attachments/PyOhio2008(2f)Talks/CrossPlatformDesktopApps.pdf)

[YADAF Code](http://code.google.com/p/yadaf/)

::: 
#### Presenter

Nicholas Bastin
:::

::: 
#### Summary

This session will introduce an application server which will allow developers to write Python backend code for a GWT (or any JSON client) interface without having to handle anything related to file serving or JSON translation on the server side, which is all taken care of automatically. Application developers merely load an application instance into the server and their application APIs are exposed as a JSON web service to be used with GWT or similar web-based UIs, thus making AJAX available as a desktop application framework without any need for developers to understand the ins and outs of application servers. This session will introduce this framework and also take discussion on future direction such as supporting other RPC mechanisms (SOAP, etc.) and deployment of stripped down browsers.
:::

::: 
#### Experience level

Intermediate to Advanced
:::
::::::

:::::: 
### Paver; easily manage Python code (Auditorim, 2:30)

::: 
#### Presenter

Author: Kevin Dangoor

Presenter: Mark Ramm
:::

::: 
#### Summary

An introduction to Paver.

Paver is a build, distribution, installation and deployment scripting package specifically geared to Python projects. It uses distutils and setuptools for packaging up code, Sphinx for documentation, virtualenv and zc.buildout for installation and wraps it all in an easy-to-use scripting setup. Using a simple model based on \"tasks\" (similar to Ruby\'s Rake), Paver helps you to have fewer random shell scripts, fewer configuration files, less duplication of project metadata and lets you stick to Python as much as possible.
:::

::: 
#### Experience level

Assumes some knowledge of Python, but does not assume knowledge of Python project management.
:::
::::::

:::::: 
### [Decorators are fun](http://scratch.tplus1.com/decoratortalk) (Auditorium, 3:30)

::: 
#### Presenter

Matthew Wilson
:::

::: 
#### Summary

\[[http://scratch.tplus1.com/decoratortalk/](http://scratch.tplus1.com/decoratortalk/) View the slides for the presentation here\].

This talk will start with a friendly walkthrough of decorators for people that have never seen them, then go into some straightforward examples, then finish with a few complex ideas. Details:

> - Write the simplest possible decorator.
> - Write a decorator that accepts arguments.
> - Preserve the function signature.
> - Coerce values into a function into types.
> - Log values coming out of a function.
> - Add a timeout to your functions.
> - Review generic functions.
> - Use Phillip Eby\'s PEAK-Rules to write generic functions.
:::

::: 
#### Experience level

Hopefully, there will be something for everyone. Novices might enjoy the material at the beginning mostly, while experts would likely be more interested in the generic functions discussion.
:::
::::::

:::::: 
### BEA WebLogic Scripting with Python (Loft, 3:30)

::: 
#### Presenter

Matthew K. Williams
:::

::: 
#### Summary

The WebLogic Scripting Tool (WLST) is one of the least documented and least understood aspects of WebLogic 9/10. However, it is very powerful and useful for daily tasks, whether they be administrative or monitoring the servers. WLST uses Jython, a version of Python which runs within the Java Virtual Machine. This session provides an overview of WLST, as well as a tutorial consisting of a number of real-life applications of WLST and python scripting with BEA\'s WebLogic platform.
:::

::: 
#### Experience level

The attendee is expected to have some level of exposure to Python
:::
::::::

:::::: 
### Beginning web development with Python and Google App Engine (Auditorium, 4:30)

::: 
#### Presenter

Pradeep Gowda
:::

::: 
#### Summary

Google has thrown open its cloud computing infrastructure to the developer community via \"Google App Engine\"(GAE). The Google Appengine allows the programmers to develop Python applications which can then be hosted on google infrastructure. This has huge implications for making web application development accessible to large cross section of python developers. In this talk, we will attempt to understand what GAE provides and how best to make use of it.

> - The Google App Engine(GAE) offering
>
> - Hello world! with Google App Engine
>
> - 
>
>   The components of a web app and GAE
>
>   :   - Data store, URL mapping, static pages, templates
>
> - Processing user input
>
> - Storing and retrieving data
>
> - Presentation and templates
>
> - Using \"web Frameworks\" (Django, web.py)
:::

::: 
#### Experience level

Beginner
:::
::::::
