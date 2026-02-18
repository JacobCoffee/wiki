# HierConfig

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Many programs are built these days by assembling components together, and Python programs are no exception. In general, the designer may choose to expose multiple configuration points, and will benefit if there is one standard way of doing so. From the perspective which views programs as hierarchical constructions of configurable components, it would seem to follow logically that configuration of the components should also be hierarchical in nature. The two-level (section, key) model as exemplified by the present [ConfigParser](../language/ConfigParser) does not offer sufficient power. If it did, why does Windows need a registry? ![;-)](/wiki/europython/img/smile4.png%20";-)")

I\'ve been thinking about how to improve the configuration of the logging package (which currently uses [ConfigParser](../language/ConfigParser)) and playing with some ideas which may have more general applicability. I\'m posting them here and seeking feedback.

I think a good configuration system should provide the following (in addition to being textual, easy to read and edit):

1.  Allow a hierarchy of configuration information, with no specific limit on the depth of the hierarchy.

2.  Allow inclusion of sub-configurations held in external files, at any point in the hierarchy.

3.  Allow the defining of sequences of items as well as items accessed by key.

4.  Allow attribute style access (cfg.item) as well as dict-style access (cfg\[\'item\'\]).

5.  Allow late-bound references to any point in the hierarchy.

6.  Allow **simple** expression evaluation, but not unrestrained eval()-type functionality.

7.  The ability to specify standard library entities (e.g. sys.stderr or os.sep)

To illustrate these points, two example configuration files are given below. Please forgive the bias towards logging-related configuration. (My excuse is that I\'m thinking about how to make logging configuration easier.)

The first is the application configuration file. It includes the logging configuration file using the notation @\"logging.cfg\".

    app:
    {
      name : MyApplication
      base: '/path/to/app/logs/'
      support_team: myappsupport
      mail_domain: '@my-company.com'
    }
    logging: @"logging.cfg"

The second file contains the logging configuration. It refers to the application configuration through \$app

    root:
    {
      level     : DEBUG
      handlers  : [$handlers.console, $handlers.file, $handlers.email]
    }
    handlers:
    {
      console:  [ StreamHandler, { level : WARNING, stream  : `sys.stderr` } ]
      file:     [ FileHandler, { filename: $app.base + $app.name + '.log', mode : 'a' } ]
      socket:   [ `handlers.SocketHandler`, { host: localhost, port: `handlers.DEFAULT_TCP_LOGGING_PORT`} ]
      nt_eventlog: [`handlers.NTEventLogHandler`, { appname: $app.name, logtype : Application } ]
      email:    [ `handlers.SMTPHandler`,
                  { level: CRITICAL,
                    host: localhost,
                    port: 25,
                    from: $app.name + $app.mail_domain,
                    to: [$app.support_team + $app.mail_domain, 'QA' + $app.mail_domain, 'product_manager' + $app.mail_domain],
                    subject: 'Take cover' } ]
    }
    loggers:
    {
      "input"     : { handlers: [$handlers.socket] }
      "input.xls" : { handlers: [$handlers.nt_eventlog] }
    }

The \$-notation resolves entries when they are required. You can think of it like substitution, which is why the \$ character was selected. The use of specific characters such as \'@\' and \'\$\' is, however, preliminary and can be easily changed if feedback warrants it. You can lay out the file with as much whitespace as you like - indent according to taste.

An implementation module using this format has been released: see the [tutorial](http://www.red-dove.com/python_config.html) and [full API documentation](http://www.red-dove.com/config/index.html). The tutorial covers changing and saving configurations, cascading and merging configurations, and integration with optparse for access to command-line options in the configuration.

You can download the latest implementation from [PyPI](http://www.python.org/pypi?:action=display&name=config) or via the download link on the tutorial page.

\-- [VinaySajip](../people/VinaySajip)

------------------------------------------------------------------------

I ([PeterOtten](./PeterOtten.html)) have tried to translate the above sample configuration into a much simpler format that was recently suggested by [SkipMontanaro](../people/SkipMontanaro).

I think that calculations like building an email address should not be performed in a configfile but are rather the task of the application that uses it. The example has therefore significantly been dumbed down.

    # -*- coding: ascii -*-
    #
    # allows the usual comment style
    #
    loggers:
        root:
            level=DEBUG
            handler=console
            handler=file
            handler=email
        input: 
            handler=socket
        input_xls:
            name=input.xls
            handler=nt_eventlog
            
    handlers:
        console:  
            class=StreamHandler
            level=WARNING
            stream=sys.stderr
        file:     
            class=FileHandler
            filename=myapp.log
            mode=append
        socket:   
            class=SocketHandler
            host=localhost
            port=DEFAULT_TCP_LOGGING_PORT
        nt_eventlog: 
            class=NTEventLogHandler
            appname=MyApplication
            logtype=Application
        email:    
            class=SMTPHandler
            level=CRITICAL
            host=localhost
            port=25
            from=myapp@mydomain.com
            to=support@pythonsolutions.com
            subject=Take cover

I ([VinaySajip](../people/VinaySajip)) like this syntax, except for:

- I don\'t see why we need to (in the above example, under loggers/root) say \"handler=XXX\" three times, rather than using a notation like \"handlers = \[console, file, email\]\".
- It may be restrictive to only allow identifiers as keys.
- It\'s a bit more limiting/verbose, if you only have one or two keys for an entry, to use the indentation approach,as opposed to e.g. { host: localhost, port: 80 } on a single line.

As far as use of expressions in the config file, I am ambivalent, and curious to hear more opinions; sometimes a declarative approach is good. But more than the syntax, I\'m interested in what people think about the semantics: for example, allowing cross-references between config elements (perhaps across multiple files), and the ability to perform restricted \"special\" evaluation of some elements (e.g. `sys.stderr`{.backtick})

------------------------------------------------------------------------

I ([StephenHansen](./StephenHansen.html)) have been evaluating this module and went so far as to plug it into our system to see how it works, and I like it a great deal.

In particular, I prefer the \"python like list\" format for specifying multiple values to using the same name multiple times, or having something like \'handler0=\...\' \'handler1=\...\'. It actually makes the config file less readable by users, I think.

The references are very useful as well, allowing a seperate \'database.cfg\' to be imported and easy that looks like\...

    Server: ourServer
    Database: Devel
    Username: Joe
    Password: ''

In a very \"user-friendly\" format, which is then turned into a proper DSN in our main config file..

    DB:@"database.cfg"

    database:
      { 
        'win32':
           'Driver={SQL Server};Server=' + $DB.Server + 'Database=' + $DB.Database,
        'darwin':
           {'server': $DB.server, 'database': $DB.database' }
      }

\... etc. Especially in our case where we actually check to see if the \"primary config file\" is digitally signed, references and such are great. We get one unified config object in the application code and organize our configuration in whatever user-friendly way we need.

------------------------------------------------------------------------

[ZCML](http://cvs.zope.org/Zope3/doc/zcml/) (unlike .ini files) handles nested input fairly well. The syntax looks a little like an Apache config; though from much of what I\'ve seen, it\'s straight XML. \-- [IanBicking](../people/IanBicking)

- Is there a better link for ZCML than the one above? There appears to be nothing in the form of overview documentation on the Zope site, including dev.zope.org - I did site searches for \"ZCML\" and \"configuration\" and nothing came up which looked immediately useful. I don\'t have a particular problem with ZCML, other than the fact that by dint of being XML, it is fairly verbose; and I would guess (please correct me if I\'m wrong) that it is Zope-centric rather than general-purpose. \-- [VinaySajip](../people/VinaySajip)

Maybe I\'m confusing ZCML and [ZConfig](http://www.zope.org/Members/fdrake/zconfig/); there\'s a ZConfig presentation at [http://zope.org/Members/mcdonc/Presentations/ZConfigPaper](http://zope.org/Members/mcdonc/Presentations/ZConfigPaper) \-- ZCML is much more XML-based, where ZConfig is like an Apache file. ZCML is used for a lot of configuration inside Zope 3, which has a very different idea of what configuration is. (Intended for \"system integrators\" as opposed to \"system administrators\".) I believe both were intended to be usable outside of Zope, but haven\'t been packaged as such (yet).

Another way to deal with nested configurations would be to parse the names. I think one package I\'ve seen does this. So sections are just a sort of \"with\" statement. I.e.:

    loggers.input = nt_eventlog
    [logggers]
    input.nt_eventlog.filename = /some/path

Well, not a very good example. Anyway, this creates the keys \"loggers.input\" and \"loggers.input.nt_eventlog\". This works for keys that are nicely named; it might be harder for a virtual host, which I\'d be apt to do like:

    [vhost my.vhost.domain]
    document_root = /some/path

Or something like that. Anyway, you want to create something like vhost\[\'my.vhost.domain\'\].document_root, not vhost.my.vhost.domain.document_root. Maybe it could be like:

    vhost[my.vhost.domain].document_root = /some/path
    # or....
    [vhost[my.vhost.domain]]
    document_root = /some/path

Anyway, there\'s still some other possibilities when using the ini syntax.

- I agree, but the approach is still more verbose than it need be. Java properties work like this; although they don\'t have sections, they give each property a hierarchical dotted name, and that can be used to create a hierarchy. For example:

<!-- -->

    app.name=GenericApp
    app.varname=surveyMaster
    app.logfile=/var/logs/${app.name}.log
    app.servlet=default_servlet
    app.templates=templates
    entity.user=User
    user.firstName.description=first name
    user.lastName.description=last name
    user.emailAddress.description=email address
    user.emailAddress.validator=email
    entity.group=Group
    group.description=respondent group
    group.name.description=name
    group.description.description=description

- You could use the above to indicate that a user entity is described by a class called User, and that a user instance has firstName, lastName and emailAddress properties \... and so on. It\'s workable, but hardly optimal.

Using my scheme, you could express the virtual hosts either like this:

    virtual_hosts :
    {
      host1 : { domain: 'host1.my-company.com', root : '/var/www/domains/host1.my-company.com/docs' }
      'host two' : { domain: 'host2.my-company.com', root : '/var/www/domains/host2.my-company.com/docs' }
    }

or like this:

    virtual_hosts : 
    [
      { domain: 'host1.my-company.com', root : '/var/www/domains/host1.my-company.com/docs' }
      { domain: 'host2.my-company.com', root : '/var/www/domains/host2.my-company.com/docs' }
    ]

The first form would be more useful for being able to refer to individual hosts by name (using \$virtual_hosts.host1 or \$virtual_hosts\[\'host two\'\]. You can also have your cake and eat it, by specifying both forms and having one refer to the other:

    virtual_host_definitions :
    {
      host1 : { domain: 'host1.my-company.com', root : '/var/www/domains/host1.my-company.com/docs' }
      'host two' : { domain: 'host2.my-company.com', root : '/var/www/domains/host2.my-company.com/docs' }
    }

    virtual_hosts : 
    [
      $virtual_host_definitions.host1
      $virtual_host_definitions['host two']
    ]

You might use the dict to access a specific host, and the sequence for iterating over the hosts in a pre-determined order. \-- [VinaySajip](../people/VinaySajip)

------------------------------------------------------------------------

I ([MichaelFoord](../people/MichaelFoord)) have improved [ConfigObj](../people/ConfigObj) to handle nested sections. The config file syntax is based on the \'INI\' format - so it will read files created for [ConfigParser](../language/ConfigParser) (with a few exceptions).

It uses \'dictionary\' access - which maintains a proper separation of the attribtues/methods of the object and the members of the config file.

Nested sections are indicated by additional square brackets around the sections headers. It allows comma separated lists. It also allows single values to be multiple lines with triple quotes.

See the [ConfigObj Homepage](http://www.voidspace.org.uk/python/configobj.html).

    [virtual hosts]

        [[host 1]]
        domain = 'host1.my-company.com'
        root = '/var/www/domains/host1.my-company.com/docs'

        [[host 2]]
        domain = 'host2.my-company.com'
        root = '/var/www/domains/host2.my-company.com/docs'

You would then access this through :

    # filename can also be a list of lines
    # or a StringIO instance
    config = ConfigObj(filename)
    #
    hosts = config['virtual hosts']
    host1 = hosts['host 1']
    host2 = hosts['host 2']
    domain1 = host1['domain']
    root1 = host1['root']
    #
    # or alternatively
    root1 = config['virutal hosts']['host 1']['root']

You can also set members and use the write method to write out the amended data.

A nice added feature is the integrated validation system. This defines a a \*simple\* and easily extendible system for validating config files. The validating process can also do type conversion of the values.

The system includes \'repeated sections\' which are an easy way of saying \'teh following specification applies to \*all\* subsections in this section\'. For the above example we could define a \'configspec\' for all hosts. Every host we added would then be validated using that spec.

For details of this see the [Validate Homepage](http://www.voidspace.org.uk/python/validate.html).

------------------------------------------------------------------------

A lot of the text format seems similar to JSON. I wonder if there would be any disadvantages to using JSON to marshal and unmarshal the configuration so that it would also be machine editable from Java as well without requiring a new custom Java library since there are already JSON libraries available for that.

Just curious because this library seems very useful and powerful but making it readable and writable programmatically outside of Python would seem advantageous. I wrote something a couple of years ago to do similar things in Java using Commons Configuration under the covers, but I get really tired of XML sometimes ![:)](/wiki/europython/img/smile.png%20":)")

Not being critical because I certainly applaud your effort and design thinking.

\-- [DavidMccurley](./DavidMccurley.html)

The format is similar to Python and JSON but a superset of it, which is why JSON wasn\'t used - it wasn\'t enough. For example, standard JSON does not support the use of the include notation (`@"abc.def"`), evaluation (`` `abc` ``), cross-reference (`$abc`), or expressions (`abc + def`). In addition, JSON (like Python, and unlike [JavaScript](./JavaScript.html)) requires use of literal strings as keys in mappings. Hence the more natural ` { path : "a/b" } ` must be written as ` { "path" : "a/b" } `, which is harder to parse.

\-- [VinaySajip](../people/VinaySajip)
