# HighScore

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

From a private chat:

    techtonik> You say yourself - there is no people to review stuff, and that's a good indicator.
    techtonik> ..of something wrong.
    > there is something wrong, but that's not necessarily related to fun
    > or not in the way you are thinking about
    > writing patch is fun
    > and rewarding
    > reviewing them is not
    > reviewing a patch is boring, takes time to do it properly, there's no glory in doing it, and if you commit it you are taking the responsability
    > whereas writing a patch is easy, challenging/fun, and you can say "I did this" once it's applied
    > so it's understandable that there are so many patches and so few reviewers
    ...
    techtonik> Few key issues:
    techtonik> 1. responsibility to patch author, but not the blame, help make patches better without placing additional burden
    techtonik> 2. glory for reviews is solved by highscore system
    techtonik> 3. proper crediting rules are required to make 1,2 possible and everyone happy
    techtonik> 3.1. that means writing author, commiter and reviewers
    techtonik> (see example of Chromium commits and process)
    ...
    techtonik> We may need to maintain IPython Notebook with XML-RPC recipes to fetch the data.
    > knowing what to do is different from doing it
    ...
    techtonik> I agree, but many people ask about a plan.
    techtonik> They don't even know what to do.

The plan:

- steal twisted highscores - [http://twistedmatrix.com/highscores/](http://twistedmatrix.com/highscores/) `bzr get http://twistedmatrix.com/highscores/`{.backtick}

  - chromium highscores - [https://chromium-status.appspot.com/cq/top](https://chromium-status.appspot.com/cq/top)

  - subversion crediting guidelines - [http://subversion.apache.org/docs/community-guide/conventions.html#crediting](http://subversion.apache.org/docs/community-guide/conventions.html#crediting)

  - and chromium commit message format

- explain why everybody will be happy

- allow to use tools under their own licenses inside Python source tree
  - or allow to use tools outside of Python source tree

- write tools to help with commit message formatting stuff
