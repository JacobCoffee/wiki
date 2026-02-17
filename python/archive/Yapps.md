# Yapps

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[Yapps](http://theory.stanford.edu/~amitp/yapps/) (Yet Another Python Parser System) is an easy to use parser generator that is written in Python and generates Python code. Yapps is simple, is easy to use, and produces human-readable parsers. It is not fast, powerful, or particularly flexible. Yapps is designed to be used when regular expressions are not enough and other parser systems are too much: situations where you may write your own recursive descent parser. Yapps 1 is more like a functional language (concise grammars of the form: when you see A B C, return P), while Yapps 2 is more like an imperative language (more verbose grammars of the form: if/while you see X, do Y). Both are completely free.

Yapps supports attributes in grammar rules. Attributes allow you to pass information from the top level rules down to the lower level rules. For example, you might want to pass a variable lookup table down from a rule for parsing blocks (where variables are declared) down to a rule for evaluating expressions (where variables are looked up).

Something that may also be of interest is that Yapps can use a context-sensitive scanner. For example, if there are tokens `num = '\d+'`{.backtick} and `name = '\w+'`{.backtick}, then there\'s an ambiguity --- `'123'`{.backtick} could match either. In Yapps, the parser drives the scanner, and can tell the scanner what tokens to look for. So if there\'s a context where only names are allowed, then the Yapps scanner would treat `'123'`{.backtick} as a name.

Yapps produces [LL(1)](http://en.wikipedia.org/wiki/LL_parser) analyzers, so it\'s unable to handle left-recursive grammars.

For example, this is a popular non-ambiguous grammar for arithmetical expressions:

    E -> E '+' T  |  T
    T -> T '*' F  |  F
    F -> '(' E ')'  |  digit 

Bison uses LALR so it can handle such grammars. For Yapps, you need to rework it into a right-recursive grammar:

    E -> T E1
    E1 -> '+' T E1  |  \epsilon
    T -> F T1
    T1 -> '*' F T1  |  \epsilon
    F -> '(' E ')'  |  digit 

However, in Yapps, you would write typically use loops instead of recursion:

    E -> T ( '+' T )*
    T -> F ( '*' F )*
    F -> '(' E ')' | digit 

where `*`{.backtick} is used to express repetition of a pattern, just as in regular expressions.

In some cases, a LL(1) grammar is much less readable than a corresponding LALR or LR one. Furthermore, some languages can be expressed by LALR grammars but not by LL(x) grammars.
