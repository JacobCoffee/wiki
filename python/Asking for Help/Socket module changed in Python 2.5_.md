# Asking for Help/Socket module changed in Python 2.5?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

I just upgraded from python 2.4.2 to 2.5 (r25:51908, Jan 4 2007, 17:18:25) and my program using the xmpp module stopped working. Investigating, it appears that ssl() is no longer part of the socket module, but I can\'t find any documenation to that effect. Here is what I see (opensuse 10.1):

    /usr/bin/python
    Python 2.4.2 (#1, May  2 2006, 08:13:46)
    [GCC 4.1.0 (SUSE Linux)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import socket
    >>> [x for x in socket.__dict__.keys() if x[0] == 's']
    ['sslerror', 'socketpair', 'socket', 'ssl', 'setdefaulttimeout', 'sys']
    >>>
    gpomper@dhcp-10-111-54-146:~/Desktop/Python-2.5$ python
    Python 2.5 (r25:51908, Jan  4 2007, 17:18:25)
    [GCC 4.1.0 (SUSE Linux)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import socket
    >>> [x for x in socket.__dict__.keys() if x[0] == 's']
    ['socketpair', 'socket', 'setdefaulttimeout', 'sys']

Where did ssl go?

------------------------------------------------------------------------

Nowhere as far as I know:

    % python2.5
    Python 2.5c1 (release25-maint:51339, Aug 17 2006, 22:15:14)
    [GCC 4.0.0 (Apple Computer, Inc. build 5026)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    import >>> import socket
    >>> socket.ssl
    <function ssl at 0x5b8170>

Maybe you have something missing from your system which is required to build Python with SSL support.

------------------------------------------------------------------------

Interesting\... any idea what that might be? I grepped all the config\* stuff for ssl and there doesn\'t seem to be any mention of it. Any suggestions on where I start to find out how to build python with ssl support on linux?

------------------------------------------------------------------------

Ok, I found it. It turns out that setup.py does look for ssl.h in various directories and I didn\'t have that file. I checked my packages and the openssl-devel package wasn\'t installed, so I installed that and rebuilt and it works now. I am thinking that there should be some noticable warning when you are missing headers, but at least it works now. Thanks for the reply!

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
