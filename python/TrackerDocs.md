# TrackerDocs

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**NOTE**: For updated instructions please refer to the [devguide](http://docs.python.org/devguide/triaging.html).

This page explains how to use the Python bug tracker:

- Python tracker: [http://bugs.python.org](http://bugs.python.org)

- Meta-tracker (bug reporting for the bug tracker): [http://psf.upfronthosting.co.za/roundup/meta/](http://psf.upfronthosting.co.za/roundup/meta/)

- Mailing list about the bug tracker: [http://mail.python.org/mailman/listinfo/tracker-discuss](http://mail.python.org/mailman/listinfo/tracker-discuss)

# Reporting (or fixing) a bug 

### Reporting 

Check the [SubmittingBugs](SubmittingBugs) page for an overview of the bug reporting process. In a nutshell, it\'s more important to provide a good description of the issue than it is to set all fields and options correctly. Understanding the usual [Issue Workflow](http://www.python.org/dev/workflow/) also helps in creating good bug reports, raising the chances of your bug report (or feature request) being resolved efficiently.

### Fixing and triaging 

If you want to get started in [developing Python](http://www.python.org/dev/why/), triaging bugs, writing tests for open issues (or undertested modules) and submitting patches are great ways to [contribute](http://www.python.org/dev/contributing/).

The [Issue Workflow](http://www.python.org/dev/workflow/) doc is even more important here, as well as taking a look at some [general Roundup guidelines](http://www.python.org/dev/intro/#general-roundup-guidelines).

# Fields 

## Classification 

Title
:   Exactly what it sounds like.

Type
:   Specify what kind of issue it is (crasher, compile error, etc.).

Components

:   **DIFFERENT**: What area of Python is the issue dealing with? This section allows for multiple selections.

Versions

:   **DIFFERENT**: The specific versions that are affected. This is a multiple selection box so all known versions that are affected can be set.

## Process 

Status

:   **DIFFERENT**: Specify whether the issue is open, pending (tentatively closed, but still waiting for OP reaction), or closed.

Resolution
:   Resolution once the issue is in closed or pending state.

Dependencies

:   **NEW**: If the issue depends on another issue(s), list them here. A complete list of issues can be found by clicking on the *list* link.

Superseder

:   **NEW**: If the issue is superseded by another issue, list it here. The *list* link pops up a window to help find the superseding issue.

Assigned To
:   Who is in charge of the issue.

Nosy List

:   **NEW**: List of usernames who will be notified when anything changes on the issue. The original poster (OP) and all commenters are automatically added.

Priority

:   How quickly must this bug be fixed? Different from *Severity* by specifying how quickly it must be dealt with, not how severe the issue is.

Keywords

:   **NEW**: Multiple selection list of keywords to set to help classify the issue.

    - **26backport**: A 3.0 feature needing backporting to 2.x

      **patch**: Issue has a patch attached (or was imported from the SF patches tracker).

      **64bit**: Bug only applies to 64bit platforms

      **easy**: A bug that is easy to fix. This might be a good task for a bug day beginner.

Change Note
:   Add a comment, which will appear as a new Message.

# Learning about Changes 

The tracker will send email messages when a message gets added (currently not if just a file gets attached, or the status is changed). These messages get sent to

- on submission of a new item, to [new-bugs-announce@mail.python.org](http://mail.python.org/mailman/listinfo/new-bugs-announce), [python-bugs-list@python.org](http://mail.python.org/mailman/listinfo/new-bugs-announce), and to the assignee (if any)

- on changes to an item, to [python-bugs-list@mail.python.org](mailto:python-bugs-list@mail.python.org), and to all people on the nosy list. Anybody adding a message is automatically put on the nosy list.

Furthermore, [http://bugs.python.org/@@file/recent-changes.xml](http://bugs.python.org/@@file/recent-changes.xml) is updated for each message or file addition, and can be used to programmatically track changes.

# Linking from Messages 

The tracker converts some specially formatted words in messages into links. The list includes

- \"#\<number\>\", \"issue\<number\>\", \"issue \<number\>\" links to the issue \<number\>

- \"msg\<number\>\" links to the message \<number\>

- \"r\<number\>, \"rev\<number\>\", \"revision \<number\>\" links to svn.python.org displaying the checked in changes.

# Access Control 

A details specification of the access control to the tracker is given in the table [TrackerAccessControl](TrackerAccessControl).

# Getting a Developer account under Roundup 

For now, an email to Tracker-discuss (mentioned later) is required for a non-SF account to become a Developer account (assuming python-dev has given clearance for the person to have Developer privileges).

# If there is a problem 

If you encounter a problem with the tracker (both in terms of it running and the transition), please create an issue at the [meta tracker](http://psf.upfronthosting.co.za/roundup/meta/). Tracker-discuss (which is discussed below) will be notified and the issue will be dealt with as best as possible.

# Improving the Tracker 

Please remember that the initial transition is not meant to drastically change how issues are handled or reported. It is simply to get Python\'s issue tracker under the control of the PSF. With that in place, discussions can begin about improving the handling of issues.

After the transition is complete and stability has been proven then discussions can begin in earnest to improve the handling of issues. To participate in such discussions, please subscribe to the [tracker-discuss](http://mail.python.org/mailman/listinfo/tracker-discuss) mailing list. This list is meant to discuss the improvement and maintenance of the various trackers hosted by python.org.

For information on how to setup your own instance of the python tracker to help with development, see [TrackerDevelopment](TrackerDevelopment).

# Logging into Roundup with your SourceForge account 

If you have ever used your [SourceForge](SourceForge) account on the old Python bug tracker, you also have a Roundup account. If you have never submitted a bug to the Python bug tracker, read [SubmittingBugs](SubmittingBugs).

To get your new Roundup password, you need to go through the \"forgotten password\" procedure (we don\'t have access to your [SourceForge](SourceForge) password). On the tracker, go to [\"Lost your login?\"](http://bugs.python.org/user?@template=forgotten), and enter your SF username into the Username field.

This will send you an email (Confirm reset of password for Tracker), where you need to follow the link. You will get another email (Password reset for tracker) which contains the new password. The two-email procedure prevents somebody else maliciously resetting your password.

You then might want to change your password. You can also change the email address, so that emails won\'t get sent through sourceforge.net anymore.

# About Differences between SF and Roundup 

[Roundup](http://roundup.sourceforge.net/) is not hugely different from [SourceForge](SourceForge) in terms of usage. Because the initial transition is mostly for resource reasons (i.e., to control our own tracker), the information presented for issues is almost identical to what the SF tracker had.

The largest change people will notice, though, are the additions of some Roundup-specific fields. Those are denoted with **NEW** in their descriptions below. All of them help with the management of bugs and thus should be used when possible and even filled in on existing issues brought over from SF.

Another change is that of monitoring. SF had a **monitor** button that subscribed you to an issue so that you always received an email on all updates. That is now replaced by the *nosy list*. By entering your username on the nosy list you will receive an email every time the issue is changed. More details can be found in the explanation of the field.

Lastly, Roundup provides an email interface to issues. This means that you can actually post to issues by simply replying to an email that you receive. This makes posting replies very easy as one does not need to go through the web interface if the reply does not involve changing fields or uploading files (which can be done through email as well).

------------------------------------------------------------------------

[CategoryTracker](CategoryTracker)
