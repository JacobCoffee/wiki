# PackagingWG/2020-02-07-pip-explanation

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

\[Bernard and Pradyun spoke on Feb 6 and Feb 7 to give Bernard an understanding of pip\'s architecture.\]

# Feb 6th 

Pradyun/Bernard discussion, 6 Feb 2020

Which side of we want to start from? User-facing or broader architecture

At a reasonably high level, what are the moving parts of pip?

Software architecture:

- pip is for installing packages, like a car is going A-B. the main bits within pip are
- a chunk of logic for downloading the things we
- a chunk of logic for converting what we\'ve downloaded into something we can install
- deciding amongst the things we see we should download and install
- final chunk for installing things
- one chunk for uninstalling things
- methods for see the environment - e.g. it\'s state, whats installed
- search - for discovering things - reading YAML files (pip search yaml)

The different parts of pip:

- env

- config files - saves the user having to express synat ever time (e.g., looking to user\'s own dev infra for downloading packages, etc)

- cli - parsing user input syntax [https://pip.pypa.io/en/stable/user_guide/#config-file](https://pip.pypa.io/en/stable/user_guide/#config-file)

- implentation files -

- [https://pip.pypa.io/en/stable/reference/](https://pip.pypa.io/en/stable/reference/)

- [https://pip.pypa.io/en/stable/user_guide/#config-precedence](https://pip.pypa.io/en/stable/user_guide/#config-precedence)

- [https://packaging.python.org/key_projects/](https://packaging.python.org/key_projects/)

- [https://pradyunsg.me/talks/slides/2019-python-packaging-overview.pdf](https://pradyunsg.me/talks/slides/2019-python-packaging-overview.pdf) \-- some relevant notes

- [https://pradyunsg.me/talks/](https://pradyunsg.me/talks/) \-- has the video of the talk corresponding to those slides

Chunks of work ([https://github.com/pypa/pip/milestone/10](https://github.com/pypa/pip/milestone/10))

knowing what the key func is

figuring out if the way we printout of the output is useful

making the info message look less like error message to the users

making the error messages more helpful

give them tools to debug the problem

there is a tradeoff here - more error messages, the more complexity you add to the codebase. every detailed message needs to add code and this adds complexity to the codebase

which switches are useful? which are not?

How possible is it for us to map all the pip command journeys\' flows? Essentially

Look at how long this is: [https://pip.pypa.io/en/stable/reference/pip_install/](https://pip.pypa.io/en/stable/reference/pip_install/) (complexity in pip\'s options)

# Feb 7th 

Pradyun / Bernard discussion 7 Feb 2020

From Zulip conversation: *\"UX research on \"professional\" workflows, closed-source/\"industry\" usage. That\'s a base of users that we have very little access to.\" I\'m not sure what routes we can find into that\...*

- research question: what are the workflows of professional users in \"closed-source/industry\"?

*pip install / wheel / download*

Install is a superset of wheel, which is a superset of download - to draw \*very\* broad strokes

*a chunk of logic for converting what we\'ve downloaded into something we can distribute/install*

pip build logic since PEP 517 we\'ve not had a good story for users who want to use sources

Bernard is fairly new to software dev; has experience w/ hardware + electronics; used software mostly as a consumer/user in the past.

Research question (needs better work):

- how do users expect to build packages into a format they can easily distribute \-- wheel distributions and source distributions

If I\'m a dev of a project that I want to publish that on PyPI. PyPI accepts certain types of files - wheels and distro - to go from local dir on my PC (which has all the files) to the state i can upload a built distro to pypi or a company server - that step is is unclear.

The reasons are described in this thread [https://discuss.python.org/t/building-distributions-and-drawing-the-platypus/2062](https://discuss.python.org/t/building-distributions-and-drawing-the-platypus/2062) . (Ignore the last 2/3 comments there\'s a lot of discussion.)

Q for me: what UX work needs to be carried out for this?

*pip list vs pip show vs pip search vs pip freeze*

These are all similar - they give information about packages

Looked at \"search\" related issues.

research questions:

- can we understand where users use these different functions in their workflow and what are they looking to do?
- how are users using these functions?
- are they discoverable?

Design: ideally the output of this would be to \"put all of this functionality into 2 buckets\"

review: install a bunch of packages and use the different

*search tagged issues: [https://github.com/pypa/pip/labels/C%3A%20search](https://github.com/pypa/pip/labels/C%3A%20search)*

2 patterns that users had issues with: no error messages / errors+info were together or \"mysterious\" messages

Q to Pradyun: is there a good approach to working out how to improve those messages?

- e.g.: paths of files that it\'s related to.

It depends on the context of how to display errors.

We have output that have holes that we want to fill - we need to work out what context needs to be given to the user

- [https://github.com/pypa/pip/milestone/25](https://github.com/pypa/pip/milestone/25)

- [https://github.com/pypa/pip/issues/5182](https://github.com/pypa/pip/issues/5182) \-- as an example - instead of displaying an exception, better to wrap it into a \"we tried to do this, but it failed\".

Past case of similar issues

- [https://github.com/pypa/pip/issues/5237](https://github.com/pypa/pip/issues/5237) (issue)

- [https://github.com/pypa/pip/pull/5239](https://github.com/pypa/pip/pull/5239) (fix)

Best practices for writing error messages: [https://www.nngroup.com/articles/ten-usability-heuristics/](https://www.nngroup.com/articles/ten-usability-heuristics/)

desk research: are there best design guidelines for writing error messages for promoting heuristic #9?

- eg. awscli, a CLI provided by Amazon; that Pradyun hopes has had UX eyeballs/inputs. Their resources might not be public though. :P
- continue with categorising print better error message issues.
- look at closed issues to see how they approached the solution

Good outcome: Maintainer guidelines for error messages

Optimistic outcome: Maintainer guidance on identifying areas where we might have such errors

[https://wiki.python.org/psf/Pip2020DonorFundedRoadmap](https://wiki.python.org/psf/Pip2020DonorFundedRoadmap)

*verbosity / output + failure visibility* Broader than error messages. is this in/out of scope?

## USER STORY 

As a user I want to know whats make the display less mysterious

- how do we want to structure our output? where (and in what order) do users expect to see errors messages, actions they have to react to? what is a useful information architecture for messages to be displayed? (install.py#L385)

The objective was to redo the output for the pip install command (and connected to wheel / download)

Do we want to interrupt the user in a resolve dep. issue, or print an error at the end?

TODO read this:

- [https://github.com/pypa/pip/issues/4649](https://github.com/pypa/pip/issues/4649)

- [https://github.com/pypa/pip/issues/4649#issuecomment-333690763](https://github.com/pypa/pip/issues/4649#issuecomment-333690763)

- [https://github.com/pypa/pip/issues/4649#issuecomment-333738894](https://github.com/pypa/pip/issues/4649#issuecomment-333738894)

Does the structure make sense?

- See how other package managers handle information output

Cascading tasks

- have helpers in the code there is a lot of output - do we want to show \*everything\*?

## Experiment 

experiment: take a package with lots of dependencies

- look at the regular output (regular = that which is not verbose), look at the verbose output see what is critical, what is not critical research question: identify what is critical, what is not critical.

how much output do users expect to see? how much output is useful to users?

what is missing from regular output, that\'s in verbose? (regular = that which is not verbose)

Are there \"defined\" steps in the complication?

- Yes and no - there are stages, not distinct steps.
- Each package that we see we download it, build it, see dependecies and do the same for them (looking at the env)
- how do we decide
- what to download
- what do we build?
- fetch dependencies
  - repeat
- then finally install

## The resolver 

*resolver* this resolves what to download, build, this gives us a state and how to get there.

*installing pip install* based on the result of the resolver

*the nuance of download, install, wheel* wheel - command for the user to run, to get wheels for all packages they will use. the user will end up with a lot of wheel files for each of the packages and deps in a dir.

when they do download they\'ll get wheels and source. Wheels have static metadata, sources do not. (this was the purpose of the proposed metadata 2.0. it also make dep resolv. harder)

This issue is grounded in the lack of metadata we have about packages.

In the process of downloading, pip might end up building wheels as part of the build anyway. in the dep resol loop, you can potentially build a wheel (they have dep information). Not sure where they end up (not so important).

Everything in the dependency resolution process it will build wheels out of those (if its not in the env already), after the resolution

if there is something downlaoded without a wheel, pip wheel will build that, or error out if its not possible.

download - we\'ll dump this into a dir the user

- TODO: user documentation about pip wheel and pip install
- TODO: discuss the nuance between install / download / wheel
  - suggestion: look at .py files for details: [https://github.com/pypa/pip/tree/master/src/pip/\_internal/commands](https://github.com/pypa/pip/tree/master/src/pip/_internal/commands)

    - [https://github.com/pypa/pip/blob/master/src/pip/\_internal/commands/download.py#L131](https://github.com/pypa/pip/blob/master/src/pip/_internal/commands/download.py#L131)

    - [https://github.com/pypa/pip/blob/master/src/pip/\_internal/commands/install.py#L327](https://github.com/pypa/pip/blob/master/src/pip/_internal/commands/install.py#L327)

    - [https://github.com/pypa/pip/blob/master/src/pip/\_internal/commands/wheel.py#L157](https://github.com/pypa/pip/blob/master/src/pip/_internal/commands/wheel.py#L157)

      - see what happens after resolver.resolve

*review the command line usability for automated scripts* pfmoore filed it \-- [https://github.com/pypa/pip/issues/6099](https://github.com/pypa/pip/issues/6099)

\"pip blowsup it usually ends up breaking someones pipeline. a lot of people are going to pinged, probably in the middle of the night.\"

technical/professional users

I get paid to work on python, everyday. I have specific workflows, I want control on how I build, where I download from, how pip is called

1\. scientific

- i have to compile
- research data science
- corporate application of data science
- more complicated build logic - using legacy/fortran/c code

2\. corporate

- software/web/dev
- easier/simplier requirements
- strict control of what we develop with

3\. distros

- who redistribute python \"stuff\"
- they are an intersection of 1 and 2
- differing requirements - they have their own audience (3) but server 2 + 3

4\. non-technical/professional users

- no idea how to even start with these; what\'s a priority etc - Pradyun

TODO: reread [https://packaging.python.org/glossary/](https://packaging.python.org/glossary/) as a result of today\'s discussion

Non-professional users will find it easier to find errors/warnings at the end

- TODO (Pradyun): Move the warn-about-conflicts to the end, based on an understanding of what we discussion

Bernard to make a branch for this work, make it and test it. Maybe work with Pradyun on the messaging.

- [https://github.com/pypa/packaging-problems/wiki](https://github.com/pypa/packaging-problems/wiki)

- [https://github.com/bokeh/bokeh/wiki](https://github.com/bokeh/bokeh/wiki)

- TODO bernard: give Pradyun link to the where I will be putting this notes.

- TODO bernard: Improve and restore packaging problems wiki

- TODO bernard: reread and digest: [https://github.com/pypa/packaging-problems/wiki/User-experience-issues](https://github.com/pypa/packaging-problems/wiki/User-experience-issues)
