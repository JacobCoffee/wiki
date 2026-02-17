# Asking for Help/I tried to port python 2.7 to iOS and got "Fatal Python error: exceptions bootstrapping error.". How can I fix it?

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Asking for Help: Embedding Python core to iOS application 

I trying to make minimal part of Python to work as part (static library) of my iOS application for internal scripting. I used configure under Mac OS X(10.7) and it was successful. Then I got compilable and linkable XCode project very fast. The problem is, when I trying to use Python by Py\_[NoSiteFlag](./NoSiteFlag.html)=1; Py_Initialize(); it fails with error \"Fatal Python error: exceptions bootstrapping error.\" inside \_[PyExc](./PyExc.html)\_Init(). I tried to debug it, but unfortunately I cant understand why it fails. May be bacause I noob in Python source, but anyway, I need to port it. Tried 2.7.3, or latest 3.x, it was the same result as above. Any solution or hint will be very helpful.

Best Regards, Dmitry Stepanushkin

------------------------------------------------------------------------

[CategoryAskingForHelp](CategoryAskingForHelp)

P.S. I found solution by myself.
