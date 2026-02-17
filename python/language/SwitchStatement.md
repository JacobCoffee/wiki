# SwitchStatement

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Many languages have a SwitchStatement Aka [CaseStatement](./CaseStatement.html). Generally, these languages don\'t have convenient mapping abstractions built in, so a [CaseStatement](./CaseStatement.html) provides a syntatic sugar (as opposed to an abstraction) to help write constructs like

    if(x==3) goto case1;
    if(x==6 || x=7) goto case 2;
    goto default:
     case1: {a();}
     case2: {b();}
     default: { foo; }

as

    switch(x)
    {
      case1: {a();}
      case2: {b();}
      default: {foo;}
    }

over ifs and gotos for mapping between an index and some corresponding code. Gotos aren\'t necessarily bad, but a dictionary that maps a value to code you want to execute is an abstraction that matches the semantics intended for case statements.

Python fortunately has mapping constructs built in, and has not need for a SwitchStatement: Simply use a dictionary to look up the code that corresponds to the case you want to handle for a given index value, and execute it.
