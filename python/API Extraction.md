# API Extraction

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

`API Extraction`{.backtick} is a process of getting available public API from a library or application. It is needed, if you want to track API changes over time, compare interfaces of libraries that claim to support certain interface, provide autocompletion for your Python tools.

There are two ways to read API of a module - `import and inspect`{.backtick} and `read without importing`{.backtick}. In the first way you import the module to read its variables, classes and functions. This can be problematic, because module import may fail if some dependencies are not installed, or do some initialization that alters behaviour of your own code. The second way - read code without importing - is done by reading and parsing .py file, but not executing it. The extraction in this way is done through syntax to AST parsing and further AST analysis. Unfortunately, Python AST parser from standard library doesn\'t preserve comments that could be used to give more info about API being exposed.

\* pydoc - standard library, public domain, regexp parsing for text modules, import for binary modules

\* astdump - public domain, proof of concept of AST parsing to extract top level module variables
