# EditorConfigurationHowto

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Python\'s syntax requires special handling in the construction of a Python editor mode. Two issues are particular to Python:

See also [HowToEditPythonCode](HowToEditPythonCode) for concrete examples of editor configuration.

## Indentation 

Python uses indentation to group statements. A well-designed mode should offer support for smart indentation of code. For example, a line beginning with the keyword `def`{.backtick} and ending with `:`{.backtick} should cause the editor to indent the following line upon hitting of the return key.

The most widely used standard is four-space indent. Using tabs is discouraged, so the editor should be configured to convert tabs to spaces.

Code examples or references on how to deal with indentation should follow.

## Strings 

Python supports three types of string literals. Strings can be enclosed in single quotes (`'`{.backtick}), double quotes (`"`{.backtick}) and in groups of three single or double quotes (referred to as triple-quoted strings). A well-designed mode should support all three types. In particular, a mode should correctly recognize that triple-quoted strings can include unescaped newlines and quotes.

Python allows for raw strings without \\-escape sequences (written with a preceding r: `r"c:\dir1\dir2"`{.backtick}). A well-designed mode should support this feature as well.

## EditorConfig 

An emerging standard for describing the configuration of code editors in a portable way is [EditorConfig](https://editorconfig.org).

------------------------------------------------------------------------

[CategoryEditors](CategoryEditors)
