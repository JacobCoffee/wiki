# Admin/Email

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Mail and Mailman administration 

![/!\\](/wiki/europython/img/alert.png "/!\") *Please note: The administration pages have all been migrated to the new [PSF Systems Wiki](https://psf.projecthut.com/trac/psfsystems/wiki). Please no longer add information to these pages. If you need access to the new wiki, please contact [psf@python.org](mailto:psf@python.org) for details.*

  ----------------------------------------------------
  [/SpamBayes](./Admin(2f)Email(2f)SpamBayes.html)  
  ----------------------------------------------------

Skip says::

    On mail.python.org I currently have Mailman running gate_news directly from

       /usr/local/src/mailman/mailman-bzr/cron/gate_news

    If you really wanted to you could fall back to the original version (it's
    commented out in Mailman's crontab) but given the popularity of the new
    reduced-spam mail version of python-list@python.org I suspect you'd be
    lynched if you did.  (Or forced to eat nothing but Hormel meat products for
    the next month as the angry mob films the new documentary, "Super-Spam Me".

    As executing recently, line 197 & 198 of gate_news.py currently read

       hold_for_approval(mlist, msg, msgdata, LooksLikeSpam)
       raise _ContinueLoop

    I simply commented out the first line to disable holds on highly spammish
    posts.  They should just be dropped on the floor now.  Uncomment that line
    to restore the hold-all-spam-even-really-obvious-stuff behavior.  Note that
    the next block below handles "unsure" posts.  Those will still require
    moderator approval.
