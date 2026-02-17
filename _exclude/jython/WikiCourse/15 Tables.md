# WikiCourse/15 Tables

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Slideshow](./WikiCourse(2f)15(20)Tables.html?action=print&media=projection) [\^](WikiCourse) [\|\<](./WikiCourse(2f)01(20)What(20)is(20)a(20)MoinMoin(20)wiki(3f).html) [\<\<](./WikiCourse(2f)14(20)Text(20)styles.html) Slide 14 of 27 [\>\>](./WikiCourse(2f)16(20)Wiki(20)internal(20)links.html) [\>\|](./WikiCourse(2f)52(20)Structure(20)in(20)the(20)wiki.html)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Tables 

## Simplest table 

     || one || two || three ||
     || four || five || six ||

- ::: {}
    ------ ------ -------
    one    two    three
    four   five   six
    ------ ------ -------
  :::

## General table layout 

     ||||||<tablewidth="80%">'''Headline'''||
     ||Cell 1||Cell 2||Cell 3||
     ||<rowspan=2> Two lines||||<bgcolor="#AAAAFF"> Two columns||
     ||<rowbgcolor="#FFFFAA">Cell 2||Cell 3||

- ::: {}
  +:---------:+:------:+:------:+
  | **Headline**                |
  +-----------+--------+--------+
  | Cell 1    | Cell 2 | Cell 3 |
  +-----------+--------+--------+
  | Two lines | Two columns     |
  |           +--------+--------+
  |           | Cell 2 | Cell 3 |
  +-----------+--------+--------+
  :::

## Cell width 

     || Narrow ||<:99%> Broad ||

- ::: {}
    -------- -------
    Narrow    Broad
    -------- -------
  :::

## Spanning rows and columns 

     ||<|2> 2 lines || line 1 ||
     || line 2 ||
     ||<-2> line 3, 2 columns broad ||

- ::: {}
  +:------------:+-------------:+
  | 2 lines      | line 1       |
  |              +--------------+
  |              | line 2       |
  +--------------+--------------+
  | line 3, 2 columns broad     |
  +-----------------------------+
  :::

## Alignment 

     ||<(50%> left ||<^|3> up ||<v|3> down ||
     ||<:> mid ||
     ||<)> right ||

- ::: {}
  +:------+:--:+:----:+
  | left  | up | down |
  +-------+    |      |
  | mid   |    |      |
  +-------+    |      |
  | right |    |      |
  +-------+----+------+
  :::

## Colors 

     ||<#FF0000> red ||<#00FF00> green ||<#0000FF> blue ||

- ::: {}
    ----- ------- ------
    red   green   blue
    ----- ------- ------
  :::
