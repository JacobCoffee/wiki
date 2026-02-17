# PUNIC

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# What is the PUNIC network? 

The PUNIC network is a group of professional Python companies and developers in the Netherlands. The network stems from the Python Usergroup Netherlands ([PUN](http://wiki.python.org/moin/PUN)) and [Django Meeting NL](http://wiki.python.org/moin/DjangoMeetingNL) groups.

## The goals of the PUNIC network 

- To provide a backup network by developers for developers looking to develop Python applications for business situations.
- To provide solid ground for business who depend on Python for their day-to-day operations.

The network consists of employees using Python within a larger company, developers within small businesses that depend on Python and independent developers.

Python developers within the network document their projects and the details around those projects. If a Python developer becomes unable to continue his/her work the PUNIC network is notified. The network document of the developer allows the PUNIC network to quickly determine which projects can be taken over by which developer or company, notify the necessary contacts and proceed to continue where the developer left off.

## Why start such a network? 

The PUNIC network was started to support the efforts of the small Python community in the Netherlands. Although Python has increased in popularity over the last decade it is still not easy to find an adequate replacement for a Python developer. Formal and informal arrangements were made but increasingly PUN members wanted to address this issue as a group.

## PUNIC project levels 

The following levels have been defined within the network:

- Level 0: The network comes into action at death, permanent disability or long-term disappearance of the developer.
- Level 1: The network comes into action at emigration, change of work or other long-term inability by choice to develop.
- Level 2: The network comes into action at illness, holiday or other short-term inability to develop.

A higher level requires a larger amount of documentation and more frequent updates. A level 2 developer must make sure that his/her projects are transferable within one work-day. A level 1 developer must make sure that his/her projects are transferable within 3 work-days. A level 0 developer must make sure that his/her projects are transferable within 5 work-days.

For now we\'ll only go for level 0 projects+documentation: it\'s harder than you might think.

## Incidents 

At the occurrence of an incident all developers of the level involved and each level below it are sent the network document. If a developer is interested in taking over the project (short- or long-term) the developer lets the network know (first-come first-serve). The developer then contacts the project client.

If the project client declines the developer the project is once again sent to the PUNIC developers.

Note that the PUNIC network isn\'t an insurance: it is a formal blanket approach from the participating Python developers to those they develop for. It is possible that a project can\'t be taken over in spite of multiple attempts. In this case the project client will have to look outside the PUNIC network.

## Documentation 

Mandatory up-to-date documentation:

- The Project: Purpose, context
- Stakeholders: Who you are dealing with
- System architecture: Hardware/hosting, OS, (Web)platform, libraries, dependencies
- Your software: How it fits together, global outline
- How to gain access: How another developer is to gain access (passwords with client, notary, in vault)

-\> allow another developer to decide if he/she can take over your project within a reasonable time-frame (eg. 1 week).

More documentation is better, but a single page from last Tuesday trumps a project plan from 5 years ago that hasn\'t been changed.

**Document your warts!**

## Tentative (voorlopige) members 

- Aperte (Alex de Landgraaf)
- You?

## Where do we go from here? 

- Interested in joining? The more the merrier!

- Get a mailinglist up (or use the PUN list?)

- Leaflet for clients (I\'ll update my first attempt once we have some tentative members)

- Simple website/wiki to point people towards (this page!)

- Refine documentation requirements & submission process

- Write documentation per project, have someone else in PUNIC verify your documentation

- Get other Python developers you would vouch for interested

- Set up a \'stichting\', have PUNIC become a part of the Django Vereniging.

- Python world domination, even if shit happens!

## Notes from PUNIC talk 13-04-2011 

- Existing European initiative, has once participant in NL
  - It\'s more complex to do this EU-wide, let\'s keep it local and gain critical mass in NL. It would be good to contact the European network and take over their approach.
- Documentation of passwords, ssh/ssl keys etc
  - There\'s no single good approach in my opinion. Giving the passwords to the project client sounds like a good idea, but this isn\'t possible with shared hosting / multiple clients on 1 server. Document how your successor is to gain access.
- Via Django Vereniging?
  - Good idea, I\'m all for PUNIC being part of PUN or the Django Vereniging. The question does arise if we want to focus on Python+Django, or aim for Python as a whole.
- 5 days take-over time might not be enough for large projects
  - Then document this fact and make it clear to the client that the take-over time will be longer. The documentation should be clear in how large the scope is of your project, how many modules/apps it contains. In the end it\'s up to the developer taking over the project to make the final decision if he/she wants to take over the project during discussion with the client.
- 5 days take-over time might be too costly
  - Note that small projects might be much quicker to take over. If so document your opinion. 5 days is a middle-of-the-road guideline between simple and complex projects. It\'s also always good to have some leeway: taking over someone elses project might sound simple but it\'s always more time-consuming than that you think.
  - Clients shouldn\'t expect a free ride: finding a new Python company willing to take over the project without any clear succession path will take much more time. The PUNIC network is to help speed up the transition, not alleviate the inherent risks of software development.
- DON\'T PANIC?
  - People weren\'t impressed with my [H2G2](./H2G2.html) references. I\'ll remove them from the leaflet.
