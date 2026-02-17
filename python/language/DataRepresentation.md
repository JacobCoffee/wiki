# DataRepresentation

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Data on the web 

There are several approaches to represent data using Python on a web page (see [WebProgramming](WebProgramming)).

- [PythonInWebPage](PythonInWebPage)

- [StructureAnnotation](StructureAnnotation)

- [Programmatic](Programmatic)

Another interesting article about this is [\"Choosing a Templating System\"](http://www.perl.com/pub/a/2001/08/21/templating.html).

### Syntax 

Different approaches lead to different design decisions. Often it is the principal reason that new template systems get invented:

- [ElementBasedSyntax](ElementBasedSyntax)

- [CommentBasedSyntax](CommentBasedSyntax)

- [AttributeBasedSyntax](AttributeBasedSyntax)

### Examples 

Some presentation systems fall neatly into the categories above. Others are less easy to classify but have a closer association to one category than the others.

#### PythonInWebPage 

- Castalian

- [Cheetah](Cheetah)

- PSP (from [Webware](./Webware.html))

- [Spyce](Spyce)

#### StructureAnnotation 

- [ClearSilver](ClearSilver)

- DOMTemplate (from [TwistedMatrix](TwistedMatrix))

- DTML (Document Template Markup Language - see [Zope](Zope))

- [Woven](http://www.twistedmatrix.com/documents/howto/woven) (from [TwistedMatrix](TwistedMatrix))

- wt (see [JonsPythonModules](JonsPythonModules))

- ZPT (Zope Page Templates - see [Zope](Zope))

#### Hybrids 

- CHTL and CGTL (from [CherryPy](CherryPy)) - [PythonInWebPage](PythonInWebPage) and [StructureAnnotation](StructureAnnotation)

- [PyMeld](PyMeld) - [StructureAnnotation](StructureAnnotation) and [Programmatic](Programmatic)

- [STML](./STML.html) (from [SkunkWeb](SkunkWeb)) - [PythonInWebPage](PythonInWebPage), [StructureAnnotation](StructureAnnotation), and [Programmatic](Programmatic) being all equally apt (or equally inadequate)

#### Programmatic 

- PTL (from [Quixote](Quixote))

### Notes 

Feel free to add more abstract descriptions and more examples to help people decide what they are looking for!

Do you need to use full-fledged python, embedded bits of definitions but no functions \-- there is a range of options depending on your problem. Sometimes there\'s no python in \"the output page\" \-- as in raw documents put thru a filter. Or there may be limited amounts of embedded python \-- as in YAPTU and other filters. Or python may be the matrix language, with text embedded within it. Your handler code can be anything from a substituter (using, say, regular expressions to catch things to be altered) to a mini python engine. See [\'Python Journal 3(1)\'](http://pythonjournal.cognizor.com) a feature article that draws together several of the options above into a series on the pure-text to pure-python \"dimension\". See what your options are.
