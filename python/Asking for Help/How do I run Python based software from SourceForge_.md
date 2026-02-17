# Asking for Help/How do I run Python based software from SourceForge?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# How do I run Python based software from SourceForge? 

There isn\'t a straightforward answer to this question because projects on SourceForge often provide software both in source form as well as in binary (executable) form. Consider the MySQL for Python [packages](http://sourceforge.net/project/showfiles.php?group_id=22307), available via the \"Download\" link on the [project page](http://sourceforge.net/projects/mysql-python/): in this case, you\'ll choose `mysql-python`{.backtick} and be presented with a [list of files](http://sourceforge.net/project/showfiles.php?group_id=22307&package_id=15775) (under \"Filename\").

- If you use Windows, you\'ll probably only need to download and run the executable installers (ending in `.exe`{.backtick}).

- If you use another platform, at least for other packages there might be similar binary packages (ending in `.rpm`{.backtick} or `.deb`{.backtick}, for example) which you would then install using the system\'s package manager.

- For files ending in `.egg`{.backtick} you can use `easy_install`{.backtick} to install the software and make it available on your system.

- For archive files ending in `.zip`{.backtick}, `.tar.gz`{.backtick} or `.tgz`{.backtick}, `.tar.bz2`{.backtick} or `.tbz2`{.backtick}, you need to unpack the software and build it from the sources, typically.

Building files from source (the last alternative above) can be tricky, but the general procedure is usually something like this:

1.  Inspect the archive file to see what the unpacked file will produce: you don\'t want the unpacking process to put files all over the place. For example:

         unzip -l package-1.0.zip
         tar ztf package-1.0.tar.gz
         tar jtf package-1.0.tar.bz2

2.  If the output of the above suggests that the files inside the archive will appear in a common directory (`package-1.0`{.backtick}, for example) then move on to the next step. Otherwise, make a new directory and move into it:

         mkdir package-1.0
         cd package-1.0

3.  Now unpack the archive using one of the following:

         unzip package-1.0.zip
         tar zxf package-1.0.tar.gz
         tar jxf package-1.0.tar.bz2

    If you created a new directory, you may need to refer to the archive in the parent directory (`../package-1.0.zip`{.backtick}, for example). You can skip the next step, though.

4.  Enter the root directory of the package, just created when you unpacked the archive:

         cd package-1.0

Now read the documentation! There will probably be a `README`{.backtick} or `INSTALL`{.backtick} file in the directory - this will explain the rest of the installation procedure.

- Some software can be run straight from the unpacked archive - this will usually be mentioned in the documentation, but it can be quite common for games written using [PyGame](PyGame) to have a `run_game.py`{.backtick} (or `run_game.pyw`{.backtick}) file, and you can just run that with `python`{.backtick}.

- Other software will provide a `setup.py`{.backtick} program which can be used to install the software.

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
