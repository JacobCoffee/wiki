# ASTBasedOptimization

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

The current optimization of Python byte code is based on the byte code. To make the maintenance of the peephole optimizations more maintainable and potentially also more powerful, it would be useful to perform them on the level of the abstract syntax tree. Students interested in this project for the Summer of Code should include an explicit list of the transformations they want to support in their proposal.

*This may not make a great GSoC project, given the existing work in this area on the issue tracker (e.g. [http://bugs.python.org/issue11549](http://bugs.python.org/issue11549)) and the attention it is likely to receive from existing core devs in the coming months \~ncoghlan*

------------------------------------------------------------------------

[CategoryIdeas](CategoryIdeas)
