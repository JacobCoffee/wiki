# techtonik/ideas

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

### FILE, DIR 

    inspired by: PHP __DIR__, __FILE__ [1]
    status:
      python34: __file__ is absolute [2]
      discussion: [3] (Sep13 Done), [4] (Oct13 Done)

    variants:
     - name: with import (27,33 compatible)
       set:
        - from os.path import FILE, DIR
        - from hacks import FILE, DIR
        - from future import FILE, DIR

     - name: auto global (28,35)
       set:
        - FILE, DIR
        - __file__, __dir__
        - __abs_file__, __abs_dir__ (MRAB, Philipp A.)

    cases:
     - name: replacement of frequent pattern
       code: os.path.join(os.path.dirname(__file__), "datafile-here")

1.  [http://www.php.net/manual/en/language.constants.predefined.php](http://www.php.net/manual/en/language.constants.predefined.php)

2.  [https://docs.python.org/3.5/whatsnew/3.4.html](https://docs.python.org/3.5/whatsnew/3.4.html)

3.  [https://mail.python.org/pipermail/python-ideas/2013-September/023469.html](https://mail.python.org/pipermail/python-ideas/2013-September/023469.html)

4.  [https://mail.python.org/pipermail/python-ideas/2013-October/023703.html](https://mail.python.org/pipermail/python-ideas/2013-October/023703.html)

<!-- -->

    objections:
     - new globals are bad (Cameron Simpson)
     - names starting with __ are bad (Cameron Simpson)
     - retrieving abs dir is trivial code (Cameron Simpson)
     - abspath is not always possible (Cameron Simpson)
     - there should not be convenience functions (Cameron Simpson)
     - everybody should use 35 for new ideas (Alyssa Coghlan, Terry Reedy)
     - retrieving abs dir is trivial code in 35 (Alyssa Coghlan)

    aspects:
     - __dir__ is won't work in packages (Paul Moore)
