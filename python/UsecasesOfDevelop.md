# UsecasesOfDevelop

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Some use cases of the \'develop\' command 

The \'develop\' command is used to pseudo-install a project source without copying any files, which is a useful feature of setuptools and will be implemented for packaging.

However, different people may have different purposes and will use \'develop\' in a very different way, so even though we argued a lot in the mailing list but have not yet reach an extensive consensus on how the future \'develop\' of packaging should behave.

Thus this page is created just to collect different use cases being talked about in our fellowship list, which will be taken as an important idea base to implement an elegant solution that work for all at the most extent.

Note: These use cases are not complete and people can help me enhance. Question should be addressed in [Issue 8668](http://bugs.python.org/issue8668).

The develop command writes three pieces of information to the filesystem:

1.  It calls upon the build action(s) to build the package within the package\'s root directory.

2.  It calls the \[build\|install\]\_distinfo action to write the .dist-info metadata inside the build directory. (see also [Issue 12279](http://bugs.python.org/issue12279))

3.  It adds the build directory\'s path to a .pth file.

## Use Case 1 (from Carl) 

**Story Description:** Carl has a foobar project which contains a \'foobar\' directory that is referenced in his setup.{py,cfg} as the a package to be installed. He also has additional Python packages alongside \'foobar\' (e.g. a \'tests\' directory), which he does not want installed.

    .
    |-- foobar
    |   |-- __init__.py
    |   |-- bar.py
    |   `-- foo.py
    |-- setup.cfg
    `-- tests
        |-- __init__.py
        |-- test_bar.py
        `-- test_foo.py

**Type:** Feature request

**Requirements:**

- The \'tests\' directory, or any directory not referenced in the setup.{cfg,py} for install, should not be importable, because it could have an unintended collision with other installed packages.

## Use Case 2 (from Tarek) 

**Story Description:** Tarek wants to install a project in-place with \'develop\' command. Because he does not have root access to the system, therefore lacks write access to the global site-packages directory. He would also like the package to be installed for no one but himself.

**Type:** Unknown

**Requirements:**

- The develop command cannot assume it has write access to the site-packages directory. Usage of the sudo command to install the development information is not a valid solution in this case.
- The develop command must write the build directory path to the user\'s site-packages directory (site.USER_SITE).

## Use Case 3 (from Tarek) 

**Story Description:**

Tarek has a foobar project and he is in its project source tree, then he runs \'develop\' in it. In addition, the virtualenv has not yet installed and he doesn\'t want to install it at that time.

**What he wants:**

- foobar seems installed for him
- foobar should not be shared with the whole system, or with everyone

## Use Case 4 (from Carl) 

**Story Description:** One has a private VPS that hosts a number of Mercurial repositories. In addition, he has some custom plugins and hooks that need to run for all users of the server. These plugins and hooks are frequently updated.

**What he wants:**

- run \'develop\' command once, and then be able to repeatedly pull code changes in and have them immediately accessible
- don\'t have to bump version numbers and make releases all the time

## Use Case 5 (from Doug) 

**Story Description:** There is a python development team and his application cann\'t work in a virtualenv for a variety of reasons.

**What he wants:**

- install into the global site-packages in \'development mode\'

## Use Case 6 (from Doug) 

**Story Description:** One is working on a foobar project and he has opened a python intepreter(we call it INTPT-A).

**What he wants:**

- all applications using INTPT-A can see foobar, without having to use an environment variable
- don\'t need to manually edit any files to configure the path for INTPT-A
- any application using INTPT-A doesn\'t need to be run from its particular directory on the filesystem in order to see the changes or his package
- all entry points, including console scripts, are registered correctly with INTPT-A
- can edit files in his project and re-run the intepreter to have the changes picked up, without having to redo the \'python setup.py develop\' or \'pysetup.py develop\' step
