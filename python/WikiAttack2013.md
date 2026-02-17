# WikiAttack2013

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Wiki Attack January 2013 

## Summary 

The python.org wikis for Python, Jython and the Python Software Foundation (PSF) were subject to a security breach and later attack which caused all of the wiki data to be destroyed on January 5 2013.

An analysis of the incident revealed that an exploit had been planted on our servers possibly as early as July 25 2012, which allowed arbitrary execution of code under the user running the [MoinMoin](MoinMoin) wiki.

It is likely that the password information was downloaded from the server in the course of the security breach, so **we recommend changing your passwords immediately**, if you have used the same password for other services as well.

During the recovery in the weeks after the attack, we reset all passwords on the wiki server to make sure that users do change their passwords. You can use the password recovery function of the resp. wiki to reset your password. The function is shown when clicking on the login link.

If you have created new accounts after June 24 2012, those accounts will no longer exist due to the data loss. You will have to recreate the accounts.

Moving forward, we will no longer allow changing wiki pages without login and have put additional security measures in place to prevent attacks like the one we came under. The PSF has also funded the change of the [MoinMoin](MoinMoin) code base to include support for the passlib library, which provides much better means of protecting password information on the server than the SHA-1 based hash scheme used before [MoinMoin](MoinMoin) 1.9.6. This new support will be available in [MoinMoin](MoinMoin) 1.9.7.

Please report any problems you find with the wiki to the [mailto:pydotorg-www@python.org](mailto:pydotorg-www@python.org) mailing list.

## Attack Analysis 

In the week of January 14 2013, we ran a longer analysis of the attack on the wiki VM. This is a summary of the things we found.

The attack used on the wiki was apparently the same as the one which hit Debian:

- [http://wiki.debian.org/DebianWiki/SecurityIncident2012](http://wiki.debian.org/DebianWiki/SecurityIncident2012)

Someone used the [https://security-tracker.debian.org/tracker/CVE-2012-6081](https://security-tracker.debian.org/tracker/CVE-2012-6081) vulnerability to upload an action plugin to the server called moinexec.py, which was then subsequently used to run commands on the moin user account.

The few logs that were still accessible showed that someone tried sudo on Dec 28 2012, but without success.

On Jan 5 at 00:10 GMT, someone else ran the \"rm -r \*\" which resulted in all files owned by the moin user to get deleted.

The VM was rebooted on Jan 7, apparently in an attempt to get things working again. The result of this was that the file system was remounted, clearing most of the transaction log, which could have been used to recover the deleted files. The VM image he was working off was created after the reboot.

Of course, without the moin user files available, getting a better picture of what happened was difficult. With the knowledge of the Debian analysis, he found a bytecode file of the uploaded plugin code in the VM image and this showed a PYC time stamp of Wed Jul 25 16:08:14 2012 GMT, closely matching the date given in the Debian analysis.

We were subsequently approached by the person who ran the rm -r \*, so we know now that the original attack was performed by different people, most probably the same that attacked the Debian wiki. It is also obvious that the people who installed the plugin, had different intentions than causing easy to detect damage on the system.

Since the logs on the VM only go back 5 ![(!)](/wiki/europython/img/idea.png "(!)") days for server web logs and 7 ![(!)](/wiki/europython/img/idea.png "(!)") days for system logs, it was impossible to determine the amount of information leakage caused by the attack.

It is likely that the passwords and user configuration details were inspected in the same way as was done for the Debian wiki.

## Content Recovery 

Since we were not in the comfortable position to use a backup for restoring the wiki content (our most recent backup dates back to June 24 2012), we tried to get as much information from archive.org, the Google cache and the Yahoo/Bing cache as possible.

It turned out that the Google cache was unusable for the task due to a surge protection on their site. Yahoo/Bing worked and results in quite a few more recent edits/updates. The archive.org pages included snapshots from end of Nov 2012, but they apparently don\'t run complete dumps of the sites they archive (and since moin has a surge protection built-in as well, it\'s not easy for such archives to crawl the wiki).

Overall, we have been able to recover around 200 pages that were created/edited after the June 2012 backup date. Not really all that much, given the amount of data in the wiki, but still better than nothing.

We then ran ext4image and photorec on the VM image in several combinations and was able to restore a number of files. Unfortunately, important meta data such as the file date/time and name was lost. This made restoring from the files very difficult.

Moin stores the wiki pages in plain text files and keeps all revisions in the file system. Furthermore, there is no meta information inside the text files, so only the headers from the file content can be used as indication of which page it belongs to and even then, you get multiple copies of the same page, with no indication as to which of those to regard as most current version.

Still, the restored files do contain pages that were not available in the archive web sites, so if there are important pages that need to be restored, we can manually try to extract the relevant data and re-add it to the wikis. For the PSF wiki, this is the only way to recover files, since there are no web archives available for it.

Additionally, none of the newer attachments to wiki pages could be restored.

## Content Restoration 

In the week of January 21, we then continued the work to prepare the archive downloads for reintegration into the wiki.

A script was used which is able to convert the archive HTML dumps back into wiki markup. We also wrote a script which uses the [MoinMoin](MoinMoin) API to readd the pages with proper timestamps and editor information back into the [MoinMoin](MoinMoin) database.

In the meantime, one of the [MoinMoin](MoinMoin) developers was working on adding passlib support to moin 1.9. The work was funded by the Python Software Foundation (PSF).

We then setup a new VM for the wiki and configured it to use the newly added passlib support in moin. After an additional security audit on the configuration and changes to harden the installation, the conversion script was used to readd the archive dumps on top of the June 24 2012 backup.

Note that as part of the recovery process, some pages were changed from ReST markup to wiki markup. This is due to the fact that the restore process via the HTML archive dumps always creates wiki markup.

## Wiki Cleanup 

After the recovery step, we ran a wiki cleanup. This means that \"empty\" and deleted pages were moved out of the way.

We also changed the user preference settings from the old \"python\" theme to the current \"europython\" theme, which is also used for all new accounts.

## Moving to HTTPS 

We have enabled HTTPS access to the wiki to further enhance security and avoid having to send clear text passwords over the network in order to log in to the wikis.

If you have not been using HTTPS links to the wiki login page yet, please be advised that your password may have been sniffed on the network at e.g. a conference. It is best to [change it again](./WikiAttack2013.html?action=userprefs) and stop using HTTP links to the wiki login page.

## Next Steps 

After the official moin 1.9.7 release, we will switch from the current moin checkout we\'re using to the official release.

## Timeline 

- 2012-07-24: Likely date of the original exploit installation

- 2013-01-05: All wiki files deleted using the exploit

- 2013-01-07: Wiki server taken down for analysis and recovery

- 2013-01-25: New wiki server switched online in test mode

- 2013-03-24: Enabled experimental [https://wiki.python.org/](https://wiki.python.org/) service

- 2013-07-30: Enabled redirect from HTTP URLs to HTTPS URLs; doesn\'t work yet, due to LB problems.

- 2013-09-03: LB was fixed and HTTPS redirects mostly work now, but the configuration is not yet complete. Removed the wiki banners and added front page section on the attack.

- 2013-09-04: HTTPS configuration is now complete. Added HSTS headers to all outgoing requests.

## Credits 

These people have put in significant work to get the wiki back online (in alphabetical order).

- Reimar Bauer (HTML conversion, adding pages to the wiki, security audit, wiki configuration)

- Noah Kantrowitz (setting up the new VM)

- Marc-Andre Lemburg (recovering pages from the archives, attack analysis, file recovery, setting up the new installation, security audit, wiki configuration, wiki cleanup, ongoing maintenance, HTTPS setup)

- Thomas Waldmann (adding passlib support to [MoinMoin](MoinMoin), help with the configuration)

\-- Python Software Foundation
