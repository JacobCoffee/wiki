# LoggingPackage

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page should cover pros and cons of current stdlib logging package.

# Pros 

- Almost every feature you could want from a logging package is there

# Cons 

- See below. Vinay made sections of each of the points in the original bulleted list for discussion.

## Docs are not complete 

**False**. There is pretty much everything in the docs. If you think something is missing, please, be more specific about the missing stuff.

## Docs are too long 

**True**. \-- techtonik

- The docs are now rearranged into reference API, tutorials (basic and advanced) and cookbook, so this complaint is not really valid. Earlier it was all in one page, so the complaint was more justified. \-- [VinaySajip](VinaySajip)

  - I agree that it became much better structurized than before, but the amount of text that an average user needs to read to completely understand how logging works didn\'t change. Neither part gives **a summary about current problems with logging** like the one about libraries below. For that part you really need to read everything, but the chances to find this are low. \-- techtonik

## Config files are a little bit hard to comprehend 

An alternate configuration mechanism is provided by the [ZConfig](http://www.zope.org/Members/fdrake/zconfig/) package ([PyPI](http://pypi.python.org/pypi/ZConfig/)). (Note ZConfig is not a small package to pull in.)

Another alternative is provided by the [config](http://www.red-dove.com/python_config.html) package, which is a single module and easy to incorporate into logging. However, what say people to the question of backward compatibility? \-- [VinaySajip](VinaySajip)

- So the answer is **True**, but can\'t not be changed, because of **backward compatibility**. \-- techtonik

  - Since dictionary-based configuration was added (Python 2.7/3.2, available in older Python versions via dictconfig on PyPI), this is not an issue. You can e.g. use YAML or JSON files for configuration. \-- [VinaySajip](VinaySajip)

If you want to suggest an alternative mechanism which uses [ConfigParser](ConfigParser), please suggest alternatives to the format. \-- [VinaySajip](VinaySajip)

I\'d rather avoid using config files (for logging) entirely in almost every project I work on. If logging has its own configuration files, that\'s a smell. If I need configfiles for my project, I\'ll choose the format I need, and expose the necessary settings to the user coherently, including logging settings. That it has its own configuration file to me is a smell, it suggests configuring in code is too hard, and too necessary. \-- [JoshuaRodman](./JoshuaRodman.html)

- It\'s not a smell - it\'s not necessary to use, but allows for easier configuration in some scenarios. You can certainly put other settings in the same file, or have separate files for other settings. I don\'t know of any convention that limits the number of configuration files in an application to zero or one. \-- [VinaySajip](VinaySajip)

## API uses camelCase (goes against PEP8 recommendation and most of the stdlib) 

PEP8 says - consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is most important.

- So **True**, but can\'t not be changed, because of **backward compatibility**. logging2 maybe. \-- techtonik

  - It\'s a low priority right now, unless there\'s an initiative to ensure the rest of the stdlib is made to conform to PEP8. \-- [VinaySajip](VinaySajip)

## Rather slow considering the large number of function calls performed internally to check which handler to use 

There is no official confirmation, but users report [25% boost](http://yuba.stanford.edu/vns/2010/02/fairness/) in performance after commenting logging stuff. So, this stays to be **True** until somebody proves otherwise.

- Unfortunately that Stanford post doesn\'t give any indication of how they used logging calls or how they configured it, so their bare statement does not really give any useful information about logging performance. \-- [VinaySajip](VinaySajip)

  - If you doubt that Stanford was right by calling logging to be slow then perhaps [stackoverflow page](http://stackoverflow.com/questions/522730/how-can-i-strip-python-logging-calls-without-commenting-them-out) will be more convincing. In short - for iner-loop-like scenarios (the 90% code) hotshot indicated logging was one of the biggest bottlenecks. \--techtonik

    - Did you notice the **accepted** answer to that Stack Overflow question? If **you** have specific performance problems, please post some code and some numbers. \-- [VinaySajip](VinaySajip)

  - Why not to include a performance related chapter into logging docs with a measurement instructions? That will be extremely handy for [http://speed.python.org](http://speed.python.org) \-- techtonik

    - In my view, there\'s no need to do this. Logging calls are of the order of 10s of microseconds, as indicated in figures on this page. \-- [VinaySajip](VinaySajip)

Vinay argues that \'logging can be too slow in some specialised scenarios\', and asks people to provide more objective metrics than \"lot of function calls\". Although we don\'t speak about specialized scenarios, it would be nice if at least these function calls were counted. There are (very simple) timing test results below.

## Is a pain in the arse for working with libraries 

Libraries should not output any logging information by default unless explicitly asked to do so. That\'s why they should not try to configure logging. But on the first call to any log() function logging configures itself automatically. This is only documented in thread safety note for logging.log() function and in logging.basicConfig() (one of the examples why **Docs are not complete** speculation is not corrent - the docs are there, they are just hard to find). So, if any used library uses logging, you **have to configure root logger** in your application even if it uses other logging means. \-- techtonik

- An application developer who uses libraries needs to configure logging in order to debug library behaviour. The alternative would be for libraries to output potentially copious debug logging information and needing to be explicitly silenced. \-- [VinaySajip](VinaySajip)

  - Ok, I removed the rant about logging being too obtrusive to debugging libraries. I don\'t want to debug these 3rd party libraries. Do I have an option to skip logging configuration in application? I don\'t even know if those libs are using logging at all. \-- techtonik
  - A second question - I am currently debugging Spyder IDE. IDE is a just a set of widgets initiated by a central window, but these are also used independently. How can I setup widget logging to be silent if used standalone and don\'t affect logging configuration of Spyder if used from the IDE? \-- techtonik
    - \-- Please don\'t post such questions here, try Stack Overflow or comp.lang.python. \-- [VinaySajip](VinaySajip)

------------------------------------------------------------------------

## Doesn\'t have runtime scoping (i.e., log messages handled based on the call stack) 

Please give some more details on what you mean here. How exactly would you want to log messages based on the call stack? \-- [VinaySajip](VinaySajip)

## Difficult to extend log records 

[LogRecords](./LogRecords.html) need to be pickleable to be sent across the wire. You can add arbitrary attributes to [LogRecords](./LogRecords.html) by using the \"extra\" keyword parameter to logging calls. Exactly how would you like to extend [LogRecords](./LogRecords.html) in a way which is difficult at the moment, and why? \-- [VinaySajip](VinaySajip)

- Changes in Python3.2 allow [more control over LogRecord creation](http://plumberjack.blogspot.com/2010/12/getting-more-control-over-logrecord.html) \-- [VinaySajip](VinaySajip)

I don\'t really know what this offers, but I usually prefer to simply add attributes to the python objects if I need to decorate them. Perhaps unconventional, but it feels pythonic to me. \-- [JoshuaRodman](./JoshuaRodman.html)

- Yes, but you don\'t normally have access to a [LogRecord](./LogRecord.html) when logging an event, so you can\'t simply add attributes to it. \-- [VinaySajip](VinaySajip)

## Difficult to add general context to log messages (e.g., add the request URL to all logging messages during the request) 

There\'s information on this very topic at [Adding contextual information to your logging output](http://docs.python.org/library/logging.html#adding-contextual-information-to-your-logging-output). Can you provide more details on how the mechanism provided fails to meet your needs? \-- [VinaySajip](VinaySajip)

I\'d prefer some log-invocation magic for the common cases, like the function name I\'m in as a token to be expanded. \-- [JoshuaRodman](./JoshuaRodman.html)

- The funtion name is already available without magic, have you checked the documentation? \-- [VinaySajip](VinaySajip)

## By default it does nothing; basicConfig makes it do something but makes it hard to tweak logging. 

How would you want to tweak logging in a way which basicConfig doesn\'t make easy? Suggest improvements which can be made to basicConfig, I\'m receptive. Remember to consider backward compatibility. \-- [VinaySajip](VinaySajip)

A logger with no handlers should default to sending to stderr or something like this. Perhaps it already has a handler. Perhaps there is a default handler set by default. I shouldn\'t have to configure anything for the simplest case of a script. Further, this means that I can test modules independently from my larger project and get a sane behavior. \-- [JoshuaRodman](./JoshuaRodman.html)

- Don\'t agree with your suggestions - a third party library which uses logging should not spew logging output by default which may not be wanted by a developer/user of an application which uses it. For the simplest case of a script, just use logging.info() etc. and it invokes basicConfig() under the covers. Have you checked the documentation? \-- [VinaySajip](VinaySajip)

## filters are an abstract class instead of callables 

Filter is not an abstract class - it\'s a concrete class with a reasonable default implementation. Is this really a major design flaw? It would be easy to modify the package to add callables to the filter list, and the system could expect either a Filter instance or a callable. \-- [VinaySajip](VinaySajip)

## Thread-local handlers aren\'t easy to setup 

Please suggest how you would like these to work, and why you need thread-local handlers? You already have the ability to insert thread-local context information into messages using non-thread-local handlers. \-- [VinaySajip](VinaySajip)

## Nothing like keywords or tags for doing multi-dimensional categorization or grouping of messages 

How many use cases need this? How would you see this being implemented? Buffering of messages is already possible. Talk is cheap, so please describe your use cases in more detail and how you think an \"ideal\" API for \"multi-dimensional categorization\" or \"grouping\" would look. \-- [VinaySajip](VinaySajip)

## No clear way to introduce HTML-formatted messages (or an HTML formatting option) 

You can post messages to web sites, and present messages in HTML format in numerous ways; is this a common use case and would we get common agreement on how this would work (i.e. a specific HTML representation) ? \-- [VinaySajip](VinaySajip)

## Not fast enough to do pervasive logging in libraries (we\'ve encountered this with Paste/Pylons, where we\'d like to put lots of logging in that people could turn on, but it becomes a notable performance hit). 

Please clarify - how much of a performance hit is it if logging is turned off for particular modules? When you encountered performance issues, what mitigating strategies did you try? (e.g. isEnabledFor) \-- [VinaySajip](VinaySajip)

I set up a very simple script to time logging calls, available [here](http://gist.github.com/191065). Output looks like this (Python 2.6 on Windows, Core Duo E8400):

    log_noop              0.13 microseconds
    log_simple           57.36 microseconds
    log_filtered          4.19 microseconds
    log_mitigated         3.78 microseconds
    log_disabled          0.98 microseconds
    No caller, thread, process info...
    log_simple           49.89 microseconds
    log_filtered          4.19 microseconds
    log_mitigated         3.79 microseconds

which means that a simple logging call takes around 57 microseconds, reduced to around 50 microseconds if you opt to not collect caller, thread or process info. That\'s for logging to a file. So what are your expectations for performance? These numbers don\'t look too shabby to me. Of course, it\'s a simplistic test, but at least there are some actual numbers there. \--[VinaySajip](VinaySajip)

## Too complicated, with logging levels, namespaces, handlers, and other things \-- they took all the terrible things from java.util.logging and log4j, which are incredibly slow (but powerful) in python 

Good ideas don\'t only come from Python people, folks. These ideas were proven in log4j and other packages and they are based on the ideas of \"what happened? where did it happen? how important is it? who wants to know?\" and if you think about it, these ideas are hardly Java-specific. OTOH, they are pretty central to the problem domain addressed by logging. So - \"what happened?\" is the details of the logging call, \"where did it happen?\" is the namespace, \"how important is it?\" is the level, and \"who wants to know?\" is the handler. Hardly that complicated, and AFAICT pretty much a minimum requirement for any logging package that aspires to the name.

And, \"incredibly slow\" is pretty emotive. Care to back that up with some hard data? See the numbers above for some ideas. Also, anyone who bothers to look at log4j in detail will see that Python logging is not a mindless translation - it\'s fairly Pythonic. Beyond the basic abstractions of \"What? Where? How Important? Who Needs To Know?\", there\'s no real correspondence between the Java artifacts and the Python ones. Using David A. Wheeler\'s SLOCCount, log4j 1.2.15 = 168 source files, around 16K SLOC; Python 2.6 logging = 3 source files, \< 1.5K SLOC. To me the Java connection and inferences that people draw from the \"Java heritage\" is bordering on FUD a lot of the time, I have to say. But feel free to put me right with *specific* comments rather than vague arm-waving, and you\'ll find me receptive. \-- [VinaySajip](VinaySajip)

It is too complicated. More defaulting is needed, and simpler construction. I should be able to get a logger talking to a rolling logfile in a single line, and that line should not be overly verbose. Sure, it might not be what I\'ll eventually want, but I need it to start working right away, so I can continue to figure out what I need. \-- [JoshuaRodman](./JoshuaRodman.html)

- Then write your own utility function in a utility library of your own to make this happen. Not everybody thinks the same way, so it\'s better if people write their own simple-to-use (for them) wrappers on top of the existing functionality. Once written, you can import from your utility package into other applications you write. \-- [VinaySajip](VinaySajip)

## The appropriate roles for args and kwargs in loggerAdapter are ambiguous. 

I\'m finding the paradigms for augmenting log arguments with relevant context info confusing. The docs and general web info are helpful but slim on the topic so far. Adding contextual info via the \'extra\' parameter with loggingAdapter(. . . ,extra=myClassObj \| extra=my.[dict] ) is slick for some use cases, not so much for others. It seems that the extra= is set in stone when the loggerAdapter object is instantiated, then passed to the individual [LogRecords](./LogRecords.html) as needed (true?/false?). Context specific to the location of the log() call is superseded by the context of the loggerAdapter instantiation. Any kwargs\[\'extra\'\] in the log() calls are overwritten silently. Perhaps that\'s a feature, and context info specific to the log() call location should be Youincorporated using log(\... args) and having Formatters manage and replace the the actual args? At present, the use of the kw extra is handled by logging in the reverse behavior of most inherited object properties, where lower level objects supercede the higher level class values. Fortunately, the logging mechanisms are so flexible that it\'s not difficult to use args in place of kwargs (even for class arguments), or to alter the default behavior of logging for the extra kw. Still, it\'s confusing as is when the use case is not to pass down the context of the logger instantiation to all subsequent log() calls. I have code for both solutions if there is interest. (This comment seems long and detailed relative to the intended context of this page. Is there another place for similar discussion? Also: where to post demo code that is neither patch nor bug?)

- Please give details of the use case which is giving you problems, on comp.lang.python rather than here: that\'s a better platform for receiving support. The \"extra= is set in stone\" only applies to the default implementation of `LoggerAdapter` - you\'re free to override this behaviour by creating a subclass of `LoggerAdapter`. The \"overwritten silently\" is clearly documented at

  [http://docs.python.org/library/logging.html#adding-contextual-information-to-your-logging-output](http://docs.python.org/library/logging.html#adding-contextual-information-to-your-logging-output)

  You should only really be using `LoggerAdapter` for specialised cases e.g. when you are logging information relating to database or network connections and need to log the context of individual connections as well as the specifics of an individual event. For most other uses, just using a %-format string and arguments should suffice. Without knowing the details of your use case, it\'s hard for me to know whether there is a real problem with `LoggerAdapter` functionality or just with your understanding of it; your comments above indicate to me that it could well be the latter. So, please post what you are trying to do on comp.lang.python, and what problems you are having, with \"logging\" in the title/subject of your post. You can post short snippets of code there directly; if you want to post longer pieces you can use any public pastebin (e.g. dpaste, `LodgeIt`, gist.github.com, \...) and link to the posted snippets from your mailing-list post. You can either mail into comp.lang.python using the email address [python-list@python.org](mailto:python-list@python.org), or use e.g. Google Groups\' web interface via

  [http://groups.google.com/group/comp.lang.python/topics](http://groups.google.com/group/comp.lang.python/topics)

  \-- [VinaySajip](VinaySajip)
