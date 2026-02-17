# BeginnerErrorsWithPythonProgramming

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Common Problems Beginners Have 

- The [Alice](http://www.alice.org/) 3D project developed a 3D programming environment for beginners. Originally, they used [Python](Python) but later switched to another language. Two Python-specific issues were found to be problematic for beginners: (1) the case-sensitivity of the language (\"variable1\" is not the same as \"Variable1\"), and (2) integer division (a carryover from the programming language C, 3 / 4 = 0, not 0.75, because the division of integers returns integers). Python 3 changed the latter by introducing an explicit integer division operator, so now 3 / 4 is 0.75 and 3 // 4 = 0. The former is just part of the language. See [interview](http://www.linuxjournal.com/article.php?sid=5028) in Linux Journal and this [dissertation](http://www.alice.org/wp-content/uploads/2017/04/ConwayDissertation.pdf) for more details.

- Indentation is part of the Python syntax, used to let the interpreter know which lines belong to a code block (or \"suite\" as the documentation calls it). Leaving out indentation or using the wrong indentation causes problems. In most of those instances, Python emits an error, but if you forget to indent the last line of a block, for example, the code is not considered part of the block and the difference may result in unrecognized faulty code.

- Forgetting to add a colon (:) at the end of if statements, class declarations, etc.

- Changing lists during iteration. A common example is to loop over a list to check an entry for some condition, which, if met, leads to deleting the entry. This will mess up the iteration. To do this safely, iterate over a copy. With Python 3, this can also happen with dicts, since the `keys`{.backtick}, `values`{.backtick} and `items`{.backtick} method of a dict, often used to generate something to iterate over, actually produce views into the dict, and thus are subject to change if the dict changes.

- Not understanding scoping rules, such as \"is this global or not?\". The classic instance of this is that assigning a value to a name in a function-local scope that is also defined in the global scope will create a new name in the local scope and not change the global name unless the function has explicitly declared that the reference is to be to the global one. Meanwhile only reading from it will access the global one if there was nothing to cause a local version to be created.

- Widely known as the \"No Module named\...\" error, this is an issue all programmers face at some point (sometimes multiple times). This article([The \"No Module Named\" Error](https://coderslegacy.com/python-no-module-named-import-error/)) addresses this issue, going through every possible scenario in which this error occurs and how to avoid running into it again.

- Subtle errors\--which may cause some fairly difficult to follow messages\--happen when built-in type and function names are \"shadowed\" (i.e., redefined). For example, using `str`{.backtick} as a variable name in a scope (i.e., a function or class) will prevent the built-in function of the same name from being usable, producing an error like this: `TypeError: 'str' object is not callable`{.backtick}

- Even for advanced users there are features of the Python language that can cause difficulties. See [PythonWarts](PythonWarts) for resources and observations on such matters. These observations have in part been used to suggest refinements in future Python versions.

- Some [Intermediate Conundrums](./Intermediate(20)Conundrums.html) have been noted with regard to the behavior of some Python features, although these may be outside the scope of beginner problems.

## Comments, Potential Solutions 

- The [PyChecker](http://pychecker.sourceforge.net/) module can alert users to many common errors. There also is a tool called [PyLint](https://www.pylint.org/).

- To see languages that have been used successfully with beginners and children, see Logo, [HyperTalk](./HyperTalk.html) (used in [HyperCard](./HyperCard.html) and [SuperCard](./SuperCard.html)), HTML, [JavaScript](./JavaScript.html), variants of Basic, etc.

- Are students learning python to \"learn to program\" or to develop real applications? Does the IDLE interactive prompt help or hinder either?

## Notes 

This page was moved from the educational wikis at *coedit.net* to here.
