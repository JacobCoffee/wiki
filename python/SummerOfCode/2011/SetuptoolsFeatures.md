# SummerOfCode/2011/SetuptoolsFeatures

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Abstract 

Distutils2 is the new, improved version of the Python Distribution Utilities, a library used to package, distribute,build and install Python projects. It will be as a substitute of current setuptools, but it's still in its early stage. This project is supposed to fill the gap for setuptools users that want to move to packaging in three aspects:

1.  add the 'develop' command for Distutils2;
2.  add the automatic script creation functionality;
3.  perfect the extensions project.

# Milestones 

The following is just a very preliminary plan about what 'product' or improvement should be realized at what time. And the specific time and milestones maybe adjusted in future development if necessary after careful communication with mentor.

## My week-by-week work plan: 

**May 25-May 27: have a good communication with mentor to understand the project better and know the preparation work**

**May 28-May 31: get all preparation work done**

Under normal circumstances, developer often rebuilds or reinstalls their projects after he has made some changes to it during development. It\'s a little boring and will take time to copy files. So it's a very important feature that setuptools offers to users, especially developers using version control system to manage code, which allows users to make the code apear as installed to Python and other code can import it, but without copying any files. However, Distutils2 doesn't support this important command currently. Thus the job with the highest priority is to add the 'develop' command and fix the bug [http://bugs.python.org/issue8668](http://bugs.python.org/issue8668)

**June 1-June 20: begin to code and fulfill the 'develop' command**

- June 1\~June 10: write tests to will-be added functions and features(run all the tests iterately to make all functions pass the test)
- June 11\~June 12: fulfill the function to create the .pth file
- June 13\~June 15: fulfill the function to generate .dist-info dirs in place
- June 16\~June 20: fulfill all parameters of the 'develop' command as in setuptools

There is no easy way to have an executable script's filename match local conventions on both Windows and POSIX platforms. Setuptools fixes it by defining 'console_scripts' or \'gui_scripts\' entry points in setup script, which can automatically generating scripts for you with the correct extension, e.g. .exe for windows. It will take great convience to users who want to make his work run on different platforms, thus, the second job is to add automatic script creation function for Distutils2 and fix the bugs --issue870479: [http://bugs.python.org/issue870479](http://bugs.python.org/issue870479) ,issue976869: [http://bugs.python.org/issue976869](http://bugs.python.org/issue976869)

**June 21- July 11: add the automatic script creation functionality**

- June 21\~June 22: study the background and discussing details of bug issue870479 and review the patch already submitted by others
- June 23\~June 24: study the background and discussing details of bug issue976869 and review the patch submitted
- June 25\~June 30: read documents and source code of setuptools automatic script creation
- July 1\~July 7: write functions to realize automatic script creation for Disutils2
- July 8\~July 11: write tests to changes

extensions is a simple plugin system inspired from setuptools entry points and it allows an application to define or use plugins. This feature offers to user great convenience to develop big systems composed of different components. So the third job is to help perfect the extensions project if necessary.

**July 12\~Aug 15: check whether the extensions project can perform perfectly as setuptools entry points does in real projects and do some necessary integration work**

- July 12\~July 15: read documents and source code of setuptools to get to know the principle of its entry points;
- July 16\~July 22: checkout the extensions project from bitbucket and read corresponding documents and source code;
- July 23\~July 29: try to construct different test cases(real project is preferred) to check whether the extensions project can 'produce' correct output as expected and has fulfilled all the features of setuptools entry points;
- July 30\~Aug 4: report bugs and fix them if new feature should be added or enhanced;
- Aug 5\~Aug 8: write tests for newly added or modified functions
- Aug 9\~Aug 15: strength early documents and write new documents for new changes

# Start of Program (May 24) 

- Create a project on bitbucket
- Create a page on python wiki
- Get familiar with Python's bug tracker
- Read PEP376 and PEP345 details
- Look into 'develop' command in setuptools
- Look into setuptools entry points
- Look into setuptools automatic script creation
- Make preliminary plan and list it on python wiki page

# Midterm Evaluation (July 12) 

Before midterm evaluation, 'develop' command and the automatic script creation functionality should be fulfilled and corresponding bugs fixed. Thus the proposed deliverables could be:

- Wrapper scripts can be created
- most parameters in setuptools should be supported
- Fix bug issue8668
- Fix bug issue870479
- Fix bug issue976869
- The patch of automatic script creation should be submitted.

# Final Evaluation (Aug 16) 

Before final evaluation, work for the extensions project makes it perform better as setuptools entry points. The detail is:

- Test cases for extensions project constructed
- Documents of extensions project enhanced
- the extensions project is more \'close\' to setuptools entry points, or even more powerful

# About Me 

I\'m an undergraduate from China and I\'m preparing for my computer science and technology bachelor degree in USTB (University of Science and Technology Beijing). Java and Python is the main programming language when I write programs and software. During my coding days, I'm getting to know more and more about the Open-Source/FOSS, especially its spirits-share, collaborate, make friends. Every time I find an excellent solution of problems occurred to me, I become so excited and learn a lot from the process of problems finding-reporting-solving.

## My Strengths: 

- Good communication, writing, reading skill with email, irc, and skype
- Good knowledge of revision control. Although I always use TortoiseSVN to host my project and do daily coding, it's not a big problem for me to use Mercurial to manage Python projects, and I will spend much time on reading the user\'s guide and other helpful documents to get myself familiar with it.
- Good problems-solving ability. If there are some problems, I will at first try to find useful information from the user and developer documents, then search them in the Google to look into if other people have the same or similar problem and have already given the solution. What the wonderful thing is that I always can find many discussing emails or archives in the google group or bug repositories, and it is the time when I begin to know and get familiar with Eclipse bugzilla and Python bug tracker(In these days).
- Formal education in programming. My major is computer science and technology.
- Adequate time. Most of the time is among my summer vocation, so time is ok for me. 40 hours a week is also no problem, because I can do the job at nights.

## My weak points: 

- Not very good knowledge of Distutils2. I can spend much more time on reading the useful documents and the source code cloned from bitbucket.
- Different timezone. I'm in China, so there maybe a problem when communicating with mentor. But email, skype and irc all are very good tools to solve it.
- Not very familiar with Python bug tracker. Actually, I'm new for the Python bug tracker and just registered an account days ago. These days I spent much time on reading discussing contents in it, and tried to write a patch to fix a bug as my first work.

# Contact Info 

a.  Name: Xu Dehai(You can call me with my English name-**higery**)

b.  Blog: [http://higery.wordpress.com/](http://higery.wordpress.com/)

c.  Email: (masked for spambots, see page history or GSoC page or Roundup or mailing lists or ask merwok)

d.  IRC: **higery** on **irc.freenode.net**

e.  Skype: (masked)

f.  Phone: (masked)

g.  Postal (masked)

h.  City, State, Zip, Country: (masked)
