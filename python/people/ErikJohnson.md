# ErikJohnson

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Erik Johnson 

I am a member of the Albuquerque Python Meetup: [http://wiki.python.org/moin/AbqPython/](http://wiki.python.org/moin/AbqPython/) [http://www.meetup.com/AbqPython/](http://www.meetup.com/AbqPython/)

My email: Spam is largely out of control on the internet. Sometimes I check email at [HedgesFan](./HedgesFan.html) at G mail dot com. If you want my regular email address that is checked almost daily, ask me for it.

## Neat Python Tricks 

#37: Actually check that download checksum: Most people I know, even most programmer, have never actually checked that checksum that is published with a download (for example: [https://code.google.com/p/pyodbc/downloads/detail?name=pyodbc-3.0.7.win-amd64-py2.7.exe](https://code.google.com/p/pyodbc/downloads/detail?name=pyodbc-3.0.7.win-amd64-py2.7.exe)). That\'s perhaps understandable, as its not immediately apparent how you would do this. Most programmers can find a way if they want to (like Google some tool), but have you ever actually done it? If you have Python installed, you\'ve got a major power tool at your disposal.

Assuming I have the file `pyodbc-3.0.7.win-amd64-py2.7.exe`{.backtick} sitting in the local directory, start the interactive python interpreter in that directory:

    >>> import hashlib
    >>> hashlib.sha1(open('pyodbc-3.0.7.win-amd64-py2.7.exe', 'rb').read()).hexdigest()

Should print out: `cc409b505428091e446316d87701d423eb984e8f`{.backtick}

(NB: 2016-Oct-02 The link above used to go to a page that had a link for the file and showed the checksum you should be getting. It looks like the structure of that page has changed such that the link goes directly to the file. I\'m not seeing the published hash now.)

## Python Ramblings 

I am currently doing a course on Coursera titled [An introduction to Interactive Programming In Python](https://class.coursera.org/interactivepython1-003). (The link is to the actual instance of the class I am in - you may need to go in through the Coursera front page and search class listings to get to the next offering of the class.)

I don\'t really expect to learn a lot about the Python language itself, but some neat things are starting to happen with programming languages in general. In this case, they are using a [wholly in-browser environment to run Python](http://www.codeskulptor.org/). It\'s not quite the same Python, but almost (one shortcoming I noticed is iteritems() on dict is missing.) This is based on [http://www.skulpt.org/](http://www.skulpt.org/).

## Programming Contest Sites 

- [The Python Challenge](http://www.pythonchallenge.com/)

- Sphere Online Judge (SPOJ) [http://www.spoj.com](http://www.spoj.com)

- CodeEval [http://codeeval.com](http://codeeval.com) (my profile: [https://www.codeeval.com/profile/epj/](https://www.codeeval.com/profile/epj/))

- CodinGame [http://codingame.com](http://codingame.com)

- ProjectEuler [http://projecteuler.net](http://projecteuler.net)

- UVa Programming Challenges [https://uva.onlinejudge.org/](https://uva.onlinejudge.org/) (kind of like SPOJ, but in Spain. There is a published book that goes with this (not needed to do challenges): [https://www.amazon.com/Programming-Challenges-Training-Computer-2003-05-12/dp/B01FKS8J0O/ref=sr_1_2](https://www.amazon.com/Programming-Challenges-Training-Computer-2003-05-12/dp/B01FKS8J0O/ref=sr_1_2) )

- uHunt Training Series [http://uhunt.felix-halim.net/series/](http://uhunt.felix-halim.net/series/)

- Competitive Programming Books by Steven Halim: [https://sites.google.com/site/stevenhalim/](https://sites.google.com/site/stevenhalim/)

## Other Programming-Related Sites 

- CodingGround [http://www.tutorialspoint.com/codingground.htm](http://www.tutorialspoint.com/codingground.htm) In-browser console windows to code simple things in many different languages.

- PythonAnywhere [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/) Hosted python you access via an in-browser console window.

- [http://www.skulpt.org/](http://www.skulpt.org/)

- CodeSkulptor [www.codeskulptor.org](http://www.codeskulptor.org/) Coursera & Rice University\'s wholly in-browser Python dev environment (based on [Skulpt](http://www.skulpt.org/))

## Vim stuff / Python indentation 

Significant whitespace (i.e., indentation) is one of the biggest complaints I hear about Python. I have to admit I was not a big fan of it at first and had some issues with spaces and tabs getting mixed up and causing my program to not run correctly.

I have since come to see Python\'s significant white space as one of its best features. Python executes just like it looks, and looks just like it executes! That\'s because they\'ve been defined to be the same thing! Code reads just like it is \*actually\* structured. Lazy programmers that add a few braces to create new blocks can create code that looks differently than it is actually structured.

So, this was a conscious decision to try to address one of C\'s problems. You can\'t be lazy and not indent your code properly. You get the structure right to get the program to run right and resolve the readability problem at the same time - not put it off as a nicety to be skipped over. \'This is an aid to ***readability*** and ***understandability***!\' IMO: It definitely is ***NOT a design flaw!*** On the contrary, it was a wise decision that ultimately saves typing and makes code more readable, letting you focus on the important parts of logic and code structure rather than a page full of curly braces (that, in other languages, ***should*** but, in general, may or may not be indented to reflect the actual block structure).

I did have a colleague come to me once (I guess as some sort of perceived representative for Python) and bitterly complain: \"I remember now why I don\'t like Python! When you store your source code in PDF format, all the indentation gets stripped! That\'s such a pain in the -bleep-! No other modern languages have this problem!\" Yes, well\... some people will \"get\" this design decision, others may not. I just laughed and told him:

\"I\'ve used Python for over 10 years, and have ***yet*** to run into this problem.\"

It\'s not a convincing argument that something is wrong with Python. Python wasn\'t designed for that nor did it ever advertise or suggest that you could store Python source as PDF. (To be fair, this wasn\'t the primary mode my colleague was using to store his code, of course, but he had lost some code and recovered a script embedded in a PDF document from somewhere else.)

It is, however, a compelling argument not to store your Python source in PDFs. Leading white space in Python is significant - you can\'t get around that. If you\'ve lost all your source formatting, I would say that\'s a problem whether your source still compiles and executes properly or not. (Other languages will have a slight advantage in this situation, but now you are confined to only running the code. If you intend to read, understand, maintain and/or develop the recovered source, you\'re going to have to reformat it anyway. [PrettyPrinters](./PrettyPrinters.html), formatting options of Eclipse and so on can help, but these are generally less than ideal.)

Using this `.vimrc`{.backtick} (or `_vimrc`{.backtick} on Windows), except for writing this, I\'ve hardly thought about this indentation issue for over a decade:

    set tabstop:4
    set shiftwidth:4
    set et
    set autoindent
    set wrap
    set textwidth=72
    syn on

Some other vim tricks/settings I don\'t want to lose track of:

- `cd %:p:h`{.backtick} Make it so you can edit files in cwd w/ `:e filename`{.backtick}

- `/pattern\c`{.backtick} Case insensitve search

  - see also `:set smartcase`{.backtick} [http://stackoverflow.com/questions/2287440/how-to-do-case-insensitive-search-in-vim](http://stackoverflow.com/questions/2287440/how-to-do-case-insensitive-search-in-vim)

- [http://vim.wikia.com/wiki/Count_number_of_matches_of_a_pattern](http://vim.wikia.com/wiki/Count_number_of_matches_of_a_pattern)

- [http://vim.wikia.com/wiki/Search_patterns](http://vim.wikia.com/wiki/Search_patterns)

- [http://stackoverflow.com/questions/3997078/how-to-paste-yanked-text-into-vim-command-line](http://stackoverflow.com/questions/3997078/how-to-paste-yanked-text-into-vim-command-line)

- problem: You open a file but the line endings are all jacked up (e.g., you see a bunch of `^M`{.backtick} embedded in your file). You can check what fileformat (ff) mode you are in with: `:set ff?`{.backtick} You can re-edit the file, telling it what mode you want to be in. For example, Mac uses CR (\^M) only, but you are opening files by default in dos mode.

<!-- -->

        :e ++ff=mac

- see [http://vim.wikia.com/wiki/File_format](http://vim.wikia.com/wiki/File_format)

## Other Stuff 

I recently had an opportunity to see [Joel Spolsky](https://en.wikipedia.org/wiki/Joel_Spolsky) speak, live in Albuquerque. I had heard the name. He\'s the CEO of Stack Exchange (Stack Overflow), as well as some other things, most notably [http://www.joelonsoftware.com/](http://www.joelonsoftware.com/). So, I went to have a look at his blog, and here is the first thing I pulled up: [http://www.joelonsoftware.com/articles/fog0000000069.html](http://www.joelonsoftware.com/articles/fog0000000069.html)

It was very apropo at the time. Still, good advice.

## Oracle SQLDeveloper (Java DB client) 

You can turn on line numbers like this:

- Tools -\> Preferences

- Left panel, open: Code Editor

- Select \"Line Gutter\"

- Check \"Show Line Numbers\" (at top)

------------------------------------------------------------------------

[CategoryHomepage](CategoryHomepage)
