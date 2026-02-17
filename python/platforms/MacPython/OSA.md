# MacPython/OSA

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Taken from Apple\'s developer website ([http://developer.apple.com/documentation/AppleScript/Conceptual/AppleScriptX/Concepts/osa.html](http://developer.apple.com/documentation/AppleScript/Conceptual/AppleScriptX/Concepts/osa.html))

Open Scripting Architecture

The Open Scripting Architecture (OSA) provides a standard and extensible mechanism for interapplication communication in Mac OS X. Communication takes place through the exchange of Apple events, a type of message designed to encapsulate commands and data of any complexity.

Apple events provide an event dispatching and data transport mechanism that can be used within a single application, between applications on the same computer, and between applications on different computers. The OSA defines data structures, a set of common terms, and a library of functions, so that applications can more easily create and send Apple events, as well as receive them and extract data from them.

Note: Apple events are not always the most efficient or appropriate mechanism for communicating between processes. Mac OS X offers other mechanisms, including distributed objects, notifications, sockets, ports, streams, shared memory, and Mach messaging. These mechanisms are described in "Interprocess Communication" in System-Level Technologies in Mac OS X Technology Overview. The OSA supports several powerful features in Mac OS X:

------------------------------------------------------------------------

[CategoryFaq](CategoryFaq)
