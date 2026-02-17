# A new pypi module

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Create a new package in python called pypi 

- PEP: XXX
- Title: Create a new package in python called pypi
- Author: Tarek Ziadé
- Discussions-To: Distutils SIG
- Status: Draft
- Python-Version: 2.6

## Abstract 

This PEP describes how the commands that are used to register and upload a package to PyPI can be extracted from distutils and put in a new independant package in Python called pypi, that would also describe the PyPI protocol.

## Motivation 

distutils is responsible for too many things, and the register and upload commands are completely standalone. In other words they can be extracted from distutils and placed into a new package that would also describe the protocol used by the PyPI server.

Secondly, there are a lot interactions in those two commands. They are interacting with the user when the .pypirc file is created, and they implement an authentication mecanism that pushes the user login and password values into the HTTP request. This is done by reading a clear text password in .pypirc.

The users have to call a very precise sequence of commands with setup.py in order to upload or even upgrade their packages.

Let\'s improve all of this by:

- improving password handling
- improving metadata controls
- providing a command line utility, independantly from setup.py
- clearly describe the PyPI protocol

The last point would let anyone implement this protocol for the client-side or the server-side, by using this package as a base.

## Improving password handling 

Currently, the password and the user are in clear text in .pypirc. This is a bit insecure. Let\'s make it an optional and if not provided let the user type it at the prompt when needed.

## Improving metadata controls 

When a package is uploaded at PyPI, there are several things that can be done on the client-side in order to control it.

- make sure the long_description compiles if it is written in reST
- make sure the author_email is the same that the email of the PyPI account in usage

A new variable in .pypirc can be added in order to block a registration or an upload if the metadata does not meet the minimum requirements:

    [distutils]
    ...
    strict-verification=true
    ...

From there, the command line utility will be able to decide if it should continue or not. The problem with the reST control is that it would require docutils.

## Providing a command line utility, independantly from setup.py 

Let\'s drop the setup.py command line to register and upload a package. The new pypi package can handle this as long as the package is pointed. A high-level script can be provided in the Scripts/ folder of Python, and a developer can use it to control, register or upload a package. And also to browse PyPI.

Here\'s a example of such a session:

        $ cd my.package
        $ pypi check
        Checking metadata...
        Warning : The 'url' metadata is missing
        Warning: The long_description seem to be in reStructuredText, 
        but does not compile

        $ pypi register -r tarek
        Registering the package using "tarek" account in .pypirc
        ...
        Registered !

        $ pypi upload 
        What kind of release do you want to upload ?
        Available releases:
            sdist   Source release
            bdist   Binary release
            ....

        Type the desired released, separated by a space [sdist] : _

        $ pypi passwd tarek
        Changing password for tarek
        What kind of hash (default: sha1) ? sha1
        Type password:
        Type password again:
        
        Password changed

The pypi command could also let you browse PyPI, like the Yolk project does (see [http://pypi.python.org/pypi/yolk](http://pypi.python.org/pypi/yolk))

Browsing capabilities using PyPI XML-RPC features : XXX TBD

## Clearly describe the PyPI protocol 

XXX TBD : describe the methods inmplemented in the [CheeseShop](CheeseShop)

## How ? 

A first refactoring was made a few months ago to allow users to handle several PyPI logins and servers in .pypirc ([http://bugs.python.org/issue1858](http://bugs.python.org/issue1858)) and the code responsible for .pypirc managment and for handling the registering and the upload were isolated.

The first action would be to create a new package called pypi and to copy the code from distutils, in order to make it work on its own.

The files to use are:

- distutils/config.py : the base class that handles .pypirc
- distutils/commands/register.py : the command that registers a package
- distutils/commands/upload.py : the command that uploads a package

We can add deprecated flags into distutils, just to warn people to use the new module instead.

XXX to be finished
