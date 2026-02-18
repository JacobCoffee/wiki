# QuestionType

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

\-- [DavidLambert](DavidLambert) 2007-07-18 14:49:27

Nameless functions, nameless types.

Please, what is purpose of name argument to new type call?

    '''
    $ python
    Python 2.5.1 (r251:54863, Jun 25 2007, 14:55:49) 
    [GCC 3.4.4 (cygming special) (gdc 0.12, using dmd 0.125)] on cygwin
    '''

    cls1 = type('*',(object,),{})        # create type named by asterisk.
    # del *                              # silly.
    # del '*'                            # silly.


    cls2 = type('*',(object,),{'f':lambda s,x: x*3})
    # cls1().f('abc')                    # causes expected AttributeError
    cls2().f('abc') == 'abcabcabc'       # class name unused


    str(cls1) == "<class '__main__.*'>"
    str(cls2) == "<class '__main__.*'>"  # so what, the classes differ.


    cls_named = type('valid_name',(object,),{})
    # del valid_name                     # raises NameError


    class C(object):
        pass
    del C
