# TestSoftware

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Complete Taxonomy 

- Please visit the [PythonTestingToolsTaxonomy](../archive/PythonTestingToolsTaxonomy) for a much more complete list of test tools of all kinds.

## Software 

- [UnitTest](./UnitTest.html) in the standard library ([http://docs.python.org/lib/module-unittest.html](http://docs.python.org/lib/module-unittest.html))

- [PyUnit](PyUnit) at [http://pyunit.sourceforge.net](http://pyunit.sourceforge.net)

- [StatementCoverage](http://www.garethrees.org/2001/12/04/python-coverage/) This module runs your code, then produces a report on how many statements were executed, and which ones were not. Use it to ensure your unit tests test everything.

- [DataTest](./DataTest.html) at [http://formencode.org/docs/DataTest/README.html](http://formencode.org/docs/DataTest/README.html)

- [McCabe](./McCabe.html)-like Python Cyclomatic Complexity analysis tools are available at [http://journyx.com/curt/complexity.html](http://journyx.com/curt/complexity.html). They\'re written in Perl, but read and analyze only Python code. Complexity is bad, this will help you simplify code - especially code you didn\'t write.

- [zope.testing](http://www.python.org/pypi/zope.testing) provides a powerful test runner that supports test discovery and a wide range of options to control how tests are run and results reported.

- [nose](http://somethingaboutorange.com/mrl/projects/nose/) is \"a discovery-based [unittest](./unittest.html) [extension](./extension.html)\" that generally also supports [PyTest](../testing/PyTest) functionality.

## Best Practices 

## Discussion 

Sprouted out by [http://formencode.org/docs/DataTest/TODO.html](http://formencode.org/docs/DataTest/TODO.html).

What I need is a layered test system like

- test suit
  - with fast/normal/detailed mode
  - with known failing tests excluded
- test package to group related tests with preset parameters
- individual test
  - with options like log details
  - with ability to flex parameters, extend options etc.
- test utilities
  - fuzzy difference
  - different logging/reporting/visualization helpers
  - with output capture capability

\-- [MikeRovner](MikeRovner) 2004-02-27 19:25:32
