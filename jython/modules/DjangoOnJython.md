# DjangoOnJython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Using Django on Jython 

Finally, Django works on Jython, without any special patching. Here are the steps to get Django on Jython running:

1.  First, get a fresh version of Jython. Any release after 2.5.0 should work fine.

2.  Check out and install Django 1.2.5.
    - $ svn co http://code.djangoproject.com/svn/django/trunk/ django
          $ cd django
          $ jython setup.py install

      You may also like to make an alias for \"django-admin.py\". Very useful if you also use Django with CPython:

          $ alias django-admin-jy="jython /path/to/jython-dev/dist/bin/django-admin.py"

3.  Download and install the latest release of django-jython:
    - $ wget http://django-jython.googlecode.com/files/django-jython-1.2.0b1.tar.gz
          $ tar xvfz django-jython-1.2.0b1.tar.gz
          $ cd django-jython-1.2.0b1
          $ jython setup.py install

4.  Start a project.
    - $ django-admin-jy startproject myproject

5.  Edit `myproject/settings.py`{.backtick} and change the `DATABASE_ENGINE`{.backtick} to `doj.backends.zxjdbc.postgresql`{.backtick}.

At this point, you can follow the great [Django documentation](http://djangoproject.com/documentation/), remembering to use the `jython25`{.backtick} command instead of `python`{.backtick}, and the `JYTHONPATH`{.backtick} variable instead of `PYTHONPATH`{.backtick}. Have fun!

## Deployment 

See [http://packages.python.org/django-jython/war-deployment.html](http://packages.python.org/django-jython/war-deployment.html)

## Troubleshooting 

### Running the test suite on Windows 

Seems like there is an issue with popen() on windows, which blocks the Django test suite. You can try skipping the offending test using these two patches (against Django 1.0.2), written by Victor Ng:

- [http://tinyurl.com/bqfcco](http://tinyurl.com/bqfcco)

- [http://tinyurl.com/aarjx2](http://tinyurl.com/aarjx2)

**Update (03/04/11): Not sure if this is an issue any longer, please edit if you run into it using the latest versions**

### Using MS SQL Server 

The Django-Jython 1.2.0b1 release is in beta as of 03/04/11. It should be compatible with Oracle, MySQL, and PostgreSQL. If you need to use MS SQL Server, you will still need to use Django version 1.1.x until otherwise noted.
