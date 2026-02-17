# MacPython/BundleBuilder

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### NOTE: \[\[../py2app\]\] is another tool for creating Mac Python applications, and many users prefer it to bundlebuilder. 

Building applications on MacOS X is very easy using bundlebuilder.py.

First create your app building script like so:

:::: 
::: 
``` 
   1 ### makeapplication.py
   2 from bundlebuilder import buildapp
   3  
   4 buildapp(
   5     name='Application.app', # what to build
   6     mainprogram='main.py', # your app's main()
   7     argv_emulation=1, # drag&dropped filenames show up in sys.argv
   8     iconfile='myapp.icns', # file containing your app's icons
   9     standalone=1, # make this app self contained.
  10     includeModules=[], # list of additional Modules to force in
  11     includePackages=[], # list of additional Packages to force in
  12     libs=[], # list of shared libs or Frameworks to include
  13 )
  14  
  15 ### end of makeapplication.py
```
:::
::::

Then do this:

    % python makeapplication.py build

That command should create a stand-alone application bundle in build/Application.app. Try running it! It may work, but it probably needs a little help first.

When you run your makeapplication.py, there will most likely be a few warnings. These can usually be ignored safely. Also, there may be additional modules and libraries that your application requires that buildapp() couldn\'t determine it needed to include. You can add those it missed using its includeModules and includePacakges arguments.

When building a stand-alone application that uses additional Frameworks besides the Python.Framework, you can have buildapp() include them for you using its libs argument. For example, if your application uses [Tkinter](http://tcltkaqua.sourceforge.net/), you\'d use this:

:::: 
::: 
``` 
   1 buildapp(
   2     ...
   3     standalone=1,
   4     libs = [
   5             '/Library/Frameworks/Tk.Framework',
   6             '/Library/Frameworks/Tcl.Framework'
   7         ]
   8     ...
   9 )
```
:::
::::

Building a stand-alone application creates an application bundle which contains everything it needs to run including its own copy of the Python.Framework. If that\'s not to your liking, you can build using \'semi-standalone=1\' instead. This will make your application bundle smaller as it won\'t include python, but it does require that your users already have a working python installed.

**How to Use [BundleBuilder](BundleBuilder) with 64-Bit Python 2.6 on 10.5 and Later**

1\. In your setup/makeapplication.py script, don\'t import or set the argvemulation option\--comment it out. Argvemulation is dependent on Carbon libraries that are not supported in 64-bit, and which are removed altogether from Python 3.x. 2. When you run the setup script, make sure you call python2.6-all as the Python interpreter\--this will hit the 64-bit and 32-bit versions. A sample call looks like this:

    python2.6-all makeapplication.py build

And that\'s it.

Bundlebuilder is not present in Python 3.x, so if you want to use it, you will have to extract bundlebuilder.py from a Python 2.x source tree and modify it as needed. Bundlebuilder is quirky and a less graceful solution than py2app: you have to do some trial and error to get all the packages bundled in your application. However, because py2app\'s development is very slow at this point and it is not keeping up with changes in Python and OS X, bundlebuilder may be a simpler and useful alternative.

There are other options you can set in the call to buildapp(). See the bundlebuilder.py module for the rest of them. In addition, all of them can be set from the command-line instead. Here the complete command-line usage:

    Usage:
      python bundlebuilder.py [options] command
      python mybuildscript.py [options] command
     
    Commands:
      build build the application
      report print a report
     
    Options:
      -b, --builddir=DIR the build directory; defaults to "build"
      -n, --name=NAME application name
      -r, --resource=FILE extra file or folder to be copied to Resources
      -f, --file=SRC:DST extra file or folder to be copied into the bundle;
                             DST must be a path relative to the bundle root
      -e, --executable=FILE the executable to be used
      -m, --mainprogram=FILE the Python main program
      -a, --argv add a wrapper main program to create sys.argv
      -p, --plist=FILE .plist file (default: generate one)
          --nib=NAME main nib name
      -c, --creator=CCCC 4-char creator code (default: '????')
          --iconfile=FILE
    afa
     filename of the icon (an .icns file) to be used
                             as the Finder icon
          --bundle-id=ID the CFBundleIdentifier, in reverse-dns format
                             (eg. org.python.BuildApplet; this is used for
                             the preferences file name)
      -l, --link symlink files/folder instead of copying them
          --link-exec symlink the executable instead of copying it
          --standalone build a standalone application, which is fully
                             independent of a Python installation
          --semi-standalone build a standalone application, which depends on
                             an installed Python, yet includes all third-party
                             modules.
          --python=FILE Python to use in #! line in stead of current Python
          --lib=FILE shared library or framework to be copied into
                             the bundle
      -x, --exclude=MODULE exclude module (with --(semi-)standalone)
      -i, --include=MODULE include module (with --(semi-)standalone)
          --package=PACKAGE include a whole package (with --(semi-)standalone)
          --strip strip binaries (remove debug info)
      -v, --verbose increase verbosity level
      -q, --quiet decrease verbosity level
      -h, --help print this message
