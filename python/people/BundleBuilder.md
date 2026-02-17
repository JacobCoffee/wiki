# BundleBuilder

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**Note:** BundleBuilder is going to be replaced by [py2app](../platforms/MacPython/py2app), a distutils extension that converts python scripts into executable Mac OS X applications, able to run without requiring an existing Python installation. This is a replacement for bundlebuilder. If you have used the PyObjC 1.2 installer, you do not need this because py2app 0.1.7 is included.

**Note:** Because py2app\'s development has slowed, BundleBuilder remains a useful alternative if you encounter issues with py2app. BundleBuilder has been removed from Python 3.x but extracting the module from the Python 2.x source tree and modifying as needed should not be difficult. See \* [http://www.pythonmac.org/wiki/BundleBuilder](http://www.pythonmac.org/wiki/BundleBuilder) for more information.

------------------------------------------------------------------------

Also see:

- [http://www.pythonmac.org/wiki/BundleBuilder](http://www.pythonmac.org/wiki/BundleBuilder)

BundleBuilder is a script that lets you create applets, or more importantly, standalone Python application bundles on Mac. To create an application bundle on Mac, you need to create a script which starts bundlebuilder, tells it what files and libraries you want to package, and then lets it do its thing. Here is an minimal bundlebuilder script for a fictional PyObjC application:

:::: 
::: 
``` 
   1 from bundlebuilder import buildapp
   2 
   3 buildapp(
   4         name = "MyApp",
   5         mainprogram = "MyAppMain.py",
   6         resources = ["MainMenu.nib"],
   7         nibname = "MainMenu",
   8 )
```
:::
::::

Bundlebuilder scripts are typically called \"buildapp.py\", and can be invoked from the command line in several ways. By default, bundlebuilder will create a folder named \"build\" in the current directory; the application will be built there.

Build an applet (depends on a Python installation):

- \% python buildapp.py build

However, the next invocation is much more useful during development, as instead of copying files to the bundle, it creates symbolic links to the original files, meaning you don\'t have to rebuild the applet after each change:

- \% python buildapp.py \--link build

To create a standalone application, it is typically invoked like this:

- \% python buildapp.py \--standalone \--strip build

The \--standalone option will cause almost everything that\'s needed (and nothing more!) to be included in the .app bundle. It analyzes which modules are (potentially) used. Sometimes this does not include enough (it may miss modules that are imported dynamically through the [import] hook), sometimes it includes too much (it follows every potential dependency, even if there on a brach of the code which will never be executed. To tweak what\'s included, use the \--include, \--package and \--exclude bundlebuilder options.

The \--strip option will strip all executable files inside the application bundle of their debugging info, which will have a huge impact on the size of the final bundle.

Try \--help for a list of options.

Here is a more elaborate example script that showcases more features of bundlebuilder, yet will only build a standalone application:

:::: 
::: 
``` 
   1 import bundlebuilder, os
   2 
   3 # I set this to make adding subfolders into the package easier
   4 packageroot = "/Users/kevino/oss/eclass/eclass_builder"
   5 
   6 # Create the AppBuilder
   7 myapp = bundlebuilder.AppBuilder(verbosity=1)
   8 
   9 # Tell it where to find the main script - the one that loads on startup
  10 myapp.mainprogram = os.path.join(packageroot, "editor.py")
  11 
  12 myapp.standalone = 1
  13 myapp.name = "EClass.Builder"
  14 
  15 # includePackages forces certain packages to be added to the app bundle
  16 myapp.includePackages.append("encodings")
  17 myapp.includePackages.append("_xmlplus")
  18 
  19 # Here you add supporting files and/or folders to your bundle
  20 myapp.resources.append(os.path.join(packageroot, "about"))
  21 myapp.resources.append(os.path.join(packageroot, "autorun"))
  22 myapp.resources.append(os.path.join(packageroot, "Graphics"))
  23 
  24 # bundlebuilder does not yet have the capability to detect what shared libraries
  25 # are needed by your app - so in this case I am adding the wxPython libs manually
  26 myapp.libs.append("/usr/local/lib/libwx_macd-2.4.0.dylib")
  27 myapp.libs.append("/usr/local/lib/libwx_macd-2.4.0.rsrc")
  28 
  29 # Here we build the app!
  30 myapp.setup()
  31 myapp.build()
```
:::
::::

In the future, BundleBuilder will be able to detect and incorporate shared libraries as well, meaning you will only need to worry about adding your own files to the bundle.

Todo: Troubleshooting bundlebuilder problems section? Yes, especially the encodings problem; it\'s a FAQ in the py2exe world. The quick fix is to add \--package=encodings to bundlebuilder\'s command line options. However, this includes all of the encodings package, which for many applications means unnecessary bloat.
