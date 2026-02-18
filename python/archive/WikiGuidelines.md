# WikiGuidelines

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Wiki Editing Guidelines 

We have these guidelines to keep things relatively organised and easy to find. Generally, when there\'s no content on a topic, it\'s better to put *something* in and let others correct it, but make sure to check what other people have written first.

## Creating an Account 

Before you edit the Wiki you will need to create an account. We ask you to do this so that your contributions can be acknowledged and so that your valuable changes are more easily distinguishable from the spam and vandalism that so often arise when people are not required to provide some kind of identity.

Remember that you can always log in via OpenID. When you do so for the first time, you will be asked to enter a username in order to create an account and to associate your OpenID with that account. (If you already have an account, you will be able to enter a username to associate it with that existing account.)

## Creating Pages 

- Before adding a new page, [check](http://wiki.python.org/moin/FindPage) if there isn\'t already a page for that topic.

- By all means choose a [WikiName](WikiName) as a page name. Most pages on this Wiki use this style.

- *Do not* change the names of things to \"force\" a [WikiName](WikiName). For example, JEdit is not a [WikiName](WikiName), but this does not mean that you should somehow make it one by changing letters and making, say, JedIt. Instead just create a page and then use the [link syntax](HelpOnLinking) (for example, `[[JEdit]]`{.backtick}) to refer to the page.

## Editing Protected Pages 

- If you see something that needs to be changed, but you don\'t have permission, send a mail to `<pydotorg-www AT python DOT org>`. Unfortunately, any Wiki editable by the general public has to lock down some pages from time to time.

## Creating a Home Page 

- If you want to create your own \"homepage\" on the Wiki, please only do so if you\'re providing or promoting Python-related content or if you have signed your name on another page (and want others to be able to contact you).

- Please use the [HomepageTemplate](HomepageTemplate) when creating your homepage so that it belongs to [CategoryHomepage](CategoryHomepage). (You will be prompted to do this when making a page.)

- Try to mention **something** about your relationship to Python on your homepage. Something like, \"I maintain the WhoSeeWhatsIt Python wrapper\" or, \"I offer Python consulting services\" would be more than sufficient. If you are just a Python fanboy (or fangirl), something like, \"Isn\'t Python the greatest language since C?\" would also be fine. If all the moderators see is an email address your page is likely to be summarily deleted. We don\'t have time to spend searching for your name and/or email elsewhere on the Wiki or in the broader Python community.

## Writing Pages 

- Please structure long pages to sections (learn to use `== headings ==`{.backtick}). Also consider using the `<<TableOfContents>>`{.backtick} macro.

- Avoid duplicating information when not necessary, and respect copyrights. If you are unsure, at least credit the source, so that others can fix things if needed.

- Learn to use Wiki format mentioned in [HelpOnFormatting](HelpOnFormatting). It allows for more consistent page styles.

- You can use [ReStructured Text](./HelpOnParsers(2f)ReStructuredText.html) mark-up, but this can be confusing to people, so try not to do this too much. Importing content from somewhere else for initial publication is probably the most excusable exception. Some features like category membership may not work for ReST pages, so consider converting ReST content to Wiki format at some point.

- If you have source code included, run it yourself to test for at least simple errors.

- Take advantage of this Wiki\'s ability to format and colour Python source code - it is easier to read than a simple, plain monochrome section. An example:

  :::: 
  ::: 
  ``` 
     1 from hello import world
     2 
     3 def say_hello():
     4     """Just say hello :)"""
     5     what = world()
     6     message = what.greet()  # no, there's no module named "hello" 
     7                             # in Python stdlib - at least not yet :)
     8     return message
     9 
    10 if __name__ == "__main__":
    11     say_hello()
  ```
  :::
  ::::

  Use `numbers=disable`{.backtick} after the language declaration (such as `#!python`{.backtick}) to remove line numbering.

### Linking 

- Although a [WikiName](WikiName) will link to another page, don\'t be afraid of using the [link syntax](HelpOnLinking) to link to, say, the [FrontPage](FrontPage) by writing `[[FrontPage|front page]]`{.backtick} instead, thus producing a link to the [front page](FrontPage) like this.

- Use the `Issue:7942`{.backtick} syntax to refer to issues in the Python bug tracker. For example, here is an issue: [7942](http://bugs.python.org/issue7942 "Issue").

- Use the `PEP:0001`{.backtick} syntax to refer to PEPs. For example, here is a PEP: [0001](http://www.python.org/dev/peps/pep-0001 "PEP").

- If a link is broken on a page, try to determine whether it is temporarily broken or whether the resource really has gone away forever. For permanently broken links, follow the instructions below.

- *Do not use link shortening services for links!* You are not limited to 160 characters (or whatever) here, and there is no benefit to using a shortened URL that has to be redirected by some third-party service to take the user to the real URL. Using shortened links exposes users to potentially dubious redirection sites and also obscures the nature of the eventual URL which may also be a dubious site itself. Moreover, obscuring the real URL makes decisions about updating links and archiving content much harder.

#### Broken Links 

- If the link pointed to a specific resource for which a substitute does not really exist, try putting the URL into the [Web Archive](http://web.archive.org/), finding the latest usable version, and then replacing the link in the page with that version or a link to the choice of versions that the Web Archive provides. You might want to add something like \"(archived link)\" to show that the resource is no longer \"live\".

- If the link pointed to a resource that has moved - perhaps it was maintained by one company but is now maintained by another - you might update it to point to the new home of that resource.

- If the link referred to a description of a topic, consider using Wikipedia or another stable, well-known resource as a replacement. For example, a replacement for a link to a definition of Python could be `[[WikiPedia:Python (programming language)]]`{.backtick} producing [Python (programming language)](http://www.wikipedia.com/wiki/Python%20%28programming%20language%29 "WikiPedia") and would probably serve the intended purpose.

### Attachments 

- Do not upload attachments without referencing them in the page they are attached to (or in some other obviously connected page). Unclaimed attachments will be deleted!

## Etiquette 

When editing existing pages, the following guidelines are proposed:

- By all means make edits to pages in order to fix mistakes, update and add information, and so on.

- Use the preview button before committing.

- When editing pages, particularly larger ones, try and commit all changes at once, or at least as many as possible at the same time. Don\'t make lots of small changes, saving each one: this fills the page history with micro-edits which make it very difficult to see earlier history information.

- Remember that some pages have been around for a long time, are actively maintained, and are the result of collaboration between a number of people. It is therefore quite impolite to go in and to spontaneously reorganise such pages or to decide that your own editorial preferences overrule those of the people who have worked hard to produce the information you want to change, remove or rearrange. Consider contacting one or more of the maintainers before seeking to \"refactor\" content.

- Respect any editorial guidelines on the pages you wish to edit. *Do not remove guidelines you do not agree with!*

------------------------------------------------------------------------

[CategoryPythonWebsite](CategoryPythonWebsite)
