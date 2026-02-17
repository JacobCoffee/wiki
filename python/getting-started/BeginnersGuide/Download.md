# BeginnersGuide/Download

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Downloading Python 

The official download page for Python is [python.org/downloads](https://python.org/downloads).

------------------------------------------------------------------------

On many systems Python comes pre-installed, you can try running the `python`{.backtick} command to start the Python interpreter to check and see if it is already installed. On windows you can try the `py`{.backtick} command which is a launcher which is more likely to work. If it is installed you will see a response which will include the version number, for example:

    Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.

If you don\'t see this, you will need to install Python on your system.

If the version number is Python 2.x.y (where `x`{.backtick} and `y`{.backtick} are any number) you are using Python 2 which is no longer supported and is not a good choice for development. You can try running `python3`{.backtick} to see if there is also a Python 3.x.y version installed, if not you\'ll want to install the latest version of Python.

If you do not have Python installed or need a newer version you can go to:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

which will provide a button to download an installer for your particular system. The Python documentation also has a detailed guide on how to install and setup Python here:

[https://docs.python.org/3/using/index.html](https://docs.python.org/3/using/index.html)

Below are some system specific notes to keep in mind.

### Windows 

On Windows the most stable build is available from the official download page

[https://www.python.org/downloads/](https://www.python.org/downloads/)

You should download and run the installer from that page to get the latest version of Python for your system. You can refer to the Python documentation for more details on the installation process and getting started:

[https://docs.python.org/3/using/windows.html](https://docs.python.org/3/using/windows.html)

### Mac 

For macOS 10.9 (Jaguar) up until 12.3 (Catalina) the operating system includes Python 2, which is no longer supported and is not a good choice for development. You should go to do the downloads page: [https://www.python.org/downloads/](https://www.python.org/downloads/) and download the installer.

For newer versions of macOS, Python is no longer included by default and you will have to download and install it. You can refer to the Python documentation for more details on the installation process and getting started:

[https://docs.python.org/3/using/mac.html](https://docs.python.org/3/using/mac.html)

### Linux 

On most Linux distributions Python comes pre-installed and/or available via the distribution\'s package managers. Below are some common examples, but refer to your specific distribution\'s documentation and package list to get the most up to date instructions.

If you\'d like to download and build Python from source (or your distribution\'s package manager does not include a version of Python you need) you can download a source tarball from the general download page: [https://www.python.org/downloads/](https://www.python.org/downloads/)

#### Red Hat, CentOS, or Fedora 

    dnf install python3 python3-devel

#### Debian or Ubuntu 

    apt-get install python3 python3-dev

#### Gentoo 

    emerge dev-lang/python

#### Arch Linux 

    pacman -S python3
