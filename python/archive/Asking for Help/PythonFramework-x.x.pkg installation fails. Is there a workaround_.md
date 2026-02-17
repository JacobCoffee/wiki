# Asking for Help/PythonFramework-x.x.pkg installation fails. Is there a workaround?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PythonFramework-x.x.pkg installation fails. Is there a workaround? 

1.  Right click on python-x.x.x-macosx.dmg, then select \"Show Package Contents.\"

2.  Right click on PythonFramework-x.x.pkg, then select \"Show Package Contents.\"

3.  Drag Archive.pax.gz out of the folder onto Desktop (this file is not archived correctly).

4.  Grab a terminal emulator, cd to \~/Desktop, then \"gunzip Archive.pax.gz\"

5.  You now need to repack the archive by \"find Archive \| cpio -oa \> Archive.pax\"

6.  Compress the archive by \"gzip Archive.pax\"

7.  Put the resulting file (Archive.pax.gz) into the same location as in step 2

8.  The package is now fixed.

Explanation: This is the error message I got: Apparently, PythonFramework was not packaged properly. Looking up the .pax file detail, it looks like it uses cpio format (This archive tool is old and not well documented.), and for some reason the cpio in my machine (PPC 1.5GHz, OSX 10.4.11) cannot read it. The instruction above basically repacks it using the local cpio program, thereby circumventing this problem.

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
