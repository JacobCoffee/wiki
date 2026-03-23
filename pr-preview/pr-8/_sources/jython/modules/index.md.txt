# Modules & Compatibility

Jython doesn't support every CPython module -- some depend on C extensions that don't exist on the JVM. This section tracks which modules work, which don't, and how popular Python frameworks and libraries run (or don't run) on Jython. If you're trying to use a specific library and want to know its Jython status, check here.

## Module Status

- [ModulesOverview](ModulesOverview) -- Jump-off page with links to detailed module discussions
- [AbsentModules](AbsentModules) -- List of CPython standard library modules missing from Jython (note: quite outdated)
- [ModulePorting](ModulePorting) -- Tracking the effort to port and update standard library modules from CPython 2.7

## Individual Modules

- [NewSocketModule](NewSocketModule) -- The rewritten socket module with non-blocking and SSL support
- [SelectModule](SelectModule) -- The select module implementation for Jython
- [SSLModule](SSLModule) -- SSL/TLS support in Jython
- [SetsModule](SetsModule) -- The sets module implementation
- [UnicodeData](UnicodeData) -- Unicode data module notes

## Frameworks on Jython

- [DjangoOnJython](DjangoOnJython) -- Running Django on top of Jython, with setup notes and known issues
- [PylonsOnJython](PylonsOnJython) -- Getting the Pylons web framework working on Jython
- [PylonsOnJythonOld](PylonsOnJythonOld) -- An older version of the Pylons-on-Jython guide
- [TwistedOnJython](TwistedOnJython) -- Status of Twisted framework compatibility with Jython
- [SqlAlchemyOnJython](SqlAlchemyOnJython) -- Running SQLAlchemy on Jython
- [MercurialOnJython](MercurialOnJython) -- Attempts to run Mercurial on Jython
- [SetuptoolsOnJython](SetuptoolsOnJython) -- Setuptools compatibility and installation on Jython

## Java Integration

- [JavaLibraries](JavaLibraries) -- Using Java libraries directly from Jython code
- [JavaScript](JavaScript) -- Interoperability between Jython and JavaScript

```{toctree}
:hidden:
:maxdepth: 1

AbsentModules
DjangoOnJython
JavaLibraries
JavaScript
MercurialOnJython
ModulePorting
ModulesOverview
NewSocketModule
PylonsOnJython
PylonsOnJythonOld
SSLModule
SelectModule
SetsModule
SetuptoolsOnJython
SqlAlchemyOnJython
TwistedOnJython
UnicodeData
```
