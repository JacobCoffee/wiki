# PackagingWG/2018-03-19-Warehouse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Warehouse core developers\' meeting 

Monday, 19 March, 2018

## Present 

- Dustin
- Sumana
- Laura
- Mark
- Nicole
- Ernest
- Donald

## Reschedule Monday March 26 meeting? 

No, don\'t reschedule. Nicole unavailable; Dustin can join

## Working on/blocked/announcements 

*Reminder: last week of March & first week of April, lots of unavailability*

\* Sumana:

- writing LWN article, draft this Thursday

- helped volunteers, triaged bugs, improved docs, supported users, tested Warehouse

- non-MOSS: improved Twine & releasing 1.11.0 today (now done [https://pypi.org/project/twine/1.11.0/](https://pypi.org/project/twine/1.11.0/) )

Dustin

- Last of the camo changes to show message for big images

- Added ability to add classifiers in the admin UI (and took care of some classifier requests)

- Load testing support

- Non-MOSS: Description-Content-Type / Markdown Support [U0001f389U0001f389U0001f389](./U0001f389U0001f389U0001f389.html)

- Will be \"out\" all of next week (non-billing, but still can attend this meeting & will be doing some light volunteer work / responding to messages)

Mark:

- PEP 541 ready for vote (sending e-mail today \[now sent\]), Nick made a couple edits last week.
- Facebook Grant Working document (will send e-mail to packaging-wg on feedback today) \[link\] due March 31

Ernest:

- Kubernetes is live on AWS! Cabotage is live on Kubernetes! Warehouse Live on Cabotage!
- Monitoring/Metrics added as we go, have deployment notifications and major alerts in Slack now #pypa-feed - may add to IRC
- Screencast link to be shared after upload
- Focusing on monitoring, stability, and performance this week with a focus on XMLRPC in Warehouse - biggest remaining blocker for switching over PyPI
- Runbooks/Docs on kubernetes installation/cabotage
- Plan to continue testing traffic redirects tomorrow. XMLRPC traffic \"replay\" can happen in the background without impacting users.
- We can continue redirect testing now that pip 9.0.2 is shipped, we can exclude Artifactory, and pip 1.5.4 (Ubuntu 14.04) confirmed fixed. - redirect people if they get an error
- Recurse Center: April 2-6, I\'ll be MIA
- no blockers

Laura:

- Has been reviewing PRs
- testing 566 compliance

Nicole

- reviewing PRs

- PR - upgrade way to make dropdowns work better

- of UX issues, issues [2612](https://github.com/pypa/warehouse/issues/2612), [3194](https://github.com/pypa/warehouse/issues/3194), [3062](https://github.com/pypa/warehouse/issues/3062), [1317](https://github.com/pypa/warehouse/issues/1317) \-- very much need to be done \-- most other stuff is nice-to-haves

- 2 volunteers for user testing - would like to run another run of tests on package detail page but may need more funds?

- no blockers

Donald

- helping with load testing

- working on releasing pip 9.0.2 [https://pypi.org/project/pip/9.0.2/](https://pypi.org/project/pip/9.0.2/) - may need 0.3

- Warehouse brownouts ?

## Followup from past meetings 

Mark, Ernest & Donald: When can we announce \[redacted\] credits?

- Ernest: still need logo for footer\... no?
- Publicize before getting logo?
- DI - remove sponsors that are no longer sponsoring
- need \[redacted\] transparent logo from Donald
- Donald - no reason to wait
- Mark will take care of announcement/logo

Mark: grant proposals for future grants?

Sumana: talk with Eric about sponsorship outreach & future fundraising - cc Betsy

Nicole & Ernest: ask volunteer contributors for more code review? (Dustin scaling back on PR review)

- yeraydiazdiaz - good front end contributions
- Alan Bato - good front end
- Al Mazan
- DI - follow up

Nicole: how much Nicole time left on grant?

- discuss after

Mark: PEP 541? (addressing) Mark: Open Tech Fund?

- Formal determination message within the next 2 weeks.
- May take some time to iterate through their process and create a finished proposal with them

## Beta & redirect schedule 

\* Should the China CAPTCHA issue be in our beta milestone? [https://github.com/pypa/warehouse/issues/3174](https://github.com/pypa/warehouse/issues/3174)

- Ernest: looking like it\'s time to switch from reCAPTCHA to some other service\...?

- DI - we may need external help or try to find another captcha service

- Donald - not part of beta but we should try to fix it

- Ernest - try to find a known good captcha instead of Google

- DI & EWDIII will take care of captcha

Who wants to review announcements Sumana writes this week?

- Nicole can review

Who\'s available & interested in being on podcasts in April?

- DI
- Ernest
- Sumana
- Nicole - user experience focused podcasts

## Bug triage 

\* Set samesite=lax on session cookies #3221 [https://github.com/pypa/warehouse/issues/3221](https://github.com/pypa/warehouse/issues/3221)

- Sumana asks: I think this is not urgent. Correct? Post-shutdown milestone?
- We should do this but it is blocked on Pyramid supporting it
  - is there an upstream bug already filed against Pyramid? is it [https://github.com/Pylons/pyramid/issues/2733](https://github.com/Pylons/pyramid/issues/2733) ?

  - Not urgent - defense in depth - nice to have but we can wait until Pyramid supports it

should Warehouse guard against people uploading broken-description wheels made with an old version of `wheel`{.backtick}? [https://github.com/pypa/warehouse/issues/3084](https://github.com/pypa/warehouse/issues/3084)

- Sumana asks: want Twine to check for this? How urgent? Doesn\'t feel like MOSS work
- Not twine\'s job, not in scope of MOSS, not a priority, but a nice-to-have

#3275 Artifactory [https://github.com/pypa/warehouse/issues/3275](https://github.com/pypa/warehouse/issues/3275)

- Sumana asks: do we have someone at JFrog we can/should reach out to?
- Actually is \"Artifactory does not like externally hosted files\"
- Will follow up with initial reporter to see if we can get JFrog involved.

Design question for Nicole on ISO dates [https://github.com/pypa/warehouse/issues/3010](https://github.com/pypa/warehouse/issues/3010)

- Progress? This week

## Ask Donald for: 

nothing this week

## TODO 

\* Ernest: DI, Mark, Donald logins for Cabotage/Tectonic
