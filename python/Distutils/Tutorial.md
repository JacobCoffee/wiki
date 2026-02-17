# Distutils/Tutorial

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Introduction to distutils 

I have recently used distutils for the first time and thought I would share what I have learned.

**Please note:** *I am not a pro. All this is based on my own hacking and struggling to get things to work. I am sure there will be alternative ways to do things and that I will make mistakes. Caveat Emptor.*

(Based on GNU/Linux)

## The layout of folders 

A proper layout of your files and folders can really save you trouble later on. I use this layout:

    top
    |-- package
    |   |-- __init__.py
    |   |-- module.py
    |   `-- things
    |       |-- cross.png
    |       |-- fplogo.png
    |       `-- tick.png
    |-- runner
    |-- MANIFEST.in
    |-- README
    `-- setup.py

- top - This is called the \"Distribution Root\". The very top of the tree is some arbitrary folder, perhaps in your home directory under pythondev. It doesn\'t matter.

- package - I call it this to indicate that it\'s where I am developing my package(s).

  *(Packages are simply folders with modules (py files) in them. They also have a special file called `__init__.py`{.backtick} so that Python will know that this folder is a package.)*

- package/things - This is where I will keep all my things. Here I have some image files, but you can put anything your module may need here. Naturally you can use any folder name you like.

- The other files are all in the root and will be described soon.

## UPDATE: How to add other files, other data and directories 

I have a tentative solution for when you need extra files and folders in your distributed tarball. This is surprisingly tricky to do. Please see the section at the end titled \"Other Files\"

## The files 

### runner

I assume that there will be a single script file that you will use to start your Python app. I call it \'runner\' (without the .py) in this example. It will import the actual package. Here is the code:

*runner*

    ##This will work in development on a relative folder basis
    ##It will then work when installed in site-packages on a target system
    ##where the runner script is in /usr/bin (or wherever)
    ##
    ##So, you don't need anything special - no fancy path tricks.

    import package.module

    package.module.start ()

### module.py

Next is the package. In this case there is only one module in the package (import package.module), so here is the module:

*module.py*

    import os, sys

    def determine_path ():
        """Borrowed from wxglade.py"""
        try:
            root = __file__
            if os.path.islink (root):
                root = os.path.realpath (root)
            return os.path.dirname (os.path.abspath (root))
        except:
            print "I'm sorry, but something is wrong."
            print "There is no __file__ variable. Please contact the author."
            sys.exit ()
            
    def start ():
        print "module is running"
        print determine_path ()
        print "My various data files and so on are:"
        files = [f for f in os.listdir(determine_path () + "/things")]
        print files
        
    if __name__ == "__main__":
        print "Decide what to do"

This uses the magic variable `__file__`{.backtick} that will return the path and name of the module. Without it you would have to jump through some hoops to locate the module on any given distro or O/S.

- *(If you can find this in the Python docs, then your grep-foo is better than mine. I found it by pouring through other Python apps in the site-packages folder of python2.4)*

It shows that it can find the data files in the things folder.

### \`\_\_init\_\_.py\` 

The `__init__.py`{.backtick} file is empty.

### README 

The README file is named that way because it\'s one of the ways that distutils automatically looks for it. You should put details about your app into it. It\'s not a required file.

### MANIFEST.in 

The MANIFEST.in file took me a while to understand. It\'s the file that distutils uses to collect *all* the files in your project that will go into the final installer tarball (the file that gets distributed).

**NB:** whatever is in MANIFEST.in will be in your installer. Whatever is **not** in there, will **not** be in your installer.

Shortly, in your setup.py file, you will see other references to the various files in your project. It seems redundant to refer to all the files you want twice, but this is a fact: MANIFEST.in == what will go **into** your installer.

Here is the file:

*MANIFEST.in*

    include runner README
    recursive-include package/things *

It has a limited syntax (see the docs),but basically:

- *include* - pick up files (by glob or name) relative to the root.

- *recursive-include path file* - pick up files (by name or glob) recursively under the given path.

You do not have to include any .py files in your package-root folder. You do have to include the runner script because it has no .py extension. (I am not sure if it would pick up .py files in the root.)

### setup.py

Finally we get to the setup.py file:

*setup.py*

    from distutils.core import setup

    #This is a list of files to install, and where
    #(relative to the 'root' dir, where setup.py is)
    #You could be more specific.
    files = ["things/*"]

    setup(name = "appname",
        version = "100",
        description = "yadda yadda",
        author = "myself and I",
        author_email = "email@someplace.com",
        url = "whatever",
        #Name the folder where your packages live:
        #(If you have other packages (dirs) or modules (py files) then
        #put them into the package directory - they will be found 
        #recursively.)
        packages = ['package'],
        #'package' package must contain files (see list above)
        #I called the package 'package' thus cleverly confusing the whole issue...
        #This dict maps the package name =to=> directories
        #It says, package *needs* these files.
        package_data = {'package' : files },
        #'runner' is in the root.
        scripts = ["runner"],
        long_description = """Really long text here.""" 
        #
        #This next part it for the Cheese Shop, look a little down the page.
        #classifiers = []     
    ) 

- *name* becomes the name of the installation tarball.

- *version* gets appended to the end of the tarball name.

- packages = \[ \] A list naming **all** the packages you want to include. *(I am unsure about how to create multiple packages. The docs are a little too concise and I read too fast.)*

- package_data = { } A dictionary where the key (\'package\') is related to the list of files (in things/). I read this as saying \"The package named \'package\' needs the files in \[list\]\"

- scripts = \[ \] A script(s) to be installed into standard locations like /usr/bin. If you include a path, you can control where they go. in this case I want /usr/bin/runner to be available on the user\'s system.

- \"long_description\" may be valid [ReStructuredText](./ReStructuredText.html) which will be turned into HTML when displayed at the Cheese Shop.

## Making the installation tarball 

Well, that\'s the lot. It\'s quite simple really, as long as you keep to the pattern. If you want extra folders and sub-packages and so forth, it gets a little hairy. But, I suppose, if you want all that then you will have no trouble extending it from this tutorial.

To make the installation tarball, you simply run:

    python setup.py sdist

That will crank through all the files in your MANIFEST.in and build the tar.gz file in a folder called dist off your root.

Look for errors. You might have to fix lines in your MANIFEST.in file.

Here is what I see:

*output*

    distutils:$ python setup.py sdist
    running sdist
    reading manifest file 'MANIFEST'
    creating appname-100
    creating appname-100/package
    creating appname-100/package/things
    making hard links in appname-100...
    hard linking README -> appname-100
    hard linking runner -> appname-100
    hard linking setup.py -> appname-100
    hard linking package/__init__.py -> appname-100/package
    hard linking package/module.py -> appname-100/package
    hard linking package/things/cross.png -> appname-100/package/things
    hard linking package/things/fplogo.png -> appname-100/package/things
    hard linking package/things/tick.png -> appname-100/package/things
    tar -cf dist/appname-100.tar appname-100
    gzip -f9 dist/appname-100.tar
    removing 'appname-100' (and everything under it)

## Testing the tarball 

I perform these steps:

    cd dist
    tar xzf appname-100.tar.gz 
    cd appname-100
    sudo python setup.py install
    password:######
    running install
    running build
    running build_py
    running build_scripts
    running install_lib
    running install_scripts
    changing mode of /usr/bin/runner to 755

Then I cd over to /usr/lib/python2.4/site-packages and have a look for a folder named \'package\'. I also try to run \'runner\' and see what ensues.

It should look (something) like this:

    distutils:$ runner
    module is running
    /usr/lib/python2.4/site-packages/package
    My various data files and so on are:
    ['cross.png', 'fplogo.png', 'tick.png']

## Registering with the Cheese Shop (PyPI) 

The Cheese Shop is a repository of Python apps. You can add your app to it quite easily, I was surprised how quickly this worked. ( Requires Python 2.3 or later )

Make sure you have the right meta-data in your setup.py file. Please consult the Python Docs for this info. Here is a sample of what you should include:

        classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: X11 Applications :: GTK',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Topic :: Desktop Environment',
          'Topic :: Text Processing :: Fonts'
          ]

Then you type:

    $ python setup.py register
    running register
    We need to know who you are, so please choose either:
     1. use your existing login,
     2. register as a new user,
     3. have the server generate a new password for you (and email it to you), or
     4. quit
    Your selection [default 1]:  2
    Username: putyournamehere
    Password:
     Confirm:
       EMail: youremailhere
    You will receive an email shortly.
    Follow the instructions in it to complete registration.

- If you have an account, obv, choose 1.
- If you chose 2, you will get an email; read and do.
- I then re-did the register command, and logged-in via option 1. Not sure if this was needed.

After all that, you can quickly find you app in the Cheese Shop via your browser, or sign up for their RSS feed.

## Submittting to the Cheese Shop (PyPI) 

Requires Python 2.5 or later:

    distutils:$ python setup.py sdist upload

TODO: need a sample output here

To GPG-sign the upload, use:

    distutils:$ python setup.py sdist upload --sign

TODO: need a sample output here

## Other Files 

**WARNING** I have found a problem with this approach that causes all the data directories to be installed to the /usr/ directory. I have no idea why and not much help seems forthcoming. I will update when I get a clue. **UPDATE TO WARNING** Okay, I think I have fixed the problem, new code has been added to the example below.

Jan 4 2008. When you need *other* stuff in your tarball (.py files included) and distutils is causing your brain to segfault, this may help you. Robin Dunn (he of wxPython fame) pointed me at his source code and I spent a little time hacking it.

I\'ll use Fonty Python as the example - I\'ll show you the tree and explain it a little, then I\'ll follow that with the code that does the job.

### The tree 

Here\'s the Fonty Python tree (as it stands, leaning wildly, right now). \'trunk\' is the **distribution root**. I have trimmed it somewhat.

    trunk:$ tree
    |-- COPYING
    |-- README
    |-- fontypython
    |-- fontypythonmodules
    |   |-- __init__.py
    |   |-- cli.py
    |   |-- help
    |   |   |-- README
    |   |   |-- common
    |   |   |   |-- README
    |   |   |   |-- fp_ticking.png
    |   |   |   `-- logo_dec_2007.png
    |   |   |-- en
    |   |   |   |-- README
    |   |   |   |-- fp_1to8.png
    |   |   |   `-- help.html
    |   |   `-- fr
    |   |       |-- README
    |   |       |-- fp_1to8.png
    |   |       `-- help.html
    |   |-- i18n.py
    |   |-- locale
    |   |   |-- fr
    |   |   |   `-- LC_MESSAGES
    |   |   |       `-- all.mo
    |   |   `-- it
    |   |       `-- LC_MESSAGES
    |   |           `-- all.mo
    |   |-- pofiles
    |   |   |-- README
    |   |   |-- fp_all.po
    |   |   |-- fr_all.merged.po
    |   |   |-- it_all.merged.po
    |   |   `-- who_did_what
    |   |-- things
    |   |   |-- README
    |   |   `-- tick.png
    |   `-- wxgui.py
    |-- fp
    `-- setup.py

So, there are .py files, text files, locale files, images and html files. I want them **all** in the tarball in the right order.

### The MANIFEST.in file 

    include fontypython fp README COPYING
    recursive-include fontypythonmodules/pofiles *
    recursive-include fontypythonmodules/things *
    recursive-include fontypythonmodules/locale *
    recursive-include fontypythonmodules/help *

I tell it to recurse all those subfolders. I include \'fp\', \'fontypython\', \'README\' and \'COPYING\' because they are in the root - perhaps there\'s a better way to do it, but this works.

### The Magic Code 

The magic stuff is in the two functions called **opj** and **find_data_files** that you put in your **setup.py** file. They work together to build a list of all the files in a given path. This list is in the right shape for distutils to swallow. You pass it in via the data_files variable in the setup() call.

(Ignore all my fontypythonmodules dot stuff - that\'s just to get strings from another module.)

After making these changes, a normal **python setup.py sdist** works without oddball errors and the tarball has all the files you\'d expect it to.

    import os, sys, glob, fnmatch

    ## Added 10 Jan 2008
    from distutils.core import setup, Extension
    import distutils.command.install_data

    ## Code borrowed from wxPython's setup and config files
    ## Thanks to Robin Dunn for the suggestion.
    ## I am not 100% sure what's going on, but it works!
    def opj(*args):
        path = os.path.join(*args)
        return os.path.normpath(path)

    ## Added 10 Jan 2008
    # Specializations of some distutils command classes
    class wx_smart_install_data(distutils.command.install_data.install_data):
        """need to change self.install_dir to the actual library dir"""
        def run(self):
            install_cmd = self.get_finalized_command('install')
            self.install_dir = getattr(install_cmd, 'install_lib')
            return distutils.command.install_data.install_data.run(self)

    def find_data_files(srcdir, *wildcards, **kw):
        # get a list of all files under the srcdir matching wildcards,
        # returned in a format to be used for install_data
        def walk_helper(arg, dirname, files):
            if '.svn' in dirname:
                return
            names = []
            lst, wildcards = arg
            for wc in wildcards:
                wc_name = opj(dirname, wc)
                for f in files:
                    filename = opj(dirname, f)

                    if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
                        names.append(filename)
            if names:
                lst.append( (dirname, names ) )

        file_list = []
        recursive = kw.get('recursive', True)
        if recursive:
            os.path.walk(srcdir, walk_helper, (file_list, wildcards))
        else:
            walk_helper((file_list, wildcards),
                        srcdir,
                        [os.path.basename(f) for f in glob.glob(opj(srcdir, '*'))])
        return file_list

    ## This is a list of files to install, and where:
    ## Make sure the MANIFEST.in file points to all the right 
    ## directories too.
    files = find_data_files('fontypythonmodules/', '*.*')

    from distutils.core import setup

    setup(name = "fontypython",
        version = fontypythonmodules.fpversion.version,
        description = fontypythonmodules.strings.description,
        author = "Donn.C.Ingle",
        author_email = fontypythonmodules.strings.contact,
        license = "GPL-3.0",
        url = "https://savannah.nongnu.org/projects/fontypython/",
        packages = ['fontypythonmodules'],
        
        data_files = files,
        
        ## Borrowed from wxPython too:
        ## Causes the data_files to be installed into the modules directory.
        ## Override some of the default distutils command classes with my own.
        cmdclass = { 'install_data':    wx_smart_install_data },
        
        #'fontypython' and 'fp' are in the root.
        scripts = ["fontypython", "fp"],
        long_description = fontypythonmodules.strings.long_description,
        classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: X11 Applications :: GTK',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Topic :: Desktop Environment',
          'Topic :: Text Processing :: Fonts'
          ]
    )

## NEW VERSION OF def walk_helper() 

Given that you may want to exclude files that contain *more* than just .pyc in them, we need something handy. Replace the def in the code above with this code.

    ## A list of partials within a filename that would disqualify it
    ## from appearing in the tarball.
    badnames=[".pyc","~","no_"]
    def walk_helper(arg, dirname, files):
        if 'CVS' in dirname: ## ADD/CHANGE as you need here too.
            return
        names = []
        lst, wildcards = arg
        for wc in wildcards:
            wc_name = opj(dirname, wc)
            for f in files:
                filename = opj(dirname, f)
                #if ".pyc" not in filename:
                ## This hairy looking line excludes the filename
                ## if any part of one of  badnames is in it:
                if not any(bad in filename for bad in badnames):
                    if fnmatch.fnmatch(filename, wc_name) and not os.path.isdir(filename):
                        names.append(filename)
        if names:
            lst.append( (dirname, names ) )

The secret is the list **badnames** which you can fill as you please.

## Fin 

I hope this helps someone. Happy coding.

[DonnIngle](mailto:donn.ingle@gmail.com)

------------------------------------------------------------------------

[CategoryFaq](CategoryFaq) [CategoryDistutilsCookbook](CategoryDistutilsCookbook)
