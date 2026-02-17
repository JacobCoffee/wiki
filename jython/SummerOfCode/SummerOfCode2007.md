# SummerOfCode/SummerOfCode2007

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Google Summer of Code 

Some project ideas that might work for Google\'s summer of code. The Python folks have [very good advice](http://wiki.python.org/moin/SummerOfCode) for submitting proposals.

## Potential Mentors 

- [FrankWierzbicki](FrankWierzbicki)

- [JimBaker](JimBaker)

- [CharlieGroves](CharlieGroves)

- [MikeTaylor](./MikeTaylor.html)

## AcceptedProjects 

### HelpSystem 

by Ryan Morillo, mentored by Charles William Groves

I would like to work on geting the help system to work on Jython, working on figuring out why the python help system doesn\'t automatically work, then either adjusting the CPython code so it works on both systems, or implimenting it nativly in Jython, barring either of those, writting it in Java and making it part of Jython distrobution. After getting help to work normally, I expect to work on Jythons import, to get it to pull the javadoc and translate it to python help in place with a lazy hook that is called with help()

- The main reasons I would like to work on this project are my enjoyment of the python language, being able to give something back to the first real language I learned, and adding a major tool to the proliferation of this wonderful tool for new programmers and developers needing the speed and information they require to use Jython to it\'s full potential. Some qualifications and experience: I have been a python evangelist for eight years, linux user for seven, Microsoft since dos 3.1, Java for two, and have recently finished my AA on my way to getting my B.S. in computer science or computer information systems (Undecided due to math vs. work and sleep) I\'ve mostly been self taught, but have vigorously pursued programming knowledge both in school, and by developing and reading my library of language references, data structure, theory, and domain specific books. Working for a multinational company, doing reports analysis work; I developed code to the point I worked myself out of the analyst job by generating the reports, documenting the interface and logic so that a secretary for the division was able to implement the project manager\'s changing needs so he was able to have the data in a succinct enough form that I was moved to another position at that company\'s command center.

### Python 2.5 Language Support in the JythonCompiler 

by Damien Lejeune, mentored by Michael Taylor

[JimBaker](JimBaker) and [MikeTaylor](./MikeTaylor.html) are currently working on adding 2.5+ **language** functionality to Jython. We are trying to limit the scope of this work, just as was done with the AST implementation in CPython 2.5:

- Write a generational grammar to build the desired AST in ANTLR 3. We may explore using a tree grammar to support enhanced visting. We think we might be able to just generate a comparable set of AST nodes as CPython, for enhanced compatibility. This is the easy part.

- Generate code using ASM; this would replace the current CodeCompiler.java. This would be the bulk of the work. There\'s some interaction with the rest of Jython, but not too much (we think). More importantly, we need to identify some best practices on mapping Python constructs to JVM byte code, basically updating what [JimHugunin](JimHugunin) worked out 10 years ago.

We\'re also looking at two additional enhancements:

- Move to using nested classes to represent methods. This just seems to be the right way to do it. Issues of [PermGen](./PermGen.html) seem to be just a red herring. We may be wrong, but it\'s the approach being taken by JRuby.

- Favor \"classworking\" instead of reflection. ASM provides support here; JRuby is also looking at caching the necessary stubs.

We would expect that there would be suitable subprojects in this that are suitable for the GSoC students. Some that come to mind:

- Facilitate Java calling Jython, via class/method decorators and possibly annotations.
- Construct translation, especially performance/correctness issues. (Subtle closure bugs still seem to be out there in CPython for example.)
- Stub cache
- Rolling up as part of the replacement to jythonc, using compileall, going to setuptools.

All of these have the advantage that they can be completed to a certain implementation, and still be useful.

### Python 2.5 Language support in Jython 

by Tobias Ivarsson, mentored by James Edward Baker

The JVM is a great platform, it is widely used, available on many devices and there are a lot of great libraries and applications available on the JVM. Python is a great programming language, it is well suited for rapid development, prototyping and agile development methods. Jython unites these two great systems. Sadly Jython is not in an up to date state at the present time. To aid this Jython needs to be brought to a state where it is compatible with the latest version of Python. That is what this project aims at. I will provide work on the parsing of Python code and generation of byte code for the JVM. Ideas for solutions can come from the latest CPython implementation, and other implementations of dynamic languages on the JVM, such as JRuby or Groovy.

### PyPy JVM backend advancements and integration with JSR-223 

by Paul deGrandis, mentored by Antonio Cuni

The recent advancements of [PyPy](./PyPy.html) have been impressive to say the least. Much work as been done to provide a JVM backend, but it still lacks full completion of finer details. The goal of my summer of code project will be to work at the remaining problems to achieve a level stability that is fitting to be used with JSR-223 (the Java Scripting addition) and Java6. Doing so will allow [PyPy](./PyPy.html) interoperability with Java, Scheme, Python, [JavaScript](JavaScript), Ruby, and many more languages that implement this JSR specification. Additionally, should time allow, an empirical experiment will be conducted to show the [PyPy](./PyPy.html)\'s affect on developer efficiency in an academic setting using the JVM backend and JSR-223 bridge.
