# ProblemSets/99 Prolog Problems Solutions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Python Solutions to [99 Prolog Problems](https://prof.ti.bfh.ch/hew1/informatik3/prolog/p-99/).

**Index**

# Problems 1-6 

André Roberge has a zip file with solutions to the first six problems, in Crunchy format: [First six](http://crunchy.googlecode.com/files/first_6_of_99_problems.zip)

# Problem 7: Flatten a nested list structure 

Based on the standard library documentation:

        from itertools import chain
        def flatten(listOfLists):
            return list(chain(*listOfLists))

The suggested solution does not work for a list like the following:

        a_list = [0, 1, [2, 3], 4, 5, [6, 7]]

as the argument name tries to imply, it only works for a list of lists, not a generic list of variously and mixedly nested lists and items. Here\'s a more general solution using the simple recursive approach:

        def flatten(nestedList):
            def aux(listOrItem):
                if isinstance(listOrItem, list):
                    for elem in listOrItem:
                        for item in aux(elem):
                            yield item
                else:
                    yield listOrItem
            return list(aux(nestedList))

This problem is also a good example of \"recursion elimination\": explicitly maintain a LIFO stack of what sublists are being expanded so as to avoid actual recursion. The rec-elim approach is usually faster and avoids issues with recursion depth limits. Here\'s a version that works when it\'s OK to dismantle the input argument \-- for variety, I have it build the result into another list by calls to .append, instead of using yield in an auxiliary generator and calling list() on it.

        def flatten(nestedList):
            result = []
            stack = [nestedList]
            while stack:
                if isinstance(stack[-1], list):
                    try: stack.append(stack[-1].pop(0))
                    except IndexError: stack.pop() # remove now-empty sublist
                else:
                    result.append(stack.pop())
            return result

If you\'re not allowed to dismantle the input argument, you can take a preliminary copy.deepcopy of it as the initial item in the stack, or you can \"pay as you go\" by doing shallow copies \"at the last minute\" when needed. Here\'s an example of the latter approach, with other little variants. Here, stack is always a list of non-empty sublists which are shallow copies of sublists from the initial argument (and so the sublists on the stack can always be dismantled with no problems) while leaves (non-list subitems) are always immediately appended to the result (this, btw, builds up the result in a reversed way, so a call to result.reverse becomes necessary).

        def flatten(nestedList):
            result = []
            if not nestedList: return result
            stack = [list(nestedList)]
            while stack:
                current = stack.pop()
                next = current.pop()
                if current: stack.append(current)
                if isinstance(next, list):
                    if next: stack.append(list(next))
                else: result.append(next)
            result.reverse()
            return result

# Problem 8: Eliminate consecutive duplicates of list elements 

        from itertools import groupby
        def compress(alist):
            return [key for key, group in groupby(alist)]

# Problem 9: Pack consecutive duplicates of list elements into sublists 

        from itertools import groupby
        def pack(alist):
            return [list(group) for key, group in groupby(alist)]

# Problem 10: Run-length encoding of a list 

        from itertools import groupby
        def encode(alist):
            return [[len(list(group)), key] for key, group in groupby(alist)]

# Problem 11: Modified run-length encoding 

        def encode_modified(alist):
            def aux(lg):
                if len(lg)>1: return [len(lg), lg[0]]
                else: return lg[0]
            return [aux(list(group)) for key, group in groupby(alist)]

# Problem 12: Decode a run-length encoded list 

        def decode(alist):
            def aux(g):
                if isinstance(g, list): return [(g[1], range(g[0]))]
                else: return [(g, [0])]
            return [x for g in alist for x, R in aux(g) for i in R]

# Problem 13: Run-length encoding of a list (direct solution) 

        def encode_direct(alist):
            def aux(k, g):
                l = len(list(g))
                if l>1: return [l, k]
                else: return k
            return [aux(key, group) for key, group in groupby(alist)]

# Problem 14: Duplicate the elements of a list 

        def dupli(L):
          return [x for x in L for i in (1,2)]

# Problem 15: Duplicate the elements of a list a given number of times 

        def dupli(L, N):
          return [x for x in L for i in range(N)]

# Problem 16: Drop every N\'th element from a list 

        def drop(L, N):
          return [x for i,x in enumerate(L) if (i+1) % N]

# Problem 17: Split a list into two parts; the length of the first part is given 

        def split(L, N):
            return L[:N], L[N:]

# Problem 18: Extract a slice from a list 

Given two indices, I and K, the slice is the list containing the elements between the I\'th and K\'th element of the original list (both limits included). Start counting the elements with 1.

        def slice(L, I, K):
            return L[I-1:K]

# Problem 19: Rotate a list N places to the left 

        def rotate(L, N):
            return L[N:] + L[:N]

# Problem 20: Remove the K\'th element from a list 

        def remove_at(L, N):
            return L[N-1], L[:N-1] + L[N:]

# Problem 21: Insert an element at a given position into a list 

        def insert_at(x, L, N):
            return L[:N-1]+[x]+L[N-1:]

# Problem 22: Create a list containing all integers within a given range 

        def irange(I, J):
            return range(I, J+1)

# Problem 23: Extract a given number of randomly selected elements from a list 

        import random
        def rnd_select(L, N):
            return random.sample(L, N)

# Problem 24: Lotto: Draw N different random numbers from the set 1 

        import random
        def rnd_select(N, M):
            return random.sample(range(1, M+1), N)

# Problem 25: Generate a random permutation of the elements of a list 

        import random
        def rnd_permu(L):
            return random.sample(L, len(L))

or

        import random
        def rnd_permu(L):
            result = list(L)
            random.shuffle(result)
            return result

# Problem 26: Generate the combinations of K distinct objects chosen from the N elements of a list 

        def combination(K, L):
            if K<=0:
                yield []
                return
            for i in range(len(L)):
                thisone = L[i:i+1]
                for another in combination(K-1, L[i+1:]):
                    yield thisone + another

in Python 2.6+:

        import itertools
        def combination(K, L):
            return itertools.combinations(L, K)

# Problem 27: Group the elements of a set into disjoint subsets 

A natural recursive approach requires \"temporarily modifying\" certain things (the main list, the list of sublists, the list of counts of remaining lengths desired in the sublists); one way to express this is by the \`with\' statement and the \"resource allocation is initialization\" (RAII) idiom it enables\...:

        from __future__ import with_statement
        import contextlib
        import itertools

        def group(alist, glens):
            # entries in glens are ints >0 summing to len(alist)
            assert all(g>0 for g in glens)
            assert sum(glens) == len(alist)
            # return the generator made by an auxliary function
            return _g(alist, glens, [ [] for g in glens ])

        #
        # helpers: with-statement contexts for RAII idioms
        #
        @contextlib.contextmanager
        def popping(L):
            item = L.pop()
            yield item
            L.append(item)

        @contextlib.contextmanager
        def appending(L, item):
            L.append(item)
            yield L
            L.pop()

        @contextlib.contextmanager
        def decrementing(L, index):
            L[index] -= 1
            yield L
            L[index] += 1

        #
        # helper: auxiliary recursive generator function
        #
        def _g(L, rls, grps):
            if sum(rls) == 0:
                yield [list(grp) for grp in grps]
                return
            with popping(L) as item:
                for i, (rl, grp) in enumerate(itertools.izip(rls, grps)):
                    if rl > 0:
                        with appending(grp, item):
                            with decrementing(rls, i):
                                for filled in _g(L, rls, grps):
                                    yield filled

However, the Zen of Python says that \"flat is better than nested\", and, of course, we *can* express \_g in a much flatter way by giving up the nesting, e.g. as follows:

        #
        # helper: auxiliary recursive generator function
        #
        def _g(L, rls, grps):
            if sum(rls) == 0:
                yield [list(grp) for grp in grps]
                return
            item = L.pop()
            for i, (rl, grp) in enumerate(itertools.izip(rls, grps)):
                if rl == 0: continue
                grp.append(item)
                rls[i] -= 1
                for filled in _g(L, rls, grps):
                    yield filled
                rls[i] += 1
                grp.pop()
            L.append(item)

Which is more readable? \"Ai posteri l\'ardua sentenza\...\"!-)

A more compact, if much less readable, solution (through the use of recursion and an unfortunate number of lambda functions - in the spirit of functional programming):

        # A list comprehension helps paste the results from combos (below) and the recursion together nicely
        def group(x, n):
            if n[0] == len(x): return [[x]]
            return [[y[0]] + z for y in combos(n[0], x) for z in group(y[1], n[1:])]

        # Enumerates all combinations, where each combination is paired with the remainder of the list
        # This is used to simplify the recursive step in the main function (as opposed to using itertools' combinations function)
        def combos (n, x, cur = 0):
            if n == 0: return [[[],x]]
            return [[[x[i]]+y[0], y[1]] for i in range(cur, len(x)) for y in combos(n-1, x[:i]+x[i+1:], i)]

This solution was tested on IDLE 3.1, apologies to anyone for whom it doesn\'t work.

# Problem 28: Sorting a list of lists according to length of sublists 

    # Part A
        def lsort(L):
            return sorted(L, key=len)

    # Part B
        from collections import defaultdict

        def lfsort(L):
            lencounts = defaultdict(int)
            for sublist in L: lencounts[len(sublist)] += 1
            def bylenfreq(sublist): return lencounts[len(sublist)]
            return sorted(L, key=bylenfreq)

# Problem 29: there is no problem 29 in the original problem set 

# Problem 30: there is no problem 30 in the original problem set 

# Problem 31: Determine whether a given integer number is prime 

Simplest approach: generate all primes, stop when the number N under test equals a prime, or is divisible by it without being equal, or when no higher prime is of interest because we\'ve checked all primes \<= sqrt(N).

        import itertools

        def erat2():
            # from Python Cookbook, 2nd Edition, recipe 18.10
            D = {}
            yield 2
            for q in itertools.islice(itertools.count(3), 0, None, 2):
                p = D.pop(q, None)
                if p is None:
                    D[q*q] = q
                    yield q
                else:
                    x = p + q
                    while x in D or not (x&1):
                        x += p
                    D[x] = p

        def is_prime(N):
            for p in erat2():
                if N == p: return True
                elif p*p > N: return True
                elif N%p == 0: return False

or (from [http://www.noulakaz.net/weblog/2007/03/18/a-regular-expression-to-check-for-prime-numbers/](http://www.noulakaz.net/weblog/2007/03/18/a-regular-expression-to-check-for-prime-numbers/))

        import re
        def is_prime(N):
            return not re.match(r'^1?$|^(11+?)\1+$', '1' * n)

# Problem 32: Calculate the Greatest Common Divisor (GCD) using Euclid\'s algorithm 

    def gcd(a,b):
        """Return the gcd of two positive integers.

        >>> gcd(36,63)
        9
        >>> gcd(63,36)
        9
        """

        while b != 0:
            a, b = b, a%b
        return a

# Problem 33: Determine if two numbers are coprime 

Two numbers are coprime if the gcd is 1. So, using gcd() from problem 32.

    def coprime(a,b):
       """return True if 'a' and 'b' are coprime.

       >>> coprime(35,64)
       True
       """

       return gcd(a,b) == 1

# Problem 34: Calculate Euclid\'s totient function 

Use a primitive method to calculate Euclid\'s totient function.

    def phi(m):
        """calculate Euler's totient function using a primitive method.

        >>> phi(1)
        1
        >>> phi(10)
        4
        """

        if m == 1:
            return 1
        else:
            r = [n for n in range(1,m) if coprime(m,n)]
            return len(r)

# Problem 35: Determine prime factors of a number 

    import itertools

    def prime_factors(value):
        """ trial divisions are all primes because of previous reductions of value
            print list(factors(1234567890987654321))
        """
        if value > 3:
            for this in itertools.chain(iter([2]), xrange(3,int(value ** 0.5)+1, 2)):
                if this*this > value:  break
                while not (value % this):
                    if value == this: break
                    value /=  this
                    yield this
        yield value

# Problem 36: Determine prime factorization of a number 

Similar to problem P35, except the result is a list of pairs \[p,m\] where prime factor, *p*, occurs *m* times in the factorization of the number.

Uses the function prime_factors() defined in problem P35.

    def prime_factors_mult(n):
        """return list [ [p_0,k_0], [p_1,k_1], ... ], where there are 'k_i'
        occurrences of 'p_i' in the prime factorization of n.

        >>> prime_factors_mult(315)
        [[3, 2], [5, 1], [7, 1]]
        """
        res = list(prime_factors(n))
        return sorted([fact, res.count(fact)] for fact in set(res))

# Problem 37: A more efficient totient function 

See Problem 34, for a simpler implementation.

    def totient(n):
        """calculate Euler's totient function.

        If [[p_0,m_0], [p_1,m_1], ... ] is a prime factorization of 'n',
        then the totient function phi(n) is given by:

            (p_0 - 1)*p_0**(m_0-1) * (p_1 - 1)*p_1**(m_1-1) * ...

        >>> phi(1)
        1
        >>> phi(10)
        4
        """
        from operator import mult

        if n == 1: return 1

        return reduce(mult, [(p-1) * p**(m-1) for p,m in prime_factors_mult(n)])

# Problem 38: Compare totient functions 

Compare the function for calculating the totient function in problems 34 and 37.

    def P38(printtimes=True):
        """Time the execution of the totient function from P34 and P37

        For doctests, set 'printtimes=False' or the doctest will likely fail,
        because the executions time will be different.

        >>> P38(printtimes=False)
        list of functions from fastest to slowest:
           totient
               phi
        """
        from timeit import Timer

        result = {}
        for funcname in ('phi','totient'):
            stmt  = "x = %s( 10090 )" % funcname
            setup = "from __main__ import %s" % funcname

            timer = Timer( stmt=stmt, setup=setup )
            result[funcname] = timer.timeit(number=100)

        print "list of functions from fastest to slowest:"
        for funcname in sorted( result.keys(), key=lambda k:result[k] ):
            print "%10s %s" % (funcname, result[funcname] if printtimes else '')

# Problem 39: Generate a list of primes in a given range 

Uses primeGenerator() from problem 35.

    def primelist(lower=0,upper=1000):
        """return list of primes greater than 'lower' and less than
        or equal to 'upper'

        >>> primelist(10,30)
        [11, 13, 17, 19, 23, 29]
        """
        from functools import partial
        from itertools import dropwhile
        from operator import ge

        return list(dropwhile(partial(ge,lower),primeGenerator(upper)))

# Problem 40: Goldbach Conjecture 

Write a function that returns the Goldbach composition of a number.

    def goldbach(n):
        """Print goldbach composition for 'n'.

        >>> goldbach(28)
        (5, 23)
        """
        assert(n&1 == 0)
        primes = primelist(1,n)
        lo = 0
        hi = len(primes) - 1
        while lo <= hi:
            sum = primes[lo] + primes[hi]
            if sum == n:
                break
            elif sum < n:
                lo += 1
            else:
                hi -= 1
        else:
            print "Goldbach conjecture fails for", n

        return primes[lo], primes[hi]

Using only functions defined in previous problems, we could also implement this as the following:

    def goldbach (x):
        if x % 2 == 1: return None
        return next(y for y in combination(2, dupli(primes(1,x))) if sum(y) == x)

# Problem 41: Print list of Goldbach compositions 

Given a range of integers by its lower and upper limit, print a list of all even numbers and their Goldbach composition.

    def goldbach_list(lower,upper):
        """Print goldbach composition for all even numbers greater than
        'lower' and less than or equal to 'upper'.

        >>> goldbach_list(9,20)
        10 = 3 + 7
        12 = 5 + 7
        14 = 3 + 11
        16 = 3 + 13
        18 = 5 + 13
        20 = 3 + 17
        """

        # Goldbach conjecture applies to even numbers > 2
        if lower&1:
            lower += 1
        if lower < 4:
            lower = 4

        for n in range(lower,upper+1,2):
            gb = goldbach(n)
            print "%d = %d + %d" % (n, gb[0], gb[1])

Part 2: print Goldbach compositions in which both primes are greater than a threshold number.

    def goldbach_list(lower,upper,threshold=0):
        """Print goldbach composition for all even numbers greater than
        'lower' and less than or equal to 'upper'.

        >>> goldbach_list(1,2000,50)
        992 = 73 + 919
        1382 = 61 + 1321
        1856 = 67 + 1789
        1928 = 61 + 1867
        """

        for n in range(lower,upper+1,2):
            gb = goldbach(n)
            if gb[0] > threshold:
                print "%d = %d + %d" % (n, gb[0], gb[1])

# Problem 42: there is no problem 42 in the original problem set 

# Problem 43: there is no problem 43 in the original problem set 

# Problem 44: there is no problem 44 in the original problem set 

# Problem 45: there is no problem 45 in the original problem set 

# Problem 46: Print a truth table for a logical expression of two variables 

    def table(expr):
        """
        print truth table for logical expression

        >>> table('and(A,or(A,B))')
        A     B     and(A,or(A,B))
        True  True  True
        True  False True
        False True  False
        False False False
        """
        # uppercase functions to avoid name clashes with
        #   python reserved words
        def AND(a,b): return a and b
        def NAND(a,b): return not (a and b)
        def OR(a,b): return a or b
        def NOR(a,b): return not (a or b)
        def XOR(a,b): return a ^ b
        def EQU(a,b): return not (a ^ b)
        def IMP(a,b): return not a or b

        # print a nice header
        format = "%-5s %-5s %-5s"
        print  format % ('A','B',expr)

        # convert the expression to uppercase and
        # compile it for later 'eval' call
        expr = compile(expr.upper(),'<expression>','eval')

        for A in (True,False):
            for B in (True, False):

                # locals() provides the environment for
                # evaluating the compiled expr, and
                # includes A, B, and the logical functions
                # defined above (AND, NAND, ...)
                print format % (A, B, eval(expr,locals()))

# Problem 47: Print a truth table for an infix logical expression of two variables 

    def table( expr ):
        """
        P47: Print a truth table for an infix logical expression

        >>> table('A and not B')
          A     B   A and not B
        True  True  False
        True  False True
        False True  False
        False False False

        >>> table('not(A imp B)')
          A     B   not(A imp B)
        True  True  False
        True  False True
        False True  False
        False False False
        """

        # convert infix expression to prefix (function call) form
        def toPrefix( expr ):
            from re import finditer

            # Pop and operator of the operators stack and one or two operands of the
            # operand stack, and assembled into a call to the appropriate function.
            # The function call is pushed onto the operand stack
            def reduce( operators, operands ):
                op = operators.pop()
                right = operands.pop()
                if op == 'not':
                    operands.append( "%s(%s)" % ( op.upper(), right ))
                else:
                    left = operands.pop()
                    operands.append( "%s(%s,%s)" % ( op.upper(), left, right ))

            prec = { '('   : 0,                 # operator precedence
                     'imp' : 1,
                     'or'  : 2, 'nor' : 3,
                     'xor' : 3, 'equ' : 3,
                     'and' : 4, 'nand': 4,
                     'not' : 5
                     }

            # operand and operator stacks
            operands  = []
            operators = []

            # Regular expression for parsing the infix expression.  It has three
            # parenthesized groups, which are returned in a tuple by the groups()
            # method of a match object (mo).  The tuple is unpacked into
            # corresponding variables in the for-statement.
            #
            #         paren |    logical operators (curop)    |ident
            regex = r"([()])|(not|and|nand|or|nor|xor|equ|imp)|(\w+)"

            for paren,curop,ident in (mo.groups() for mo in finditer(regex,expr)):
                # identifiers (i.e., variable names) are pushed on the operand stack
                if ident is not None:
                    operands.append( ident )

                # left parens are pushed on the operator stack
                elif paren == '(':
                    operators.append( paren )

                # for a right paren, the stacks are reduced until the matching
                # left paren is encountered.  The left paren is discarded.
                elif paren == ')':
                    while operators[-1] != '(':
                        reduce( operators, operands )

                    _ = operators.pop()

                else:
                    # while the operator being parsed (curop) has a lower
                    # precedence than the one on the top of the operator stack,
                    # reduce the higher priority operator.  Then push the curop
                    # onto the operator stack
                    while operators != [] and prec[ curop ] <= prec[ operators[-1] ]:
                        reduce( operators, operands )

                    operators.append( curop )

            # after the input expression is exhausted, reduce the operands on the
            # operand stack until it is empty
            while operators != []:
                reduce( operators, operands )

            return operands.pop()

        def NOT(a): return not a
        def AND(a,b): return a and b
        def NAND(a,b): return not AND(a,b)
        def XOR(a,b): return a ^ b
        def EQU(a,b): return not XOR(a,b)
        def OR(a,b): return a or b
        def NOR(a,b): return not OR(a,b)
        def IMP(a,b): return not a or b

        stmnt = compile(toPrefix(expr),'<string>','eval')

        format = "%-5s %-5s %-5s"
        print format % ('  A  ','  B  ',expr)

        for A in (True,False):
            for B in (True,False):
                print format % (A,B,eval(stmnt,locals()))

    if __name__ == "__main__":
        import doctest
        doctest.testmod(verbose=True)

# Problem 48: Print truth table for logical infix expression having an arbitrary number of variables 

    def table(expr):
        '''
        Print a truth table for infix boolean expression with
        arbitrary number of variables.

        Implemented as an interpreter using a recursive decent parsing technique.

        Uses the tokenize module to convert expression to tokens.

        >>> table('A and (B or C) equ A and B or A and C')
        A     B     C     A and (B or C) equ A and B or A and C
        True  True  True  True
        True  True  False True
        True  False True  True
        True  False False True
        False True  True  True
        False True  False True
        False False True  True
        False False False True

        >>> table('(not A or B) equ (A imp C)')
        A     B     C     (not A or B) equ (A imp C)
        True  True  True  True
        True  True  False False
        True  False True  False
        True  False False True
        False True  True  True
        False True  False True
        False False True  True
        False False False True

        >>> table('A and B and C')
        A     B     C     A and B and C
        True  True  True  True
        True  True  False False
        True  False True  False
        True  False False False
        False True  True  False
        False True  False False
        False False True  False
        False False False False

        >>> table('not not A')
        A     not not A
        True  True
        False False
        '''
        from tokenize import generate_tokens
        from StringIO import StringIO

        def evaluate(expr):
            '''entry point for recursive decent parser/interpreter'''

            readline = StringIO(expr).readline

            # tokenize returns a tuple. element[1] is the text of the token
            # tokenize returns '' as the final token
            tokens = [t[1] for t in generate_tokens(readline)][:-1]

            return imp_expr(tokens)

        def imp_expr(tokens):
            '''imp_expr := or_expr [ 'imp' or_expr ]*'''

            value = or_expr(tokens)
            while tokens and tokens[0] == 'imp':
                _ = tokens.pop(0)
                right = or_expr(tokens)
                value = not value or right
            return value

        def or_expr(tokens):
            '''or_expr := xor_expr [ ('or'|'nor') xor_expr ]*'''

            value = xor_expr(tokens)
            while tokens and tokens[0] in ('or','nor'):
                op = tokens.pop(0)
                right = xor_expr(tokens)
                value = value or right
                if op == 'nor':
                    value = not value
            return value

        def xor_expr(tokens):
            '''xor_expr := and_expr [ ('xor'|'equ') and_expr ]*'''

            value = and_expr(tokens)
            while tokens and tokens[0] in ('xor','equ'):
                op = tokens.pop(0)
                right = and_expr(tokens)
                value = value == right
                if op == 'xor':
                    value = not value
            return value

        def and_expr(tokens):
            '''and_expr := not_expr [ ('and'|'nand') not_expr ]*'''

            value = not_expr(tokens)
            while tokens and tokens[0] in ('and','nand'):
                op = tokens.pop(0)
                right = not_expr(tokens)
                value = value and right
                if op == 'nand':
                    value = not value
            return value

        def not_expr(tokens):
            '''not_expr := [ 'not' ] atom'''
            invert = False

            while tokens and tokens[0] == 'not':
                _ = tokens.pop(0)
                invert = not invert

            value = atom(tokens)
            if invert:
                value = not value

            return value

        def atom(tokens):
            '''atom := '(' imp_expr ')'
                    |  variable
            '''

            if tokens and tokens[0] == '(':
                _ = tokens.pop(0)
                value = imp_expr(tokens)
                _ = tokens.pop(0)
            else:
                ident = tokens.pop(0)
                value = variable[ident]

            return value

        def combos(variable,varlist):
            '''generate all possible combinations of values for the
            variables in "varlist", updating the values in "variable"
            '''

            if varlist == []:
                yield []
            else:
                for variable[varlist[0]] in (True,False):
                    for rest in combos(variable,varlist[1:]):
                        yield [variable[varlist[0]]] + rest

        keywords = 'and nand xor equ or nor imp not ( )'.split()
        readline = StringIO(expr).readline

        # generate a list of variable names, by parsing 'expr' and collecting
        # text tokens that aren't keywords.  The values are kept in the dict
        # 'variable'.
        variable = {}
        for token in generate_tokens(readline):
            text = token[1]
            if text != '' and text not in keywords:
                variable[text] = text
        varlist = sorted(variable.keys())
        variable['result'] = expr

        # format has a '%(varname)-5s' field for each variable and result
        format = " ".join("%%(%s)-5s" % v for v in varlist + ["result"])

        print format % variable

        for _ in combos(variable,varlist):
            variable["result"] = evaluate(expr)
            print format % variable

    if __name__ == "__main__":
        import doctest
        doctest.testmod(verbose=True)

# Problem 49: Generate list of n-bit Gray codes. 

    def binaryString(n,w=0):
        """return binary representation of 'n' as a 'w'-width string.

        >>> binaryString(6)
        '110'
        >>> binaryString(3,4)
        '0011'
        """

        from collections import deque
        bits = deque()
        while n > 0:
            bits.appendleft(('0','1')[n&1])
            n >>= 1
        while len(bits) < w:
            bits.appendleft('0')
        return ''.join(bits)

    def gray(width):
        """return list with 'width'-bit gray code.

        >>> gray(1)
        ['0', '1']
        >>> gray(2)
        ['00', '01', '11', '10']
        >>> gray(3)
        ['000', '001', '011', '010', '110', '111', '101', '100']
        """

        return [binaryString(n ^ (n>>1),width) for n in range(2**width)]


    if __name__ == "__main__":
        import doctest
        doctest.testmod(verbose=True)

A much briefer, recursive solution (employing the mirror, concatenate, prepend \'0\' and \'1\' technique found on the [Wikipedia](http://en.wikipedia.org/wiki/Gray_code#Constructing_an_n-bit_Gray_code) page):

    def gray (n):
        if n == 0: return ['']
        return ['0'+x for x in gray(n-1)]+['1'+y for y in gray(n-1)[::-1]]

# Problem 50: Generate Huffman codes 

    def huffman(freqtable):
        """Return a dictionary mapping keys to huffman codes
        for a frequency table mapping keys to frequencies.

        >>> freqtable = dict(a=45, b=13, c=12, d=16, e=9, f=5)
        >>> sorted(huffman(freqtable).items())
        [('a', '0'), ('b', '101'), ('c', '100'), ('d', '111'), ('e', '1101'), ('f', '1100')]
        """

        from collections import defaultdict
        from heapq import heappush, heappop, heapify

        # mapping of letters to codes
        code = defaultdict(list)

        # Using a heap makes it easy to pull items with lowest frequency.
        # Items in the heap are tuples containing a list of letters and the
        # combined frequencies of the letters in the list.
        heap = [ ( freq, [ ltr ] ) for ltr,freq in freqtable.iteritems() ]
        heapify(heap)

        # Reduce the heap to a single item by combining the two items
        # with the lowest frequencies.
        while len(heap) > 1:
            freq0,letters0 = heappop(heap)
            for ltr in letters0:
                code[ltr].insert(0,'0')

            freq1,letters1 = heappop(heap)
            for ltr in letters1:
                code[ltr].insert(0,'1')

            heappush(heap, ( freq0+freq1, letters0+letters1))

        for k,v in code.iteritems():
            code[k] = ''.join(v)

        return code

    if __name__ == "__main__":
        import doctest
        doctest.testmod(verbose=True)

**Note**: problems 51-99 still to be done (PLEASE edit this place-holder as you do more problems!)
