# DocutilsSprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

(For the Docutils sprint at [PyCon2007](../conferences/pycon/PyCon2007), see [PyCon2007/DocutilsSprint](../conferences/pycon/PyCon2007/DocutilsSprint). For the Docutils sprint at [PyCon2006](../conferences/pycon/PyCon2006), see [PyCon2006/Sprints/DocutilsSprint](../conferences/pycon/PyCon2006/Sprints/DocutilsSprint).)

## Preliminaries 

PyConDC2004 is over. See [A Week at PyCon DC 2004](http://starship.python.net/~goodger/pycon_dc_2004/) for a narrative account of events.

For introductory information and information about the other sprints going on at [PyConDC2004](../conferences/pycon/PyConDC2004), please see [SprintPlan2004](./SprintPlan2004.html).

We also had a birds-of-a-feather session; see [DocutilsBof](DocutilsBof).

Also see the [Docutils home page](http://docutils.sourceforge.net) and the [reStructuredText home page](http://docutils.sourceforge.net/rst.html).

### Duration 

The sprints at [PyConDC2004](../conferences/pycon/PyConDC2004) were held from March 20 (Saturday) through March 23 (Tuesday), for a total of 4 days. I was there for all 4 sprint days, and sprinters joined in as they were able.

Please feel free to comment here or [email me](mailto:goodger@python.org).

### Cost 

There was no cost to attend the sprints beyond being present.

### Sprinters 

Everyone was welcome! No prior Docutils hacking experience was required. Participants were either experienced Python programmers, or interested in documentation.

Here are the sprinters who attended:

- [David Goodger](mailto:goodger@python.org) (coach)

- [Ollie Rutherfurd](mailto:oliver@rutherfurd.net) (Saturday and Sunday)

- [Fred Drake](mailto:fdrake@acm.org) (Saturday)

- [Ian Bicking](mailto:ianb@colorstudy.com) (Saturday, Monday, & Tuesday)

- [Aahz](mailto:aahz@pythoncraft.com) (All four days)

- [Edward Loper](mailto:edloper@gradient.cis.upenn.edu) (Sunday through Tuesday)

- [Tracy Ruggles](mailto:tracer@axiomfire.com) (Sunday & Tuesday?)

- [Matt Gilbert](mailto:gilbert@voxmea.net) (All four days)

- [Steve Holden](mailto:sholden@holdenweb.com) (Saturday and Sunday)

- Bill Sconce (all four days)

- Andrew Kuchling (Saturday)

- Reggie Dugard (Sunday through Tuesday)

- Mike Orr (Monday)

- Lloyd Kvam (Tuesday)

- Laura Creighton (Sunday through Tuesday)

- Jacob Hallen (Sunday through Tuesday)

### Sponsorship 

This sprint and my participation at [PyConDC2004](../conferences/pycon/PyConDC2004) were sponsored by Silver Sponsor [Wing IDE (Archaeopteryx Software)](http://WingIDE.com), the [Python Software Foundation (PSF)](http://www.python.org/psf), and individual contributors. Thank you all!

## Sprint Topic Ideas 

Each sprint day began with an interactive overview of the Docutils architecture and codebase.

I will update this page with actual results from the sprint. For now, here is the original list of ideas for the sprint, in no particular order:

- **PROGRESS!** Python source reader (autodocumentation subsystem). There\'s a lot of support for this. Ideas:

  - [PEP 258](http://docutils.sf.net/spec/pep-0258.html#python-source-reader)

  - [detailed exploration of some ideas](http://docutils.sf.net/spec/pysource.html)

  - [notes](http://docutils.sf.net/spec/notes.html#python-source-reader)

  - [DavidG\'s module parser code (incomplete)](http://docutils.sf.net/docutils/readers/python/)

  - [DavidG\'s sandbox code (incomplete)](http://docutils.sf.net/sandbox/davidg/pysource_reader)

  - [Tibs\' sandbox code (incomplete)](http://docutils.sf.net/sandbox/tibs/)

  - [IanB\'s sandbox code (hack)](http://docutils.sourceforge.net/sandbox/ianb/extractor/)

  - Extending [EpyDoc](EpyDoc) with python source parsing (this has been on the todo list for a while now).

- Test framework \-- extend unittest with support for packages of test modules (i.e., integrate [this](http://docutils.sf.net/test/package_unittest.py) into unittest.py).

- **PROGRESS!** DocPy (Python\'s dialect of LaTeX) writer completion \-- would allow easier entry for documentation newbies, \"make authorship more accessible\" ([initial implementation](http://docutils.sf.net/sandbox/edloper/docpy/)). *This would be a major interest for me, I would like to make the Python docs more accessible to new authors \-- SH*

- **DONE!** Add an [epytext parser](http://docutils.sourceforge.net/sandbox/edloper/epytext) (requires [epydoc](http://epydoc.sourceforge.net)).

- **DONE!** HTML fragment writer \-- establish API (useful for ht2html and templating systems). ([Notes](http://docutils.sf.net/spec/notes.html#html-fragments), and [related work](http://docutils.sf.net/sandbox/oliverr/ht/).) Fred Drake and Mike Orr are both interested in this.

  - Reggie Dugard implemented a new docutils.core.publish_parts() convenience function, with Mike Orr\'s initial help.

- [XHTML 2.0](http://www.w3.org/TR/2003/WD-xhtml2-20030506/) writer. Though the spec is in the \"working draft\" stage, it would be nice to start experimenting with it. \-- *Fred Drake*

- Other writers:
  - OpenOffice.org (original hack in [Aahz\'s sandbox](http://docutils.sf.net/sandbox/aahz/OO/) & mods in [Patrick O\'Brien\'s sandbox](http://docutils.sf.net/sandbox/pobrien/OpenOffice/))

  - **PROGRESS!** DocBook ([Oliver Rutherfurd\'s sandbox](http://docutils.sf.net/sandbox/oliverr/docbook/))

  - RTF

- **PROGRESS!** Aahz will be running a sprint to create a base protocol for binary writers, leading to a reactoring of the OpenOffice.org writer and a new MIFWriter for Frame.

- Interpreted text [role bindings](http://docutils.sf.net/spec/notes.html#role-bindings).

- [Large document](http://docutils.sf.net/spec/notes.html#large-documents) issues, including [formal elements](http://docutils.sf.net/spec/notes.html#object-numbering-and-object-references).

- Nested inline markup \-- may require new inline markup parser with proper tokenization & lexing. Or stack-based. Currently under discussion on the [docutils-develop mailing list](http://lists.sourceforge.net/lists/listinfo/docutils-develop). David Abrahams has checked in an initial implementation to the \"nesting\" branch under CVS.

- [Math markup](http://docutils.sf.net/spec/notes.html#math-markup).

- **PROGRESS!** Complete [\"The Docutils Document Tree\"](http://docutils.sf.net/spec/doctree.html) reference doc.

- **PROGRESS!** Wikis ([Ian Bicking\'s sandbox](http://docutils.sf.net/sandbox/ianb/wiki/), [FAQ entry](http://docutils.sourceforge.net/FAQ.html#are-there-any-wikis-that-use-restructuredtext-syntax)). If [MoinMoin](MoinMoin) is python.org\'s official wiki, it would be nice if it fully supported reStructuredText ;-).

- **PROGRESS!** [Squash bugs](http://docutils.sf.net/spec/notes.html#bugs)

- Add internationalization to [footer boilerplate text](http://docutils.sf.net/spec/notes.html#footer-boilerplate-text).

- [Adaptable file extensions](http://docutils.sf.net/spec/notes.html#adaptable-file-extensions).

- [Emacs reStructuredText mode](http://docutils.sf.net/tools/editors/emacs).

- [Docstring semantics](http://docutils.sf.net/spec/semantics.html).

- Extend [EpyDoc](EpyDoc) support for reStructuredText (e.g., for LaTeX output).

- Auto-numbering syntax.
  - The ability to reference (internal link) an auto-numbered section sans the number.

- (One just slightly off-topic idea would be to extend an existing documentation generator, such as [EpyDoc](EpyDoc), to support Zope-style interfaces. This would be especially nice since [EpyDoc](EpyDoc) already supports reStructuredText. \-- *Fred Drake*)

  - ([EpyDoc](EpyDoc) \*should\* already support Zope-style interfaces. If not, then please let me know where it needs to be extended for proper support. \-- *Edward Loper*)

- **DONE!** implemented a directive to embed the ABC music notation in reStructuredText.

There are more ideas in the [Docutils to-do list](http://docutils.sf.net/spec/notes.html#to-do).

## Comments 

Please feel free to add any comments you like. Include your name for feedback; anonymous comments OK too. I hope to see you at PyCon! \-- *David Goodger*

I shan\'t be able to make PyCon (no surprise there), but I hope the sprint goes really well. I have no objection at all if one of the items of work is the pysource reader, whether based on my work or not - indeed, I\'d love to see a working implementation out there. \-- *Tibs*

I\'d be very interested in working on the/a Python source code reader \-- it seems like the giant missing piece of docutils. \-- *Ian Bicking*

Two 2-day sprints would be better for me. I wasn\'t planning to attend any sprint, but Docutils is tempting me. I\'d most likely attend Monday-Tuesday. I\'m not that good at understanding intricate parser code, but perhaps I can work on some other aspect. My wishlist item is for the HTML generator to just produce an HTML fragment I can plug into a larger page, rather than all the header/footer/style stuff it adds. There has also been much interest in our local Python user group about having a ReST syntax in [MoinMoin](MoinMoin). \-- *Mike Orr*

An enhanced client API with better support for [writing fragments](http://docutils.sf.net/spec/notes.html#html-fragments) would be *really* nice to have; I\'d be willing to spend some time on that as well. Each time I have tried to make a simple script that used docutils in some way, the API has been difficult to figure out. It may be that documentation is all that\'s needed, or just a more-visible entry point into existing documentation, but I know how hard that is to do. I think it would be worth having at least a little brain-storming session to figure out where people are getting hung up on the API and letting you tell us how much of it is there in some form already, and guiding an effort to make it more effectively exposed. Whether that\'s documentation, a little code, or a pile of new stuff, I don\'t know, but my past explorations make me think there\'s some limited amount of \"API stuff\" that needs to be done. It is unlikely I\'ll be able to sprint on this topic Monday/Tuesday though. \-- *Fred Drake*

I\'ll probably be there for all four days. Anyone who\'s interested in automatic API documentation generation might want to take a look at [EpyDoc](EpyDoc), which currently supports reStructuredText. I\'d like to work on extending it with better docutils support, and improve it in other ways. \-- *Edward Loper*

I use [EpyDoc](EpyDoc) quite a bit, and would like to help with it\'s docutils support. And, just in general, would like to help out the docutils project. \-- *Tracy Ruggles*

I\'d love to get the DocBook writer finished up \-- I think it\'s pretty close. It needs tests, better bibliographic field handling, and probably a bit of polishing. \-- *Ollie Rutherfurd*
