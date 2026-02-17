# JythonDeveloperGuide/EclipseSubclipse

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Setting up the jython development environment in Eclipse with Subclipse 

Another way (see [EclipseNotes](./EclipseNotes.html)) to obtain the jython sources to Eclipse is to use the Subclipse plugin (Subversion for Eclipse). (I\'m not sure whether sf.net has some temporary technical problems right now, but at least I wasn\'t able get the sources via CVS at all.)

This advice is applicable to Eclipse 3.2, but might work for previous releases too.

## Installing the Subclipse plugin 

- Go to Help -\> Software Updates -\> Find and Install\...

- Go to Search for new features to install

- Add a new remote site: [http://subclipse.tigris.org/update_1.2.x](http://subclipse.tigris.org/update_1.2.x) (see [http://subclipse.tigris.org/callisto.html](http://subclipse.tigris.org/callisto.html) for more details)

- Install the plugin by selecting the product from the subclipse site.

## Checking out the Jython project 

- Switch to SVN Repository Exploring perspective

- Add a new SVN repository, URL: [https://svn.sourceforge.net/svnroot/jython](https://svn.sourceforge.net/svnroot/jython)

- Select trunk/jython from the repository tree and Checkout the project as usual.
