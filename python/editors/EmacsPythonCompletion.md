# EmacsPythonCompletion

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Python Completion in emacs 

- new version 16/10-2003
  - now runs on windows, does not need rlcompleter
  - significantly simpler
  - now got install instructions for auto-load

I whipped up some support for completion of python code when using emacs, which basically completes based on the stuff in scope in the current interactive python session. It\'s rather crude, but seems to work rather nice for me at least.

Several uses are supported:

1.  hippie-expand support via try-complete-py-complete-symbol, just like the lisp-version, nice for the \[S-tab\] hungry.
2.  minibuffer-complete, pressing \[M-return\] brings up a minibuffer completion of the expression before point, usefull if you want to get an overview of your options.
3.  pressing \[f1\] brings up help on a python symbol before point (just what \"help(thingy)\") gives
4.  pressing \"(\" or \[f2\] tries to parse the preceeding tokens as a funtion or method, and retrieve the signature via the \"inspect\" module, and messages it to you
5.  pressing \",\" shows last signature.
6.  tries to work for both py-execute-buffer and py-execute-import-or-reload oriented work-styles.

TRICK: (4+5) is great for calling functions like:

- string.join

where I can \_never\_ remember whether it\'s the list or seperator first

Get it directly from SVN: [http://slog.dk/svn/home/jensen/emacs-lisp/addon/py-complete.el](http://web.archive.org/web/*/http://slog.dk/svn/home/jensen/emacs-lisp/addon/py-complete.el) (link to archived versions)

Feel free to suggest improvements, or to just improve the code yourself.

\-- Helge

- 2007-02-15 add

also check this: [Bash-like Tab Completion in Emacs python-mode](http://timchen119.blogspot.com/2007/02/bash-like-tab-completion-in-emacs.html)

------------------------------------------------------------------------

[CategoryEditors](CategoryEditors)
