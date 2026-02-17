# ElectionsWorkgroupPlanning

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[https://mail.python.org/pipermail/elections-wg/2015-May/000074.html](https://mail.python.org/pipermail/elections-wg/2015-May/000074.html)

Kicking off a thread about what requirements we think we should have for a PSF voting system.

The first requirement I can think of comes from the PSF bylaws:

- Section 14.8. Electronic Voting. Any vote of the Board of Directors, any committee, or the members may be conducted through electronic means and shall have the same effect as action taken by written consent; provided that such voting mechanism meets the criteria set forth in this Section 14.8. Any vote conducted through electronic means must be done through a mechanism by which both the identity of each voter and the date that such vote is made can be verified. No vote conducted pursuant to this Section 14.8 may remain open for more than sixty (60) days after the commencement of the applicable voting period. Each such vote shall have a specific approval requirement identified prior to the commencement of such vote, which requirement shall not be less than the requirements set forth in the corporation\'s Certificate of Incorporation, these Bylaws or the General Corporation Law of the State of Delaware. The effective date of any vote conducted through electronic means shall be the first date upon which the requisite threshold for approval of such action has been obtained.

IANAL, but I read this as stating that we need to be able to verify if a particular voted or if they did not, and we need to be able to verify when they voted. I do not read in this a requirement that we know \*what\* they voted for, only who and when. I believe this is a hard requirement, since not only is it in the bylaws, but it\'s required to support another part of the bylaws:

- Section 4.12. Loss of Voting Rights. A voting member who does not cast a vote for four (4) votes within a single calendar year shall immediately have his or her voting rights revoked for the remainder of such year.

Beyond that, the bylaws don\'t make any other requirements on what a voting system looks like. To get us started I\'m going to throw out some things to try and get a discussion going.

I think that any system we have should not make it available to the general public who voted for what. I think that if it\'s public information who voted for what then people will feel pressured to vote for what\'s popular or what has support than for what they truly want to vote for. I also think that it will cause some people to be a target for others who didn\'t agree with the way they\'ve voted.

I think that any system we have should make it possible for the general public to verify the results of the election given only public information.

I think that any system we have should make it easy for the board, working groups and committees to also utilize this system for any votes they need to hold as well if they so choose to do so.

I think we also need to define a threat model we want to operate under and how important particular attributes are to us. For instance, do we consider a malicous election administrator to be something we need to protect against? What about a malicious system administrator? If we\'re OK with a malicous system administrator being able to de-anonymize then we don\'t need any system that\'s particularly complicated. A fairly simple web application that just lets people vote and doesn\'t display who a particular vote is for (but still records it) is a simple thing that gets us all of the above, assuming trustworthy systems administrators. If we want to consider these people within the threat model then we\'ll need to look at more complicated systems that rely on the ability to use cryptography to ensure certain properties.

Defining a threat model is probably the first thing we should do really, because our threat model is going to dictate what kind of system we\'re looking at, whether a simple solution that uses ACL and the software to ensure the properties we want or a more complex solution that uses math and cryptography to ensure it.

\-\-- Donald Stufft PGP: 7C6B 7C5D 5E2B 6356 A926 F04F 6E3C BCE9 3372 DCFA

------------------------------------------------------------------------

[https://mail.python.org/pipermail/elections-wg/2015-May/000083.html](https://mail.python.org/pipermail/elections-wg/2015-May/000083.html) These are the hard requirements I think we need for the PSF:

- voting should be easy
- voting should be possible in a central place and via a web
  - interface
- people should get voting notifications in both a direct email
  - (as per the bylaws requirements for notifications) and a public forum (psf-members-announce ML; so that people can check whether they also received the direct email)
- the voting system needs to be able to record the identity of
  - the voter and the voting date/time (bylaws requirement)
- people should get a notification of whether their vote was
  - recorded (by email or via the web UI; to reduce support requests)
- after the vote has ended: display a summary of the results

All this under the premisses that we have trustful election administrators. We\'ve operated under this premisses ever since the PSF was founded, and don\'t think that a malicious admin is a threat model to consider.

Soft requirements (these are nice to have, but not essential):

- be able check your own ballot
- get email pings if you haven\'t cast your vote a few days
  - before the end of the voting period
- have the voting system cryptographically secure (not really
  - a high priority, esp. not if it makes voting harder)

Ideally, I would like to see the \"emailing links to ballots\" approach go away, since this is really a completely insecure method of distributing ballot information. Having to log in to a website is not a big deal and makes the process of voting much more reliable.

\-- Marc-Andre Lemburg eGenix.com

------------------------------------------------------------------------

[https://mail.python.org/pipermail/elections-wg/2015-May/000060.html](https://mail.python.org/pipermail/elections-wg/2015-May/000060.html)

I found the mailing list email finally ![:)](/wiki/europython/img/smile.png ":)")

Working group: please see my charter request below.

On Fri, May 22, 2015 at 3:22 PM, Ewa Jodlowska \<ewa at python.org\> wrote:

\> Hi Ian and Laura, \> \> I was not sure which email address you went with for this mailing list so \> I am emailing you individually. Please feel free to send my request on to \> the mailing list. \> \> As a PSF working group, there needs to be a charter in place. At minimal, \> we need to know how you will operate (make decisions, vote, etc), how you \> will communicate, and who is so far part of the group. \> \> There is a template available here: \> [https://wiki.python.org/psf/Example%20PSF%20Workgroup%20Charter](https://wiki.python.org/psf/Example%20PSF%20Workgroup%20Charter) \> \> Once you have this complete, please send it to me so I can get the board \> to acknowledge the working group.

\-- Best regards, Ewa Jodlowska

------------------------------------------------------------------------

bylaws

informing those who won that they have.
