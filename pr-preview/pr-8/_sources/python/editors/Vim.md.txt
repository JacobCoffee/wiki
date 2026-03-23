# Vim

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Vi Improved 

VI Improved (Vim) is an improved version of the editor \"vi\", one of the standard text editors on UNIX systems. It has all the features you\'ll ever need from an editor, and probably three times that many more that you\'ll never use ![;-)](/wiki/europython/img/smile4.png%20";-)") The newer versions also include a \'vimdiff\' mode that you can use to diff and merge file(s). Oh, I didn\'t mention it\'s also scriptable in Python, and there\'s a graphical version: GVIM. Get it from [http://www.vim.org/](http://www.vim.org/).

Vim is also available in your favourite OS. Since version 6.0 it has folding. Folding makes your life easy when you have some long files.

You can download many scripts from [http://www.vim.org/](http://www.vim.org/) and learn new tips from the site [http://vim.wikia.com/wiki/Main_Page](http://vim.wikia.com/wiki/Main_Page)

Vim 7.0 (released mid-2006) includes the Intellisense-like omni-completion for several languages. Here is the latest version of [pythoncomplete](http://www.vim.org/scripts/script.php?script_id=1542).

### Configuring Vim 

You can automatically enable syntax coloring and automatic indentation for Python code by adding the following lines to your \~/.vimrc file:

    syntax on
    filetype indent plugin on

The following sections correspond to the guidelines from the [HowToEditPythonCode](../guides/HowToEditPythonCode) page.

#### Indentation 

A useful addition to Python source files is this comment:

    # vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

This may need the modeline option enabled in your `~/.vimrc`{.backtick} file:

    set modeline

(In Debian and Ubuntu, for example, the modeline option has been disabled for security reasons.)

The above `# vim: ...`{.backtick} text, when embedded in a source file, tells Vim that when the file is loaded, tabs are always expanded to spaces and that the width of each tab is four characters. Type the following in command mode to achieve the same effect:

    :set tabstop=8 expandtab shiftwidth=4 softtabstop=4

Or:

    :set ts=8 et sw=4 sts=4

If you want to do this automatically for all files identified as Python, add the following to `~/.vim/ftplugin/python.vim`. Create the directory and/or file if it does not already exist.

    set tabstop=8
    set expandtab
    set shiftwidth=4
    set softtabstop=4

#### Syntax Highlighting 

You may be lucky enough to have syntax highlighting already switched on in your version of Vim. If not, edit a `vimrc`{.backtick} file (either `/etc/vimrc`{.backtick} or, preferably,`.vimrc`{.backtick} in your home directory) and add the following:

    syntax on

If you use a dark background, this command may help adjust the default colours for better contrast:

    set background=dark

#### Alternative 

Some find that the methods described above do not work. An alternative method is adding\...

    set tabstop=8
    set expandtab
    set softtabstop=4
    set shiftwidth=4
    filetype indent on

\...to your `~/.vimrc`{.backtick} file. The first rule sets tab stops to [eight characters wide](http://docs.python.org/reference/lexical_analysis.html#indentation). The second converts tabs to white space. The third makes the Tab key indent by four spaces. `set shiftwidth`{.backtick} sets the width for autoindents. Finally, the last rule allows auto-indenting depending on file type. With this method, tab settings do not need to be set in your python file and the `# vim: ...`{.backtick} line in the template below is not needed.

#### A Simple Template 

You could copy the following simple template and save it to a file somewhere. Then, when you need to make a new source file, just copy it to the intended location with a name of your choice.

:::: 
::: 
``` 
#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

## vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
```
:::
::::

This contains useful UNIX-related information on the first line, and a docstring which can be used to describe what your program or module is about. As noted above, to work this requires modeline support to be enabled.

#### Scripting Vim with Python 

There is a presentation given by Sean Reifschneider about scripting Vim with Python: [Vim and Python: Two Great Tastes that Taste Great Together](http://www.tummy.com/Community/Presentations/) If you want to access the visual selection from Vim in Python read [http://www.tummy.com/journals/entries/jafo_20070301_035949](http://www.tummy.com/journals/entries/jafo_20070301_035949)

#### Links 

- Python-mode for Vim: [Screencast](http://www.youtube.com/watch?v=67OZNp9Z0CQ&feature=share)

- Some hints about configuring Vim: [Notes on using Vim with Python](http://www.vex.net/~x/python_and_vim.html)

- [Turning Vim into a modern Python IDE](http://sontek.net/turning-vim-into-a-modern-python-ide), 2011, Anderson (sontek)

- [VIM as Python IDE](http://blog.dispatched.ch/2009/05/24/vim-as-python-ide/), 2009-05-24, Alain M. Lafon

- [Python and vim: Make your own IDE](http://dancingpenguinsoflight.com/2009/02/python-and-vim-make-your-own-ide/), February 16, 2009 14:28, Samuel Huckins

------------------------------------------------------------------------

[CategoryEditors](CategoryEditors)
