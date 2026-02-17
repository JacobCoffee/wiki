# PEP3107FunctionAnnotationsRehash

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Missing exceptions in PEP 3107 

Thread: [http://groups.google.com/group/comp.lang.python/browse_thread/thread/ba7e0dd75d2b57d1](http://groups.google.com/group/comp.lang.python/browse_thread/thread/ba7e0dd75d2b57d1)

    Having the list of possible exceptions as annotation alone would be 
    already helpful. Of course it could be also discussed whether Python 
    should check that the function really raises only these exceptions (as 
    in C++), or we could even have checked exceptions (as in Java, but this 
    seems to be a controversial issue). 

    Has this already been discussed, or is it in a different PEP? 
    _Cristoph Zwerschke_

    ...a package or application that uses 
    annotation could simply use the data-structure associated with 
    "return" to also contain exception information. That might not seem 
    intuitive, but keep in mind that the value associated with "return" in 
    the associations dictionary is going to be a special case anyway. 

    _Matimus_

    If you really want this then you can use a decorator to insert a 'raise' 
    key into the annotations: 
    @raises("exc info") 
    def foo(a: "a info", b: "b info") -> "ret info": 
            return "hello world" 

    ...

    Consider the syntax set in concrete. The meaning of the annotations on the 
    other hand is completely up for grabs.

    _Duncan Booth_
