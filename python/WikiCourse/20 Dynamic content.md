# WikiCourse/20 Dynamic content

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Slideshow](./WikiCourse(2f)20(20)Dynamic(20)content.html?action=print&media=projection) [\^](WikiCourse) [\|\<](./WikiCourse(2f)01(20)What(20)is(20)a(20)MoinMoin(20)wiki(3f).html) [\<\<](./WikiCourse(2f)19(20)Symbols.html) Slide 19 of 27 [\>\>](./WikiCourse(2f)21(20)Macros.html) [\>\|](./WikiCourse(2f)52(20)Structure(20)in(20)the(20)wiki.html)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![(!)](/wiki/europython/img/idea.png "(!)") *The following four chapters are about advanced details. If you don\'t care about this, you can just [skip](./WikiCourse(2f)30(20)The(20)graphical(20)editor.html) them.*

# Dynamic content 

[MoinMoin](MoinMoin) is built in a quite modular way, so its functions are expandable by using plug-ins. Macros, parsers, actions, etc. can either be built-in, included, or installed as a plug-in.

## Macros 

A macro is entered as wiki markup and it processes a few parameters to generate an output, which is displayed in the content area.

## Parsers 

A parser is entered as wiki markup and it processes a few parameters and a multiline block of text data to generate an output, which is displayed in the content area.

## Actions 

An action is mostly called using the menu (or a macro) and generates a complete HTML page on its own.
