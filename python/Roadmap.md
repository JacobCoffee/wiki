# Roadmap

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page lists major tasks and goals for enhancing \*.python.org infrastructure along with their status. The page should be similar to [this one](http://dungeonhack.sourceforge.net/Roadmap) or at least [this one](http://ufoai.ninex.info/wiki/index.php/TODO/2.3). If you have questions about tasks or their status - ask owner or try [#pydotorg](irc://freenode.net/pydotorg) IRC channel. If we succeed in organizing our efforts around enhancing \*.python.org services, then this page can be extended to cover core Python Development as well.

### Legend 

Task status description:

- **open**: no one has claimed this task yet or the task has not been started

- **wip**: work-in-progress; someone has claimed/started this task

- **done**: task is finished

Additional tasks can be found on our [SiteImprovements](SiteImprovements) page.

## Generic 

- (high) Split Python codebase into modules for independent development - open (techtonik)
  - convenient way for interested parties to subscribe and monitor information related to one module
    - bugs
    - code repository - ! (several views)
    - use cases - !
    - discussions
    - drafts (wiki, google wave)
    - documentation

    (try multiproject Trac)

- (high) contribulyzer similar to used in Subversion community - open

- (medium) centralized login.python.org [spec](http://code.google.com/p/rainforce/wiki/CentralizedLogin) - open (techtonik)

## Documentation 

- (medium) Online editor for Docs - open
  - depends on centralized login above

  - need to implement [ModerationQueue](http://code.google.com/p/rainforce/wiki/ModerationQueue) for anonymous users

## Wiki 

- (high) Mercurial process to maintain and share modifications to [MoinMoin](MoinMoin) installations - wip (techtonik)

- (medium) Roadmap plugin/extensions for [MoinMoin](MoinMoin) - open
