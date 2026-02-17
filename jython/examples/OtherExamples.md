# OtherExamples

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Other Examples in Jython 

[DocumentationAndEducation](DocumentationAndEducation)

------------------------------------------------------------------------

### Log4j 

- This is a simple [Log4jExample](Log4jExample) that show how to use this excellent logger with Jython. Yes, Python provides a logger but log4j can be used for debugging apache stuff. What ever you use loggers use its better then using print statements. You can get log4j from [http://logging.apache.org/log4j/1.2/download.html](http://logging.apache.org/log4j/1.2/download.html)

### Apache Poi 

- No this isn\'t really bad Hawaiian food but a really slick way to write out Excel xls and other Microsoft Office format files with out have to have any microsoft software installed. Poi is really slick Java API and pretty easy to use. Take a look at the [PoiExample](PoiExample) and to download it and get more information on Poi and visit [http://poi.apache.org/](http://poi.apache.org/)

### PyServlet 

See [Sean McGrath\'s PyServlet Turorial](http://seanmcgrath.blogspot.com/JythonWebAppTutorialPart1.html) for an introduction. Below are a couple of examples:

Simple:

:::: 
::: 
``` 
   1 from javax.servlet.http import HttpServlet
   2 
   3 class Simple(HttpServlet):
   4     def doGet(self, request, response):
   5         response.setContentType("text/plain")
   6         response.getWriter().println("Veni, vidi, vici!")
```
:::
::::

Using servlet context:

:::: 
::: 
``` 
   1 from javax.servlet.http import HttpServlet
   2 
   3 class Simple(HttpServlet):     
   4     def doGet(self, request, response):
   5         response.setContentType("text/plain")
   6         response.getWriter().println(self.getServletContext().getServerInfo() +
   7                                      " Veni, vidi, vici!")
```
:::
::::

### Apache Derby 

[ApacheDerby](ApacheDerby) Example(s)

Apache Derby is a Java relational database management system that can be embedded in Java programs and used for online transaction processing. for more information on Apache Derby see [http://db.apache.org/derby/index.html](http://db.apache.org/derby/index.html) or [http://en.wikipedia.org/wiki/Apache_Derby](http://en.wikipedia.org/wiki/Apache_Derby)

### BioJava 

Bioinformatic analysis using [BioJava](http://biojava.org) can be simplified using Jython. A Genbank file, like the ones used to describe chromosomes in the Human Genome can be open and parsed with a few lines of Jython.

    import sys
    from java.io import *
    from java.util import *
    from org.biojava.bio import *
    from org.biojava.bio.seq.db import *
    from org.biojava.bio.seq.io import *
    from org.biojava.bio.symbol import *

    if __name__ == "__main__":
        br = BufferedReader( FileReader( sys.argv[1] ) )
        sequences = SeqIOTools.readGenbank(br)
        while sequences.hasNext():
            seq = sequences.nextSequence()
            print seq.seqString()
