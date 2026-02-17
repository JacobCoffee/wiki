# RangeGenerator

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Below is a little range generator, irange, which is compatible with range. More specifically, `[i for i in irange(*args)] == range(*args)]`. This will let us iterator over large spans of numbers without resorting to [xrange](./xrange.html), which is a lazy list as opposed to a generator.

Would a function of similar semantics likely be accepted into the standard library within itertools?

[lwickjr](lwickjr): I like the idea. Anyone else?

The author doesn\'t have the time/energy to write/push a [PEP](PEP) for the [PythonEnhancementProcess](./PythonEnhancementProcess.html). If you think this generator is a good idea, please submit a [PEP](PEP).

[lwickjr](lwickjr): Neither do I. Anyone else?

# Test Suite 

Here is the test:

    import unittest

    from iter import irange
    class TestIter(unittest.TestCase):
        def testIrangeValues(self):
            testArguments = ( [10],[0],[7,70], [-10], [10,700,17], [10,1000,-3],[10,-99,-7] )
            l = lambda *x: list(irange(*x))

            for args  in testArguments:
                list1 = l(*args)
                list2 = range(*args)
                self.assertEqual(list1,list2)

        def testIrangeArguments(self):
             self.assertRaises(ValueError,irange,0,99,0) #0 step
            #self.assertRaises(irange(1,2,3,4)) #too many arguments



    if __name__ == '__main__':
        unittest.main()

# implementation

    """generator for a range of integers that matches the output
    of an iterator over the list range(...)

    """

    from itertools import count,takewhile
    """private generator over the unchecked arguments start, stop, step
       [i for i in __irange3(start,stop,step)] produces range(start,stop,step)
    """
    def __irange3__(start,stop,step):
        #the stop condition changes depending on the sign of step
        predicate = step > 0 and (lambda x : x < stop) or (lambda x : x > stop)
        i = start
        while predicate(i):
            yield i
            i += step

    """ generator to produce the same output as an iterator over
    range(args).  The advantage of this over range() or xrange() is a list
    is not created in order to provide the generator.
    [i for i in irange(args) ] == [range(args)]
    """
    def irange(*args):
        if len(args) not in (1,2,3):
            raise TypeError, "expected 1,2, or 3 arguments to irange"

        #the stop value will be the 1st argument when 1 argument supplied, it
        #will the the second argument otherwise. The index is one less than the
        #argument
        stop = args[(1,0)[len(args) == 1]]
        if len(args) == 3:
            step = args[2]
            #we check the step before we create the generator, for earlier
            #error annunciation.
            if step == 0:
                raise ValueError()
            return __irange3__(args[0],stop,step)

        #for the cases with no step (1 or two args) its easy to
        #use the built in count() generator and filter
        predicate = lambda x : x < stop
        #set up the arguments to count, depending on whether we have a start
        counter_args = len(args) != 1 and [args[0]] or ()
        counter = count(*counter_args)
        return takewhile(predicate, counter)

# Alternate Implementation 

Perhaps a simple implementation can be constructed using \*count\* and \*islice\* from intertools?. \-- Anon

I think it\'s way too much code, and also it does not accept named parameters. How about this? \-- [JürgenHermann](./J(c3bc)rgenHermann.html) 2005-10-19 20:06:52

- def irange(start, stop=None, step=1):
          """ Generator for a list containing an arithmetic progression of integers.
              range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
              When step is given, it specifies the increment (or decrement).
              For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
              These are exactly the valid indices for a list of 4 elements.
          """
          if step == 0:
              raise ValueError("irange() step argument must not be zero")

          if stop is None:
              stop = start
              start = 0
          continue_cmp = (step < 0) * 2 - 1

          while cmp(start, stop) == continue_cmp:
              yield start
              start += step

      if __name__ == "__main__":
          cases = [
              (0,),
              (1,),
              (2,),

              (1, 0),
              (1, 1),
              (1, 2),
              (1, 4),

              (1, 4, 1),
              (1, 4, 2),
              (1, 4, 3),
              (1, 4, -1),
              (1, 4, -2),
              (1, 4, -3),

              (4, 1, 1),
              (4, 1, 2),
              (4, 1, 3),
              (4, 1, -1),
              (4, 1, -2),
              (4, 1, -3),
          ]
          for case in cases:
              assert range(*case) == [i for i in irange(*case)]

          print "All %d tests passed!" % len(cases)

*The alternate implementation is fine, though I\'d prefer to see a \"takewhile\" rather than a while loop in the spirit of functional programming - but thats minor.*

The test case I am less fond of - while it does test the functionality, it doesn\'t support [TestDrivenDevelopment](TestDrivenDevelopment) as well. It would be nice to have a test from unitest to allow someone building a big system to easily run a suite of tests they like.

Next step write a PEP someone?
