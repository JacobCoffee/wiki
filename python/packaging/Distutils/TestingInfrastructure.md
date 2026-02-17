# Distutils/TestingInfrastructure

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

=David Lyon=

## Question 

What\'s the existing Testing Infrastructure for distutils?

The following comments may be beyond the scope of Distutils [TestingInfrastructure](./TestingInfrastructure.html).

I may need to withdraw them shortly.

## Introduction 

One of the big challenges for Python going forward is providing a testing infrastructure for Python Packages.

There are now over 6,000 packages listed on [PyPi](./PyPi.html) - and this number can only get bigger.

Then, there are the three major operating systems:

- Windows
- Mac
- Linix/Unix

To complicate the problem, there are now many versions of each operating system.

Multiply those two combinations by all of the versions of Python that already exist (not to mention the ones coming) and we start to that we are heading into complexity. If there are 4 major windows revisions and 4 major Linuxes, and two major Mac platforms, we end up with perphaps (6,000 x (4 + 4 + 2)) 60,000 delivery possibilities.

That number then needs to be multiplied by the number of python versions, which possibly include 2.1, 2.2, 2.3, 2.4, 2.5, 2.6 and coming up.. the 3 series\...

So that could be (60,000 x 7 (python versions)) 420,000 variations of known python packages.

To date\... the testing has been done\... we have to assume\... manually with some automation.

But we can\'t expect package maintainers to be forever testing their own code on platforms that they simply don\'t have access to.

A more reasonable and cost effective option is to have this testing done on a server farm virtual environment building infrastructure.

In simple terms, we need to build all the packages that exist for Python on a daily basis on all of the environments and report any issues back to the registered maintainers.

This job is too big to be done manually. We need to use either a Super-Computer or a Server Farm. Fortunately, Server Farms are close at hand.

## Server Farm Virtual Environments 

Google and Amazon web services are two organisations amongst others that offer commercial virtual server farms that could be employed to do the above build process of all the python packages.

Python scripts would be developed utilising the python \"test\" frameworks to supervise the build on each and every platform.

With this basic structure, a daily building/testing infrastructure working across the different versions of python and operating systems, could easily become a reality.

At present AWS offer virtual environments for both Windows and Linux. These can be seen on these links:

- [http://developer.amazonwebservices.com/connect/kbcategory.jspa?categoryID=209](http://developer.amazonwebservices.com/connect/kbcategory.jspa?categoryID=209)

- [http://developer.amazonwebservices.com/connect/kbcategory.jspa?categoryID=208](http://developer.amazonwebservices.com/connect/kbcategory.jspa?categoryID=208)

A service to do building on Mac Virtual Machines needs to be located.

## Test Scripts 

A test script will be developed that will cycle through all the packages on pypi, download the package and build it on all available platforms.

The results of the build can then be made available via some sort of web delivery system. Describing on which platforms the builds were successful and not.

In the past, it has been difficult for developers to test on all platforms.

These facilities are bound to improve overal code quality across the python universe.

## Scope of Testing 

It\'s important to define what and can be and what cannot be tested.

The scope of the framework will be:

- to check that each package can be installed on all the relevant platforms
  - using the setup.py script
- to run the built in tests within the package
- to check that the package can be de-installed on the relevant platforms
