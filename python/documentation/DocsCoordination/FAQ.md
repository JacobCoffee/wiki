# DocsCoordination/FAQ

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## FAQ for documentation team members 

**How do I get started?**

- As a start, everybody should have a Python checkout and a doctools checkout. The [GitHub](./GitHub.html) URLs are

  [https://github.com/python/cpython](https://github.com/python/cpython) and [https://github.com/sphinx-doc/sphinx](https://github.com/sphinx-doc/sphinx)

  The sphinx repository appears to be the current project with `doctools`{.backtick} directory contains all the toolset that\'s been written so far (moved there from the docutils berlios SVN).

  The Python directory contains the source code of Python and has a subdirectory called `Doc/`{.backtick}, in which the reST sources lie. The README there tells you how to build the docs.

**What time commitment is necessary?**

- As this is a voluntary effort, nobody is \"required\" to do anything. When the new system goes live, it depends on the amount of comments and change suggestions that come in how much the group will have to shoulder. (More on that below.) But as always, every contribution helps.

**What mailing lists are there?**

- The [docs@python.org](mailto:docs@python.org) list will mainly be our private coordination place. (The archives are not publicly accessible.) Additionally, outside mails to [docs@python.org](mailto:docs@python.org) will get here too, they can usually be answered, and if needed, discussed, quickly. Also, for a start I had in mind to let the web application send patches and comment notifications here too, which can later be changed if the traffic gets too hard.

  There is also the Doc-SIG (special interest group) at [doc-sig@python.org](mailto:doc-sig@python.org), which is at the moment quite deserted. In the tradition of open source, I think it would be good if discussions that are of public interest are at least crossposted there, in order to allow others to participate.

**What other infrastructure is there?**

- While a mailing list is a very nice thing to have, sometimes a Wiki page is better suited to coordinating a task. For now, we have the subhierarchy of the Python wiki here \-- if this is found impractical, we\'ll have to think about some other solution. As a bug tracker, we\'ll use SF for now, and the new bugs.python.org tracker as soon as it goes live. There will be a new category \"doctools\" in the latter, so that content and toolset bugs can be separated.

  There is also an IRC channel `#python-docs`{.backtick} at `irc.freenode.net`{.backtick}. I (Georg) will be there most of the time, so short questions can be settled there as well with private email; everyone is welcome to join and idle there.

  Finally, for those who don\'t like IRC for direct contact, my Jabber address is [gbrandl@pocoo.org](mailto:gbrandl@pocoo.org).

**How do I get SVN commit access?**

- Those of you who\'ll contribute more than the occasional patch (which can be just mailed to a committer) can get SVN access to svn.python.org. For that, I\'ll need an SSH2 compatible public key, your full name and, of course, your word that you won\'t touch things outside the documentation tree ![:)](/wiki/europython/img/smile.png ":)")
