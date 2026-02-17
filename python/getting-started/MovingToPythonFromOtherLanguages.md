# MovingToPythonFromOtherLanguages

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

If you are already a programmer, Python could be the easiest to learn of all the languages you have encountered. It is pretty typical to learn the Python language while you are writing your first non-trivial Python program, so feel free to skip \"Hello World\" and move right to file administration, GUI programming, and numerical analysis. You may definitely be much farther with Python during your first 3 days than you would be with any other language.

Here is an account of a programmer coming to Python and being extremely productive far sooner than he expected to be.

- [Eric S. Raymond \'Why Python?\'](https://www.linuxjournal.com/article/3882)

Below are the key points to be aware when starting Python. Make sure to visit [LanguageComparisons](LanguageComparisons) page for detailed info about Python differences from particular language.

## Significant Whitespace 

Whitespace and **indents are important**. Python uses whitespace to signify end-of-line and code blocks. This may annoy you at first, but the more you read the code the more you will like it.

## comp.lang.python

Probably your most valuable Python resource, right after python.org. Spot Python luminaries in their native habitat! Don\'t be surprised to have your questions answered by the original programmer or the author of the book open on your desk! The best thing about **comp.lang.python** is how \"newbie-friendly\" the mail group is. You can ask any question and never get a \"RTFM\" thrown back at you.

## Where is Python\'s CPAN? 

See the [Python Package Index (PYPI)](http://www.python.org/pypi), Python\'s centralised database of software. Any developer of Python software packaged using distutils (the built-in packaging system) may easily submit their package information to the index.

Before PYPI, Pythonistas contributed code to [The Vaults of Parnassus](http://www.vex.net/parnassus). Unfortunately, the Vaults are not standardized or automated to the degree that the CPAN is, and the site now appears to be inactive. All hail its many useful years of service.

## Python PEP 8: Style Guide for Python Code 

[Style Guide for Python Code](http://www.python.org/peps/pep-0008.html)

You will read this sooner or later. Why not sooner?

Back when I was learning programming and I was learning C, I made my own personal convention for braces and parentheses, just like every C newbie does. And like every C newbie, I thought my personal convention was right, all other ways of doing it were wrong, and I was willing to fight to the death over it.

Of course the best way to program in any language is to become a member of that language\'s community and follow the community\'s norms. It is initially hard to program in a style that goes against your preferences and prejudices. But the sooner you pick up the community norms, and join the community, the sooner you can take full advantage of all the community\'s resources.

PEP 8 is a style guide written mainly by Guido. Beyond learning stylistic norms, you will also be presented with a style that is very well thought out (like most things in Python). If you follow this guide, you *will* program more **Pythonically**, and you will be more productive with Python.

## Tips for \"Thinking in Python\" 

(The phrase *Thinking in Python* was borrowed from [a book Bruce Eckel was writing](http://www.mindview.net/Books/Python/ThinkingInPython.html) of the same name. The book was not meant for beginners to Python, however. It is the Python equivalent of Bruce Eckel\'s popular *Thinking in C++* and *Thinking in Java*)

- *Thinking in Python* is completely different from *Thinking in C++/Java*. It\'s adapted from Eckel\'s draft for *Thinking in Patterns*, a bit like the [DesignPatternsBook](http://c2.com/cgi/wiki?DesignPatternsBook "Wiki") by the [GangOfFour](http://c2.com/cgi/wiki?GangOfFour "Wiki").

The following was taken from a post in comp.lang.python from Mel Wilson, which I thought well summarized good Python programming style for people coming from other languages. I also added some things I would have appreciated knowing during my first 3 days with Python.

- The docs at python.org are very, very good. Hold onto that wallet, you don\'t need a trip to the bookstore to learn Python!
- Scan the full list of built-in module names early on. Python is advertised as \"batteries included\", so knowledge of the built-in modules could reduce the lines of code by a factor of ten.
- Learn Python slice notation, you will be using it a lot. I have this chart taped to my monitor:

<!-- -->

    Python indexes and slices for a six-element list.
    Indexes enumerate the elements, slices enumerate the spaces between the elements.

    Index from rear:    -6  -5  -4  -3  -2  -1      a=[0,1,2,3,4,5]    a[1:]==[1,2,3,4,5]
    Index from front:    0   1   2   3   4   5      len(a)==6          a[:5]==[0,1,2,3,4]
                       +---+---+---+---+---+---+    a[0]==0            a[:-2]==[0,1,2,3]
                       | a | b | c | d | e | f |    a[5]==5            a[1:2]==[1]
                       +---+---+---+---+---+---+    a[-1]==5           a[1:-1]==[1,2,3,4]
    Slice from front:  :   1   2   3   4   5   :    a[-2]==4
    Slice from rear:   :  -5  -4  -3  -2  -1   :
                                                    b=a[:]
                                                    b==[0,1,2,3,4,5] (shallow copy of a)

- Lose the braces, as you know them, and most of the semicolons, obviously.

- Backslash can be used to allow continuing the program line past a carriage-return, but you almost never have to use it. Python is smart enough to do the right thing when it sees an open bracket, a comma separated list, and a carriage-return.

- Strings are immutable. Whenever you think you have changed a string, remember that you really created a new string.

- Where you would use `<vector T>`{.backtick}, use lists, or tuples, that is \[\] or (). Where you would use `<map T1, T2>`{.backtick}, use dictionaries, that is {} .

- The semantics of iterators is available, but most of the syntax goes away. `for item in alist:`{.backtick} iterates over all the items in alist, one by one .. where `alist`{.backtick} is a sequence, i.e. a list, tuple, or string. To iterate over a sublist, use slices: `for item in alist[1:-1]:`{.backtick} does as above, but omits the first and last items.

- For trickier iterations, read and re-read the Library doc on the topic of general-purpose functions. There are some functions that apply to sequences: map, filter, reduce, zip. that can work wonders. Hidden somewhere under the documentation for sequences there is a description of string methods that you\'ll want to read.

- Hidden under the docs for \'Other Types\' are the descriptions of all the file methods. There are no iostreams per se, but the class method [str] can get some of the effect for your own classes, and there are surely other angles I haven\'t thought of.

- Forget overloading. You can define a function, and call it with anything you want, but if it has to behave differently for different type operands, you have to use the run-time type identification `type`{.backtick} function explicitly within the single definition of the function. Default arguments to functions are just as powerful a tool as in C++. *Actually polymorphism does work as expected, it just doesn\'t require deriving from a base class as in C++ or Java.*

- In class definitions the equivalents of operator methods are covered in a chapter in the Python Language Reference. (Look for the double-underscore methods like `__cmp__`{.backtick}, `__str__`{.backtick}, `__add__`{.backtick}, etc.)

- In C, the gotcha for new users is probably about pointers; they\'re tricky and they can\'t be avoided. The gotchas in Python are situations when you use different references to a single object, thinking you are using different objects. I believe the difference between mutable and immutable objects comes into play. I have no clear answers here .. I still get caught once in a while .. keep your eyes open.

- Read the Tutorial once, skim the Library Reference .. at least the table of contents, then skim the Language Reference and you will probably have encountered everything you need.

- For reference the [Module Index](https://docs.python.org/3/py-modindex.html) of the Python docs are generally sufficient.

## Python Culture 

- [Python Culture (Tim Peters channeling Guido)](http://www.python.org/dev/culture/)

------------------------------------------------------------------------

See also: [LanguageComparisons](LanguageComparisons) [MovingToPythonFromPerl](MovingToPythonFromPerl)
