# CoreSprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## 1. PyConDC 2004 Core Sprint plan 

Some ideas:

- Complete the implementation of Generator Expressions, SF 872326
- sandbox work:
  - \+ statistics package + Complete Decimal package
- Add more data structures to collections module
- Reduce python\'s start-up time.
- Revisit the cache_attr patch for new-style attribute lookup
- Python bug fixing sprint
- PythonASTSprint \-- finish the new compiler on the ast-branch \-- this should be a top priority because the project has been open for so long.
- Examine optimizations proposed by Neal Norwitz and Michael Hudson
  - \+ Add 2 custom op-codes for CALL_FUNCTION where the number of arguments is known in advance, SF 864059 + Fast frame subclass, SF 876206.
- Add \'diff3\' and \'patch\' to difflib
- Unify doctest\'s two approaches to finding test cases, SF 764504
- Documentation sprint
  - \+ People liked the examples in the docs for unittest, sets, and itertools. Apply that model to other parts of the docs. For instance, the email and logging packages would be a lot easier to use if there were a semi-comprehensive example section in the docs. + document the smtpd module, SF 450803
- Improve the byte code optimizer. Several new transformations can be added after checking for basic blocks and if the jump targets can be fixed up when the total number of bytes changes. Also, the line numbering has to be kept intact during the transformations.
- Update, pare-down, and clean-up Demo and Tools/Scripts
- Guido to practice throwing pies.

Back to [SprintPlan2004](./SprintPlan2004.html)
