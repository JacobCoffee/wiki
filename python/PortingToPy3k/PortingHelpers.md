# PortingToPy3k/PortingHelpers

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Porting Helpers 

There are quite a few people who are interested in running their application/workflow using python3. In order to do that they need to port the stack of libraries underneath their application to use python3. This page is to start collecting and organizing these people so they don\'t duplicate work when porting libraries to python3, figure out how to get the changes merged upstream, figure out what libraries are important to port, and other sorts of coordination.

We\'ve just started on this but as we get more feedback of what people want to work on what tools would help them do their job we\'ll update the page.

## Knowledge we need 

- Lists of dependencies between python modules. Modules that are at the base of a lot of important dependency trees are more in need of a port.
  - Possibility \-- Linux distributions have extensive dependency information between packages. We should be able to run a script against the repository metadata on several Linux distributions to get an idea about this.
  - egginfo has some dep information as well. Does pypi pull out that information into a central location or would we have to download all the files from pypi and parse the egginfo?
- Status of modules moving to python3
  - Upstream status/branches for python3

  - Presence of python3 packages in Linux distributions where the python3 package is not upstream.
    - Patches to source code that make this possible
    - Build instructions for building the python3 version (like invoking 2to3 manually on the sources)

  - Presence of python3 packages upstream where the Linux distributions aren\'t providing them
    - This is useful for the Linux distribution so they can start working on them

  - Links to patches/branches/separate projects that provide python3 versions of a python2 module

  - Here\'s a rough example: [PortingToPy3k/Modules](./PortingToPy3k(2f)Modules.html) It\'s labor intensive so possibly not the best way to do this.

    - Information from [https://fedoraproject.org/wiki/Python3#Porting_status](https://fedoraproject.org/wiki/Python3#Porting_status) with some research of what the packages are using to build/patch
- Some table to track how best to contact upstreams
  - Whether the code should be branched on bitbucket/github/etc or we need to save patches somewhere
  - Mailing list or personal email to discuss python3 patches
  - Has upstream been asked if they\'ll accept python3 patches?
  - Has upstream professed interest in either a combined source or a separate source?

## Tools we need/could use 
