# Admin/Email/SpamBayes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

![/!\\](/wiki/europython/img/alert.png "/!\") *Please note: The administration pages have all been migrated to the new [PSF Systems Wiki](https://psf.projecthut.com/trac/psfsystems/wiki). Please no longer add information to these pages. If you need access to the new wiki, please contact [psf@python.org](mailto:psf@python.org) for details.*

# SpamBayes on mail.python.org 

As a highly visible mail server, mail.python.org receives more than its fair share of spam, originating both from incoming SMTP traffic and from Usenet. Just one part of the suite of tools used to stem the tide, the [SpamBayes](http://www.spambayes.org/) spam filter is integrated into the mail handling system on mail.python.org at both places. In the SMTP processing pipeline it is the last filter applied to incoming mail before it is handed off to [Mailman](http://www.list.org). It is the only filter applied to messages arriving via Usenet, gated between the Usenet newsgroup `comp.lang.python` and the `python-list@python.org` mailing list.

## Integration With Postfix 

SpamBayes is integrated into the mail processing on mail.python.org in a daemon process, `mpo_smtpd` which serves as the local mail transport agent (**correct term?**). This server does more than run SpamBayes, but it does that, rejecting messages which appear to be spam during the SMTP session, passing along messages which appear to be clearly good (ham) and delaying, then later holding messages for moderator review which score in the middle (unsure). The source for the server is in `/usr/local/src/mpo_proxy`.

By agreed upon policy, emails destined for certain addresses on mail.python.org (mostly, but not entirely, addresses associated with individuals) are passed through unfiltered. When a new user is added to the system the `people` file must be updated, the server reinstalled, and the proxy restarted::

    (vi|emacs) people
    sh install.sh

Note that the source directory is just an rsync of a Subversion repository, so you probably don\'t want to directly edit files in the source directory except in emergency situations. If you do edit files in the `mpo_proxy` directory make sure to also apply them to the Subversion repository. If you don\'t have a repository of your own send a unidiff to `postmaster@python.org` with a brief explanation of the changes.

## Integration With Usenet 

Usenet news postings from `comp.lang.python` are distributed to the `python-list@python.org` mailing list using Mailman\'s `gate_news` program. A locally modified version uses SpamBayes to score these posts. Messages which score as spam or unsure are held for moderator approval. Messages which score as ham are forwarded to the mailing list. These changes have been (are being? will be?) propagated upstream to the Mailman developers.

## Care and Feeding 

SpamBayes scores messages based on the collected wisdom stored in a set of known good (ham) and bad (spam) messages. Messages can be scored as ham, spam or unsure. Messages which score as spam are discarded, ham messages are forwarded on to their destination and unsure messages are held for moderator review.

Both messages held by `mpo_smtpd` and `gate_news` will land in the moderator\'s queue(s). `mpo_smtpd` is a little cleaner in its implementation, saving unsure messages to `/var/spool/spambayes/unsure`, one message per file. `gate_news` currently only holds messages for the list moderator but doesn\'t save a copy in the unsure directory. It\'s currently the responsibility of the moderator to forward such messages to someone who can incorporate them into the training database. Fortunately, since this only affects those of us who moderate the `python-list` mailing list, only a few people need to understand this extra step. When moderating such messages, simply use the Mailman moderation forwarding capability to send them to the person primarily responsible for the training database. At the moment that is `Skip Montanaro|mailto:skip@pobox.com`.

### Classifying Held Mail 

I have a typically idiosyncratic way of processing the held messages. I rely heavily on bash history to recall and execute the necessary steps. YMMV. For all of this you need to be root. Feedback on streamlining the process is welcome.

- Collect all unsure messages into an mbox file:

<!-- -->

    (cd /var/spool/spambayes/unsure ; rm -f /tmp/u.mbox ; for m in *.msg ; do cat $m >> /tmp/u.mbox; echo "" >> /tmp/u.mbox; rm $m; done)

- Copy them to your computer where you can process u.mbox using your favorite mail toolchain. (I use VM inside XEmas which gives me full access to the Emacs command/macro facility, speeding up the process substantially.) You need to use your judgement about some messages. Things like subscription confirmation, mailer daemon messages and PSF donation receipts I simply delete. I generally only save one message with a given subject because of the way the training database is managed (see below).

- When you\'re finished, let\'s assume you have segregated the messages into two mbox files `~/tmp/s.mbox` and `~/tmp/h.mbox`. There should be no messages left in `u.mbox`, so you can delete it. Copy the `[sh].mbox` files back to albatross:

<!-- -->

    touch ~/tmp/s.mbox ~/tmp/h.mbox ; scp ~/tmp/[sh].mbox mail.python.org:/tmp && rm -f ~/tmp/[sh].mbox

- Back on albatross (again, you need to be root), tack those new messages onto the end of the proper training database and move the result into place for the next training run:

<!-- -->

    cd /usr/local/spambayes-corpus
    cat /tmp/h.mbox >> ham.mbox.cull ; cat /tmp/s.mbox >> spam.mbox.cull
    mv ham.mbox.cull ham.mbox ; mv spam.mbox.cull spam.mbox

- Now train:

<!-- -->

    sh train.sh

The training scheme currently in use is called \"train to exhaustion\". Mail mesages in the ham and spam collections are trained in alternating small groups. Messages which don\'t classify correctly the first time are retrained in successive rounds. Google for \"spambayes train to exhaustion\" for more detail. When you run the `train.sh` script you will get some progress output, each round generally training fewer and fewer messages until everything is properly classified:

    round:  1, msgs:  576, ham misses: 149, spam misses: 203, 2.6s
    round:  2, msgs:  576, ham misses:  16, spam misses:  30, 2.1s
    round:  3, msgs:  576, ham misses:   2, spam misses:   1, 2.0s
    round:  4, msgs:  576, ham misses:   0, spam misses:   0, 2.0s
    writing new ham mbox...
      324 of   324
    writing new spam mbox...
      252 of   252

It typically only takes three to five rounds to converge to no misses. If it takes longer than that take a look at `tte.log` in the current directory. It lists message ids of the misses. You might have a misclassified message which needs to be removed from the training database or moved from ham to spam, or vice versa. The \"writing\" messages will often write fewer messages into the output ` {spam,ham}.mbox.cull ` than the input. If that\'s the case, just reexecute the `mv` command and retrain.

- Install the result:

<!-- -->

    sh install.sh

The last bit of `install.sh` just tails the current log file. It\'s probably a good idea to take a little longer look at it with `tail -f /var/log/mpo_smtpd/current`.

### Troubleshooting 

TBD. :-/
