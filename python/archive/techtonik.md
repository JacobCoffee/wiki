# techtonik

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

[techtonik/ideas](./techtonik(2f)ideas.html)

- prematurely closed: [https://github.com/pypa/pip/issues/2409](https://github.com/pypa/pip/issues/2409)

### Python wishlist 

Core Python 2 flaws.

- locals() returns a variable that can be updated at any moment (and changes behavior under trace function)

- internal representation of .py file paths is not normalized (comparisons and identity checks are impossible)

- `-*- coding -*-`{.backtick} header [is not used as default encoding](http://bugs.python.org/issue17439) when transforming string literals in the source file

- can not modify variables in outer scope (see nonlocal from Python 3)

Missing features of community development process.

- +1 on mailing list posts, on tracker comments and bugs

- personal roadmaps listing features people find important and work on

- de-facto roadmap for the next Python version - Trac milestones

- real-time activity feed for [http://bugs.python.org/](http://bugs.python.org/)

  - activity by module, by version

- tracker fixes
  - \'action item\' issue type
  - everybody should be able to add/remove blockers
  - \'reply\' link for each message to track threads

- monthly mailing list FAQ (status) posts on busy mailing lists [.](https://mail.python.org/pipermail/distutils-sig/2010-March/015907.html)

  - contain the most updated info on list topic
  - encourage replies with fixes
  - encourage collaborative roadmaps

PEP process improvements.

- credit contributors, and not only authors as rereading and validating the spec requires time too

- reduce formalism on [who can participate](http://mail.python.org/pipermail/python-dev/2012-December/123231.html)

- accept edits as patches ([create online editor](https://code.google.com/p/pydotorg/source/browse/?repo=doceditor))

- build list of contributors with Mercurial

Ideas:

- Normalized Python
- Iterative Development Process
- Language for humans should help them save time for most frequent operations
- Replace pipes with channels for subprocess (rotated queue of strings)

### Component wishlist 

Public domain or MIT preferred.

- [wikify](https://bitbucket.org/techtonik/wikify) - micro-framework for text wikification (easy to extend and debug) ([1](http://issues.roundup-tracker.org/msg4572), [2](http://psf.upfronthosting.co.za/roundup/meta/msg2666))

  - \[ \] describe the \"conflicting replacements\" (idempotency) problem what the wikify solves
  - split text by regexp, process matched, exclude processed
  - run the next regexp on the list of text that is left
  - reassemble

- treeworks - tools to work with 2D data structures (trees), including common visualization and debugging

### Ideas open for the taking 

Open Source artists wanted (credits available):

- 3D robot nut in Blender for rirror on Bitbucket

- 128x128 wikify logo on Bitbucket

- Logo for [web.py](http://webpy.org/)

GSoC/Help needed for tools that support Python development:

- complete module-2-source tree map at [https://bitbucket.org/techtonik/python-stdlib](https://bitbucket.org/techtonik/python-stdlib)

  - this will allow to track changes in repository on a module level
  - this will allow to find out where a file belongs to

- [HighScore](HighScore)

Just a list:

- RIDLE - replace IDLE with modern alternative
  - minimalism (perfection achieved not when it is nothing more to add\...)
    - get a list of current IDLE features, put them in a table
    - filter out features that are the most critical
    - accent on User eXperience
  - incrementalism (development process)
    - monthly development iterations
    - schedule the most important feature per iteration
  - community process

### steAm and SMArt (dealing with complexity) 

Canvas2D ideas:

- redo \*key status script\* for PySDL2, pyprocessing and (maybe) pyglet

- [http://devinvenable.blogspot.com/2009/12/creating-digital-synth-sounds-using.html](http://devinvenable.blogspot.com/2009/12/creating-digital-synth-sounds-using.html)

- [http://devinvenable.blogspot.com/2010/07/opengl-intellivision-man.html](http://devinvenable.blogspot.com/2010/07/opengl-intellivision-man.html)

Dynamic data visualization examples:

- [http://www.fudgie.org/](http://www.fudgie.org/)

- [https://code.google.com/p/logstalgia/](https://code.google.com/p/logstalgia/)

### Human Language Translation Table 

`Explicit is better than implicit.`{.backtick} doesn\'t apply to humans, apparently.

::: {}
  ---------------------------------------- --------------------------------------------- ---------------------------------------------------------------
  **Explicit**                             **Implicit**                                  **Comment**
  it\'s annoying, urgent, really serious   \--                                           humans don\'t like serious issues, remove
  fix it ASAP                              \--                                           humans read it as a direct command, become aggravated, remove
  you\'re wrong                            I\'m not sure that\'s a good idea             humans don\'t like to be wrong, become demotivated
  X suxx                                   I think Y would be a better solution that X   humans attached to X don\'t like when X suxx, but may like Y
  X suxx                                   X is great, but..                             humans attached to X may get outrageous to hear that X suxx
  ---------------------------------------- --------------------------------------------- ---------------------------------------------------------------
:::

------------------------------------------------------------------------

[CategoryHomepage](CategoryHomepage)
