# Karrigell

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### Masthead 

URL:: [http://www.karrigell.com](http://www.karrigell.com)

version::3.1 (*2010-04-25*)

licence::BSD revised

platforms::any platform that supports Python 2.3

Python versions::2.3 and above

### Deployment Platforms 

No requirement besides Python : Karrigell is provided with a web server and a Python database engine ([PyDbLite](./PyDbLite.html)). It can also run behind Apache (CGI mode or mod_python) an any web server that supports proxy mode

### Suitability 

Web programming with all the usual tasks (session management, cookies, user management, etc)

### Development Interfaces 

Servlet-style : the scripts, either pure Python or mixing HTML and Python, are executed in a namespace which provides all useful information, including HTTP headers, authentication data, etc. For instance, form fields are available as the REQUEST dictionary, or with a variable available in the namespace

The namespace also provides custom exceptions to stop its execution, such as HTTP_REDIRECTION (see the on-line documentation)

A function Include(script_or_file, \*\*args) allows the inclusion of an html file or of a file inside a script. If script B is included inside script A, it is executed in script A\'s namespace ; additional \*\*args can be added to this namespace

### Environment Access 

Standard Python mechanisms : environment data is available in the namespace where scripts are executed

### Session, Identification and Authentication 

Provided through functions available in scripts

Session() returns a session object, to which attributes can be set (arbitrary Python objects : user login, database connexion and cursor, etc.)

A user management framework allows the site administrator to manage a user database with roles(admin, editor, visitor). In scripts, function Login(role) checks if the user is logged in with the specified role, or redirects to an authentication script ; Role() returns user\'s role

### Persistence Support 

Karrigell is provided with the pure-Python [PyDbLite](./PyDbLite.html) database engine. It can be linked to all databases for which there is a Python API (SQLite, MySQL, PostGres, etc)

### Presentation Support 

- Python scripts, where the \"print\" statement is used to send output to the client

- \"Karrigell services\" : Python scripts where functions are mapped to URLs (allows to build a whole site with just one script)

- \"Python Inside HTML\" (PIH) which looks like PHP, ASP, etc : HTML code with Python code inserted inside \<% and %\>, with shortcuts for variables : \<%= myVar %\> and for translated strings which use the gettext mechanism (for which Karrigell provides a simple interface) : \<%\_ \"string to translate\" %\>

- \"HTML Inside Python\" which are Python scripts, except that the lines beginning with a string are sent to standard output as if there were a \"print\" statement before

- plain CGI scripts, running much faster than usual because the interpreter is not loaded for each request

### InTheirOwnWords 

Karrigell aims at simplicity for web developers :

- a built-in web server, interfaces to run behind Apache

<!-- -->

- no configuration needed to get started ; on Windows, an installer allows running an application from an USB drive, even on PCs without Python installed
  - a namespace for Python scripts in which developers will find all useful data and functions for the most ordinary tasks
  - a way to nest pages and scripts with the Include() function

The inspirations were EasyPHP, a package which provides Apache, PHP, mySql and PHPmyAdmin all in one, and saves the pain of installing each of them and make them all work together ; the wittily named Poor Man\'s Zope (PMZ) which showed how easy it was to make Python servlets (unfortunately unmaintained) ; and the pleasure I have programming things in Python

Performance and stability have been very much improved since the first versions. Karrigell can now be safely used in production environments

### Comments 

### Hosting 

[WebFaction](http://www.webfaction.com) supports Karrigell

All web hosts using Apache and allowing CGI scripts can support it
