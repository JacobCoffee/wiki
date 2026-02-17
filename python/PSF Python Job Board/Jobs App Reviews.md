# PSF Python Job Board/Jobs App Reviews

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Jobs App Reviews 

Please post your jobs app review here. We will then use them as basis for the job app design and user stories.

## Review 1 

From an initial scan of the newjobs URL, I generated these issues:

1\. It reports three jobs from two companies, but doesn\'t display any job postings.

2\. Except for the Submit link, the other three links at the top of the page (Types, Categories, Locations) all take the user to some sort of style guide.

3\. Should we scan the existing postings and try to expand the category and job types?

4\. Should both the category and job types sections have \"Other\" as a choice?

5\. How do I add a new company?

6\. I think the telecommuting checkbox should be disabled by default. Despite recent trends, I think most work is still conducted on-site, so fewer mistakes will be made if it is off by default.

7\. The \"agency\" checkbox should be a property of the company info. Either a company hires its own workforce directly, or is an agency hiring on behalf of other companies. I\'ve yet to see an agency advertising for Python programmers to fill its own needs.

## Run-though of the job submission process by GilesThomas 

- Went to jobs site.

- Saw the job Marc-Andre had approved (Netmail s.r.o.)

- Clicked on the \"fill out this form\" link

- There was a dropdown for company, with every company we\'d entered manually in there, no way to enter a new company. And we probably don\'t want anyone to select a company that isn\'t theirs.

- There was no indication of which fields were required and which weren\'t.

- The \"is it OK for agencies to contact the poster\" field was labelled \"Is job on behalf of an agency?\"

- To be able to investigate further, I selected Rackspace and then hit the \"Submit for approval\" button.

- The page came back with \"This field is required\" placed badly, underneath the fields above the three required fields (with a bit poking out below)

- Once I entered everything, I was dumped onto a page showing the job, with a field below for comments. This was confusing.

- From the jobs admin page, I saw the job but the status was \"Draft\"

- As you\'d expect from that, when I went to [http://www.python.org/newjobs/review/](http://www.python.org/newjobs/review/), the job was not there (and nor was the one Marc-Andre approved earlier)

- Went back to the window where I submitted it, and added a comment.

- Was taken to a \"thank you for your comment\" page, \"A moderator will review the post before it becomes available on the site.\"

- No email was sent the address I entered the comment as (which was pre-populated from my address as the logged in user) but one did go to the one I had entered as the contact for the new job.

- It remained in a draft state as viewed from the admin page.

- Going back and refreshing showed the comment entered as you\'d hope.

- Flipped it into a \"review\" state in the Django admin

- Refreshed the review list; it showed up.

- Clicked on the job ID

- Taken to the page describing the job. No approve/reject/remove buttons.

- Went back to the review list.

- Hit reject.

- Status changed in Django admin to \"rejected\"

- No email received, but possibly my email system was being slow (I was using a forwarding address)

- Tweaked the state back into \"review\" and changed contact email to a non-forwarded one

- Rejected again.

- No email to any address again.

- Tweaked state back into \"review\"

- Hit \"remove\" button from review list.

- Marked as \"removed\" in database

## Suggested review workflow 

1\. Submit an example job via [http://www.python.org/newjobs/create/](http://www.python.org/newjobs/create/); use your email address as submitter address so that you can check the emails being sent by the system

2\. Check posting in [http://www.python.org/newjobs/review/](http://www.python.org/newjobs/review/)

3\. Review by clicking on the job ID, e.g. [http://www.python.org/newjobs/68/review/](http://www.python.org/newjobs/68/review/)

4\. Add a note; see where it goes and whether an email is generated

5\. Approve a job in [http://www.python.org/newjobs/review/](http://www.python.org/newjobs/review/); see whether an email is generated

6\. Reject a job in [http://www.python.org/newjobs/review/](http://www.python.org/newjobs/review/); see whether an email is generated
