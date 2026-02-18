# ConfigObj

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# ConfigObj 

[ConfigObj 4 Manual and Download](http://www.voidspace.org.uk/python/configobj.html)

This is now a very powerful config file parser - by [MichaelFoord](MichaelFoord) and [NicolaLarosa](./NicolaLarosa.html).

As of version 4 it reads and writes sections nested to \*any\* depth. It uses square brackets round section markers to denote nesting. this means it is compatible with most files written for [ConfigParser](../language/ConfigParser) : ::

        key = value
        key2 = member1, member2, memebr3
        [section name]
            key = value
            key2 = value2
            [[sub-section]]
                key = value
                key2 = value2

Each section is acessed as a dictionary.

It has various features (e.g. list values), and can be initialised from a variety of sources (list of lines, StringIO instance, filename). Because of the straightforward write method it is also very useful for data persistence.

e.g.

        config = ConfigObj()
        config['key'] = value
        config['section'] = {'key': 'value', 'key2': ['val1', 'val2']}
        config.filename = filename
        config.write()

ConfigObj also has a feature I \*think\* is unique - in the shape of a tightly integrated type checking/conversion system. This is (allegedly) substantially simpler than the type system of ZConfig and \*doesn\'t\* involve storing type info in the config file.

The type specification is kept in a separate schema (which has a simple key = checkname(parameters) syntax and also allows for default values. The validation process checks that the config file matches the schema and fills in any default values. It also converts all values that pass into the required type.

This means a ConfigObj is an abstraction of \*config data\* - not just the config file, at no cost to the \*user\*. The validation system is simple and extendable.
