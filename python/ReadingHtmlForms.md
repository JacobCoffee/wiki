# ReadingHtmlForms

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A friend of mine recently asked, \"Is there anything in Python that can read forms?

He\'s got perl code that looks like this:

            my $form = HTML::Form->parse($writeFormPage, $res->base());
            defined($form) or return "Can't even get wiki edit form at $URL";
        if ($form->find_input('savetext')) {
            $form->value('savetext',$pagetext);
        }
            my $req = $form->click('button_save');
            my $res = $ua->request($req);

I thought, \"`cgi` module,\" but realized it\'s for writing pages, not reading them. Then I thought `urllib`, but didn\'t see anything very promising over there, either.

Does anyone know of Python code or a Python module that will help you read out forms, and create responses to them?

\-- [StefanBehnel](StefanBehnel)

[lxml.html](http://lxml.de/lxmlhtml.html#forms) has pretty sophisticated HTML form support.

\-- [LionKimbro](LionKimbro) 2004-06-03 07:39:12

Look at:

- Mechanize: [http://wwwsearch.sourceforge.net/mechanize/](http://wwwsearch.sourceforge.net/mechanize/) (which is based on a Perl module)

- Webunit: [http://www.mechanicalcat.net/tech/webunit/](http://www.mechanicalcat.net/tech/webunit/)

------------------------------------------------------------------------

[CategoryFaq](CategoryFaq)
