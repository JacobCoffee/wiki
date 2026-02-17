# MacPython/SystemConfiguration

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Note on a solution to problems running the installer for [SystemConfig](./SystemConfig.html) 0.3 on a [MacBook](./MacBook.html) Pro running OS 10.4:

\<pre\> Subject: Pythonic wrapper for the Apple\'s [SystemConfiguration](./SystemConfiguration.html) API Date: Dec 16, 2006 12:59 PM

Bob:

I was trying to install the [SystemConfig](./SystemConfig.html) python wrapper in order to use Nicholas Riley\'s OpenVPN helper script ([http://njr.sabi.net/2005/08/04/overriding-dns-for-domains-in-os-x-tiger/](http://njr.sabi.net/2005/08/04/overriding-dns-for-domains-in-os-x-tiger/) )

I\'m not a python expert by any stretch, but when I ran \"setup.py install\", I got this error:

warngin: no files found matching \'\*\' under directory \'build/lib.macosx-10.3-fat-2.4/SystemConfiguration/UNSystemConfiguration.framework\'

Changing this line in the setup.py script:

- template = \[\'recursive-include build/lib.%s-%s/%s/UNSystemConfiguration.framework \*\' % (get_platform(), get_python_version(), NAME),\],

to this:

- template = \[\'recursive-include build/lib.%s-%s/%s/ Default/UNSystemConfiguration.framework \*\' % (get_platform(), get_python_version(), NAME),\],

finds the files and eliminates the warning.

Is this something which should be fixed? Or did I misunderstand something about the install process? If I just failed to read some instructions, then forgive my oversight.

\</pre\>

I just tried to add the above to [http://wiki.python.org/moin/MacPython/SystemConfiguration](http://wiki.python.org/moin/MacPython/SystemConfiguration) to no avail. Perhaps someone with patience could add
