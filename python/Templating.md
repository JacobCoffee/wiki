# Templating

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Templating in Python 

Templating, and in particular web templating is a way to represent data in different forms. These forms often (but not always) intended to be readable, even attractive, to a human audience. Frequently, templating solutions involve a document (the template) and data. Template usually looks much like the final output, with placeholders instead of actual data (or example data in simplified form), bears common style and visual elements. Data which is presented using that template may be also separated in two parts - data required to be rendered, and data required for template itself (navigation elements if it is a site, button names if it is some UI). Combining template+data produces the final output which is usually (but not always) a web page of some kind.

## Templating Engines 

There are many, many different HTML/XML templating packages and modules for Python that provide different feature sets and syntaxes. These libraries usually assume that you know how to write HTML or XML.

The number of templating engines is so great because the mechanisms involved are pretty easy to write in Python, at least for a fairly basic template engine; [this recipe from the Python Cookbook](http://code.activestate.com/recipes/52305/) shows how easy it is.

### Engines using Value Substitution 

The simplest form of templating engine is that which merely substitutes values into a template in order to produce the final output. They sometimes provide tags for if statements or loops, but they are crude.

- [string.Template (python 3.x)](https://docs.python.org/3.4/library/string.html#template-strings) in the python standard library.

- [stringtemplate](http://www.stringtemplate.org/) - employs recursion in order to provide support for complicated templating whilst avoiding side-effects

- [mustache](http://mustache.github.com/) - logic-less templates based on [CTemplate](http://code.google.com/p/google-ctemplate/) with implementation in many languages including Python

- [ctemplate-python](https://github.com/mll/ctemplate-python) - fast templating with simple if/loop logic based on [libCtemplate](http://libctemplate.sourceforge.net)

### Engines Mixing Logic into Templates 

A popular approach with templating engines is to embed logic or control-flow statements into the templates themselves in a way that can make the the final output appear rather different from the original template. For example:

    <table>
      <%
      for item in items:
        %>
        <tr>
          <th>Name</th>
          <td><%= item.name %></td>
        </tr>
        <%
      %>
    </table>

The introduction of such logic may also cause problems for some XML-based tools. Despite these shortcomings, such templating engines may be more applicable to non-Web templating problems or for situations where separating logic from content may actually make the solution harder to understand.

- [Airspeed](http://airspeed.pythonconsulting.com/) - Velocity Templates for Python

- [Castalian](Castalian)

- [Chameleon](http://chameleon.readthedocs.org/en/latest/) - fast page template implementation which compiles markup templates into python byte code. Used by Pyramid, Zope, Plone and Grok projects.

- [Cheetah](Cheetah)

- [CubicTemp](CubicTemp)

- [Django template system](https://docs.djangoproject.com/en/1.6/topics/templates/)

- [Elements](http://www.nthwave.net/elements/)

- [EmPy](EmPy)

- [Evoque page on pypi](https://pypi.python.org/pypi/evoque) - managed eval-based full-featured templating engine, for Python 2.4, 2.5, 2.6 **and 3.0**, features such as unicode, dynamic overlays, *format-extensible* automatic quoting, in-process sandbox, et cetera, while still remaining small, simple and extremely fast \-- performance benchmarks show it to be more or less as fast as Mako, and faster on simpler templates.

- [HRL (HTML Redemption Language)](http://blog.aerojockey.com/post/hrl) - Powerful macro preprocessor for HTML; macros can embed arbitrary Python code. ( **2010-07-04, Officially discontinued**)

- [Genshi](http://genshi.edgewall.org/) - XML-based templating engine, used in the popular python tool [trac](./trac.html). *Performance tests show that it is the fastest of all xml based templating engines in Python.*

- [Jinja 2](http://jinja.pocoo.org/) - an extensible, sandboxed text-based templating engine with Django-like syntax (but faster).

- [Ashes](https://github.com/mahmoud/ashes#ashes) - A Python 2/3-compatible version of [the Dust templating language](http://akdubya.github.io/dustjs/), implemented in a single file, also usable through a built-in CLI. Enables template reuse on the frontend through Dust.js.

- [Mako](http://www.makotemplates.org/) - a fast, non-xml, templating engine based on ideas from Myghty.

- [moody-templates](https://github.com/etianen/moody-templates) - A fast, extensible templating engine for Python 3 with Django-like syntax.

- [Myghty](http://www.myghty.org/) inspired by Perl\'s Mason, replaced by Mako and [MyghtyUtils](http://www.python.org/pypi/MyghtyUtils).

- [Qpy](https://www.mems-exchange.org/software/DurusWorks/) provides a convenient mechanism for generating safely-quoted html text from python code. It does this by implementing a quoted-string data type and a modification of the python compiler.

- [Quik](http://quik.readthedocs.org/) - A fast and lightweight Python template engine

- [PML](http://codingrecipes.com/pml-a-python-template-engine) is a high performance template engine implemented in Python, it supports many advanced features such as template filters, output filters, and more.

- [pyratemp](http://www.simple-is-better.org/template/pyratemp.html) - a very small (\<500 LOC) but complete template-engine, using restricted python-expressions. There are also some [benchmarks and comparisons](http://www.simple-is-better.org/template/) of different template-engines.

- [Spitfire](https://github.com/youtube/spitfire) - A super fast [Cheetah](Cheetah)-like template system used by [YouTube](https://www.youtube.com/).

- [Spyce](Spyce)

- [SUIT](https://pypi.python.org/pypi/suit/) - powerful template engine that allows one to define their own syntax to transform templates by using rules.

- [Tempita](http://pythonpaste.org/tempita) - a fairly simple, small templating language with full Python expressions

- [Template Toolkit](http://tt2.org/python/index.html) - Python port of Perl template engine

- [Templet](http://davidbau.com/templet) - a 90-line BSD-licensed utility that defines \@stringfunction and \@unicodefunction python function decorators for simple, robust, and speedy templating.

- [Templite+](http://www.joonis.de/content/TemplitePythonTemplatingEngine) - A light-weight, fully functional, general purpose templating engine

- [Tenjin](http://www.kuwata-lab.com/tenjin/) is a fast template engine implemented in pure Python. Some benchmarks have shown it to be about x2 faster than Mako, x3 than Cheetah, x9 than Django, x60 than Kid in some situations. However [50% slower](http://mindref.blogspot.com/2012/07/python-fastest-template.html) wheezy.template.

- [Texthon](http://texthon.chipsforbrain.org) - Python-eval based template engine with a focus on generating readable code.

- [thrases](http://www.sourceforge.net/projects/the-next-please) - format-free Python needing just needing a reserved string (default: \~\~) for separating phrases. Template.init() analyses, which phrases are python and which not, building a python script for exec(). This script is containing only minimal overhead then - Template.render() is near to the theoretical maximum speed. Template.render() can also write directly on a file descriptor for improved performance.

- [Tonnikala](https://github.com/tetframework/Tonnikala) - XML syntax that is very close to that of Kajiki. Tonnikala writes code as Abstract Syntax Trees and optimizes the resulting trees extensively

- [trender](https://github.com/transceptor-technology/trender) - A fast, simple and stand-alone Python template engine.

- [wheezy.template](https://bitbucket.org/akorn/wheezy.template) is written in pure Python code. It is a lightweight template library. The design goals achived:

  - Compact, Expressive, Clean: Minimizes the number of keystrokes required to build a template. Enables fast and well read coding.

  - Intuitive, No time to Learn: Basic Python programming skills plus HTML markup. You are productive just from start. Use full power of Python with minimal markup required to denote python statements.

  - Do Not Repeat Yourself: Master layout templates for inheritance; include and import directives for maximum reuse.

  - [Blazingly Fast](http://mindref.blogspot.com/2012/07/python-fastest-template.html): Maximum rendering performance: ultimate speed and context preprocessor features.

### Engines with Annotated Templates 

The following engines feature template documents whose sections are marked using special attributes (or, less frequently, special elements or tags). For example:

    <table annotation:element="items">
      <tr annotation:element="item">
        <th>Name</th>
        <td>{name}</td>
      </tr>
    </table>

In some systems, the sections are then manipulated within program code; in others, the template structure indicates sections which are to be repeated, omitted, and so on, and the templating system then merges the template with some data structure provided by the program. Generally, the reason for annotating templates in this way (particularly through the use of attributes) is to better support the editing of such templates in XML-based tools which might otherwise complain about or damage template information if it were not included carefully in documents.

- [ClearSilver](ClearSilver) - uses special elements/tags

- [HTMLTemplate](http://sourceforge.net/projects/py-templates//) - special attributes denote HTML elements that can be manipulated as Python objects (**As of 2013-12-05, this project is no longer under active development.**)

- [JonsPythonModules](JonsPythonModules) - uses special comment-like markers

- [meld3](http://www.plope.com/software/meld3/) and [PyMeld](http://www.entrian.com/PyMeld) are very similar

- [Pyxer](https://github.com/holtwick/pyxer) - based on Genshi parser engine. Optimized for work with Google App Enginge (GAE)

- [pso](pso)

- [Sprite](https://web.archive.org/web/20060819140627/http://pytan.com/public/sprite/) - uses special comment-like markers

- [teng](teng) - uses processing instruction-like markers

- [webstring](http://psilib.sf.net/webstring.html) - uses attributes in XML/HTML templates and a specific character in text templates

- [XSLTools](https://pypi.python.org/pypi/XSLTools) - uses special attributes (with XML documents providing the data)

- [PyPa](http://gna.org/projects/pypa) - nested comment-delimited blocks that are accessible from Python code as objects.

- [TDI](http://opensource.perlig.de/tdi/) - Manipulate tagged HTML/XML elements with normal Python code. Fast.

In other systems, the annotations are actually evaluated in order to produce repeated sections, to omit or include sections, and so on:

- [Genshi](http://genshi.edgewall.org/) - Template engine inspired by Kid, supports both [XML](http://genshi.edgewall.org/wiki/Documentation/xml-templates.html) and [plain-text](http://genshi.edgewall.org/wiki/Documentation/text-templates.html) templates

- [kajiki](http://sourceforge.net/p/kajiki/home/) - Template engine inspired by Genshi

- [htmltmpl](http://htmltmpl.sourceforge.net/) - uses HTML-like elements/tags and supports compilation

- [Kid](https://pypi.python.org/pypi/kid/) - XML based, compiling template engine

- [SimpleTAL](http://www.owlfish.com/software/simpleTAL/) - introduces a certain amount of logic but in an XML-compatible fashion

- [CherryTemplate](http://sourceforge.net/projects/cherrypy/) - is a Pythonic HTTP toolkit.

## HTML Shorthand Processors 

The libraries in this section implement simpler markup languages that can be automatically converted to HTML. This lets you avoid having to write HTML by hand.

- [AsciiDoc](http://www.methods.co.nz/asciidoc/)

- [Markdown](https://pypi.python.org/pypi/Markdown)

- [PyTextile](PyTextile)

- [reStructuredText](reStructuredText)

- [txt2tags](http://txt2tags.sourceforge.net/)

- [PottyMouth](https://pypi.python.org/pypi/PottyMouth/2.2.1) (for untrusted text input)

- [Creole](http://code.google.com/p/python-creole/) (creole to html and html to creole)

## Template engines implemented as Internal DSL\'s 

These engines are implemented as an internal DSL, that is, they don\'t process text into markup, rather they represent the final document as actual Python code and data structures. See: [An overview of the benefits of this internal DSL approach vs external template languages](http://bitbucket.org/tavisrudd/throw-out-your-templates/src/tip/throw_out_your_templates.py)

- [Stan](http://docs.g-vo.org/meetstan.html)

- [Brevé](http://breve.twisty-industries.com/)

- [Dirty](http://dirty.googlecode.com/)

## HTML Generation Packages 

**Many of these links are dead. Perhaps someone more knowledgeable might want to fix or prune them.**

These packages are not really templating systems in that they do not typically employ a template document as such to define the form of the output they produce, but they can be useful in applications where it is more convenient to programmatically generate output.

- [WebElements](http://www.webelements.in/) allows creating html documents using python objects that represent their DOM equivalents, inspired by QT.

- [Genshi](http://genshi.edgewall.org/) The genshi.builder module provides [simple markup generation](http://genshi.edgewall.org/wiki/Documentation/builder.html)

- [HTMLgen](https://packages.debian.org/sid/python-htmlgen) A old-school module first written for Python 1.x. Debian\'s package maintainers\' patches bring it into the twenty-first century with Python 2.7 compatibility. [Mirrored](https://github.com/dbohdan/HTMLgen) on [GitHub](./GitHub.html).

- [webhelpers.htmlgen](https://web.archive.org/web/20080914004317/http://pylonshq.com/WebHelpers/module-webhelpers.htmlgen.html) Kind of like HTMLGen, only much simpler. Like stan, only not.

- [html](https://pypi.python.org/pypi/html) Provides a simple syntax to generate HTML, XHTML and XML.

- [HTMLTags](http://code.activestate.com/recipes/366000/)

- [HyperText](https://web.archive.org/web/20070202041542/http://dustman.net/andy/python/HyperText/)

- [markup](http://markup.sourceforge.net/) A light-weight and flexible HTML/XML generator

- [XIST](http://www.livinglogic.de/Python/xist/)

- [pyhtmloo](http://pyhtmloo.sourceforge.net/) pyhtmloo is a library that allows python developers to use HTML code like any other python objects.

- [Yattag](http://www.yattag.org/) Provides a readable way to write HTML or XML within Python using indented blocks instead of \<tag\>\...\</tag\> constructs.

## Static Website Generators 

Static website generators are more than templating engines in that they create *the whole site structure*, not just individual files. While templating is an important part of their function, determining the site structure and *incorporating structural information* in the output (for example to automatically generate navigational elements) is what really makes a static website generator a useful tool.

See [StaticSiteGenerator](StaticSiteGenerator) for the list.

## Java Templating Engines 

The following templating engines are accessible or usable via Jython:

- [FreeMarker](http://freemarker.org/index.html) (with Jython data binding)

- [Java Server Pages, JSP](http://www.oracle.com/technetwork/java/jsp-138432.html)

- [Velocity](http://velocity.apache.org/)

- [WebMacro](http://www.webmacro.org/)

## CPython-accessible C Templating Engines 

- [ClearSilver](ClearSilver) - HTML generation, uses HDF as input format

------------------------------------------------------------------------

[CategoryTemplate](CategoryTemplate)
