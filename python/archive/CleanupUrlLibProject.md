# CleanupUrlLibProject

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The URL-specific code is spread across three modules (urllib, urllib2, and urlparse). All three modules are rather old and could stand a cleanup and modernization along with a unification into a single module. The modules at [http://wwwsearch.sf.net](http://wwwsearch.sf.net) should be taken into consideration in the process.

- Hi, I\'m interested in this project and would therefore like to receive further information on what you expect it to be. The first thing that came to my mind was rewriting the url modules in order to get parallelity (using select or poll). This would futhermore include a bit of redesign with the main focus on the http protocol. \-- [HelmutGrohne](http://linuxwiki.org/HelmutGrohne "LinuxWiki")

- Possible things to do is to unify the various URL-handling modules more into a single module. Another is to consider whether the API could stand a change (more OO, less OO, total removal of unneeded functions, provide decorators, etc.). Modernization of the code with current Python abilities should speed things up and simplify the code. As for the parallelization, that\'s fine but realize that poll() and select() are in no way guaranteed so you will have to code around it. And I personally would advise against poll() since it is broken on OS X (at least as of 10.3.9; have not checked 10.4). \-- Brett Cannon
  - Thanks a lot for your suggestions. The rough idea of what I can work out will change the API a lot. Indeed I\'d turn a bit towards OO. As for parallelization I know about issues on different platforms. Thus following this approach the parallelization code has to be exchangable and there must be a method to replace it with non-parallel code. Though working with a clean and parallel url retrieving module on some unix would be a nice feature too, right? ![;)](/wiki/europython/img/smile4.png%20";)") So what ever I do, I\'ll (have to) ensure portability as this is intended to go into the Python distribution. \-- [HelmutGrohne](http://linuxwiki.org/HelmutGrohne "LinuxWiki")

- About urlparse, see [\"urlparse brokenness\"](http://mail.python.org/pipermail/python-dev/2005-November/058301.html) for suggestions on improvements to the module. \-- [PaulBoddie](../people/PaulBoddie)

- Am yet another student, interested in taking this project. About combining the three modules, urllib, urllib2 and urlparse, I definitely agree to it, same/similar functionality is spread across three different modules. While all three modules can be combined together into a single module, in a more OO way that would provide all the features of url handling in a much faster way that currently implemented.

\-- [SenthilKumaran](./SenthilKumaran.html)
