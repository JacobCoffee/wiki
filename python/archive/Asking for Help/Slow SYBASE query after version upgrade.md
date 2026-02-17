# Asking for Help/Slow SYBASE query after version upgrade

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: Why is a query to Sybase slow after a Python version upgrade? 

Python script running long after version upgrade(s) - querying to Sybase, so Sybase Module for Python involved

During server upgrades/refresh, we have upgrade FROM -\> TO below:

[RedHat](RedHat) 4.3 (32-bit) -\> 5.5 (64-bit) / Python 2.3.4 -\> 2.4.3 / Sybase Module for Python (static) 0.39 -\> 0.39

After this upgrade, a Python script used to query sybase tables and extract data and load back to [RedHat](RedHat) server is taking 6x as long.

Network settings have been compared from original server and new server, and network ports for original and new, all match and FTP transfers have ruled out the network configuration as a problem. Are there any known bugs/defects in Phython version 2.4.3 that could be resulting in our situation/experience?

------------------------------------------------------------------------

If the server configuration has remained the same, then it quite possibly is something related to the client configuration, and maybe there is an issue with the client\'s network configuration (or how Python uses that configuration). Frequently, long delays involving network communications become introduced because of things like DNS queries, although this is often something which manifests itself on the server side (when a server process is writing hostnames to a log, for example). Network-related factors can also probably include things like routing (including firewall rules); other factors could include things like SELinux, I would imagine, and Red Hat do tend to encourage SELinux usage by default.

I\'ve looked on the bug tracker ([http://bugs.python.org/](http://bugs.python.org/)) for network-related bugs, but I can\'t find much that suggests a change between 2.3 and 2.4, and I also looked at the [What\'s New](http://docs.python.org/whatsnew/index.html) documents. You might want to [profile](../../performance/PythonSpeed/Profiling) your application, or at least use trace statements, to be sure of where the extra time is being spent, and I imagine that the developers of the [Sybase](Sybase) interface would be the best people to ask about performance issues: Python 2.4 is rather old, and there has been plenty of time for user experiences on such matters to have been reported. \-- [PaulBoddie](PaulBoddie) 2011-06-05 18:25:50

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
