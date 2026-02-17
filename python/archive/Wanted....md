# Wanted...

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Wanted:

- a means to participate in Python bug reporting.

Situation:

- I [\[lwickjr](./(5b)lwickjr.html)\] do the bulk of my computing on a computer that seldom connects to the Internet, and then via dial-up.

- I have periodic access to a system with a broadband connection to the Internet, approximately three hours per week.

- During those three hours, I am expected to devote the bulk of my time to specific projects, mostly not of my own choosing.

Proposed solution:

- I would like a Python module to install on both systems.
- On my system, it would collect the information required for a bug report, and save it to a file that can be transported via sneaker-net to the other system.
- On the other system, it would unpack the information from the file, and submit it in an appropriate format to whatever system is established to accept bug reports from this module.

Once the module exists, I would be capable of maintaining it, but I lack the data required to create it in the first place.

If someone is able and willing to create such a module, please arrange that I can download it when I click [here](./here.html).

------------------------------------------------------------------------

Wanted:

- an e-mail client written in Python, which I can then modify for my own uses.

Situation:

- I [\[lwickjr](./(5b)lwickjr.html)\] am unsatisfied with the junk-mail filtering capabilities available in the various e-mail clients I have available.

- The [Python Standard Library](./Python(20)Standard(20)Library.html) contains several modules for processing Internet data in various formats and several other modules for exchanging data via various protocals, but lacks any module that ties them together into ANY kind of client.

- The documentation for those modules appears \[to me\] to be inadaquate for guiding programmers not well versed in Internet-related programming through the process of combining them into functional clients.

Proposed solution:

- I would like a Python module that ties together the various Internet-related data-transfering and data-processing modules into clients with basic functionality and hooks for installing additional functionality.
- Said module should, at a minimum, handle SMTP and POP3 protocals, all data formats in common use on the Internet for e-mail, provide hooks for installing custom filters, and provide a variety of actions for the filters to trigger.
- Such actions should include, at a minimum, deleting the message from the server \[without downloading it if it hasn\'t been downloaded yet\], diverting the message to a selected \"mailbox\", leaving the message on the server \[instead of deleting it\], generating an automatic reply with optional attachments, and other common actions.
- This module will also need to allow the transport of the message-base and the rule-base from one system to another and back again, without disrupting operations. It should be possible to put both databases on a Zip disk for sneaker-net transfer. Operation direct from the removable medium is acceptable.

Once the module exists, I would be capable of maintaining it, provided it makes use of [Python Standard Library](./Python(20)Standard(20)Library.html) modules to handle the Internet-related grunt-work, but I lack the data required to create it in the first place.

If someone is able and willing to create such a module, please arrange that I can download it when I click [here](./here.html).

Resolution:

- I [\[lwickjr](./(5b)lwickjr.html)\] am constructing such a module myself. I use modules smtp, pop3, and email \--I think\-- to handle most of the gruntwork. I have an abstraction of a mailbox, in two flavors: Local and Pop3. I have rudimentary \--but functional\-- commands to blacklist, delete, list, and read messages in a Pop3 mailbox, but the Local mailbox is still an empty class. RFQ/RFC [here](lwickjr), please.

------------------------------------------------------------------------

Wanted:

- Is anyone willing to host some storage for a few modules I [\[lwickjr](./(5b)lwickjr.html)\] have written and would like to share?

Resolution:

- I\'ve posted some of them as attachments to one of [my personal pages here](lwickjr).
