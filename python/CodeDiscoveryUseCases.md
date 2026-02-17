# CodeDiscoveryUseCases

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Based on Python-ideas thread [My objections to implicit package directories](https://groups.google.com/d/topic/python-ideas/QYlbtgnSfM4/discussion) by Alyssa Coghlan and [this message](https://groups.google.com/d/msg/python-ideas/QYlbtgnSfM4/jJCM6PirLYIJ) from Yuval Greenfield:

    I've always had trouble understanding and explaining the complexities and intricacies of python packaging.`

    Is there a most basic but comprehensive list of use cases?

standard library

:   import from a list of paths to be searched.\<

current project
:   import from a relative path based on this file\'s current directory

package bundled with project
:   import from a relative path based on an anchor directory

virtual-env
:   import from an alternative lists of paths based on an anchor directory
