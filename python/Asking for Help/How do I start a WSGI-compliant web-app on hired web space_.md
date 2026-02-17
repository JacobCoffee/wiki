# Asking for Help/How do I start a WSGI-compliant web-app on hired web space?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help/How do I start a WSGI-compliant web-app on hired web space? 

I have some web space to play with, and I want to use it to teach myself python programming for the web. The Python docs ([http://docs.python.org/howto/webservers.html](http://docs.python.org/howto/webservers.html)) say I should write a WSGI compliant app, but every piece of documentation I read about WSGI or one of the frameworks, suggests running a new process on some port number to act as a web server. This obviously isn\'t possible on the web space I rent. They have an apache installation, and I need to co-operate with it. If someone could point me in the direction of some documentation that will help me make a start, or show me how a WSGI-compliant \'Hello World\' application can be built on a machine I don\'t own, or even tell me which (well documented) framework doesn\'t require owning the machine, I would be very grateful.

------------------------------------------------------------------------

If the Apache installation doesn\'t support [mod_wsgi](http://code.google.com/p/modwsgi/), and if you can\'t have long-running processes for various [Web frameworks](WebFrameworks), then you may have to start off deploying your application using CGI and then see how you get on. Fortunately, you can write WSGI applications and then decide how to deploy them - you won\'t need to rewrite everything - so not having mod_wsgi support isn\'t necessarily a problem. Once you have an application ready, or as you\'re testing your first \"hello world\" application, you just need to find a suitable program that can launch your WSGI code from a CGI environment.

For this launcher program, one thing to look at might be the [wsgiref](./stdlib(3a)wsgiref(2e)html.html) module that is available in Python from version 2.5 onwards. You can write a very simple program that uses `wsgiref`{.backtick} to launch your application, and the [CGI deployment instructions for Werkzeug](http://werkzeug.pocoo.org/docs/deployment/cgi/) provides a suitable template.

So, to summarise\...

1.  Get your WSGI application ready, probably starting with a \"hello world\" test.

2.  Make a simple launcher program using `wsgiref`{.backtick} and customise it to use your application.

3.  Deploy the launcher in a CGI directory on the server.

You may need a few attempts to get it working. The hard part is often to configure the CGI script to be executable by the server and to be able to find your application and any libraries that you use. Your hosting provider may have some useful information about this.

Good luck! \-- [PaulBoddie](PaulBoddie) 2012-07-05 20:53:40

------------------------------------------------------------------------

Brilliant, thanks. My *hello world* is working now. \-- [hughcharlesparker](./hughcharlesparker.html) 2012-07-08 14:42:55

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
