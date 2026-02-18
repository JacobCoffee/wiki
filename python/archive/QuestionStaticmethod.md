# QuestionStaticmethod

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

\-- [DavidLambert](DavidLambert) 2007-07-18 15:08:31

    '''
        $ python
        Python 2.5.1 (r251:54863, Jun 25 2007, 14:55:49)
        [GCC 3.4.4 (cygming special) (gdc 0.12, using dmd 0.125)] on cygwin
        Type "help", "copyright", "credits" or "license" for more information.
        >>>
    '''


    x = 'abc'
    expect = 'abcabcabc'

    class C(object):
        def f(x):
            return x*3
        __call__ = staticmethod(f)

    assert expect == C()(x)                 # works great
                                            # straightforward from docs




    E = type('E',(object,),dict(__call__=staticmethod(C.__call__)))

    assert expect == E()(x)                 # works great, why must I
                                            # repeat staticmethod?





    def f(x):
        return x*3

    class G(object):
        __call__ = staticmethod(f)

    assert expect == G()(x)                 # works great, works as I expect







    # My opportunity to make a static method has passed?

    I = type('I',(C,),dict(__call__ = staticmethod(C.f)))

    try:
        assert expect == I()(x)
    except TypeError,info:                  # I don\'t understand.
        assert info.message.startswith('unbound method f()')




    # Staticness lost?

    F = type('F',(object,),dict(__call__=C.__call__))

    try:
        assert expect == F()(x)
    except TypeError,info:                  # misunderstood,
        assert info.message.startswith('f() takes exactly 1 argument (2 given)')
