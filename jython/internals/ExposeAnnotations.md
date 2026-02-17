# ExposeAnnotations

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

New-style types in Jython 2.2 were created from Java code using a system of templates that inserted code in the types to be exposed to Python and created new \*Derived classes that allowed them to be subclasses. The type exposing templates have been replaced with Java annotations and bytecode generation as explained in [PythonTypesInJava](PythonTypesInJava), but the \*Derived items are still generated from templates. They need to be hooked into the bytecode generation system as well.
