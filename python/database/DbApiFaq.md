# DbApiFaq

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

These are the frequently asked questions from the DB-SIG mailing list.

## How do I pass parameters to the cursor.execute method? 

Don\'t use the \'%\' concatenation operator, pass them as a series of extra parameters. For instance

`>>> cursor.execute("SELECT * FROM my_table WHERE my_column = '%s'" % "column_value") `

May do what you want, but more by accident than design. If you change it to;

`>>> cursor.execute("SELECT * FROM my_table WHERE my_column = %s", "column_value") `

Then the DB-API module will make sure your value is correctly escaped and turned into an object appropriate for the database.

![/!\\](/wiki/europython/img/alert.png "/!\") Drivers differ in the way the parameters are passed to .execute();

Some examples of parameter passing:

- a list: `.execute ("... col = ?", ["value"])`

- a tuple: `.execute ("... col = ?", ("value"))`

- variable arguments: `.execute ("... col = ?", "value")`

- a dictionary: `.execute ("... col = :arg", {'arg': "value"})`

- keyword args: `.execute ("... col = :arg", arg = "value")`

![/!\\](/wiki/europython/img/alert.png "/!\") Drivers also differ in the substitution sequence used to denote a parameter. The substitution style can be inspected by reading the `paramstyle` atribute of the module being used:

    >>> print module_name.paramstyle
    'qmark'

Some examples of usage for each `paramstyle`:

- format: `.execute("... WHERE my_column = %s", (value,)) `

- pyformat: `.execute("... WHERE my_column = %(name)s", {"name": value}) `

- qmark: `.execute("... WHERE my_column = ?", (value,)) `

- numeric: `.execute("... WHERE my_column = :1", (value,)) `

- named: `.execute("... WHERE my_column = :name", {"name": value}) `

See the `paramstyle` section (under Module Interface) in the [DB-API 2.0 specification](http://www.python.org/peps/pep-0249.html) for more information.

See also: [DbApiCheatSheet](DbApiCheatSheet) (under construction)

------------------------------------------------------------------------

[CategoryDatabase](./CategoryDatabase.html)
