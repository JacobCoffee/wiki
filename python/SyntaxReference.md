# SyntaxReference

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

This page aims to introduce the most important elements of [MoinMoin](MoinMoin)\'s syntax at a glance, showing first the markup verbatim and then how it is rendered by the wiki engine. Additionally, you\'ll find links to the relative help pages. Please note that some of the features depend on your configuration.

# Table of Contents 

    '''Contents''' (up to the 2nd level)
    <<TableOfContents(2)>>

**Contents** (up to the 2nd level)

# Headings 

***see:** [HelpOnHeadlines](HelpOnHeadlines)*

    = heading 1st level =
    == heading 2nd level ==
    === heading 3rd level ===
    ==== heading 4th level ====
    ===== heading 5th level =====

# heading 1st level 

## heading 2nd level 

### heading 3rd level 

#### heading 4th level 

##### heading 5th level 

# Text Formatting 

***see:** [HelpOnFormatting](HelpOnFormatting)*

     * ''emphasized (italics)''
     * '''boldface'''
     * '''''bold italics'''''
     * `monospace`
     * {{{source code}}}
     * __underline__
     * ,,sub,,script
     * ^super^script
     * ~-smaller-~
     * ~+larger+~
     * --(strike through)--

- *emphasized (italics)*

- **boldface**

- ***bold italics***

- `monospace`{.backtick}

- `source code`

- [underline]

- ~sub~script

- ^super^script

- [smaller]

- larger

- [strike through]

# Hyperlinks 

***see:** [HelpOnLinking](HelpOnLinking)*

## Internal Links 

     * FrontPage
     * [[FrontPage]]
     * HelpOnEditing/SubPages
     * /SubPage
     * ../SiblingPage
     * [[FrontPage|named link]]
     * [[#anchorname]]
     * [[#anchorname|description]]
     * [[PageName#anchorname]]
     * [[PageName#anchorname|description]]
     * [[attachment:filename.txt]]

- [FrontPage](FrontPage)

- [FrontPage](FrontPage)

- [HelpOnEditing/SubPages](./HelpOnEditing(2f)SubPages.html)

- [/SubPage](./SyntaxReference(2f)SubPage.html)

- [../SiblingPage](./SiblingPage.html)

- [named link](FrontPage)

- [#anchorname](SyntaxReference#anchorname)

- [description](SyntaxReference#anchorname)

- [PageName#anchorname](./PageName.html#anchorname)

- [description](./PageName.html#anchorname)

- [filename.txt]( "Upload new attachment "filename.txt"")

## External Links 

     * http://moinmo.in/
     * [[http://moinmo.in/]]
     * [[http://moinmo.in/|MoinMoin Wiki]]
     * [[http://static.moinmo.in/logos/moinmoin.png]]
     * {{http://static.moinmo.in/logos/moinmoin.png}}
     * [[http://static.moinmo.in/logos/moinmoin.png|moinmoin.png]]
     * MeatBall:InterWiki
     * [[MeatBall:InterWiki|InterWiki page on MeatBall]]
     * [[file://///servername/share/full/path/to/file/filename%20with%20spaces.txt|link to file filename with spaces.txt]]
     * user@example.com

- [http://moinmo.in/](http://moinmo.in/)

- [http://moinmo.in/](http://moinmo.in/)

- [MoinMoin Wiki](http://moinmo.in/)

- [http://static.moinmo.in/logos/moinmoin.png](http://static.moinmo.in/logos/moinmoin.png)

- ![](http://static.moinmo.in/logos/moinmoin.png "http://static.moinmo.in/logos/moinmoin.png")

- [moinmoin.png](http://static.moinmo.in/logos/moinmoin.png)

- [InterWiki](http://www.usemod.com/cgi-bin/mb.pl?InterWiki "MeatBall")

- [InterWiki page on MeatBall](http://www.usemod.com/cgi-bin/mb.pl?InterWiki "MeatBall")

- [link to file filename with spaces.txt](file://///servername/share/full/path/to/file/filename%20with%20spaces.txt)

- [user@example.com](mailto:user@example.com)

## Avoid or Limit Automatic Linking 

     * Wiki''''''Name
     * Wiki``Name
     * !WikiName
     * WikiName''''''s
     * WikiName``s
     * `http://www.example.com`
     * [[http://www.example.com/]]notlinked

- WikiName

- WikiName

- WikiName

- [WikiName](WikiName)s

- [WikiName](WikiName)s

- `http://www.example.com`{.backtick}

- [http://www.example.com/](http://www.example.com/)notlinked

# Drawings 

- [![myexample.tdraw](./SyntaxReference.html?action=AttachFile&do=box&target=myexample.tdraw&member=drawing.png "myexample.tdraw")](attachments/SyntaxReference/myexample.tdraw)

# Blockquotes and Indentations 

     indented text
      text indented to the 2nd level

- indented text
  - text indented to the 2nd level

# Lists 

***see:** [HelpOnLists](HelpOnLists)*

## Unordered Lists 

     * item 1

     * item 2 (preceding white space)
      * item 2.1
       * item 2.1.1
     * item 3
      . item 3.1 (bulletless)
     . item 4 (bulletless)
      * item 4.1
       . item 4.1.1 (bulletless)

- item 1
- item 2 (preceding white space)
  - item 2.1
    - item 2.1.1
- item 3
  - item 3.1 (bulletless)
- item 4 (bulletless)
  - item 4.1
    - item 4.1.1 (bulletless)

## Ordered Lists 

### with Numbers 

     1. item 1
       1. item 1.1
       1. item 1.2
     1. item 2

1.  item 1
    1.  item 1.1
    2.  item 1.2
2.  item 2

### with Roman Numbers 

     I. item 1
       i. item 1.1
       i. item 1.2
     I. item 2

I.  item 1
    i.  item 1.1
    ii. item 1.2
II. item 2

### with Letters 

     A. item A
       a. item A. a)
       a. item A. b)
     A. item B

A.  item A
    a.  item A. a)
    b.  item A. b)
B.  item B

## Definition Lists 

     term:: definition
     object::
     :: description 1
     :: description 2

term
:   definition

object

:   

:   description 1

:   description 2

# Horizontal Rules 

***see:** [HelpOnRules](HelpOnRules)*

    ----
    -----
    ------
    -------
    --------
    ---------
    ----------

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

------------------------------------------------------------------------

# Tables 

***see:** [HelpOnTables](HelpOnTables)*

## Tables 

    ||'''A'''||'''B'''||'''C'''||
    ||1      ||2      ||3      ||

::: {}
  ------- ------- -------
  **A**   **B**   **C**
  1       2       3
  ------- ------- -------
:::

## Cell Width 

    ||minimal width ||<99%>maximal width ||

::: {}
  --------------- ---------------
  minimal width   maximal width
  --------------- ---------------
:::

## Spanning Rows and Columns 

    ||<|2> cell spanning 2 rows ||cell in the 2nd column ||
    ||cell in the 2nd column of the 2nd row ||
    ||<-2> cell spanning 2 columns ||
    ||||use empty cells as a shorthand ||

::: {}
+:--------------------:+--------------------------------------:+
| cell spanning 2 rows | cell in the 2nd column                |
|                      +---------------------------------------+
|                      | cell in the 2nd column of the 2nd row |
+----------------------+---------------------------------------+
| cell spanning 2 columns                                      |
+--------------------------------------------------------------+
| use empty cells as a shorthand                               |
+--------------------------------------------------------------+
:::

## Alignment of Cell Contents 

    ||<^|3> top (combined) ||<:99%> center (combined) ||<v|3> bottom (combined) ||
    ||<)> right ||
    ||<(> left ||

::: {}
+:--------------:+:-----------------:+:-----------------:+
| top (combined) | center (combined) | bottom (combined) |
|                +-------------------+                   |
|                | right             |                   |
|                +-------------------+                   |
|                | left              |                   |
+----------------+-------------------+-------------------+
:::

## Coloured Table Cells 

    ||<#0000FF> blue ||<#00FF00> green    ||<#FF0000> red    ||
    ||<#00FFFF> cyan ||<#FF00FF> magenta  ||<#FFFF00> yellow ||

::: {}
  ------ --------- --------
  blue   green     red
  cyan   magenta   yellow
  ------ --------- --------
:::

## HTML-like Options for Tables 

    ||A ||<rowspan="2"> like <|2> ||
    ||<bgcolor="#00FF00"> like <#00FF00> ||
    ||<colspan="2"> like <-2>||

::: {}
+------------------+--------------+
| A                | like \<\|2\> |
+------------------+              |
| like \<#00FF00\> |              |
+------------------+--------------+
| like \<-2\>                     |
+---------------------------------+
:::

# Macros and Variables 

## Macros 

***see:** [HelpOnMacros](HelpOnMacros)*

- `<<Anchor(anchorname)>>`{.backtick} inserts a link anchor `anchorname`{.backtick}

- `<<BR>>`{.backtick} inserts a hard line break

- `<<FootNote(Note)>>`{.backtick} inserts a footnote saying `Note`{.backtick}

- `<<Include(HelpOnMacros/Include)>>`{.backtick} inserts the contents of the page `HelpOnMacros/Include`{.backtick} inline

- `<<MailTo(user AT example DOT com)>>`{.backtick} obfuscates the email address `user@example.com`{.backtick} to users not logged in

## Variables 

***see:** [HelpOnVariables](HelpOnVariables)*

- `@`{.backtick}`SIG`{.backtick}`@`{.backtick} inserts your login name and timestamp of modification

- `@`{.backtick}`TIME`{.backtick}`@`{.backtick} inserts date and time of modification

# Smileys and Icons 

***see:** [HelpOnSmileys](HelpOnSmileys)*

:::: {}
::: {}
  ------------ --------------------------------------------------------------------------- -- ------------ -------------------------------------------------------------------------- -- ------------ ---------------------------------------------------------------------------- -- ------------ ----------------------------------------------------------------------------
  **Markup**   **Display**                                                                    **Markup**   **Display**                                                                   **Markup**   **Display**                                                                     **Markup**   **Display**
  `X-(`        ![X-(](/wiki/europython/img/angry.png "X-(")           `:D`         ![:D](/wiki/europython/img/biggrin.png ":D")          `<:(`        ![\<:(](/wiki/europython/img/frown.png "<:(")           `:o`         ![:o](/wiki/europython/img/redface.png ":o")
  `:(`         ![:(](/wiki/europython/img/sad.png ":(")               `:)`         ![:)](/wiki/europython/img/smile.png ":)")            `B)`         ![B)](/wiki/europython/img/smile2.png "B)")             `:))`        ![:))](/wiki/europython/img/smile3.png ":))")
  `;)`         ![;)](/wiki/europython/img/smile4.png ";)")            `/!\`        ![/!\\](/wiki/europython/img/alert.png "/!\")         `<!>`        ![\<!\>](/wiki/europython/img/attention.png "<!>")      `(!)`        ![(!)](/wiki/europython/img/idea.png "(!)")
  `:-?`        ![:-?](/wiki/europython/img/tongue.png ":-?")          `:\`         ![:\\](/wiki/europython/img/ohwell.png ":\")          `>:>`        ![\>:\>](/wiki/europython/img/devil.png ">:>")          `|)`         ![\|)](/wiki/europython/img/tired.png "|)")
  `:-(`        ![:-(](/wiki/europython/img/sad.png ":-(")             `:-)`        ![:-)](/wiki/europython/img/smile.png ":-)")          `B-)`        ![B-)](/wiki/europython/img/smile2.png "B-)")           `:-))`       ![:-))](/wiki/europython/img/smile3.png ":-))")
  `;-)`        ![;-)](/wiki/europython/img/smile4.png ";-)")          `|-)`        ![\|-)](/wiki/europython/img/tired.png "|-)")         `(./)`       ![(./)](/wiki/europython/img/checkmark.png "(./)")      `{OK}`       ![{OK}](/wiki/europython/img/thumbs-up.png "{OK}")
  `{X}`        ![{X}](/wiki/europython/img/icon-error.png "{X}")      `{i}`        ![{i}](/wiki/europython/img/icon-info.png "{i}")      `{1}`        ![{1}](/wiki/europython/img/prio1.png "{1}")            `{2}`        ![{2}](/wiki/europython/img/prio2.png "{2}")
  `{3}`        ![{3}](/wiki/europython/img/prio3.png "{3}")           `{*}`        ![{\*}](/wiki/europython/img/star_on.png "{*}")       `{o}`        ![{o}](/wiki/europython/img/star_off.png "{o}")                       
  ------------ --------------------------------------------------------------------------- -- ------------ -------------------------------------------------------------------------- -- ------------ ---------------------------------------------------------------------------- -- ------------ ----------------------------------------------------------------------------
:::
::::

# Parsers 

***see:** [HelpOnParsers](HelpOnParsers)*

## Verbatim Display 

    {{{
    def hello():
        print "Hello World!"
    }}}

    def hello():
        print "Hello World!"

## Syntax Highlighting 

    {{{#!python
    def hello():
        print "Hello World!"
    }}}

:::: 
::: 
``` 
   1 def hello():
   2     print "Hello World!"
```
:::
::::

## Using the wiki parser with css classes 

    {{{#!wiki red/solid
    This is wiki markup in a '''div''' with __css__ `class="red solid"`.
    }}}

::: 
This is wiki markup in a **div** with [css] `class="red solid"`{.backtick}.
:::

# Admonitions 

***see:** [HelpOnAdmonitions](HelpOnAdmonitions)*

    {{{#!wiki caution
    '''Don't overuse admonitions'''

    Admonitions should be used with care. A page riddled with admonitions will look restless and will be harder to follow then a page where admonitions are used sparingly.
    }}}

::: caution
**Don\'t overuse admonitions**

Admonitions should be used with care. A page riddled with admonitions will look restless and will be harder to follow then a page where admonitions are used sparingly.
:::

# Comments 

***see:** [HelpOnComments](HelpOnComments)*

    Click on "Comments" in edit bar to toggle the /* comments */ visibility.

Click on \"Comments\" in edit bar to toggle the [comments] visibility.

    {{{#!wiki comment/dotted
    This is a wiki parser section with class "comment dotted" (see HelpOnParsers).

    Its visibility gets toggled the same way.
    }}}

::: 
This is a wiki parser section with class \"comment dotted\" (see [HelpOnParsers](HelpOnParsers)).

Its visibility gets toggled the same way.
:::
