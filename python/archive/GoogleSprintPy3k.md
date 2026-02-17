# GoogleSprintPy3k

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python 3000 Goals for the Google Sprint 

## The sprint is over 

Thanks to all who participated! Here\'s my blog with the report: [http://www.artima.com/weblogs/viewpost.jsp?thread=173453](http://www.artima.com/weblogs/viewpost.jsp?thread=173453)

Below is the list of Py3k tasks we worked on (or wanted to work on) at the [GoogleSprint](GoogleSprint).

## Suggested Tasks 

(We didn\'t get to these.)

- Make IDLE work \-- there are relative import issues, perhaps others.

- When the I/O library is ready, start unifying str/unicode.

- Put back nb\_ \<true division\> slots (regular and augmented)

- Make map() and filter() iterators and make them stop at the end of the shortest input (like zip()) instead of at the end of the longest input (like itertools?)

- See PEP [3100](http://www.python.org/dev/peps/pep-3100 "PEP") for more ideas

## Claimed Tasks 

- [Py3kConversionTools](Py3kConversionTools): Work on tool to help convert (flag keywords like with/as, removed functions/methods: apply/{}.iter\*/{}.has_key/etc) (Jeremy Hylton)

- Work on the new I/O library (I have much interest in this but need help \-- Guido); you can check [http://sebulba.wikispaces.com/project+iostack+v2](http://sebulba.wikispaces.com/project+iostack+v2) for a reference on what was generally agreed in the py3k list. (Hasan, Charles)

- Unify int/long (Martin von Löwis; see [http://mail.python.org/pipermail/python-3000/2006-August/003046.html](http://mail.python.org/pipermail/python-3000/2006-August/003046.html))

- Implement PEP [3102](http://www.python.org/dev/peps/pep-3102 "PEP") (keyword-only arguments) (Jiwon Seo, Brett C.)

- Rewrite import in Python (Brett Cannon?, Alex Martelli?, Osvaldo Santana)

- Make xrange() support longs; then rename it to range() (see [http://www.python.org/sf/1472639](http://www.python.org/sf/1472639) for all but the supporting-long part) (Neal)

- Remove basestring.find and basestring.rfind, per [PEP 3100](http://www.python.org/dev/peps/pep-3100/) (done, Hasan \-- needs to be reviewed and checked in)

## Finished Tasks 

- Make zip() an iterator (like itertools.izip()) (done; Guido) (Brian too!)

- Clean up comparisons. Remove the ability to order objects where it doesn\'t make sense. (Guido, Alex)

- Fix various unit tests that are currently failing in the p3yk branch (done, various sprinters).

- Rip out the last remains of coerce (done, Neal; need to rename nb_coerce slot)

- Make it so that [hash] can be set to None to declare an unhashable type, and to automatically do this the first time [eq] or [cmp] are overridden but [hash] is not (done, Guido & Alex)

- Rip out reduce() (done, John Reese and Jacques Frechet)

- Kill uses of has_key() in idlelib (done, John R & Jacques F).

- Get rid of all references to file() in favor of open(). (done, Anna)

- Rip out classic classes (done pre-sprint, Guido)
