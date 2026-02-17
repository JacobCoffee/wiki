# ArithmoGraph

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

An [arithmograph](http://de.wikipedia.org/wiki/Arithmograph) is a kind of a numeric crossword puzzle, where instead of filling the rows and columns with words, digits must be found that give numbers that fit the equations. In this example a following arithmograph has been used:

    ABC - BBD = DEF
     /     +     -
     GH *  GD = BGC
     =     =     =
     DI + BJI = BIF

Each letter corresponds to a digit, always the same one, and different digits for different letters

To check all possibilities, 10! = 3628800 permutations would have to be checked. A brief analysis of the equation system allows us to reduce this number significantly.

First, we can see from III-down that C = 0. From II-down, I is even, non-zero. from I-down and II-down, H = 5. Further, we can see that some digits are no greater than a certain number, like from II-across we can see that (10\*G)^2^ \< 1000, hence G^2^ \< 10, hence G \<= 3, and since we already know that 0 is taken by C, G is in (1, 2, 3), etc.

All resulting constraints are specified in the CONSTRAINTS array. As a result, we now have less than 294912 permutations to check.

    from operator import add, sub, mul

    def DigitPoly(letterdigits):
        """Creates polynomial from digit IDs specified as abc..."""
        # 'abc' = 10*(10*a + b) + c
        orda = ord('a')
        digids = [ord(x.lower()) - orda for x in letterdigits]
        def tmp(values):
            val = 0
            for x in digids:
                val = 10*val + values[x]
            return val
        return tmp

    def Equation(eqndata):
        """Creates equation test function from eqndata."""
        exp1 = DigitPoly(eqndata[0])
        exp2 = DigitPoly(eqndata[2])
        exp3 = DigitPoly(eqndata[3])
        def tmp(digits):
            return eqndata[1](exp1(digits), exp2(digits)) == exp3(digits)
        return tmp

    def check_permutations(constraints, equations, digits):
        """Recursively checks all permutations in constraints on equations."""
        if constraints:
            for x in constraints[0]:
                if x in digits:
                    continue
                check_permutations(constraints[1:], equations, digits+[x])
        else:
            for x in equations:
                if not x(digits):
                    return
            print "Successful set of digits:", digits

    NZ_EVEN = (2, 4, 6, 8)
    CONSTRAINTS = ((1, 2, 3, 4, 6, 7, 8, 9),
                   (1, 2, 3, 4),
                   (0,),
                   NZ_EVEN,
                   (1, 2, 3, 4, 6, 7, 8, 9),
                   NZ_EVEN,
                   (1, 2, 3),
                   (5,),
                   NZ_EVEN,
                   (1, 2, 3, 4, 6, 7))

    EQUATIONS = (('abc', sub, 'bbd', 'def'),
                 ('gh', mul, 'gd', 'bgc'),
                 ('di', add, 'ji', 'if'),
                 ('di', mul, 'gh', 'abc'),
                 ('bd', add, 'gd', 'ji'),
                 ('de', sub, 'bg', 'bi'))

    if __name__ == "__main__":
        eqns = [Equation(x) for x in EQUATIONS]
        check_permutations(CONSTRAINTS, eqns, [])
