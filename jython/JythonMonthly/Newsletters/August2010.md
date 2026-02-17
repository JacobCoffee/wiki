# JythonMonthly/Newsletters/August2010

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: {}
  ----------------------------------------- ---------------------------------------------------------------------------------------------------
  ***Jython Monthly***                       ![](http://www.jython.org/css/jython.png "http://www.jython.org/css/jython.png")
  **August/September 2010 \-- Issue #45**   
  ----------------------------------------- ---------------------------------------------------------------------------------------------------
:::

This is the Jython Monthly newsletter for the months of August and September of 2010. These are exciting times for Jython as the second beta for 2.5.2 has been released. Please download and test now if you haven\'t done so already! Due to a lack of materials over the past couple of months, the newsletter will combine both August and September together. I plan to distribute a separate special [JavaOne](./JavaOne.html) update after the conference as well.

If you have any questions or suggestions for the newsletter, please feel free to send them to [jythonpodcast@gmail.com](mailto:jythonpodcast@gmail.com). I appreciate the feedback!

Thanks

My information is as follows:

Josh Juneau

- Podcast Website: [http://www.jythonpodcast.com](http://www.jythonpodcast.com)

- [jythonpodcast@gmail.com](mailto:jythonpodcast@gmail.com)

- Podcast Feed: [http://feeds.feedburner.com/JythonPodcast](http://feeds.feedburner.com/JythonPodcast)

## News 

**Jython 2.5.2 b2 Has Been Released**

The Jython development team has released the second beta for the 2.5.2 release. The list of issues that have been addressed are as follows:

\[ 1327 \] Classloaders cannot GC, which exhausts permgen (partial bug fix)

\[ 1604 \] [PyBuiltinCallable](./PyBuiltinCallable.html).Info should be serializable

\[ 1397 \] Bugs in [PyList](./PyList.html) and [PyJavaType](./PyJavaType.html).[ListIndexDelegate](./ListIndexDelegate.html) slice setting

\[ 1503 \] Java constructors should take keyword arguments

\[ 1648,1495,1516 \] Incomplete implementation of pep328 for relative imports

\[ 1611 \] Jython bytecode violated JLS, causing NPE on Sun\'s JVM when using -Xcomp option

\[ 1643 \] Tools subdirectory still exists in trunk

\[ 1455 \] Classes loaded dynamically from sys.path do not have their package defined

\[ 1555 \] Jython does not publish MIME types via JSR 223 ([ScriptEngine](./ScriptEngine.html).getFactory().getMimeTypes() is empty).

\[ 1632 \] cPickle.Unpickler does not allow assignment of find_global

\[ 1395 \] [PyList](./PyList.html).indexOf() and [PyTuple](./PyTuple.html).indexOf() do not function properly

\[ 1373 \] Jython [ClassLoader](./ClassLoader.html) getResource does not work

\[ 1506 \] Jython applies PEP263 pattern for determining source-code encoding on noncomments

\[ 1630 \] threading.Thread lacks [tojava] method

\[ 1558 \] [PyFunction](./PyFunction.html) to single method interface wrapping does not andle java.lang.Object methods

\[ 1622 \] array type prevents [radd] fallback

Please go [download](http://www.jython.org/downloads.html) the release and test today! Report any issues to the [Jython bug tracker](http://bugs.jython.org). Congrats to the development team on another excellent release.

**Blog Series - Jython and Swing**

*By: Bob Gibson*

Bob Gibson\'s blog series on Jython and Swing continues and it is available at [DeveloperWorks Blogs](http://www.stumbleupon.com/su/30gLrh/www.ibm.com/developerworks/mydeveloperworks/blogs/JythonSwing/entry/unsafe_at_any_speed150?ca=twtrJythonSwingSafedth-MydW). Excellent work done by Bob Gibson, author of Websphere Application Server Administration Using Jython.

## Blogs 

[Jython 2.5.2 Beta 2 Is Released](http://zyasoft.com/pythoneering/2010/09/jython-2.5.2-beta-2-is-released/) - Jim Baker

[Jython 2.5.2 Beta 2 Is Released](http://fwierzbicki.blogspot.com/2010/09/jython-252-beta-2-is-released.html) - Frank Wierzbicki

[Multithreading in Jython](http://blog.asolofnenko.cjb.net/index.php/2010/09/12/multithreading_in_jython)

[Jython Python Function](http://openfoo.org/blog/jython_python_function.html)

## Articles 

[Swing Texting Can Be Fun](https://www.ibm.com/developerworks/mydeveloperworks/blogs/JythonSwing/entry/texting_can_be_fun20?oldlang=ko&lang=en) - Bob Gibson

## Discussions 

[Jython Classes and Variable Scope](http://stackoverflow.com/questions/3681002/jython-classes-and-variable-scope)

[Getting the Previous Line in Jython](http://www.weask.us/entry/previous-line-jython)

## Frameworks 

[Django-Jython Project](http://code.google.com/p/django-jython/)

[Pylons on Jython](http://wiki.pylonshq.com/display/pylonscookbook/Pylons+on+Jython)

[Web2Py](http://www.web2py.com/)

## Documentation 

[Glassfish Server 3.0.1 Scripting Docs](http://docs.sun.com/app/docs/doc/821-1760/gjiam?a=view-oracle)

[Glassfish V3 Admin Console](http://wiki.glassfish.java.net/attach/GlassFishV3AdminConsole/admingui-3.1-modules.html)

[WSO2 Documentation](http://wso2.org/project/wsf/jython/documentation)

## IDE 

[Field Project](http://openendedgroup.com/field)

[PyDev 1.6.2](http://pydev.sourceforge.net/)

[Netbeans 6.9.1](http://www.netbeans.org)

[jHepWork](http://jwork.org/jhepwork)

[Intellij](http://www.jetbrains.com/idea/)

[Jython Processor with Swing GUI](http://jythonprocessor.sourceforge.net/)

::: {}
  ----------------------------------------------------------------
  **Links**
  [Jython Home](http://www.jython.org)
  [Python Home](http://www.python.org)
  [Jython WikiPedia](http://en.wikipedia.org/wiki/Jython)
  [Freshmeat.net](http://freshmeat.net/projects/jython/)
  [Python Daily News](http://www.pythonware.com/daily/)
  [Planet Jython](http://planet.jython.org/)
  ----------------------------------------------------------------
:::
