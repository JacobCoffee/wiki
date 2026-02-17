# VersionTransition

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

In moving to a new version of Jython, the Lib files included from CPython are upgraded to the version Jython will move to. Since Jython pulls many of its tests directly from CPython\'s Lib, large numbers of the upgraded tests will fail right after the version transition: they\'re testing new CPython features that have yet to make it into Jython. This is bad since we want the older parts of the tests that Jython has already implemented to be run successfully so it\'s clear when adding a new features broke an old one. To get the tests quickly into a state where breakages are noticeable, a three-pronged approach is taken:

1.  Tests for completely new features with no bearing on existing Jython code are added to the \_failures or \_skips test sets in regrtest.py so they\'re ignored until someone gets around to implementing them.
2.  Tests revealing minor problems or tiny new features are fixed immediately in Jython.
3.  Tests that cover much existing code but also have failing tests for major new features have those failing parts of the tests excluded until someone can work on them with a \"Jython transition\" comment.

1 and 3 both provide fertile ground for new developers to start working on Jython. For 1, open up Lib/test/regrtest.py and look at the test cases in \_failures and \_skips. If a test case is in \_failures, that most likely means part of its implementation already exists but there\'s a major part of it missing. You can just run the test directly to see what\'s wrong to start going about fixing it. The status of a test in \_skips might not be quite as simple. It may just be that the test is for a module implemented in C that hasn\'t been ported to Jython yet, or it may be that the module in question will never be ported to Jython as Java can\'t support it. curses and the audio modules are good examples of the latter. Porting a module that can run on Java is a good chunk of work to start on. See [JythonDeveloperGuide/PortingPythonModulesToJython](./JythonDeveloperGuide(2f)PortingPythonModulesToJython.html) for some direction and available modules.

The items created by 3 are smaller in nature. Each of these will have tests commented out with a \"Jython transition\" comment above this and will also have a bug filed in the [test failure causes group](http://bugs.jython.org/issue?%40search_text=&title=&%40columns=title&id=&%40columns=id&creation=&creator=&activity=&%40columns=activity&%40sort=activity&actor=&nosy=&type=&components=&versions=&severity=&dependencies=&assignee=&keywords=2&priority=&%40group=priority&status=1&%40columns=status&resolution=&%40pagesize=50&%40startwith=0&%40action=search). To work on one of those bugs, grep through the test code for the bug\'s id number, uncomment the relevant portion of the test case, and then start working on implementing the feature of fixing the bug that\'s needed until the test passes.
