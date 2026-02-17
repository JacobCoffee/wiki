# EuroPython2007/VisualStudio2005

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Visual Studio 2005 Sprint 

## This sprint has been canceled due to lack of interest 

------------------------------------------------------------------------

### This is a sprint suggestion to work on making Visual Studio 2005 a fully supported build platform for python 2.5 and 2.6 

- Where: Vilnius, Lithuania

- When: after [EuroPython](EuroPython), 12-14 july

- Organizer: Kristján Valur Jónsson \<[kristjan@ccpgames.com](mailto:kristjan@ccpgames.com)\>

Visual Studio 2005 has been availible for more than two years but still it is not an officially supported compiler for python. The benefits of using it are:

- greater performance, particularly through profiler guided optimization
- cross compilation for amd64 platform.

Although the PCBuild8 subdirectory is availible in the release25-maint branch and the trunk, a few things need to be done to make it complete:

- Fixup dependency on externals for some modules (bz2 etc), particularly for amd64
- Polish automatic PGO builds
- Fix and polish install script generation, and CRT redistribution
- Work on setting up a buildbot

Please contact me at \<[kristjan@ccpgames.com](mailto:kristjan@ccpgames.com)\> if you think this is a worthwhile project and want to participate.
