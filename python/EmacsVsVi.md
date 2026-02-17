# EmacsVsVi

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Emacs vs. Vi 

Both of these editors support many fundamental virtues of text editors such as extensive syntax highlighting, collapsible functions, spell checking, macros, undo-redo, multiple document editing, and a large support community. They are both free, Open Source, mature and well developed pieces of software. But\...while both [Emacs](EmacsEditor) and [Vim](Vim) are considered powerful text editors, both capable of providing many of the same feature lists for general editing commands, the primary difference between these editors is the fundamental philosophy behind their design, and more to the point, the types of workflow that they were originally designed to handle. A search online for \"philosecurity ninja or pirate\" will produce a fun read on Vi creator Bill Joy and Emacs creator Richard Stallman. Because of the major design differences between these editors, emac/xemac extensions to emulate vi and vim are readily available online. For those more interested in personal versatility and combining the best attributes of both editors, there is information provided at the bottom of this wiki under the heading \"More Tips\".

At first, Vi (and its popular variant [Vim](Vim)) were considered mere small text editors built for speed with their focus on editing text quickly, but as they\'ve matured have become considered to be on par with emacs/xemacs. Ultimately, these editors may have different pros and cons depending primarily on your style and workflow needs. For instance, \"Vi\" and [Vim](Vim) starts much faster than [Emacs](EmacsEditor) and their usual workflow assumes that you often will both enter through and exit from them alone. [Vim](Vim) has matured to using a tabbed interface which can be used to edit multiple files very quickly, while [Emacs](EmacsEditor) are based more on the assumption that you\'ll be working in one spot for a more extended period of time.

Historically, among sysadmins, *vi*/*vim* has tended to be the preferred software, while *emacs*/*xemacs* has tended to be favored more by programmers. This is not very surprising when you compare the typical editing needs of sysadmins v/s programmers to the relative merits of the two different editors. For a VERY detailed explanation of why this has been the case and the pros and cons of each editor, visit [Emacs for Sysadmins](http://devopsanywhere.blogspot.com/2011/11/emacs-for-sysadmins.html)

Commonly, systems administrators are working on many different machines, in varying states of installation, configuration and repair. They are making relatively quick edits to many different files. An editor with a quick load time, blazing keyboard efficiency (with the right expertise) and few library or other dependencies is essential. Preferably it will be the editor that virtually every version of UNIX includes by default. It is even, occasionally, handy that the editor be able to fall back on an old fashioned line editing mode when even the terminal emulation subsystem is non-functional.

Programmers, on the other hand, tend to work extensively on large complex sets of related files. However they tend to have all of them located on one single machine (usually checked out of a version control system *en masse*). For programmers the overhead of starting a larger, slower, more complex editor is amortized over their usage. They may have the same instance of the editor up for weeks or months at a time, closing and opening buffers as necessary. Having an editor support a full programming language internally is important to many programmers, as they need IDE (integrated development environment) features and tools like *ediff* and *emerge* (for comparing and merging different versions of a file, for example).

Of course this generalization can fail us. Many programmers started as, or spent stints as systems administrators and developed a preference for *vi* over *emacs.* A modern version of *vim* can support almost any of the features one would expect of *emacs.* (*including* a full programming language \[python\] available for use in vim, but it tends to be less integrated and feel less natural for programming editing than Elisp). In contrast, many people feel uncomfortable with *vi\'s* notorious \"modal\" paradigm. They never become accustomed to \"command\" vs. \"insert\" or \"replace\" modes and often consider the very notion to be atavistic.

Helpful Tips:

- With emacs/xemacs one can access the vi keybindings use the command: **M-x viper** (That\'s \[Alt\]+\[x\]viper\[Enter\] or \[Esc\]\[x\]viper\[Enter\] \-\-- either should work, but the latter will work on terminals/keyboards that don\'t have an \[Alt\] key).

- To emulate vim features such as visual selection and text objects, the extensible vi layer \"[Evil](http://emacswiki.org/emacs/Evil)\" is available on emacswiki.org.

- In *vim* use the *ex*-mode command **:syntax on** to enable syntax highlighting (which is often configured to be off by default).

- To learn the basics of *vim* very quickly run the command *vimtutor* (it\'s a set of macro files that run in *vim* and teach one how to use it).

- To learn the rudiments of *emacs* use: **C-h, t** (from inside the editor of course). (That\'s \[Ctrl\]+\[h\] and then \[t\]). This will start the tutorial system that\'s written in emacs\' \"elisp\" version of the Lisp programming language.

Ultimately the choice of a text editor is a highly personal one, so flame wars on the topic of vi vs. emacs are very common and often considered rather frivolous, but what\'s important is that you find what works best for you. Try them for yourself, and perhaps take Bryan Berry\'s advice to heart, \"Using vi is like being in a relationship, you are involved. Using Emacs is like a marriage, you are committed, in large part because there is so much to learn.\"

------------------------------------------------------------------------

[CategoryEditors](CategoryEditors)
