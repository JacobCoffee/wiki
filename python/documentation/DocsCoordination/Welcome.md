# DocsCoordination/Welcome

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```


    Hi,

    welcome, everyone, to the Python docs maintainer team!  I'm positively
    flattened by the sheer number of volunteers, and the broad spectrum of
    people caring about the docs.

    To get to know each other, I suggest everyone posts a (short) introduction
    about himself, his involvement with Python and documentation, and how he
    likes to help -- with writing, editing, the software or else. [1]_

    (I know many have already done that in their first mail, but not everyone
    will have read those.)

    Ah yes, and the timezone may be useful information too  :) 


    Now, here are a few things you'll want to know about:

    Getting started

      As a start, everybody should have a Python checkout and a doctools
      checkout. The SVN URLs are

      http://svn.python.org/projects/python/trunk and
      http://svn.python.org/projects/doctools/trunk

      (there are some tips on SVN at http://www.python.org/dev/faq/)

      The doctools directory contains all the toolset that's been written
      so far (I've moved it there from the docutils berlios SVN).

      The README file in there tells you how to get started with the conversion
      and how to use the "sphinx" [2]_ builder. (At least on *NIX, if anybody
      wants to work out a similar thing for Windows...)

      The Python directory contains the source code of Python and has a
      subdirectory called Doc/, in which the current LaTeX sources lie, and
      which we will replace sooner or later with the reST sources.

    Time Commitment

      As this is a voluntary effort, nobody is "required" to do anything.
      When the new system goes live, it depends on the amount of comments
      and change suggestions that come in how much the group will have to
      shoulder.  (More on that below.)
      But as always, every contribution helps.

    Mailing Lists

      This list, docs@python.org, will mainly be our private coordination place.
      (The archives are not publicly accessible.)
      Additionally, outside mails to docs@python.org will get here too, they
      can usually be answered, and if needed, discussed, quickly.
      Also, for a start I had in mind to let the web application send patches
      and comment notifications here too, which can later be changed if the
      traffic gets too hard.

      There is also the Doc-SIG (special interest group), which is at the moment
      quite deserted.  In the tradition of open source, I think it would
      be good if discussions that are of public interest are at least crossposted
      there, in order to allow others to participate.

    Other Infrastructure

      While a mailing list is a very nice thing to have, sometimes a Wiki page
      is better suited to coordinating a task.  For now, I suggest using a
      subhierarchy of the Python wiki at wiki.python.org -- if this is found
      impractical, we'll have to think about some other solution.

      As a bug tracker, we'll use SF for now, and the new bugs.python.org tracker
      as soon as it goes live.  I'll have a new category "doctools" created in
      the latter, so that content and toolset bugs can be separated.

      Finally, I've set up an IRC channel #python-docs at irc.freenode.net.
      I'll be there most of the time, so short questions can be settled there
      as well with private email; everyone is welcome to join and idle there.

    SVN Access

      Those of you who'll contribute more than the occasional patch (which
      can be just mailed to a committer) can get SVN access to svn.python.org.
      For that, I'll need an SSH2 compatible public key, your full name and,
      of course, your word that you won't touch things outside the documentation
      tree  :) 

    First Tasks

      The first task for those who want to develop the toolset is to make
      themselves familiar with it.  It's not quite documented at the moment,
      but I'll try and write up a cursory code overview after I finish this
      mail, so expect it to turn up in SVN soon.

      I'd like to ask all of you to look at the new built documentation and
      collect thoughts about it -- not the content, but mainly the infrastructure
      such as navigational elements, accessibility etc.

      Note that the web application does use JavaScript in some places, but only
      for better usability (hopefully).  Users without JavaScript may not lose
      any functionality.  (This should be confirmed every now and then.)

      Finally, I have some finer points of the content structure to discuss,
      for which you don't have to be familiar with the toolset yet,
      but I'll send that out in separate mails.

    Next Tasks

      When we find the toolset reasonably complete, we'll convert both the
      Python 2.6 and Python 3.0 SVN documentation branches to the new system.
      The conversion itself is (should be, you'll see yourself) painless, but
      it can't do everything right.  For example, as the toplevel documents
      were completely separate until now, you couldn't directly link from, e.g.
      the library reference to a specific section of the language reference.
      These links will have to be corrected.

      All these tasks to do after conversion are listed in the
      ``doctools/converter/newfiles/TODO`` file, which is copied to the reST
      source tree on conversion.

      All other tasks that are independent of the converter I've collected in
      ``doctools/TODO``.

    cheers,
    Georg


    .. [1] Starting with myself: I'm a student of Physics, based in Munich, Germany,
           and am involved with Python development since 2005, and have been hacking
           up the new doctools, together with Armin, since March.

    .. [2] Actually, the name comes from the python.org website builder, which is
           called Pyramid.
