# Asking for Help/Why does IDLE refuse to start on Windows?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: Why does IDLE refuse to start on Windows? 

Bonjour,

after a long time without Python, I loaded Python 262. IDLE is refusing to start, claiming there is a personnal firewall Protection hindering subprocesses. I\'m on Win XP. What should I do?

Thanks on forward

------------------------------------------------------------------------

This is a rather irksome issue, caused by the way personal firewall software works on Windows as compared to other platforms (Linux, Mac OS X, \...). I won\'t bore you with the technical details of this problem, but I\'m not familiar with the way you have things set up, so I will break this into five cases:

1.  You have personal firewall software (ZoneAlarm, BlackICE Defender, \...) installed. This can be handled simply by telling your personal firewall package not to block IDLE from connecting to its subprocess. Also, make sure you don\'t have Windows Firewall turned on too; if you have it on in this case, turn it off.

2.  You are relying on Windows Firewall. You\'ll have to go into Control Panel and tell Windows Firewall not to block IDLE from connecting to its subprocess.

3.  You are behind a home router of some sort (an external box that takes your Internet connection and sort of \"splits it up\", allowing multiple computers to use it, or providing you with a wireless connection). If so, turn OFF Windows Firewall, and uninstall any personal firewall software you may have in addition to the router. All home routers act as firewalls.

4.  Somebody else set your PC up, and you have no clue what is going on. If so, ask them for help.

5.  This is happening with something besides a home PC. If so, talk to whoever runs the IT department there, and ask them for help.

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
