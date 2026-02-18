# ConfigParserGoals

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

There has been some confusion between \"In memory storage of configuration data\" and \"Simple persistent storage of configuration data\". Part of the problem is that almost every configuration storage system (including [ConfigParser](ConfigParser), optparse, and getopt) comes with its own in-memory API. In memory needs a good programmer API. Persistent needs a good user API, and may not need to reflect the full power of the in-memory. How should we separate these?

I ([VinaySajip](../people/VinaySajip)) think these concerns are to some extent orthogonal. Access to values should be powerful but easy, whether the data comes from a persistent store or not. I presume that\'s what you mean by \'programmer API\'. If by \'Persistent needs a good user API\' you mean \'The file format should be easy to use\', I agree. Or is there some other aspect of \'user API\', other than the file format, which I\'m missing?

Yes. They are orthogonal. But an API that is good for programmers (needed in-memory) is different from one that is good for users (needed for the persistent storage). Part of the problem is that most configuration solutions have tried to do both at once \-- anything that could be represented by the program had to be represented by the text file (and often in exactly the same way), so either the text format got unwieldy, or the configuration options were too limited. \-- JimJJewett

## ConfigParser NG Goals: Competing Concepts 

### Keep It Simple And Useful 

In this target, the existing [ConfigParser](ConfigParser) interface is cleaned up and modernized. Features such as string interpolation should be separated out from the base [ConfigParser](ConfigParser) class, in order to lower the entry level for usage and the overall simplicity of the base class.

Attribute and mapping-like access should not be included, as it teaches the Python beginner a bad habit early on in their programming life. Both are essentially syntactic hacks, attribute access also places unnecessary restrictions on the key item - it must be matched by \[a-zA-Z\_\]\[a-zA-Z0-9\_\]+ (ie. Python identifier).

#### Comments 

There is no single standard library module that I swear at more often than [ConfigParser](ConfigParser). It is beyond disgusting, yet it\'s core functionality is infinitely useful in nearly every small application I write. In none of these applications would a more complex configuration system be used, so adding a \"[ConfigParser2](./ConfigParser2.html)\" in the style of urllib2 (needless complexity) would not benefit me at all. I suspect this is the case for most current users of the [ConfigParser](ConfigParser) module. \-- [DavidWilson](./DavidWilson.html).

#### Pros 

- Beginners: a Python beginner will have an easier time moving from defining his program configuration inline, to having a user-editable external configuration. The simplicity of the implementation would also make a good reference for simple, clean Python.

- This is similar to how the old [ConfigParser](ConfigParser) worked, only better.

- Involves no wheel reinvention, only natural improvement that won\'t ruffle existing users\' feathers. No major extension of the existing [ConfigParser](ConfigParser) concept is involved.

- Functionality: without sacrificing simplicity, we cover 90% or more of the common use cases for the module.

#### Cons 

- Only very simple data storage is supported, although this is sufficient for many common cases.
- Most data validation is left to the end user of the module.
- Multiple data formats are not supported, although this could be seen as a Pro, depending on your point of view.

#### Implementations 

A variety of alternate configuration parsers are linked from the [ConfigParserShootout](ConfigParserShootout) page.

### Rich, Complex Data Storage 

Many programs are built these days by assembling components together, and Python programs are no exception. In general, the designer may choose to expose multiple configuration points, and will benefit if there is one standard way of doing so. From the perspective which views programs as hierarchical constructions of configurable components, it would seem to follow logically that configuration of the components should also be hierarchical in nature. The two-level (section, key) model as exemplified by the present [ConfigParser](ConfigParser) does not offer sufficient power. If it did, why does Windows need a registry? ![;-)](/wiki/europython/img/smile4.png%20";-)")

I\'ve posted a more detailed proposal on the [HierConfig](../libraries/HierConfig) page.

- \-- [VinaySajip](../people/VinaySajip)

#### Pros 

- Needn\'t be harder to use than .ini files.
- Not necessarily verbose like XML.
- Provides much more expressive power than .ini files.

#### Cons 

- Not standard like XML, so people have to spend more time learning it.

- Rich, complex data storage is *already* accomplished in a popular, industrial standard called XML, including schema validation (DTDs). Why, really, reinvent the wheel?

  - Not really a con, since XML is overly verbose for many scenarios. \-- [VinaySajip](../people/VinaySajip)

    - *This is a massive con; XML, despite its verbosity is simple and well understood. [ConfigParser](ConfigParser) ads yet another thing to learn and makes computers harder to use* [DougRansom](../people/DougRansom)

      - I\'m not *against* the use of XML - I just don\'t think it should be *mandatory*. \-- [VinaySajip](../people/VinaySajip)

- Should this not be provided by a different module that supports complex data storage?
  - That\'s what I\'ve suggested - see the [HierConfig](../libraries/HierConfig) page. \-- [VinaySajip](../people/VinaySajip)
