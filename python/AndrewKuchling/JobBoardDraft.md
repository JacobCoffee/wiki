# AndrewKuchling/JobBoardDraft

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Title: Automating the python.org job board

The python.org website includes a job board at [http://www.python.org/community/jobs/](http://www.python.org/community/jobs/) that is currently updated manually by volunteers in response to emails from companies.

The tasks done manually include:

- Adding a job upon request
- Rejecting a posting with a reason (it may be non-Python or needs to be reformatted)
- Dropping a posting without reply if it\'s spam
- Reformatting a received posting or updating a posting on request
- Removing a posting on request when the job is filled
- Removing a posting because it has expired (say, when it\'s 3 months old).

When processing a request, one of several form emails are used (job has been posted, rejected w/ reason, job has been removed, or job has been updated).

For this task, we seek to partially automate this process using Roundup. While Roundup is best-known as a bug tracker, it\'s very flexible and the schema can be adapted for different uses.

First, you need to setup the schema - change the \"issue\" class to \"joboffer\", add fields for \"company name\", \"address\", \"country\", \"posted-on\". Set the \"status\" values to \"submitted\", \"reviewed\", \"closed\", \"rejected\".

Then create roles \"Submitter\", \"Reviewer\", and give the Submitter role to all people who have an account. Submitters can do anything to their job description until it\'s reviewed, when they can only close it. Reviewers can see all job offers; Submitters only their own ones. We \*could\* allow anonymous submissions, but then submitters cannot close or review them.

Either allow editing messages (which I\'m not sure whether it\'s supported), or declare that the last message on each job offer is the one that gets posted. As yet another alternative, a \"post-this\" field could be added to the msg class, to be set by the reviewer.

Edit the issue template page to incorporate the new fields, and drop the fields that we don\'t need (such as keyword, priority, status - or start with the \"minimal\" schema in the first place).

Write a \"react\" hook that gets invoked every time a joboffer changes to \"reviewed\" or \"closed\" state; this hook would probably generate a page So only the submitters and reviewers would see the roundup interface.

The common \"nosy\" react hook would send messages to the job board every time a new job offer is added, and send messages to the submitter whenever a job is posted or rejected (for rejection, there probably should be an explicit message also; for posting, we could arrange for some standard message).

A script should automatically close job offers once they are six months old.

Students will have to set up Roundup on their own machine, and develop the new schema and hooks using that installation; we will then work to get the work deployed on the PSF\'s live Roundup server.

This system will probably be maintained and used for a long time. You aren\'t signing up to maintain the code long-term (though it\'s great if you\'re willing to do so), but the code will need to be nicely modular and clear; the reviewer will be fairly strict about this.
