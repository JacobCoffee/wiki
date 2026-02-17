# PylonsOnJython

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

::: 
### Pylons on Jython

**Status**: [Jython is supported as of Pylons 0.9.7](http://pylonshq.com/docs/en/0.9.7/jython/)
:::

::::::: 
### Pending Improvements

Support more of the out of the box optional components, such as:

::: 
#### SQLAlchemy

See [SqlAlchemyOnJython](SqlAlchemyOnJython)
:::

::: 
#### Jinja2

Jinja2 is supported on Jython as of version 2.2.1
:::

::: 
#### Genshi

Jim Baker and Ariane Paola have played around with Genshi on Jython. Its use of pyexpat is the biggest roadblock. Jython now includes a pyexpat, but it\'s not fully compatible with CPython\'s (and doesn\'t support all the features Genshi uses).
:::

::: 
#### Turbogears 2

Ariane Paola made some progress porting TurboGears 2 components to Jython for Google\'s Summer of Code. Genshi and SQLAlchemy are the most important pieces that need porting

Older details: [PylonsOnJythonOld](PylonsOnJythonOld)
:::
:::::::
