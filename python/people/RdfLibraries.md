# RdfLibraries

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# RDF Libraries for Python 

There are several [RDF](http://esw.w3.org/topic/RDF) processing libraries for Python, however many seem abandoned. [RdfLib](https://rdflib.readthedocs.io/en/stable/) is the primary library that is still maintained.

Active:

- [RdfLib](https://rdflib.readthedocs.io/en/stable/) (see [RdfLib](RdfLib)) - Has utilities for constructing triplestores, loading and parsing rdf, searching, and other functions.

  - [Actively maintained](https://pypi.org/project/rdflib/#history) as of late 2023

  - Easily installed with pip, pure python implementation

- [SparqlWrapper](https://sparqlwrapper.readthedocs.io/en/latest/) is provided by RDFLib and provides utilities for querying a sparql endpoint (such as an RDF4J triplestore) from Python and parsing output

  - [Latest release](https://pypi.org/project/SPARQLWrapper/#history) (as of Oct. 2023) in 2022

Abandoned:

- [Oort](http://oort.to/overview.html) is a toolkit using rdflib, Paste and Genshi, focusing on Web views of RDF graphs.

  - [Last release](https://pypi.org/project/Oort/) was 0.4 in 2007

- [RedlandRdf](./RedlandRdf.html) - [http://librdf.org/docs/python.html](http://librdf.org/docs/python.html) -

  - Redland is a python \[and other-lang\] wrapper around a C library.

  - The interface is not as pythonic as rdflib, but \"feels\" about the same.

  - Redland uses Raptor for parsing/serialization; Raptor supports NTriples, RDF/XML, Turtle, RSS, Atom.

  - [Latest release](https://librdf.org/NEWS.html) around 2014

- [Rx4RDF](./Rx4RDF.html) - [http://rx4rdf.liminalzone.org](http://rx4rdf.liminalzone.org) - is an application stack for building RDF-based applications and web sites. It uses either 4Suite, rdflib or [RedlandRdf](./RedlandRdf.html) as the RDF store and layers on the following:

  - [RxPath](./RxPath.html) lets you query, transform and update RDF using familar XML technologies like XPath, XSLT and XUpdate.

  - Raccoon is a simple application server that uses an RDF model for its data store, roughly analogous to RDF as [Apache Cocoon](http://cocoon.apache.org) is to XML.

  - Rhizome is a content management and delivery system that runs on Raccoon that treates everything (structure and content) as RDF and lets you edit the RDF in a Wiki-like fashion.

  - [Latest release](https://pypi.org/project/rx4rdf/#history) around 2004

- [SemanticWebApplicationPlatform](./SemanticWebApplicationPlatform.html) - [http://www.w3.org/2000/10/swap/](http://www.w3.org/2000/10/swap/) - has a lot of stuff, feels like a big lump of code with little differentiation - looks great, but, what is it?

  - It\'s a big lump of code. ![:)](/wiki/europython/img/smile.png ":)") It\'s the W3C-semweb-hacker\'s playground.

  - It has migrated to [github](https://github.com/linkeddata/swap), but is described as historic

  - [Last formal release](https://github.com/linkeddata/swap/tags) in 2007, but updated in 2022

  - Primary contributor is Tim Berners-Lee

- [sqltriples](http://www.python.org/pypi/sqltriples) is a triple store implementation which uses relational databases to offer transactional storage and enhanced querying.

  - [Latest release](https://pypi.org/project/sqltriples/#history) in 2007

## Editorial Notes 

The above lists should be arranged in ascending alphabetical order - please respect this when adding new entries. When specifying release dates please use the format YYYY-MM-DD.
