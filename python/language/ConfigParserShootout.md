# ConfigParserShootout

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

In 2004 there was a debate about [ConfigParser](http://python.org/doc/current/lib/module-ConfigParser.html) on the Python mailing lists. But since that initial discussion there hasn\'t been any strong push to resolve the situation. For more, see these threads:

- [ConfigParser patches](http://mail.python.org/pipermail/python-dev/2004-October/049167.html)

- [ConfigParser shootout, preliminary entry; comp.lang.python](http://groups.google.com/groups?hl=en&lr=&c2coff=1&selm=mailman.5093.1098051158.5135.python-list%40python.org)

- [ConfigParser shootout, preliminary entry; python-dev](http://mail.python.org/pipermail/python-dev/2004-October/049454.html)

- [What are the goals for ConfigParser 3000?](http://mail.python.org/pipermail/python-dev/2004-October/049527.html)

This page serves as a place to record alternatives, and discuss (in a semi-permanent way) the features such a library might have. A new configuration parsing library could go into the Python standard library, probably in addition to the current [ConfigParser](ConfigParser) module (perhaps with that module being deprecated).

See the \"Status of Shootout\" section (from about 2006) for a summary of the major period of discussion which lasted on the order of a year.

## Goals 

Discussion of people\'s goals for revising [ConfigParser](ConfigParser) have been broken out to the page [ConfigParserGoals](ConfigParserGoals): what is [ConfigParser](ConfigParser) really for?

Also note that there has been some confusion between \"In memory storage of configuration data\" and \"Simple persistent storage of configuration data\". Part of the problem is that almost every configuration storage system (including [ConfigParser](ConfigParser), optparse, and getopt) comes with its own in-memory API. There should be some uniform means of accessing data from configuration files and command line options parsed via optparse or getopt, including the ability to override options in configuration files with command line options. Ideally, the programmer API should not normally care whether an option was set in the configuration or the command line.

## Implementations 

Please list interesting implementations of config parsers here.

### ConfigObj 4 

[ConfigObj - A simple to use config file parser](http://www.voidspace.org.uk/python/configobj.html)

This is now a very powerful config file parser that addresses many of the issues raised here.

As of version 4 it reads and writes sections nested to \*any\* depth. It uses square brackets round section markers to denote nesting. this means it is compatible with most files written for [ConfigParser](ConfigParser) : ::

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

[ConfigObj](../people/ConfigObj) also has a feature I \*think\* is unique - in the shape of a tightly integrated type checking/conversion system. This is (allegedly) substantially simpler than the type system of ZConfig and \*doesn\'t\* involve storing type info in the config file.

The type specification is kept in a separate schema (which has a simple key = checkname(parameters) syntax and also allows for default values. The validation process checks that the config file matches the schema and fills in any default values. It also converts all values that pass into the required type.

This means a [ConfigObj](../people/ConfigObj) is an abstraction of \*config data\* - not just the config file, at no cost to the \*user\*. The validation system is simple and extendable.

### M. Chermside\'s candidate 

[code](http://www.mcherm.com/publish/2004-10-17/config.py) and [test cases](http://www.mcherm.com/publish/2004-10-17/configTest.py). Currently allows files in either str or unicode, with sensible defaults. Allows dictionary or dotted-name access (though dotted-name can fail in some cases). Allows subsections of arbitrary length. For example,

        x.y = True
        x.y.z = 47
        x.y.a = prime

Would allow x.y to be viewed as either a value (\"True\") or a section.

        x.y == "True"

but also

        x.y['a'] = 'prime'
        x.y['z'] = '47'

Note that keys and values are always strings or unicode \-- no autoconversion to other types. Note that this focuses on storage and API \-- reading and writing is left out at the moment, and might reasonably be in a separate module for each format supported.

### INITools 

[INITools](http://pythonpaste.org/initools/) is factored into a parser that conforms to the [ConfigParser](ConfigParser) sense of what an INI file is (`initools.iniparser`), and a couple of implementations based on that. One of those implementations is `initools.configparser`, which is compatible with the standard library [ConfigParser](ConfigParser).

It includes several features that can normally be built on to [ConfigParser](ConfigParser), but enables these through simple class variables per feature. These include features like:

- Percent or dollar substitution (dollar substitution is like what zc.buildout uses)
- Options outside of a section (i.e., leading options before any section is defined)
- A different name for the global section besides DEFAULT
- Case insensitivity without case folding (i.e., preserves case)
- Some unicode handling
- Can be written out preserving comments and ordering
- Allow an extend option, similar to what zc.buildout uses
- You can turn off the behavior where file not found is ignored
- There\'s a method to get the filename and line number where an option was read from

Because it preserves all the information from the file you could write a view on top of this structure, to present any reasonable API \-- the [ConfigParser](ConfigParser) API is awkward, but given a few additions it is at least a reasonably complete description.

### Skip\'s Idea 

In my use of INI files I\'ve always been annoyed that I couldn\'t nest sections to an arbitrary depth and had to resort to baroque XML APIs to accomplish that sort of task. I also figured a structure defined by indentation would be a good way to go, though YAML always seemed too complex. I worked up a little [config file parser](https://github.com/smontanaro/python-bits/blob/master/cfgparse.py) that reads and writes files like

    empty section1:
    level1 = new val
    section1:
    # this is a comment for section1.item1:
        item1 = item 1
              # this is another comment
        subsection:
            item2 = item 2
    section2:
       subsection:
           item3 = item 3
    very last = 7

### Dan Gass\' 

I\'ve just released a new configuration parser ([http://cfgparse.sourceforge.net/](http://cfgparse.sourceforge.net/)). It has many of the features outlined as desireable:

- Simple ini style configuration syntax
- Type checking with error handling and help messages
- Help summary modelled after that in optparse
- Round trip - read, modify, write configuration files with comment retention
- Cooperates with optparse for configuration file options that should be overridden by command line options
- Supports heirarchically organized option settings
  - User may store multiple option settings in a arbitrarily deep keyed dictionary.
  - Application uses a key list to walk into the dictionary to obtain a setting.
  - User controls key list with setting in configuration file.
  - Supports adding keys to the list through a command line option or from environment variables.
- Supports allowing user control of configuration files used.
  - Environment variables may be used to allow user to specify a default configuration file.
  - Command line options to specify configuration file supported.
  - Configuration files may include other configuration files where sections are read in parallel.
  - Configuration files may be nested heirarchically by including configuration files from within a section or subsection.
- Configuration files may alternatively be written in Python.
  - full power and flexibility of Python available for creation of option settings
  - allows options settings to be real Python objects
  - this feature is NOT enabled by default
- May be extended to support syntax such as XML.

The documentation is complete and is available in HTML and PDF. The home page ([http://cfgparse.sourceforge.net/](http://cfgparse.sourceforge.net/)) is the HTML version online. The documentation and the module functionality is quite complete and useful as it is. But I am looking forward to feedback so that it may be improved. The distribution contains the module, help documentation (including source) and a fairly extensive test suite (you\'ll need Python2.4 to run the tests).

I figure I will make an announcement after any dust settles from this posting. By the way, I apologize for using the same name (cfgparse) as another entry but since this is modelled after optparse, that was the most logical choice.

Enjoy, Dan Gass \-- [dan.gass@gmail.com](mailto:dan.gass@gmail.com)

### Vinay Sajip\'s implementation 

The [config](http://www.red-dove.com/python_config.html) module allows a hierarchical configuration scheme with support for mappings and sequences, cross-references between one part of the configuration and another, the ability to flexibly access real Python objects without full-blown eval(), an include facility, simple expression evaluation and the ability to change, save, cascade and merge configurations. It has been developed on python 2.3 but should work on version 2.2 or greater.

A simple example - with the example configuration file:

    messages:
    [
      {
        stream : `sys.stderr`
        message: 'Welcome'
        name: 'Harry'
      }
      {
        stream : `sys.stdout`
        message: 'Welkom'
        name: 'Ruud'
      }
      {
        stream : $messages[0].stream
        message: 'Bienvenue'
        name: Yves
      }
    ]

a program to read the configuration would be::

    from config import Config

    f = file('simple.cfg')
    cfg = Config(f)
    for m in cfg.messages:
        s = '%s, %s' % (m.message, m.name)
        try:
            print >> m.stream, s
        except IOError, e:
            print e

which, when run, would yield the console output::

    Welcome, Harry
    Welkom, Ruud
    Bienvenue, Yves

One problem I have with this implementation is the configuration file syntax. I respect the need for a syntax to handle dictionaries and lists but why invent yet another language? If one wants a Python like syntax make it the Python syntax. I don\'t think everyone is on board with a Python syntax for configuration files though. My biggest concern is to have a syntax that supports heirarchies and being able to construct Python objects for configuration settings. I lean toward using Python as the syntax (and even the parser) because of the flexibility offered but if there was another way that makes sense I\'m ok with that. \-- [dan.gass@gmail.com](mailto:dan.gass@gmail.com)

My reasons for not using Python itself for the syntax and parser are:

1.  I couldn\'t see how to just parse the required subset of Python - lists and dicts - while preventing arbitrary code from being executed.
2.  I wanted to be more forgiving of missing commas.
3.  I wanted to allow easy cross-referencing, inclusion and evaluation, using a more compact notation, which precludes the use of standard Python.

If someone could show me a way to meet the above desires whilst using Python syntax and parser, I\'ll gladly revisit the issue. \-- [VinaySajip](../people/VinaySajip)

### cfgparse

[cfgparse](http://www.cs.wisc.edu/~param/software/cfgparse/) - cfgparse is a Python module that provides mechanisms for managing configuration information. It is backward compatible with [ConfigParser](ConfigParser), in addition to having the following features:

- Preserves structure of INI files: Order of sections & options, indentation (to some extent), comments, and blank lines are preserved when data is updated.

- More convenient than [ConfigParser](ConfigParser): Values can be accessed using dotted notation, or using container syntax (cfg\[key\]).

- Backward compatibility: Backward compatible implementations of [ConfigParser](ConfigParser), [RawConfigParser](./RawConfigParser.html), and [SafeConfigParser](./SafeConfigParser.html) are included that are API-compatible with the Python standard library. They pass all the unit tests in Python-2.3.4.

- Extensible: It is possible to add other configuration formats, and to convert between different formats (as long as the data models are compatible).

### ZConfig 

[ZConfig](http://www.zope.org/Members/fdrake/zconfig/) - This Python package is a bit larger than some of the others, but provides for schema-based development of configuration structures. The schema language uses XML, but the configuration language is more like Apache\'s. Sections are typed and completely nestable. The basic implementation does have some limitations that are tedious to work around if you run into them. One that can bite quickly is that names in the configuration language are case-insensitive by default; for versions before 2.3.1 this was terribly difficult to work around without copying lots of code, and even with 2.3.1 it takes more than it should.

### tconfpy

OK, I\'ll Toss My Hat Into The Ring. I just found this discussion tonight for the first time. A fascinating topic and one very much dear to my heart. So much so that, ahem, uh, \... [http://www.tundraware.com/Software/tconfpy](http://www.tundraware.com/Software/tconfpy)

### configparse

[configparse](http://www.gustaebel.de/lars/configparse/) is an extension that is built on top of the command line parsing library optparse. It provides the same interface and is intended to be uses as a drop-in-replacement for optparse. configparse is very limited in its abilities, there\'s no support for sections, recursiveness or sophisticated value checking etc. Its advantage is that it takes only a few modifications to existing code to add simple support for config files which can be quite handy sometimes.

### plistlib

[plistlib](http://svn.red-bean.com/pyobjc/branches/branch_1_0/pyobjc/MPCompat/plistlib.py) plistlib is a small module for generating and parsing Mac OS X .plist files. It supports:

- lists
- dictionaries
- arbitrary nesting
- bool, int, float, string and date types

As the default config format on OS X, plist files are already used by hundreds of apps. Though popular on the Mac, the format can be used from any platform or language since it\'s a [subset of XML](http://developer.apple.com/documentation/MacOSX/Conceptual/BPRuntimeConfig/Articles/ConfigFiles.html). Graphical editors are available from Apple as part of its free developer tools, as well as from [third party developers](http://homepage.mac.com/bwebster/plisteditpro.html)

### PyOptionTree 

[PyOptionTree](http://pyoptiontree.sourceforge.net) is a hierarchical parameter parser that I wrote with the goal being to allow the user to both specify parameters \*and\* modify, control, structure, copy, and record them in a efficient and intuitive way. I\'ve been using and refining it for over a year, and it has many of the options that people seem to find desirable, plus a few more, so I thought it\'d be worthwhile to post here. If people have any comments, please let me know.

It supports:

- Lists, tuples, and dictionaries (through dict() and list of 2-tuples). Also supports nesting lists and tuples.
- Embedded python code.
- Linking options (even forward linking) using a directory-like syntax.
- A useful set of functions for importing additional files, loading pickles to be the value of objects, string operations, summation, concatenation, etc.
- Allowing for program-defined functions that can be passed to the parser.
- Inheritance and a more object oriented feel through by allowing branches to be copied and modified.
- Saving the tree in the same format. The saving preserves the original order of nodes.
- Allowing the programmer to modify the tree \-- even inserting arbitrary pickleable objects \-- and save it in the same format.
- Parse and incorporating command line arguments.

Here\'s a simple example:

    Tasks = [exercises/jog, eating/eatcereal, eating/eattoast]   # links to the following subtrees

    exercises = {
      jog = {
        action = "jog"
        minutes = 30
      }
      # etc.
    }

    eating = {
      eatcereal = {
        action = "eat"
        food = "cereal"
      }
      
      eattoast = copy(eatcereal)  # this creates a copy of the eatcereal subtree
      eattoast/food = "toast"     # this changed the food option of that copy
    }

On the programmer\'s end, each of the braches behaves like a full tree, e.g.:

    def runTests(opttreefile):
        ot = PyOptionTree(opttreefile)
        for t in ot('Tasks'):   # According to the above definition,
            runTest(t)         # t is a subtree (branch).

    def runTest(ot):
        print 'Current Action: ', ot("name")

### configparser2

A slightly cleaned up version of the original [ConfigParser](ConfigParser) [here](http://code.google.com/p/configparser2/source/browse/trunk/configparser.py?spec=svn2&r=2).

## Features 

This is a list of features that should be taken into account. Certainly not all these features are required; maybe some aren\'t even desired.

- Uses a human-editable source file format. Everyone seems fairly happy with INI files as a basis, but

  [ZCML](http://cvs.zope.org/Zope3/doc/zcml/) is an example of a different syntax.

- Has a simple API, especially for the simplest case (read a bunch of key-value string pairs from a file).

- Can be round-tripped, i.e. a program can modify the configuration, then write the new configuration out.
  - Bonus if you can keep comments intact when writing the file. Or at least keep track of the comments in some way, so it can be extended by someone else later (throwing away comments entirely puts up brick walls).
  - Keeps track of the order of items in the configuration file.
  - Is intelligent about default values; writes out a minimal config file.

- Supports some notion of a config schema. You might define a certain key as being an integer, and it would be automatically converted when the file was loaded. This becomes a bit more difficult when you have more complex structures, multiple sections, etc. Defaults fit in here as well. Obviously the types available should not be fixed.

- Supports repeating values in some fashion. Maybe a key can appear multiple times in the file. Maybe nested structures are allowed otherwise. Repeating values are common.

- Allows multiple config files to be combined, e.g., a site config, user config, custom config. Consideration should be given to repeating values; sometimes a user config file may want to add to a site config without repeating all items in the site config.

- Allows dynamic nesting. E.g., some configuration values may be modified only in a small context, or for a single request in a long-running server. The nesting needs to be undone later. Maybe this simply requires the config to be easily copiable (i.e., copy the config, modify that copy, throw it away when you are done); maybe something more sophisticated is possible.

- Supports multiple syntaxes; e.g., an XML plist syntax, an INI syntax, a ZCML syntax.

- Gives good error messages. Error messages should include file and line number. If we define types in a schema, invalid values should give good errors.

- Supports (maybe through utility functions or otherwise) more advanced configuration directives, like including other files or string

  interpolation. But a lot of people don\'t like [ConfigParser](ConfigParser)\'s current string interpolation.

- Consider the general case of configuration settings, not just config.ini. While round-trip to human readable is important, it is also important that the in-memory version play well with other ways of setting parameters \-- including some that set arbitrary python objects.

To be more explicit, it should work well with at least optparse (Optik), .ini files, .xml files, and computed-at-runtime values. The interface to the various storage mechanisms can be different, but developers shouldn\'t have to repeat information across the various formats; adding an option (and default value/help message/restrictions) should only need to be done once.

- Backward compatible; at least to Python 2.2, best if portable to Python 2.1.
- Implements a true parser that can be subclassed and specialized. If it only has a method that parses the config file into a dictionary, then any attempts to extend or specialize the parser won\'t have access to line information. The parser need not be a high-profile part of the module, so long as it is available.

## Discussion 

Discuss. Please sign your name.

What exactly is the goal? A new API to access configuration info? Or a specific file format itself? Or both? I don\'t have much problem with the current [ConfigParser](ConfigParser) but ideally I would like use a \'simpler\' API. This would allow attribute access (a.b.c) to values, provide default values, convert some types, and do some constraint checking (xyz is required) etc. It\'s very possible to get this functionality through a wrapper on top of [ConfigParser](ConfigParser). IMO that is the best approach, as long as there is a way to map the same API over a different underlying file format, such as XML. I think the \'dynamic nesting\' point above is outside the scope of the config access API. \-- Shalabh

Three features I want in a config parser are 1) keyed settings 2) pulling in settings from multiple configurition files, and 3) ability for user to pass in real python objects through the settings. The \"keyed\" settings can be thought of as namespaces and I need an arbitrary number of key nestings. For certain applications I EXPECT the user to pass in python objects that meet a specified API. This allows the user to customize a certain operation however they would like with the full power and flexibility of python. I then don\'t need my tool to be tailered with a switch statement having custom solutions for each user type. This would require the configuration file (or parts of it) to be able to be executed as a python script and I realize this is a security hole that would be unacceptable to many. What I would propose is the config parser module support two methodologies, both sharing the same API and configuration file syntax. One would parse the config file and prevent security issues, the other would either execute the whole config file or be a combination parse/execute but would support attaching real python objects to configuration settings. These features have been implemented in a configuration parser [https://sourceforge.net/projects/cfgparse/](https://sourceforge.net/projects/cfgparse/) (needs python 2.3 unless the use of the textwrap module is removed) and is available for experimentation/use. \-- [dan.gass@gmail.com](mailto:dan.gass@gmail.com)

I think it is reasonable to ask the setting code to create the object (possibly by running a random string); the config system just needs to accept objects that have already been made. A round-trip is useful, but I\'m not sure source code is the best way to do that; editing will probably require an external tool anyhow. Maybe just use pickle to save arbitrary objects? (And avoid storing them \*within\* the config, as much as possible.) \-- Jim J Jewett

### ConfigParser, optparse Marriage 

A marriage of the two would make a lot of sense to me. My thought is for the user (script) to instantiate a parser and add options to it much like optparse does today. When the parser processes the command line args (or args passed to it) it should also look at the configuration file (possibly using the long setting name) for the option settings. Its first priority would be command line args.

- I don\'t believe that a configuration module should need to interface directly to command line options. Rather, an application should inspect command line arguments, select one or more configuration files to load, and then examine the configuration data together with command line options to determine behaviour. My [config module documentation](http://www.red-dove.com/python_config.html#integrating-with-command-line-options) shows one way to easily interface with optparse. \-- [VinaySajip](../people/VinaySajip) An easy way, maybe, but it doesn\'t seem very useful to me. What\'s the advantage of fetching a command-line option from cfg.cmdline_values.verbose instead of options.verbose? Also, we need to specify every option twice, once for optparse and once in the configuration file itself. For docutils, this would mean every config file would have 40(!) lines which are, essentially, implementation details.

  - It was only an example, and I accept it may not be the best example to showcase the functionality. Consider this, though: you can use a [ConfigList](./ConfigList.html) to cascade configurations. If one of these is a set of options picked up from the command line, and another is from configuration files, then you can easily in your application just get e.g. \'cfglist.verbosity\' which is picked from a command line option (if defined) or from the configuration file (otherwise). There\'s no need to define things twice, other than to define what happens when command line options are not provided. I\'ll work with you, if you like, to see how docutils configuration can be achieved using the module. See the example for verbosity below - you\'ll see that you don\'t necessarily need to specify things twice, and can access values from either command line or configuration transparently. \-- [VinaySajip](../people/VinaySajip)

  These are probably fixable, but I think they exist because you\'re not solving the interesting part of optparse integration: every application still has to merge the command-line options with the options from the configuration file manually. I just grepped through my \'src\' directory and found shtoom, docutils, roundup, logilab-common and spambayes all have modules which allow them to specify options only once. IPython, offlineimap, and trac are still merging without the aid of such a module.

  - The work required to merge can be as simple as setting up a [ConfigList](./ConfigList.html) with a command-line-based configuration object first in the list, followed by one or more configurations read from files. Thereafter, the application resolves configuration data by asking the [ConfigList](./ConfigList.html). If a configuration item has been referenced in the command line, that value is returned; otherwise, a value defined in a configuration file is returned. You could even have e.g. project, user and application level configuration files, though there is no need for such complexity in most cases, and the API remains IMO fairly lean. \-- [VinaySajip](../people/VinaySajip)

  Given that this is a problem which is being solved again and again, maybe the Python library should be providing mechanism \*and\* policy here. I don\'t think it would be too hard to draw up a reasonable default.

  \-- [JohannesGijsbers](../people/JohannesGijsbers)

  I whole heartedly agree with Johannes\' comments. In my scripts I have no interest in knowing whether the setting came from the command line or from a configuration file. It just adds complexity to the script and the explanation how to use it to even allow the use of such knowledge. I don\'t know if I understood the [ConfigList](./ConfigList.html) approach completely but it seems to me it adds an unnecessary layer and complexity. If we were to go down the road of a marriage I believe it would be one of three possibilities 1) add functionality to optparse 2) subclass optparse or 3) make a new module independent of optparse that duplicates alot of its functionality. I think we would need the input from the optparse implementors to help with the decision as the first option would require a great deal of work for them and the second option would require a commitment by them to an interface between us. The third wouldn\'t require any work but they may want to be involved. \-- [dan.gass@gmail.com](mailto:dan.gass@gmail.com)

  I feel that the option \"4) provide a mechanism for using optparse as is\", as I have proposed, warrants further study because it lacks the drawbacks you have identified with the other 3 options. I\'ll try to address your concerns about how to make configuration-with-command-line-override work easily using the config module. As a first cut, I\'ll aim for a simple example of a \"verbose\" flag which can be placed in a configuration and overridden via a command-line option. If you think that\'s too simple as a proof of how it can work, please indicate a use case you\'d like to see. Otherwise, below is the \'verbose\' example: \-- [VinaySajip](../people/VinaySajip)

Assume that the config file is simply

    #This file is config.cfg
    verbose : False

and suppose you want to be able to override this using the command line. One possible program is:

    #This is test.py
    from config import Config, ConfigList
    from optparse import OptionParser

    def getMergedConfig(filename):
        optcfg = Config()
        filecfg = Config(filename)
        parser = OptionParser()
        parser.add_option('-v', '--verbose', action='store_true', dest='verbose', help='Produce verbose output')
        args = parser.parse_args(None, optcfg)[1]
        cfglist = ConfigList()
        cfglist.append(optcfg)
        cfglist.append(filecfg)
        return cfglist, args

    def main():
        cfg, args = getMergedConfig('config.cfg')

        print "verbose output? %r" % cfg.getByPath('verbose')
        print "args: %s" % args

    main()

If you run this with

    python test.py an_arg

the output is

    verbose output? False
    args: ['an_arg']

whereas if you run this with

    python test.py -v an_arg

the output is

    verbose output? True
    args: ['an_arg']

This admittedly simple example points to how simple the actual application code - i.e. main() could be. I\'m assuming that getMergedConfig() is a utility function which could be shared across multiple scripts, but even so it is pretty simple, in my view. Notice that main() does not know where the configured value of \'verbose\' came from.

To forestall the complaint that the optparse specification appears to require some duplication, you could change the config file to:

    #This file is config.cfg
    verbose : False
    optparse:
    [
      { name: verbose, short: '-v', long: '--verbose', action: 'store_true', default: None, help: 'Produce verbose output'}
    ]

and the code which sets the parser options to (indent appropriately):

    for optspec in filecfg.optparse:
        parser.add_option(optspec.short, optspec.long, action=optspec.action, dest=optspec.name, help=optspec.help)

Remember, this is just one way of doing it - not the only way and perhaps not the best way for your needs, but a simple enough way.

\-- [VinaySajip](../people/VinaySajip)

A hierarchical "key" or "namespace" scheme should exist so that multiple settings may be stored in the user configuration file. I would propose a standard -k, --key option always present in the parser so the user can pass a list of keys to control the group of settings to use (I'd also like some of the other ways to control keys that I use in my config.py module). In addition I'd propose a -c, --config option that specifies a configuration file to use instead of the user's default configuration file.

- I ([VinaySajip](../people/VinaySajip)) agree that a hierarchical namespace is essential. I\'m not sure I agree with removing \"-k\" and \"-c\" from the command line namespace for all applications by reserving these for use by particular library modules.

  Along the lines of Johannes\' comment regarding \"providing a mechanism \*and\* policy\" (which I agree with), I think having a consistent command line option such as -k and -c is important. I don\'t really care what specifically they are, even if we required the use of long form \--keys and \--config (change the names if you like). So long as policy is set I\'m happy. \-- [dan.gass@gmail.com](mailto:dan.gass@gmail.com)

  I\'m not sure about the policy part, because people have different needs and I\'m not sure it\'s good to be too prescriptive here. \-- [VinaySajip](../people/VinaySajip)

My last proposal for today is to change the "options" interface a bit from optparse. Instead of returning a static object of options it should be an object with a get() method so that additional keys can be used to get at settings in the configuration "on the fly". One application where this is important is in test frameworks. "Test specification" input files may have additional "keys" to be used and aren't known when the parser is instantiated.

- Please take a look at [this config module](http://www.red-dove.com/python_config.html) and let me know how you think it fails to meet the particular use case you have in mind. I don\'t see any need to change optparse to work well with a configuration module \-- [VinaySajip](../people/VinaySajip)

  I looked and here is where it falls short from my perspecitve. To get a setting using your module you would use \"cfg.setting\". Instead a method should be offered so that keys may be passed \"cfg.setting.get(\'key1\')\". Sometimes a script needs more than one instance of the setting. Other times the script processes an input file (after the configuration has already been read) which specifies the key. I\'m sure there are other cases as well. \-- [dan.gass@gmail.com](mailto:dan.gass@gmail.com) I don\'t think this is a real showstopper. To get a setting using my module you can use cfg.setting, cfg\[\'setting\'\] or even cfg.getByPath(\'setting\'). The last of these is useful when you have a hierarchical path which you compute, as in:

<!-- -->

    path = sys.platform + ".database.connection"
    connstr = cfg.getByPath(path)

- I\'m assuming the config file could have a database connection setting for each platform, in the above example. If this is not what you meant by \'more than one instance of the setting\', please clarify.

  \-- [VinaySajip](../people/VinaySajip)

One benefit of this marriage is that the help messages available from the command line would also apply to what can be set in the configuration file. Also there is a lot of flexibility for the user with this scheme. For options they always use they can hard code them in their default configuration as settings. If they want to temporarily override them they can use command line options. For groups of settings that are always used together, they can be used by simply passing in a key with the -k option to select the group.

- There are other ways in which help messages for configuration can be implemented. For example, with full hierarchical name support for configuration items, you could locate help for a configuration item in the configuration item itself - e.g. help on \"a.config.item\" might be found at \"help.a.config.item\". This approach can be used to store other meta-information, not just help text. \-- [VinaySajip](../people/VinaySajip)

  It\'s my preference to have the application control the help like optparse does. IMO its better to have that information close to where the parser is being set up and not have to have or go to another file for that information. \-- [dan.gass@gmail.com](mailto:dan.gass@gmail.com)

  Well, you\'re not being \*forced\* to use any particular idiom. Want to hardcode the information in the program? No problem. Want to have it in the file? That\'s fine, too. Want to use gettext for internationalization? That\'s also quite easy. \-- [VinaySajip](../people/VinaySajip)

The part that isn't addressed here that bothers me yet is how to weave in the ability to pass in real python objects as settings. It would be good to have both a secure (restricted to strings and simple settings) and a second less than secure parser for those applications that need the flexibility of python. I'd like to see the API's of the same for both the parser and the configuration file. \-- [dan.gass@gmail.com](mailto:dan.gass@gmail.com)

- I ([VinaySajip](../people/VinaySajip)) believe that I have covered this in [this config module](http://www.red-dove.com/python_config.html) - if you feel something fundamental is missing, please let me know.

  When I use python to set up objects to pass in as settings I often use multiple lines of code to do it. Sometimes I need to import modules so that I can instantiate a class. Other times I\'m using the os module to figure out where the configuration file is located because I need the path information to figure out the absolute paths of other things that are located relative to it. Don\'t change yours on my account I\'m holding tight with mine until a new and improved standard is available (so long as it works for me). Who is concerned about the security hole of executing Python and what restrictions do they want? \-- [dan.gass@gmail.com](mailto:dan.gass@gmail.com)

  Well, I do have this concern - not so much for a security hole in the sense of bad guys in black hats, but the possibility of end users editing configuration files with executable code isn\'t in my view a recipe for robust software which behaves predictably. I don\'t fancy those support headaches , thanks. \-- [VinaySajip](../people/VinaySajip)

### Extension to configuration editing 

The configuration parsers mentioned so far may handle textual configuration files and maybe extensions into options parsing, but there is a need sometimes to graphically change options . Maybe an amalgamation of the above ideas with the traits package of scipy [http://old.scipy.org/site_content/traits](http://old.scipy.org/site_content/traits) would allow options to be set in all three places - command line, GUI and options file.

- \-- Donald \'Paddy\' [McCarthy](./McCarthy.html)

My implementation ([http://cfgparse.sourceforge.net/](http://cfgparse.sourceforge.net/)) could be useful for implementing a GUI option editor by using the round trip capability. I\'m sure some of the other parsers would as well. A GUI editor seems so application specific that I don\'t think we would want a GUI editor built into the standard library. \-- [dan.gass@gmail.com](mailto:dan.gass@gmail.com)

### Status of Shootout 

So where are we? The wiki hasn\'t seen much activity since January of 2005. Are any of these on track for 2.5? As strictly a user, most of these seem over-engineered for the standard library (to me anyway). `cfgparse`{.backtick} (dan gass) seemed the most approachable to me. XML, or some new configuration \'language\' in the file is way too much. Keeping to a similar (or even matching) API to optparse is important to me. But where are we? \-- [HunterMatthews](./HunterMatthews.html) (showing up as 82 in the edit log)

[GuidoVanRossum](./GuidoVanRossum.html) has discussed possible changes to [ConfigParser](ConfigParser) in a thread on [python-dev](http://mail.python.org/pipermail/python-dev/2006-January/060138.html). He doesn\'t see a great deal of need to improve on [ConfigParser](ConfigParser). He dislikes \*most\* of the suggestions on this page because he doesn\'t want to see nested sections in configuration files.

His reason for this is that he wants to discourage developers from mixing configuration options with application data more suited to a data persistence format. For this he recommends an XML type solution.

I personally think that complex configuration use cases are reasonably common, and that nested sections is a reasonable requirement. Editing/reading XML is not fun, whether it\'s for configuration \*or\* data persistence. For this reason [ConfigObj](../people/ConfigObj) is listed as an [XML Alternative](http://www.pault.com/xmlalternatives.html).

- I agree that nested configurations may be overkill for non-technical users, but they definitely have a useful place. I don\'t like to use XML everywhere, one notable exception being where interoperability is a factor. Even if a new non-backward-compatible module doesn\'t make it into the standard library, the community would still benefit from a peer review of the available offerings on this page. \-- [VinaySajip](../people/VinaySajip)

That aside, it seems like he wouldn\'t be averse to improvements on [ConfigParser](ConfigParser) in the following ways :

- Round tripping - saving config files in the order they are in the file, possibly preserving comments/whitespace.
- Mapping protocol access, for more convenient use.
- Better way of supplying default values.
- Tracking values from more than one file, and storing which file changes apply to.

\-- [MichaelFoord](../people/MichaelFoord)

I think we have to distinguish between configurations primarily intended for editing by *users* and configurations primarily intended for *programmatic* editing. For example, XML makes a lot of sense as an interchangeable language for systems configurations (e.g., SuSE Linux AutoYaST). But XML is a horrid format for manual editing. The delimiter cruft makes it hard to comprehend for all but the simplest cases.

I also do not understand the allergy to nesting, conditionals, and hierarchical namespaces. I implemented all three of these in [tconfpy](http://www.tundraware.com/Software/tconfpy) precisely because they make the resultant configuration file *simpler* - both to understand by the human reader and to subsequently maintain.

I realize there is always the danger of backing into a configuration language that becomes Turing-complete in its own right, but there is a balance to be struck between utility and simplicity. (One [tconfpy](http://www.tundraware.com/Software/tconfpy) tester kiddingly said I was on my way to a reimplementation of *m4* \<shudder\> ![;)](/wiki/europython/img/smile4.png%20";)") My general view on this tradeoff is that configuration \"languages\" should be more-or-less entirely about lexical replacement and not carry a lot of deep semantics around. There is, of course, some semantic content when you introduce nesting, conditionals, and hierarchical namespaces, but even these really serve just a lexical purpose.

[ConfigParser](ConfigParser) is fine for simple day-to-day configurations but I still think there is room for a more full-featured configuration \"language\". One does not preclude the other.

\-- Tim Daneliuk

------------------------------------------------------------------------

With an eye to \"simple configuration scripts and storing data in a user-friendly way\", Babar K. Zafar worked out his [idea of a safe evaluator](http://www.zafar.se/dump/safe.py).
