# Castalian

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

A framework for [WebProgramming](WebProgramming).

### Masthead 

URL

:   [http://www.kryogenix.org/code/castalian/](http://www.kryogenix.org/code/castalian/)

version

:   0.5 (*2002-07-01*)

licence
:   Python

platforms
:   Apache (developed on Linux, but should work with Windows etc too)

Python versions
:   2.0 or better

### Sample 

    <?cas
    response.write("And from the Castalian corner: Hello, World!<br>")
    ?>

### Deployment Platforms 

Should work with any Web server that supports CGI and Apache\'s Action directive \-- only tested on Apache/Linux.

### Suitability 

An easy way to embed Python in your HTML pages, Castalian is particularly suitable for coders used to Microsoft\'s Active Server Pages, as it provides (most of) the ASP object model \-- if you\'re used to using request.querystring, response.write and so forth, but want to code in Python, you\'ll love Castalian.

### Development Interfaces 

Presentation oriented \-- embed Python directly in your HTML pages, like PHP or Microsoft\'s ASP.

### Environment Access 

You have read access from the ASP-a-like request.servervariables, but you can also use the Pythonic os.environ to make changes if required.

### Session, Identification and Authentication 

Sessions are currently not supported.

### Persistence Support 

Outside Castalian\'s scope \-- persist objects as you would in any other Python application.

### Presentation Support 

HTML with embedded Python, which looks much like PHP. To run Python code in your pages, just enclose in \<?cas and ?\> tags.

### InTheirOwnWords 

Castalian is an engine that allows you to embed Python in HTML pages, and also provides (an approximation to) the Active Server Page object model. Documentation for the object model and Castalian generally is available with the package. Castalian is very easy to install \-- simply drop the CGI in place on your web server and point .cas files to it. This simplicity comes at a speed price, though; it is a little slower than frameworks that use mod_python or similar methods. This is unlikely to be a problem for sites not serving vast numbers of users. (sil \-- Castalian author)

### Comments 
