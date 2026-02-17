# MacPython/AppleScriptNotes

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# filesystem bookmarks 

- [file:///Library/ScriptingAdditions/](file:///Library/ScriptingAdditions/) (probably)

- [file:///System/Library/ScriptingAdditions/](file:///System/Library/ScriptingAdditions/) (.app and .osax bundles)

- [file:///System/Library/Components/AppleScript.component](file:///System/Library/Components/AppleScript.component) (the core stuff in here)

- [file:///System/Library/Frameworks/Python.framework/Versions/2.3/lib/python2.3/plat-mac/Carbon/AppleEvents.py](file:///System/Library/Frameworks/Python.framework/Versions/2.3/lib/python2.3/plat-mac/Carbon/AppleEvents.py) (constants)

# bookmarks

- [http://developer.apple.com/technotes/tn/tn1164.html](http://developer.apple.com/technotes/tn/tn1164.html)

- [http://developer.apple.com/documentation/mac/IAC/IAC-2.html](http://developer.apple.com/documentation/mac/IAC/IAC-2.html)

- [http://developer.apple.com/documentation/AppleScript/Conceptual/AppleScriptLangGuide/index.html](http://developer.apple.com/documentation/AppleScript/Conceptual/AppleScriptLangGuide/index.html)

- [http://maccentral.macworld.com/features/applescriptprimer16/](http://maccentral.macworld.com/features/applescriptprimer16/)

- [http://www.mactech.com/articles/develop/issue_10/Clark_final.html](http://www.mactech.com/articles/develop/issue_10/Clark_final.html)

- [http://www.mactech.com/articles/mactech/Vol.10/10.01/ExtendApplescript/](http://www.mactech.com/articles/mactech/Vol.10/10.01/ExtendApplescript/)

- [http://www.mactech.com/articles/mactech/Vol.11/11.07/aeteResources/](http://www.mactech.com/articles/mactech/Vol.11/11.07/aeteResources/)

- [http://www.mactech.com/articles/develop/issue_12/Berdahl_final.html](http://www.mactech.com/articles/develop/issue_12/Berdahl_final.html)

- [http://www.mactech.com/articles/develop/issue_21/21simone.html](http://www.mactech.com/articles/develop/issue_21/21simone.html)

- [http://www.mactech.com/articles/develop/issue_23/according.html](http://www.mactech.com/articles/develop/issue_23/according.html)

- [http://soundfarmer.com/moin.cgi/AppleEventsPython](http://soundfarmer.com/moin.cgi/AppleEventsPython)

- [http://www.prefab.com/scriptweb/archive/developerarticles.html](http://www.prefab.com/scriptweb/archive/developerarticles.html)

- [http://www.scripting.com/samples/](http://www.scripting.com/samples/)

- [http://search.cpan.org/\~cnandor/Mac-Glue/Glue.pm](http://search.cpan.org/~cnandor/Mac-Glue/Glue.pm)

- [http://citeseer.nj.nec.com/555351.html](http://citeseer.nj.nec.com/555351.html)

# snippets from mactech aeteResources 

## suites

It's important to remember that organization of events by suites doesn't draw any boundary lines in functionality; the Apple Event Manager doesn't even know about suites. Aside from being a convenience in organizing related events and classes, their only functional significance is that you can import whole suites by name from the 'aeut' resource.

You may also want to create a singe suite which puts together pieces of standard suites without completely implementing any of them. In this case, you should give the suite an ID of \'\*\*\*\*\'. If you implement a significant part of a suite, though, you should include it as a separate suite.

The suite ID 'tpnm', conventionally called "Type Names," is magical. If you give a suite this ID, it won't appear in the Script Editor's dictionary listing. This is useful for defining classes you want to hide from the user.

If a suite is described in the system's 'aeut' resource and you support it completely, all that you have to do is include this basic information about it; you don't have to list the events and classes which it supports. However, if you support only some of the events and classes in a suite, or if you support extensions to any of them (extra parameters, elements, or properties), then you must itemize them in the suite. If you include any events or classes in a suite, you're saying that you support only those events and classes.

## events

Parameters do not have to be named, since they can be identified by their position in the event as long as no parameters are left out before them. However, if there is more than one optional parameter, all optional parameters should be named. Also, optional parameters should come after all required parameters, to minimize the chances of confusing [/AppleScript](./MacPython(2f)AppleScriptNotes(2f)AppleScript.html) or the Apple Event Manager with omitted positional parameters.

## classes

A class contains zero or more properties, followed by zero or more elements. The difference between properties and elements has been much discussed in the Apple Event literature, but is worth mentioning here one more time: An element is an item of information which is contained in an object, while a property is something which gives information about an object. Elements can include windows, text, and pictures; properties can include color, font, and size. Some borderline cases are hard to decide; what is most conveniently treated as a property in the usual case may be treated as an object and thus have element-like characteristics. If there can be more than one of something in an object (e.g., the characters in a text object, or pixels in a graphic), it should almost certainly be an element.

## properties

The class of a property indicates what type of object the property is, but just what this means is ill-defined. Sometimes it will be one of the object classes defined in AERegistry.h, sometimes it will be a descType (like typeInteger), and sometimes it will be unique to the application. What the class actually means is known only to the application itself. If it is a class name, it indicates what kind of object (using the Apple Event object model) is referred to by the property, without saying anything about the object's physical representation. For example, cGraphicLine ('glin') indicates a graphic line, and cPixel 'cpxl' indicates a pixel. How they might be stored is up to the application.

When an object is actually passed around by Apple Events, it becomes a parameter or reply of an event, and then its storage format is specified by the type of the event. When a parameter of an Apple Event is of type typeObjectSpecifier ('obj '), then the object specifier contains information about the class of the object; this is the link between parameters, whose structure is known to the Apple Event Manager, and objects, whose structure is known only to the application.

As links go, this is a very tenuous one. In particular, there's no way to specify what kind of object a parameter of type 'obj ' refers to. You can't make an 'aete' resource say that a point or a line is acceptable, but a document or a window isn't. This is a fact we have to live with, and should make up for in the documentation.

Some properties are magical. There is a special property ID, called kAESpecialClassProperties and represented as 'c@#!', which tells you that the property really isn't a property at all, but a place to store flags which describe the class itself. (The ID undoubtedly immortalizes the language some programmer used on discovering that the lack of class flags made this kludge necessary.)

A property with this class is the way that you create a plural synonym for a class (which is something you should do for all classes that may be used in scripts). Having created the singular class, you create another class which has the same ID, a plural version of the name (e.g., "windows" instead of "window"), no elements, and only one property. This property has ID 'c@#!' and class 'type', and the property has its Plural flag set.

Another magic ID can be useful for eliminating redundant information. If the first property of a class has the ID 'c@#\^', this signifies that the class inherits properties from another class. In this case its class is the ID of its base class, and the name of the property must be "\<Inherited\>", including the angle brackets. Using this trick can make some 'aete' resources significantly smaller, if there are a number of bulky classes which are largely similar.

A property can also belong to more than one class. To do this, you must set the Enumerated flag, and set the class to the ID of an enumeration. The enumerated set specifies the classes to which the property can belong. Alternatively, you can use the Wild Card class ('\*\*\*\*'), which says that a property can be of any class.

If a property can be modified by an event, then the Read/Write flag should be set. If its value is a list (e.g., the styles which are applied to a text item), then the List of Values flag should be set. The Masculine and Feminine flags, once again, don't apply to English.

# text chunks 

useful builtin suites:
