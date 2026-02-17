# Powerful Python One-Liners

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Powerful Python One-Liners 

This page is devoted to short programs that can perform powerful operations called *Python One-Liners*.

You may ask: why should I care? The answer is profound: if you cannot read and write one-liner code snippets, how can you ever hope to read and write more complicated codebases? Python one-liners can be just as powerful as a long and tedious program written in another language designed to do the same thing. In other languages (think: Java) this would be nearly *impossible*, but in Python, it\'s a lot easier to do. The trick is to think of something that will \"do a lot with a little.\" Most importantly, reading and writing about Python one-liners (e.g., in this post) is a lot of fun! There\'s even a whole subculture around who can write the shortest code for a given problem.

It would be awesome if this page expanded to the point where it needs some sort of organization system. *(**Edit**: The one-liners are now sorted more or less by ease-of-understanding \-- from simple to hard. Please use a \"sorted insert\" for your new one-liner.)*

The source code is contributed from different Python coders \-\-- Thanks to all of them! Special thanks to the early contributor [JAM.](JAM)

Of course, there is debate on whether one-liners are even *Pythonic*. As a rule of thumb: if you use one-liners that are confusing, difficult to understand, or to show off your skills, they tend to be *Unpythonic*. However, if you use well-established one-liner tricks such as [list comprehension](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) or the [ternary operator](https://blog.finxter.com/python-one-line-ternary/), they tend to be Pythonic.

So, use your one-liner superpower wisely!

## Free Python One-Liners Learning Resources 

- [Free \'\'Python One-Liners\'\' videos & book resources](https://pythononeliners.com/)

- [Collection of \'\'One-Liners\'\' with interactive shell](https://blog.finxter.com/10-python-one-liners/)

- [Book \'\'Python One-Liners\'\'](https://www.amazon.com/gp/product/B07ZY7XMX8)

- [Interesting Quora Thread \'\'Python One-Liner\'\'](https://www.quora.com/What-are-some-of-the-most-elegant-greatest-Python-one-liners)

- [Python One-Line X](https://blog.finxter.com/python-one-line-x/) - How to accomplish different tasks in a single line

- [Subreddit \'\'\'Python One-Liners\'\'\'](https://www.reddit.com/r/PythonOneLiners/)

- [Github \'\'\'Python One-Liners\'\'\'](https://github.com/finxter/PythonOneLiners/) - Share your own one-liners with the community

## Overview: 10 one-liners that fit into a tweet 

I visited this page oftentimes and I loved studying the one-liners presented above. Thanks for creating this awesome resource, JAM, and RJW! ![:)](/wiki/europython/img/smile.png ":)")

Because I learned a lot from studying the one-liners, I thought why not revive the page (after almost ten years since the last change happened)?

After putting a lot of effort into searching the web for inspiration, I created the following ten one-liners. Some of them are more algorithmic (e.g. Quicksort). Some day, I will add a detailed explanation here - but for now, you can [read this blog article](https://blog.finxter.com/10-python-one-liners/) to find explanations.

:::: 
::: 
``` 
   1 # Palindrome Python One-Liner
   2 phrase.find(phrase[::-1])
   3 
   4 # Swap Two Variables Python One-Liner
   5 a, b = b, a
   6 
   7 # Sum Over Every Other Value Python One-Liner
   8 sum(stock_prices[::2])
   9 
  10 # Read File Python One-Liner
  11 [line.strip() for line in open(filename)]
  12 
  13 # Factorial Python One-Liner
  14 reduce(lambda x, y: x * y, range(1, n+1))
  15 
  16 # Performance Profiling Python One-Liner
  17 python -m cProfile foo.py
  18 
  19 # Power set Python One-Liner
  20 lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])
  21 
  22 # Fibonacci Python One-Liner
  23 lambda x: x if x<=1 else fib(x-1) + fib(x-2)
  24 
  25 # Quicksort Python One-liner
  26 lambda L: [] if L==[] else qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])
  27 
  28 # Sieve of Eratosthenes Python One-liner
  29 reduce( (lambda r,x: r-set(range(x**2,n,x)) if (x in r) else r), range(2,int(n**0.5)), set(range(2,n)))
```
:::
::::

## Find All Indices of an Element in a List 

Say, you want to do the same as the list.index(element) method but return all indices of the element in the list rather than only a single one.

In this one-liner, you're looking for element \'Alice\' in the list lst = \[1, 2, 3, \'Alice\', \'Alice\'\] so it even works if the element is not in the list (unlike the list.index() method).

:::: 
::: 
``` 
   1 # List
   2 lst = [1, 2, 3, 'Alice', 'Alice']
   3 
   4 # One-Liner
   5 indices = [i for i in range(len(lst)) if lst[i]=='Alice']
   6 
   7 # Result
   8 print(indices)
   9 # [3, 4]
```
:::
::::

## echo unicode character: 

:::: 
::: 
``` 
python -c "print unichr(234)"
```
:::
::::

This script echos \"ê\"

### Reimplementing cut 

Print every line from an input file but remove the first two fields.

:::: 
::: 
``` 
python -c "import sys;[sys.stdout.write(' '.join(line.split(' ')[2:])) for line in sys.stdin]" < input.txt
```
:::
::::

### Decode a base64 encoded file 

:::: 
::: 
``` 
import base64, sys; base64.decode(open(sys.argv[1], "rb"), open(sys.argv[2], "wb"))
```
:::
::::

### Editing a list of files in place 

I came up with this one-liner in response to an [article](http://linuxgazette.net/issue96/orr.html) that said it couldn\'t be done as a one-liner in Python.

What this does is replace the substring \"at\" by \"op\" on all lines of all files (in place) under the path specified (here, the current path).

- ***Caution:*** Don\'t run this on your home directory or you\'re going to get **all your text files edited**.

:::: 
::: 
``` 
import sys,os,re,fileinput;a=[i[2] for i in os.walk('.') if i[2]] [0];[sys.stdout.write(re.sub('at','op',j)) for j in fileinput.input(a,inplace=1)]
```
:::
::::

Clearer is: `import os.path; a=[f for f in os.listdir('.') if not os.path.isdir(f)]`

### Set of all subsets 

- Function that returns the set of all subsets of its argument

:::: 
::: 
``` 
f = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]
```
:::
::::

:::: 
::: 
``` 
>>>f([10,9,1,10,9,1,1,1,10,9,7])
[[], [9], [10], [9, 10], [7], [9, 7], [10, 7], [9, 10, 7], [1], [9, 1], [10, 1], [9, 10, 1], [7, 1], [9, 7, 1], [10, 7, 1], [9, 10, 7, 1]]
```
:::
::::

-RJW

Alternative (shorter, more functional version):

:::: 
::: 
``` 
f = lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])
```
:::
::::

### Terabyte to Bytes 

Want to know many bytes a terabyte is? If you know further abbreviations, you can extend the list.

:::: 
::: 
``` 
import pprint;pprint.pprint(zip(('Byte', 'KByte', 'MByte', 'GByte', 'TByte'), (1 << 10*i for i in range(5))))
```
:::
::::

### Largest 8-Bytes Number 

And what\'s the largest number that can be represented by 8 Bytes?

:::: 
::: 
``` 
print '\n'.join("%i Byte = %i Bit = largest number: %i" % (j, j*8, 256**j-1) for j in (1 << i for i in range(8)))
```
:::
::::

Cute, isn\'t it?

## Display List of all users on Unix-like systems 

:::: 
::: 
``` 
print '\n'.join(line.split(":",1)[0] for line in open("/etc/passwd"))
```
:::
::::

## CSV file to json 

:::: 
::: 
``` 
python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"
```
:::
::::

## Compress CSS file 

:::: 
::: 
``` 
python -c 'import re,sys;print re.sub("\s*([{};,:])\s*", "\\1", re.sub("/\*.*?\*/", "", re.sub("\s+", " ", sys.stdin.read())))'
```
:::
::::

## Decode string written in Hex 

:::: 
::: 
``` 
python -c "print ''.join(chr(int(''.join(i), 16)) for i in zip(*[iter('474e552773204e6f7420556e6978')]*2))"
```
:::
::::

## Retrieve content text from HTTP data 

:::: 
::: 
``` 
python -c "import sys; print sys.stdin.read().replace('\r','').split('\n\n',2)[1]";
```
:::
::::

## Broadcast magic packet to power on wakeonlan enabled computer 

Small [Wikipedia Python script](https://en.wikipedia.org/wiki/Wake-on-LAN#Creating_and_sending_the_magic_packet) squeezed out to 166 characters length one-liner:

:::: 
::: 
``` 
python -c "import socket as S;s=S.socket(S.AF_INET,S.SOCK_DGRAM);s.setsockopt(S.SOL_SOCKET,S.SO_BROADCAST,1);s.sendto(b'\xff'*6+b'\x84\x47\x09\x0b\x7f\xfd'*16,('<broadcast>',7))"
```
:::
::::

Uglier, with Python constant names replaced by their values, squeezed out to 123 characters only:

:::: 
::: 
``` 
python -c "import socket as S;s=S.socket(2,2);s.setsockopt(1,6,1);s.sendto(b'\xff'*6+b'\x84\x47\x09\x0b\x7f\xfd'*16,('<broadcast>',9))"
```
:::
::::

Replace mac address \\x84\\x47\\x09\\x0b\\x7f\\xfd with mac address of computer that should be powered on.

## Prints file extension 

:::: 
::: 
``` 
print '~/python/one-liners.py'.split('.')[-1]
```
:::
::::

## Escapes content from stdin 

This can be used to convert a string into a \"url safe\" string

:::: 
::: 
``` 
python -c "import urllib, sys ; print urllib.quote_plus(sys.stdin.read())";
```
:::
::::

## Reverse lines in stdin 

:::: 
::: 
``` 
python -c "import sys; print '\n'.join(reversed(sys.stdin.read().split('\n')))"
```
:::
::::

## Print top 10 lines of stdin 

:::: 
::: 
``` 
python -c "import sys; sys.stdout.write(''.join(sys.stdin.readlines()[:10]))" < /path/to/your/file
```
:::
::::

## Apply regular expression to lines from stdin 

:::: 
::: 
``` 
[another command] | python -c "import sys,re;[sys.stdout.write(re.sub('PATTERN', 'SUBSTITUTION', line)) for line in sys.stdin]"
```
:::
::::

## Modify lines from stdin using map 

:::: 
::: 
``` 
python -c "import sys; tmp = lambda x: sys.stdout.write(x.split()[0]+'\t'+str(int(x.split()[1])+1)+'\n'); map(tmp, sys.stdin);"
```
:::
::::

### Cramming Python into Makefiles 

A related issue is embedding Python into a Makefile. I had a really long script that I was trying to cram into a makefile so I automated the process:

:::: 
::: 
``` 
   1 import sys,re
   2 
   3 def main():
   4     fh = open(sys.argv[1],'r')
   5     lines = fh.readlines()
   6     print '\tpython2.2 -c "`printf \\"if 1:\\n\\'
   7     for line in lines:
   8         line = re.sub('[\\\'\"()]','\\\g<0>',line)
   9         # grab leading white space (should be multiples of 4) and makes them into
  10         # tabs
  11         wh_spc_len = len(re.match('\s*',line).group())
  12 
  13         sys.stdout.write('\t')
  14         sys.stdout.write(wh_spc_len/4*'\\t'+line.rstrip().lstrip())
  15         sys.stdout.write('\\n\\\n')
  16     print '\t\\"`"'
  17 
  18 if __name__=='__main__':
  19     main()
```
:::
::::

This script generates a \"one-liner\" from make\'s point of view.

## Sony\'s Open Source command-line tool for performing python one-liners using unix-like pipes 

They call it \"The Pyed Piper\" or pyp. It\'s pretty similar to the -c way of executing python, but it imports common modules and has its own preset variable that help with splitting/joining, line counter, etc. You use pipes to pass information forward instead of nested parentheses, and then use your normal python string and list methods. Here is an example from the homepage:

Here, we take a Linux long listing, capture every other of the 5th through the 10th lines, keep the username and filename fields, replace \"hello\" with \"goodbye\", capitalize the first letter of every word, and then add the text \"is splendid\" to the end:

:::: 
::: 
``` 
ls -l | pyp "pp[5:11:2] | whitespace[2], w[-1] | p.replace('hello','goodbye') | p.title(),'is splendid'"
```
:::
::::

and the explanation:

This uses pyp\'s built-in string and list variables (p and pp), as well as the variable whitespace and its shortcut w, which both represent a list based on splitting each line on whitespace (whitespace = w = p.split()). The other functions and selection techniques are all standard Python. Notice the pipes (\"\|\") are inside the pyp command.

[http://code.google.com/p/pyp/](http://code.google.com/p/pyp/) [http://opensource.imageworks.com/?p=pyp](http://opensource.imageworks.com/?p=pyp)

## Contributed Code 

- [JAM/Code/PlatformFinder](./JAM(2f)Code(2f)PlatformFinder.html) - This program tells you what platform you are using.

- [JAM/Code/ComPYiler](./JAM(2f)Code(2f)ComPYiler.html) - This program compiles every .py file in the Python directory.

- [Powerful Python One-Liners/Hostname](./Powerful(20)Python(20)One(2d)Liners(2f)Hostname.html) - This program tells you what your hostname is.
