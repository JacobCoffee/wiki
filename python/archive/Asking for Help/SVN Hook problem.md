# Asking for Help/SVN Hook problem

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

I have a python script which is called from the svn repository hooks folders through a batch file post_commit.bat In the batch file in have D:\\Test\\SVNHook.py %1 %2

The problem arised is stated below

------------------------------------------------------------------------

When i run the python script using IDLE then the svn command is executed and the result is formed as an xml. The svn command is given below svn log \--verbose \--xml file///D:/Repositories/Test -r 65 \>\> a.xml

The output for the above command is an xml with the log details while running with IDLE only.

- If the file is committed then the SVNHook.py is called but the resultant a.xml doesnot

have any content. But i can retrieve the repository and revision id on BOTH cases.

Please guide me through this problem.
