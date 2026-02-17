# PyCon2006/Tutorials/GettingStartedWithTwisted

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Getting started with the Twisted Framework 

This 3-hour tutorial session will introduce the fundamentals of Twisted. It answers the question: \"Where do I start?\" And while some complaints have been made regarding a lack of documentation, there\'s plenty of it out there if you know how to read and understand it.

### Target audience 

Programmers experienced with Python but no real experience with Twisted.

### Focus 

This tutorial explains how to use Twisted in a controlled environment, where the programmer has the ability to define what\'s running on both sides of a network connection. (This means that I will \_not\_ be talking about Twisted in the context of the web, or the use of a browser as the user interface.)

#### Outline 

A. Fundamental Concepts

1.  The asynchronous programming model
2.  Finite State machines

A. Twisted Features

1.  Reactors
2.  Cred
3.  Deferreds
4.  Perspective Broker
    a.  Realms
    b.  Avatars
    c.  Perspectives

### Case Study 

Using Twisted to build a Chat Server.

This sample application is capable of highlighting all the topics listed above. A full exploration of a chat server will include issues like authentication and authorization, and can include discussions about topics like moving more arbitrary data between clients such as executables or graphical images. Some other subjects, such as using a GUI toolkit on the client, will be touched on just enough to provide necessary functionality.

**Note:** Students are encouraged to bring a laptop - preferably preloaded with Python, Twisted, and wxPython.
