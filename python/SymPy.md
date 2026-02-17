# SymPy

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

SymPy is a symbolic manipulation package, written in pure Python. Its aim is to become a full featured CAS in Python, while keeping the code as simple as possible in order to be comprehensible and easily extensible.

![](http://sympy.org/media/logo.png "http://sympy.org/media/logo.png")

Homepage: [http://sympy.org/](http://sympy.org/)

Source Code: [http://github.com/sympy/sympy](http://github.com/sympy/sympy)

Mailing list: [https://groups.google.com/forum/?fromgroups#!forum/sympy](https://groups.google.com/forum/?fromgroups#!forum/sympy)

## Examples 

    >>> from sympy import *
    >>> x, y, z, t = symbols('x y z t')
    >>> k, m, n = symbols('k m n', integer=True)

    >>> integrate(exp(x)*x**2, x)
    ⎛ 2          ⎞  x
    ⎝x  - 2⋅x + 2⎠⋅ℯ

    >>> expand((x + y)**3)
     3      2          2    3
    x  + 3⋅x ⋅y + 3⋅x⋅y  + y
    >>> factor(_)
           3
    (x + y)

    >>> Sum((-1)**n*x**n/factorial(n), (n, 0, oo))
      ∞
     ____
     ╲
      ╲       n  n
       ╲  (-1) ⋅x
       ╱  ────────
      ╱      n!
     ╱
     ‾‾‾‾
    n = 0
    >>> _.doit()
     -x
    ℯ
