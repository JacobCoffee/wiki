# WikiCourse/10 Text layout with wiki markup

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Slideshow](./WikiCourse(2f)10(20)Text(20)layout(20)with(20)wiki(20)markup.html?action=print&media=projection) [\^](WikiCourse) [\|\<](./WikiCourse(2f)01(20)What(20)is(20)a(20)MoinMoin(20)wiki(3f).html) [\<\<](./WikiCourse(2f)08(20)Hot(20)Keys.html) Slide 9 of 27 [\>\>](./WikiCourse(2f)11(20)Paragraphs.html) [\>\|](./WikiCourse(2f)52(20)Structure(20)in(20)the(20)wiki.html)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Text layout with wiki markup 

[MoinMoin](MoinMoin) does *not* simply use HTML (the *HyperText Markup Language* usually used for websites), but its own, simplified **MoinMoin Wiki Markup Language**, [MoinMoin](MoinMoin)\'s convention for the input of content^[1](#fnref-a7f3cb2912f4b8b7a459cd862b9cb07cedbfb921)^.

## HTML 

    <h1>Headline</h1>
    <p>This is a link to my own homepage: <a href="/FirstnameLastname">FirstnameLastname</a></p>
    <p>A list:
    <ul>
     <li>foo</li>
     <li>bar</li>
    </ul>
    </p>

## MoinMoin wiki 

    = Headline =
    This is a link to my own homepage: FirstnameLastname

    A list:
     * foo
     * bar

![(!)](/wiki/europython/img/idea.png "(!)") The [MoinMoin](MoinMoin) wiki markup will be explained in more detail on the following pages.

------------------------------------------------------------------------

::: footnotes
1.  [][MoinMoin](MoinMoin) also supports other markup languages, such as [creole](HelpOnCreoleSyntax), HTML and many others, see [HelpOnParsers](HelpOnParsers) ([1](#fndef-a7f3cb2912f4b8b7a459cd862b9cb07cedbfb921-0))
:::
