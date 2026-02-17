# VPython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

VPython is an extension for Python to allow easy, \"pythonic\" 3D. It is used in education for various purposes, including teaching physics and programming, but it has also been used by research scientists to visualize systems or data in 3D.

[VPython Home Page](http://vpython.org/)

## 2013-03-02: VPython 6.04 

## New (Dec. 2008): Opacity, Materials, Local Lights 

At [vpython.org](http://vpython.org) there is now available the Visual 5.0 release candidate for Windows, Mac 10.4 or 10.5 (Intel or PowerPC), and Linux. The native-mode Mac version does not use X11 nor depend on Fink.

Major new features include opacity, local lighting, and materials such as wood. Of interest to researchers is the new \"points\" object which is useful for representing data in 3D.

Visual 5.0 was created by David Scherer and Bruce Sherwood. Jonathan Brandmeyer while an undergraduate at NCSU provided support in Visual 4beta for opacity, local lighting, and textures, and made some important architectural changes, but had to stop work on the project before it was completed. Further development has led to API changes which are incompatible with the Visual 4beta release, so this release is called version 5 instead of 4.

You will see shader errors and/or the inability to display materials such as wood if your graphics hardware does not support Pixel Shader 3.0. The key point is this statement in the Visual 5.0 help (see the \"What\'s new\" section or the \"materials\" section):

Materials will work with graphics cards that support Pixel Shader 3.0 (\"PS 3.0\"). For details, see [en.wikipedia.org/wiki/Pixel_shader#Hardware](http://en.wikipedia.org/wiki/Pixel_shader#Hardware). Some materials may work with graphics cards that support PS 2.0, but other materials may need to be manually disabled; see instructions in the site-settings.py module in the Visual package in your site-packages folder. If the graphics hardware does not support pixel shaders, the material property is ignored. If you think you should be able to use materials but have trouble with their display or performance, we highly recommend upgrading your video card drivers to the latest version.

# Projects using VPython 

[PyGeo](http://pw1.netcom.com/~ajs/) A dynamic geometry laboratory and toolkit by Arthur Siegel.

[Matter & Interactions](http://www4.ncsu.edu/~rwchabay/mi/) An introductory calculus-based physics curriculum for engineering and science students by Ruth Chabay and Bruce Sherwood (NCSU) that emphasizes a small number of powerful fundamental principles, incorporates the atomic nature of matter throughout, and includes an introduction to computational physics, in which students write programs in VPython to predict motion and to visualize fields. At this URL you\'ll find a bunch of VPython lecture demo programs useful in teaching introductory physics.

[Physics Applications](http://physics.syr.edu/~salgado/software/vpython/) by Rob Salgado. Includes an extensive list of links to projects using VPython.

[Earth Science Applications](http://lurbano-6.memphis.edu/GeoMod/index.php/Main_Page) created by Lensyl Urbano and students at the University of Memphis (NOTE: this site is moving to [http://earthsciweb.org/GeoMod/](http://earthsciweb.org/GeoMod/)). It includes [Educational models](http://lurbano-6.memphis.edu/GeoMod/index.php/Main_Page#Interactive_Educational_Models) (some adapted from [Matter & Interactions](http://www4.ncsu.edu/~rwchabay/mi/) to add interactivity) as well as, python models that use Vpython for runtime visualization in [active research](http://lurbano-6.memphis.edu/GeoMod/index.php/Main_Page#Python_models) and an [introductory, computer modeling class](http://lurbano-6.memphis.edu/GeoMod/index.php/Introduction_to_Modeling).

# VPython FAQ 

*This could also be moved to its own page if it grows unwieldy.*

[VPython video tutorials](http://www.archive.org/search.php?query=subject%3A%22vpython%22) by Erik Thompson (archived at archive.org)

------------------------------------------------------------------------

[CategoryPyGUI](CategoryPyGUI)
