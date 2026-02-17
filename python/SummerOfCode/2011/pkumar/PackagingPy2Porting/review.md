# SummerOfCode/2011/pkumar/PackagingPy2Porting/review

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Here's a review of your proposal. You can reply to specific issues in comments of the GSoC site or amend your wiki page to address my comments.

1.  Since \'Packaging\' is made after many improvisations and modifications over distutils2, it will prove to be a better utility than the currently existing distutils2 for all the versions of python.

This is a slight misunderstanding: packaging == distutils2. The current status of the merge of packaging can be confused, since new contributors are working on it in new repos, and some feature work has been mixed with the 3.x porting, but in general packaging does not have many improvisations over d2. packaging is the name of the new distutils in the 3.3 stdlib, distutils2 is the name of the same thing as a standalone release.

- The tutorial provided will help in the further development of the project.

That's a good point in your application: tooling, documentation and blog posts should be helpful to other projects doing 3to2 conversions.

- \- Applying 3to2 to \'Packaging\' for all the versions of python2.

What about 3.1, which does not have all the features that packaging uses in 3.3?

- \- Fixing \'type\' issues corresponding to bytes and string.

How? Manual fixes, librefactor fixers, magic comments used with a special fixer, runtime checks (which can be broken by 3to2)?

- \- Fixing import errors wherever required.

2to3 fixes imports, 3to2 probably does too, it's one of the basic and easy things.

- \- Few basic modifications in the code to make it compatible with other versions of python.

Precisely?

- Adding and rewriting few tests for the newly made changes.

Why is there a special line for tests? Are they handled differently than the rest of the code?

Also, what about docs?

- Ensure that build and installation process go well for all the versions of python i.e. 2.4 - 3.2

How? You're not supposed to have everything figured out before GSoC starts, but you have to have a general idea.

- Initial preparations includes the following:

How far are you on those steps? You should also read docs.python.org/devguide

I find your timeline unsatisfying. It's rather vague, and your approach of ad-hoc fixing of modules does not look sustainable. What we want is a robust, repeatable way of making releases out of the stdlib. Your list of deliverables is incomplete: first, it's vague ("\'Packaging\' compatible with 2.4-3.2" should be "sdists of distutils2 for each supported version"), second, it shows that the approach you have chosen is "convert once, document, hope it's easy too the next time", which is not the approach I would have taken.

In my opinion, this project is more about 3to2 than packaging. Its deliverable should be a command-line script which copies packaging from a directory, runs 3to2 with a set of fixers and runs sdist commands. The main milestones should involve reading about other projects using 3to2, how to solve difficult bytes/string issues, and writing custom fixers for that. The goal is that we can use that script in six months and a year and three years, with new fixers or minor adjustments to the code, but not just "run 3to2 + fix all the problems".

What do you think?

## Second review 

- Some functionalities in python2 works differently compared to python3 i.e. we may need to write slight different codes for the same result, say \'tokenize\' in this case.

Are you talking about manual edition to the code after running 3to2? That's the ad-hoc approach I speak against in the end of my review.

- At certain instances, tests written for python3 may not work for python2 i.e. the returned value may differ. In those cases, we would have to manually rewrite codes for different test behaviors.

This does not answer my question. Tests may exercise code that returns different values, but that's not specific to tests.

- Documentations would be updated simultaneously with the progress of the work.

Manually? Can 3to2 convert Python code in docs?

- Currently \'import build_py_2to3 as build_py\' is taking care of build and installation process for different versions of distutils2. But that won\'t be adequate for the backport. For this project, I\'m not sure if we can modify \'build_py\' file in distutils for \'build_py_3to2\', so that it can work other way round. If we can\'t, in that case there should be a piece of script which will run 3to2 on all files of \'packaging\' and then copy them to a temporary directory or may be directly build it.

Ah, writing a build_3to2 class is an interesting idea.

1.  \'Packaging\' compatible with python2.4 to python3.2.

Again, please be precise: say whether this will be a VCS branch, or an sdist, etc.

1.  A automated system of \'packaging\' to govern the porting process for different specified versions of python.

I see you've taken my suggestion. Just a note about the wording: "a automated system of packaging" is not clear at all, maybe say "a script running 3to2 with custom fixers for each support Python version".

Can you go through my first review again and reply to the things that you've left out in your first reply?

I recommend you to remove the bits of discussion from your wiki page and amend it quickly (today or tomorrow) to integrate the result of our discussion: reworked list of deliverables (script and 3to2 fixers needed for each version) and adapted timeline (esp. with time allotted to research whether fixers can fix everything or if you'll have to develop a magic comment system to have version-specific code in comments to be uncommented for the right version).
