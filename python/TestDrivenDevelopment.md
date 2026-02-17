# TestDrivenDevelopment

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Overview 

**Test Driven Development** (TDD) is a method of designing software.

It goes roughly as follows: write [UnitTests](UnitTests) for the code *before* you write the code itself.

Why do it the \"non-natural\" way, then? Well, there are some benefits and very few - if any - drawbacks:

- Coding tests means you have to call your non-existing code with all the parameters thus forcing you to think how your library should work, thus it fixes the [Signature](./Signature.html) of your code

- You realize many errors in the code before you even wrote it, especially design-related errors

- You will get better estimate how long coding will take

It is very important to emphasize TDD is *not* a testing methodology; it is a *design* methodology.

## More information 

- [http://www.agiledata.org/essays/tdd.html](http://www.agiledata.org/essays/tdd.html)

- [UnitTests](UnitTests)

- [CodeCoverage](CodeCoverage)

- [ContinuousIntegration](ContinuousIntegration)
