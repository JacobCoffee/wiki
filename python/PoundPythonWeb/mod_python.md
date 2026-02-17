# PoundPythonWeb/mod_python

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

At [#python.web](PoundPythonWeb) we warn against using mod_python. Here\'s a handful of the reasons:

1.  It complicates your upgrade process, as versions of Python, Apache, and mod_python must be coordinated. The appropriate versions are not always available for some combinations.

2.  It makes user separation or chrooting of webapps impossible.

3.  If you\'re using PHP and mod_python, and you\'re using MySQL in both languages, you generally **must** coordinate versions of MySQL as well, or suffer lots of configuration headaches. The same applies for many other popular C libraries.

4.  Apache\'s processes will be heavier because you\'re embedding a python interpreter in it.

5.  Debugging a wsgi app is a lot easier.

6.  mod_python is a module for Apache, which is tested less than other well known Apache modules such as mod_proxy. Because of this reason the server administrator (which might not be you) might not want to install this module for security reasons.

7.  You wont find a lot of hosting companies offering mod_python, which makes wsgi applications (which can be deployed through several ways) very flexible in your quest for a hosting company.

8.  Using nginx as a front-end is usually a more speedy and flexible solution.

9.  When using mod_python.publisher you have to keep in mind that any object globaly accessible with string representation is exposed to the web except you add an underscore in front. If not thought on ahead this kills your code in notime (so make sure to read this first ![:))](/wiki/europython/img/smile3.png ":))")
