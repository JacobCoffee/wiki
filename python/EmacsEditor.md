# EmacsEditor

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Emacs 

Emacs (the major flavors being [GnuEmacs](GnuEmacs) and XEmacs) is a text editor which come with good support for writing Python code. Each has its strengths and weaknesses, but in general either provide very nice environments for the Python programmer.

## Tools for Python coders 

Please [get involved](http://mail.python.org/mailman/listinfo/python-mode) if you want to help.

Some tools have been written for using Python from Emacs:

- [python-mode.el](http://launchpad.net/python-mode)

  - Addresses a lot of languages specific features, navigates nested blocks, deals with different Python versions and flavors etc.

    How to setup a complete IDE around python-mode.el was shown at [EuroPython 2013](http://www.youtube.com/watch?v=0cZ7szFuz18If). Other approaches relying on company-mode, Pymacs, ropemacs and pycomplete are known to work likewise

- python.el of Emacs 22. For a version with fixes and enhancements (as of 2006-06) and one that works with Emacs 21, see [http://www.loveshack.ukfsn.org/emacs](http://www.loveshack.ukfsn.org/emacs).

- python.el of Emacs 24.2.

- Emacs GUD PDB, support for sourcelevel debugging of Python code in Emacs. (Note: thanx to Ganesan R: Create the following script with the file name as \"pdb\" in your path so emacs can find pdb and default to filename arguments in the current dirctory: exec python /usr/lib/python2.3/pdb.py \"\$@\")

- [Pymacs(download)](http://www.iro.umontreal.ca/~pinard/pymacs/Pymacs.tar.gz), an extension for allowing Emacs users to extend Emacs using Python, where they might have traditionally used Emacs LISP. \' There are also [PyMacs notes on the Emacs wiki.](http://www.emacswiki.org/cgi-bin/wiki.pl?cgi-bin/wiki.pl%3FPyMacs "EmacsWiki")

- [ropemacs](https://github.com/python-rope/rope) is a plugin for performing python refactorings in emacs. It uses rope library and pymacs.

- [Emacs Language Sensitive Editor (ELSE)](http://home.exetel.com.au/peterm), an template-based minor mode for Emacs, with templates for Python.

- [OO-Browser](http://sourceforge.net/projects/oo-browser/), an Emacs class browser for object-oriented languages with support for Python.

- The [emacspeak audio desktop](http://www.cs.cornell.edu/home/raman/emacspeak) is a speech interface that allows visually impaired users to interact independently and efficiently with the computer. It has editing support for interactive Python development. Features aural highlighting, structured browsing and debugging.

## Support for C Python core developers 

Both Emacs and XEmacs have support for developers hacking on the Python C code itself. If you\'re developing Python 2.x, just use the standard `python`{.backtick} style that comes with c-mode. If you\'re hacking on Python 3.x, you\'ll want to add the following code to your `.emacs`{.backtick} file (given by [Georg Brandl](http://mail.python.org/pipermail/python-dev/2008-May/079582.html)):

    (c-add-style
      "python-new"
      '((indent-tabs-mode . nil)
        (fill-column      . 78)
        (c-basic-offset   . 4)
        (c-offsets-alist  . ((substatement-open . 0)
                             (inextern-lang . 0)
                             (arglist-intro . +)
                             (knr-argdecl-intro . +)))
        (c-hanging-braces-alist . ((brace-list-open)
                                   (brace-list-intro)
                                   (brace-list-close)
                                   (brace-entry-open)
                                   (substatement-open after)
                                   (block-close . c-snug-do-while)))
        (c-block-comment-prefix . "* "))
      )

    ;; This is a very crude hook that auto-selects the C style depending on
    ;; whether it finds a line starting with tab in the first 3000 characters
    ;; in the file
    (defun c-select-style ()
       (save-excursion
         (if (re-search-forward "^\t" 3000 t)
             (c-set-style "python")
           (c-set-style "python-new"))))
    (add-hook 'c-mode-hook 'c-select-style)

**Note:** *We should try to get the style into upstream c-mode.*

## Other resources 

- [The Emacs Wiki](http://www.emacswiki.org/emacs/SiteMap), a good starting place. Look for relevant articles:

  - [PythonProgrammingInEmacs](http://emacswiki.org/emacs/PythonProgrammingInEmacs).

  - [ProgrammingWithPythonModeDotEl](http://emacswiki.org/emacs/ProgrammingWithPythonModeDotEl).

- [GnuEmacs web page](http://www.gnu.org/software/emacs/emacs.html).

- [XEmacs web page](http://www.xemacs.org/).

------------------------------------------------------------------------

[CategoryEditors](CategoryEditors)
