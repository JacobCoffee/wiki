# LaunchpadTracker

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Launchpad is a collection of services including bug tracking, translations and specification tracking. It is the official Ubuntu bug tracker and is also used as the official bug tracker by about 150 upstreams. In addition, there are about another 250 communities which coordinate bugs between Launchpad and their own bug infrastructure.

Some of the highlights of Launchpad bug tracking are documented here:

- [http://help.launchpad.net/MaloneHighlights](http://help.launchpad.net/MaloneHighlights)

## Python Bugs Import 

The Python bugs from Source Forge have been imported into a demonstration instance, also containing a copy of the production data:

- [https://demo.launchpad.net/products/python/+bugs](https://demo.launchpad.net/products/python/+bugs)

## Outgoing Email Filter 

To avoid spamming uninterested people, the outgoing email for the demo Launchpad instance is being filtered. We can whitelist email addresses on request (email [james.henstridge@canonical.com](mailto:james.henstridge@canonical.com)). The infrastructure committee\'s emails are white listed:

- Brett Cannon (brett at python.org, bcannon at users.sourceforge.net)
- Richard Jones (richard at python.org)
- A.M. Kuchling (amk at amk.ca, akuchling at users.sourceforge.net)
- Martin v. Löwis (martin at v.loewis.de, loewis at users.sourceforge.net)
- Barry Warsaw (barry at python.org, bwarsaw at users.sourceforge.net)
- Thomas Wouters (thomas at python.org, twouters at users.sourceforge.net)

## Accounts 

Accounts for each bug reporter, assignee or commenter have been created using the `$USERNAME@users.sourceforge.net`{.backtick} address. People can claim the account using the password recovery page:

- [https://demo.launchpad.net/+forgottenpassword](https://demo.launchpad.net/+forgottenpassword)

For people who already had launchpad accounts, the `$USERNAME@users.sourceforge.net`{.backtick} account can be merged here:

- [https://demo.launchpad.net/people/+requestmerge](https://demo.launchpad.net/people/+requestmerge)

## Old Bug Numbers 

Each imported [SourceForge](SourceForge) bug has a nickname assigned of the form \"sfNNNN\", where NNNN is the old bug number. This makes it easy to look up bugs by the old SF bug number. For example, [bug 1101399](http://sourceforge.net/tracker/index.php?func=detail&aid=1101399&group_id=5470&atid=105470) is accessible as [https://demo.launchpad.net/bugs/sf1101399](https://demo.launchpad.net/bugs/sf1101399)

## Email Interface 

The Launchpad email interface is described here:

- [https://help.launchpad.net/UsingMaloneEmail](https://help.launchpad.net/UsingMaloneEmail)

For the demonstration launchpad instance, the bug submission email address is `new@bugs.demo.launchpad.net`{.backtick} and bugs can be updated with `NNNN@bugs.demo.launchpad.net`{.backtick} addresses.

Submitting new bugs or changing the status of a bug by email requires that the message be PGP signed with a key registered to your Launchpad account.

## Feature Requests 

We welcome feature requests, which can be filed in Launchpad at:

- [https://launchpad.net/products/launchpad/+filebug](https://launchpad.net/products/launchpad/+filebug)

Note that this URL is for the production Launchpad instance. Bugs filed against Launchpad in the demo instance will not be seen and may be blown away in the future.

## Coming Soon 

- Shorter bug URLs \-- the main python bug listing URL will be shortened to `https://demo.launchpad.net/python/+bugs`{.backtick}

## Status 

- ownership of python product set to python-infrastructure team

- bug contact set to python-dev team, whose email address is set to the existing `python-bugs-list@python.org`{.backtick} (not added to the outgoing email filter though, so won\'t receive email).

- [SourceForge](SourceForge) bug data imported.

- incoming and outgoing email support enabled for demo launchpad instance, subject to outgoing email whitelist.

## Questions 

Stephane:

- Where can I download this tracker and how can install it. I saw this already in the past but did not understand what to do.

Bignose:

- My understanding is that Launchpad is not free software; we\'re currently unable to examine the source to ensure it does what we expect (and \*doesn\'t\* do what we don\'t expect). Why is a non-free tracker being considered at all for Python?

  The [word on the street](http://sayspy.blogspot.com/2006/06/request-for-test-trackers-to-get.html): \"We want the best solution possible without being political.\" Sounds like a minor [BitKeeper](./BitKeeper.html) incident in the making, but then [SourceForge](SourceForge) isn\'t entirely run on open source software, either. \-- [PaulBoddie](PaulBoddie)

------------------------------------------------------------------------

[CategoryTracker](CategoryTracker)
