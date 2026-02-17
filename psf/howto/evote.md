# howto/evote

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Election Contacts 

::: {}
  --------------------------------------
  Ian Cordasco, Election Administrator
  Mark Mangoba, PSF IT Manager
  --------------------------------------
:::

# Adding a New Election Administrator 

When an Election Administrator is approved (by the PSF Board), the Election Adminsitrator will sign up for an account at: [https://vote.python.org/init/default/user/register?\_next=/init/default/index](http://when%20an%20election%20administrator%20is%20approved,%20the%20election%20adminsitrator%20will%20sign%20up%20for%20an%20account%20at:%20https//vote.python.org/init/default/user/register?_next=/init/default/index.). The election is managed through [https://vote.python.org](https://vote.python.org/). The Election Administrator manages the election by inputing their email address in the managers tab of the election as well as the PSF IT Manager (to supervise the election process).

# Creating a New Election 

Managers should log into [https://vote.python.org](https://vote.python.org/) and click on the \"Elections\" link at the top of the page. There should be a button that says \"Create a New Election\". When you do that, the WSGI editor should help guide you through creating a ballot.

# PSF Managing/Contributing Membership Self-Certification 

You must be a PSF Managing Member or Contributing Member in order to be eligible for voting rights. To learn more about being a basic member: [https://www.python.org/users/membership/](https://www.python.org/users/membership/). An electronic self-certificaton form will be sent from the PSF Director of Operations **30 days before the elections start.** This process is to verify your e-mail address and your election rights before the ballot is sent.

# Ballot E-Mail List Verification 

The PSF Director of Operations and the Administrator runs the member report in CiviCRM, exports the email address and merges the self ceritification list from Google Forms. Once the report is created, it is sent to the Election Administrator and the PSF IT Manager. The Election Administrator consoldates and deups the email list before importing them into [https://vote.python.org](https://vote.python.org). **This should be done 2 weeks before the start of the election.**

# Ballot Summary Text 

The ballot text is created by the Election Administrator and is approved by the PSF Administrator before it is imported into [https://vote.python.org](https://vote.python.org). **This shoud be done two weeks before the start of the election.**

# Creating/Sending the Ballot 

The Election Administrator imports the ballot summary text approved and the candidates are placed in random order. Example below:

- Candidate 1 yes/no/abstain
- Candidate 3 yes/no/abstain
- Candidate 2 yes/no/abstain
- Candidate 4 yes/no/abstain
- Candidate 5 yes/no/abstain
- The apporved and deduped email address are imported. E-mail address are double checked and the election managers email are listed.
- Deadline is inputed in UTC/GMT time, should reflect AoE deadline. The Election Administrator should use a Time Zone converter to make sure the time is inputed correctly.
- Text of email should include a summary of the election with a link to the ballot (it should never be sent without a summary as it will confuse voters or marked as spam), example:
  - Summary of ballot (describe the election)
  - Link to vote:
  - Link to ballots:
  - Link to results:
- Once it is reviewed, the Election Administrator will send the ballots. Each ballot UUID is comprised of an actual UUID and an RSA signature of the UUID using the election private_key.
- Ballot is emailed through Rackspace Mailgun for reliable email delivery. Send/Recieve logs are avaiaible throught the Rackspace dashboard, you must contact the PST IT Manager for reports or a member of the Infrastructure Team.

# Results 

Once the election has ended, the ballots are calucalted automatically. The calculations can be found by having the Election Administrator close the election and the \"results\" page is viewable. **The offical results are annonnced by the Director of Operations.**
