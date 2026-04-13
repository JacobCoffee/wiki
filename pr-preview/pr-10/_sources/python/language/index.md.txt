# Language Reference

This section covers Python language features, design patterns, standard library modules, and internal details like the AST and time complexity of built-in operations. It is a mix of explanations, proposals, and discussions -- some of it historical, some still useful as reference. If you want to understand how a particular feature works under the hood, or why Python made the design choices it did, look here.

## Core Language Features

- [Decorators](Decorators) -- syntax, use cases, and links to the decorator library on PyPI
- [Generators](Generators) -- how generator functions work and how to use them as iterators
- [Iterator](Iterator) -- the iterator protocol, `__iter__` and `__next__` explained
- [With Statement](WithStatement) -- discussion of PEP 343 and context managers
- [Abstract Base Classes](AbstractBaseClasses) -- the proposed Python 3K class tree
- [Switch Statement](SwitchStatement) -- historical proposals for adding switch/case to Python
- [Alternate Lambda Syntax](AlternateLambdaSyntax) -- community proposals for lambda alternatives before Python 3

## AST and Internals

- [AST](AST) -- overview of Python's Abstract Syntax Tree for source analysis
- [AST-Based Optimization](ASTBasedOptimization) -- performing peephole optimizations at the AST level instead of bytecode
- [Byteplay Documentation](ByteplayDoc) -- docs for the byteplay bytecode manipulation library

## Patterns and Design

- [Observer Pattern](ObserverPattern) -- implementing the observer pattern in Python
- [Adapter Registry](AdapterRegistry) -- a component that adapts one interface to another
- [Computed Attributes Using Property Objects](ComputedAttributesUsingPropertyObjects) -- using `property()` for computed attributes
- [Alternative Description of Property](AlternativeDescriptionOfProperty) -- another take on how Python properties work

## Configuration Parsing

- [ConfigParser](ConfigParser) -- overview of the ConfigParser module and its design
- [ConfigParser Examples](ConfigParserExamples) -- basic usage examples for configparser
- [ConfigParser Goals](ConfigParserGoals) -- separating in-memory config from persistent storage
- [ConfigParser Shootout](ConfigParserShootout) -- comparing ConfigParser alternatives and debating future directions

## Path Handling

- [Alternative Path Class](AlternativePathClass) -- directory-based path classes as an alternative to PEP 355
- [Alternative Path Discussion](AlternativePathDiscussion) -- community discussion on path class design decisions
- [Alternative Path Module](AlternativePathModule) -- source code for the proposed alternative path module
- [Alternative Path Module Tests](AlternativePathModuleTests) -- test suite for the alternative path module

## Data and Text

- [Data Representation](DataRepresentation) -- working with data on the web and in Python
- [Structured Text](StructuredText/index) -- StructuredText markup language resources and discussion
- [Structured Text](StructuredText) -- creating rich documents without explicit markup
- [Structure Annotation](StructureAnnotation) -- annotating web page regions to map onto data structures
- [Language Parsing](LanguageParsing) -- evaluation of different parser libraries available for Python

## Concurrency

- [Concurrency](Concurrency/index) -- collected resources on concurrent programming in Python
- [Concurrency](Concurrency) -- overview of concurrency approaches and threading

## Performance Reference

- [Time Complexity](TimeComplexity) -- Big-O time and space complexity for Python built-in types
- [Time Complexity (Set Code)](TimeComplexity%20(SetCode)) -- analysis and implementation notes for set operation complexity

```{toctree}
:hidden:
:maxdepth: 1

Concurrency/index
StructuredText/index
AST
ASTBasedOptimization
AbstractBaseClasses
AdapterRegistry
AlternateLambdaSyntax
AlternativeDescriptionOfProperty
AlternativePathClass
AlternativePathDiscussion
AlternativePathModule
AlternativePathModuleTests
ByteplayDoc
ComputedAttributesUsingPropertyObjects
Concurrency
ConfigParser
ConfigParserExamples
ConfigParserGoals
ConfigParserShootout
DataRepresentation
Decorators
Generators
Iterator
LanguageParsing
ObserverPattern
StructureAnnotation
StructuredText
SwitchStatement
TimeComplexity (SetCode)
TimeComplexity
WithStatement
```
