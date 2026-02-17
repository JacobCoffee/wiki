# PSF Python Job Board/Jobs App User Stories

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Jobs App User Stories 

Please write up job apps user stories on this page. They should be based on the reviews and the overall higher level design described on the main page.

The user stories will then provide the needed outline for the tickets to get the app changes implemented.

## A job submitter wants to file a new job posting 

\- The job submitter clicks on the link \"submit a job post\"

\- If he is not logged in, show a screen with a login window and a signup option

\- Once logged in, display the form to submit a job posting

\- When the user submits the job posting, a notification is displayed \"Your job posting is being reviewed, you\'ll receive an email at the end of the review process.\"

\- The user receives an email notification of the job posting just created.

## A job reviewer wants to review a new posting 

\- The job reviewer logs in to the job application backend

\- Once logged in, the reviewer clicks on a job posting with the status \"Pending review\"

\- The Job posting is displayed and the user can review the content

\- At the bottom of the job application there are 3 buttons: Approve, Request Correction and Reject.

## A job reviewer wants to approve a new posting 

\- The user clicks the Approve button on the Job posting review screen

\- An automated email is sent to the Job submitter with the notification about the Job posting approval and a link to view it

\- The job reviewer is sent back to the list of job postings with a notification \"Job posting approved\"

## A job reviewer wants to request a correction of a new posting 

\- The user clicks the Request Correction button on the Job posting review screen

\- A textarea field is displayed below with 2 buttons Confirm and Cancel.

\- The Job reviewer writes down the suggested corrections on the textarea field and clicks Confirm

\- An automated email is sent to the Job submitter with the notification about the Job posting correction containing a link to the job posting edition.

\- The job reviewer is sent back to the list of job postings with a notification \"Job posting correction requested\"

## A job reviewer wants reject a new posting 

\- The user clicks the Reject button on the Job posting review screen

\- A textarea field is displayed below with 2 buttons Confirm and Cancel.

\- The Job reviewer writes down the reasons of rejection on the textarea field and clicks Confirm

\- An automated email is sent to the Job submitter with the notification about the Job posting rejection

\- The job reviewer is sent back to the list of job postings with a notification \"Job posting rejected\"

------------------------------------------------------------------------

[CategoryPythonJobs](CategoryPythonJobs)
