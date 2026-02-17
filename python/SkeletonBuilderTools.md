# SkeletonBuilderTools

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Skeleton Builder Tools 

A skeleton builder tools are tools that takes a directory skeleton, copies over its directory structure to a target folder and uses a template engine to dynamically generate the files.

In alphabetical order:

- [Cookiecutter](http://cookiecutter.readthedocs.org/en/latest/)

  - uses Jinja2 template engine.

  - config file can be in either json and yaml formats.

  - Tested for use with Python 3.3, 2.7, 2.6, Linux, Mac OS X, and Windows.

  - Extremely popular, with over 30 community contributed templates available for Python, Django, Flask, [JavaScript](./JavaScript.html), Ruby, C, Open Stack, and HTML.

  <!-- -->

  - List of [Full feature set](https://github.com/audreyr/cookiecutter#features)

  - 3rd-party: [cookiedough](https://pypi.org/project/cookiedough/) GUI browser/installer with \~4150 cookiecutter templates.

- [django-admin.py startproject](https://docs.djangoproject.com/en/1.5/intro/tutorial01/)

  - (limited to [Django](https://docs.djangoproject.com/) framework)

- [Echafaudage](http://harobed.github.io/echafaudage/)

  - use [tempita](http://pythonpaste.org/tempita/) template engine

  - config file is in json format

  - specific feature : standalone file executable directly with python -c \"\$(curl \...)\"

- [mr.bob](http://mrbob.readthedocs.org/en/latest/)

  - use Jinja2 template engine

  - config file is in ini format

  - specific feature : pre, post [hooks](http://mrbob.readthedocs.org/en/latest/templateauthor.html#hooks)

- [pcreate](http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/project.html?highlight=pcreate) (limited to [Pyramid](http://pyramid.readthedocs.org/en/latest/) framework)

- [Paste Script](http://pythonpaste.org/script/)

### Limited to package creation 

- [python-packager](https://github.com/fcurella/python-packager)

- [modern-package-template](https://pypi.python.org/pypi/modern-package-template/) (deprecated)
