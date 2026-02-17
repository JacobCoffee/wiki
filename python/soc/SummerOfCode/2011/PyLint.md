# SummerOfCode/2011/PyLint

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# PyLint Ideas for GSoC 2011 

The best way to get started is to join our XMPP room at [public@conference.jabber.logilab.org](mailto:public@conference.jabber.logilab.org) and/or mailing list at [python-projects@lists.logilab.org](mailto:python-projects@lists.logilab.org).

Remember that applicants are required to commit code to be eligible for acceptance, though this may be after their application is submitted. The contributed code need not be in the same area as their proposal would have them working in.

## improve understanding of code 

This project would consist in enhancing pylint underlying library (astng) to understand things it doesn\'t yet, such as metaclasses, [new], 2.6 properties, etc\...

Expected skills: good knowledge of python language, including meta-object protocol, ability to grasp hairy code

## make inference customisable 

The aim of this project would be to define and implement a way to provide static descriptions of some classes, and also to allow control of inference for dynamic classes (such as found in web frameworks for instance), making pylint (more) usable in case where it\'s not yet. That would implies working on underlying astng library as well.

Expected skills: good knowledge of python language, ability to grasp hairy code

## benefit from python3 annotations 

Python3 brings type annotation to the language. This project would be to enhance pylint current type inference by using this information,

Expected skills: good knowledge of python language, ability to grasp hairy code

## pylint as an interactive tool to help learning python 

This project consist in thinking and implementing a new way to use pylint for new-comers, where it would help them in learning the langage (and sometime general programmation).

Expected skills: knowledge of python language, ability to sketch a new-comer application
