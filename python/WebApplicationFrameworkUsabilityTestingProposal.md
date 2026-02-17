# WebApplicationFrameworkUsabilityTestingProposal

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Preparation Stage 

As many frameworks as possible are contacted about a usability test taking place in 2 months\' time after the notice goes out. If they want to participate, they need to provide:

1.  The full code necessary to solve a specific problem given to them (a trivial pet shop website or whatever)
2.  A tutorial in any format that explains how to duplicate the code solution that they provide. This document should explain how the framework works in the process.

Each framework is responsible for individually coordinating how these documents will be prepared and produced.

If a framework is not bundled with either of (a) a templating system, or (b) a persistence system, the framework is responsible for recommending a third-party system that should be used for this testing. The framework is also responsible for either documenting how these systems should be used in conjunction with their framework, or arranging for the third-party to write this portion of the documentation.

# Testing Stage 

Undergraduate computer science students at the University of Toronto (where I have a large pool to draw from) would be recruited for the testing stage. The students recruited would have the following experience:

- CSC207 (which provides them with Python experience), and
- Either CSC309 (Introduction to Web Programming) or equivalent work experience

The testing stage would last one full working day (7.5 hours) and students would be paid a small stipend in order to simulate a work environment.

Each student would be assigned a framework. Although more than one student would work on a framework, they wouldn\'t work together. They would have to complete as much of the following tasks as they could in one day:

1.  Read through the code and tutorial provided.
2.  Make a small change to the code. For example, adding in a specific new feature. This tests code readability when the code is written \"properly\" (the way that the official framework says that it should be written).
3.  Start a whole new website. They would be given HTML outlines of the desired site and would be allowed to use the tutorial, code, and any online resources that they wish. However, all online resources that they use would be resources that they independently were able to find.

Every half hour, the students would be stopped for a brief period to jot down any problems that they\'re facing, documents they\'re using, things they liked, etc. This would be done continuously because it\'s easy to forget what problems you were having an hour ago.

Also, as a small but separate testing stage, a handful of graphic designers would be recruited. These graphic designers would be chosen as ones who know nothing about Python and would be asked to make a small layout change to the website that the frameworks provided us with. This would test the separation of presentation and logic, as well as the readability of the templates.

# Analysis Stage 

The code produced by the testing participants would be analyzed, and their comment logs would be thoroughly examined in order to produce usability testing conclusions for the participating frameworks.

In exchange for participating, each framework would gain:

- Better documentation (the extensive tutorial written by them)
- A list of the pros and cons of their framework as seen by the testing participants
- A chance to be recognized as one of the strongest frameworks if theirs is one of the frameworks that \"wins\". This recognition can be used as publicity, incentive for book publication deals, etc.

The Python community in general would gain:

- A document containing conclusions about which frameworks were determined to be the easiest to use.
- A list of strengths and weaknesses for each of the participating frameworks.
- Stronger documentation for all participating frameworks.
- An assessment of which frameworks should be pushed forward as the \"official recommendations\" of the community.

# Comments 

This proposal is still being designed. Please send comments to [ml@cs.toronto.edu](mailto:ml@cs.toronto.edu), or add below

------------------------------------------------------------------------

*Hope I\'m not taking too much of a liberty by putting this proposal here. \--[ChrisAkre](./ChrisAkre.html)*

------------------------------------------------------------------------

I would change the tasks performed by the students to something like the following:

1.  Follow the steps in the tutorial, taking notes after the completion of each tutorial step/chapter:
    i.  download
    ii. configure
    iii. load starting data
    iv. create application
    v.  test application
2.  Make a number of small, well defined changes to the tutorial application, again taking notes after the completion of each tutorial step/chapter. For example:
    i.  Add a reporting/data summary page
    ii. Add a per-user customizable parameter (such as a CSS theme)
3.  Create a whole new website.

For the new webiste creation task, the tester would be given HTML samples, starting data, and a functional specification for the desired site and would be allowed to re-use any code from the tutorial. The functional specification would break up the desired functionality into blocks of work that an experienced developer could implement in 30-90 minutes. This should allow a more objective comparision of partially completed work.

------------------------------------------------------------------------
