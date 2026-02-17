# Django

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [https://www.djangoproject.com/](https://www.djangoproject.com/)

version
:   1.6.2

licence
:   BSD

platforms
:   Unix, Windows, Mac

Python versions

:   \>= 2.6

### Deployment Platforms 

mod_python is preferred, but it has full WSGI support, so it can run with FCGI, etc. It also comes with a standalone Web server for development purposes.

### Suitability 

Django was originally developed and mainly used for content management, but its rich features \-- templating, and automatic generation of database, database access layer, and admin interface generation from a model description given in straight python code \-- are useful in other kinds of web applications.

### URL dispatching 

URLs are mapped to request handler functions using simple regular expressions. A regex may capture parts of the URL, which are then passed to the function as arguments.

### Environment Access 

Django creates an [HttpRequest](./HttpRequest.html) object that contains metadata about the request. This is automatically passed to the function that the URL is mapped to, and gets to create the response.

### Session, Identification and Authentication 

Sessions are propagated using cookies, the session data stored in a dictionary within the request object. Identification / Authentication: For each application, a pretty sophisticated admin interface is generated that knows about superusers, groups, users and privileges. Support for normal users registering themselves exists but isn\'t yet documented.

### Persistence Support 

Django\'s object-relational mapper provides the core of the framework, currently supports PostgreSQL, MySQL, SQLite3, and MSSQL. Django generates production-ready CRUD interfaces from the ORM. The automatic creation of database tables and database abstraction layer from Pythonic model definition is really quite elegant and probably Django\'s most distinctive feature. A very nice feature is that you can still embed SQL in an unobtrusive way within your model\'s methods if you have to, e.g. for complex queries with joins over multiple tables. Thus, the mapper can handle the 90% of the cases that are simple, yet will step aside elegantly where it should.

### Presentation Support 

Django has a Smarty-like template language. It looks like this:

{% block title %}section.title{% endblock %}

### Documentation 

Not 100% complete yet, but what\'s there is phenomenally good. It\'s no coincidence that one of Django\'s lead developers is a professional journalist.

### InTheirOwnWords 

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

Developed and used over the past two years by a newspaper Web operation, Django is well-suited for developing content-management systems. It was designed from scratch to handle the intensive deadlines of a newsroom and the stringent requirements of experienced Web developers. It focuses on automating as much as possible and adhering to the DRY principle.

Includes a template system, object-relational mapper and a framework for dynamically creating admin interfaces.

Ruby on Rails is similar to it, but Django is written in Python and has a few more advanced conveniences for super-quick Web development.

Read the [Django overview](https://www.djangoproject.com/overview/).

### Hosting 

See [https://code.djangoproject.com/wiki/DjangoFriendlyWebHosts](https://code.djangoproject.com/wiki/DjangoFriendlyWebHosts)

### Django Jobs and Developers 

[The Django Jobs Board](https://djangojobsboard.com/) : \[NOT UP ANYMORE\] The Django Jobs Board was built by members of the Django community *for* the Django community. Unfortunately, the platform was recently shut down.

[Django Python Jobs and Developers](https://www.djangojobs.org/) [DjangoJobs](./DjangoJobs.html).org is for listing permanent or freelance jobs for Django / Python developers,it is also a portal for the Django Python community.

[Fully Remote Django (Python) Jobs](https://django.on-remote.com/) The best resource to find fully remote Django Jobs. Very useful since it\'s 100% free and the jobs are really high quality.

### Django Packages 

List and comparison of Django packages.

[https://djangopackages.com/](https://djangopackages.com/)
