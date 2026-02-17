# SteveHowell

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Hi, my name is Steve Howell, and I have been programming in Python more or less full time since 2001.

In 2010 I attempted to submit a patch to CPython shown here: [ProposalToSpeedUpListOperations](ProposalToSpeedUpListOperations)

I mainly use Python at work now, but I have also contributed to open source projects. Here are some things that I\'ve done in the Open Source world:

- [http://gvr.sourceforge.net/](http://gvr.sourceforge.net/) (Guido van Robot learning IDE)

  the initial version of [LocalSiteMap](./LocalSiteMap.html) feature in [MoinMoin](MoinMoin)

Here is an early version of the code on the [SimplePrograms](SimplePrograms) page. I wrote most of the initial code, with helpful edits from other folks.

I am keeping it here for posterity. The code below is free for use under the Python license. I encourage you to try building up your own suite of examples.

One thing unique about the format below is that each program gets one line longer than the previous.

All of this code has been tested on 2.4 or 2.5.

        ------ 1 Output
        print 'hello world'

        ------ 2 Looping
        for name in ['peter', 'paul', 'mary']:
            print name

        ------ 3 Input, comments
        # This is a Python comment. \n is a newline
        name = raw_input('What is your name?\n')
        print 'Hi', name

        ------ 4 Fibonacci, tuple assignment
        parent_rabbits, baby_rabbits = (1, 1)
        while baby_rabbits < 100:
            print 'This generation has %d rabbits' % baby_rabbits
            parent_rabbits, baby_rabbits = (baby_rabbits, parent_rabbits + baby_rabbits)

        ------ 5 Functions
        def greet(name):
            print 'hello', name
        greet('Jack')
        greet('Jill')
        greet('Bob')

        ------ 6 Import, regular expresssions
        import re
        for test_string in [ '555-1212', 'ILL-EGAL']:
            if re.match('\d\d\d-\d\d\d\d$', test_string):
                print test_string, 'is a valid US local phone number'
            else:
                print test_string, 'rejected'

        ------ 7 Dictionaries, generator expressions
        prices = {'apple': 0.40, 'banana': 0.50}
        my_purchase = {
            'apple': 1,
            'banana': 6}
        grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                           for fruit in my_purchase)
        print 'I owe the grocer $%.2f' % grocery_bill


        ------ 8 Command line arguments, exception handling
        #!/usr/local/bin/python
        # This program adds up integers in the command line
        import sys
        try:
            total = sum(int(arg) for arg in sys.argv[1:])
            print 'sum =', total
        except ValueError:
            print 'Please supply integer arguments'


        ------ 9 Opening files
        # indent your Python code to put into an email
        import glob
        # glob supports Unix style pathname extensions
        python_files = glob.glob('*.py')
        for fn in sorted(python_files):
            print '    ------'
            for line in open(fn):
                print '    ' + line.rstrip()
            print

        ------ 10 Time, conditionals
        import time
        now = time.localtime()
        hour = now.tm_hour
        if hour < 8: print 'sleeping'
        elif hour < 9: print 'commuting'
        elif hour < 17: print 'working'
        elif hour < 18: print 'commuting'
        elif hour < 20: print 'eating'
        elif hour < 22: print 'resting'
        else: print 'sleeping'

        ------ 11 Triple-quoted strings, while loop
        REFRAIN = '''
        %d bottles of beer on the wall,
        %d bottles of beer,
        take one down, pass it around,
        %d bottles of beer on the wall!
        '''
        bottles_of_beer = 99
        while bottles_of_beer > 1:
            print REFRAIN % (bottles_of_beer, bottles_of_beer,
                bottles_of_beer - 1)
            bottles_of_beer -= 1

        ------ 12 List slicing
        def sieve_of_eratosthenes(candidates):
            i = 0
            while True:
                divisor = candidates[i]
                if divisor * divisor > candidates[-1]:
                    return candidates
                else:
                    i += 1
                candidates = candidates[:i] + \
                    [num for num in candidates[i:]
                        if num % divisor != 0]
        print sieve_of_eratosthenes(range(2,100))

        ------ 13 Unit testing
        # Let's write reusable code, and unit test it.
        def add_money(amounts):
            # do arithmetic in pennies so as not to accumulate float errors
            pennies = sum([round(int(amount * 100)) for amount in amounts])
            return float(pennies / 100.0)
        if __name__ == '__main__':
            import unittest
            class TestAddMoney(unittest.TestCase):
                def test_float_errors(self):
                    self.failUnlessEqual(add_money([0.13, 0.02]), 0.15)
                    self.failUnlessEqual(add_money([100.01, 99.99]), 200)
                    self.failUnlessEqual(add_money([0, -13.00, 13.00]), 0)
            unittest.main()

        ------ 14 Classes
        class BankAccount:
            def __init__(self, initial_balance = 0):
                self.balance = initial_balance
            def deposit(self, amount):
                self.balance += amount
            def withdraw(self, amount):
                self.balance -= amount
            def overdrawn(self):
                return self.balance < 0
        my_account = BankAccount()
        my_account.deposit(15)
        my_account.withdraw(5)
        print my_account.balance
        print my_account.overdrawn()

        ------ 15 itertools
        import itertools
        lines = '''
        This is the
        first paragraph.

        This is the second.
        '''.splitlines()
        # Use itertools.groupby and bool to return groups of
        # consecutive lines that either have content or don't.
        for has_chars, frags in itertools.groupby(lines, bool):
            if has_chars:
                print ' '.join(frags)
        # PRINTS:
        # This is the first paragraph.
        # This is the second.

------------------------------------------------------------------------

[CategoryHomepage](CategoryHomepage)
