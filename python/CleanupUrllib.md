# CleanupUrllib

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Describe CleanupUrllib here.

This proposal aims to clean up the urllib module and proposes a unified module to handle the url specific functions. The approach to implement these changes to be fix the existing identified bugs, implement the changes requested and develop a unified solution modeling the existing available url handling modules.

The bugs which will be fixed with the clean up tasks are:

1\) Implement a timeout method for the connection.

Implementing urllib2.timeout() for timeout at specified intervals and ability to pass a timeout to underlying socket. Urllib and urllib2 uses socket module and does not yet have to feature to timeout when the request has not been served for specified interval of time. Providing a timeout value to the request methods will be an useful addition to urllib.

2\) \[ 600362 \] relocate cgi.parse_qs() into urlparse

url parsing stuff seems distributed among the urlparse and cgi modules The location of the url-handling functions are distributed among several modules, and it would be good to consolidate them to make them easier to find.

The urlparse.urlparse() function splits an url into its relative pieces.However, it does not parse out the query string into a dictionary \-\-- that role is played by cgi.parse_qs(). And to convert a dictionary back to a query string, the programmer needs to know that that function is in urllib.urlencode.

It would be nice to have cgi.parse_qs() and urllib.urlencode() in a unified place, within in the urlparse module if appropriate. This will help reduce the amount of hunting-and-pecking that beginners do when they\'re trying to deal with URLs.

Reference: [http://mail.python.org/pipermail/tutor/2002-August/016823.html](http://mail.python.org/pipermail/tutor/2002-August/016823.html)

3\) \[ 735515 \] urllib,urllib2 to cache redirections.

Urllib / urllib2 should cache the results of 301 (permanent) redirections. This shouldn\'t break anything, since it\'s just an internal optimisation from one point of view \-- but it\'s also what the RFC (2616, section 10.3.2, first para) says SHOULD happen.

Fixes with the patches submitted at sourceforge.

While writing the new modules, only the functionality provided by these patches will be kept intact; but the module as such needs to be re-written supporting the new features of python to enable faster processing. Contacting the authors, informing the changes will be necessary when implementing the changes.

1\) \[ 1648102 \] proxy_bypass in urllib handling of \<local\> macro

Adding of the \<local\> macro in urllib.proxy_bypass is broken. According to the Microsoft documentation for this macro, what should be checked is simply that the host name specified does not contain a period. Since urllib gets its proxy information directly from the Windows registry it would make sense to use the same definitions that Microsoft does. Attached is a patch that does this.

Here is a link to the documentation that specifies this: [http://msdn2.microsoft.com/en-gb/library/aa384098.aspx](http://msdn2.microsoft.com/en-gb/library/aa384098.aspx)

2\) \[ 1664522 \] Fix for urllib.ftpwrapper.retrfile()

When trying to retrieve a none existing file using the urllib.ftpwrapper.retrfile() method the behavior is that instead of an error message a valid hook is returned and you will receive a 0 byte file.

The current behavior tries to emulate what one typically sees with http servers and Dir Indexes, which means:

\- Try to RETRIVE the file. - If that fails, assume it is a directory and LIST it.

3\) \[ 1667860 \] urllib2 raises an [UnboundLocalError](./UnboundLocalError.html) if \"auth-int\" is the qop urllib2 raises an [UnboundLocalError](./UnboundLocalError.html) if \"auth-int\" is the qop If a proxy server is connected to that specifies the \"auth-int\" quality of protection (qop) code\--or any qop code aside from \"auth\", actually\--urllib2 raises an [UnboundLocalError](./UnboundLocalError.html) exception.

4\) \[ 1673007 \] urllib2 requests history + HEAD support Add history off all sent and received headers/requests to addinfourl object. Save redirections history too.

5\) \[ 1675455 \] Use getaddrinfo() in urllib2.py for IPv6 support The number of base Python modules use gethostbyname() when they should be using getaddrinfo(). The big limitation hit when using gethostbyname() is the lack of IPv6 support. This patch for urllib2.py. It replaces all uses of gethostbyname() with getaddrinfo() instead. getaddrinfo() returns a 5-tuple, so additional code needs to wrap a getaddrinfo() call when replacing gethostbyname() calls.

Major proposal being the unification of the module, this has to research into the backward compatibility and communication with the older modules aspects.

The design of the unified module can follow the same as the mechanize module; which provides bug fixes, simpler interface and co-existing features of urllib2 and also provides communication mechanism for urllib2 objects to mechanize objects.

Compliance to RFC3986 and RFC3987 is stressed in all the changes.

As in [mechanize](mechanize) and urlgrabber,Implement higher level interfaces to url module,which can accomplish most common tasks. urllib is a relatively raw inteface to the underlying protocols, urlgrabber much better interface to support urlgrabbing.It is extremely simple to drop into an existing program and provides a clean interface to protocol-independent file-access.

Patch 1462525 for writing a new uriparse library has received comments/suggestions.

\[Python-Dev\] Some more comments re new uriparse module, patch 1462525 John J Lee jjl at pobox.com Sat Jun 3 01:19:01 CEST 2006 As that patch tries to adhere to new RFC3986, understanding the suggestions is required.

\* Providing better consistency to PROXY SUPPORT Features of urllib modules.

\* Enable caching feature in urllib (as present in the mechanize module) and Include a function to query if a particular url is in cache.

The following cases, can be adopted from the mechanize module.

1.  Handler classes HTTPRefreshProcessor, HTTPEquivProcessor,

- HTTPRobotRulesProcessor

  1.  HTTPRedirectHandler.HTTPRequestUpgradeProcessor and

  [ResponseUpgradeProcessord](./ResponseUpgradeProcessord.html) classes.

  1.  Request and response objects from code based on urllib work with
      - mechanize,urlgrabber and other majorly used modules.

\* Understand the realworld scenarios of URL Encoding with respect to unicode and discuss about implement changes required. Comment by Mike Brown at python-dev. [http://mail.python.org/pipermail/python-dev/2007-March/072330.html](http://mail.python.org/pipermail/python-dev/2007-March/072330.html)

\* Writing Unit Tests for all the changes.

\* Update the Documentation for all the affected modules.

With the above mentioned proposal, the plan for completion of Cleaning of Urllib can be drawn. As reviewers at python-dev inform that the task should be looked from Python 3K point of view, I would be discussing this with my mentor and would be willing to work beyond the SOC time frame with an eye towards inclusion in Python 3K release.

Rough Plan:

Phase 1: - Start with Bug Fixes. - After homogeneous implementation of code, identify the overlapping area. - Understand the RFC specifications. - Identify other standard library dependencies on the existing code. - Draw the table for dependency breaks with changes to urllib. - Discussing with Mentor and device a plan to handle the dependency breakups.

Phase 2: - Draw time line for the activity for urllib merge. - Draw time line for the project activity for handling dependencies in other standard lib modules.

Phase 3: - Design and Develop the urllib modules.

Phase 4: - Write tests for changes. - Write tests for other standard lib modules.

Phase 5:

\- Running Python Test Suite with changes implemented. - Documentation update for Python.

Thank you.

About Author:

I am O.R.Senthil Kumaran, a student currently undertaking a part time course on Introduction to Artificial Intelligence with Indian Institute of Science, Bangalore. I have completed my under graduation in Computer Science and Engineering with National Engineering College, Tamil Nadu, India. I am working for Dell Product Group in India, where Python is used for Test Automation.

I have about 1 year of experience with Python Programming Language; I worked with C Programming language for more than 3 year.

I have contributed to a number of Free Software Projects in terms of bug-reports, bug-fixes,implementing change request, and sometimes developing features.

I wish participate in large free software projects to understand the mechanics and interact with developers gain knowledge. I think Google Summer of Code can give me a chance to work with Python Software Developers with this proposal of mine on cleanup task of urllib.

Free Software Projects which I have worked so far: 1) Rapple. [http://rapple.sf.net](http://rapple.sf.net). Contributed code to html parsing facility as a developer. Involved in unit testing, bug fixes.

2\) Nanoblogger. [http://nanoblogger.sourceforge.net/](http://nanoblogger.sourceforge.net/) Testing and Changes during the initial stages of the project.

3\) Libsmbios [http://linux.dell.com/libsmbios/](http://linux.dell.com/libsmbios/) Unit-testing code to test features

Apart from that, smaller projects which I have done, include: 4) ngwallpaper. [http://code.google.com/p/ngwallpaper/](http://code.google.com/p/ngwallpaper/) In progress and fun time project:

5\) PyLJvim [http://www.vim.org/scripts/script.php?script_id=1724](http://www.vim.org/scripts/script.php?script_id=1724) Python [LiveJournal](./LiveJournal.html) Plugin for VIM Editor.

6\) Code snippets at uthcode. [http://uthcode.sarovar.org](http://uthcode.sarovar.org) Snippets of C Programming Code, solving K&R Problems.

Home Page: [http://puggy.symonds.net/\~senthil](http://puggy.symonds.net/~senthil) Blog: [http://phoe6.livejournal.com](http://phoe6.livejournal.com)
