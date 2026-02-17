# PackagingWG/2020-12-15-pip-team-meeting

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Tuesday 15 Dec

Participants

- Sumana
- Ee
- Pradyun
- Nicole
- Bernard

Agenda

- status and blockers
  - Pradyun: fine. Need to cut a new pip release because 20.3.2 was b0rked. No blockers. Now keeping up with issue tracker
    - as Ee points out: pip CI calling the real PyPI XML/RPC is something to fix - tests calling internet services \-- something to fix
    - search endpoint is turned off till further notice because of current level of attempted requests. \[Ee is working on escalating this to find source of excess requests and turn off\]
      - fix is merged in pip CI already

  - Bernard: \[personal status\]. Working through report on research output, did some work on what we will do in research training.
    - it would be useful to know what the consensus is on when the trainings will happen.
    - starting to think about all the things one has learned, questions come up spontaneously, etc. while synthesizing all one has learned

  - Nicole: \[personal status\]. Today: reviewing feedback on documentation writeup & summary, maybe share to wider audience. That would be the docs side of work done! Then: turning back to functionality epic, wrapping up and summarizing and synthesizing all that. Thus: pip search question. Our research may be able to help team make a decision on what to do there

    - nothing getting in her way!

  - Ee: nothing to share.

  - Sumana: \[personal status\] in thse surviving mode. Happy moment: book release! am glad that 20.3 release has been chugging along w/ fixes. got my TODOs done; some paperwork is still TODO. only thing concerned about: UX training signups.
- pip search
  - Nicole has thoughts: we\'ve had some people from Simply Secure analyzing survey results, Ngoc looked at it
  - We sent out a survey asking for feedback on pip search
  - some analysis
    - probably not the most popular feature within pip functionality

    - \~31% think it is useful

    - people think it is more clear than not clear

    - people generally think it should be searching PyPI, 40% think it should also be able to search other local indexes or private package repositories

    - looks like people are looking to be able to search more than name - description, keywords, tags, etc

    - does that help us? most interesting thing: idea of deprecating it: 60/177 nearly never use it, 9/177 didn\'t know it existed. cross-reference with buy-a-feature data, which tells us how popular it is compared to other functionality

    - but we still have a technical issue that needs to be addressed.

    - Some results \-- Some people use it, but it is not the most popular functionality in pip

    - removing this will not break EVERYONE\'S workflow

    - Ee: 2 things are being discussed for deprecation: PyPI search endpoint, and pip search to use that API. Unfortunately hands are fairly tied from PyPI; can\'t support ? endpoint anymore\.... we don\'t have any way to really limit (by design of XML-RPC) the way we need to. We could move to 1 search per second per IP, but that also breaks local workflows just as badly. Appreciate research. Outcome: understanding use case for a future version of pip search. But concern: ultimately, providing search to command-line clients will lead to same kind of misbehavior we are seeing by automated systems. History of pip search, problem, began: puppet used pip search to find the right version of the pkg to install. So massive corp clusters threw thousands of search reqs to PyPI \-- seems like it is happening in some other system we don\'t know about\.... unfortunately, can\'t really keep PyPI search endpoint up anymore
      - Nicole: sad that bad behavior from other org means indivs can\'t have this functionality
      - Ee: has spent months of personal volunteer time, and paid time, to maintain endpoint. But growth of usage in automated fashion\.... problem is automated, not personal users. Can\'t effectively differentiate between two. They send pip\'s user agent.
      - Research can help us see what a replacement could look like, and design something that can be cached, but can\'t maintain the arch. as is. Ultimately we end up with search being #1 by request volume that hits the backend systems.
        - Re-arching the search terms would allow caching the terms at the CDN (to take pressure off backends)
      - pypi search endpoint will be going away, unless:
        - someone can architect and implement it
      - Pradyun: People expect pip search to hit pypi - for them it looks like pip search is failing.

    - Nicole will work out some content to explain why pip search will fail

    - Design of \"new pip search\" will be informed by the pip search research

    - If there is a need for pip search (devs at corps) then that might be a \<good?\> thing\.... we have now defined a constituency/market and could ask them to help fund the joint PyPI/pip effort to make a new, sustainable pip search
- UX training \[move to tomorrow\'s call\]
  - \~5 so far have responded
- wrapping up and handing over UX stuff by end of year or Jan (this may move to tomorrow\'s call)
