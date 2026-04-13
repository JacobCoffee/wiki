# Distutils Sprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Schedule 

[FredDrake](../people/FredDrake) suggested we start at 10:00am, at least on Saturday and Sunday, but apparantly others were better able to rise in the mornings. The DistutilsSprint was held in room 301 at the conference center.

## Topics 

Some projects which saw progress during the sprint included:

- The implementation of [PEP 314: Metadata for Python Software Packages v1.1](http://www.python.org/peps/pep-0314.html) should be complete; someone who isn\'t involved in the implementation should review what\'s in CVS and check it against the PEP. Work performed at the sprint included supporting the *provides*, *requires*, and *obsoletes* metadata fields in both the `distutils` package and in PyPI. The work was performed by [FredDrake](../people/FredDrake), [RichardJones](../people/RichardJones), and [AndyHarrington](../people/AndyHarrington). There may be some untracked changes in [AndrewKuchling](../people/AndrewKuchling)\'s draft of PEP 314; these should also be checked (also, the catalog-sig archives). [FredDrake](../people/FredDrake) believes that there are still some glaringly obvious metadata fields missing, necessitating a further revision of the package metadata specification.

- [RichardJones](../people/RichardJones) migrated the database away from the single-user sqlite database to a multi-user postgres one.

- [RichardJones](../people/RichardJones) and [MartinvonLoewis](../people/MartinvonLoewis) worked on implementing [PEP 243: Module Repository Upload Mechanism](http://www.python.org/peps/pep-0243.html), supporting a package repository as part of PyPI. There are revisions needed to PEP 243 which haven\'t been written yet (mostly to do with cleaning up the use of the HTTP spec). [FredDrake](../people/FredDrake) thinks he uploaded the first package into the live repository, a tarball containing ZConfig 2.2. Richard implemented the changes to the PyPI application, and Martin added an **upload** command to the `distutils` package to make it easy to add files from a command line. Uploads may also have an accompanying MD5 (for simple validation) and OpenPGP signature.

- [AndrewKuchling](../people/AndrewKuchling) integrated work done to add XML-RPC support based on efforts from the [ChiPy](../people/ChiPy) sprint. See [Ian Bicking\'s blog](http://blog.ianbicking.org/first-chipy-sprint-pypi.html) for more on the [ChiPy](../people/ChiPy) work.

- [RichardJones](../people/RichardJones) and [MichaelTwomey](../people/MichaelTwomey) integrated work started at the [ChiPy](../people/ChiPy) sprint to convert the PyPI web interface to use [ZopePageTemplates](../web/ZopePageTemplates) instead of hard-coded HTML in the Python code. This should make it a lot easier to keep the logic and presentation separate. \"Unit\" tests using Selenium were also developed.

- [JohnCamara](../people/JohnCamara) worked on some distutils bugs, and also implemented the [reStructuredText](../archive/reStructuredText) formatting of description fields. [DavidGoodger](../people/DavidGoodger) implemented a couple of safety switches in docutils allowing us to turn off the \"raw\" and \"include\" directives.

At a separate table in the other sprint room, this suggested topic was addressed:

- Phillip Eby brought up the idea of application plugins; it would be really nice to see this happen. He and Bob Ippolito have some [design notes](http://peak.telecommunity.com/DevCenter/PythonEggs) and Bob Ippolito has begun an implementation of the runtime. In addition to plugins, this \"Python Egg\" format should be useful for distributing libraries and building applications (via py2exe/py2app) as well.

The following topics had been suggested, but were not discussed during the \[PyConDC2005/Sprints\]:

- Installing large applications; see [Fred\'s post to the Distutils-SIG](http://mail.python.org/pipermail/distutils-sig/2005-February/004389.html) for more on this topic.

- Defining a way to define new *classes* of files that can be installed. Zope 3 would like this for the \"package-includes\" files we use; it\'s likely generally useful.

## Participants 

If you aren\'t planning to be available for all four days of the sprints, please note which days you will be around.

- [FredDrake](../people/FredDrake) (Saturday and Sunday)

- [RichardJones](../people/RichardJones)

- [MikeTaylor](../people/MikeTaylor)

- [JohnCamara](../people/JohnCamara)

- [AndrewKuchling](../people/AndrewKuchling) (Saturday and Sunday)

- [AndyHarrington](../people/AndyHarrington)

- [JeffreyHarrington](./JeffreyHarrington.html)

- [MartinvonLoewis](../people/MartinvonLoewis)

- [IanBicking](../people/IanBicking) (Saturday, maybe Sunday?)

------------------------------------------------------------------------

[CategoryPyCon2005](CategoryPyCon2005)
