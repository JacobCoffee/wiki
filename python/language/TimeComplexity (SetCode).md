# TimeComplexity (SetCode)

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

I don\'t know about the implementation, but as an exercise, the set union is O(N) w.r.t. len(s)+len(t), and stays the same regardless of the degree of coincidence of s and t.

Check [TimeComplexity](TimeComplexity) for more details

================

import timeit

\# Time with varying length of s and t

setup = \"\"\" from random import random s = set(random() for i in xrange(%d)) t = set(random() for i in xrange(%d)) \"\"\"

cmd = \"u = s\|t\"

for len_s in xrange(1,101,10):

- for len_t in xrange(1,101,10):
  - ans = timeit.Timer(cmd, setup=setup % (len_s, len_t)).timeit(200) print \'%3d\' % (len_s+len_t), \'%6.4f\' % (ans\*1e4/(len_s+len_t))

\# Time with varying % of elements in both sets

setup = \"\"\" from random import random n = 2000 k = int(n \* %4.3f) u = set(random() for i in xrange(k)) s = set(random() for i in xrange(n-k)) \| u t = set(random() for i in xrange(n-k)) \| u \"\"\"

cmd = \"\"\"v = s\|t\"\"\"

for i in xrange(0,101,5):

- k = 0.01\*i ans = timeit.Timer(cmd, setup=setup % k).timeit(100) print \'%3.2f\' % k, \'%6.1f\' % (ans\*1e4)
