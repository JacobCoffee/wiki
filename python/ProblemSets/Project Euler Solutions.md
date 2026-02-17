# ProblemSets/Project Euler Solutions

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Python Solutions to [Project Euler](http://projecteuler.net/index.php?section=problems).

**Index**

# Solutions to the first 40 problems in functional Python 

Just found this site which is apparently devoted to solutions for the Euler problem set, in python, with a functional flavor.

[http://pyeuler.wikidot.com/](http://pyeuler.wikidot.com/)

# Problem 1: Add all the natural numbers below 1000 that are multiples of 3 or 5. 

[http://projecteuler.net/index.php?section=problems&id=1](http://projecteuler.net/index.php?section=problems&id=1)

        def multiples_of_3_or_5():
            for number in xrange(1000):
                if not number % 3 or not number % 5:
                    yield number

        print sum(multiples_of_3_or_5())

In one line:

        print sum( number for number in xrange(1000) if not (number % 3 and number % 5) )

# Problem 2: Find the sum of all the even-valued terms in the Fibonacci sequence which do not exceed one million. 

[http://projecteuler.net/index.php?section=problems&id=2](http://projecteuler.net/index.php?section=problems&id=2)

        def fib():
            x,y = 0,1
            while True:
                yield x
                x,y = y, x+y

        def even(seq):
            for number in seq:
                if not number % 2:
                    yield number

        def under_a_million(seq):
            for number in seq:
                if number > 1000000:
                    break
                yield number   

        print sum(even(under_a_million(fib())))

Alternately:

        import itertools

        def fib():
            x,y = 0,1
            while True:
                yield x
                x,y = y, x+y

        print sum(x for x in itertools.takewhile(lambda x: x <= 1000000, fib()) if x % 2 == 0)

# Problem 3: Find the largest prime factor of 317584931803. 

[http://projecteuler.net/index.php?section=problems&id=3](http://projecteuler.net/index.php?section=problems&id=3)

        plist = [2]

        def primes(min, max):
            if 2 >= min: yield 2
            for i in range(3, max, 2):
                for p in plist:
                    if i%p == 0 or p*p > i: break
                if i%p:
                    plist.append(i)
                    if i >= min: yield i
            
        def factors(number):
            for prime in primes(2, number):
                if number % prime == 0:
                    number /= prime
                    yield prime
                if number == 1:
                    break

        print max(factors(317584931803))
