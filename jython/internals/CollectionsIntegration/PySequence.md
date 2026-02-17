# CollectionsIntegration/PySequence

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Notes/Discussion/Decisions on having `PySequence`{.backtick} implement `java.util.List`{.backtick}\...

### Topics 

- [InitModule](./CollectionsIntegration(2f)PySequence.html#initmodule)

------------------------------------------------------------------------

Topic: `InitModule`{.backtick}\
[ClarkUpdike](ClarkUpdike) Feb 26 2005\
I had originally put in here a detailed anaysis of conflicts between the comments and the source code regarding the `InitModule`{.backtick} interface. The comments seemed to indicate that `PySequence`{.backtick} should implement `InitModule`{.backtick} but couldn\'t because the class was abstract and `PyJavaClass`{.backtick} would try to instatiate it erroneously. But `PyJavaClass`{.backtick} was already correctly using reflection to give an error message in `PyObject __call__(PyObject[] args, String[] keywords)`{.backtick} if an abstract class was passed in. So then I was trying to track down why the `PyList`{.backtick} wasn\'t implementing `ClassDictInit`{.backtick}. It was providing the required static method classDictInit() but it was a do-nothing method and it wasn\'t calling `PySequence.classDictInit()`{.backtick} like the comments said it should. So then I diff\'d the changes from 2.2a to the tip with new style class changes. Apparently, all this changed with new style classes. A case of comments being 2 to 3 generations old.

\<whine\>\
My personal opinion:

- Under-commenting code is bad (only comment the unobvious)
- Over-commented code can also be bad, and potentially leads to\...
- Wrong/Out-Of-Date comments are worst of all

This wasn\'t a case of over-commenting, just a case of not maintaining the comments with the code.

\</whine\>

Of course, if I knew more about the code to begin with, I probably would have figured it out faster. But the comments are supposed to be there help the neophytes, no?
