# Zope2Sprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Signed up:

- Chris [McDonough](./McDonough.html) ([chrism@plope.com](mailto:chrism@plope.com)) (availablility: Mar 20 - Mar 23)

  [PaulWinkler](../people/PaulWinkler) (availability: Mar 20 (mid-afternoon) - Mar 23)

  Duncan [McGreggor](./McGreggor.html) (availability: Mar 20 (mid-afternoon), Mar 22,23)

Topic Suggestions for Zope 2 sprint at Pycon

- (please add more topics!)

<!-- -->

- Bugathon
  - Maybe boring but really useful: we haven\'t had a Bug Day in a loooong time. There are well over 1000 active bugs in the Collector. That\'s ridiculous. How many do you think we could stomp out with 2-6 smart Zopatistas in one room?

  Improved Large Blob Support
  - Downloading and uploading large binary files to Zope sucks rocks. ZEO may exacerbate the issue, I\'m not sure. Chris, I know you\'ve worked on this before \... ZC has some code but they tell me it\'s not production-quality and nobody has time to work on it\... maybe we could tackle it for this sprint. This would be very useful to my

    employer and would help justify my attending the sprint ![;-)](/wiki/europython/img/smile4.png%20";-)") - [PaulWinkler](../people/PaulWinkler) Addendum: I now suspect that 99% of the problem in practice is due to the initial load time when using ZEO. Without ZEO, zope benchmarks much slower than apache on localhost - but across a network zope is very close to apache. Adding ZEO to the mix is about 10 times slower. After that, if the data (or most of it) is in the ZEO cache, speed is very close to plain-Zope speed. More testing needed.

  CMF Core / Default
  - There\'s probably plenty of useful work that could be done on CMF. Suggestions?

  Documentation
  - There\'s a number of things that could use attention \... The API reference is outdated and hard to maintain: it lives in its own little corner of the CVS tree, doesn\'t use docstrings of actual classes or interfaces, omits lots of useful information, contains at least

    one big lie ([ObjectManagerItem](../archive/ObjectManagerItem)), and is hard to synchronize with the online Zope Book API reference. We could create & implement a better plan. The Zope Book hasn\'t been updated in about a year and does not cover 2.7. We could spend a day or two editing the book. :-P The Developers\' Guide could probably use attention\... at least, integrating the accumulated user comments. The Backtalk Book product used for all of the above docs could really benefit from a new feature: an auto-generated table of contents within each chapter, showing the structure of the chapter. This would really help in the HTML version - some of the chapters are really long!

  Fix Sessions
  - Help Chris bail himself out of session hell!

  Event Service
  - Implement Chris\' event scheduling proposal: [http://plope.com/Members/chrism/scheduling_service](http://plope.com/Members/chrism/scheduling_service)

  Improved Error Log Pages
  - Some things I\'d love to see in Error Log pages: When error is in a ZPT:
  - Line number of the error in the ZPT When error is in a Script or ZPT:
  - value of here/context, container, and template, giving full acquisition path and meta_type
  - value of all names in the current scope. This is potentially problematic (e.g. when a name is bound to a 10,000-character string, or a binary blob, or a 500-element list, or\...). But some effort could be made to present useful information\... type of the object at the least. I\'m sure we could come up with others, but the above would really help. Finally, when logging errors to the event log, we should NOT dump HTML into the log. yuck!
