# Programmatic

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Programmatic presentation systems (see [DataRepresentation](DataRepresentation)) use Python program units to produce output for Web application \"screens\" and other purposes. The simplest form of such systems is the traditional \"print to standard output\" technique used in the earliest days of the Web and probably in numerous CGI (Common Gateway Interface) programs to this day:

    print "<table>"
    for item in items:
        print "<tr>"
        print "<th>Name</th>"
        print "<td>%s</td>" % item.name
        print "</tr>"
    print "</table>"

More recent programmatic presentation systems are very likely to employ more sophisticated approaches including the direct inclusion of HTML text within the Python code - a technique reminiscent of various SQL-based environments which embed SQL statements in other programming languages to supposedly reduce the complexity of the resulting source code.
