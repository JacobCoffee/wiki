# PhpPhrasebook

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Comparation of simple tasks in php and python - a guide for php programmers wanting to create python applications

strtolower:

    $x=strtolower('Some String');
    echo $x

In Python you can do:

    x = lower('Some String')
    print x

But remember: everything is an object, including every string.

    x = 'Some String'.lower()
    print x
