# PackagingWG/2018-03-26-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Monday, March 26th meeting notes

Present \[Nicole unavailable\]:

- Laura
- Sumana
- Ernest
- Dustin
- Mark

# News 

Beta released [https://pyfound.blogspot.com/2018/03/warehouse-all-new-pypi-is-now-in-beta.html](https://pyfound.blogspot.com/2018/03/warehouse-all-new-pypi-is-now-in-beta.html)

# Blocked on anything? Announcements? 

Laura:

- will be reviewing PRs - starting with [GitHub](./GitHub.html)-Flavored Markdown

Sumana:

- unavailable Friday but working with Donald

- note: this week & next week, lots of people unavailable/working less

Ernest:

- XMLRPC caching is all set!
- Simple redirects have been going super well overall, Artifactory only lingering issue but JFrog has responded
- Docs Destroy shipped \\o/, needs minor refactor
- Docs redirect functionality planned for this week
- A couple backend migrations planned
  - SES for email instead of Mailgun (Donald lead, will be supporting) (consolidating services)
  - Elasticache Redis instead of AMQP for Celery Broker (consolidating services)
  - Monitoring, Metrics, Load Testing, etc! We\'re looking \_great\_ though!!!
- Primarily off radar next week!
- \[infra\] credits are good for 18 months

Dustin:

- notification bars
- \[redacted anti-spam note\]
- reduced how often we issue purges - removed per-action purges from common models
- this week, fairly unavailable for MOSS-funded Warehouse work, but will review Jon Parrot\'s GFM stuff

Mark:

- NLnet Grant (April 1): - due this week

- review part of grant \"compare project with existing projects\"

- FB Grant (March 31st): due this week - Mark will try to finish draft by Wed, submit Fri

- PEP 541 Finalized: [https://www.python.org/dev/peps/pep-0541/](https://www.python.org/dev/peps/pep-0541/)

- Needs licenses and binaries for [HashiCorp](./HashiCorp.html) from Ernest (not high priority)

# Followup 

- When can we announce \[infra\] credits? - PSF drafting a letter to \[other\] contact - that they will be getting PSF infra

- Packaging WG approving fund reallocation \-- Ernest & Dustin, could you project your current end dates based on that? Yes

- Mark: Facebook & NLNet grants: see above

# Bug triage 

User support ticket system [https://github.com/pypa/warehouse/issues/3231](https://github.com/pypa/warehouse/issues/3231)

- Sumana asks: prioritize higher?

- look for a support queue instead of [GitHub](./GitHub.html) issues

- find inexpensive commercial solution and pay for out of Packaging WG funds

- build a simple queue into Warehouse?

- Resolution: revisit in 2 weeks when team is reassembled, see who has time to investigate

# Need from Donald 

- transparent \[sponsor\] logo (sponsor really, Ernest can email our contact)

# TODO 

- Ernest & Dustin - project end dates based on updated fund allocation

- review part of NL Net grant \"compare project with existing projects\" - Mark will grab from Open Tech Fund application

- trim NL Net grant application since we can only ask for \$35,000 - SH will do, coordinate with Ernest

- Mark needs licenses and binaries for [HashiCorp](./HashiCorp.html) from Ernest (not high priority)
