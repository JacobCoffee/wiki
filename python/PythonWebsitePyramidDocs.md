# PythonWebsitePyramidDocs

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Welcome to Pyramid 

Pyramid is the internal website templating system used to build the python.org pages. (It is not connected to the Pyramid web framework, formerly named BFG, that\'s used with Pylons.)

Pyramid uses Nevow as its templating system and YAML as the format for its file based data. At the moment, Pyramid is closely tied with the python.org redesign project and is being used to build the site at [http://www.python.org](http://www.python.org). See [PythonWebsitePyramidUsersGuide](PythonWebsitePyramidUsersGuide) for more information.

Pyramid has been tested on Debian, Ubuntu and Windows XP.

## Obtaining Pyramid 

To check out and install pyramid:

    svn co svn://pyramid.pollenation.net/pyramid/trunk pyramid-trunk
    cd pyramid-trunk
    python setup.py build
    sudo python setup.py install

## Requirements 

Pyramid requires Python 2.4.

Pyramid also requires the following modules.

Important: Use the links at the bottom of this document to obtain the correct versions of the required packages:

- Zope Interfaces (required by Twisted)
- Twisted (I generally install the sumo package or see links below)
- Nevow (optionally use the egg in the PYTHONPATH set by exportpathCHANGEME.sh, but this is only for nevow 0.5.0)
- docutils (see links below)
- syck and pysyck (see links below)
- Beautiful Soup (see links below)
- xmldiff if you want to run the tests.

To install the Python packages (all but syck), do this:

    python setup.py build
    sudo python setup.py install

To install syck, use the usual configure/make/install:

    ./configure
    make
    sudo make install

## Using Eggs 

See [PythonWebsitePyramidEggs](PythonWebsitePyramidEggs) for information on installing from eggs (tho I don\'t know if this is up to date).

## Windows Users 

Should be able to get away with Twisted Sumo windows installer [http://twistedmatrix.com/projects/core/](http://twistedmatrix.com/projects/core/) (which includes zope interfaces as well as twisted and twisted web) and [PySyck](./PySyck.html) windows installer from xitology (which includes syck windows build)

## Testing 

XXX: Apparently, the exportpathCHANGEME.sh script is no longer used?

Once everything is installed, update the exportpathCHANGEME.sh script to point to your install location and try from the top pyramid subversion source directory:

    python pyramid/test/tests.py

XXX: Three tests are failing right now. I do know xmldiff is being used right now, but I don\'t know the accuracy of the rest.

This should pass nicely. (actually it may not as different installations spit out html attributes in different orders.. The unittests are being changed to perform xmldiff\'s to get around this - in the mean time as long as the diff that you see when you run the script looks very similar you should be ok). Note.. this is really a regression test rather than a unit test. The second test will probable show differences depending on what version of docutils that you are using.

## Usage 

For python.org-specific instructions, take a look at [http://www.python.org/dev/pydotorg/website/](http://www.python.org/dev/pydotorg/website/).

If you have installed pyramid you should be able to use build.py as follows:

    python <PATHTOPYRAMID>/pyramid/build.py -d testdata -o testout -v -R<rebuilddirs>

Be warned that the testout folder is emptied before being used. It won\'t delete any folders with .svn files in them. It will create the output folder if it doesn\'t already exist.

The basic instantwebserver works ok but needs fixing as it doesn\'t add a slash at the end of urls (anyone know how to do this?). When using instantwebserver, point your browser to [http://localhost:8000/](http://localhost:8000/)

Beginner\'s documentation is at:

[https://svn.python.org/www/trunk/beta.python.org/resources/docs/readme.rst](https://svn.python.org/www/trunk/beta.python.org/resources/docs/readme.rst)

The documentation has some python.org specific stuff in it but that is a good thing at the moment.

## Debugging in Wing IDE 

To debug pyramid in Wing IDE, set up a project, add pyramid (or a copy of it) as the \"main debug file\" and set the parameters and starting directory in the File Properties (right click on file or file\'s name in project view). This can help point at problems when running w/ -V doesn\'t provide enough info.

XXX: Are these \*specific\* versions required, or are more recent versions OK? The Twisted Sumo distribution includes Twisted Core 2.2.0. The Docutils development snapshot is a moving target (see the next FIXME note below).

We should specify version ranges where applicable, and allow the latest packages where possible.

TP: I\'ll check on this..

## Zope Interfaces 

A requirement for Twisted

homepage [http://www.zope.org/Products/ZopeInterface](http://www.zope.org/Products/ZopeInterface)

download [http://www.zope.org/Products/ZopeInterface/3.1.0c1/ZopeInterface-3.1.0c1.tgz](http://www.zope.org/Products/ZopeInterface/3.1.0c1/ZopeInterface-3.1.0c1.tgz)

## Twisted & Twisted Web 

homepage [http://twistedmatrix.com/projects/core/](http://twistedmatrix.com/projects/core/)

download [http://tmrc.mit.edu/mirror/twisted/Twisted/2.0/Twisted-2.0.0.tar.bz2](http://tmrc.mit.edu/mirror/twisted/Twisted/2.0/Twisted-2.0.0.tar.bz2)

homepage [http://twistedmatrix.com/projects/web/](http://twistedmatrix.com/projects/web/)

download [http://tmrc.mit.edu/mirror/twisted/Web/0.5/TwistedWeb-0.5.0.tar.bz2](http://tmrc.mit.edu/mirror/twisted/Web/0.5/TwistedWeb-0.5.0.tar.bz2)

## Nevow 

homepage [http://divmod.org/trac/wiki/DivmodNevow](http://divmod.org/trac/wiki/DivmodNevow)

download [http://divmod.org/trac/attachment/wiki/SoftwareReleases/Nevow-0.7.0.tar.gz?format=raw](http://divmod.org/trac/attachment/wiki/SoftwareReleases/Nevow-0.7.0.tar.gz?format=raw)

## docutils

home page [http://docutils.sourceforge.net/](http://docutils.sourceforge.net/)

download [http://docutils.sourceforge.net/docutils-snapshot.tgz](http://docutils.sourceforge.net/docutils-snapshot.tgz)

## syck & pysyck 

You will need bison and yacc to build and install syck.

syck project page [http://rubyforge.org/projects/syck/](http://rubyforge.org/projects/syck/)

Download [http://rubyforge.org/frs/download.php/4492/syck-0.55.tar.gz](http://rubyforge.org/frs/download.php/4492/syck-0.55.tar.gz)

We\'re now using the pysyck build from xitology.org - it\'s being used for dumping and reading YAML. The latest version should soon be in the rubyforge repository but for the moment can be obtained from the link below.

pysyck interface: [http://xitology.org/pysyck](http://xitology.org/pysyck)

Download [http://xitology.org/pysyck/PySyck-0.55.1.tar.gz](http://xitology.org/pysyck/PySyck-0.55.1.tar.gz)

## Beautiful Soup 

Download version 2.1.1 or later from [http://www.crummy.com/software/BeautifulSoup/index.html#Download](http://www.crummy.com/software/BeautifulSoup/index.html#Download)

Home page [http://www.crummy.com/software/BeautifulSoup/](http://www.crummy.com/software/BeautifulSoup/)

## xmldiff from logilab 

If you are having problems getting pyramid to work, you might like to try the built in tests. The tests require comparing xml files and because of which we have another requirement for xmldiff

xmldiff [http://www.logilab.org/projects/xmldiff/documentation](http://www.logilab.org/projects/xmldiff/documentation)

Download [ftp://ftp.logilab.org/pub/xmldiff/xmldiff-0.6.7.tar.gz](ftp://ftp.logilab.org/pub/xmldiff/xmldiff-0.6.7.tar.gz)

The python2.4-xmldiff (or python2.3-xmldiff) packages on debian/ubuntu work.

Please note that some versions of docutils build slightly different html and as such the \'testing firstpythontest\' may fail but the system will still work. As long as the \'testing basic\' wokrks then the system should be ok (or at least a vast majority of the system). Typical errors that may show up in the firstpythontest are entity encoding errors or changes in id\'s on links (due to docutils version differences).

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite)
