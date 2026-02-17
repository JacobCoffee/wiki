# PythonVsNice

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Nice 

Nice is basically a minor improvement on Java. It offers features like multimethods, but its syntax is essentially that of Java and it compiles to run on a JVM. Therefore, this comparison will actually compare Jython with Nice. More about Nice can be found at [http://nice.sourceforge.net/](http://nice.sourceforge.net/).

Note that the original document for this was written for Nice\'s wiki ([http://nice.sourceforge.net/cgi-bin/twiki/view/Doc/NiceVersusJython](http://nice.sourceforge.net/cgi-bin/twiki/view/Doc/NiceVersusJython)), but the comparison is valid in either direction.

------------------------------------------------------------------------

In order of the Nice manual:

## Philosophy: 

- Nice\'s philosophy is Safety / Modularity / Expressivity.
- Jython has far LESS emphasis on Safety \-- it is more inclined toward letting the programmer do as she pleases if she intentionally steps into \"black magic\" land.
- Jython\'s approach to Modularity is similar to Nice\'s.
- Jython has at LEAST as much emphasis on expressivity as Nice, perhaps more.

## Packages 

- Jython\'s \"modules\" are pretty much equivalent to Nice\'s \"packages\". Both can contain classes AND functions/methods AND miscellaneous variables/constants. Unlike Nice, Jython allows importing an entire module OR a single class/function/whatever from a module.

## Classes 

### Fields 

- Nice\'s classes have a fixed set of fields, while methods are actually separate (but via multi-dispatch, can be associated with a class).
- Jython\'s classes are more like a bare namespace \-- the fields can be initialized, but additional fields can be added (or removed) at runtime. Methods ARE actually associated with a class, in fact, they are simply fields, whose type is \"function\"\[\*\].

\[\*\] Not strictly true, but close enough. See \"bound methods\" below.

### Constructors 

- Jython, like Nice, has a single constructor for each class (Jython allows but does not require the use of keyword arguments).
- Unlike Nice, Jython requires the programmer to write out the constructor.
- Like Nice, Jython encourages the use of factory functions if multiple construction mechanisms are required.

### Parametric Classes 

- Jython does not have this feature, nor is it needed. The reason is a very fundamental difference between Nice and Jython: dynamic typing. Jython (like Nice) is \"strongly typed\" \-- objects have a type with specific capabilities, so you can\'t take a String an use it like a pointer or a number (C, for example, is \"weakly typed\" and DOES allow this). However, Jython is \"dynamically typed\" (unlike Nice, which is \"statically typed\"). This means that individual variables or items in a container do NOT have well-specified types. In Nice, a variable x is declared to be int, or String, or ?MyOwnClass, and may only contain those values; Python does not have a similar restriction. Some people prefer static languages (more errors caught at compiletime instead of runtime), others prefer dynamic (no need to declare variable types, sometimes more flexibility).

### Functions and Methods 

- Functions and methods are first-class objects in BOTH Jython and Nice.

- Jython does NOT support multi-dispatch, only single-dispatch.

- Nice distinguishes between \"functions\" and \"methods\" (the latter can be specialized for multi-dispatch). *Not anymore: everything is a method in Nice, a \"function\" is now simply a method with a default implementation. This might allow to reorganize these sections, but I leave that to somebody more fluent in Python.*

- \"Functions\" and \"methods\" are the same in Jython, except that there exists something called a \"bound method\". If \"fido\" is an instance of the class \"Dog\" with the method \"bark(timesToBark)\", then Dog.bark is an ordinary function taking two arguments, a Dog and an integer, while fido.bark is a \"bound method\" taking ONE argument (an integer), and performing a call to Dog.bark with the first parameter automatically set to fido. In Nice, you would need to write \"fido.bark\" as the closure \"int timesToBark =\> fido.bark(timesToBark)\".

## Functions 

- Both Jython and Nice allow parameters to be named, and allow callers to specify inputs by keyword OR by parameter order.
- Both Jython and Nice allow optional parameters. Nice allows the value of optional parameters to depend on the values of other parameters; Jython does not allow this, but a common idiom has a default of \"None\" and then checks for \"None\" at the top of the function and sets the value accordingly.
- Jython allows the function to operate on its arguments as a tuple, or a dict (for named parameters), thus making possible things like functions that take a variable number of parameters. Nice does not allow this, although one can always use a single argument of type Tuple instead.

## Methods 

- Jython functions/methods do not need to be declared. This is in keeping with the dynamic typing of Jython.
- Jython does not support type parameters in methods, since it doesn\'t support type parameters at all. Again, it is not required / not available because of Jython\'s dynamic typing.
- Again, Jython does not support multi-dispatch \-- methods are dispatched only on their first argument.
- Nice supports \"value dispatch\" (like multi-dispatch, but declaring special code to be executed for particular values). Jython does not support this at all. Most of the things that Value Dispatch would be used for would be accomplished in Jython using a dict (built-in mapping (hashtable) type), but some of the more advanced things possible with value dispatch would simply be a pain to implement in Jython.
- Both Jython and Nice allow optional parameters just as with functions (more details above).

## Assertions and Contracts 

- Both Nice and Jython support assertions.
- Nice supports preconditions and postconditions. Jython does not (although assertions can be used and/or there are some libraries to support them).

## Statements 

- Both Nice and Jython allow local and package-level variables.

- Nice allows local and package-level constants. Jython has no way of enforcing constantness, relying solely on the convention that a name in ALL_CAPS is never intended to be changed.

- Both Jython and Nice allow looping through the items in a container with a simple for statement. Although this seems trivial, it is in fact a very important simplification of nearly all programs, improving readability and reducing errors. Both allow looping over the characters of a string, and the items in a list; Jython also allows looping over dicts.

- Nice allows the declaration of local functions with access to their enclosing scope. Jython allows this also, but it permits the local functions to be named. (*Nice also requires local functions to be named. Anonymous functions are also allowed, but these are expressions. An anonymous local function declaration statement does not seem to make sense: how would you refer to it?*) In either case, the result is a first-class object which captures its local environment.

## Expressions 

- Both Nice and Jython allow either the f(x,y,z) or the x.f(y,z) form for method calls.
- Both Nice and Jython allow easily-constructed tuple types, which can be used to pass around grouped values or return multiple values from a function. This is more powerful than it sounds.
- Nice allows the easy creation of small anonymous functions. Jython has anonymous functions (using the regrettably named \"lambda\"), but they are limited to a single expression statement. Anything more, and the function needs to be named (there are no restrictions on the power of named functions).
- Nice uses Java\'s primitive types, but provides \"autoboxing\", so they are converted to object types automatically if used as an object. Jython does not have autoboxing \-- primitive types are ALWAYS treated as objects. Conversion to/from primitive types will occur only when interfacing with java code. So pure computational tasks will be notably slower in Jython.

## Interfacing with Java 

- One of the most powerful features of Nice is that it is VERY easy to interface quite closely with java. Java methods can be called from Nice, and Nice methods from java (although they cannot yet be overriden in Java). Nice classes can subclass java classes or implement java interfaces and java classes can subclass Nice classes, all without writing special interface code.
- Jython has the same incredibly good level of integration with java. Java methods can be called from Jython, or Jython functions or methods from java. Jython classes can subclass java classes and java classes can subclass Jython classes, all without writing special interface code.
- Let me just repeat again, that for BOTH languages, the level of integration with java is extraordinary.

## Types 

- Nice provides \"option types\", distinguishing between variables allowed to be null, and those not allowed to be null. Jython has no such distinction \-- because it is dynamically typed, ANY Jython variable (or instance variable or container slot) can take on ANY value, including \"None\" (which is an ordinary object used in Jython as the \"not set\" value).
- Again, Nice has type parameters, but no such feature exists in Jython.
- Nice offers abstract interfaces \-- like an interface, but the declaration that the class implements it need not reside with the class itself. Jython, does not provide such a feature, but because it is dynamically typed it offers many (but not all) of the same benefits. In Nice, abstract interfaces allow one to declare that some function will operate on any of several unrelated types, and provides multimethods for performing the desired operations on the different types. In Jython, any function will operate on any type passed to it, so long as the type has methods with the right names and signatures. However, creating new methods (eg: adding toLogString() to String objects) would require some sort of wrapper object in Jython.

## Things Specific To Jython 

The above is organized according to the Nice manual, but there are a few points that still need to be touched on because they are more specific to Jython than to Nice.

- **Whitespace:** Jython uses indentation level to indicate subsidiary statements instead of using \"{\" \"}\" pairs. This is the feature most frequently and most vehamently denounced by people who have never used the language (and is usually mis-named \"significant whitespace\"). But almost NO ONE who has used the language for at least a week complains about this, nearly all find it BETTER (after all, you\'re going to indent anyway\... why not have the programmer and the compiler looking for the same indicators). Try it out\... you\'ll like it.

- **Data Types:** Jython has some more powerful data types built in. In addition to tuples (which Nice also has) it has Lists (automatically re-sizing, like ArrayList, not like arrays), and Dicts (like Map). Furthermore, there is basic language syntax supporting these elementry types (\"myDict\[\'abc\'\]\" to access an item in myDict, or \"myList\[3:6\] = \[\]\" to delete items 3 up through 6 from myList. These data types make the language tremendously more expressive.

- **Booleans:** Nice uses java\'s (primitive) boolean type. Jython provides all objects with a truth value (0, \"\", and empty collection types are false, most other things are true). Normally, Jython will use 1 and 0 for true and false (can also be spelled \"True\" and \"False\". This offers less type safety (might accidentally test truth value of something you didn\'t intend to), but often is more expressive (eg: \"if myList:\" instead of \"if (myList.size() \> 0) {\").

- **Operator Overloading:** Jython allows user-defined classes to declare special methods to overload operators and special language syntax (like subscripting). Nice provides a similar ability to overload the \"\[\]\" syntax (collection subscripting) and all existing operators. Does Jython allow the definition of arbitrary operators (e.g. \"+==+\") ?

- **Changing objects dynamically:** In Nice (or java) an object, once created, has a particular set of fields and methods\... no more, no fewer. In Jython, new fields or new methods can be added AT RUNTIME, even to INDIVIDUAL OBJECTS. Imagine, your function was passed some random objects, and you simply add a \"sortOrder\" field to each one. Or you take an individual object and replace some of its methods (kind of like value dispatch, but performed at runtime).

- **Creating classes dynamically:** In Jython, functions or methods can also create new classes dynamically, even at runtime. The feature is rarely used, but can be quite powerful for advanced users. Nice has no equivalent feature.

- **Interpreter:** Jython is called a \"scripting language\" for two reasons \-- it is easy to write very simple programs in it (no classes required if not desired\... no functions required either if just one \"function\" is to be performed). And secondly, because it is interpreted. You can fire up a Jython interpreter and just type code at it\... create a new class, create an instance, run some code, then stop and examine the objects returned. This is a very useful way of \"playing around\" with Jython code (it takes less time to just TRY IT than to look up syntax in the manual!). It is also an invaluable debugging tool \-- I often use Jython to debug my pure java programs because it provides a way to interactively investigate a live program.

------------------------------------------------------------------------

Contributors: [MichaelChermside](MichaelChermside), [DanielBonniot](DanielBonniot) See also [LanguageComparisons](LanguageComparisons).
