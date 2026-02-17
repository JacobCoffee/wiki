# WebSolutionComparison

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Real-world comparisons of Python web solutions 

### Introduction 

I\'ve been a Python programmer for quite some time \-- since the 1.5.2 days. I learned early on how easy it is to create web sites in Python, and I\'ve done several.

In fact, I realized this week that I have built non-trivial web sites using at least 4 of the popular web architecture solutions. Arrogantly, I thought that my experiences and personal evaluations of these architectures might be useful to other programmers faced with the daunting list of possibilities.

I will address the architectures in the order in which I used them. I\'ve been programming for a long time, and in that time I\'ve learned a few things about what kinds of techniques make for workable and maintainable programs. For web programming, in particular, I\'ve learned that it is important to separate processing from presentation: the bulk of the HTML should not be deeply embedded in the programming code that creates the page. You\'ll see that theme repeated in my comments.

By the way, I have a terrible tendency towards verbosity. I do not hesitate to use 25 words to express concepts that could be expressed in 10. You\'ve been warned.

One other background note is that I prefer PostgreSQL as a database back-end. All of the solutions I mention below are paired with a Postgres backend. The last time I tried MySQL (which was quite a while ago), it just didn\'t scale as well as Postgres.

Please note that these are strictly **my personal opinions**.

### Python CGI with HTMLgen Templates 

The first big Python site I did was written entirely in plain, ordinary CGI scripts, using HTMLgen to generate the HTML. This site, [http://www.verticalemail.com/](http://www.verticalemail.com/), is a database-driven, categorized e-mail redistribution site with 30 or 35 forms. It currently supports about 3,000 registered users, with a million rows in a back-end database.

The site works extremely well. Conventional wisdom says that a purely CGI-based solution will not work for a production site, because of the penalty of invoking the interpreter each time. That isn\'t necessarily true. Knowing what I know now, I\'d love to go back and recreate this with a more deeply embedded solution, but the CGI-only solution is simple, easy to debug, and easy to extend, and it\'s been running here for three years. It\'s also easy to upgrade, since there is no additional software beyond Python itself.

I used HTMLgen because I like the way I could create HTML constructs in an object-oriented way:

- tbl = Table(
  - TR(
    - TD(
      - Link(\"This is a link\", \"[http://site.com](http://site.com)\")

      )

    ), border=1

  )

However, as neat as this looks, HTMLgen does not encourage the separation of processing and presentation. HTMLgen does include a basic templating scheme, but it is only a small step above the %(field)s substitution scheme built-in to Python.

### Webware / WebKit 

After my CGI experience, I decided I wanted to use a real web framework for my next site. I investigated the available choices at the time (about 4 years ago), and Webware looked like it was more mature and easier to understand than the others, so I gave it a shot.

Without a doubt, Webware has a higher entry bar than straight CGI programming. There is a LOT of stuff in Webware (much of which goes unused for most sites), and it requires root access for at least part of the installation process, so you can fire up the persistent server process at boot time.

One of the nice things about Webware, from a programming perspective, is that it uses class inheritance as a fundamental part of its operation. Your basic [SitePage](./SitePage.html), which contains the basic layout rules for your site, derives from the basic Page class in [WebKit](WebKit) (or one of its useful subclasses). If you have several different areas in your web site, you can derive subclasses for each area. You can derive a subclass to use as a base for the parts that need username/password protection. Finally, you derive leaf classes for each page. This encourages re-use and good programming practice.

### Webware with PSP Templates 

After playing with Webware for a while, I got jealous of the kind of inline symbol substitution that the .ASP programmers were doing over on Windows. Thus, I started playing with the PSP (Python Server Pages) capability included with Webware. (Note that there are at least 2 completely different technologies calling themselves PSP; I\'m talking specifically about the one built-in to Webware.)

The Webware PSP module allows you to write pages and modules in a manner very similar to ASP. Unlike straight Webware, where you have Python scripts with the occasional HTML chunk, a PSP script is a web page with special tags containing Python code and symbols. The fun thing about PSP and [WebKit](WebKit) is that the PSP pages get compiled into Python code, so they can participate fully in the inheritance structure. You can put the guts of your processing in a Python module, and derive a PSP from it containing the presentation. Plus, the PSP files are sufficiently standard HTML that you can use an HTML editor, should that be your cup of tea.

Webware, by default, doesn\'t care about the extension on your files. So, if you have a file that starts out as a .psp but later needs to migrate to a .py, you don\'t have to change any of the references, and your users\' saved bookmarks will still work. You can even include plain .html files; the Webware server will deliver them without further processing, and you can change it to a .psp later, should your needs change.

### WebWare with Cheetah Templates 

While I was writing my Webware/PSP site, I started doing some reading about other Python templating systems. I was intrigued by the shortcut approach to templating taken by Cheetah. An expression that would be written like this in PSP:

- \<%= mySymbols\[\'extraDict\'\].method(\'lookup\') %\>

can be written in Cheetah as:

- \$mySymbols.extraDict.method.lookup

There is something about the dotted notation that I find very appealing. In my view, it makes the page read consistently and cleanly.

Interestingly, Cheetah is not at all tied to HTML. It is a general-purpose templating/substitution tool. The Cheetah package can be used in a standalone way, but I find it to be very useful as an add-on to Webware. Do the processing in the neat inheritance structure of Webware, prepare the symbols and substitution calues in a dictionary, compile the Cheetah template, and print the results. There is even code on the Webware mailing list that shows how to implement a Cheetah caching scheme with a long-running server process, so that pages are only recompiled when the changed.

For the time being, this is still my favorite Python web solution.

### CherryPy 

With [CherryPy](CherryPy), all of the templeted HTML pages in your web site are compiled into a single Python file, *including* the web server. I find this concept fascinating, and over the years, I came back to the [CherryPy](CherryPy) web site several times. I finally did get the time to create a small web site, and I still think it is fascinating.

It is powerful, neat, and standalone. You compile your site to a file, and deploy that file to a Windows or Linux system without modification, regardless of which web server is installed, and even if the host has no web server at all.

The [CherryPy](CherryPy) language strongly enforces the processing/presentation split. The model/view/controller concept is built-in to the language, although they use slightly different terminology. [CherryPy](CherryPy) templates can do simple substitution and limited symbol manipulation, but no heavy processing.

[CherryPy](CherryPy) is well worth a look.

\- Note that the current version 2 of Cherrypy does no longer perform compilation. Instead, you just import cherrypy and declare a method as \'exposed\' to turn it into a request handler. It\'s even more elegant and efficient now.

### PHP 

Before you jump in to correct me, I **know** that PHP is not Python. However, because PHP is so popular, I decided that no self-respecting web site developer should ignore it. So, I dug in.

I have to say the experience was not a happy one. The fundamentals of the language seem quite reasonable, at least in the recent versions (I looked at 4.1). The Perl-derived syntax is a bit hard for me to read, but you get used to it. The standard library is quite extensive, although the fact that all of it exists in the global namespace is a bit confusing. The wiki-based reference manual is quite good.

PHP has full support for classes, attributes and methods, and supports object-orientation, but the key problem is that no one seems to use it! There is a *vast* body of sample PHP code on the web, but nearly all of it is absolutely dreadful. HUGE long procedures, no structure, little code refactoring, and intermixed code and HTML that is impossible to read and must be impossible to maintain.

It is a fascinating situation, and I wish I had a government grant to study the cause and effect. Is it that the *ad hoc* nature of the language encourages sites that grow from nothing without structure? Is it that the language is simple enough that people without solid programming backgrounds are enable to create complete web sites without having the fundamentals of code structure? Is it that the earliest versions of PHP required sucky code, and everyone since then has just used those samples and extended them even more?

### Conclusions 

I\'m not sure there are any conclusions yet. I\'m the kind of guy that likes trying new things, so I will probably run thorugh a few more architectures before I\'m done, and I hope I remember to add my thoughts to this page. For now, I use Webware as the appserver, with Cheetah for the templating. I\'m a happy camper, and a Python believer.

### Comments/Discussion 

I welcome your comments, disagreements, and your own experiences. That\'s the fun of a wiki.

\-- [TimRoberts](./TimRoberts.html) 2004-10-01

I started web programming on Linux/UNIX systems with PHP, but quickly became disgusted with the messes I created. Maybe PHP can be used in a more object-oriented way, but it certainly doesn\'t lend itself to managable applications. The end result usually looks like one large monolithic hack.

I totally concur with Daniel Robbins when he said \"if you haven\'t started using Python yet, you\'re only hurting yourself.\" Webware is a bit tough for a newbie, but it really does take advantage of Python\'s extensibility. The only real plague is not having a standard way to set it up in a shared hosting environment.

\-- [EricRadman](./EricRadman.html) 2004-10-01

My evolution in web programming is similar: *Perl -\> PHP2 -\> PHP3 -\> Python CGI + HTMLgen -\> Webware -\> Webware + Cheetah* always with `PostgreSQL`{.backtick}. I totally agree with the statement concerning the maintainability of average PHP code (my own projects are definitely no exception). In my experience Python + Webware + Cheetah build a stable and performant platform for websites and applications.

The often criticized diversity of the python web programming projects is a \"paradise of choice\" for me. Maybe the only thing we need is a good decision support for beginners. Something like a document or website saying:

- If you are new to programming or python, take a look at: [Zope](Zope), Plone, [PythonWebModules](PythonWebModules), \...

- If you want to dig into network programming, take a look at [TwistedMatrix](TwistedMatrix), \...

- If you want to have an environment containing application server, servlets, python server pages etc. take look at [Webware](./Webware.html), \...

- If you want a self-contained environment (including http server etc.) take a look at [Zope](Zope), [TwistedMatrix](TwistedMatrix), [CherryPy](CherryPy), \...

- \...

IMHO the necessity of choice could turn from confusion to pleasure when you can make your decision on a solid foundation when confronted with the wide range of great python web projects.

\-- [AndiPoisel](./AndiPoisel.html) 2004-10-06

I\'ve spent a lot of time over the last few months researching how best to use my Python skills to develop a website. This is one of the few articles that actually dares to choose which application(s) are the best. Thank-you for taking the time to write this. (I\'m glad you like Cheetah because that is where my research leads me also).

\-- [StephenDay](./StephenDay.html) 2005-19-04

Would be nice to add [PythonServletEngine](./PythonServletEngine.html) [http://nick.borko.org/pse](http://nick.borko.org/pse) (\"PHP in Python\"). It seems much easier than templating in PTL, Cheetah, PSP or HTMLgen.

\-- [MichalGajda](./MichalGajda.html) 2005-20-04

A number of frameworks can be run with mod_python (rather than as their own standalone server), and are listed on the [ModPython](ModPython) page.

\-- [JohnGabriele](JohnGabriele) 2006-01-26

How does this compare to [Django](Django), [TurboGears](TurboGears), other more recent Python web components, i.e. [Kid](./Kid.html), [Myghty](./Myghty.html), and even Ruby on Rails?

\-- [MikeSchinkel](./MikeSchinkel.html) 2007-02-20
