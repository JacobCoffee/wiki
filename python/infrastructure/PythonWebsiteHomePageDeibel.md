# PythonWebsiteHomePageDeibel

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Stephan Deibel\'s Python.org Home Page Candidate Plan 

(basing this on [PythonWebsiteHomePageGoodger](PythonWebsiteHomePageGoodger))

## Home Page 

The home page should contain the intro paragraph (minus What is Python header) and \*some\* material that overviews the language and what it\'s used for \-- but this should be 1-2 additional paragraphs only and not mention any specific packages as is done now.

I do think it\'s important to overview the language on the home page. It is, after all, the universal home page \*for the language\*.

- But a brief overview only (I really think the existing one paragraph is enough), with a prominent link to \"More About Python\". I think it\'s very important that the main content (the center column) of the home page, including the first \"News\" item, fit on the screen without scrolling. The home page serves dual duty: introducing newcomers to Python, and informing returning visitors of news. The former should not overwhelm the latter. Look at the \"ABOUT\" page; its content overlaps the home page too much. \-- David Goodger

Change title to \"Python Programming Language \-- Official Website\"

Left sidebar:

- navigation menu
- Quick Links (\*not\* \"quicklinks\"). And rename \"Cheese Shop\" to \"Package Index\"

Center:

- One-paragraph intro, but remove the \"What is Python?\" header

- 1-2 more paragraphs describing Python and what it is used for \-- don\'t mention specific packages

- Prominent \"More detail\...\" link to /apps (new section proposed in [PythonWebsiteHomepageGoodger](./PythonWebsiteHomepageGoodger.html)) (maybe also another to /about/benefits, tho I\'m less wild about that page)

- Under \"Try Python Today!\" header: prominent Download, Get Started, Documentation buttons/icons

- News & Announcements (3 items is probably enough) (and move the rest of the stuff on the home page now to /apps; see below)

Right sidebar:

- Success Story box like now \-- ideally changed automatically weekly from a subset of all the success stories (manual for now)

- A Quote \-- change monthly from selected subset or manually for now

- \"Using Python For\...\" box as now

- \"Written in Python\" \-- get rid of this entirely (How about moving it into a page under ABOUT? I think listing prominent Python projects \[& Python users?\] is useful for marketing. \--David Goodger)

## Navigation Menu 

- I disagree that PSF should be higher up \-- I think it\'s fine after Community. Also no need to spell this out. The PSF is referenced from elsewhere when appropriate (license page, etc) and otherwise just isn\'t that interesting to most users of the site.
- I also disagree w/ David that we should change \"Python-dev\" to \"Developers\" \-- this is going to cause more confusion I think
- Add \"Applications\" section /apps (see below) \-- This should be right after About

## ABOUT section 

Change order:

- Benefits (new page; see [http://www.squidoo.com/pythonology/](http://www.squidoo.com/pythonology/)) (I think this should be first) (I\'m not entirely wild about this page \-- I think abstract benefits are not the reason people are going to be interested in or pick up Python; they are things people appreciate only after the fact and otherwise view as hype. But I\'m willing to try having such a page)

- Getting Started

- Success Stories

- Quotes

- Website

- Help

## APPLICATIONS section /apps 

One item & page per major application area (i.e. \"Using Python For\...\" items from the home page) Sort existing home page content under there and expand substantially. This is where wiki style editing might be nice although I think I would prefer to have these pages not actually entirely in the wiki. Rather, have the reflect what people are most commonly using (those items are first, not alphabetical) and refer to wiki for \"others\" that are not commonly used. We need to help new users sort through to find the most likely solutions quickly.

## RELATED subnav 

The /apps sections should index success stories related to each and show them in a subnav box on the right.

Success stories should show appropriate /apps pages in subnav box on the right.

Would be nice to similarly cross reference other related materials like stuff /doc (onsite or elsewhere, esp howto style content, which is most useful for people getting started), link into cheeseshop categories, /audio, and other stuff.

This needs to start simple but we could eventually base on Evelyn\'s classification of the success stories plus the items in the \"using python for\" box on home page plus cheeseshop categories to come up w/ standard classification of resources that would let us automatically generate a list of related resources. I may be dreaming\... but we can probably do something reasonable or at least manually add some useful subnav items.

(The new Google related box at the bottom of every page might do this for us but it doesn\'t seem to be working well \-- maybe it\'s broken pending reindexing or something)

## QUESTIONS / misc 

\* /apps and not /about/apps? If we don\'t do /about/benefits, I\'d almost thing /about/apps

- is better tho we do end up w/ /about/apps/web or whatever. I\'m undecided but we clearly do need to keep the top level list under control.

\* One alternative for longer top level menu is to section the list so we have groups::

        ABOUT
        APPLICATIONS             <-- High level info sections
        NEWS
        -                        <-- Divider / space
        DOCUMENTATION            <-- Users sections
        DOWNLOAD
        LINKS
        -
        COMMUNITY                <-- Community/developers sections
        PYTHON-DEV
        PSF

- (This is just one possible arrangement; not sure if this works well w/ the sub-menu expansion except maybe if color is used instead of divider/space)
