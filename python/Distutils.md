# Distutils

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Distutils 

Distutils is a mechanism to distribute Python packages and extensions provided in the Python standard library since Python 1.6.

### Current status 

Maintenance of the Python packaging ecosystem has largely moved away from the standard library and the CPython core development team and is now being handled by distutils-sig and the Python Packaging Authority.

- For up to date user focused documentation, refer to the Python Packaging User Guide: [https://packaging.python.org](https://packaging.python.org)

- For more details on the Python Packaging Authority, its goals, and current activities: [https://www.pypa.io](https://www.pypa.io)

::: caution
The rest of this page and its subpages relate to a previous attempt at improving the Python packaging ecosystem, known as distutils2. Much of it can likely be deleted, but it should be reviewed first to see if any of it should be preserved.
:::

------------------------------------------------------------------------

## Historical distutils2 focused content 

- [Distutils/DiscussionOverview](./Distutils(2f)DiscussionOverview.html)

- plugin systems, entry points

- static metadata

- testing infrastructure

### Past distutils2 work 

- [Distutils/Terminology](./Distutils(2f)Terminology.html): New terminology

- [Distutils/VersionComparison](./Distutils(2f)VersionComparison.html) : the goal is to come up with a version comparison system that superseds Distutils\' current one

- [Distutils/StandardizeEggInfo](./Distutils(2f)StandardizeEggInfo.html) : the goal is to finalize PEP 376

- [Distutils/Metadata](./Distutils(2f)Metadata.html) : the goal is to finalize PEP 345

- [Distutils/StaticMetadata](./Distutils(2f)StaticMetadata.html) : the goal is to come out with a proposal to split setup.py into a static metadata file + a lighter, almost empty script.

- [Distutils/Friends](./Distutils(2f)Friends.html) : the goal is to try to find a project, a person or a group of person on each platform that is willing to maintain a third-party tool that build system-specific distros out of python package.

- [Distutils/PluginSystem](./Distutils(2f)PluginSystem.html) : a Plugin system to extend commands

- [Distutils/TestingInfrastructure](./Distutils(2f)TestingInfrastructure.html) : Testing infrastructure

### Learning Distutils 

#### Documentation 

- [distutils --- Building and installing Python modules](http://docs.python.org/library/distutils.html)

  - [Distributing Python Modules](http://docs.python.org/distutils/) - information for developers

  - [Installing Python Modules](http://docs.python.org/install/) - information for users and system administrators

- [distutils SIG](http://www.python.org/sigs/distutils-sig/)

- [PyPI\'s XML-RPC interface](http://wiki.python.org/moin/PyPiXmlRpc) for querying the packages database

- [/Cookbook](./Distutils(2f)Cookbook.html)

- [/FAQ](./Distutils(2f)FAQ.html)

#### Projects 

- [/Projects](./Distutils(2f)Projects.html) - please add a listing to this page if you\'re working on Distutils (and help us reduce duplication of effort)

- [/Extensions](./Distutils(2f)Extensions.html) is a repository of extensions for your \"setup.py\".

#### Tutorials 

- [/Tutorial](./Distutils(2f)Tutorial.html) is a small tutorial to introduce the topic. It includes a complete demo, from start to finish.

- [CheeseShopTutorial](CheeseShopTutorial) is a related tutorial that just covers submitting information to the [Python Package Index](http://pypi.python.org/pypi)

- [Python Package Index Tutorial](http://www.python.org/~jeremy/weblog/030924.html) by Jeremy Hylton covers the use of the distutils register command.

#### History 

Distutils module was included in standard distribution in Python 1.6. It was back in year 2000. Before that Distutils was available in Python 1.5.2 as a separate download. [Since then](http://www.python.org/doc/1.6/dist/dist.html) Distutils expanded with new commands, but after almost 10 years basic principles stays the same - there is central **setup.py** file, which everybody can add its own code to. There is configuration **setup.cfg** where you can set default options for supported Distutils commands. The flexibility that Distutils architecture promotes, the lack of conventions and API that enforces them resulted in that there still no way to uninstall or list installed packages/modules, no way to query their versions either. Absence of clear border between Distutils and custom code places additional burden on newcomers in Distutils packaging that prefer to learn by example from some other existing configuration.

#### Misc. 

[Distutils/DistributeSprint](./Distutils(2f)DistributeSprint.html) : Sprint ideas

[/Proposals](./Distutils(2f)Proposals.html)

#distutils - irc channel for Distutils
