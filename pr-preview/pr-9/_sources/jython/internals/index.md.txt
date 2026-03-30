# Internals

Deep technical documentation about how Jython works under the hood. This section is for people who want to understand the compiler, the type system, method dispatch, performance characteristics, and the design decisions behind them. It also includes the Jython Enhancement Proposal (JEP) process and forward-looking design work for Jython 3.x.

## Enhancement Proposals

- [JepIndex](JepIndex) -- Index of all Jython Enhancement Proposals (JEPs)
- [JepGuidelines](JepGuidelines) -- How to write and submit a JEP
- [NewProposal](NewProposal) -- Template and process for creating a new proposal

## Compiler & Bytecode

- [JythonCompiler](JythonCompiler) -- How Jython compiles Python source to Java bytecodes
- [CodeSpeedupExperiments](CodeSpeedupExperiments/index) -- Experiments in speeding up generated code, including PyByteCode work
- [CodeSpeedupExperiments (notes)](CodeSpeedupExperiments) -- Additional notes on code speedup experiments

## Type System & Object Model

- [NewStyleClasses](NewStyleClasses) -- Implementation of new-style classes in Jython
- [ImplementNewType](ImplementNewType) -- How to implement a new Python type in Java
- [ImplementSequenceType](ImplementSequenceType) -- Implementing sequence protocol types
- [GeneratedDerivedClasses](GeneratedDerivedClasses) -- How Jython generates derived classes at runtime
- [PythonTypesInJava](PythonTypesInJava) -- Representing Python types on the Java side
- [ExposeAnnotations](ExposeAnnotations) -- Using annotations to expose Java methods to Python

## Method Dispatch & Conversions

- [MethodDispatch](MethodDispatch) -- How Jython resolves and dispatches method calls between Python and Java
- [IntegerConversion](IntegerConversion) -- Integer type conversion between Python and Java

## Collections & Buffers

- [CollectionsIntegration](CollectionsIntegration/index) -- Integrating Python collections with Java's Collections framework, including PySequence
- [CollectionsIntegration (notes)](CollectionsIntegration) -- Additional notes on collections integration
- [BufferProtocol](BufferProtocol) -- Implementation of the buffer protocol

## Standard Library Internals

- [DateTimeModule](DateTimeModule) -- Notes on the datetime module implementation
- [SysPackageManager](SysPackageManager) -- How Jython discovers and manages Java packages
- [PackageScanning](PackageScanning) -- The package scanning mechanism for finding Java classes
- [ThreadLocalVariables](ThreadLocalVariables) -- Thread-local variable handling in Jython

## Performance

- [PerformanceEnhancements](PerformanceEnhancements) -- Performance improvement efforts and techniques
- [PyFileBenchmarks](PyFileBenchmarks) -- Benchmarks for file I/O operations
- [ComparisonJavaJython](ComparisonJavaJython) -- Performance and feature comparisons between Java and Jython

## Future & Migration

- [Jython3000](Jython3000) -- Ideas and plans for backwards-incompatible changes in Jython 3.x
- [BiggerTasks](BiggerTasks) -- Larger work items tracked for Jython 2.3 and beyond
- [ReplaceJythonc](ReplaceJythonc) -- Plans to replace the legacy jythonc compiler


```{toctree}
:hidden:
:maxdepth: 1

CodeSpeedupExperiments/index
CollectionsIntegration/index
ShashankBharadwaj/index
BiggerTasks
BufferProtocol
CodeSpeedupExperiments
CollectionsIntegration
ComparisonJavaJython
DateTimeModule
ExposeAnnotations
GeneratedDerivedClasses
ImplementNewType
ImplementSequenceType
IntegerConversion
JepGuidelines
JepIndex
Jython3000
JythonCompiler
MethodDispatch
NewProposal
NewStyleClasses
PackageScanning
PerformanceEnhancements
PyFileBenchmarks
PythonTypesInJava
ReplaceJythonc
ShashankBharadwaj
SysPackageManager
ThreadLocalVariables
```
