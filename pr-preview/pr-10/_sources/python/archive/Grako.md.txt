# Grako

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[Grako](https://pypi.python.org/pypi/grako) (for grammar compiler) is a tool that takes grammars in a variation of EBNF as input, and outputs memoizing (Packrat) [PEG](http://en.wikipedia.org/wiki/Parsing_expression_grammar) parsers in Python.

Grako is different from other PEG parser generators in that the generated parsers use Python\'s very efficient exception-handling system to backtrack. Grako generated parsers simply assert what must be parsed; there are no complicated if-then-else sequences for decision making or backtracking.

Requires: 2.7+, 3.3+, PyPy
