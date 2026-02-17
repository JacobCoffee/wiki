# ConfigParser

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

(Also see [ConfigParserShootout](ConfigParserShootout) for discussion on alternatives and possible directions for future development.)

If you want to know how to use ConfigParser, see [ConfigParserExamples](ConfigParserExamples).

Python\'s `ConfigParser`{.backtick} module is part of the standard library. The module provides a parser for simple configuration files consisting of groups of named values. The best known format supported by this module is the \"INI\" syntax, most commonly used on the Microsoft platforms. The module was originally written to support a variant syntax in which the contents of each section resembled RFC 822 headers; the implementation still allows named values to be specified using either syntax. Between this historical accident and lack of a clear specification of the \"INI\" format has made this module very tedious to maintain, so the implementation has been changed in almost every Python release, and the behavior of the module has proven very tedious to describe completely.

The current behavior of the defaults has always been what was intended. The module was designed to support a suite of programs that could provide some information that was either used directly or to form parts of other values (such as path names that included the host name of the computer running a program). There was at the time no need to distinguish between different uses of \"default\" values, as [MartinManey](MartinManey) suggests below. (It\'s not clear to me now that there\'s a real need to do so, since the API provided by `ConfigParser`{.backtick} is so spare.)

The use of a \"magic section name\" for the current \"defaults\" in the current implementation is something I consider unfortunate; the defaults dictionary should be completely separate from the dictionary of sections. Should additional namespaces (\"types of defaults\") ever be considered, I\'d hope they don\'t become part of the set of section names by dumb accident. The inclusion of the defaults by the `write()`{.backtick} method is unfortunate; these were intended to be a way for an application to supply computed values that would be used if a specific configuration did not override them.

------------------------------------------------------------------------

In at least some applications (plucker), there are already several magic sections. In addition to defaults, there is a section (or two) based on the operating system, that acts like it is part of defaults. I believe the various default sections override more specific information in a less specific file, but I would have to look that up. (I.e., if the system .ini sets a value in the \"MyApp\" section, but a user .ini sets it in the \"Defaults\" section, which wins?)

I don\'t know how universal these conventions are.

JimJJewett

At Zope Corporation, we\'re using ConfigParser for configuration files used in our \"buildout\" process. We use a wrapper API that takes the section and option names, and searches for a platform-specific value before getting the non-specific value. The platform-specific values are given in alternate sections that have derived names. This seems to work well. \--[FredDrake](FredDrake)

------------------------------------------------------------------------

I\'ve been thinking about writing up some thoughts I\'ve had while trying to use `ConfigParser`{.backtick} for what seemed like a dirt-simple application a while ago. I ran into both the handwaviness of the documentation and either the *every version some changes* effect or perhaps it was just a bug shared by 2.1 and 2.2 (IIRC). Here I feel less inhibited from posting a rough draft, so\...

The problem I ran into was the handling of the default section. Apparently the latest thinking is that items in the default section should appear as items in every section. The version(s) I was using only injected them into the dictionary used for parameter substitutions (I think that was how it went, anyway). In the course of getting this straightened out, I had the thought that there are really two different types of defaults that would be useful, or perhaps three. One sort would supply default definitions only for substitution; its entries would never be pushed into the sections\' namespaces. The other sort works as I understand the 2.3 library version does, which may have been intended all along, and injects the default entries into every section (and hence are available for substitutions). I\'d like to have the first sort available, too. This seems to require another magic section name.

There, that\'s the essence of my too-small-for-a-PEP talk! [MartinManey](MartinManey)

------------------------------------------------------------------------

I don\'t know what the original model for ConfigParser was (aside from a vague wave in the direction of Windows INI files of some vintage; I\'m slightly familiar with them from the Win4Workgroups era), or how much variance there might be in later versions of Windows (aside from that note in the docs about the extended form that CP does not support).

I had an application where I needed a good-sized swath of config data that would be fairly static; at least in part generated by a human, AIs being found only in fiction and mostly bad movies at this time; partly generated or updated by some program (this part now seems doubtful, but I was optimistic then). Looking back now, I see that the bug in 2.1 and/or 2.2\'s implementation was in the has_option method, and in the end I worked around that. My experience with this, an app that had a need before I was familiar with ConfigParser, leads me to suggest that whatever abstract elegance there would be in doing away with the magic *DEFAULT* section, it is in fact very convenient in practice. Without it I should have had to split data that was all very closely related into two separate parts. Or, I suppose, I could have generated the config file from some meta-config file that would have included some functionality similar to ConfigParser-as-it-is, but then I\'d use that instead of ConfigParser, wouldn\'t I? Sorry, just being silly about being explicit here.

It was in the course of revising this same app that I encountered some cases where I should have liked to have had a *DEFINE* magic section: one whose values were only used in substitutions in the normal sections, not directly injected into them like *DEFAULT*. The same desire to keep related data together in the absence of some good reason not to would make it desirable to have this as another magic section. Of course the programmatic way of injecting default values (or defined ones, if that were added to the model) has its place as well. The most obvious one, at least to me, is when the default values should in fact be kept separately from the sections\' data, or when they are a way of injecting information from the environment into the config. I suspect the latter was the way substitutions are used in real Windows INI files, yes?

Funny, I thought I was going to talk about improvements to the docs here. Maybe next time! \-- [MartinManey](MartinManey)

It seems to me defaults are just place holders, what I want is to check for file.ini and if it is not found in the current directory write it with defaults. There is no \'defaults\' section, if I want defaults I just delete the file.ini. \-- [GaryMoffatt](GaryMoffatt)

Is there any rationale in `ConfigParser`{.backtick} for `sections()`{.backtick} not returning the list of sections in the order presented in the file? \-- [StephenHahn](./StephenHahn.html)

- Very simple: the order isn\'t stored; the sections are stored as a dictionary. It\'s also possible that the file contains multiple sections by the same name, which are collapsed into a single entry in the internal dictionary. \--[FredDrake](FredDrake)

  - Thanks. I had thought that .INI files had to have unique sections, but perhaps not. Being order-preserving allows sections to have precedence based on order, rather than an explicit attribute (which is what the config file I\'ve inherited has done, although it was parsed using another language\'s INI module). \-- [StephenHahn](./StephenHahn.html)

    - Hmm. Other parsers may be less forgiving. Too bad there\'s no real specification for the INI format (as best as I\'ve been able to tell). \--[FredDrake](FredDrake)
