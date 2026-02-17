# BuildAnIntranet

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Build an Intranet 

For an intranet solution for a company or organisation of almost any size, the processes might look something like this:

1.  Find out what applications you need:
    - Announcements - this is often needed, but where do they come from, how are they entered? Consider the review workflow (if any).
    - Discussions - are these really required? Do employees really get to have a say on announcements and other things? What about the public?
    - Other information - project databases, competence databases - are these already around, or is it some Excel spreadsheet someone is keeping?
    - Manage documents - are they structured or categorised in some way? What kind of documents are they?

2.  Now think about [ContentManagement](ContentManagement) solutions for a moment.

    - Would an established solution like Plone be enough, perhaps with customisation?

    - Or are you looking at some development from the ground up on top of one of the [WebFrameworks](WebFrameworks)?

3.  Now choose a server! Apache on GNU/Linux is quite versatile, but you may not need Apache if you\'re set on running a multi-protocol server like Zope or even one of the [WebServers](WebServers).

4.  Generate content:
    - A Wiki engine like [MoinMoin](MoinMoin) (the basis for the Python Wiki) can provide a flexible solution, especially where the editing and review processes aren\'t fully defined or mapped out.

    - You may be extracting data from different sources and then need to present it as Web pages. Here, the [DataRepresentation](DataRepresentation) and [Templating](Templating) may provide good solutions. And there\'s probably lots of existing documents lying around anyway which can be served up as they are.

5.  Integrate into business processes - not only merits a \"top level\" mention, but an entire Web site devoted to it. ![:)](/wiki/europython/img/smile.png ":)")

6.  Test! It\'s nice if your [WebProgramming](WebProgramming) framework allows development and testing outside a Web browser, XML-RPC, SOAP, etc. Like from the command prompt, for example.

------------------------------------------------------------------------

[CategoryPythonInBusiness](CategoryPythonInBusiness)
