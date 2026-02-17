# CodeCoverage

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page discusses code coverage in general.

[Python Developers Guide Coverage](https://docs.python.org/devguide/coverage.html) discusses coverage testing of Python, the language.

## Overview 

There are several subconcepts of **Code coverage**, which is just a quantitative measure of finding out how much of the code has been executed. The concept can be deceptive, though, if one doesn\'t know exactly what those figures mean.

For example, all of the following are subconcepts of code coverage:

- Statement coverage
- Line coverage
- Condition coverage
- Decision coverage
- Multiple condition coverage
- Path coverage
- \...

The problems is that 100% line coverage doesn\'t guarantee *anything* (well, except that the interpreter has traversed each line, nothing more :). For example, consider the line

    if a.bar() and b.frob() or c.frob():
        do_something()

if a.bar() evaluates to false, b.frob() isn\'t usually executed at all due to [ShortCircuit](./ShortCircuit.html) evaluation. b.frob() can be as broken as ever, but still line coverage can read 100% thus lulling developer into false sense of security. Condition coverage is a bit better, but it still doesn\'t try everything: what about loops? And even if a loop is executed no times at all and maximum amount of iterations, it still doesn\'t test everything.

Certainly one discovers quickly that to really test all execution paths, you have to test all possible paths, and even that leaves questions (what about if some loop is executed only max/2 iterations? what about all possible inputs?).

Still, even line coverage is not useless. For developer, it allows one to notice those parts of codes that haven\'t been even glanced at yet. In interpreted languages, those parts can contain even typos which usually lead to immediate crashes (calling a non-existing method, for example). Part coverage tests much, much more, but unfortunately, the amount of test paths rises exponentially in each decision. For a simple module with 20 if statements, each having 2 possible alternatives, there are 2\*\*20 \~ 1 million different paths of execution. Add to that a few loops and one more complex condition there and another elsewhere, and you quickly run into billions of test paths. In any real-life project, even 10% path coverage can be just impossible to achieve.

Still, path coverage may be useful for testing only single methods which contain complex algorithms. For Python, it seems like we have only statement coverage so far, thanks to efforts of Gareth Rees and Ned Batchelder. More advanced tools are under development, however.

## Tools 

- [http://pypi.python.org/pypi/coverage](http://pypi.python.org/pypi/coverage) Code coverage measurement for Python by Ned Batchelder

- [http://darcs.idyll.org/\~t/projects/figleaf/doc/](http://darcs.idyll.org/~t/projects/figleaf/doc/) figleaf by C. Titus Brown

## References 

- [http://www.bullseye.com/coverage.html](http://www.bullseye.com/coverage.html) Code Coverage Analysis

- [http://pycheesecake.org/wiki/PythonTestingToolsTaxonomy#CodeCoverageTools](http://pycheesecake.org/wiki/PythonTestingToolsTaxonomy#CodeCoverageTools)

------------------------------------------------------------------------

[CategoryEditors](CategoryEditors)
