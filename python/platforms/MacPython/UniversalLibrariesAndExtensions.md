# MacPython/UniversalLibrariesAndExtensions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Universal Libraries and Extensions for OS X 10.4+ 

## Introduction and Background 

Recent versions of Xcode for Mac OS X 10.4 Tiger introduced the ability to create multi-architecture (PowerPC and x86) executables and libraries, known as *Universal* binaries. Most UNIX libraries' build configurations have not adapted their build \'recipes\' to utilize this capability, so they produce only the approriate binary for the platform on which they were compiled, resulting in slower or no execution on the other platform. This is certainly true of PIL, the Python Imaging Library, as of version 1.1.5. While each build \'recipe\' differs depending upon the tools used by its maker and the libraries it is dependent upon, here are some instructions for builidng a Universal PIL and associated libraries, and a few tips on getting \'off-the-shelf\' UNIX libraries to compile as Universal libraries.

**Note:**

- Prebuilt universal packages for Python 2.4 are available at

[http://pythonmac.org/packages/py24-fat/index.html](http://pythonmac.org/packages/py24-fat/index.html)

- Prebuilt universal packages for Python 2.5 are available at

[http://pythonmac.org/packages/py25-fat/index.html](http://pythonmac.org/packages/py25-fat/index.html)

## PIL (Python Imaging Library) Example 

To build a Universal PIL, we must first build Universal versions of its dependent libraries:

- freetype2,
- jpeg-6b, and
- zlib\*
  - *\*Since Apple includes zlib with OS X 10.4, we only have to make Universal binaries for freetype2 and jpeg-6b.*

### Notes and Assumptions 

1.  The source code versions here are valid at the time of writing but will inevitably become out of date. If we are lucky, newer versions will detect OS X and build Universal versions for us. If not, you\'ll have to adjust the instructions accordingly.
2.  I assume you are famliar with operating the UNIX shell on OS X and with the typical UNIX install \'recipe\':
    - /configure; make; sudo make install
3.  I allow the libraries to be installed on my system in the default locations rather than just a temporary build directory because this recipe is about making a working installation and not about building the components to create a package.
4.  We really don\'t need to make Universal binaries jsut to install on a single paltform, but I am providing this to show the diffrerent techniques I have stumbled upon to coax UNIX libraries to compile \'universally\'

### Universal freetype2 

1.  first get the source and put it a working directory you choose: [http://easynews.dl.sourceforge.net/sourceforge/freetype/freetype-2.1.10.tar.gz](http://easynews.dl.sourceforge.net/sourceforge/freetype/freetype-2.1.10.tar.gz)

2.  open a Terminal window and change your working directory to the local of the archive file: *pushd \<your directory path here\>*

3.  unarchive it: *tar zxf freetype-2.1.10.tar.gz*

4.  change to the working directory for the source: *cd freetype-2.1.10*

5.  configure the source for your platform: *./configure*

6.  find the file freetype uses to determine hwo to compile the source on UNIX platforms and open it in your favorite text editor: *./builds/unix/unix-cc.mk*

7.  change the line: *CFLAGS := -c* to *CFLAGS :=-arch ppc -arch i386 -c*

8.  build the library: *make*

9.  Install it in the default location (/usr/local); *sudo make install*

10. return to the original directory: *popd*

### Universal jpeg-6b 

1.  first get the source and put it a working directory you choose: [http://www.ijg.org/files/jpegsrc.v6b.tar.gz](http://www.ijg.org/files/jpegsrc.v6b.tar.gz)

2.  open a Terminal window and change your working directory to the local of the archive file: *pushd \<your directory path here\>*

3.  unarchive it: *tar zxf jpegsrc.v6b.tar.gz*

4.  change to the working directory for the source: *cd jpeg-6b*

5.  configure the source for your platform: *./configure*

6.  find the make file created by the *configure* command: *./Makefile* and opeon in the text editor

7.  change the line: *CFLAGS= -O2 -I\$(srcdir)* to *CFLAGS= -arch ppc -arch i386 -O2 -I\$(srcdir)*

8.  build the library: *make*

9.  Install it in the default location (/usr/local): *sudo make install-lib* (this will install the header files and libjpeg.a)

10. return to the original directory: *popd*

### Universal PIL 

1.  first get the source and put it a working directory you choose: [http://effbot.org/downloads/Imaging-1.1.5.tar.gz](http://effbot.org/downloads/Imaging-1.1.5.tar.gz) -o Imaging-1.1.5.tar.gz

2.  open a Terminal window and change your working directory to the local of the archive file: *pushd \<you directory path here\>*

3.  unarchive it: *tar zxf Imaging-1.1.5.tar.gz*

4.  change to the working directory for the source: *Imaging-1.1.5*

5.  find the file used by Python to guide a build of an extension module: *setup.py* and open it in th text editor.

6.  change the line: *JPEG_ROOT = None* to *JPEG_ROOT = libinclude(\"/usr/local\")* (the place we put the jpeg library and header files)

7.  build the Python extension: *sudo python setup.py build_ext -i* (the sudo is necessary if you don\'t have the requried permissions for the /usr/local directories)

8.  run the self tests to ensure it all worked: *python selftest.py* and you should see the output: *55 tests passed.*

9.  if it passes all 55 tests, install the PIL module: *sudo python setup.py install*

10. We are done. return to the starting point *pushd* and we should have a working installation of PIL.

### A few More 

\"It just goes to show you\--there\'s always *something*\"

- \-- Roseanne Roseannadanna (Gilda Radner) from Saturday Night *LIVE*

Each library has its own tricks but there are some standard way of changing the build environment and paramters without making permanent changes to the files. Why didn\'t I use them above? Because, just as the famous saying for that *other* language (hint: PERL) says: *there\'s more than one way to do it\" and this is about techniques and tricks, not efficiency for now.*

- Most make files use standard variable names for their configuraiton parameters and setting those same variables in the shell environment (either permanently or for that shell) will override them.

- For example we could have set the CFLAGS variable in our shell after the

configure *command but before the* make *command to compile and link libjpeg as Universal build. Of course if the make file also sets a value for that paramter in the make file, then setting our own value will mask that and the build operation may not go as planned. we would set it just for the shell session thus* CFLAGS=\"\--arch ppc -arch i386 \" (note: the space at the end is important as these values may be followed by others for the individual make commands and without the space, the command line may become garbled.

Some build \'recipes\' are just not easy to modify because they are inscrutable due to complexity or they were not deisgned to be built in optional ways without permanent changes. Freetype2, because it uses the Jam tool, is one such example.

\[Reader note: Copying the files /usr/share/libtool/config.sub and config.guess into your build directory will cause the ./configure script to work properly for jpeg-6a and freetype2\]

\[Note on building PIL for Intel Macs: ppc libraries for zlib are not included by default in some versions of OS X. You will either have to install universal zlib libraries yourself or configure distutils to only build for the i386 architecture. You can do the latter by removing all references to \"-arch ppc\" from lib/pythonX.Y/config/Makefile. This procedure works if using the Python installed from python.org which resides by default in /Library/Frameworks/Python.framework/Versions/Current (not the system python).\]

\[Note on building PIL for Snow Leopard: you have to build a 64bit version using -arch x86_64. Otherwise you will get the error: The \_imaging C module is not installed.\]
