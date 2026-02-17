# SummerOfCode/2011/SetuptoolsFeatures/review

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Here's a more detailed review, following my comments on the fellowship mailing list (which you haven't all addressed in your proposal or wiki page!).

- Under normal circumstances, people use the distutils to build a distribution of a project by rebuilding or reinstalling the project every time he made a change to it during development. So it's a very important feature that setuptools offers to users, especially developers using version control system to manage code, which allows users to deploy their projects for use in a common directory or staging area, but without copying any files.

I think there's still a slight misunderstanding, despite the exchange we've had in private and public email. Python does support running uninstalled code; for extension modules, running build_ext \--inplace does the trick. In other words, a developer does \*not\* have to rebuild and reinstall the project to run tests after each change.

The specific feature provided by the develop command is twofold: make the code appear as installed to Python, so that other code can import it, and make the egg-info metadata available to the pkg_resources system (in distutils2, it's dist-info and pkgutil). Does this make sense now?

Regarding implementation, the easy-install.pth hack used by setuptools is unacceptable for the standard library. Finding a clean way to implement it will be an interesting challenge.

With the advent of "python -m" as a way to run modules as scripts, I think that the part about generating wrapper scripts is not essential, and I'd suggest that it waits for after you've completed the feature about script generation, which should let you learn a lot about scripts. It's only a suggestion, other people in our group more familiar with setuptools may have a different opinion.

You'll need to learn a bit more about egg-info and dist-info metadata, which are not the same thing. For example, when you say "use PEP376 new apis to read metadata from .dist-info to create wrapper scripts", you show that you don't know that scripts are not mentioned in PEP 376 at all.

- June 15\~June 20: create the patch, then fix the bug.

Here your application shows a (very minor) misunderstanding of the tools: as you'll be working in a Mercurial repo, creating the final patch will only take seconds, not days. In a similar way, "fixing" a bug is only a bureaucrating task that consists in editing an HTML form. Writing the code is the actual work; closing the bug is just a thing we do to keep track of things, it does not take days. So please edit your timeline to remove those steps and reallocate the days for concrete tasks.

- Packaging and installing script can be a bit awkward with the distutils,

That's not true. You can call the suppport for Python scripts basic, but it's a simple and useful system which works. The setuptools feature is just a layer of added convenience and platform-specific workarounds.

- and there is no easy way to have a script's filename match local conventions on both Windows and POSIX platforms. Setuptools fixes these problems by defining 'entry points' in setup script.

To be precise, the "console_scripts" entry point is used to generate scripts. The feature we discuss is to port that thing only, not the whole entry points system: that's the extensions project.

- An opensource or free software always faces such kind of platform problems.

There is proprietary software that is deployed on many platforms too. Python and distutils don't take sides about software freedom, they support both worlds.

- As a outstanding packaging tool and perfect substitution of setuptools

To make things clear: distutils2 aims to be a better replacement for distutils, and also obsolete setuptools by taking its good ideas and running with it, but it is not a drop-in replacement. Also, perfection is never achieved : )

- June 21- July 11: add the automatic script creation function

I like that you plan to review the distutils patches before looking at the setuptools code, it sounds a sane way of diving in.

- July 5\~July 10: add automatic script creation function for Disutils2

This is a bit vague. Do you mean function as a Python function or the functionality, which will probably require multiple functions? Also, how will you do it? Are you familiar with writing tests? How about tests that run commands and inspect the file system? Is there already support in distutils2 for that? Again, you are not supposed to master the codebase before the GSoC nor have all the answers, but you have to show that you've given thought to it, made a bit of research and have concrete plans.

- extensions is a simple plugin system inspired from setuptools entry points and it allows an application to define or use plugins. This feature offers to user great convenience to develop big systems composed of different components. So the third job is to help perfect the extensions project if necessary.

I've read some old messages and blog posts again and found that Tarek explicitly wanted the extensions system to be decoupled from the packaging tool, so maybe my suggestion about it weakens your application. However, you did find a way to show the three tasks as a coherent proposal. I also think that it is a very important part of setuptools which we have to consider, and the knowledge of setuptools and Python that you will acquire during the first two tasks will make you suited to tackle this one. Last summer, a distutils2 student did work on it after all. It may also be that you're given other tasks after the student selection or after midterm.

- Aug 5\~Aug 11: strength the documents

Does this mean that you won't write docs and tests alongside the code?

- Aug 11\~Aug 15: report all these work to Distutils2 administrator

What does this mean? Why does it take four days?

- Configure development environment: python, revision control, email, skype, irc, etc.

The patch that we required serves to make sure that this is done ahead of time.

- Thus the proposed deliverables can be: - .pth file can be created on site-packages

Don't get too specific about implementation (especially since I don't want this one detail :--), stay at the user level.

- all parameters in setuptools should be supported, e.g. \--multiversion

Not all. Multiversion is a whole can of worms in itself, and would require discussion with the developpers of the import system; it's another topic entirely.

I hope this long message is helpful. To reply to it, please amend your proposal on the wiki (I will get automatically notified) or reply to specific items on the GSoC site.

# Second Review 

- May 25-May 27: have a good communication with mentor to understand the project better and know the preparation work

Looks like we've already started on that :--)

The first paragraph describing the develop command still says that people run distutils to test changes, which is still not true, but the rest of the paragraph is good, as it says that the feature is to make the code appear as installed (including making egg-info/dist-info metadata available to the system, which you did not explicitly say).

→ This is still true.

- June 1-June 20: begin to code and fulfill the 'develop' command

Regarding the timeline, I would encourage you to write tests before code. You'll probably take as much or more time to write tests than code, and writing tests beforehand helps you covering all cases and figuring out the API of the code. It may appear a strange method, but it turns out that it's really helpful and working. Of course, this being Python, sometimes you just write the code in ten minutes before the tests because it's too easy :--)

→ Xu edited his proposal to take that recommendation into account.

I wrote this in the first review:

- With the advent of "python -m" as a way to run modules as scripts, I think that the part about generating wrapper scripts is not essential, and I'd suggest that it waits for after you've completed the feature about script generation, which should let you learn a lot about scripts. It's only a suggestion, other people in our group more familiar with setuptools may have a different opinion.

What is your opinion?

→ Reply by private email: I think you are right, future work on script generation will make me more clear about the wrapper scripts functionality, so I removed this task from my application and adjusted the timeline.

- There is no easy way to have an executable script's filename match local conventions on both Windows and POSIX platforms. Setuptools fixes it by defining 'console_scripts' or \'gui_scripts\' entry points in setup script,

I had forgotten gui_scripts, very good catch!

- June 21\~June 22: study the background and discussing details of bug issue870479 and review the patch already submitted by others June 23\~June 24: study the background and discussing details of bug issue976869 and review the patch submitted

I will create a new bug to track your new work and close the older ones as duplicates (the discussions will still be there to read), it will be easier to use than half a dozen of duplicate bugs.
