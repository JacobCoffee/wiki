# JythonSprint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

## Redirection 

We\'re moving this page to the official [JythonSprint](http://wiki.python.org/jython/JythonSprint) page on the Jython wiki.

## Rationale 

Jython is certainly a juicy project: it's still actively used, there are interesting technical challenges, and in this one, we see substantial organizational challenges to overcome as well.

## Some other targets 

[http://wiki.python.org/jython/JythonDeveloperGuide/PleaseAdoptMe](http://wiki.python.org/jython/JythonDeveloperGuide/PleaseAdoptMe)

## Design Ideas 

This is the result of some ideas from the sprint on Jan 6. Our overall thinking was based on the premise of unification and reuse:

- Unification. Try to bring Jython into the main branch of CPython development, to avoid chasing what's going on there. There's simply too much to catch up on. This means updating the grammar, getting more of the Python standard library that is pure Python running on Jython, etc.

- Reuse. What can Jython use from the Java ecosystem, especially other dynamic languages. As we will see, this means mostly frameworks for bytecode engineering, specifically [ASM](http://asm.objectweb.org/).

Note that unification without 2.5 is not without controversy. In particular, an incremental approach might in fact be the best course of action.

### Keep JavaCC 

In the spirit of radical revolution, we looked at the feasibility of using CPython's new AST approach. (AST = abstract syntax tree, think of a specific snippet of Python code as a Lisp expression.) This is documented in [PEP 339](http://www.python.org/dev/peps/pep-0339/). This was motivated by the idea, why not just lift the grammar -- Python.asdl - from CPython 2.5 exactly. This is elegantly written and would allow for exact compliance. Seems like a nice idea!

Notice that some of Jython was generated using an older version of this new approach see: [http://svn.python.org/view/sandbox/trunk/ast/asdl_java.py?rev=40754&view=log](http://svn.python.org/view/sandbox/trunk/ast/asdl_java.py?rev=40754&view=log)

First, let's look at what's currently happening in Jython. Jython uses [JavaCC](https://javacc.dev.java.net/) and the related project [JJTree](https://javacc.dev.java.net/doc/JJTree.html). JJTree in particular is used to preprocess the JavaCC grammar (python.jjt), which is then compiled to python.jj, then to [PythonGrammar](./PythonGrammar.html).java (a standard YACCish state machine), and all of the AST nodes in ast/\*.java.

CPython 2.5 is using Zephyr's ASDL (Abstract Syntax Definition Language), which is a language for writing tree grammars. At first, we thought that it meant it was using Zephyr code generation -- and this is convenient, asdlGen supports both Java and C generation. But this is not in fact the case. The reason is very sound: to enable introspection of any ASTs, the module asdl_c.py generates nodes for the AST that are made out of standard Python internal data structures like [PyObject](./PyObject.html). But of course we are not interested in C data structures here. We also should mention that [Zephyr](http://sourceforge.net/projects/asdl) itself has not been updated in nearly 5 years on [SourceForge](SourceForge).

ANTLR is another approach, but this does not address the unification goal with CPython development.

Conclusion: we should simply update the JavaCC grammar in python.jjt.

However, we quickly realized that just like is done with ANTLR, we could immediately test this new version of the grammar for compliance, simply by parsing large numbers of Python source files. One potential corpus, in addition to the standard library: the Python Cookbook. Casual inspection of its entries suggests it would be a good coverage test.

Would it make sense to unify the actual AST nodes as well? We need to look at that too.

### Move to ASM for Bytecode Generation 

ASM has emerged as a standard library for manipulating and emitting bytecode. The analogy that might be used here is think of writing XML output. The first instinct is to DIY with print because it's so easy. But then consider entities, encodings, etc., and quickly one realizes that even just writing XML is a hassle without using packages like [ElementTree](ElementTree).

#### Removing Reflection 

ASM also readily enables what Dennis Sosnoski described as [classworking](http://www-128.ibm.com/developerworks/java/library/j-dyn0610/), a method of replacing reflection with bytecode generation, since this is what ASM directly supports. Comments in the current code, [PyJavaClass](./PyJavaClass.html).java, to support reflection suggest there's an [ancient (1997) bug](http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=4071957) lurking here. Is it possible to remove reflection then completely in favor of just a bit more bytecode generation? It would seem so.

#### Comparative Generation 

Here's a list of modules that perform bytecode generation in the respective languages:

- Jython. [CodeCompiler](./CodeCompiler.html).java

- Groovy. [AsmClassGenerator](./AsmClassGenerator.html).java

- CPython. compile.c

Some relevant resources:

- [Java VM specification](http://java.sun.com/docs/books/vmspec/2nd-edition/html/VMSpecTOC.doc.html)

### Fix a Compliance Target 

Regression testing against the CPython test suite is certainly a noble goal. Probably what will excite more interest are supported applications in Jython. Here's a list:

- Django

- [TurboGears](../web/TurboGears)

This follows what Charles Nutter observed about JRuby and Rails: [Setting a compelling goal](http://sourceforge.net/mailarchive/forum.php?thread_id=30988621&forum_id=5587)

### Replacing JythonC 

Kip Lehman noted in one post that his impression from sporadic reading of the jython-dev mailing list is that jythonc isn\'t going to be a workable part of 2.2.

Apparently the current implementation of jythonc has been abandoned, because the idea of translating to Java instead of Java bytecode turned out to be a bad decision.

The right decision is probably to provide for emitting Java bytecode persistently and providing runtime eval access to the Jython Jar, possibly via an embedding via the Jar Jar tool. A great discussion topic for the sprint!

- [Jar API](http://java.sun.com/j2se/1.4.2/docs/api/java/util/jar/package-summary.html)

- [Jar Jar Links](http://tonicsystems.com/products/jarjar/)

### Supporting select 

Various networking modules in the standard library do not work because of a lack of Posix style select. Java NIO has what looks like a close match in [java.nio.channels.Selector](http://java.sun.com/j2se/1.4.2/docs/api/java/nio/channels/Selector.html).

## Sprint Participation 

### Engineering 

Charlie Groves (jython committer) suggests:

I\'ve been starting people out with porting a Python module written in C to Jython as described in [http://wiki.python.org/jython/JythonDeveloperGuide/PortingPythonModulesToJython](http://wiki.python.org/jython/JythonDeveloperGuide/PortingPythonModulesToJython). Paul has been making a nice writeup of porting the csv module in more detail in his blog at [http://gushieblog.blogspot.com/](http://gushieblog.blogspot.com/)

I\'ve wanted to get unicodedata for a while since several things depend on it. If you\'ve got someone with some serious unicode experience that could be nice. We\'re moving to Java 1.4(or 5) for 2.3 so the select implementation could use Java\'s nio which would be much better than the current implementation. If someone has serious nio or select experience, that could be a good target.

You could also look at [http://wiki.python.org/jython/BiggerTasks](http://wiki.python.org/jython/BiggerTasks) for things to do. They\'re probably a little too much to pick up and do something significant with in one day, but if someone wants to get started before hand, there\'s a fair amount in there. Some of those are more involved than they appear at first glance, so I\'d run any selections from there past the list before embarking on them.

Kip Lehman:

### Jython status communication 

The likelihood that you, unless you are a core Jython developer, know what components are complete in Jython for a 2.2 release is quite small. Why? There appears to be no publicly available and easily digestible record of what is done, what is being worked on (and how far along it might be) and what remains to be done.

A starting point might be to segment the product into a handful of categories (with some subcategorization) and put up a red/yellow/green scoreboard for each item on the Jython web-site. What might those categorizations be? later\... There is a Jython wiki page that might be an appropriate target for this. Having some rudimentary form of project status tracking might be helpful in terms of bringing in additional help. If you don\'t know what needs to be done or fixed, you might not want to volunteer your time. Knowing specific areas or items that are in need of attention and have a close relationship to your area of interest/expertise could be a catalyst for involvement and action.

### Design 

Jim Baker: One insight I got from the Django-Oracle sprint is the value of design. Well, no one questioned that, but what we saw was the input of design even late into the process with respect to supporting Oracle. We had enough experts in the room to resolve definitively some open questions - or redress some ones that had not been done satisfactorily before. So some design issues to be addressed for Jython would be byte code translation of Python features, possibly via an intermediary like Janino; requisite modules; etc. (I was looking at the list of missing modules, and there was Bastion, disabled as of 2.3\...)

### Testing 

And if we are doing design up front, why not testing too ![;)](/wiki/europython/img/smile4.png%20";)") . So here\'s one addition to having an effective test-driven process. It would be nice if Jython were in the Pybots. I mean, why should Jython be chasing CPython constantly, when it comes to pure Python code? Complex projects like Twisted and Django have their dependencies too, and that\'s why they\'re in Pybots. My intuitive feeling is that Jython should not be converging on CPython 2.3 but on 2.6.

### Designate a champion 

As for a big sponsor, a white knight, my feeling is that is not going to happen until after some progress is made, if even then. (But Sun could still sponsor the [PyCon](../conferences/pycon/PyCon) sprint.) Still, if we get the participation of a company or group out there that\'s actively using Jython, that would add significant focus, just as Array Biopharma helped on the Django-Oracle sprint.

## Technical Wish List 

Kip Lehman:

strawman categories:

- core language capabilities (new style classes, slots, generators, etc.) Most of these are implemented in the alpha release.
- modules
- Java version compatibility
- installer
- GUI development/usage/examples
- Jythonc.
- Web related considerations (server side, client side?)
- applet related considerations (environment, howto, examples)

### Classpath / invocation environment issues 

Having observed the Jython mailing for some years, a repeated topic of confusion is one related to setting the CLASSPATH, using jars and how to properly reference jars/dirs in manifests. Providing a primer on how to operate using the different constructs and some pointers on the decision making process of when and how to use said constructs would be a valuable addition to the Jython community.

### Improving coverage and awareness of Jython environments 

- Jython 2.1 supports Java 1.2 through Java 1.5
- Jython 2.2x is slated to support Java 1.2? through Java 1.5 .
- Java 1.6 has either had an alpha release or such a release will occur within the next 3 months.

Identifying features and capabilities within Java 1.5 and 1.6 that would be candidates for exploitation from Jython or need documentation to introduce/explain them to Jython developers would be helpful and a good advertisement for Jython.

Results of running the Jython test suite on various platforms/ JVM versions could provide a one-stop shop for those wondering if Jython could work in their environment and also serve to display the wide range of Jython applicability.

### Jython installation package 

Unknown what state the 2.2x version is in. My recollection is that the 2.1 version was characterized as not being suitable for continued use. A Jython installation package that can:

1.  be configured/scripted for large scale installations (aka headless)
2.  offer novice users a GUI with helpful explanations of installation choices and the opportunity to return and modify those choices (aka headed)

would be a important component in polishing the Jython image. It could be that most of the work for the new installer is done and that testing activities would be the most important contribution.

o Jython and web-services / SOAP

Python SOAP implementations seem to offer only limited coverage and the documentation can be somewhat difficult to comprehend.

Java web-services implementations seem to have a wider range of capabilities and larger operational acceptance. Leveraging some of the better Java web-services products with Jython might be a niche that could widen and diversify the Jython community.

## Resources 

- [Developers\' FAQ](http://www.jython.org/Project/devfaq.html)

- [Developers\' Guide](http://www.jython.org/Project/devguide.html)

## Supporting Comments 

- Matt Boersma. I\'d like to help, especially if it involves getting at least Python 2.3-level support. I wrote a large EJB/Swing app all in jython 2.1 a few years ago, and it was fast enough and much more pleasant than writing the equivalent Java code. Plus, we can\'t let the Rubyists get ahead of us. :- )
- Bill Simons. Yes! I\'m a fan of jython and it\'s been disappointing to see it lagging behind the other python implementations. Probably like a lot of other bellyachers I\'m not sure I have the time or energy to make a significant contribution to its development, but a sprint sounds like a good way to get our feet wet.
