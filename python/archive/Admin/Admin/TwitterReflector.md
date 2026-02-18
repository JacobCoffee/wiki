# Admin/TwitterReflector

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## History 

![/!\\](/wiki/europython/img/alert.png "/!\") *Please note: The administration pages have all been migrated to the new [PSF Systems Wiki](https://psf.projecthut.com/trac/psfsystems/wiki). Please no longer add information to these pages. If you need access to the new wiki, please contact [psf@python.org](mailto:psf@python.org) for details.*

The Twitter reflector script was originally written by Stephen Crim (stephencrim @ google mail). He originally ran it on his own machine, but was given a login account on ximinez.python.org to run it on a PSF machine.

In June 2010 Twitter changed its authentication method to OAuth, breaking the reflector script. Stephen no longer had time to maintain it, so AMK copied it to the \'amk\' user account on ximinez and modified the script to work under OAuth.

## Behaviour 

Once per minute, the script scans for new tweets that are replies to the \@pycon user. The script takes out the \'@pycon\' string, truncates the text as necessary, and appends \'from \@original-user\'. The truncation is not intelligent, and will happily cut off in the middle of a word or a URL.

## Set-up 

The script lives in \~amk/twitter-reflect/ . This is a Mercurial-versioned directory, so if you make any changes as the super-user, please use \'hg commit\' to record them.

The script is currently run manually. To run it:

      cd ~amk/twitter-reflect
      killall reflect.py
      nohup python reflect.py

Output from the script will be appended to the nohup.out file in that directory. The script will also e-mail exceptions to a configured address; currently this address is AMK\'s personal e-mail. It would be nice to redirect this e-mail to pydotorg-www or some other mailing list, but I\'m nervous about doing so for fear of spamming the list. (The script does throttle exception e-mail and will only send one every 15 minutes, so maybe that\'s just paranoia on my part.)

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite)
