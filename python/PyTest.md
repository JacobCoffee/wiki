# pytest

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

**pytest**, aka *we-don\'t-need-no-stinking-API unit test suite*, is an alternative, more pythonic way of writing your tests. The best part is, the overhead for creating unit tests is close to zero!

For example, assume you have a prime generator in module `prime.py`{.backtick}, and you\'d want to write a simple test for it (if you don\'t know it, a prime is a non-negative integer being divisible only by 1 and itself, and the first prime is 2). Now, you should know that it would be probably wise to start writing test suite before you actually write any code for prime generator itself, because it makes the whole process of software development less error prone as well as less ad-hoc, but I digress. Let\'s get on with the test:

:::: 
::: 
``` 
   1 from prime import PrimeGenerator
   2 
   3 def test_first_primes():
   4     pg = PrimeGenerator()
   5 
   6     assert pg.first_primes(6) == [2, 3, 5, 7, 11, 13]
```
:::
::::

That\'s it - you have a working, albeit far from complete, test suite you can run by giving the test file as argument for pytest. If you saved above snippet to file `test_primegen.py`{.backtick}, you could run the tests by simply saying

`pytest test_primegen.py`{.backtick}

However, let us assume you\'d like to extend the test suite a bit further - add a second test for testing primality using instance method `isprime()`{.backtick}:

:::: 
::: 
``` 
   1 from prime import PrimeGenerator
   2 
   3 def test_first_primes():
   4     pg = PrimeGenerator()
   5 
   6     assert pg.first_primes(6) == [2, 3, 5, 7, 11, 13]
   7 
   8 def test_primality():
   9     pg = PrimeGenerator()
  10     
  11     known_primes = (17, 19, 23, 29, 31)
  12     known_nonprimes = (21, 27, 33, 49)
  13     
  14     for p in known_primes:
  15         assert pg.isprime(p)
  16     for np in known_nonprimes:
  17         assert not pg.isprime(np)
```
:::
::::

It is nice and everything, but now there are two issues. First, if you have many tests, it is bothersome to write `pg = PrimeGenerator()`{.backtick} in every method - ok, not that bothersome, but in programming, being lazy in particular way is not only elegant, but saves your from errors and other problems in the future, trust me.

The other issue is that if your method `isprime()`{.backtick} is not working correctly, you do see the error, but you don\'t see *what* number triggered the error. Let\'s fix these two problems at next attempt.

:::: 
::: 
``` 
   1 from prime import PrimeGenerator
   2 
   3 class TestPrime:
   4 
   5     def setup_class(self):
   6         self.pg = PrimeGenerator()        
   7 
   8     def test_first_primes(self):
   9         # come to think of it, wrap left side inside list() so that
  10         # generator methods work as well
  11         assert list(self.pg.first_primes(start=5, 4)) == [5, 7, 11, 13]
  12 
  13     def _isprime(self, n, expected):
  14         assert self.pg.isprime(n) == expected
  15 
  16     def test_isprime(self):
  17         known_primes = (17, 19, 23, 29, 31)
  18         known_nonprimes = (21, 27, 33, 49)
  19 
  20         for p in known_primes:
  21             yield self._isprime, p, True
  22 
  23         for np in known_nonprimes:
  24             yield self._isprime, np, False            
```
:::
::::

What happen, you say? Jokes aside, you should notice that first off, you no longer need to setup prime generator instance in every method - `setup_class()`{.backtick} takes care of instantiating needed object. Secondly, `test_isprime()`{.backtick} looks now a tad more exotic - it uses generator expression `yield`{.backtick} for generating tests on the fly. Now if your prime generator fails, you see the exact error - ie. what argument failed to give the correct, expected result.

Oh, one little confession: I did a bit more in addition to those two changes above. For testing statements which return lists, it might be advisable to add extra `list()`{.backtick} around the statement. Then your test suite works both for list returning methods as well as those using generator expressions. Or you can circumvent the problem by using method generators - as shown in the second test method. I also added a new (keyword?) parameter `start`{.backtick} to `first_primes()`{.backtick} - thus specifying where the prime sequence should start, duh. Hmm\... perhaps `stop`{.backtick} could be specified as well, specifying the range to search primes from? Or should we introduce a whole different method for that kind of thing?

These are decisions you *have to* make, and perhaps you already realized one very nice aspect of [TestDrivenDevelopment](TestDrivenDevelopment) (TDD); if you write your tests before the code, you really have to think of your [API](API) quite thoroughly, which is a good thing. Just imagine fiddling with a method for days, debugging it, optimizing, documenting.. only to realise later you don\'t need the method at all! So, write tests first, if only to get your API right the first time.

You may now wonder - please do! - how pytest knows which methods to run. Well, there *has* to be some magic going on behind the scenes, because you don\'t see any `testsuite.run(method)`{.backtick} or `testsuite.add(class_instance)`{.backtick} etc. Well, you\'re right. There *is* some serious magic going on and here there be dragons, but the programmer API is very simple. It\'s all transparent.

That is, every class starting with *Test* and every method starting with *test\_* is treated specially and considered to be part of unit test suite. Also, assert is *very* magic, but you don\'t need to know that\... just use it as you are, well, used to ![:-)](/wiki/europython/img/smile.png ":-)") Things are that way just to give you cleaner, more informative tracebacks, and more fulfilling and rewarding unit-testing experience.

There are so many oh-so-nice features in pytest, making it quite cute tool to work with. Here I will only list some of them:

- tests are run in the order you specify them, making tests both deterministic and predictable
- you can ask pytest to abort on first error encountered using -x option
- running tests will start immediately upon collecting them
- you can start pytest in daemon mode, which will then constantly monitor your modules for changes and running tests automatically when needed

So, if you consider giving [TestDrivenDevelopment](TestDrivenDevelopment) a try, please try pytest at least. It makes writing unit tests much more **fun** ![:-)](/wiki/europython/img/smile.png ":-)")

More information:

- [pytest on PyPI](https://pypi.org/project/pytest/)

- [getting-started](https://docs.pytest.org/en/latest/getting-started.html#getstarted)

------------------------------------------------------------------------

Still more information (quite old though):

- [http://blog.ianbicking.org/pytest.html](http://blog.ianbicking.org/pytest.html)

- [http://ianbicking.org/docs/pytest-presentation/pytest-slides.html](http://ianbicking.org/docs/pytest-presentation/pytest-slides.html)

- [http://agiletesting.blogspot.com/2005/01/python-unit-testing-part-3-pytest-tool.html](http://agiletesting.blogspot.com/2005/01/python-unit-testing-part-3-pytest-tool.html)

------------------------------------------------------------------------

[UnitTests](UnitTests)
