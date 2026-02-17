# PowerPiano17/Doodles

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Sometimes, it doesn\'t hurt to play around with programming languages. Python is probably the easiest and most enjoyable language to play around with, so I decided to create this section devoted to playing. Feel free to write a program, edit an existing one, delete an existing one, etc. It\'s like having an open source python-only playground! Attachments are available for these little code \"doodles,\" but please don\'t forget to update the attachments page if you make any changes here.

# Doodle #1 

{{{#A doodle that tells the user what version of Windows they are using, the version, CSD level, and processor configuration. It gives the #win32_ver function of the platform module a nice output engine.

from platform import win32_ver

[SystemInformation](./SystemInformation.html) = win32_ver(release=*, version=*, csd=*, ptype=*) print \'Opperating System: Microsoft Windows\', [SystemInformation](./SystemInformation.html)\[0\] print \'Version:\', [SystemInformation](./SystemInformation.html)\[1\] print \'CSD:\', [SystemInformation](./SystemInformation.html)\[2\] print \'Processor Configuration:\', [SystemInformation](./SystemInformation.html)\[3\] print raw_input(\'Press Enter to quit. \')}}}
