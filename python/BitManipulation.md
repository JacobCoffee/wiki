# BitManipulation

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

Here is some information and goals related to Python bit manipulation, binary manipulation.

Some tasks include:

- Turn \"11011000111101\...\" into bytes, (padded left or right, 0 or 1,) and vice versa.
- Slice ranges of bits
- Rotate bits, addressed by the bit. That is, say: \"rotate bits 13-17, wrapping around the edges,\" or, \"rotate bits 13-17, lose bits on the one side, set all new bits to 0.\"
- Similarly, revert regions of bits, apply logic to regions of bits, etc.,.
- Switch Endianness, with different block sizes.
- Apply operations in block groupings: ex: apply XOR 10101 (5 bits) repeatedly across a field.

Relevant libraries include:

- [ctypes --- A foreign function library for Python --- Python Documentation](https://docs.python.org/library/ctypes.html) - part of the standard library

- [bitarray - efficient arrays of booleans \-- C extension](https://pypi.python.org/pypi/bitarray/)

- [python-bitstring - A Python module to help you manage your bits. - Google Project Hosting](https://code.google.com/p/python-bitstring/)

- [bitstruct - This module performs conversions between Python values and C bit field structs represented as Python bytearrays.](https://pypi.python.org/pypi/bitstruct/)

Some simple code is at [ActiveState Code Recipes: Bit-field manipulation](https://code.activestate.com/recipes/113799-bit-field-manipulation/) (in Python 2 syntax).

Here are some other examples.

## Manipulations 

To integer.

:::: 
::: 
``` 
   1 >>> print(int('00100001', 2))
   2 33
```
:::
::::

To hex string. Note that you don\'t need to use x8 bits.

:::: 
::: 
``` 
   1 >>> print("0x%x" % int('11111111', 2))
   2 0xff
   3 >>> print("0x%x" % int('0110110110', 2))
   4 0x1b6
   5 >>> print("0x%x" % int('0010101110101100111010101101010111110101010101', 2))
   6 0xaeb3ab57d55
```
:::
::::

To character. 8 bits max.

:::: 
::: 
``` 
   1 >>> chr(int('111011', 2))
   2 ';'
   3 >>> chr(int('1110110', 2))
   4 'v'
   5 >>> chr(int('11101101', 2))
   6 '\xed'
```
:::
::::

Characters to integers, but not to strings of 1\'s and 0\'s.

:::: 
::: 
``` 
   1 >>> int('01110101', 2)
   2 117
   3 >>> chr(int('01110101', 2))
   4 'u'
   5 >>> ord('u')
   6 117
```
:::
::::

Individual bits.

:::: 
::: 
``` 
   1 >>> 1 << 0
   2 1
   3 >>> 1 << 1
   4 2
   5 >>> 1 << 2
   6 4
   7 >>> 1 << 3
   8 8
   9 >>> 1 << 4
  10 16
  11 >>> 1 << 5
  12 32
  13 >>> 1 << 6
  14 64
  15 >>> 1 << 7
  16 128
```
:::
::::

## Transformations Summary 

Strings to Integers:

- `"1011101101"`: `int(str, 2)`

- `"m"`: `ord(str)`

- `"0xdecafbad"`: `int(str, 16)` (known to work in Python 2.4)

- `"decafbad"`: `int(str, 16)` (known to work in Python 2.4)

Integers to Strings:

- `"1011101101"`: built-in to Python 3 (see below)

- `"m"`: `chr(str)`

- `"0xdecafbad"`: `hex(val)`

- `"decafbad"`: `"%x" % val`

We are still left without a technique for producing binary strings, and decyphering hex strings.

## Hex String to Integer 

Use the int type with the base argument:

:::: 
::: 
``` 
   1 >>> int('0xff',16)
   2 255
   3 >>> int('d484fa894e',16)
   4 912764078414
```
:::
::::

Do not use alternatives that utilize eval. eval will execute code passed to it and can thus compromise the security of your program.

## Integer to Bin String 

Python 3 supports binary literals (e.g. 0b10011000) and has a bin() function. For older versions:

:::: 
::: 
``` 
   1 >>> def bin(a):
   2         s=''
   3         t={'0':'000','1':'001','2':'010','3':'011',
   4            '4':'100','5':'101','6':'110','7':'111'}
   5         for c in oct(a)[1:]:
   6                 s+=t[c]
   7         return s
```
:::
::::

or better:

:::: 
::: 
``` 
   1 def bin(s):
   2     return str(s) if s<=1 else bin(s>>1) + str(s&1)
```
:::
::::

## Python Integers 

From \"The Python Language Reference\" page on the Data Model:

\"Integers (int) These represent numbers in an unlimited range, subject to available (virtual) memory only. For the purpose of shift and mask operations, a binary representation is assumed, and negative numbers are represented in a variant of 2's complement which gives the illusion of an infinite string of sign bits extending to the left.\"

Prior to Python 3.1, there was no easy way to determine how Python represented a specific integer internally, i.e. how many bits were used. Python 3.1 adds a bit_length() method to the int type that does exactly that.

Unless you know you are working with numbers that are less than a certain length, for instance numbers from arrays of integers, shifts, rotations, etc. may give unexpected results.

The number of the highest bit set is the highest power of 2 less than or equal to the input integer. This is the same as the exponent of the floating point representation of the integer, and is also called its \"integer log base 2\".(ref.1)

In versions before 3.1, the easiest way to determine the highest bit set is\*:

\* There is a long discussion on this topic, and why this method is not good, in \"Issue 3439\" at Python.org: [http://bugs.python.org/issue3439](http://bugs.python.org/issue3439) This discussion led up to the addition of bit_length() in Python 3.1.

:::: 
::: 
``` 
   1 import math
   2 
   3 hiBit = math.floor(math.log(int_type, 2))
```
:::
::::

An input less than or equal to 0 results in a \"[ValueError](./ValueError.html): math domain error\"

The section \"Finding integer log base 2 of an integer\" on the \"Bit Twiddling Hacks\"(ref.1) web page includes a number of methods for determining this value for integers of known magnitude, presumably when no math coprocessor is available. The only method generally applicable to Python integers of unknown magnitude is the \"obvious way\" of counting the number of bitwise shift operations needed to reduce the input to 0.

### Bit Length Of a Python Integer 

bitLen() counts the actual bit length of a Python integer, that is, the number of the highest non-zero bit *plus 1*. Zero, with no non-zero bit, returns 0. As should be expected from the quote above about \"the illusion of an infinite string of sign bits extending to the left,\" a negative number throws the computer into an infinite loop.

The function can return any result up to the length of the largest integer your computer\'s memory can hold.

:::: 
::: 
``` 
   1 def bitLen(int_type):
   2     length = 0
   3     while (int_type):
   4         int_type >>= 1
   5         length += 1
   6     return(length)
   7 
   8 for i in range(17):
   9      print(bitLen(i))
  10 
  11 # results: 0, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5
```
:::
::::

The method using the math module is much faster, especially on huge numbers with hundreds of decimal digits.

### bitLenCount() 

In common usage, the \"bit count\" of an integer is the number of set (1) bits, not the bit length of the integer described above. bitLen() can be modified to also provide the count of the number of set bits in the integer. There are faster methods to get the count below.

:::: 
::: 
``` 
   1 def bitLenCount(int_type):
   2     length = 0
   3     count = 0
   4     while (int_type):
   5         count += (int_type & 1)
   6         length += 1
   7         int_type >>= 1
   8     return(length, count)
```
:::
::::

## Operations on Integers of Unknown Magnitude 

Some procedures don\'t need to know the magnitude of an integer to give meaningful results.

### bitCount() 

The procedure and the information below were found in \"Bit Twiddling Hacks\"(ref.1)

- \- - - - - - - - - - - - - - - - - - - - - - - -

Counting bits set, Brian Kernighan\'s way\*

:::: 
::: 
``` 
   1 unsigned int v;          // count the number of bits set in v
   2 unsigned int c;          // c accumulates the total bits set in v
   3 for (c = 0; v; c++)
   4 {   v &= v - 1;  }       //clear the least significant bit set
```
:::
::::

This method goes through as many iterations as there are set bits. So if we have a 32-bit word with only the high bit set, then it will only go once through the loop.

\* The C Programming Language 2nd Ed., Kernighan & Ritchie, 1988.

Don Knuth pointed out that this method was published by Peter Wegner in CACM 3 (1960), 322. Also discovered independently by Derrick Lehmer and published in 1964 in a book edited by Beckenbach.

- \- - - - - - - - - - - - - - - - - - - - - - - -

Kernighan and Knuth, potent endorsements!

This works because each subtraction \"borrows\" from the lowest 1-bit. For example:

:::: 
::: 
``` 
   1 #       loop pass 1                 loop pass 2
   2 #      101000     101000           100000     100000
   3 #    -   #!python
   4   & 100111         -   #!python
   5   & 011111
   6 #    = 100111   = 100000         = 011111   =      0
```
:::
::::

It is an excellent technique for Python, since the size of the integer need not be determined beforehand.

:::: 
::: 
``` 
   1 def bitCount(int_type):
   2     count = 0
   3     while(int_type):
   4         int_type &= int_type - 1
   5         count += 1
   6     return(count)
```
:::
::::

### parityOf() 

From \"Bit Twiddling Hacks\"

Code almost identical to bitCount(), above, calculates the parity of an integer, returning 0 if there are an even number of set bits, and -1 if there are an odd number. In fact, counting the bits and checking whether the result is odd with **bitcount & 1** is about the same speed as the parity function.

:::: 
::: 
``` 
   1 def parityOf(int_type):
   2     parity = 0
   3     while (int_type):
   4         parity = ~parity
   5         int_type = int_type & (int_type - 1)
   6     return(parity)
```
:::
::::

### lowestSet() 

To determine the bit number of the *lowest* bit set in an integer, in twos-complement notation **i & -i** zeroes all but the lowest set bit. The bitLen() proceedure then determines its position. Obviously, negative numbers return the same result as their opposite. In this version, an input of 0 returns -1, in effect an error condition.

:::: 
::: 
``` 
   1 For example:
   2 #    00111000     # 56
   3 #    11001000     # twos complement, -56
   4 # &= 00001000
```
:::
::::

:::: 
::: 
``` 
   1 def lowestSet(int_type):
   2     low = (int_type & -int_type)
   3     lowBit = -1
   4     while (low):
   5         low >>= 1
   6         lowBit += 1
   7     return(lowBit)
```
:::
::::

### Single bits 

The usual single-bit operations will work on any Python integer. It is up to the programmer to be sure that the value of \'offset\' makes sense in the context of the program.

:::: 
::: 
``` 
   1 # testBit() returns a nonzero result, 2**offset, if the bit at 'offset' is one.
   2 
   3 def testBit(int_type, offset):
   4     mask = 1 << offset
   5     return(int_type & mask)
   6 
   7 # setBit() returns an integer with the bit at 'offset' set to 1.
   8 
   9 def setBit(int_type, offset):
  10     mask = 1 << offset
  11     return(int_type | mask)
  12 
  13 # clearBit() returns an integer with the bit at 'offset' cleared.
  14 
  15 def clearBit(int_type, offset):
  16     mask = ~(1 << offset)
  17     return(int_type & mask)
  18 
  19 # toggleBit() returns an integer with the bit at 'offset' inverted, 0 -> 1 and 1 -> 0.
  20 
  21 def toggleBit(int_type, offset):
  22     mask = 1 << offset
  23     return(int_type ^ mask)
```
:::
::::

## Bit fields, e.g. for communication protocols 

If you need to interpret individual bits in some data, e.g. a byte stream in a communications protocol, you can use the ctypes module.

:::: 
::: 
``` 
   1 import ctypes
   2 c_uint8 = ctypes.c_uint8
   3 
   4 class Flags_bits( ctypes.LittleEndianStructure ):
   5     _fields_ = [
   6                 ("logout",     c_uint8, 1 ),  # asByte & 1
   7                 ("userswitch", c_uint8, 1 ),  # asByte & 2
   8                 ("suspend",    c_uint8, 1 ),  # asByte & 4
   9                 ("idle",       c_uint8, 1 ),  # asByte & 8
  10                ]
  11 
  12 class Flags( ctypes.Union ):
  13     _anonymous_ = ("bit",)
  14     _fields_ = [
  15                 ("bit",    Flags_bits ),
  16                 ("asByte", c_uint8    )
  17                ]
  18 
  19 flags = Flags()
  20 flags.asByte = 0x2  # ->0010
  21 
  22 print( "logout: %i"      % flags.bit.logout   )
  23 # `bit` is defined as anonymous field, so its fields can also be accessed directly:
  24 print( "logout: %i"      % flags.logout     )
  25 print( "userswitch:  %i" % flags.userswitch )
  26 print( "suspend   :  %i" % flags.suspend    )
  27 print( "idle  : %i"      % flags.idle       )
```
:::
::::

:::: 
::: 
``` 
   1 >>> 
   2 logout: 0
   3 logout: 0
   4 userswitch:  1
   5 suspend   :  0
   6 idle  : 0
```
:::
::::

## References 

ref.1. \"Bit Twiddling Hacks\" By Sean Eron Anderson

- [http://graphics.stanford.edu/\~seander/bithacks.html](http://graphics.stanford.edu/~seander/bithacks.html)

ref.2. \"The Art of Assembly Language\" by Randall Hyde

- [http://webster.cs.ucr.edu/AoA/index.html](http://webster.cs.ucr.edu/AoA/index.html) Volume 4, Chapter 5 \"Bit Manipulation\"

ref.3. Hacker\'s Delight

- [http://www.hackersdelight.org/](http://www.hackersdelight.org/)

## Research Links 

this is the sort of thing we\'re looking for:

- [https://code.activestate.com/recipes/113799-bit-field-manipulation/](https://code.activestate.com/recipes/113799-bit-field-manipulation/) (in Python 2 syntax).

related modules:

- [array module](http://www.python.org/doc/current/lib/module-array.html) \-- (issued with Python)

- [struct module](http://www.python.org/doc/current/lib/module-struct.html) \-- (issued with Python)

- [binascii module](http://www.python.org/doc/current/lib/module-binascii.html) \-- (issued with Python)

- [pySerial module](http://pyserial.sourceforge.net/) \-- access the serial port

see also: [BitwiseOperators](BitwiseOperators)
