# SecureShell

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

There are several ways to use **Secure Shell (SSH)** in Python.

## paramiko

Paramiko is a native Python implementation of SSH.

- [Paramiko website](http://www.paramiko.org/) \-- project home page

- [https://github.com/paramiko/paramiko](https://github.com/paramiko/paramiko)

- [http://jessenoller.com/2009/02/05/ssh-programming-with-paramiko-completely-different/](http://jessenoller.com/2009/02/05/ssh-programming-with-paramiko-completely-different/) \-- Article by Jesse Noller

## pyssh

- [pyssh website](http://pyssh.sourceforge.net/) \-- project home page

- [pyssh mailing list](http://sourceforge.net/mailarchive/forum.php?forum=pyssh-discuss) \-- not very active (2006-03-26)

## conch

conch is another native implementation of SSH and part of the Twisted Matrix project

- [http://twistedmatrix.com/projects/conch](http://twistedmatrix.com/projects/conch) \-- conch home

## Fabric 

Fabric uses paramiko to implement a higher-level API for performing commands over SSH, particularly for deployment and system administration tasks.

- [http://fabfile.org](http://fabfile.org)

## Spur 

Spur is a thin wrapper around paramiko, aiming to provide a simpler API than paramiko for common SSH operations.

- [https://github.com/mwilliamson/spur.py](https://github.com/mwilliamson/spur.py)

## SSH wrapper 

Some tools just wrap around existing ssh/sftp implementations.

- [keyphrene SSH wrapper, UNIX, Windows & MacOS](http://sourceforge.net/projects/orgkeyphrene/)

- [PySCP pscp wrapper](http://membres.lycos.fr/fredp/python/pyscp.html) \-- wraps Windows `pscp`, which is part of [the Putty suite](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)

## See Also 

- [Wikipedia:SSH](http://en.wikipedia.org/wiki/SSH) \-- wikipedia article on Secure Shell

## Discussion 

I\'m investigating the use of SSH in Python.

I want something that will work in both Windows and Linux, that can operate like sftp/psftp. So, I\'m thinking about paramiko, since it\'s pure Python.

\-- [LionKimbro](LionKimbro) 2006-03-26 00:20:01

You can use org.keyphrene. This library has been tested on Windows, Linux, and MacOS.

\-- Vincent 2006-04-06 18:02:01
