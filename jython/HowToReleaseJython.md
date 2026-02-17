# HowToReleaseJython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

These are just some rough notes on the steps needed to make a full release of Jython. I generally run ant full-build as a test beforehand, as well as testing many of these steps throughout, but since that isn\'t strictly necessary I\'m not including it here. full-build requires all of the optional jars for the build be available and named in ant.properties. See build.xml for more information.

1.  Update files in trunk that have information on the current version
    1.  build.xml - update properties jython.version, version.noplus, jython.major_version, jython.minor_version, jython.micro_version, jython.release_level, and jython.release_serial.
    2.  imp.java - If there has been any compiler change, increment magic number APIVersion.
    3.  NEWS (double check with the bug tracker)
    4.  README
2.  Run regrtest and the bugtests
3.  Copy maint to a tag
    1.  svn cp [https://jython.svn.sourceforge.net/svnroot/jython/branches/Release_2_2maint](https://jython.svn.sourceforge.net/svnroot/jython/branches/Release_2_2maint) [https://jython.svn.sourceforge.net/svnroot/jython/tags/Release_2_2_1](https://jython.svn.sourceforge.net/svnroot/jython/tags/Release_2_2_1)
4.  build from tag
    1.  \"svn up\" to get the revision number incremented by the tagging above.
    2.  set local properties in ant.properties, mine for 2.5.1rc1:
        - informix.jar=\${basedir}/extlibs/ifxjdbc.jar
        - oracle.jar=\${basedir}/extlibs/ojdbc14.jar
        - svn.revision=6742
        - svn.main.dir=tags/Release_2_5_1rc1
        - jython.version=2.5.1
        - jython.version.noplus=2.5.1
    3.  ant full-build
5.  upload installer
    1.  go to Project Admin\>Feature Settings\>File Release on sourceforge

    2.  Click on Add release next to the jython package

    3.  create with a name in line with the version like 2.2rc1

    4.  upload the built installer [https://frs.sourceforge.net/webupload](https://frs.sourceforge.net/webupload) as documented on [http://apps.sourceforge.net/trac/sitedocs/wiki/Release%20files%20for%20download](http://apps.sourceforge.net/trac/sitedocs/wiki/Release%20files%20for%20download)

    5.  associate the uploaded file with the new release

    6.  also update the SourceForge News page (announcement can be added in Admin/News/Submit)
6.  update files in the website that reference the current release
    1.  index.txt - news and link to the new download
    2.  redirects/downloads.txt - link to the new download, checksums (from file properties in the SF file manager)
    3.  redirects/latest.txt - a copy of NEWS
    4.  redirect/constants.txt - if there is a new stable release
    5.  jysite.py - update the site template for docutils
    6.  building and uploading of the website is described in README.txt
7.  upload maven package
    1.  ant -Dproject.version=2.2-rc1 in jython/maven

    2.  scp dist/jython-2.2-rc1-bundle.jar shell.sf.net:/home/groups/j/jy/jython/htdocs

    3.  File a jira issue for the upload as described in \"Posting the request\" on [http://maven.apache.org/guides/mini/guide-central-repository-upload.html](http://maven.apache.org/guides/mini/guide-central-repository-upload.html)
8.  other actions after publishing
    1.  change the #jython irc channel topic
    2.  announce on twitter (as jython), irc channel, mailing lists, blog \...
    3.  add a new level in the bug tracker
    4.  update build.xml for trunk again
