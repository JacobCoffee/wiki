# Asking for Help/How to run python from HTML

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: How to run python from HTML? 

I am looking for a way to link python to HTML but have not yet found one that suits my needs. What I want is that when my users use HTML code they put their name in a box and HTML sends that name to a python program that records it. I have no problem coding the python bit but how do I execute python script via HTML without going to a new page? Also does the python script have to be on the same PC as the website is hosted on, IE will it have to be on my hosting company\'s PC or can it be on one that is elsewhere but us on all the time with a port forwarded IP?

------------------------------------------------------------------------

The HTML will refer to the Python script using the `action`{.backtick} attribute on a `form`{.backtick} element - this is presumably what you mean by \"going to a new page\" - but you could actually publish your Python script at a particular URL and have that location as both the \"HTML\" and the script mentioned by the `action`{.backtick}. How this would work is as follows\...

1.  You set up your Web server to serve the script (as dynamic content, CGI, or whatever, but *not* as static content) for the chosen URL.

2.  You tell your users the URL of the service.

3.  The user enters the URL.

4.  The Web server invokes your Python script in order to serve the URL.

5.  The Python script checks for form data. Initially, there will be no form data, so the script should output the HTML page containing the form in response. Thus, the URL looks as if it just serves a static HTML page, but it is really a script doing the work.

6.  The user fills out the form and submits it.

7.  Here, if you used the URL of the script as the `action`{.backtick} (leaving it empty also works because the browser will just send the form data to the URL the form came from), the Web server will invoke your Python script again.

8.  The Python script will now have some form data and can validate it. In response, it can produce the same HTML page again, or it can produce another HTML page, making it seem that the page being served has changed.

I hope this makes sense. \-- [PaulBoddie](PaulBoddie) 2012-01-09 22:07:55

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp) [CategoryAskingForHelpAnswered](CategoryAskingForHelpAnswered)
